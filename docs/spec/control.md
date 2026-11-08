# control skill

Status: implemented

The design of `skills/control/`, for agents editing that skill. Agents running the skill
never read this file; every rule they follow lives in the skill's own `SKILL.md`,
`references/` and `templates/`.

## What it is

One skill, invoked in different folders, that sets up the user's agent coordination on a
single machine: three fixed levels of control agents in tmux, rules and memory in one
engram store, and registries. It replaces copying control repos between orgs and
machines.

The skill is self-contained for any user. Its wording addresses "the user"; "chakrit"
appears only as an example name, and no rule rests on what chakrit wants.

## Structure

- Three fixed levels, never a fourth: machine control (`~/Documents/control`), org
  control (`~/Documents/<org>/control`), project control
  (`~/Documents/<org>/<project>`).
- Agent names: `<machine>:control`, `<machine>:<org>:control`,
  `<machine>:<org>:<project>`. `<org>` is the user's short name (`datawow`).
- Higher levels hold less context. Machine control keeps work across orgs and work
  that belongs to no org, and sends one org's tasks to that org control. Org controls
  track tasks and alignment, not project details. Project controls own project context
  and may do hands-on work.
- Every control (machine, org and project) is a local git repo. It needs no remote; it
  tracks the control's own edits. Setup runs `git init` in a control folder that is not
  one.
- Single machine. No sync content anywhere.
- A single-repo project's control runs in that repo's own folder. A project with
  several repos gets a local wrapper repo that keeps `repos.txt` and `bin/clone-repos`;
  its clones are plain and gitignored. No submodules.

## Instructions and rules

- After setup no agent needs the skill for daily work. Each agent's instruction file
  carries the standing grant and pointers to the rule entries it loads.
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
  with `mem_update` by ID, appending the quoted ruling. The user syncs amendments back
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
- A control never edits another agent's files. Org and project setup only puts the
  folder in place: use it, clone the repo (single-repo project) or `git init`, run the
  school setup, and copy the level's templates as they are, the instruction template
  only when the folder has no instruction file. Then the parent initiates the agent,
  which takes its files over: fills the template values or adds the `## Control`
  block to its own file, records its port block, pins engram, clones its repos, runs
  its init skill. There is one initiation message; the control adapts it to what it
  sees in the folder. Machine setup, which has no parent to initiate it, fills its
  own templates.

## Environment

- ACE is preferred where it exists, never required. An environment may use its own
  CLI and skills instead, so the skill names none of them.
- An agent started through its environment already has that environment's start and
  save skills; waking and saving name none.
- A control starts agents below it with the command that started its own session.
- The Environment table (machine control's instruction file, each org control's) holds
  only the school and init skill, for onboarding.

## Agent handling

- The user's "stop" for an agent means wind down: save, clear, exit the harness, exit
  the shell.
- `clear-context` and `wind-down` require `--saved <location>`; `force-clear` requires
  `--ruling` with the user's quoted words, a last resort. The flag is named `--ruling`,
  not `--reason`, so an agent cannot fill it with a reason of its own. All three log to
  `clears.log`.
- Agents resume their previous session, which keeps its name marker and settings. On
  some harnesses a clear followed by no message does not hold, and the next resume
  reopens the old conversation, so waking an agent always clears it again (reusing a
  save already reported) and sends the wake message at once.
- Waking and giving a task are separate messages: an agent given both at once may skip
  orientation. The control checks the task against the agent's state report first.
- Messages never interrupt an agent's work. A ruling or reply within its current work
  needs no wake. A control holds a new task for a busy agent until it reports done or
  is idle. A task that reaches a busy agent anyway waits for its current work, and the
  agent's own save carries it through the clear. An agent finishes a wake-up or
  initiation before taking any task.
- Messages go through the harness's agent messaging first; `scripts/control-agents`
  is the fallback, and the only way to send keystroke-only commands (`/clear`,
  `/rename`, `/quit`).
- Two message classes: rulings are the user's decisions and are applied as given; task
  asks may be misread in relay, so the receiver pushes back and the control resolves it
  with the user.
- Org and machine controls present a plan and get the user's confirmation before each
  new task.
- Nothing runs upward. A child reaches its parent through agent messaging or asks
  the user to start the parent and relay. Machine control never acts on a project's
  pane; it reaches project work through the org control, starting and waking it when
  it is not running.
- Long-running processes, dev and preview servers included, run only in tmux panes
  the user can see, never in the harness's own shell. A project control creates and lays
  out its process panes against `"$TMUX_PANE"`, never a typed pane or window ID, so a
  wrong target cannot land in the window the user is viewing.
- After a machine or org control is set up or initiated, it scans one level down for
  folders that should get controls, gets the user's approval, and runs the setups. Setup
  lodges this as a backlog row; a parent sends it as a task after the wake, and the user
  asks machine control.

## Records

- Registries are Markdown files a control keeps to track shared things; the templates
  are examples, not a required set.
- Agent rows hold slug, checkout and the last-known window and pane. The user starts
  and moves agents alongside the controls, so the pane IDs are a cache: controls use
  them as they are and correct a row only when the script refuses the pane or the cells
  are empty.
- Ports nest: machine control grants blocks to org controls, which grant blocks to
  projects. Heavy-job slots do not nest: only machine control records them, holder
  `<org>:<project>`; org controls relay requests.
- Machine control alone decides what to pause, serialize or clean up when disk,
  memory or CPU runs low: only the top level sees every agent's work.
- Engram holds rules, knowledge, decisions, state reports and done tasks. Registries
  and live tasks stay in files, for now, because scripts and the control page read
  them by path. Without engram, a `memory/` folder per level holds what engram would.
- Knowledge about one component repo goes in that repo's own docs, so it travels with
  the clone.
- `control.html` is the one page the user checks. It is a fixed template rendering
  `control.data.js`, the only live task record. Agents edit only the data file for
  updates, and change `control.html` when the user asks for a different view (pages,
  columns). The
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
  instead of matching harness names, so a new harness needs no change. The one
  exception is wind-down's fixed `exit`, typed once the harness has quit.
- `send` refuses a pane that printed since the control's last `inspect`, or was never
  inspected: `inspect` records the pane's `pane_last_output_time` in `inspected.tsv`.
  The control then inspects again and retries. Idle harness screens print nothing, so
  the check passes for an idle agent and refuses a busy one.
- It refuses to type when the pane's cursor line holds a letter or digit left of the
  cursor: typed input the paste would join. It reads only left of the cursor, since an
  empty prompt's placeholder sits to the right.
- It runs through `uv run --script` (Python 3.10 or newer). Tests, from
  `skills/control/`: `uv run --no-project --python '>=3.10' python -B -m unittest
  discover -s tests`.

## Lineage

Conventions and scripts come from chakrit's Data Wow control repo on lz49
(`~/Documents/datawow/control`, commit `ea49ab4`). Earlier variants: gz44
`~/Documents/control`, gz44 `~/Documents/appbaobao/control`, lz49
`~/Documents/ircp-sso/control`. The manifest and clone script follow gz44
`~/Documents/naxon-ai` (`repos.txt`, `bin/clone-repos`).
