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
- Tag the pane with the agent's name, then rename the harness session:

  ```sh
  tmux set-option -p -t <pane_id> @agent <agent-name>
  scripts/control-agents rename-session <slug> <agent-name>
  ```

  `scripts/control-agents` finds an agent only by this tag. The agent re-tags its own
  pane at every session start, so the tag comes back after a tmux restart.

## Message an agent

1. Identify the sender in the first line: `FROM: <agent-name> (<folder>)`. Never write
   as the user.
2. Send through the harness's own agent messaging whenever it reaches the receiver.
   It is the default channel for every message in these procedures, the wake message
   and the task included: it delivers whole, with no pane to read first and no refusal
   on new output. Some harnesses load agent-messaging tools only on demand, so search
   your tools for one before concluding you have none; once its agent list shows the
   receiver, use it without further checks.
   Only when it does not reach the receiver, read the pane with
   `scripts/control-agents inspect <slug>`, then use
   `scripts/control-agents send <slug>` with the message on stdin. It types only into
   the one pane tagged with the agent's name, in the agent's folder, while a program other than the pane's
   shell holds it, nobody is viewing it, its prompt holds no typed input, and it has
   printed nothing since your last `inspect`. When it refuses for new output, inspect
   again and retry. Never hand-type into a pane the script refused.
3. Clear, rename and wind down an agent only through `scripts/control-agents`. These
   are keystroke commands, not messages: the message you send right after one still
   goes through step 2.
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
   and resolve it, or ask the user. The pane closes, and its tag with it.

"Wake up an agent" starts it again later and clears the resumed session.

## Wake up an agent

Waking an agent and giving it a task are two separate messages. Never put a task, or
background on one, in the wake message: an agent may jump to the task before it has
finished loading its context.

1. **Start.** If the script finds no pane tagged with the agent's name, look for the
   agent's harness in a pane open in its folder and tag it ("Start an agent"); if it
   has none, start it.
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
initiates project controls. Never edit the agent's files yourself; the agent takes them
over.

1. **Check the setup.** The agent's folder is set up when it is a git repo with an
   instruction file. If it is not, load the `control` skill and run its setup reference
   for that level ("Set up an org control" or "Set up a project control"), which
   returns you here.
2. **Start** the agent if it is not running ("Start an agent").
3. **Record it.** Add the agent's row to your registry with Status `initiating` if it
   has none. Grant a port
   block if it has none: machine control grants an org control a block from
   8000–9000, an org control grants a project control a block from its own. Record it
   in your `registries/ports.md`. Machine control also adds the org's line under
   `## GitHub orgs` in `registries/orgs.md` and a link to the org's `control.html` in
   its `control.data.js`. Commit.
4. **Write the message.** Start from the message below and adapt it to what you see in
   the agent's folder: whether its instruction file is the level template as copied or
   its own file, which other templates setup copied, and what is still missing. Give
   the context from your own work that the agent cannot find itself: its agent name,
   parent and engram project, its port block, how folders are onboarded here (the
   school and init skill you use), and any rulings or context it needs; for an org
   control, its GitHub org and the control page's font steps ("Point the control page
   at PragmataPro" in the control skill's `references/operations.md`); for a project,
   its repos. When the instruction file is its own, include the `## Control` section, down
   to the next `##` heading, of the agent's level template (the control skill's
   `templates/instructions/<level>-control.md`; without the skill, from a set-up
   sibling's instruction file).

   ```text
   FROM: <your agent name> (<your folder>). This message is written by a control
   agent, not the user.

   INITIATION: Take over your instruction file (AGENTS.md; keep CLAUDE.md a link to
   it). It is <the control template as copied: replace every {{value}} with the
   values below and adapt it to this folder | your own: add the `## Control` block
   below to it>. Keep your existing rules, and move any governance rule your level
   policy now covers out of it. Fill the {{values}} in <the other files setup
   copied>. Record your port block <under "Ports" | in registries/ports.md>. When
   `command -v engram` prints a path, run `engram init <engram project>` and commit
   `.engram/config.json`<; this folder is a clone, so add `.engram/` to
   .git/info/exclude instead of committing it>. <Clone your repos, adding `.engram/`
   to each clone's .git/info/exclude.> <Run your init skill, <init skill>.> Commit
   your changes and the files setup copied. Then load the rule entries your
   instruction file names, in full, as it describes. Reply with everything you did:
   the files you changed, the entries you loaded, whether engram is installed, and any
   conflict with your existing rules.

   <values>
   <block>
   ```

5. **Wake it** ("Wake up an agent"), then send the message as its task.
6. **Judge the report.** Delivery is not acknowledgment; wait for the agent's report.
   When it shows everything the message asked for done, set the agent's Status to
   `initiated` in your registry and commit. Otherwise reply with what is missing and
   judge the next report.
7. **Hand an org control its planning.** For an org control, send "Plan downstream
   controls" as its next task ("Give a task"): it loads the `control` skill and runs
   that section of `references/operations.md` for its own org.
