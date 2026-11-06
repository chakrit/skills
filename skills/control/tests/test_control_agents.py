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

| Project | Checkout | Window | Agent pane |
| ------- | -------- | ------ | ---------- |
| web     | web      | @3     | %7         |
| api-v2  | api      | @4     | %9         |
| docs    | docs     |        |            |
"""
WEB = agents.Agent("web", DOCUMENTS / "acme/web", "@3", "%7")
DOCS = agents.Agent("docs", DOCUMENTS / "acme/docs", "", "")


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
            "docs": DOCS,
        })

    def test_parse_refuses_targets_that_are_not_tmux_ids(self) -> None:
        for row in ("| web | web | main:1 | %7 |",
                    "| web | web | @3 | main:1.0 |",
                    "| web | web | @3 | |",
                    "| web | web | | %7 |",
                    "| web | ../other | @3 | %7 |",
                    "| web | /etc | @3 | %7 |",
                    "| web | a/.. | @3 | %7 |",
                    "| web | ../other | | |"):
            with self.subTest(row=row):
                with self.assertRaises(ValueError):
                    agents.parse(row, DOCUMENTS / "acme")


class ListingTest(unittest.TestCase):
    def test_listing_marks_agents_with_no_pane_recorded(self) -> None:
        self.assertEqual(
            agents.listing({"web": WEB, "docs": DOCS}),
            f"web\t@3\t%7\t{DOCUMENTS}/acme/web\n"
            f"docs\t-\t-\t{DOCUMENTS}/acme/docs\tno pane recorded\n")


class RecordedPaneTest(unittest.TestCase):
    def test_agent_with_a_recorded_pane_is_returned(self) -> None:
        self.assertEqual(agents.recorded_pane(WEB), WEB)

    def test_agent_with_no_pane_recorded_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "docs has no pane recorded"):
            agents.recorded_pane(DOCS)


class PaneTest(unittest.TestCase):
    def test_registered_live_pane_returns_its_shell_pid(self) -> None:
        self.assertEqual(agents.check_pane(WEB, f"@3\t{DOCUMENTS}/acme/web\t0\t4100\n"),
                         4100)

    def test_mismatched_panes_are_refused(self) -> None:
        for info in (f"@3\t{DOCUMENTS}/acme/web\t1\t4100",
                     f"@8\t{DOCUMENTS}/acme/web\t0\t4100",
                     f"@3\t{DOCUMENTS}/acme/api\t0\t4100"):
            with self.subTest(info=info):
                with self.assertRaises(ValueError):
                    agents.check_pane(WEB, info)

    def test_pane_someone_is_viewing_is_refused(self) -> None:
        with self.assertRaises(ValueError):
            agents.check_unwatched(WEB, "%2\n%7\n")
        agents.check_unwatched(WEB, "%2\n%17\n")


class ForegroundTest(unittest.TestCase):
    def test_shell_holds_foreground_when_it_leads_the_terminal_group(self) -> None:
        self.assertTrue(agents.shell_holds_foreground(4100, " 4100\n"))

    def test_program_holds_foreground_when_another_group_leads(self) -> None:
        self.assertFalse(agents.shell_holds_foreground(4100, " 4188\n"))


class DraftTest(unittest.TestCase):
    """A paste joins whatever the agent's prompt already holds; see docs/spec/control.md
    "Script"."""

    def test_empty_prompts_pass(self) -> None:
        for line, cursor_x in (("❯", 2), ("│ >                        │", 4),
                               ("› Ask Codex to do anything", 2), ("", 0)):
            with self.subTest(line=line):
                agents.check_no_draft(WEB, cursor_x, line)

    def test_prompt_holding_typed_input_is_refused(self) -> None:
        for line, cursor_x in (("❯ fix the login bug", 19), ("│ > hello        │", 9),
                               ("❯ 42", 4), ("› ok Ask Codex", 4)):
            with self.subTest(line=line):
                with self.assertRaisesRegex(ValueError, "typed input"):
                    agents.check_no_draft(WEB, cursor_x, line)


class SessionNameTest(unittest.TestCase):
    def test_only_agent_names_pass(self) -> None:
        for name in ("lz49:control", "lz49:acme:control", "lz49:acme:web-v2"):
            agents.check_session_name(name)
        for name in ("web", "lz49:acme:web:extra", "Lz49:control", "lz49:control\n/quit"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    agents.check_session_name(name)


class ClearRecordTest(unittest.TestCase):
    NOW = datetime(2026, 11, 5, 9, 30, tzinfo=timezone.utc)

    UNPRINTABLE = ("", "   ", "engram #1\n/exit", "a\tb", "engram\x1b[2J")

    def test_record_names_time_agent_kind_and_detail(self) -> None:
        for kind, detail in (("saved", "engram acme-web #412"),
                             ("wind-down", "engram acme-web #413"),
                             ("forced", "chakrit: 'clear web, no save'")):
            with self.subTest(kind=kind):
                self.assertEqual(agents.clear_record(self.NOW, WEB, kind, detail),
                                 f"2026-11-05T09:30:00+00:00\tweb\t{kind}\t{detail}\n")

    def test_detail_must_be_one_printed_line(self) -> None:
        for kind, hint in (("saved", "--saved"), ("wind-down", "--saved"),
                           ("forced", "--ruling")):
            for detail in self.UNPRINTABLE:
                with self.subTest(kind=kind, detail=detail):
                    with self.assertRaisesRegex(ValueError, hint):
                        agents.clear_record(self.NOW, WEB, kind, detail)


if __name__ == "__main__":
    unittest.main()
