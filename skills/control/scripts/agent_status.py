"""Own each agent's single current-state record under control/.ace/status."""

from contextlib import contextmanager
from dataclasses import asdict, dataclass, replace
import datetime
import enum
import fcntl
import json
import os
from pathlib import Path
import re
from typing import Callable, Iterator, Sequence
import uuid

from runtime_directory import runtime_directory


# An observation threshold for flagging silent records, not a timeout on agents.
STALE_AFTER = datetime.timedelta(minutes=15)
# Task value of a record control created without knowing the agent's task.
NO_TASK = "-"
SUMMARY_LIMIT = 200
# The reader keeps every table line within TABLE_WIDTH terminal columns.
TABLE_WIDTH = 160
SUMMARY_COLUMN = 40
SUBAGENT_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")


class State(str, enum.Enum):
    IDLE = "idle"
    WORKING = "working"
    WAITING_USER = "waiting-user"
    BLOCKED = "blocked"
    DONE = "done"


class Context(str, enum.Enum):
    UNSAVED = "unsaved"
    SAVED = "saved"
    CLEARED = "cleared"


class SubagentState(str, enum.Enum):
    RUNNING = "running"
    DONE = "done"


@dataclass(frozen=True)
class Subagent:
    id: str
    description: str
    state: SubagentState
    updated_at: str

    @classmethod
    def parse(cls, raw: object) -> "Subagent":
        if not isinstance(raw, dict) or set(raw) != FIELDS[cls]:
            raise ValueError("malformed subagent entry")

        return cls(subagent_id(raw["id"]), one_line(raw["description"], "description"),
                   SubagentState(raw["state"]), timestamp(raw["updated_at"]))


@dataclass(frozen=True)
class Status:
    slug: str
    task: str
    state: State
    summary: str
    context: Context
    updated_at: str
    subagents: tuple[Subagent, ...]

    @classmethod
    def parse(cls, raw: object) -> "Status":
        if not isinstance(raw, dict) or set(raw) != FIELDS[cls]:
            raise ValueError("malformed status record fields")
        if not isinstance(raw["slug"], str) or not isinstance(raw["task"], str):
            raise ValueError("malformed status record identity")
        if not isinstance(raw["subagents"], list):
            raise ValueError("malformed status record subagents")

        return cls(raw["slug"], raw["task"], State(raw["state"]),
                   one_line(raw["summary"], "summary"), Context(raw["context"]),
                   timestamp(raw["updated_at"]),
                   tuple(Subagent.parse(entry) for entry in raw["subagents"]))

    def running(self) -> tuple[Subagent, ...]:
        return tuple(entry for entry in self.subagents
                     if entry.state is SubagentState.RUNNING)


@dataclass(frozen=True)
class Invalid:
    """A record file that exists but cannot be read as a status record."""
    reason: str


Entry = Status | Invalid | None
FIELDS = {Subagent: {"id", "description", "state", "updated_at"},
          Status: {"slug", "task", "state", "summary", "context", "updated_at",
                   "subagents"}}


def report_state(previous: Status | None, slug: str, state: State, summary: str,
                 task: str | None, context: Context | None,
                 now: datetime.datetime) -> Status:
    """Overwrite state and summary, keeping task, context and subagents unless given.

    A new task keeps only subagents still running; finished ones belonged to the old task.
    """
    if task is None and (previous is None or previous.task == NO_TASK):
        raise ValueError("--task is required when the record names no current task")

    current_task = task if task is not None else previous.task
    previous_context = previous.context if previous is not None else Context.UNSAVED
    current_context = context if context is not None else previous_context
    kept = previous.subagents if previous is not None else ()
    subagents = previous.running() if task_changed(previous, current_task) else kept

    return Status(slug, current_task, state, one_line(summary, "summary"), current_context,
                  stamp(now), subagents)


def report_cleared(previous: Status | None, slug: str, now: datetime.datetime) -> Status:
    """Record control's context clear: idle and cleared, keeping task and subagents."""
    task = previous.task if previous is not None else NO_TASK
    subagents = previous.subagents if previous is not None else ()

    return Status(slug, task, State.IDLE, "Context cleared by control", Context.CLEARED,
                  stamp(now), subagents)


def task_changed(previous: Status | None, task: str) -> bool:
    return previous is not None and previous.task != task


def report_subagent(previous: Status | None, identifier: str, state: SubagentState,
                    description: str | None, now: datetime.datetime) -> Status:
    """Insert or update one subagent entry; a new ID must carry a description."""
    if previous is None:
        raise ValueError("set a status record before reporting subagents")
    subagent_id(identifier)
    existing = {entry.id: entry for entry in previous.subagents}
    if identifier not in existing and description is None:
        raise ValueError(f"subagent {identifier} needs a description on first report")

    known = existing.get(identifier)
    text = (one_line(description, "description") if description is not None
            else known.description)
    entry = Subagent(identifier, text, state, stamp(now))
    subagents = (tuple(entry if item.id == identifier else item
                       for item in previous.subagents)
                 if known is not None else (*previous.subagents, entry))

    return replace(previous, updated_at=stamp(now), subagents=subagents)


def is_stale(status: Status, now: datetime.datetime,
             threshold: datetime.timedelta) -> bool:
    if status.state in (State.IDLE, State.DONE):
        return False
    active = status.state is State.WORKING or bool(status.running())

    return active and age(status, now) > threshold


def age(status: Status, now: datetime.datetime) -> datetime.timedelta:
    return now - datetime.datetime.fromisoformat(status.updated_at)


def render(rows: Sequence[tuple[str, Entry]], now: datetime.datetime,
           threshold: datetime.timedelta) -> str:
    """Align columns; truncate SUMMARY and then SUBAGENTS so lines fit TABLE_WIDTH."""
    header = ("SLUG", "TASK", "STATE", "CONTEXT", "AGE", "FLAG", "SUMMARY", "SUBAGENTS")
    lines = (header, *(row_cells(slug, entry, now, threshold) for slug, entry in rows))
    fitted = tuple((*line[:6], truncate(line[6], SUMMARY_COLUMN), line[7]) for line in lines)
    widths = tuple(max(len(line[column]) for line in fitted)
                   for column in range(len(header) - 1))
    remaining = max(len(header[-1]), TABLE_WIDTH - sum(widths) - 2 * len(widths))

    return "\n".join("  ".join((*(cell.ljust(width) for cell, width in zip(line, widths)),
                                truncate(line[-1], remaining))).rstrip()
                     for line in fitted) + "\n"


def truncate(text: str, width: int) -> str:
    return text if len(text) <= width else text[:width - 1] + "…"


def row_cells(slug: str, entry: Entry, now: datetime.datetime,
              threshold: datetime.timedelta) -> tuple[str, ...]:
    if entry is None:
        return (slug, "-", "no-record", "-", "-", "-", "-", "-")
    if isinstance(entry, Invalid):
        return (slug, "-", "invalid", "-", "-", "-", "-", entry.reason)

    flag = "STALE" if is_stale(entry, now, threshold) else "-"
    return (slug, entry.task, entry.state.value, entry.context.value,
            duration(age(entry, now)), flag, entry.summary,
            subagent_summary(entry.subagents))


def subagent_summary(subagents: tuple[Subagent, ...]) -> str:
    groups = tuple(
        f"{state.value}: " + ", ".join(f"{entry.id} ({entry.description})"
                                       for entry in subagents if entry.state is state)
        for state in SubagentState
        if any(entry.state is state for entry in subagents))

    return "; ".join(groups) if groups else "-"


def duration(elapsed: datetime.timedelta) -> str:
    seconds = max(0, int(elapsed.total_seconds()))
    minutes, hours, days = seconds // 60, seconds // 3600, seconds // 86400
    if seconds < 60:
        return f"{seconds}s"
    if minutes < 60:
        return f"{minutes}m"
    if hours < 24:
        return f"{hours}h{minutes % 60:02d}m"

    return f"{days}d{hours % 24:02d}h"


class Records:
    """Own reads and atomic replacement of .ace/status/SLUG.json under a per-slug lock."""

    def __init__(self, repository: Path) -> None:
        self.repository = repository

    def read(self, slug: str) -> Status | None:
        with runtime_directory(self.repository, "status") as directory:
            return self.load(directory, slug)

    def observe(self, slug: str) -> Entry:
        """Read for display, reporting an unreadable record instead of failing the table."""
        try:
            return self.read(slug)
        except (OSError, ValueError) as error:
            return Invalid(str(error))

    def update(self, slug: str, change: Callable[[Status | None], Status]
               ) -> tuple[Status | None, Status]:
        """Apply CHANGE under the lock; return the previous and the written record."""
        with runtime_directory(self.repository, "status") as directory, \
                self.lock(directory, slug):
            previous = self.load(directory, slug)
            status = change(previous)
            if status.slug != slug:
                raise ValueError("status record slug does not match its file")
            self.write(directory, status)

        return previous, status

    def load(self, directory: int, slug: str) -> Status | None:
        try:
            descriptor = os.open(f"{slug}.json", os.O_RDONLY | os.O_NOFOLLOW,
                                 dir_fd=directory)
        except FileNotFoundError:
            return None
        with os.fdopen(descriptor, "r", encoding="utf-8") as stream:
            status = Status.parse(json.load(stream))
        if status.slug != slug:
            raise ValueError("status record slug does not match its file")

        return status

    @contextmanager
    def lock(self, directory: int, slug: str) -> Iterator[None]:
        descriptor = os.open(f"{slug}.lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW,
                             0o600, dir_fd=directory)
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            yield
        finally:
            os.close(descriptor)

    def write(self, directory: int, status: Status) -> None:
        content = (json.dumps(asdict(status), ensure_ascii=False, indent=2) + "\n")
        temporary = f".{status.slug}.{uuid.uuid4()}.pending"
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                             0o600, dir_fd=directory)
        published = False
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            # Rename replaces the name itself, so readers see the old or new record whole.
            os.replace(temporary, f"{status.slug}.json",
                       src_dir_fd=directory, dst_dir_fd=directory)
            published = True
        finally:
            if not published:
                os.unlink(temporary, dir_fd=directory)


def one_line(text: object, name: str) -> str:
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f"{name} must contain text")
    if len(text.splitlines()) != 1 or any(ord(char) < 32 or ord(char) == 127
                                          for char in text):
        raise ValueError(f"{name} must be one line without control characters")
    if len(text) > SUMMARY_LIMIT:
        raise ValueError(f"{name} must be at most {SUMMARY_LIMIT} characters")

    return text


def subagent_id(identifier: object) -> str:
    if not isinstance(identifier, str) or not SUBAGENT_ID.fullmatch(identifier):
        raise ValueError("subagent ID must be 1-64 letters, digits, dots, hyphens "
                         "or underscores")

    return identifier


def timestamp(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("malformed status timestamp")
    parsed = datetime.datetime.fromisoformat(value)
    if parsed.utcoffset() != datetime.timedelta(0):
        raise ValueError("status timestamps must be UTC")

    return value


def stamp(now: datetime.datetime) -> str:
    return now.astimezone(datetime.timezone.utc).isoformat(timespec="seconds")
