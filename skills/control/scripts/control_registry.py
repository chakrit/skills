"""Read registered project identities and task identifiers from durable control records."""

import pathlib
import re
from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping

from control_config import Config


@dataclass(frozen=True)
class Project:
    slug: str
    checkout: pathlib.Path
    window: str
    agent_pane: str
    backend: str


def load_projects(config: Config) -> Mapping[str, Project]:
    text = config.projects_registry.read_text(encoding="utf-8")

    rows = re.findall(r"^\|\s*([a-z][a-z0-9-]*)\s*\|([^\n]+)\|\s*$", text, re.M)
    projects = tuple(project(config.root, slug, columns) for slug, columns in rows)
    index = {entry.slug: entry for entry in projects}
    if not index or len(index) != len(projects):
        raise ValueError("project registry is empty or has duplicate identifiers")

    return MappingProxyType(index)


def project(root: pathlib.Path, slug: str, columns: str) -> Project:
    fields = tuple(column.strip() for column in columns.split("|"))
    if len(fields) != 5:
        raise ValueError(f"invalid project registry row for {slug}")
    checkout, window, agent_pane, backend, _assignment = fields
    path = pathlib.Path(checkout)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"invalid relative checkout for {slug}")
    if not re.fullmatch(r"@\d+", window):
        raise ValueError(f"invalid window identifier for {slug}")
    if not re.fullmatch(r"%\d+", agent_pane):
        raise ValueError(f"invalid pane identifier for {slug}")

    return Project(slug, root / path, window, agent_pane, backend)


def load_task_ids(config: Config) -> frozenset[str]:
    text = config.tasks_registry.read_text(encoding="utf-8")

    tasks = frozenset(re.findall(r"^## ([a-z][a-z0-9-]*) — ", text, re.M))
    if not tasks:
        raise ValueError("task registry is empty or malformed")

    return tasks
