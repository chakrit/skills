"""Exercise the agent status protocol: status records, subagents, reports and wrapper."""

import concurrent.futures
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from config_fixture import write_control


SOURCE = Path(__file__).parents[1]
SCRIPTS = ("control-agent", "control-agents", "control_config.py", "control_registry.py",
           "agent_inbox.py", "agent_status.py", "runtime_directory.py", "tmux_transport.py")
# The per-checkout wrapper each project agent installs, with CONTROL and SLUG filled in.
WRAPPER = '#!/bin/sh\nexec CONTROL/scripts/control-agent --slug SLUG "$@"\n'


class Fixture(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.checkout = self.root / "control"
        scripts = self.checkout / "scripts"
        scripts.mkdir(parents=True)
        for filename in SCRIPTS:
            shutil.copy2(SOURCE / "scripts" / filename, scripts / filename)
        write_control(self.checkout, self.root,
                      "| example | example | @1 | %2 | Claude | tests |\n"
                      "| other | other | @3 | %4 | Codex | tests |\n",
                      "## regression — project agent\n\n## follow-up — project agent\n")
        self.records = self.checkout / ".ace/status"
        self.inbox = self.checkout / ".ace/inbox"

    def agent(self, *arguments: str, slug: str = "example",
              body: str = "") -> subprocess.CompletedProcess[str]:
        command = [sys.executable, str(self.checkout / "scripts/control-agent"),
                   "--slug", slug, *arguments]
        return subprocess.run(command, input=body, text=True, capture_output=True,
                              cwd=self.root)

    def succeed(self, *arguments: str, body: str = "") -> subprocess.CompletedProcess[str]:
        result = self.agent(*arguments, body=body)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def record(self, slug: str = "example") -> dict:
        return json.loads((self.records / f"{slug}.json").read_text(encoding="utf-8"))

    def write_record(self, record: dict, slug: str = "example") -> None:
        self.records.mkdir(parents=True, exist_ok=True)
        (self.records / f"{slug}.json").write_text(json.dumps(record), encoding="utf-8")


class StatusWriteTests(Fixture):
    def test_status_writes_complete_record_with_script_timestamp(self) -> None:
        before = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
        self.succeed("status", "working", "Writing the login flow", "--task", "regression")
        record = self.record()
        self.assertEqual(set(record), {"slug", "task", "state", "summary", "context",
                                       "updated_at", "subagents"})
        self.assertEqual((record["slug"], record["task"], record["state"], record["summary"],
                          record["context"], record["subagents"]),
                         ("example", "regression", "working", "Writing the login flow",
                          "unsaved", []))
        updated = datetime.datetime.fromisoformat(record["updated_at"])
        self.assertEqual(updated.utcoffset(), datetime.timedelta(0))
        self.assertGreaterEqual(updated, before)

    def test_invalid_inputs_fail_without_writing_a_record(self) -> None:
        cases = (
            ("unknown", ("status", "working", "summary", "--task", "regression")),
            ("../example", ("status", "working", "summary", "--task", "regression")),
            ("example", ("status", "working", "summary", "--task", "unknown")),
            ("example", ("status", "sleeping", "summary", "--task", "regression")),
            ("example", ("status", "working", "summary", "--task", "regression",
                         "--context", "lost")),
            ("example", ("status", "working", "two\nlines", "--task", "regression")),
            ("example", ("status", "working", "  ", "--task", "regression")),
            ("example", ("status", "working", "x" * 201, "--task", "regression")),
            ("example", ("status", "working", "first record needs a task")),
            ("example", ("subagent", "a1", "running", "no status record yet")),
        )
        for slug, arguments in cases:
            with self.subTest(slug=slug, arguments=arguments):
                result = self.agent(*arguments, slug=slug)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertFalse(self.records.exists() and any(self.records.glob("*.json")))

    def test_slug_is_required_and_cannot_be_overridden(self) -> None:
        script = str(self.checkout / "scripts/control-agent")
        missing = subprocess.run([sys.executable, script, "whoami"], text=True,
                                 capture_output=True)
        self.assertNotEqual(missing.returncode, 0)
        for arguments in (("whoami", "--slug", "other"), ("--slug", "other", "whoami")):
            with self.subTest(arguments=arguments):
                override = self.agent(*arguments)
                self.assertNotEqual(override.returncode, 0)
                self.assertEqual(override.stdout, "")

    def test_overwrite_keeps_task_context_and_subagents_and_replaces_atomically(self) -> None:
        self.succeed("status", "working", "Start", "--task", "regression")
        self.succeed("subagent", "a1", "running", "Survey fixtures")
        first = os.stat(self.records / "example.json").st_ino
        self.succeed("status", "waiting-user", "Need a ruling on scope")
        record = self.record()
        self.assertEqual((record["task"], record["state"], record["summary"],
                          record["context"]),
                         ("regression", "waiting-user", "Need a ruling on scope", "unsaved"))
        self.assertEqual([entry["id"] for entry in record["subagents"]], ["a1"])
        self.assertNotEqual(os.stat(self.records / "example.json").st_ino, first)
        self.assertEqual(sorted(path.name for path in self.records.iterdir()),
                         ["example.json", "example.lock"])
        self.succeed("status", "working", "Next task", "--task", "follow-up",
                     "--context", "saved")
        self.assertEqual((self.record()["task"], self.record()["context"]),
                         ("follow-up", "saved"))

    def test_symlinked_record_is_replaced_without_writing_through_it(self) -> None:
        outside = self.root / "outside.json"
        outside.write_text("preserve\n", encoding="utf-8")
        self.records.mkdir(parents=True)
        (self.records / "example.json").symlink_to(outside)
        result = self.agent("status", "working", "Start", "--task", "regression")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(outside.read_text(encoding="utf-8"), "preserve\n")

    def test_symlinked_status_directory_cannot_escape_checkout(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.checkout / ".ace").mkdir()
        (self.checkout / ".ace/status").symlink_to(outside, target_is_directory=True)
        result = self.agent("status", "working", "Start", "--task", "regression")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])

    def test_done_or_idle_with_running_subagents_warns_but_writes(self) -> None:
        self.succeed("status", "working", "Start", "--task", "regression")
        self.succeed("subagent", "a1", "running", "Survey fixtures")
        for state in ("done", "idle"):
            with self.subTest(state=state):
                result = self.succeed("status", state, "Finished")
                self.assertIn("a1", result.stderr)
                self.assertIn("running", result.stderr)
                self.assertEqual(self.record()["state"], state)
        self.succeed("subagent", "a1", "done")
        quiet = self.succeed("status", "done", "Finished")
        self.assertEqual(quiet.stderr, "")


class SubagentTests(Fixture):
    def test_subagent_upsert_requires_first_description_and_keeps_it(self) -> None:
        self.succeed("status", "working", "Start", "--task", "regression")
        missing = self.agent("subagent", "a1", "running")
        self.assertNotEqual(missing.returncode, 0)
        self.assertEqual(self.record()["subagents"], [])
        self.succeed("subagent", "a1", "running", "Survey fixtures")
        self.succeed("subagent", "b2", "running", "Draft docs")
        self.succeed("subagent", "a1", "done")
        self.succeed("subagent", "b2", "running", "Draft docs and guides")
        entries = {entry["id"]: entry for entry in self.record()["subagents"]}
        self.assertEqual(list(entries), ["a1", "b2"])
        self.assertEqual((entries["a1"]["state"], entries["a1"]["description"]),
                         ("done", "Survey fixtures"))
        self.assertEqual((entries["b2"]["state"], entries["b2"]["description"]),
                         ("running", "Draft docs and guides"))
        self.assertEqual(self.record()["state"], "working")

    def test_task_change_drops_done_subagents_and_warns_about_running_ones(self) -> None:
        self.succeed("status", "working", "Start", "--task", "regression")
        self.succeed("subagent", "a1", "running", "Survey fixtures")
        self.succeed("subagent", "b2", "running", "Draft docs")
        self.succeed("subagent", "b2", "done")
        for arguments in (("status", "working", "Same task"),
                          ("status", "working", "Same task", "--task", "regression")):
            with self.subTest(arguments=arguments):
                result = self.succeed(*arguments)
                self.assertEqual(result.stderr, "")
                self.assertEqual([entry["id"] for entry in self.record()["subagents"]],
                                 ["a1", "b2"])
        changed = self.succeed("status", "working", "Next task", "--task", "follow-up")
        self.assertEqual([(entry["id"], entry["state"])
                          for entry in self.record()["subagents"]], [("a1", "running")])
        self.assertIn("follow-up", changed.stderr)
        self.assertIn("a1", changed.stderr)
        self.succeed("subagent", "a1", "done")
        quiet = self.succeed("status", "working", "Back again", "--task", "regression")
        self.assertEqual((quiet.stderr, self.record()["subagents"]), ("", []))

    def test_invalid_subagent_inputs_leave_record_unchanged(self) -> None:
        self.succeed("status", "working", "Start", "--task", "regression")
        before = self.record()
        for arguments in (("../a1", "running", "desc"), ("a1", "paused", "desc"),
                          ("a1", "running", "two\nlines"), ("", "running", "desc")):
            with self.subTest(arguments=arguments):
                self.assertNotEqual(self.agent("subagent", *arguments).returncode, 0)
                self.assertEqual(self.record(), before)

    def test_concurrent_subagent_upserts_lose_no_entries(self) -> None:
        self.succeed("status", "working", "Start", "--task", "regression")
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            results = list(executor.map(
                lambda number: self.agent("subagent", f"s{number}", "running",
                                          f"Parallel part {number}"),
                range(16)))
        self.assertTrue(all(result.returncode == 0 for result in results),
                        [result.stderr for result in results])
        self.assertEqual({entry["id"] for entry in self.record()["subagents"]},
                         {f"s{number}" for number in range(16)})


class WhoamiAndReportTests(Fixture):
    def test_whoami_prints_slug_checkout_and_current_status(self) -> None:
        empty = json.loads(self.succeed("whoami").stdout)
        self.assertEqual(empty, {"slug": "example", "checkout": str(self.root / "example"),
                                 "status": None})
        self.succeed("status", "working", "Start", "--task", "regression")
        current = json.loads(self.succeed("whoami").stdout)
        self.assertEqual(current["status"], self.record())

    def test_report_submits_to_inbox_with_task_from_status_record(self) -> None:
        self.succeed("status", "working", "Start", "--task", "follow-up")
        body = "Evidence: tests passed.\n$(touch nope)\n"
        receipt = json.loads(self.succeed("report", "done", body=body).stdout)
        self.assertEqual(receipt["status"], "submitted")
        message = json.loads((self.inbox / f"{receipt['message_id']}.json").read_text())
        self.assertEqual((message["project"], message["task"], message["kind"],
                          message["body"]), ("example", "follow-up", "done", body))
        explicit = json.loads(self.succeed("report", "status", "--task", "regression",
                                           body="Progress\n").stdout)
        message = json.loads((self.inbox / f"{explicit['message_id']}.json").read_text())
        self.assertEqual(message["task"], "regression")
        self.assertFalse((self.root / "nope").exists())

    def test_record_without_task_requires_an_explicit_task(self) -> None:
        self.write_record({"slug": "example", "task": "-", "state": "idle",
                           "summary": "Context cleared by control", "context": "cleared",
                           "updated_at": "2026-11-02T00:00:00+00:00", "subagents": []})
        self.assertNotEqual(self.agent("status", "working", "Start").returncode, 0)
        self.assertNotEqual(self.agent("report", "status", body="Progress\n").returncode, 0)
        self.assertEqual(self.record()["task"], "-")
        self.succeed("status", "working", "Start", "--task", "regression")
        self.assertEqual((self.record()["task"], self.record()["context"]),
                         ("regression", "cleared"))

    def test_report_refuses_invalid_input_without_inbox_files(self) -> None:
        refused = (
            (("report", "done"), "no task in a record yet\n"),
            (("report", "execute", "--task", "regression"), "body\n"),
            (("report", "done", "--task", "unknown"), "body\n"),
            (("report", "done", "--task", "regression"), " \n"),
        )
        for arguments, body in refused:
            with self.subTest(arguments=arguments):
                result = self.agent(*arguments, body=body)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertFalse(self.inbox.exists() and any(self.inbox.iterdir()))


class WrapperTests(Fixture):
    def test_wrapper_passes_slug_and_arguments_through(self) -> None:
        project = self.root / "example"
        project.mkdir()
        path = project / "control-agent"
        path.write_text(WRAPPER.replace("CONTROL", str(self.checkout))
                        .replace("SLUG", "example"), encoding="utf-8")
        path.chmod(0o755)
        environment = dict(os.environ,
                           PATH=f"{Path(sys.executable).parent}:{os.environ['PATH']}")
        run = subprocess.run(["./control-agent", "status", "working",
                              "Summary with  spaces; $(touch nope)", "--task", "regression"],
                             cwd=project, text=True, capture_output=True, env=environment)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(self.record()["summary"], "Summary with  spaces; $(touch nope)")
        whoami = subprocess.run(["./control-agent", "whoami"], cwd=project, text=True,
                                capture_output=True, env=environment)
        self.assertEqual(json.loads(whoami.stdout)["slug"], "example")
        self.assertFalse((project / "nope").exists())


class StatusReaderTests(Fixture):
    NOW = datetime.datetime(2026, 11, 2, 12, 0, tzinfo=datetime.timezone.utc)

    def status_module(self):
        sys.path.insert(0, str(self.checkout / "scripts"))
        self.addCleanup(sys.path.remove, str(self.checkout / "scripts"))
        import importlib
        sys.modules.pop("agent_status", None)
        return importlib.import_module("agent_status")

    def record_at(self, state: str, minutes: int, subagents: tuple = (),
                  now: datetime.datetime = NOW) -> dict:
        updated = (now - datetime.timedelta(minutes=minutes)).isoformat()
        return {"slug": "example", "task": "regression", "state": state,
                "summary": "Summary", "context": "unsaved", "updated_at": updated,
                "subagents": [{"id": identifier, "description": f"Part {identifier}",
                               "state": sub_state, "updated_at": updated}
                              for identifier, sub_state in subagents]}

    def test_stale_flag_follows_state_subagents_age_and_threshold(self) -> None:
        status = self.status_module()
        threshold = status.STALE_AFTER
        self.assertEqual(threshold, datetime.timedelta(minutes=15))
        cases = (
            ("working", 14, (), threshold, False),
            ("working", 16, (), threshold, True),
            ("working", 16, (), datetime.timedelta(minutes=30), False),
            ("waiting-user", 60, (), threshold, False),
            ("blocked", 60, (), threshold, False),
            ("blocked", 60, (("a1", "running"),), threshold, True),
            ("blocked", 60, (("a1", "done"),), threshold, False),
            ("idle", 600, (("a1", "running"),), threshold, False),
            ("done", 600, (("a1", "running"),), threshold, False),
        )
        for state, minutes, subagents, limit, expected in cases:
            with self.subTest(state=state, minutes=minutes, subagents=subagents,
                              limit=limit):
                record = status.Status.parse(self.record_at(state, minutes, subagents))
                self.assertEqual(status.is_stale(record, self.NOW, limit), expected)

    def test_table_lists_every_registered_slug_with_age_flag_and_subagents(self) -> None:
        status = self.status_module()
        record = status.Status.parse(self.record_at(
            "working", 75, (("a1", "running"), ("b2", "done"))))
        table = status.render((("example", record), ("other", None)),
                              self.NOW, status.STALE_AFTER)
        lines = table.splitlines()
        self.assertEqual(lines[0].split(), ["SLUG", "TASK", "STATE", "CONTEXT", "AGE",
                                            "FLAG", "SUMMARY", "SUBAGENTS"])
        self.assertEqual(lines[1].split()[:7], ["example", "regression", "working",
                                                "unsaved", "1h15m", "STALE", "Summary"])
        self.assertIn("running: a1 (Part a1)", lines[1])
        self.assertIn("done: b2 (Part b2)", lines[1])
        self.assertEqual(lines[2].split(),
                         ["other", "-", "no-record", "-", "-", "-", "-", "-"])

    def test_table_truncates_long_cells_to_fit_160_columns(self) -> None:
        status = self.status_module()
        summary = "Reviewing the consent banner copy " + "and its translations " * 8
        raw = self.record_at("working", 5, tuple((f"agent-{number}", "running")
                                                 for number in range(6)))
        raw["summary"] = summary.strip()[:200]
        raw["task"] = "confirmed-blocker-batch"
        short = status.Status.parse(self.record_at("idle", 5))
        table = status.render((("example", status.Status.parse(raw)), ("other", short)),
                              self.NOW, status.STALE_AFTER)
        lines = table.splitlines()
        self.assertTrue(all(len(line) <= 160 for line in lines),
                        [len(line) for line in lines])
        start = lines[0].index("SUMMARY")
        cell = lines[1][start:].split("  ")[0]
        self.assertTrue(cell.endswith("…"), cell)
        self.assertTrue(summary.startswith(cell[:-1]), cell)
        self.assertLess(len(cell), len(summary.strip()))
        self.assertIn("running: agent-0 (Part agent-0)", lines[1])
        self.assertTrue(lines[1].endswith("…"), lines[1])
        self.assertEqual(lines[2][start:].split("  ")[0], "Summary")

    def test_reader_command_prints_table_and_honours_stale_override(self) -> None:
        self.write_record(self.record_at("working", 20,
                                         now=datetime.datetime.now(datetime.timezone.utc)))
        command = [sys.executable, str(self.checkout / "scripts/control-agents"), "status"]
        table = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(table.returncode, 0, table.stderr)
        self.assertIn("STALE", table.stdout)
        self.assertIn("other", table.stdout)
        single = subprocess.run([*command, "example", "--stale-minutes", "30"],
                                text=True, capture_output=True)
        self.assertEqual(single.returncode, 0, single.stderr)
        self.assertNotIn("STALE", single.stdout)
        self.assertNotIn("other", single.stdout)
        unknown = subprocess.run([*command, "missing"], text=True, capture_output=True)
        self.assertNotEqual(unknown.returncode, 0)

    def test_malformed_record_is_shown_as_invalid_not_hidden(self) -> None:
        self.write_record({"slug": "example", "state": "working"})
        command = [sys.executable, str(self.checkout / "scripts/control-agents"), "status"]
        result = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("invalid", result.stdout)
        refused = self.agent("status", "working", "Start", "--task", "regression")
        self.assertNotEqual(refused.returncode, 0)
        self.assertEqual(self.record(), {"slug": "example", "state": "working"})


if __name__ == "__main__":
    unittest.main()
