"""Write the control.toml and registries that tests of copied scripts run against."""

from pathlib import Path


AGENT = "testhost:example-org:control"
PRINCIPAL = "tester"
SOCKET = "/synthetic/socket"
EXIT_CONFIRMATION = """
[exit_confirmation]
notice = "Background work is running"
footer = "Enter to confirm · Esc to cancel"
marker = "❯"
option = "1. Exit and stop tasks"
"""


def config_text(root: Path, tables: str = EXIT_CONFIRMATION) -> str:
    return (f'level = "org"\n'
            f'machine = "testhost"\n'
            f'org = "example-org"\n'
            f'parent = "/synthetic/control"\n'
            f'principal = "{PRINCIPAL}"\n'
            f'root = "{root}"\n'
            f'harness = ["ace"]\n'
            f'tmux_socket = "{SOCKET}"\n'
            f'tmux_session = "main"\n'
            f'sort_prefixes = ["D", "a", "p", "c", "n", "f"]\n'
            + tables)


def write_control(checkout: Path, root: Path, rows: str,
                  tasks: str = "## regression — project agent\n") -> None:
    """Write control.toml, registries/projects.md with ROWS, and tasks.md."""
    (checkout / "control.toml").write_text(config_text(root), encoding="utf-8")
    registries = checkout / "registries"
    registries.mkdir(parents=True)
    (registries / "projects.md").write_text(
        "| Project | Checkout | Window | Agent | Backend | Assignment |\n"
        "| ------- | -------- | ------ | ----- | ------- | ---------- |\n" + rows,
        encoding="utf-8")
    (checkout / "tasks.md").write_text(tasks, encoding="utf-8")
