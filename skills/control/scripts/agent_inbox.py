"""Compose and publish registered agent messages into control's fixed inbox."""

import datetime
import enum
import json
import os
from pathlib import Path
import uuid
from dataclasses import asdict, dataclass

from runtime_directory import runtime_directory


class Kind(str, enum.Enum):
    STATUS = "status"
    BLOCKER = "blocker"
    QUESTION = "question"
    DONE = "done"


@dataclass(frozen=True)
class Message:
    project: str
    task: str
    kind: Kind
    time: str
    message_id: str
    body: str


def compose(project: str, task: str, raw_kind: str, body: str,
            projects: frozenset[str], tasks: frozenset[str]) -> Message:
    if project not in projects:
        raise ValueError("project must be a registered identifier")
    if task not in tasks:
        raise ValueError("task must be a registered identifier")
    kind = Kind(raw_kind)
    if not body.strip():
        raise ValueError("message body must contain text")

    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    identifier = str(uuid.uuid4())

    return Message(project, task, kind, timestamp, identifier, body)


def publish(repository: Path, message: Message) -> None:
    content = (json.dumps(asdict(message), ensure_ascii=False) + "\n").encode("utf-8")
    filename = f"{message.message_id}.json"
    temporary = f".{message.message_id}.pending"

    with runtime_directory(repository, "inbox") as inbox_fd:
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                             0o600, dir_fd=inbox_fd)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            # Hard-link publication exposes a complete file and never replaces a name.
            os.link(temporary, filename, src_dir_fd=inbox_fd, dst_dir_fd=inbox_fd)
        finally:
            os.unlink(temporary, dir_fd=inbox_fd)


def receipt(message: Message) -> dict[str, str]:
    return {"status": "submitted", "message_id": message.message_id}
