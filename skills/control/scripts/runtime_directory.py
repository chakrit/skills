"""Open confined directories under control's gitignored .ace runtime root."""

from contextlib import contextmanager
import os
from pathlib import Path
import stat
from typing import Iterator


DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


@contextmanager
def runtime_directory(repository: Path, name: str) -> Iterator[int]:
    """Yield a descriptor for repository/.ace/NAME, refusing symlinks on the way."""
    repository_fd = os.open(repository, DIRECTORY_FLAGS)
    try:
        runtime_fd = child(repository_fd, ".ace")
        try:
            directory_fd = child(runtime_fd, name)
            try:
                yield directory_fd
            finally:
                os.close(directory_fd)
        finally:
            os.close(runtime_fd)
    finally:
        os.close(repository_fd)


def child(parent_fd: int, name: str) -> int:
    try:
        os.mkdir(name, 0o700, dir_fd=parent_fd)
    except FileExistsError:
        existing = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if not stat.S_ISDIR(existing.st_mode):
            raise ValueError(f"runtime path {name} must be a real directory")

    return os.open(name, DIRECTORY_FLAGS, dir_fd=parent_fd)
