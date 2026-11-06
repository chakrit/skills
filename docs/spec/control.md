# control skill

Status: implemented

The design of `skills/control/`, for agents editing that skill. Agents running the skill
never read this file; every rule they follow lives in the skill's own `SKILL.md`,
`references/` and `templates/`.

## What it is

One skill, invoked in different folders, that sets up chakrit's agent coordination on a
single machine: three fixed levels of control agents in tmux, rules and memory in one
engram store, and registries. It replaces copying control repos between orgs and
machines.

## Structure

- Three fixed levels, never a fourth: machine control (`~/Documents/control`), org
  control (`~/Documents/<org>/control`), project control
  (`~/Documents/<org>/<project>`).
- Agent names: `<machine>:control`, `<machine>:<org>:control`,
  `<machine>:<org>:<project>`. `<org>` is chakrit's short name (`datawow`).
- Higher levels hold less context. Machine control keeps work across orgs and work
  that belongs to no org, and sends one org's tasks to that org control. Org controls
  track tasks and alignment, not project details. Project controls own project context
  and may do hands-on work.
- The org root `~/Documents/<org>/` is neither a level nor a repo, yet carries an
  `AGENTS.md` owned by the org control and shares engram project `<machine>-<org>`: an
  agent started there must still load rules and the org's memory.
- Single machine. No sync content anywhere.
- Projects keep `repos.txt` and `bin/clone-repos`; clones are plain and gitignored.
  No submodules.

## Instructions and rules

- After setup no agent loads the skill again. Each agent's instruction file carries
  the standing grant and pointers to the rule entries it loads.
- Every instruction file states the session-start step itself (load the rule entries,
  then `mem_context`) instead of pointing to it: a pointer chain to the step was
  skipped after restarts.
- Rules are five engram entries in a dedicated project, `<machine>-control-rules`:
  `rule/policy-machine`, `rule/policy-org`, `rule/policy-project` (governance only),
  `rule/memory` and `rule/handling-agents`. The dedicated project exists because a
  save under an existing topic key replaces that entry.
- An entry loads by searching its key, taking the exact `topic_key` match, then
  `mem_get_observation` by ID, since search returns only previews.
- Seeds live in `templates/rules/`. Machine control owns the entries and amends them
  with `mem_update` by ID, appending the quoted ruling. chakrit syncs amendments back
  to the seeds and handles backups.
- With engram, engram is the only copy of the rules; setup writes no rule files.
  Without engram, setup copies the seeds to `~/Documents/control/rules/`.
- Engram project names start with the machine (`<machine>-control`,
  `<machine>-<org>`, `<machine>-<org>-<project>`, `<machine>-control-rules`), so a
  later cross-machine sync would not merge two machines' projects. Topic keys are
  unprefixed.
- `rule/handling-agents` holds the procedures controls run on agents (start, message,
  before a clear, clear, wind down, wake, give a task, initiate). Initiation lives
  there so a control can run it without the skill; it loads the skill only when the
  agent's folder needs setup first.
- Policies name these procedures instead of restating them.

## Environment

- ACE is preferred where it exists, never required. An environment may use its own
  CLI and skills instead, so the skill names none of them.
- An agent started through its environment already has that environment's start and
  save skills; waking and saving name none.
- A control starts agents below it with the command that started its own session.
- The Environment table (machine control's instruction file, each org root's) holds
  only the school and init skill, for onboarding.

## Agent handling

- chakrit's "stop" for an agent means wind down: save, clear, exit the harness, exit
  the shell.
- `clear-context` and `wind-down` require `--saved <location>`; `force-clear` requires
  `--ruling` with chakrit's quoted words, a last resort. The flag is named `--ruling`,
  not `--reason`, so an agent cannot fill it with a reason of its own. All three log to
  `clears.log`.
- Agents resume their previous session, which keeps its name marker and settings. On
  some harnesses a clear followed by no message does not hold, and the next resume
  reopens the old conversation, so waking an agent always clears it again (reusing a
  save already reported) and sends the wake message at once.
- Waking and giving a task are separate messages: an agent given both at once may skip
  orientation. The control checks the task against the agent's state report first.
- Messages go through the harness's agent messaging first; `scripts/control-agents`
  is the fallback, and the only way to send keystroke-only commands (`/clear`,
  `/rename`, `/quit`).
- Two message classes: rulings are chakrit's decisions and are applied as given; task
  asks may be misread in relay, so the receiver pushes back and the control resolves it
  with chakrit.
- Org and machine controls present a plan and get chakrit's confirmation before each
  new task.
- Nothing runs upward. A child reaches its parent through agent messaging or asks
  chakrit to start the parent and relay. Machine control never acts on a project's
  pane; it reaches project work through the org control, starting and waking it when
  it is not running.
- Long-running processes, dev and preview servers included, run only in tmux panes
  chakrit can see, never in the harness's own shell.
- After a machine or org control is set up or initiated, it scans one level down for
  folders that should get controls, gets chakrit's approval, and runs the setups. Setup
  lodges this as a backlog row; a parent sends it as a task after the wake, and chakrit
  asks machine control.

## Records

- Registries are Markdown files a control keeps to track shared things; the templates
  are examples, not a required set.
- Agent rows hold slug, checkout and the last-known window and pane. chakrit starts
  and moves agents alongside the controls, so the pane IDs are a cache: controls use
  them as they are and correct a row only when the script refuses the pane or the cells
  are empty.
- Ports nest: machine control grants blocks to org controls, which grant blocks to
  projects. Heavy-job slots do not nest: only machine control records them, holder
  `<org>:<project>`; org controls relay requests.
- Engram holds rules, knowledge, decisions, state reports and done tasks. Registries
  and live tasks stay in files, for now, because scripts and the control page read
  them by path. Without engram, a `memory/` folder per level holds what engram would.
- Knowledge about one component repo goes in that repo's own docs, so it travels with
  the clone.
- `control.html` is the one page chakrit checks. It is a fixed template rendering
  `control.data.js`, the only live task record. Agents edit only the data file. The
  data is JSON wrapped as `window.CONTROL = {...};` and loaded by a script tag, since a
  page opened from disk cannot `fetch` a local file. Views: Tasks, Needs Attention and
  Agent Backlog. The page shows no registries or records.

## Script

- One reference script, `scripts/control-agents`, with no configuration: it finds its
  registry from the folder layout, talks to the tmux server it runs in, and hard-codes
  the harness slash commands. Controls copy it and may adapt it.
- It targets panes only by tmux ID, re-checks the pane before typing, and never changes
  windows or layout, except that wind-down's exit closes the agent's pane.
- It refuses to type when the pane's own shell holds the terminal's foreground group,
  instead of matching harness names, so a new harness needs no change.
- It runs through `uv run --script` (Python 3.10 or newer). Tests, from
  `skills/control/`: `uv run --no-project --python '>=3.10' python -B -m unittest
  discover -s tests`.

## Lineage

Conventions and scripts come from chakrit's Data Wow control repo on lz49
(`~/Documents/datawow/control`, commit `ea49ab4`). Earlier variants: gz44
`~/Documents/control`, gz44 `~/Documents/appbaobao/control`, lz49
`~/Documents/ircp-sso/control`. The manifest and clone script follow gz44
`~/Documents/naxon-ai` (`repos.txt`, `bin/clone-repos`).
