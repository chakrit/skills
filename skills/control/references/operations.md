# Control operations

Shared procedures the setup references call. Setup writes the parts agents need daily
into their policy and instruction files; agents do not read this file after setup.

## Install scripts

Copy this skill's `scripts/` into the control repo as `scripts/`. Project controls
skip this; they reach their parent through messages. To refresh later, copy the
skill's `scripts/` again and review the diff before committing.

## Start an agent

Run the harness inside a shell in a tmux window, never as the window's command, so
chakrit can restart it. Type the harness named in the registry's Backend column.

```sh
tmux new-window -d -P -F '#{window_id} #{pane_id}' -c <folder>
tmux send-keys -t <pane_id> <harness> Enter
```

- Never `exec` the harness. Never rename tmux windows.
- Record the window and pane IDs in the parent's registry, then rename the harness
  session: `scripts/control-agents rename-session <slug> <agent-name>`.

## Wake up an agent

Waking an agent and giving it a task are two separate flows. Never put a task, or
background on one, in the wake message: an agent may jump to the task before it has
finished loading its context.

1. **Start.** If the agent is not running, start it ("Start an agent").
2. **Send the wake message** ("Message an agent"):

   ```text
   FROM: <your agent name> (<your folder>). This message is written by a control
   agent, not chakrit.

   WAKE-UP: Run your session-start skill (ace, dw-start or similar); without one,
   follow the session-start steps in your instruction file. Then report your current
   state: work in progress, open questions, anything blocking. Take no new work yet.
   ```

3. **Wait** until the agent has reported. Read the report with
   `scripts/control-agents inspect <slug>`.
4. **Check the fit.** Before giving a task, judge it against the report. If the task
   does not fit the agent's state (for example, a feature request to an agent in the
   middle of a large refactor), hold the task and take it to chakrit with a
   recommendation. Otherwise continue with "Give a task".

## Give a task

Send the task ask or ruling as its own message ("Message an agent"), only after the
wake-up check.

- Give the context from chakrit's conversation with you that the agent cannot know:
  the goal, constraints, deadlines, decisions, granted resources.
- Do not give everything you know. The agent has the project's docs, specs and code;
  leave the how to it.
- Keep it short. Point to files, PRs or panes instead of restating them; expect the
  agent to look things up itself.

## Message an agent

1. Identify the sender in the first line: `FROM: <agent-name> (<folder>)`. Never write
   as chakrit.
2. Use the harness's own agent messaging when sender and receiver both have it.
   Otherwise use `scripts/control-agents send <slug>` with the message on stdin. It
   types only into the registered pane, while it runs a harness in the agent's folder
   and nobody is viewing it. Never hand-type into a pane the script refused.
3. Clear and rename an agent only through `scripts/control-agents`.
4. Quote rulings verbatim with chakrit's name and the date:
   `chakrit, 2026-11-04: "<exact words>"`.

## Reach a parent

Messages run downward through `scripts/control-agents`; nothing runs upward. An agent
that needs its parent (for a port, a heavy-job slot, a ruling) uses the harness's own
agent messaging when it reaches the parent. Otherwise it asks chakrit to start the
parent and relay the message, for example: "We need a port for the XYZ server and the
org control is not running; can you start it and pass this on?" A child never starts
its parent or runs the parent's scripts.

Machine control that needs a project pane while the org control is down manages that
pane directly; it starts the org control first only when that is faster or the work
needs org context.

## Save and clear an agent

1. Ask the agent to save. It saves before a clear, preferring engram's
   `mem_session_summary`, and reports what it saved and where.
2. If the save failed, stop and record it in `human.html`. Never clear.
3. Check with `scripts/control-agents inspect <slug>` that the pane shows no newer
   unsaved work or typed draft.
4. Clear with `scripts/control-agents clear-context <slug>`.

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
