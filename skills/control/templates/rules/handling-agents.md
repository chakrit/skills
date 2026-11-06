# Rules: handling agents

Engram entry `rule/handling-agents` in project
`<machine>-control-rules` (without engram, the file
`~/Documents/control/rules/handling-agents.md`). The procedures a control runs on the
agents it manages. Machine control owns this entry. Load it in full at the times your
instruction file names, and follow the section for the step you are on. Each step guards
against a failure the obvious command causes: a bare `/clear` can drop unsaved work, and
a wake-up sent to a resumed session lands on a stale conversation.

## Start an agent

Run the harness inside a shell in a tmux window, never as the window's command, so
the user can restart it and `scripts/control-agents` can tell the harness from the shell.
Start it with the same command that started your own session. Your shell's ancestor
processes show it: run `ps -o ppid=,command= -p <pid>` from your shell's parent upward
(for example `claude --continue` under `ace`), and take the command whose parent is
your tmux pane's shell.

```sh
tmux new-window -d -P -F '#{window_id} #{pane_id}' -c <folder>
tmux send-keys -t <pane_id> '<start command>' Enter
```

Resume the folder's last session by default. The session keeps its name marker and its
per-conversation settings, which a new session loses; "Wake up an agent" clears the
old conversation. Start a new session only when the task explicitly requires one or
the command reports no session to resume.

- Never `exec` the harness. Never rename tmux windows.
- Record the window and pane IDs in your registry, then rename the harness session:
  `scripts/control-agents rename-session <slug> <agent-name>`.

## Message an agent

1. Identify the sender in the first line: `FROM: <agent-name> (<folder>)`. Never write
   as the user.
2. Use the harness's own agent messaging when sender and receiver both have it.
   Otherwise use `scripts/control-agents send <slug>` with the message on stdin. It
   types only into the registered pane, in the agent's folder, while a program other
   than the pane's shell holds it, nobody is viewing it, and its prompt holds no typed
   input. Never hand-type into a pane the script refused.
3. Clear, rename and wind down an agent only through `scripts/control-agents`.
4. Quote rulings verbatim with the user's name and the date:
   `chakrit, 2026-11-04: "<exact words>"`.

## Before a clear

Establish that the agent's work is saved, and where. A save already reported counts;
asking for another wastes the agent's tokens.

1. Read the agent's latest report where it arrives: its reply through the harness's
   agent messaging, or, without that, its pane: `scripts/control-agents inspect <slug>`.
2. The agent is saved when that report says what it saved and where, with nothing
   after it: no newer work and no typed draft. A session resumed after a wind-down
   usually shows exactly this.
3. Otherwise ask the agent to save ("Message an agent") and report what it saved and
   where. It saves as `rule/memory` ("Saving") describes. Wait for the report, then
   read it as in step 1.
4. If the save failed, stop: add it to Needs Attention in `control.data.js` and do not
   clear.

The result is the save location the agent reported, such as an engram observation, a
session file its save skill wrote, or a memory file.

## Clear an agent

1. Run "Before a clear".
2. Clear with the reported save location:
   `scripts/control-agents clear-context <slug> --saved "<save location>"`. The script
   logs each clear to `clears.log` in your control repo.
3. A clear holds only once a message follows it. On some harnesses, resuming a session
   whose last action was a clear reopens the conversation before the clear. When the
   agent is to work now, send the next message at once ("Wake up an agent").

**Force a clear** only on the user's ruling, as a last resort: the user orders a clear
without a save, or approves one because the agent is stuck or hung, agents are being
torn down, or another circumstance requires it. Without the user's words, ask the user
first. Skip "Before a clear" and run
`scripts/control-agents force-clear <slug> --ruling "<the user's quoted words>"`. Step
3 still applies.

## Wind down an agent

When the user says to stop, wind down or shut down an agent, this is the procedure: the
agent saves, clears, exits its harness, and its shell exits, which closes the pane.

1. Run "Before a clear".
2. Run `scripts/control-agents wind-down <slug> --saved "<save location>"`. It types
   `/clear` and `/quit`, waits for the shell to take the pane back, then types `exit`.
   If the harness does not exit, the script types nothing into the shell; read the pane
   and resolve it, or ask the user.
3. Empty the agent's Window and Agent pane cells in your registry: the agent is not
   running. Commit the registry change.

"Wake up an agent" starts it again later and clears the resumed session.

## Wake up an agent

Waking an agent and giving it a task are two separate messages. Never put a task, or
background on one, in the wake message: an agent may jump to the task before it has
finished loading its context.

1. **Start.** If the script refuses the agent's recorded pane, find its pane as your
   registry's header says; if it has none, start it ("Start an agent").
2. **Clear.** Unless the session was started new, run "Clear an agent". A resumed or
   still-running session holds its previous conversation, even when it was cleared at
   a wind-down.
3. **Send the wake message** at once ("Message an agent"). Name the engram entries the
   agent must load: its level policy (`rule/policy-org` for an org control,
   `rule/policy-project` for a project control) and `rule/memory`.

   ```text
   FROM: <your agent name> (<your folder>). This message is written by a control
   agent, not the user.

   WAKE-UP: Load your rules first, in full: engram entries <entries> in project
   <machine>-control-rules (mem_search the topic key, take the exact topic_key match,
   then mem_get_observation its ID), or the files in ~/Documents/control/rules/
   without engram. Then run your session start, as your environment and your
   instruction file describe. Report your current state: work in progress, open
   questions, anything blocking. Take no new work yet.
   ```

4. **Wait** until the agent has reported. Read the report where it arrives, as in
   "Before a clear" step 1.
5. **Check the fit.** Judge the task against the report. If it does not fit the
   agent's state (for example, a feature request to an agent in the middle of a large
   refactor), hold it and take it to the user with a recommendation. Otherwise run
   "Give a task".

## Give a task

Send a new task ask as its own message ("Message an agent"), only after "Wake up an
agent". If the agent is still working, hold the task until it reports done or sits
idle, then wake it (the wake saves and clears it first) and send the task. A ruling or
reply within the agent's current work is a plain "Message an agent", with no wake.

- Give the context from the user's conversation with you that the agent cannot know:
  the goal, constraints, deadlines, decisions, granted resources.
- Do not give everything you know. The agent has the project's docs, specs and code;
  leave the how to it.
- Keep it short. Point to files, PRs or panes instead of restating them; expect the
  agent to look things up itself.

## Initiate an agent

Brings an agent one level below you under control: it gets the standing grant (the
`## Control` section of its instruction file) and the rule-entry pointers, so it works
without the control skill. Machine control initiates org controls; an org control
initiates project controls.

1. **Check the setup.** The agent's folder is set up when it is a git repo and has an
   instruction file, a row in your registry, and, when `command -v engram` prints a
   path, an engram pin (`.engram/config.json`). If it is not a git repo, run `git init`
   in it. If any other part is missing, load the `control` skill and run its setup reference
   for that level ("Set up an org control" or "Set up a project control"), which adds
   the missing parts without replacing existing files. Then continue here.
2. **Start** the agent if it is not running ("Start an agent").
3. **Fill the block.** Take the `## Control` section, down to the next `##` heading,
   from the agent's level template (the control skill's
   `templates/instructions/<level>-control.md`; without the skill, copy the section
   from a set-up sibling's instruction file). Replace every placeholder; for an org
   control's Environment rows, take the values from the instruction files already in
   its org's projects, or ask the user. Grant a port
   block if the agent has none: machine control grants an org control a block from
   8000–9000, an org control grants a project control a block from its own. Record it
   in your `registries/ports.md`. For a project control, write it in the block under
   "Ports"; for an org control, add a line after the block asking it to record the
   block in its `registries/ports.md`.
4. **Wake it** ("Wake up an agent"), then send the message below as its task, with the
   block inside it. Never edit the agent's instruction file yourself; the agent writes
   its own instructions.

   ```text
   FROM: <your agent name> (<your folder>). This message is written by a control
   agent, not the user.

   INITIATION: Add the block below to your always-loaded instruction file (AGENTS.md;
   keep CLAUDE.md consistent with it). Preserve your existing rules. Move any
   governance rule that your level policy now covers out of your instruction file.
   Then load the rule entries the block names, in full, as the block describes. Reply
   with the instruction path you changed, the entries you loaded, and any conflict
   with your existing rules.

   <block>
   ```

5. **Wait for the acknowledgment.** Delivery is not acknowledgment. Record it in the
   Agent Backlog of your `control.data.js` with the paths the agent reported.
6. **Hand an org control its planning.** For an org control, send "Plan downstream
   controls" as its next task ("Give a task"): it loads the `control` skill and runs
   that section of `references/operations.md` for its own org.
