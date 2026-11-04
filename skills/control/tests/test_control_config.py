"""Exercise control.toml parsing: levels, agent names and loud refusal of bad keys."""

from pathlib import Path
import sys
import tempfile
import tomllib
import unittest

from config_fixture import config_text


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import control_config

REPOSITORY = Path("/synthetic/repository")
MACHINE = {"level": "machine", "machine": "lz49", "principal": "tester",
           "root": "/synthetic", "harness": ["ace"], "tmux_socket": "/synthetic/socket",
           "tmux_session": "main"}
ORG = {**MACHINE, "level": "org", "org": "datawow", "parent": "/synthetic/control"}
PROJECT = {**ORG, "level": "project", "project": "cookiewow",
           "parent": "/synthetic/datawow/control"}


def parse(raw: dict) -> control_config.Config:
    return control_config.parse(REPOSITORY, raw)


class LevelTests(unittest.TestCase):
    def test_each_level_derives_its_agent_name_and_sender(self) -> None:
        cases = ((MACHINE, "lz49:control"), (ORG, "lz49:datawow:control"),
                 (PROJECT, "lz49:datawow:cookiewow"))
        for raw, agent in cases:
            with self.subTest(level=raw["level"]):
                config = parse(raw)
                self.assertEqual(config.agent, agent)
                self.assertEqual(config.sender.splitlines()[0],
                                 f"FROM: {agent} ({REPOSITORY}), acting under tester's "
                                 "delegated authority.")

    def test_keys_of_another_level_are_refused(self) -> None:
        cases = (({**MACHINE, "org": "datawow"}, "org"),
                 ({**MACHINE, "parent": "/synthetic/control"}, "parent"),
                 ({**ORG, "project": "cookiewow"}, "project"))
        for raw, key in cases:
            with self.subTest(key=key, level=raw["level"]):
                with self.assertRaisesRegex(ValueError, f"{key} does not apply"):
                    parse(raw)

    def test_unknown_level_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "level must be one of"):
            parse({**MACHINE, "level": "team"})


class RequiredKeyTests(unittest.TestCase):
    def test_every_required_key_is_named_when_missing(self) -> None:
        for raw in (MACHINE, ORG, PROJECT):
            for key in raw:
                with self.subTest(level=raw["level"], key=key):
                    incomplete = {name: value for name, value in raw.items() if name != key}
                    with self.assertRaisesRegex(ValueError, f"missing required key {key}"):
                        parse(incomplete)

    def test_malformed_values_are_refused_with_the_key_name(self) -> None:
        cases = (("machine", "LZ49"), ("org", "data wow"), ("root", "relative/path"),
                 ("parent", "/synthetic/../escape"), ("tmux_socket", "default"),
                 ("principal", " "), ("principal", "two\nlines"), ("harness", []),
                 ("harness", "ace"), ("harness", ["ace", ""]), ("tmux_session", 3),
                 ("sort_prefixes", "D"), ("projects_registry", "/etc/projects.md"),
                 ("tasks_registry", "../tasks.md"))
        for key, value in cases:
            with self.subTest(key=key, value=value):
                with self.assertRaisesRegex(ValueError, key):
                    parse({**ORG, key: value})

    def test_unknown_keys_are_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown keys: harnesses"):
            parse({**ORG, "harnesses": ["ace"]})


class OptionalKeyTests(unittest.TestCase):
    def test_registries_default_inside_the_repository_and_can_move(self) -> None:
        default = parse(ORG)
        self.assertEqual((default.projects_registry, default.tasks_registry),
                         (REPOSITORY / "registries/projects.md", REPOSITORY / "tasks.md"))
        moved = parse({**ORG, "projects_registry": "registries/orgs.md",
                       "tasks_registry": "ledger/tasks.md"})
        self.assertEqual((moved.projects_registry, moved.tasks_registry),
                         (REPOSITORY / "registries/orgs.md", REPOSITORY / "ledger/tasks.md"))

    def test_sort_prefixes_and_exit_confirmation_are_optional(self) -> None:
        config = parse(ORG)
        self.assertEqual((config.sort_prefixes, config.exit_confirmation), ((), None))

    def test_exit_confirmation_needs_exactly_its_four_keys(self) -> None:
        complete = {"notice": "n", "footer": "f", "marker": ">", "option": "o"}
        parsed = parse({**ORG, "exit_confirmation": complete}).exit_confirmation
        self.assertEqual(parsed, control_config.ExitConfirmation("n", "f", ">", "o"))
        for table in ({"notice": "n", "footer": "f", "marker": ">"},
                      {**complete, "extra": "x"}, {**complete, "footer": ""}):
            with self.subTest(table=table):
                with self.assertRaisesRegex(ValueError, "exit_confirmation"):
                    parse({**ORG, "exit_confirmation": table})


class FileTests(unittest.TestCase):
    def test_load_reads_control_toml_at_the_repository_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            (repository / "control.toml").write_text(config_text(repository),
                                                     encoding="utf-8")
            config = control_config.load(repository)
        self.assertEqual(config.agent, "testhost:example-org:control")
        self.assertEqual(config.exit_confirmation.marker, "❯")

    def test_missing_or_invalid_file_names_the_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            with self.assertRaisesRegex(ValueError, "control.toml is missing"):
                control_config.load(repository)
            (repository / "control.toml").write_text("level = \n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, str(repository / "control.toml")):
                control_config.load(repository)

    def test_example_file_documents_every_key_and_parses(self) -> None:
        example = Path(__file__).resolve().parents[1] / "scripts/control.example.toml"
        text = example.read_text(encoding="utf-8")
        raw = tomllib.loads(text)
        self.assertEqual(parse(raw).agent, "lz49:datawow:control")
        for key in control_config.KEYS:
            with self.subTest(key=key):
                self.assertRegex(text, rf"(?m)^(# )?\[?{key}\]?( =|$)")


if __name__ == "__main__":
    unittest.main()
