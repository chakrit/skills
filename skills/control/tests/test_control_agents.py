"""Command-loop dispatch checks use isolated panes, never a user's agent sessions."""

import concurrent.futures
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from config_fixture import AGENT, PRINCIPAL, config_text, write_control


FAKE_TMUX = '''#!/usr/bin/env python3
import json, os, pathlib, sys
root = pathlib.Path(os.environ["FAKE_TMUX_ROOT"])
state = json.loads((root / "state.json").read_text())
args = sys.argv[1:]
command = args[2]
with (root / "commands.jsonl").open("a") as stream:
    stream.write(json.dumps(args) + "\\n")
if command == "display-message":
    print("\\t".join(state["metadata"]))
elif command == "capture-pane":
    print(state["capture"], end="")
elif command == "list-clients":
    if args[-1] == "#{pane_id}":
        print(state["focus"], end="")
    else:
        print(state.get("clients", ""), end="")
elif command == "load-buffer":
    body = sys.stdin.buffer.read()
    (root / "payload").write_bytes(body)
    (root / "buffer").write_bytes(body)
    if state.get("change_before_paste"):
        state["capture"] = "new manual draft\\n"
        (root / "state.json").write_text(json.dumps(state))
elif command == "paste-buffer":
    if state.get("change_after_paste"):
        state["metadata"][6] = "456"
        (root / "state.json").write_text(json.dumps(state))
elif command == "send-keys":
    if state.get("fail_submit"):
        sys.exit(1)
    (root / "submitted").write_text(args[args.index("-t") + 1])
elif command == "delete-buffer":
    if state.get("fail_cleanup"):
        sys.exit(1)
    (root / "buffer").unlink()
'''


# Runs the real main() with a pause that logs itself instead of sleeping, so tests keep
# the paste-settle ordering in view without waiting for it.
LAUNCH = '''
import json, os, pathlib, runpy, sys
script = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(script.parent))
api = runpy.run_path(str(script))
def pause(seconds):
    with (pathlib.Path(os.environ["FAKE_TMUX_ROOT"]) / "commands.jsonl").open("a") as stream:
        stream.write(json.dumps(["pause", seconds]) + "\\n")
sys.exit(api["main"](sys.argv[2:], pause))
'''


class DispatchTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.checkout = self.root / "control"
        scripts = self.checkout / "scripts"
        scripts.mkdir(parents=True)
        source = Path(__file__).parents[1] / "scripts"
        for filename in ("control-agents", "control_config.py", "control_registry.py",
                         "tmux_transport.py", "runtime_directory.py", "agent_status.py"):
            shutil.copyfile(source / filename, scripts / filename)
        self.command = scripts / "control-agents"
        write_control(self.checkout, self.root, "| example | example | @1 | %2 | Codex | tests |\n")
        self.state = {"metadata": ["%2", "@1", "main", str(self.root / "example"),
                                   "ace", "0", "123", "80", "24"],
                      "capture": "Agent prompt >\n", "focus": "%28\n"}
        self.save_state()
        binary = self.root / "bin"
        binary.mkdir()
        (binary / "tmux").write_text(FAKE_TMUX)
        (binary / "tmux").chmod(0o755)
        self.environment = dict(os.environ, PATH=f"{binary}:{os.environ['PATH']}",
                                FAKE_TMUX_ROOT=str(self.root))

    def save_state(self) -> None:
        (self.root / "state.json").write_text(json.dumps(self.state))

    def invoke(self, *arguments: str, body: str = "Approved work\n") -> subprocess.CompletedProcess[str]:
        return subprocess.run(["python3", "-c", LAUNCH, str(self.command), *arguments],
                              input=body, text=True, capture_output=True,
                              env=self.environment)

    def inspect(self) -> str:
        result = self.invoke("inspect", "example")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith("{"), result.stdout)
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["slug"], "example")
        self.assertEqual(Path(receipt["capture_path"]).read_text(), "Agent prompt >\n")
        return receipt["snapshot"]

    def test_review_then_send_records_identity_and_submission_without_acknowledgment(self) -> None:
        snapshot = self.inspect()
        result = self.invoke("send", "example", "--snapshot", snapshot,
                             body="Literal $(touch nope)\nSecond line\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["state"], "submission-attempted-unacknowledged")
        payload = (self.root / "payload").read_text()
        self.assertTrue(payload.startswith(f"FROM: {AGENT} ({self.checkout.resolve()}), "),
                        payload)
        self.assertIn(f"acting under {PRINCIPAL}'s delegated authority", payload)
        self.assertTrue(payload.endswith("Literal $(touch nope)\nSecond line\n"))
        commands = [json.loads(line) for line in
                    (self.root / "commands.jsonl").read_text().splitlines()]
        self.assertTrue(any("paste-buffer" in row and "-p" in row for row in commands))
        actions = [row[0] if row[0] == "pause" else row[2] for row in commands]
        self.assertEqual([action for action in actions
                          if action in ("paste-buffer", "pause", "send-keys")],
                         ["paste-buffer", "pause", "send-keys"])
        self.assertIn(["pause", 1], commands)
        self.assertTrue((self.root / "submitted").exists())
        self.assertFalse((self.root / "buffer").exists())
        repeated = self.invoke("send", "example", "--snapshot", snapshot)
        self.assertNotEqual(repeated.returncode, 0)

    def test_changed_metadata_capture_or_focus_never_pastes(self) -> None:
        for change in ("capture", "focus", "path", "process", "pane", "dead"):
            with self.subTest(change=change):
                original = json.loads(json.dumps(self.state))
                snapshot = self.inspect()
                if change == "capture":
                    self.state["capture"] = "manual draft\n"
                elif change == "focus":
                    self.state["focus"] = "%2\n"
                else:
                    index = {"path": 3, "process": 4, "pane": 0, "dead": 5}[change]
                    self.state["metadata"][index] = "changed"
                self.save_state()
                result = self.invoke("send", "example", "--snapshot", snapshot)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())
                self.state = original
                self.save_state()

    def test_unknown_slug_and_invalid_snapshot_fail_closed(self) -> None:
        for arguments in (("inspect", "unknown"),
                          ("send", "example", "--snapshot", "../escape")):
            with self.subTest(arguments=arguments):
                result = self.invoke(*arguments)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())

    def test_stale_receipt_is_refused(self) -> None:
        snapshot = self.inspect()
        receipt_path = self.checkout / ".ace/tmux" / f"{snapshot}.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["created"] = 0
        receipt_path.write_text(json.dumps(receipt))
        result = self.invoke("send", "example", "--snapshot", snapshot)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "payload").exists())

    def test_failed_enter_preserves_partial_delivery_and_prevents_replay(self) -> None:
        snapshot = self.inspect()
        self.state["fail_submit"] = True
        self.save_state()
        result = self.invoke("send", "example", "--snapshot", snapshot)
        self.assertNotEqual(result.returncode, 0)
        runtime = self.checkout / ".ace/tmux"
        self.assertTrue((runtime / f"{snapshot}.pasted.json").exists())
        self.assertTrue((runtime / f"{snapshot}.failed.json").exists())
        self.assertFalse((runtime / f"{snapshot}.submission-attempted-unacknowledged.json").exists())
        self.state["fail_submit"] = False
        self.save_state()
        repeated = self.invoke("send", "example", "--snapshot", snapshot)
        self.assertNotEqual(repeated.returncode, 0)
        self.assertFalse((self.root / "submitted").exists())
        self.assertFalse((self.root / "buffer").exists())

    def test_simultaneous_dispatch_to_one_slug_submits_only_once(self) -> None:
        snapshots = (self.inspect(), self.inspect())
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(
                lambda receipt: self.invoke("send", "example", "--snapshot", receipt),
                snapshots,
            ))
        self.assertEqual(sum(result.returncode == 0 for result in results), 1)
        commands = [json.loads(line) for line in
                    (self.root / "commands.jsonl").read_text().splitlines()]
        self.assertEqual(sum("send-keys" in row for row in commands), 1)

    def test_invalid_body_and_mismatched_receipt_never_paste(self) -> None:
        for body in (" ", "FROM: chakrit\nDo this", "text\x1b[3~", "text\x7f"):
            with self.subTest(body=body):
                snapshot = self.inspect()
                result = self.invoke("send", "example", "--snapshot", snapshot, body=body)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())
        snapshot = self.inspect()
        path = self.checkout / ".ace/tmux" / f"{snapshot}.json"
        raw = json.loads(path.read_text())
        raw["slug"] = "other"
        path.write_text(json.dumps(raw))
        result = self.invoke("send", "example", "--snapshot", snapshot)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "payload").exists())

    def test_symlinked_runtime_never_writes_outside_checkout(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.checkout / ".ace").symlink_to(outside, target_is_directory=True)
        result = self.invoke("inspect", "example")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])

    def test_listing_is_registry_only_without_tmux_contact(self) -> None:
        result = self.invoke("list")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["projects"],
                         [{"slug": "example", "checkout": str(self.root / "example"),
                           "pane": "%2", "window": "@1"}])
        self.assertFalse((self.root / "commands.jsonl").exists())

    def test_changes_during_delivery_withhold_paste_or_enter(self) -> None:
        for phase in ("change_before_paste", "change_after_paste"):
            with self.subTest(phase=phase):
                snapshot = self.inspect()
                self.state[phase] = True
                self.save_state()
                result = self.invoke("send", "example", "--snapshot", snapshot)
                self.assertNotEqual(result.returncode, 0)
                runtime = self.checkout / ".ace/tmux"
                pasted = (runtime / f"{snapshot}.pasted.json").exists()
                self.assertEqual(pasted, phase == "change_after_paste")
                self.assertFalse((self.root / "submitted").exists())
                self.assertFalse((self.root / "buffer").exists())
                self.state.pop(phase)
                self.save_state()

    def test_symlinked_and_malformed_receipts_are_refused(self) -> None:
        for kind in ("symlink", "malformed"):
            with self.subTest(kind=kind):
                snapshot = self.inspect()
                receipt = self.checkout / ".ace/tmux" / f"{snapshot}.json"
                if kind == "symlink":
                    outside = self.root / "outside-receipt.json"
                    outside.write_text(receipt.read_text())
                    receipt.unlink()
                    receipt.symlink_to(outside)
                else:
                    receipt.write_text('{"slug": "example"}')
                result = self.invoke("send", "example", "--snapshot", snapshot)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())

    def test_clear_context_sends_only_command_and_logs_checkpoint_and_sender(self) -> None:
        snapshot = self.inspect()
        checkpoint = str(self.root / "example/.ace/save.md")
        result = self.invoke("clear-context", "example", "--snapshot", snapshot,
                             "--checkpoint", checkpoint, body="Must not be sent")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "payload").read_text(), "/clear")
        attempted = json.loads((self.checkout / ".ace/tmux" /
                                f"{snapshot}.attempted.json").read_text())
        self.assertEqual(attempted["checkpoint"], checkpoint)
        self.assertEqual(attempted["action"], "clear-context")
        self.assertIn(f"FROM: {AGENT} ", attempted["sender"])
        self.assertIn(f"acting under {PRINCIPAL}'s delegated authority", attempted["sender"])
        self.assertEqual(json.loads(result.stdout)["state"],
                         "submission-attempted-unacknowledged")
        repeated = self.invoke("clear-context", "example", "--snapshot", snapshot,
                               "--checkpoint", checkpoint)
        self.assertNotEqual(repeated.returncode, 0)

    def clear(self) -> subprocess.CompletedProcess[str]:
        return self.invoke("clear-context", "example", "--snapshot", self.inspect(),
                           "--checkpoint", str(self.root / "example/.ace/save.md"))

    def status_record(self) -> dict:
        return json.loads((self.checkout / ".ace/status/example.json").read_text())

    def test_clear_context_creates_idle_cleared_record_with_no_task(self) -> None:
        result = self.clear()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status_record"], "cleared")
        record = self.status_record()
        self.assertEqual((record["slug"], record["task"], record["state"], record["context"],
                          record["subagents"]),
                         ("example", "-", "idle", "cleared", []))

    def test_clear_context_keeps_task_and_subagents_of_existing_record(self) -> None:
        earlier = "2026-11-02T00:00:00+00:00"
        records = self.checkout / ".ace/status"
        records.mkdir(parents=True)
        subagent = {"id": "a1", "description": "Survey", "state": "running",
                    "updated_at": earlier}
        (records / "example.json").write_text(json.dumps(
            {"slug": "example", "task": "regression", "state": "done", "summary": "Saved",
             "context": "saved", "updated_at": earlier, "subagents": [subagent]}))
        result = self.clear()
        self.assertEqual(result.returncode, 0, result.stderr)
        record = self.status_record()
        self.assertEqual((record["task"], record["state"], record["context"],
                          record["subagents"]),
                         ("regression", "idle", "cleared", [subagent]))
        self.assertGreater(record["updated_at"], earlier)

    def test_refused_clear_leaves_status_record_alone(self) -> None:
        self.state["focus"] = "%2\n"
        self.save_state()
        result = self.clear()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.checkout / ".ace/status/example.json").exists())

    def test_unwritable_status_record_does_not_hide_a_submitted_clear(self) -> None:
        records = self.checkout / ".ace/status"
        records.mkdir(parents=True)
        (records / "example.json").write_text('{"slug": "example"}')
        result = self.clear()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "payload").read_text(), "/clear")
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["state"], "submission-attempted-unacknowledged")
        self.assertTrue(receipt["status_record"].startswith("not updated:"))
        self.assertEqual(self.status_record(), {"slug": "example"})

    def test_clear_context_rejects_paths_outside_registered_checkout(self) -> None:
        checkpoint_paths = (".ace/save.md", str(self.root / "other/.ace/save.md"),
                            str(self.root / "example/../other/save.md"),
                            str(self.root / "example2/save.md"), str(self.root / "example"))
        for checkpoint in checkpoint_paths:
            with self.subTest(checkpoint=checkpoint):
                snapshot = self.inspect()
                result = self.invoke("clear-context", "example", "--snapshot", snapshot,
                                     "--checkpoint", checkpoint)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())

    def test_clear_context_refuses_focused_or_stale_receipts(self) -> None:
        for kind in ("focus", "stale"):
            with self.subTest(kind=kind):
                snapshot = self.inspect()
                if kind == "focus":
                    self.state["focus"] = "%2\n"
                    self.save_state()
                else:
                    receipt = self.checkout / ".ace/tmux" / f"{snapshot}.json"
                    raw = json.loads(receipt.read_text())
                    raw["created"] = 0
                    receipt.write_text(json.dumps(raw))
                result = self.invoke("clear-context", "example", "--snapshot", snapshot,
                                     "--checkpoint", str(self.root / "example/.ace/save.md"))
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())
                self.state["focus"] = "%28\n"
                self.save_state()

    def test_rename_session_sends_rename_command_with_sender_audit(self) -> None:
        snapshot = self.inspect()
        result = self.invoke("rename-session", "example", "--snapshot", snapshot,
                             "--name", "nkkt:clos-frontend", body="Must not be sent")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "payload").read_text(), "/rename nkkt:clos-frontend")
        event = json.loads((self.checkout / ".ace/tmux" /
                            f"{snapshot}.attempted.json").read_text())
        self.assertEqual(event["action"], "rename-session")
        self.assertEqual(event["name"], "nkkt:clos-frontend")
        self.assertIn(f"FROM: {AGENT} ", event["sender"])
        repeated = self.invoke("rename-session", "example", "--snapshot", snapshot,
                               "--name", "nkkt:clos-frontend")
        self.assertNotEqual(repeated.returncode, 0)

    def test_rename_session_accepts_every_control_level_agent_name(self) -> None:
        for name in ("lz49:control", "lz49:datawow:control", "lz49:datawow:cookie_wow"):
            with self.subTest(name=name):
                result = self.invoke("rename-session", "example", "--snapshot",
                                     self.inspect(), "--name", name)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual((self.root / "payload").read_text(), f"/rename {name}")

    def test_rename_session_rejects_names_outside_agent_name_format(self) -> None:
        names = ("", "datawow", "datawow:", ":control", "data wow:control",
                 "datawow:control\n/exit", "lz49:datawow:control:extra", "Datawow:Control",
                 "datawow:-control", "lz49::control")
        for name in names:
            with self.subTest(name=name):
                snapshot = self.inspect()
                result = self.invoke("rename-session", "example", "--snapshot", snapshot,
                                     "--name", name)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "payload").exists())

    def test_clients_reports_exact_identity_and_known_slug(self) -> None:
        self.state["clients"] = "/dev/ttys001\tmain\t%2\n/dev/ttys002\tother\t%99\n"
        self.save_state()
        result = self.invoke("clients")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["clients"], [
            {"name": "/dev/ttys001", "session": "main", "pane": "%2", "slug": "example"},
            {"name": "/dev/ttys002", "session": "other", "pane": "%99", "slug": ""},
        ])
        self.assertFalse((self.checkout / ".ace").exists())

    def test_malformed_clients_fail_closed(self) -> None:
        for reply in ("client\tmain\n", "client\tmain\tbad-pane\n"):
            with self.subTest(reply=reply):
                self.state["clients"] = reply
                self.save_state()
                result = self.invoke("clients")
                self.assertNotEqual(result.returncode, 0)

    def test_exit_agent_sends_literal_command_with_checkpoint_audit(self) -> None:
        snapshot = self.inspect()
        checkpoint = str(self.root / "example/.ace/save.md")
        result = self.invoke("exit-agent", "example", "--snapshot", snapshot,
                             "--checkpoint", checkpoint)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "payload").read_text(), "/exit")
        event = json.loads((self.checkout / ".ace/tmux" /
                            f"{snapshot}.attempted.json").read_text())
        self.assertEqual(event["checkpoint"], checkpoint)
        self.assertEqual(event["action"], "exit-agent")
        self.assertIn(f"FROM: {AGENT} ", event["sender"])

    def exit_confirmation(self) -> str:
        self.state["capture"] = ("Background work is running\n"
                                 "❯ 1. Exit and stop tasks\n"
                                 "  2. Keep working\n"
                                 "Enter to confirm · Esc to cancel\n")
        self.save_state()
        result = self.invoke("inspect", "example")
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)["snapshot"]

    def test_confirm_exit_sends_only_enter_and_audits_checkpoint_sender(self) -> None:
        snapshot = self.exit_confirmation()
        checkpoint = str(self.root / "example/.ace/save.md")
        result = self.invoke("confirm-exit", "example", "--snapshot", snapshot,
                             "--checkpoint", checkpoint)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "submitted").read_text(), "%2")
        self.assertFalse((self.root / "payload").exists())
        self.assertFalse((self.root / "buffer").exists())
        event = json.loads((self.checkout / ".ace/tmux" /
                            f"{snapshot}.attempted.json").read_text())
        self.assertEqual(event["action"], "confirm-exit")
        self.assertEqual(event["checkpoint"], checkpoint)
        self.assertIn(f"FROM: {AGENT} ", event["sender"])
        repeated = self.invoke("confirm-exit", "example", "--snapshot", snapshot,
                               "--checkpoint", checkpoint)
        self.assertNotEqual(repeated.returncode, 0)

    def test_confirm_exit_requires_recognized_selected_active_prompt(self) -> None:
        prompts = ("Agent prompt >\n",
                   "❯ 1. Exit and stop tasks\nEnter to confirm · Esc to cancel\n",
                   "Background work is running\n❯ 2. Keep working\n"
                   "Enter to confirm · Esc to cancel\n",
                   "Background work is running\n❯ 1. Exit and stop tasks\n"
                   "Enter to confirm · Esc to cancel\nNew input >\n")
        for capture in prompts:
            with self.subTest(capture=capture):
                self.state["capture"] = capture
                self.save_state()
                result = self.invoke("inspect", "example")
                snapshot = json.loads(result.stdout)["snapshot"]
                denied = self.invoke("confirm-exit", "example", "--snapshot", snapshot,
                                     "--checkpoint", str(self.root / "example/.ace/save.md"))
                self.assertNotEqual(denied.returncode, 0)
                self.assertFalse((self.root / "submitted").exists())
                self.assertFalse((self.root / "payload").exists())

    def test_confirm_exit_refuses_focus_stale_changed_or_mismatched_receipts(self) -> None:
        for kind in ("focus", "stale", "changed", "mismatch"):
            with self.subTest(kind=kind):
                snapshot = self.exit_confirmation()
                if kind == "focus":
                    self.state["focus"] = "%2\n"
                elif kind == "changed":
                    self.state["capture"] = "Background work is running\n❯ 2. Keep working\n"
                else:
                    path = self.checkout / ".ace/tmux" / f"{snapshot}.json"
                    raw = json.loads(path.read_text())
                    raw["created" if kind == "stale" else "slug"] = 0 if kind == "stale" else "other"
                    path.write_text(json.dumps(raw))
                self.save_state()
                result = self.invoke("confirm-exit", "example", "--snapshot", snapshot,
                                     "--checkpoint", str(self.root / "example/.ace/save.md"))
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.root / "submitted").exists())
                self.assertFalse((self.root / "payload").exists())
                self.state["focus"] = "%28\n"

    def test_exit_operations_reject_stale_receipts_and_invalid_checkpoints(self) -> None:
        snapshot = self.inspect()
        result = self.invoke("exit-agent", "example", "--snapshot", snapshot,
                             "--checkpoint", str(self.root / "other/save.md"))
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "payload").exists())
        snapshot = self.inspect()
        receipt_path = self.checkout / ".ace/tmux" / f"{snapshot}.json"
        raw = json.loads(receipt_path.read_text())
        raw["created"] = 0
        receipt_path.write_text(json.dumps(raw))
        result = self.invoke("exit-agent", "example", "--snapshot", snapshot,
                             "--checkpoint", str(self.root / "example/.ace/save.md"))
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "payload").exists())

    def commands(self) -> list[list[str]]:
        path = self.root / "commands.jsonl"
        lines = path.read_text().splitlines() if path.exists() else []
        return [json.loads(line) for line in lines]

    def test_exit_shell_types_exit_into_the_idle_shell_left_by_the_harness(self) -> None:
        self.state["metadata"][4] = "zsh"
        self.save_state()
        result = self.invoke("exit-shell", "example")
        self.assertEqual(result.returncode, 0, result.stderr)
        keys = [command[3:] for command in self.commands() if command[2] == "send-keys"]
        self.assertEqual(keys, [["-t", "%2", "-l", "exit"], ["-t", "%2", "Enter"]])
        receipt = json.loads(result.stdout)
        event = json.loads((self.checkout / ".ace/tmux" /
                            f"{receipt['receipt']}.attempted.json").read_text())
        self.assertEqual(event["action"], "exit-shell")
        self.assertIn(f"FROM: {AGENT} ", event["sender"])

    def test_exit_shell_refuses_a_running_harness_focus_or_foreign_folder(self) -> None:
        cases = {"harness": (4, "ace"), "foreign": (3, "/elsewhere"),
                 "job": (4, "node"), "focus": None}
        for kind, change in cases.items():
            with self.subTest(kind=kind):
                self.state["metadata"] = ["%2", "@1", "main", str(self.root / "example"),
                                          "zsh", "0", "123", "80", "24"]
                self.state["focus"] = "%2\n" if change is None else "%28\n"
                if change is not None:
                    self.state["metadata"][change[0]] = change[1]
                self.save_state()
                result = self.invoke("exit-shell", "example")
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(any(command[2] == "send-keys" for command in self.commands()))

    def test_registry_rows_with_a_shell_pane_column_are_refused(self) -> None:
        (self.checkout / "registries/projects.md").write_text(
            "| Project | Checkout | Window | Agent | Shell | Backend | Assignment |\n"
            "| ------- | -------- | ------ | ----- | ----- | ------- | ---------- |\n"
            "| example | example | @1 | %2 | %3 | Codex | tests |\n"
        )
        result = self.invoke("list")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid project registry row for example", result.stderr)
        self.assertFalse((self.root / "commands.jsonl").exists())

    def write_config(self, text: str) -> None:
        (self.checkout / "control.toml").write_text(text, encoding="utf-8")

    def test_harness_processes_come_from_config(self) -> None:
        self.state["metadata"][4] = "codex"
        self.save_state()
        refused = self.invoke("inspect", "example")
        self.assertNotEqual(refused.returncode, 0)
        self.assertIn("checkout/process", refused.stderr)
        self.write_config(config_text(self.root).replace('harness = ["ace"]',
                                                         'harness = ["ace", "codex"]'))
        result = self.invoke("send", "example", "--snapshot", self.inspect())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.root / "submitted").exists())

    def test_tmux_session_and_socket_come_from_config(self) -> None:
        self.state["metadata"][2] = "work"
        self.save_state()
        self.assertNotEqual(self.invoke("inspect", "example").returncode, 0)
        self.write_config(config_text(self.root)
                          .replace('tmux_session = "main"', 'tmux_session = "work"')
                          .replace('"/synthetic/socket"', '"/synthetic/other-socket"'))
        self.inspect()
        sockets = {row[1] for row in self.commands()}
        self.assertEqual(sockets, {"/synthetic/socket", "/synthetic/other-socket"})
        self.assertEqual([row[1] for row in self.commands()][-1], "/synthetic/other-socket")

    def test_confirm_exit_without_configured_screen_is_refused(self) -> None:
        snapshot = self.exit_confirmation()
        self.write_config(config_text(self.root, tables=""))
        result = self.invoke("confirm-exit", "example", "--snapshot", snapshot,
                             "--checkpoint", str(self.root / "example/.ace/save.md"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exit_confirmation", result.stderr)
        self.assertFalse((self.root / "submitted").exists())

    def test_confirm_exit_recognizes_the_configured_screen_only(self) -> None:
        self.write_config(config_text(self.root, tables=(
            '[exit_confirmation]\nnotice = "Tasks still running"\n'
            'footer = "y/n?"\nmarker = ">"\noption = "Stop them"\n')))
        claude = self.exit_confirmation()
        denied = self.invoke("confirm-exit", "example", "--snapshot", claude,
                             "--checkpoint", str(self.root / "example/.ace/save.md"))
        self.assertNotEqual(denied.returncode, 0)
        self.assertFalse((self.root / "submitted").exists())
        self.state["capture"] = "Tasks still running\n> Stop them\n  Keep them\ny/n?\n"
        self.save_state()
        snapshot = json.loads(self.invoke("inspect", "example").stdout)["snapshot"]
        result = self.invoke("confirm-exit", "example", "--snapshot", snapshot,
                             "--checkpoint", str(self.root / "example/.ace/save.md"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / "submitted").read_text(), "%2")

    def test_cleanup_failure_preserves_original_submission_error(self) -> None:
        snapshot = self.inspect()
        self.state.update(fail_submit=True, fail_cleanup=True)
        self.save_state()
        result = self.invoke("send", "example", "--snapshot", snapshot)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("send-keys", result.stderr)
        self.assertIn("delete-buffer", result.stderr)
        failed = json.loads((self.checkout / ".ace/tmux" /
                             f"{snapshot}.failed.json").read_text())
        self.assertIn("send-keys", failed["error"])
        self.assertIn("delete-buffer", failed["error"])
        self.assertTrue((self.root / "buffer").exists())
        self.assertFalse((self.root / "submitted").exists())


if __name__ == "__main__":
    unittest.main()
