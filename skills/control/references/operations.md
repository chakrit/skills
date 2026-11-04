# Control operations

Shared procedures the setup references call. Setup writes the parts agents need daily
into their policy and instruction files; agents do not read this file after setup.

## Install scripts

1. Copy this skill's `scripts/` and `tests/` into the control repo (`scripts/`,
   `tests/`).
2. Copy `scripts/control.example.toml` to `control.toml` at the repo root and fill in
   every key for this level. Leave no example values.
3. Record the source in `scripts/SOURCE`: this skill's repo path and
   `git rev-parse --short HEAD` of that repo.
4. Run the tests: `python3 -m unittest discover -s tests`. All must pass before commit.

Project controls skip this section unless chakrit asks; they reach their parent through
messages.

The repo's copy belongs to the repo. Its agent may change it. To refresh from the skill
later, diff the skill's scripts against the revision in `scripts/SOURCE` and merge the
changes into the local copy. Never overwrite the local copy.

## Start an agent

Run the harness inside a shell in a tmux window, never as the window's command, so
chakrit can restart it.

```sh
tmux new-window -d -P -F '#{window_id} #{pane_id}' -c <folder>
tmux send-keys -t <pane_id> ace Enter
```

- Never use `exec ace`. Never rename tmux windows.
- If `ace` prints "No conversation found to continue", run `ace new` in that pane.
- Rename the harness session to the agent name: `/rename <agent-name>` sent to the pane
  (`scripts/control-agents rename-session` does this safely).
- Record the window and pane IDs in the parent's registry.

## Message an agent

1. Identify the sender in the first line: `FROM: <agent-name> (<folder>)`. Never write
   as chakrit.
2. Use the harness's own agent messaging when sender and receiver both have it.
   Otherwise use `scripts/control-agents send <slug> --snapshot <uuid>`, which checks
   the pane before typing. Never hand-type into a pane the script refused.
3. Harness commands (`/clear`, `/rename`, `/exit`) always go through
   `scripts/control-agents`.
4. Quote rulings verbatim with chakrit's name and the date:
   `chakrit, 2026-11-04: "<exact words>"`.

## Wake up a control

When an agent needs its parent (for a port, a heavy-job slot, a ruling) and the parent
is not running:

1. Check: `tmux list-panes -a -F '#{pane_id} #{pane_current_path} #{pane_current_command}'`
   shows no harness running in the parent's folder.
2. Start it with "Start an agent".
3. Send the ask.

An org control may wake machine control the same way. Machine control that needs a
project pane while the org control is down manages that pane directly; it starts the
org control first only when that is faster or the work needs org context.

## Save and clear an agent

1. Ask the agent to run its session-save skill (`ace-save` or the school's equivalent).
2. Wait for the reply naming the checkpoint paths it wrote and read back.
3. If the save failed, stop and record it in `tasks.md`. Never clear.
4. Check the pane shows no newer unsaved work or typed draft.
5. Clear with `scripts/control-agents clear-context <slug> --snapshot <uuid>
   --checkpoint <path>`.

## Run a process

Every long-running process (dev server, preview server, test server, watcher) runs in a
visible tmux pane in the agent's own window. Never run one through the harness's
background shell.

Layout: the harness pane on the left at half the width, one pane per process stacked
on the right with equal heights.

```sh
tmux split-window -d -P -F '#{pane_id}' -t <harness_pane> -c <folder>   # once per process
tmux set-option -w -t <window_id> main-pane-width 50%
tmux select-layout -t <window_id> main-vertical
```

The harness must be the window's first pane, so `main-vertical` keeps it on the left.
Re-run the last two commands after adding or removing a process pane.

Bind servers to `0.0.0.0` on ports from the project's block. Report pane IDs to the
parent control.
