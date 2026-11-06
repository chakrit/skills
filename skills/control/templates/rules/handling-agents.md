# Rules: handling agents

Engram entry `rule/handling-agents` in project
`<machine>-control-rules` (without engram, the file
`~/Documents/control/rules/handling-agents.md`). The procedures a control runs on the
agents it manages. Machine control owns this entry. Load it in full before you start,
message, clear or wake an agent, and follow the section for the step you are on. Each
step guards against a failure the obvious command causes: a bare `/clear` can drop
unsaved work, and a wake-up sent to a resumed session lands on a stale conversation.

## Start an agent

Run the harness inside a shell in a tmux window, never as the window's command, so
chakrit can restart it. Type the harness named in the registry's Backend column.

```sh
tmux new-window -d -P -F '#{window_id} #{pane_id}' -c <folder>
tmux send-keys -t <pane_id> '<start command>' Enter
```

Resume the folder's previous session by default. The session keeps its name marker and
its per-conversation settings, which a new session loses; "Wake up an agent" clears the
old conversation. Start a new session only when the task explicitly requires a fresh
one or the folder has no previous session to resume.

| Backend  | Resume (default)      | New session |
| -------- | --------------------- | ----------- |
| `ace`    | `ace`                 | `ace new`   |
| `claude` | `claude --continue`   | `claude`    |
| `codex`  | `codex resume --last` | `codex`     |

If the resume command reports no session to resume, type the new-session command.

- Never `exec` the harness. Never rename tmux windows.
- Record the window and pane IDs in your registry, then rename the harness session:
  `scripts/control-agents rename-session <slug> <agent-name>`.

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

## Before a clear

Establish that the agent's work is saved, and where. A save already reported counts;
asking for another wastes the agent's tokens.

1. Read the pane: `scripts/control-agents inspect <slug>`.
2. The agent is saved when the pane shows its report of what it saved and where, with
   nothing after the report: no newer work and no typed draft. A session resumed after
   a wind-down usually shows exactly this: the wind-down saved and cleared, but no
   message followed the clear, so the harness reopened the conversation before it.
3. Otherwise ask the agent to save ("Message an agent") and report what it saved and
   where. It saves with its own session-save skill when it has one (an `ace` agent
   writes `.ace/save.md` in its folder), otherwise as `rule/memory` describes. Wait
   for the report, then read the pane again.
4. If the save failed, stop: add it to Needs Attention in `control.data.js` and do not
   clear.

The result is the save location the agent reported, such as an engram observation, a
`.ace/save.md` path or a memory file.

## Clear an agent

1. Run "Before a clear".
2. Clear with the reported save location:
   `scripts/control-agents clear-context <slug> --saved "<save location>"`. The script
   logs each clear to `clears.log` in your control repo.
3. A clear holds only once a message follows it. On some harnesses, resuming a session
   whose last action was a clear reopens the conversation before the clear. When the
   agent is to work now, send the next message at once ("Wake up an agent"). At a
   wind-down, leave it; "Wake up an agent" clears it again on the next start.

**Force a clear** only when chakrit orders a clear without a save, the agent is stuck or
hung, agents are being torn down, or another circumstance makes a save impossible or
pointless. Skip "Before a clear" and run
`scripts/control-agents force-clear <slug> --reason '<chakrit's quoted words, or what
happened>'`. Step 3 still applies.

## Wake up an agent

Waking an agent and giving it a task are two separate messages. Never put a task, or
background on one, in the wake message: an agent may jump to the task before it has
finished loading its context.

1. **Start.** If the agent is not running, start it ("Start an agent").
2. **Clear.** Unless the session was started new, run "Clear an agent". A resumed or
   still-running session holds its previous conversation, even when it was cleared at
   a wind-down.
3. **Send the wake message** at once ("Message an agent"). Name the engram entries the
   agent must load: its level policy (`rule/policy-org` for an org control,
   `rule/policy-project` for a project control) and `rule/memory`, plus
   `rule/handling-agents` for an org control.

   ```text
   FROM: <your agent name> (<your folder>). This message is written by a control
   agent, not chakrit.

   WAKE-UP: Load your rules first, in full: engram entries <entries> in project
   <machine>-control-rules (mem_search the topic key, take the exact topic_key match,
   then mem_get_observation its ID), or the files in ~/Documents/control/rules/
   without engram. Then run your session-start skill (ace, dw-start or similar);
   without one, follow the session-start steps in your instruction file. Report your
   current state: work in progress, open questions, anything blocking. Take no new
   work yet.
   ```

4. **Wait** until the agent has reported. Read the report with
   `scripts/control-agents inspect <slug>`.
5. **Check the fit.** Judge the task against the report. If it does not fit the
   agent's state (for example, a feature request to an agent in the middle of a large
   refactor), hold it and take it to chakrit with a recommendation. Otherwise run
   "Give a task".

## Give a task

Send the task ask or ruling as its own message ("Message an agent"), only after "Wake
up an agent".

- Give the context from chakrit's conversation with you that the agent cannot know:
  the goal, constraints, deadlines, decisions, granted resources.
- Do not give everything you know. The agent has the project's docs, specs and code;
  leave the how to it.
- Keep it short. Point to files, PRs or panes instead of restating them; expect the
  agent to look things up itself.
