"""Load this control repository's identity and environment from control.toml."""

from dataclasses import dataclass
from pathlib import Path
import re
import tomllib
from typing import Mapping


FILENAME = "control.toml"
NAME = re.compile(r"[a-z0-9][a-z0-9-]*")
DEFAULT_PROJECTS_REGISTRY = "registries/projects.md"
DEFAULT_TASKS_REGISTRY = "tasks.md"
# Keys that exist only at some levels; LEVEL_KEYS says which level admits which.
LEVEL_KEYS = {"machine": frozenset(),
              "org": frozenset({"org", "parent"}),
              "project": frozenset({"org", "project", "parent"})}
KEYS = frozenset({"level", "machine", "org", "project", "parent", "principal", "root",
                  "harness", "tmux_socket", "tmux_session", "projects_registry",
                  "tasks_registry", "sort_prefixes", "exit_confirmation"})
EXIT_CONFIRMATION_KEYS = frozenset({"notice", "footer", "marker", "option"})


@dataclass(frozen=True)
class MachineLevel:
    machine: str

    @property
    def agent(self) -> str:
        return f"{self.machine}:control"


@dataclass(frozen=True)
class OrgLevel:
    machine: str
    org: str
    parent: Path

    @property
    def agent(self) -> str:
        return f"{self.machine}:{self.org}:control"


@dataclass(frozen=True)
class ProjectLevel:
    machine: str
    org: str
    project: str
    parent: Path

    @property
    def agent(self) -> str:
        return f"{self.machine}:{self.org}:{self.project}"


Level = MachineLevel | OrgLevel | ProjectLevel


@dataclass(frozen=True)
class ExitConfirmation:
    """The harness screen that asks whether to stop background work before exiting."""
    notice: str
    footer: str
    marker: str
    option: str


@dataclass(frozen=True)
class Config:
    repository: Path
    level: Level
    principal: str
    root: Path
    harness: frozenset[str]
    tmux_socket: str
    tmux_session: str
    projects_registry: Path
    tasks_registry: Path
    sort_prefixes: tuple[str, ...]
    exit_confirmation: ExitConfirmation | None

    @property
    def agent(self) -> str:
        return self.level.agent

    @property
    def sender(self) -> str:
        return (f"FROM: {self.agent} ({self.repository}), acting under "
                f"{self.principal}'s delegated authority.\n"
                f"This message is authored by the control agent, not {self.principal}.")


def load(repository: Path) -> Config:
    path = repository / FILENAME
    try:
        with path.open("rb") as stream:
            raw = tomllib.load(stream)
    except FileNotFoundError:
        raise ValueError(f"{path} is missing; copy scripts/control.example.toml there "
                         "and fill in every key") from None
    except tomllib.TOMLDecodeError as error:
        raise ValueError(f"{path}: {error}") from error

    return parse(repository, raw)


def parse(repository: Path, raw: Mapping[str, object]) -> Config:
    unknown = sorted(set(raw) - KEYS)
    if unknown:
        raise ValueError(f"{FILENAME}: unknown keys: {', '.join(unknown)}")

    harness = strings(required(raw, "harness"), "harness")
    if not harness:
        raise ValueError(f"{FILENAME}: harness must name at least one process")

    return Config(repository, level(raw), text(raw, "principal"), absolute(raw, "root"),
                  frozenset(harness), str(absolute(raw, "tmux_socket")),
                  text(raw, "tmux_session"),
                  registry(repository, raw, "projects_registry", DEFAULT_PROJECTS_REGISTRY),
                  registry(repository, raw, "tasks_registry", DEFAULT_TASKS_REGISTRY),
                  strings(raw.get("sort_prefixes", []), "sort_prefixes"),
                  exit_confirmation(raw.get("exit_confirmation")))


def level(raw: Mapping[str, object]) -> Level:
    kind = text(raw, "level")
    if kind not in LEVEL_KEYS:
        raise ValueError(f"{FILENAME}: level must be one of {', '.join(LEVEL_KEYS)}")
    stray = sorted((LEVEL_KEYS["project"] - LEVEL_KEYS[kind]) & set(raw))
    if stray:
        raise ValueError(f"{FILENAME}: {', '.join(stray)} does not apply at level {kind}")

    machine = name(raw, "machine")
    if kind == "machine":
        return MachineLevel(machine)
    if kind == "org":
        return OrgLevel(machine, name(raw, "org"), absolute(raw, "parent"))
    return ProjectLevel(machine, name(raw, "org"), name(raw, "project"),
                        absolute(raw, "parent"))


def exit_confirmation(raw: object) -> ExitConfirmation | None:
    if raw is None:
        return None
    if not isinstance(raw, dict) or set(raw) != EXIT_CONFIRMATION_KEYS:
        raise ValueError(f"{FILENAME}: [exit_confirmation] needs exactly the keys "
                         f"{', '.join(sorted(EXIT_CONFIRMATION_KEYS))}")

    return ExitConfirmation(*(text(raw, key, "exit_confirmation.")
                              for key in ("notice", "footer", "marker", "option")))


# Field readers: each refuses a missing or malformed value with the key's name.

def required(raw: Mapping[str, object], key: str, prefix: str = "") -> object:
    if key not in raw:
        raise ValueError(f"{FILENAME}: missing required key {prefix}{key}")

    return raw[key]


def text(raw: Mapping[str, object], key: str, prefix: str = "") -> str:
    value = required(raw, key, prefix)
    if not isinstance(value, str) or not value.strip() or len(value.splitlines()) != 1:
        raise ValueError(f"{FILENAME}: {prefix}{key} must be one non-empty line of text")

    return value


def name(raw: Mapping[str, object], key: str) -> str:
    value = text(raw, key)
    if not NAME.fullmatch(value):
        raise ValueError(f"{FILENAME}: {key} must be lowercase letters, digits and hyphens")

    return value


def absolute(raw: Mapping[str, object], key: str) -> Path:
    path = Path(text(raw, key))
    if not path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{FILENAME}: {key} must be an absolute path without ..")

    return path


def registry(repository: Path, raw: Mapping[str, object], key: str, default: str) -> Path:
    path = Path(text(raw, key) if key in raw else default)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{FILENAME}: {key} must be a path inside the repository")

    return repository / path


def strings(value: object, key: str) -> tuple[str, ...]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item
                                          for item in value):
        raise ValueError(f"{FILENAME}: {key} must be a list of non-empty strings")

    return tuple(value)
