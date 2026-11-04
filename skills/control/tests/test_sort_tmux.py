"""Contracts for control-sort-tmux ordering and client checks; no live tmux mutation."""

import importlib.machinery
import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "control-sort-tmux"
sys.path.insert(0, str(SCRIPT.parent))
loader = importlib.machinery.SourceFileLoader("sort_tmux", str(SCRIPT))
spec = importlib.util.spec_from_loader(loader.name, loader)
module = importlib.util.module_from_spec(spec)
sys.modules[loader.name] = module
loader.exec_module(module)
PRIORITIES = ("D", "a", "p", "c", "n", "f")


class OrderingTests(unittest.TestCase):
    def window(self, identity: str, index: int, name: str) -> module.Window:
        return module.Window(identity, index, name, "%1", "/project")

    def test_control_identity_precedes_reference_groups_and_names(self) -> None:
        names = ("other", "f/z", "c/a", "p/a", "n/a", "a/z", "D/z", "a/a", "D/a", "d/control")
        windows = tuple(self.window(f"@{index}", index, name) for index, name in enumerate(names))

        actual = tuple(window.name for window in module.ordered(windows, "@9", PRIORITIES))

        self.assertEqual(actual, ("d/control", "D/a", "D/z", "a/a", "a/z", "p/a", "c/a", "n/a", "f/z", "other"))

    def test_control_identity_survives_rename_and_another_control_name(self) -> None:
        windows = (self.window("@2", 1, "d/control"), self.window("@7", 5, "renamed"))

        self.assertEqual(tuple(window.identity for window in module.ordered(windows, "@7", PRIORITIES)), ("@7", "@2"))

    def test_swaps_preserve_slots_and_sort_idempotently(self) -> None:
        windows = (self.window("@1", 2, "z"), self.window("@2", 7, "a/z"), self.window("@3", 20, "control"))
        positions = {window.identity: window.index for window in windows}

        for left, right in module.swaps(windows, "@3", PRIORITIES):
            positions[left], positions[right] = positions[right], positions[left]
        after = tuple(module.Window(window.identity, positions[window.identity], window.name, window.pane, window.cwd)
                      for window in windows)

        self.assertEqual(tuple(window.identity for window in sorted(after, key=lambda window: window.index)), ("@3", "@2", "@1"))
        self.assertEqual(set(positions.values()), {2, 7, 20})
        self.assertEqual(module.swaps(after, "@3", PRIORITIES), ())

    def test_equal_names_keep_original_order(self) -> None:
        windows = (self.window("@2", 8, "a/x"), self.window("@1", 2, "a/x"), self.window("@3", 12, "control"))

        self.assertEqual(tuple(window.identity for window in module.ordered(windows, "@3", PRIORITIES)), ("@3", "@1", "@2"))

    def test_without_prefixes_control_leads_and_the_rest_sort_by_name(self) -> None:
        windows = (self.window("@1", 1, "f/z"), self.window("@2", 2, "D/a"),
                   self.window("@3", 3, "control"), self.window("@4", 4, "b"))

        actual = tuple(window.name for window in module.ordered(windows, "@3", ()))

        self.assertEqual(actual, ("control", "D/a", "b", "f/z"))


class ClientBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmux = module.Tmux(None)
        self.root = SCRIPT.parent.parent
        self.replies = ["client\t$1\nother\t$2", "0", f"@7\t{self.root}",
                        f"@7\t3\td/control\t%1\t{self.root}", "@7\n@8"]

    def test_unrelated_client_and_session_are_allowed(self) -> None:
        with patch.object(self.tmux.connection, "run", side_effect=self.replies):
            session, windows, active = self.tmux.snapshot("client", self.root)

        self.assertEqual((session, windows[0].identity, active), ("$1", "@7", "@7"))

    def test_multiple_clients_fail_closed(self) -> None:
        with patch.object(self.tmux.connection, "run", return_value="client\t$1\nother\t$1"):
            with self.assertRaisesRegex(ValueError, "multiple clients"):
                self.tmux.snapshot("client", self.root)

    def test_unknown_client_fails_closed(self) -> None:
        with patch.object(self.tmux.connection, "run", return_value="other\t$2"):
            with self.assertRaisesRegex(ValueError, "attached client"):
                self.tmux.snapshot("client", self.root)

    def test_non_control_active_pane_fails_closed(self) -> None:
        self.replies[2] = "@7\t/other"
        with patch.object(self.tmux.connection, "run", side_effect=self.replies):
            with self.assertRaisesRegex(ValueError, "active pane"):
                self.tmux.snapshot("client", self.root)

    def test_grouped_session_fails_closed(self) -> None:
        self.replies[1] = "1"
        with patch.object(self.tmux.connection, "run", side_effect=self.replies):
            with self.assertRaisesRegex(ValueError, "grouped session"):
                self.tmux.snapshot("client", self.root)

    def test_linked_window_fails_closed(self) -> None:
        self.replies[4] = "@7\n@7"
        with patch.object(self.tmux.connection, "run", side_effect=self.replies):
            with self.assertRaisesRegex(ValueError, "linked"):
                self.tmux.snapshot("client", self.root)

    def test_malformed_window_fails_closed(self) -> None:
        self.replies[3] = "@7\t3\tname\twith-tab\t%1\t/project"
        with patch.object(self.tmux.connection, "run", side_effect=self.replies):
            with self.assertRaisesRegex(ValueError, "Malformed tmux window"):
                self.tmux.snapshot("client", self.root)


if __name__ == "__main__":
    unittest.main()
