"""Pane lookup and pane checks of scripts/control-agents; no live tmux."""

from datetime import datetime, timezone
from pathlib import Path
import runpy
from types import SimpleNamespace
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "control-agents"
agents = SimpleNamespace(**runpy.run_path(str(SCRIPT)))

HOME = Path("/home/chakrit")
DOCUMENTS = HOME / "Documents"
MACHINE = agents.MachineControl("lz49", DOCUMENTS)
ACME = agents.OrgControl("lz49", DOCUMENTS / "acme")
# `tmux list-panes -a -F '#{pane_id}\t#{@agent}'`; an untagged pane prints an empty name.
PANES = agents.parse_tagged("%1\t\n"
                            "%7\tlz49:acme:web\n"
                            "%9\tlz49:acme:api-v2\n"
                            "%3\tlz49:acme:control\n"
                            "%6\tlz49:control\n"
                            "%4\tlz49:other:web\n"
                            "%5\tgz44:acme:web\n"
                            "%8\tlz49:acme:docs:extra\n")
WEB = agents.Agent("web", DOCUMENTS / "acme/web", "%7")


class ScopeTest(unittest.TestCase):
    def test_machine_control_manages_org_controls(self) -> None:
        self.assertEqual(agents.control_scope(DOCUMENTS / "control", HOME, "lz49"),
                         MACHINE)

    def test_org_control_manages_its_org_projects(self) -> None:
        self.assertEqual(agents.control_scope(DOCUMENTS / "acme/control", HOME, "lz49"),
                         ACME)

    def test_other_folders_are_refused(self) -> None:
        for repository in (DOCUMENTS / "acme/web", DOCUMENTS / "acme/x/control",
                           HOME / "control", DOCUMENTS / "control/control"):
            with self.subTest(repository=repository):
                with self.assertRaises(ValueError):
                    agents.control_scope(repository, HOME, "lz49")

    def test_slug_gives_the_agent_name_and_folder(self) -> None:
        self.assertEqual((MACHINE.name("acme"), MACHINE.folder("acme")),
                         ("lz49:acme:control", DOCUMENTS / "acme/control"))
        self.assertEqual((ACME.name("web"), ACME.folder("web")),
                         ("lz49:acme:web", DOCUMENTS / "acme/web"))


class FindAgentTest(unittest.TestCase):
    def test_the_one_tagged_pane_is_found(self) -> None:
        self.assertEqual(agents.find_agent(ACME, "web", PANES), WEB)
        self.assertEqual(agents.find_agent(MACHINE, "acme", PANES),
                         agents.Agent("acme", DOCUMENTS / "acme/control", "%3"))

    def test_untagged_agent_is_refused_with_the_tagging_command(self) -> None:
        with self.assertRaisesRegex(
                ValueError, "^docs: no pane is tagged @agent lz49:acme:docs; tag the "
                            "agent's pane with `tmux set-option -p -t <pane> @agent "
                            "lz49:acme:docs`$"):
            agents.find_agent(ACME, "docs", PANES)

    def test_name_on_several_panes_is_refused_naming_them(self) -> None:
        doubled = PANES + agents.parse_tagged("%12\tlz49:acme:web\n")
        with self.assertRaisesRegex(ValueError, "^web: .*%7.*%12"):
            agents.find_agent(ACME, "web", doubled)

    def test_slugs_that_are_not_managed_agents_are_refused(self) -> None:
        for slug in ("", "Web", "../web", "web:x", "-web", "control"):
            with self.subTest(slug=slug):
                with self.assertRaisesRegex(ValueError, "not a slug"):
                    agents.find_agent(ACME, slug, PANES)


class ListingTest(unittest.TestCase):
    def test_org_control_lists_its_tagged_projects(self) -> None:
        self.assertEqual(agents.listing(ACME, PANES),
                         f"web\t%7\t{DOCUMENTS}/acme/web\n"
                         f"api-v2\t%9\t{DOCUMENTS}/acme/api-v2\n")

    def test_machine_control_lists_its_tagged_org_controls(self) -> None:
        self.assertEqual(agents.listing(MACHINE, PANES),
                         f"acme\t%3\t{DOCUMENTS}/acme/control\n")


class PaneTest(unittest.TestCase):
    def test_live_pane_in_the_agent_folder_returns_its_shell_pid(self) -> None:
        self.assertEqual(agents.check_pane(WEB, f"{DOCUMENTS}/acme/web\t0\t4100\n"), 4100)

    def test_mismatched_panes_are_refused(self) -> None:
        for info in (f"{DOCUMENTS}/acme/web\t1\t4100", f"{DOCUMENTS}/acme/api\t0\t4100"):
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


class InspectionTest(unittest.TestCase):
    """`send` refuses a pane that printed since the control's last `inspect`."""

    SEEN = {"web": agents.Inspection("%7", 1762594200)}

    def test_inspections_round_trip_one_line_per_slug(self) -> None:
        text = "api-v2\t%9\t1762594100\nweb\t%7\t1762594200\n"
        parsed = agents.parse_inspections(text)

        self.assertEqual(parsed, {"api-v2": agents.Inspection("%9", 1762594100),
                                  "web": agents.Inspection("%7", 1762594200)})
        self.assertEqual(agents.inspections_text(parsed), text)

    def test_malformed_inspection_lines_are_refused(self) -> None:
        for line in ("web\t%7", "web\t@3\t1762594200", "Web\t%7\t1762594200",
                     "web\t%7\tnow", "web\t%7\t-1", "web\t%7\t1\textra"):
            with self.subTest(line=line):
                with self.assertRaisesRegex(ValueError, agents.INSPECTIONS):
                    agents.parse_inspections(line + "\n")

    def test_output_time_must_be_a_tmux_timestamp(self) -> None:
        self.assertEqual(agents.parse_output_time(WEB, "1762594200\n"), 1762594200)
        for text in ("", "\n", "soon\n", "-5\n"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    agents.parse_output_time(WEB, text)

    def test_pane_quiet_since_its_inspect_passes(self) -> None:
        for output_time in (1762594100, 1762594200):
            with self.subTest(output_time=output_time):
                agents.check_inspected(WEB, self.SEEN, output_time)

    def test_pane_never_inspected_is_refused(self) -> None:
        for seen in ({}, {"api-v2": agents.Inspection("%9", 1762594200)},
                     {"web": agents.Inspection("%12", 1762594200)}):
            with self.subTest(seen=seen):
                with self.assertRaisesRegex(ValueError, "inspect web.*retry"):
                    agents.check_inspected(WEB, seen, 1762594200)

    def test_pane_that_printed_since_its_inspect_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "printed since.*inspect web again.*retry"):
            agents.check_inspected(WEB, self.SEEN, 1762594201)


if __name__ == "__main__":
    unittest.main()
