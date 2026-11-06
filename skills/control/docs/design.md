# control: design notes

Maintainer notes for the `control` skill. Agents running the skill do not read this.

## What it is

One skill, invoked in different folders, that sets up chakrit's agent coordination
structure on a single machine: three fixed levels of control agents in tmux, central
rules and memory in a shared engram store, and registries. It replaces copying and
adapting control repos between orgs and machines.

## Decisions

- **Three fixed levels, no recursion.** Machine control (`~/Documents/control`), org
  control (`~/Documents/<org>/control`), project control (`~/Documents/<org>/<project>`).
  Naming every level removes later decisions about what a "control" is.
- **Higher levels hold less context.** Machine control keeps tasks no single org owns.
  Org controls track tasks and alignment, not project details. Project controls own
  project context and may do hands-on work.
- **Agent names:** `<machine>:control`, `<machine>:<org>:control`,
  `<machine>:<org>:<project>`. The org slug is chakrit's short name (`datawow`).
- **ACE is preferred, never required, and named per environment.** An environment may
  wrap ACE in its own launcher and skills, so the skill hard-codes none of them. Setup
  records each environment's school, resume and new-session commands, start skill, init
  skill and save skill in an Environment table (machine control's instruction file and
  each org root's), and starting, waking, saving and onboarding read that table.
- **Org roots carry instruction files.** `~/Documents/<org>/` is not a level and not a
  repo, but an agent started there must still load rules and the org's memory, so it
  gets an `AGENTS.md` (owned by the org control) and shares engram project
  `<machine>-<org>`. Every instruction file states the session-start step itself (load
  the rule entries, then `mem_context`), because a pointer chain to the step was
  skipped after restarts.
- **No script configuration.** The script finds its registry from the folder layout,
  talks to the tmux server it runs in, and hard-codes the harness slash commands. An
  agent starts another by typing the resume command from the org root's Environment
  table.
- **After setup, agents shouldn't need to load the skill.** Setup writes each agent's
  instruction file with the standing grant and pointers to the rule entries it loads.
  Small context means each agent loads only what it needs and should.
- **Rules live in engram, loaded by pointer.** Five rule entries in a dedicated engram
  project, `<machine>-control-rules`: one policy per level (`rule/policy-machine`,
  `-org`, `-project`, governance only), `rule/memory`, and `rule/handling-agents`.
  A dedicated project keeps ordinary memories from colliding with a rule key, since a
  save under an existing key replaces the entry, and keeps key searches free of noise.
  Each instruction file has a table naming every entry it loads and the trigger for
  loading it (session start, after a clear, before a save, before handling an agent).
  Engram returns full text only through `mem_get_observation(id)`; search returns
  previews, with an exact `topic_key` match ranked first. So loading is: search the
  key, take the exact `topic_key` match, fetch it by ID. Engram's docs put must-follow
  behaviour in the system prompt; here the instruction file and the wake message carry
  the must-load directive and engram carries the text. Seeds live in
  `templates/rules/`; machine control owns the entries and amends them with
  `mem_update` by ID, the documented safe edit, appending the quoted ruling. chakrit
  syncs worthwhile amendments back to the seeds and handles backups. With
  engram, engram is the only copy: no rule files are written, so edits cost no file
  I/O and nothing drifts. Without engram, setup copies the seeds to
  `~/Documents/control/rules/` as the live rules.
- **Engram project names carry the machine,** like agent names (`<machine>-control`,
  `<machine>-<org>`, `<machine>-<org>-<project>`, `<machine>-control-rules`), so a later
  cross-machine sync would not merge two machines' projects. Nothing syncs today.
  Topic keys stay unprefixed: the project already places them.
- **Procedures compose by name.** `rule/handling-agents` holds the procedures
  controls run on agents (start, message, before a clear, clear, wind down, wake, give
  a task, initiate). Initiation lives there, not only in the skill, so a control can
  bring an agent under control without loading the skill; it loads the skill only when
  the agent's folder needs setup first.
- **Stop means wind down.** chakrit's "stop" for an agent is save, clear, exit the
  harness, exit the shell. `scripts/control-agents wind-down` requires `--saved` like a
  clear and types `exit` only once the shell holds the pane again.
  Policies name its sections instead of restating them, so each rule has one home and a
  caller cannot drop a step such as the save check before a clear.
- **Clears leave evidence.** `scripts/control-agents clear-context` requires
  `--saved <location>`; `force-clear` requires `--ruling` with chakrit's quoted words,
  a last resort for when chakrit orders a clear without a save or approves one because
  the agent is stuck, hung or being torn down. The flag is named for its source, so an
  agent cannot fill it with a reason of its own. Both log to `clears.log`. The script
  cannot verify either value, so the flags are a prompt to run the procedure and an
  audit trail, not proof.
- **Resume, then clear.** Agents start by resuming their previous session because it
  keeps the session's name marker and per-conversation settings, which a new session
  loses. A clear followed by no message does not hold on some harnesses: the next
  resume reopens the conversation before the clear. So waking an agent always clears it
  again, reusing a save already reported instead of asking for another, and sends the
  wake message at once.
- **Registries** are a building block: files a control keeps to track shared things.
  The templates are examples, not a required set.
- **Ports nest; heavy-job slots do not.** Machine control grants port blocks to org
  controls, and org controls sub-allocate to projects. Heavy-job slots are recorded only
  in machine control's registry, holder `<org>:<project>`; org controls relay requests.
- **Two message classes.** Rulings (authority, policy) are chakrit's decisions and are
  applied as given. Task asks may be misread in relay; the receiving agent pushes back
  and the control resolves it with chakrit.
- **Wake-up apart from task-give.** A woken agent loads its context through its own
  session-start skill and reports its state before any task arrives, because an agent
  given both at once may skip orientation. The control checks the task against that
  report before sending it. Task messages carry only what the agent cannot find in its
  own docs, specs and code.
- **Setup plans the level below.** After a machine or org control is set up or
  initiated, it scans one level down for folders that should get controls, asks
  chakrit (or applies chakrit's existing request), lodges the approved setups in
  `control.data.js` and runs them, so the structure is completed rather than grown one
  folder at a time. The new control runs the scan itself. Setup lodges it as a backlog
  row; a parent sends it as a task after the wake, and chakrit triggers it for machine
  control.
- **Controls confirm every new task.** Org and machine controls present a plan and get
  chakrit's confirmation before each new task.
- **Nothing runs upward.** Controls start, message and clear the agents below them. A
  child reaches its parent through the harness's own agent messaging, or asks chakrit
  to start the parent and relay; it never starts a parent or runs its scripts. Machine
  control never acts on a project's pane; it reaches project work through the org
  control, starting and waking it when it is not running.
- **Visible processes.** Agents may start long-running processes, dev and preview
  servers included, only in tmux panes chakrit can see, never in the harness's own
  shell.
- **No submodules.** Projects keep `repos.txt` and `bin/clone-repos`; clones are plain
  and gitignored.
- **Engram first; files for what is read by path or shown.** Engram holds rules,
  knowledge, decisions and their reasoning, agents' state reports and done tasks.
  Registries and live tasks stay in files, for now, because scripts and the control
  page read them by path. Knowledge about one component repo goes in that repo's own
  docs, so it travels with the clone (with the environment's docs skill; none is set
  up without chakrit's permission). Without engram, a `memory/` folder per level holds
  what engram would, one file per topic key. A rule in engram is reliable only because
  pointers name it by topic key and agents load it in full; a rule found by searching
  alone is not guaranteed to apply.
- **Saving names one order:** save before a clear or handoff with the agent's own
  session-save skill when its Environment table names one, otherwise
  engram's `mem_session_summary`; report what was saved and where.
- **`control.html` is the one page chakrit checks,** opened in a local browser. It is
  a fixed template that renders from `control.data.js` beside it, the only live task
  record; there is no separate task file. Agents edit the small data file, never the
  page, to save tokens. The data is JSON wrapped as `window.CONTROL = {...};` and
  loaded with a script tag, because a page opened from disk cannot `fetch` a local
  file. Machine and org controls keep the same three views: Tasks (work only chakrit
  can do), Needs Attention (what an agent waits on, grouped by agent) and Agent
  Backlog (agents' tasks, grouped by status). The page shows no records: a page opened
  from disk cannot read or render other local files, and links to raw Markdown added
  little. Registries stay Markdown files of their own. One template gives every page
  the same look and a vertical rhythm built from row tokens.
  Machine control keeps work across orgs and anything that belongs to no org; it sends
  one org's tasks, including that org's project tasks, to the org control.
- **Single machine.** No sync content anywhere; chakrit manages cross-machine state.
- **Scripts are a small reference,** not a product: one `control-agents` that lists,
  reads and types into registered panes. It targets panes only by tmux ID, re-checks
  the pane before typing, and never changes windows or layout. Before typing it refuses
  when the pane's own shell holds the foreground (the shell's PID equals the terminal's
  foreground process group), instead of matching harness names, so a new harness needs
  no change. It runs through `uv run --script` (Python 3.10 or newer), never the
  system Python. Tests: `uv run --no-project --python '>=3.10' python -B -m unittest
  discover -s tests` from the skill folder. Controls copy it and may adapt it.

Decision provenance (chakrit's words) was recorded during design in this repository's
ignored session ledger, not in the published package.

## Lineage

Conventions and scripts come from chakrit's Data Wow control repo on lz49
(`~/Documents/datawow/control`, commit `ea49ab4`), the most mature control at the time.
Earlier variants: gz44 `~/Documents/control`, gz44 `~/Documents/appbaobao/control`,
lz49 `~/Documents/ircp-sso/control`. The manifest and clone script follow gz44
`~/Documents/naxon-ai` (`repos.txt`, `bin/clone-repos`). Engram rules generalize the
naxon-ai engram decisions.
