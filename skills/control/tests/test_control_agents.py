"""Registry lookup and pane checks of scripts/control-agents; no live tmux."""

from datetime import datetime, timezone
from pathlib import Path
import runpy
from types import SimpleNamespace
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "control-agents"
agents = SimpleNamespace(**runpy.run_path(str(SCRIPT)))

HOME = Path("/home/chakrit")
DOCUMENTS = HOME / "Documents"
REGISTRY = """# Projects

| Project | Checkout | Window | Agent pane | Backend | Assignment |
| ------- | -------- | ------ | ---------- | ------- | ---------- |
| web     | web      | @3     | %7         | claude  | login page |
| api-v2  | api      | @4     | %9         | codex   |            |
"""
WEB = agents.Agent("web", DOCUMENTS / "acme/web", "@3", "%7")


class RegistryTest(unittest.TestCase):
    def test_machine_control_reads_orgs_relative_to_documents(self) -> None:
        self.assertEqual(agents.registry(DOCUMENTS / "control", HOME),
                         (DOCUMENTS / "control/registries/orgs.md", DOCUMENTS))

    def test_org_control_reads_projects_relative_to_its_org(self) -> None:
        self.assertEqual(agents.registry(DOCUMENTS / "acme/control", HOME),
                         (DOCUMENTS / "acme/control/registries/projects.md",
                          DOCUMENTS / "acme"))

    def test_other_folders_are_refused(self) -> None:
        for repository in (DOCUMENTS / "acme/web", DOCUMENTS / "acme/x/control",
                           HOME / "control", DOCUMENTS / "control/control"):
            with self.subTest(repository=repository):
                with self.assertRaises(ValueError):
                    agents.registry(repository, HOME)

    def test_parse_reads_slug_rows_only(self) -> None:
        parsed = agents.parse(REGISTRY, DOCUMENTS / "acme")

        self.assertEqual(parsed, {
            "web": WEB,
            "api-v2": agents.Agent("api-v2", DOCUMENTS / "acme/api", "@4", "%9"),
        })

    def test_parse_refuses_targets_that_are_not_tmux_ids(self) -> None:
        for row in ("| web | web | main:1 | %7 | claude | |",
                    "| web | web | @3 | main:1.0 | claude | |",
                    "| web | web | @3 | | claude | |",
                    "| web | ../other | @3 | %7 | claude | |",
                    "| web | /etc | @3 | %7 | claude | |",
                    "| web | a/.. | @3 | %7 | claude | |"):
            with self.subTest(row=row):
                with self.assertRaises(ValueError):
                    agents.parse(row, DOCUMENTS / "acme")


class PaneTest(unittest.TestCase):
    def test_registered_live_harness_pane_passes(self) -> None:
        agents.check_pane(WEB, f"@3\t{DOCUMENTS}/acme/web\tclaude\t0\n")

    def test_mismatched_panes_are_refused(self) -> None:
        for info in (f"@3\t{DOCUMENTS}/acme/web\tclaude\t1",
                     f"@8\t{DOCUMENTS}/acme/web\tclaude\t0",
                     f"@3\t{DOCUMENTS}/acme/api\tclaude\t0",
                     f"@3\t{DOCUMENTS}/acme/web\tzsh\t0"):
            with self.subTest(info=info):
                with self.assertRaises(ValueError):
                    agents.check_pane(WEB, info)

    def test_pane_someone_is_viewing_is_refused(self) -> None:
        with self.assertRaises(ValueError):
            agents.check_unwatched(WEB, "%2\n%7\n")
        agents.check_unwatched(WEB, "%2\n%17\n")


class SessionNameTest(unittest.TestCase):
    def test_only_agent_names_pass(self) -> None:
        for name in ("lz49:control", "lz49:acme:control", "lz49:acme:web-v2"):
            agents.check_session_name(name)
        for name in ("web", "lz49:acme:web:extra", "Lz49:control", "lz49:control\n/exit"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    agents.check_session_name(name)


class ClearRecordTest(unittest.TestCase):
    NOW = datetime(2026, 11, 5, 9, 30, tzinfo=timezone.utc)

    UNPRINTABLE = ("", "   ", "engram #1\n/exit", "a\tb", "engram\x1b[2J")

    def test_saved_record_names_time_agent_and_save_location(self) -> None:
        self.assertEqual(
            agents.saved_clear_record(WEB, "engram acme-web #412", self.NOW),
            "2026-11-05T09:30:00+00:00\tweb\tsaved\tengram acme-web #412\n")

    def test_save_location_must_be_one_printed_line(self) -> None:
        for location in self.UNPRINTABLE:
            with self.subTest(location=location):
                with self.assertRaises(ValueError):
                    agents.saved_clear_record(WEB, location, self.NOW)

    def test_forced_record_names_time_agent_and_reason(self) -> None:
        self.assertEqual(
            agents.forced_clear_record(WEB, "chakrit: 'clear web, no save'", self.NOW),
            "2026-11-05T09:30:00+00:00\tweb\tforced\tchakrit: 'clear web, no save'\n")

    def test_reason_must_be_one_printed_line(self) -> None:
        for reason in self.UNPRINTABLE:
            with self.subTest(reason=reason):
                with self.assertRaises(ValueError):
                    agents.forced_clear_record(WEB, reason, self.NOW)


if __name__ == "__main__":
    unittest.main()
