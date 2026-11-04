"""Own tmux subprocess invocation shared by control's terminal tools."""

import subprocess


class Connection:
    def __init__(self, socket: str | None) -> None:
        self.command = ("tmux", "-S", socket) if socket else ("tmux",)

    def run(self, *arguments: str, body: str | None = None) -> str:
        result = subprocess.run((*self.command, *arguments), input=body, check=True,
                                capture_output=True, text=True)

        return result.stdout
