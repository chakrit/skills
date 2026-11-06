# Control operations

Shared procedures the setup references call. The procedures controls run on agents
every day (start, message, clear, wake, give a task) live in
`templates/rules/handling-agents.md`, which machine setup seeds as engram entry
`rule/handling-agents`.

## Install scripts

Copy this skill's `scripts/` into the control repo as `scripts/`. Project controls
skip this; they reach their parent through messages. To refresh later, copy the
skill's `scripts/` again and review the diff before committing.

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
   `control.data.js`, with chakrit's quoted words as the source. Commit.
4. **Do.** Run the setup or initiation for each approved candidate, one at a time.
   Each org control set up this way runs this section again for its own projects.
   Mark each backlog entry done with its commit hash.

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
