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
- **No ACE dependency.** The skill works for users without ACE or its save skill.
- **No script configuration.** The script finds its registry from the folder layout,
  talks to the tmux server it runs in, and hard-codes Claude Code's commands. An agent
  starts another by typing the harness the registry names.
- **After setup, agents shouldn't need to load the skill.** Setup writes each agent's
  instruction file with the standing grant and pointers to the rule entries it loads.
  Small context means each agent loads only what it needs and should.
- **Rules live in engram, loaded by pointer.** Five rule entries in engram project
  `control`: one policy per level (`control/policy-machine`, `-org`, `-project`,
  governance only), `control/memory`, and `control/handling-agents`. Each instruction
  file has a table naming every entry it loads and the trigger for loading it (session
  start, after a clear, before a save, before handling an agent), loaded in full with
  `mem_search` then `mem_get_observation`. The wake message repeats the entries to
  load, so the reminder is in the agent's context at once. Seeds live in
  `templates/rules/`; machine control owns the entries and amends them on chakrit's
  rulings, with the quoted ruling in the entry. With engram, engram is the only copy:
  no rule files are written, so edits cost no file I/O and nothing drifts. Without
  engram, setup copies the seeds to `~/Documents/control/rules/` as the live rules.
- **Procedures compose by name.** `control/handling-agents` holds the procedures
  controls run on agents (start, message, before a clear, clear, wake, give a task).
  Policies name its sections instead of restating them, so each rule has one home and a
  caller cannot drop a step such as the save check before a clear.
- **Clears leave evidence.** `scripts/control-agents clear-context` requires
  `--saved <location>`; `force-clear` requires `--reason` and is allowed only when
  chakrit orders it, the agent is stuck or hung, agents are being torn down, or a
  similar circumstance requires it. Both log to `clears.log`. The script cannot verify
  either value, so the flags are a prompt to run the procedure and an audit trail, not
  proof.
- **Resume, then clear.** Agents start by resuming their previous session because it
  keeps the session's name marker and per-conversation settings, which a new session
  loses. A clear followed by no message does not hold on some harnesses: the next
  resume reopens the conversation before the clear. So waking an agent always clears it
  again, reusing a save already reported instead of asking for another, and sends the
  wake message at once.
- **Registries** are a building block: files a control keeps to track shared things.
  The templates are examples, not a required set.
- **Resources nest.** Machine control grants port blocks and heavy-job slots to org
  controls; org controls sub-allocate to projects.
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
  folder at a time.
- **Controls confirm every new task.** Org and machine controls present a plan and get
  chakrit's confirmation before each new task.
- **Nothing runs upward.** Controls start, message and clear the agents below them. A
  child reaches its parent through the harness's own agent messaging, or asks chakrit
  to start the parent and relay; it never starts a parent or runs its scripts. Machine
  control manages project panes directly when the org control is down, unless waking
  the org control is faster or needs its context.
- **Visible processes.** chakrit's global "leave server startup to me" is exempt in this
  setup; every long-running process runs in a visible tmux pane instead.
- **No submodules.** Projects keep `repos.txt` and `bin/clone-repos`; clones are plain
  and gitignored.
- **Engram first; files for what is read by path or shown.** Engram holds rules,
  knowledge, decisions and their reasoning, agents' state reports and done tasks.
  Registries and live tasks stay in files, for now, because scripts and the control
  page read them by path. Knowledge about one component repo goes in that repo's own
  docs, so it travels with the clone (`ace-docs` where ACE exists; none is set up
  without chakrit's permission). Without engram, a `memory/` folder per level holds
  what engram would, one file per topic key. A rule in engram is reliable only because
  pointers name it by topic key and agents load it in full; a rule found by searching
  alone is not guaranteed to apply.
- **Saving names one preference:** save before a clear or handoff, prefer engram's
  `mem_session_summary`, report what was saved and where.
- **`control.html` is the one page chakrit checks,** opened in a local browser. It is
  a fixed template that renders from `control.data.js` beside it, the only live task
  record; there is no separate task file. Agents edit the small data file, never the
  page, to save tokens. The data is JSON wrapped as `window.CONTROL = {...};` and
  loaded with a script tag, because a page opened from disk cannot `fetch` a local
  file. Machine and org controls keep the same three views: Tasks (work only chakrit
  can do), Needs Attention (what an agent waits on, grouped by agent) and Agent
  Backlog (agents' tasks, grouped by status). Registries stay Markdown; the page links
  them rather than rendering them, so a port or heavy-job change touches one file. One
  template gives every page the same look and a vertical rhythm built from row tokens.
  Machine control keeps work across orgs and anything that belongs to no org; it sends
  one org's tasks, including that org's project tasks, to the org control.
- **Single machine.** No sync content anywhere; chakrit manages cross-machine state.
- **Scripts are a small reference,** not a product: one `control-agents` that lists,
  reads and types into registered panes. It targets panes only by tmux ID, re-checks
  the pane before typing, and never changes windows or layout. Controls copy it and
  may adapt it.

Decision provenance (chakrit's words) was recorded during design in this repository's
ignored session ledger, not in the published package.

## Lineage

Conventions and scripts come from chakrit's Data Wow control repo on lz49
(`~/Documents/datawow/control`, commit `ea49ab4`), the most mature control at the time.
Earlier variants: gz44 `~/Documents/control`, gz44 `~/Documents/appbaobao/control`,
lz49 `~/Documents/ircp-sso/control`. The manifest and clone script follow gz44
`~/Documents/naxon-ai` (`repos.txt`, `bin/clone-repos`). Engram rules generalize the
naxon-ai engram decisions.
