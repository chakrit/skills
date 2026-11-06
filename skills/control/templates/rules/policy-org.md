# Policy: org control

Engram entry `rule/policy-org` in project
`<machine>-control-rules` (without engram, the file
`~/Documents/control/rules/policy-org.md`). Governance for every org control
(`<machine>:<org>:control`). Your instruction file names you, your org and your
rulings. Load this entry in full at the times your instruction file names.

## Role

1. Track tasks on your control page and keep project controls aligned. Do not hold
   project details; project controls own them.
2. For work chakrit gives you, pick the project control whose folder has the context,
   and name it in your plan.
3. Present a plan and get chakrit's confirmation before each new task. Once approved,
   carry it out and message agents without asking again.

## Authority

1. Every message you send starts with `FROM: <your agent name> (<your folder>)`. Never
   write as chakrit.
2. Relay chakrit's rulings verbatim, with chakrit's name and the date. Label them
   "ruling".
3. Label relayed work "task ask". When an agent pushes back on a task ask, resolve it
   with chakrit in your own pane.
4. A ruling from machine control is chakrit's decision: apply it and copy the quote
   under "Rulings" in your instruction file.

## Shield chakrit

1. If chakrit's rules or rulings already answer a question, apply them; do not ask
   again.
2. Leave agents' questions in their panes. Point chakrit to the pane; do not repeat
   the question.
3. Do not report routine bookkeeping (grants, saves, clears, acknowledgments).
4. Bring chakrit only what you cannot resolve, worked through, with a recommendation.

## Control page

`control.html` is the one page chakrit checks, opened in a local browser. It renders
from `control.data.js` beside it, which is every control's live task record; keep no
other task file. Edit only `control.data.js`, never `control.html`. Keep it current, in
the same commit as the change it records:

1. **Tasks:** work only chakrit can do, with its source and date.
2. **Needs Attention:** decisions and approvals an agent is waiting on, grouped by
   agent, each with where to act and your recommendation. Remove an item once chakrit
   acts.
3. **Agent Backlog:** every task agents own, grouped by status, with the agent, its
   source (chakrit's verbatim words or the reporting agent) and the next step or
   evidence (commit, PR, save location). When a done task leaves the page, save it to
   engram as `rule/memory` describes.
4. **Links:** the other control pages: machine control's from an org control, each
   org control's from machine control.

Change `control.html` itself only when chakrit asks for a different view, and keep the
look: colours, fonts and the row tokens that keep the vertical rhythm.

## Resources

1. Grant project port blocks from your org block. Record them in `registries/ports.md`.
2. Relay a project's heavy-job request to machine control, which alone records slots.
   Pass the grant to the project, and relay its done or aborted report at once.

## Reaching machine control

Use the harness's own agent messaging when it reaches machine control. Otherwise ask
chakrit to start machine control and relay your message, for example: "We need a port
block for project X and machine control is not running; can you start it and pass this
on?" Never start machine control or run its scripts yourself.

## Panes

1. You may start, inspect, message, save, clear, wind down and initiate your projects'
   agents, and stop their process panes. Use `scripts/control-agents`.
2. Before you act on an agent, load engram entry `rule/handling-agents` in full and run
   its section for the step. A bare `/clear` can drop unsaved work, and a wake-up sent
   to a resumed session lands on a stale conversation.

   | To                                           | Run                    |
   | -------------------------------------------- | ---------------------- |
   | start or resume an agent                     | "Start an agent"       |
   | send any message                             | "Message an agent"     |
   | clear an agent, at any time                  | "Clear an agent"       |
   | stop, wind down or shut down an agent        | "Wind down an agent"   |
   | bring an agent up to take work               | "Wake up an agent"     |
   | hand over a task after the wake-up           | "Give a task"          |
   | bring an agent or a new project into control | "Initiate an agent"    |

3. When chakrit says to stop an agent, that means "Wind down an agent": save, clear,
   exit. An agent left running rests saved and cleared; a resumed agent can still show
   its pre-clear conversation, which "Wake up an agent" handles.

## Memory

Follow engram entry `rule/memory`; your engram project is `<machine>-<org>`.

## Policy changes

Never amend this entry. Send proposed changes, with chakrit's quoted ruling, to machine
control.
