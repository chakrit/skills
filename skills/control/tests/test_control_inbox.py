"""Exercise the inbox submission contract of control-inbox."""

import concurrent.futures
import datetime
import json
import pathlib
import runpy
import sys
import shutil
import subprocess
import tempfile
import unittest
import uuid

from config_fixture import config_text, write_control


class SubmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.checkout = pathlib.Path(self.temporary.name) / "control"
        self.command = self.checkout / "scripts" / "control-inbox"
        self.command.parent.mkdir(parents=True)
        source = pathlib.Path(__file__).parents[1] / "scripts"
        for filename in ("control-inbox", "control_config.py", "control_registry.py",
                         "agent_inbox.py", "runtime_directory.py"):
            shutil.copyfile(source / filename, self.command.parent / filename)
        write_control(self.checkout, self.checkout.parent,
                      "| example | example | @1 | %2 | agent | regression |\n")
        self.inbox = self.checkout / ".ace" / "inbox"

    def submit(self, *arguments: str, body: bytes = b"Evidence: tests passed.\n") -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["python3", str(self.command), *arguments], input=body, capture_output=True,
            cwd=self.temporary.name,
        )

    def test_submission_reports_id_and_persists_body_as_data(self) -> None:
        body = "$(touch escaped); `whoami`\nUnicode: สวัสดี\n"
        result = self.submit("example", "regression", "done", body=body.encode())
        self.assertEqual(result.returncode, 0, result.stderr)
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["status"], "submitted")
        identifier = uuid.UUID(receipt["message_id"])
        self.assertEqual(identifier.version, 4)
        files = list(self.inbox.iterdir())
        self.assertEqual([file.name for file in files], [f"{identifier}.json"])
        message = json.loads(files[0].read_text(encoding="utf-8"))
        self.assertEqual(set(message), {"project", "task", "kind", "time", "message_id", "body"})
        self.assertEqual((message["project"], message["task"], message["kind"]),
                         ("example", "regression", "done"))
        self.assertEqual(message["body"], body)
        self.assertEqual(message["message_id"], str(identifier))
        self.assertEqual(datetime.datetime.fromisoformat(message["time"]).utcoffset(),
                         datetime.timedelta(0))
        self.assertFalse((pathlib.Path(self.temporary.name) / "escaped").exists())

    def test_all_message_kinds_are_supported(self) -> None:
        for kind in ("status", "blocker", "question", "done"):
            with self.subTest(kind=kind):
                result = self.submit("example", "regression", kind)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_inputs_fail_without_creating_runtime_files(self) -> None:
        cases = (
            (("../outside", "regression", "done"), b"body"),
            (("example", "../outside", "done"), b"body"),
            (("unknown", "regression", "done"), b"body"),
            (("example", "unknown", "done"), b"body"),
            (("example", "regression", "execute"), b"body"),
            (("example", "regression", "done", "/tmp/target"), b"body"),
            (("example", "regression", "done"), b" \n"),
            (("example", "regression", "done"), b"\xff"),
            ((), b"body"),
        )
        for arguments, body in cases:
            with self.subTest(arguments=arguments, body=body):
                result = self.submit(*arguments, body=body)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(b"control-inbox:", result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertFalse((self.checkout / ".ace").exists())

    def test_missing_registry_fails_closed(self) -> None:
        (self.checkout / "tasks.md").unlink()
        result = self.submit("example", "regression", "done")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.checkout / ".ace").exists())

    def test_missing_or_incomplete_config_fails_closed_naming_the_problem(self) -> None:
        config = self.checkout / "control.toml"
        complete = config_text(self.checkout.parent)
        cases = (
            (None, "control.toml is missing"),
            (complete.replace('principal = "tester"\n', ""), "principal"),
            (complete.replace(f'root = "{self.checkout.parent}"', 'root = "relative"'),
             "root"),
            ('surprise = "value"\n' + complete, "unknown keys: surprise"),
        )
        for content, reason in cases:
            with self.subTest(reason=reason):
                if content is None:
                    config.unlink()
                else:
                    config.write_text(content, encoding="utf-8")
                result = self.submit("example", "regression", "done")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(reason, result.stderr.decode())
                self.assertFalse((self.checkout / ".ace").exists())

    def test_registry_location_comes_from_config(self) -> None:
        config = self.checkout / "control.toml"
        moved = self.checkout / "elsewhere/agents.md"
        moved.parent.mkdir()
        (self.checkout / "registries/projects.md").rename(moved)
        self.assertNotEqual(self.submit("example", "regression", "done").returncode, 0)
        config.write_text(config_text(self.checkout.parent).replace(
            "[exit_confirmation]", 'projects_registry = "elsewhere/agents.md"\n\n'
            "[exit_confirmation]"), encoding="utf-8")
        result = self.submit("example", "regression", "done")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_malformed_project_registry_fails_closed(self) -> None:
        registry = self.checkout / "registries/projects.md"
        original = registry.read_text(encoding="utf-8")
        cases = (
            original.replace("@1", "@wrong"),
            original.replace("%2", "other-pane"),
            original.replace("| example | example |", "| example | ../outside |"),
            original + "| example | example | @2 | %4 | %5 | agent | regression |\n",
            "| example | example | @1 | %2 | %3 | agent | regression |\n",
            "",
        )
        for content in cases:
            with self.subTest(content=content):
                registry.write_text(content, encoding="utf-8")
                result = self.submit("example", "regression", "done")
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.checkout / ".ace").exists())

    def test_message_id_collision_never_overwrites_existing_file(self) -> None:
        sys.path.insert(0, str(self.command.parent))
        try:
            api = runpy.run_path(str(self.command.parent / "agent_inbox.py"))
        finally:
            sys.path.pop(0)
        identifier = "da7f476f-6e9d-4ab1-a6df-bd1e6e05e01a"
        self.inbox.mkdir(parents=True)
        existing = self.inbox / f"{identifier}.json"
        existing.write_bytes(b"original evidence\n")
        message = api["Message"]("example", "regression", api["Kind"].DONE,
                                 "2026-10-12T00:00:00+00:00", identifier, "new body")
        with self.assertRaises(FileExistsError):
            api["publish"](self.checkout, message)
        self.assertEqual(existing.read_bytes(), b"original evidence\n")
        self.assertEqual(list(self.inbox.iterdir()), [existing])

    def test_concurrent_submissions_preserve_existing_messages(self) -> None:
        self.inbox.mkdir(parents=True)
        existing = self.inbox / "existing.json"
        existing.write_bytes(b"preserve exact evidence\n")
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            results = list(executor.map(
                lambda number: self.submit("example", "regression", "status",
                                           body=f"message {number}".encode()),
                range(24),
            ))
        self.assertTrue(all(result.returncode == 0 for result in results),
                        [result.stderr for result in results])
        identifiers = {json.loads(result.stdout)["message_id"] for result in results}
        self.assertEqual(len(identifiers), 24)
        self.assertEqual(existing.read_bytes(), b"preserve exact evidence\n")
        messages = [json.loads((self.inbox / f"{identifier}.json").read_text())
                    for identifier in identifiers]
        self.assertEqual({message["body"] for message in messages},
                         {f"message {number}" for number in range(24)})
        self.assertEqual(len(list(self.inbox.iterdir())), 25)

    def test_symlinked_runtime_directories_cannot_escape_checkout(self) -> None:
        for location in (".ace", ".ace/inbox"):
            with self.subTest(location=location):
                outside = pathlib.Path(self.temporary.name) / location.replace("/", "-")
                outside.mkdir()
                link = self.checkout / location
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(outside, target_is_directory=True)
                result = self.submit("example", "regression", "done")
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(list(outside.iterdir()), [])
                link.unlink()


if __name__ == "__main__":
    unittest.main()
