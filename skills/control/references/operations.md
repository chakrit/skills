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
tmux send-keys -t <pane_id> '<start command>' Enter
```

Resume the folder's previous session by default; it holds context a fresh session
lacks. Start a new session only when the task explicitly requires a fresh one or the
folder has no previous session to resume.

| Backend  | Resume (default)      | New session |
| -------- | --------------------- | ----------- |
| `ace`    | `ace`                 | `ace new`   |
| `claude` | `claude --continue`   | `claude`    |
| `codex`  | `codex resume --last` | `codex`     |

If the resume command reports no session to resume, type the new-session command.

- Never `exec` the harness. Never rename tmux windows.
- Record the window and pane IDs in the parent's registry, then rename the harness
  session: `scripts/control-agents rename-session <slug> <agent-name>`.

## Plan downstream controls

Run after a machine control or an org control is set up or initiated. It finds the
folders one level down that should get their own control, so the structure is complete
rather than set up one folder at a time.

1. **Scan** the new control's level:
   - **Machine control:** every folder `~/Documents/<name>/` except `control`. A
     folder is an org candidate when it has no `control/` subfolder and holds git
     repos (`find ~/Documents/<name> -maxdepth 3 -name .git`). Suggest the folder
     name as `<org>` and the GitHub org from its repos' `gh` remotes.
   - **Org control:** every folder `~/Documents/<org>/<name>/` except `control`.
     Classify each one:

     | Folder holds                                    | Candidate for                     |
     | ----------------------------------------------- | --------------------------------- |
     | `AGENTS.md` with a `## Control` section         | nothing; register it if missing   |
     | `AGENTS.md` or `CLAUDE.md` without that section | `references/initiation.md`        |
     | several git clones and no `AGENTS.md`           | `references/setup-project.md`     |
     | one git repo at its top level                   | ask chakrit which project owns it |

     For a project candidate, suggest the folder name as `<project>` and its clones'
     `gh` remotes as `repos.txt` lines.
   - Skip folders without git repos and list them as skipped.
2. **Check authorization.** If chakrit already asked for downstream setup ("set up
   all the orgs", "do the projects too"), quote those words and continue. Otherwise
   send chakrit the candidate list with the suggested names, and ask which to set up.
   Wait for chakrit's answer. Never move or rename a folder chakrit has not named.
3. **Lodge.** Add one Agent Backlog entry per approved candidate in the new control's
   `control.html`, with chakrit's quoted words as the source. Commit.
4. **Do.** Run the setup or initiation for each approved candidate, one at a time.
   Each org control set up this way runs this section again for its own projects.
   Mark each backlog entry done with its commit hash.

## Wake up an agent

Waking an agent and giving it a task are two separate flows. Never put a task, or
background on one, in the wake message: an agent may jump to the task before it has
finished loading its context.

1. **Start.** If the agent is not running, start it ("Start an agent").
2. **Clear before resuming work.** Agents mostly start in resume mode, so the harness
   reopens the previous conversation, and an agent left running still holds its last
   one. Either way the wake message would land on stale context. Clear the agent
   first ("Save and clear an agent"). When its last save is already reported and the
   pane shows nothing newer, clear without asking for another save; otherwise ask it
   to save first. Skip this step only for a session started fresh.
3. **Send the wake message** ("Message an agent"):

   ```text
   FROM: <your agent name> (<your folder>). This message is written by a control
   agent, not chakrit.

   WAKE-UP: Run your session-start skill (ace, dw-start or similar); without one,
   follow the session-start steps in your instruction file. Then report your current
   state: work in progress, open questions, anything blocking. Take no new work yet.
   ```

4. **Wait** until the agent has reported. Read the report with
   `scripts/control-agents inspect <slug>`.
5. **Check the fit.** Before giving a task, judge it against the report. If the task
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
2. If the save failed, stop and add it to Needs Attention in `control.html`. Never
   clear.
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
