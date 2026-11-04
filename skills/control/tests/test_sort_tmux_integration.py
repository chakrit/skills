"""Opt-in contract checks against the retained isolated sorter fixture.

Supply CONTROL_SORT_TMUX_SOCKET and CONTROL_SORT_TMUX_CLIENT for an attached client
on the sorter-fixture session. The socket must be under this repository's .ace/, and
control.toml must set sort_prefixes = ["D", "a", "p", "c", "n", "f"].
These tests retain fixture sessions and panes; they never kill a tmux session.
"""

import os
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "control-sort-tmux"
SOCKET = os.environ.get("CONTROL_SORT_TMUX_SOCKET", "")
CLIENT = os.environ.get("CONTROL_SORT_TMUX_CLIENT", "")


@unittest.skipUnless(SOCKET and CLIENT, "requires explicit isolated fixture socket/client")
class IsolatedTmuxTests(unittest.TestCase):
    def run_tmux(self, *arguments: str) -> str:
        result = subprocess.run(("tmux", "-S", SOCKET, *arguments),
                                check=True, capture_output=True, text=True)
        return result.stdout.strip()

    def run_sorter(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run((str(SCRIPT), "--socket", SOCKET, "--client", CLIENT),
                              capture_output=True, text=True)

    def setUp(self) -> None:
        self.assertEqual(Path(SOCKET).resolve().parent, ROOT / ".ace")
        session = self.run_tmux("display-message", "-p", "-c", CLIENT, "#{session_name}")
        self.assertEqual(session, "sorter-fixture")
        self.control = self.run_tmux("display-message", "-p", "-c", CLIENT, "#{window_id}")
        self.pane = self.run_tmux("display-message", "-p", "-c", CLIENT, "#{pane_id}")
        self.unrelated = self.run_tmux("list-windows", "-t", "sorter-unrelated", "-F",
                                       "#{window_id}\t#{window_index}\t#{window_name}\t#{window_active}")

    def test_order_repeated_sort_focus_and_unrelated_session(self) -> None:
        last = self.run_tmux("list-windows", "-t", "sorter-fixture", "-F", "#{window_id}").splitlines()[-1]
        if last != self.control:
            self.run_tmux("swap-window", "-d", "-s", self.control, "-t", last)
            self.run_tmux("select-window", "-t", self.control)
        before_panes = self.run_tmux("list-panes", "-t", self.control, "-F", "#{pane_id}\t#{pane_active}")

        first = self.run_sorter()
        after = self.run_tmux("list-windows", "-t", "sorter-fixture", "-F", "#{window_id}\t#{window_name}")
        second = self.run_sorter()

        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(after.splitlines()[0].split("\t")[0], self.control)
        self.assertEqual(tuple(row.split("\t")[1] for row in after.splitlines()[1:]),
                         ("D/z", "a/a", "a/z", "f/z", "other"))
        self.assertEqual(after, self.run_tmux("list-windows", "-t", "sorter-fixture", "-F", "#{window_id}\t#{window_name}"))
        self.assertEqual(before_panes, self.run_tmux("list-panes", "-t", self.control, "-F", "#{pane_id}\t#{pane_active}"))
        self.assertEqual(self.unrelated, self.run_tmux("list-windows", "-t", "sorter-unrelated", "-F",
                                                      "#{window_id}\t#{window_index}\t#{window_name}\t#{window_active}"))

    def test_rename_does_not_change_control_identity(self) -> None:
        original = self.run_tmux("display-message", "-p", "-t", self.control, "#{window_name}")
        self.run_tmux("rename-window", "-t", self.control, "z/renamed-control")

        try:
            result = self.run_sorter()
            self.assertEqual(result.returncode, 0, result.stderr)
            windows = self.run_tmux("list-windows", "-t", "sorter-fixture", "-F", "#{window_id}")
            self.assertEqual(windows.splitlines()[0], self.control)
        finally:
            self.run_tmux("rename-window", "-t", self.control, original)

    def test_changed_active_pane_cwd_refuses_without_reordering(self) -> None:
        other_cwd = ROOT / ".ace" / "sorter-other-cwd"
        other_cwd.mkdir(exist_ok=True)
        panes = self.run_tmux("list-panes", "-t", self.control, "-F", "#{pane_id}\t#{pane_current_path}")
        existing = tuple(row.split("\t")[0] for row in panes.splitlines()
                         if row.split("\t")[1] == str(other_cwd))
        pane = existing[0] if existing else self.run_tmux(
            "split-window", "-d", "-P", "-F", "#{pane_id}",
            "-t", self.control, "-c", str(other_cwd), "/bin/sh")
        before = self.run_tmux("list-windows", "-t", "sorter-fixture", "-F", "#{window_id}\t#{window_index}")
        self.run_tmux("select-pane", "-t", pane)

        try:
            result = self.run_sorter()
            self.assertEqual(result.returncode, 1)
            self.assertIn("active pane", result.stderr)
            self.assertEqual(before, self.run_tmux("list-windows", "-t", "sorter-fixture", "-F", "#{window_id}\t#{window_index}"))
        finally:
            self.run_tmux("select-pane", "-t", self.pane)


if __name__ == "__main__":
    unittest.main()
