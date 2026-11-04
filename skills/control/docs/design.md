# control: design notes

Maintainer notes for the `control` skill. Agents running the skill do not read this.

## What it is

One skill, invoked in different folders, that sets up chakrit's agent coordination
structure on a single machine: three fixed levels of control agents in tmux, central
governance policies, registries, and a shared engram memory. It replaces copying and
adapting control repos between orgs and machines.

## Decisions

- **Three fixed levels, no recursion.** Machine control (`~/Documents/control`), org
  control (`~/Documents/<org>/control`), project control (`~/Documents/<org>/<project>`).
  Naming every level removes later decisions about what a "control" is.
- **Higher levels hold less context.** Machine control does machine-wide tasks only.
  Org controls track tasks and alignment, not project details. Project controls own
  project context and may do hands-on work.
- **Agent names:** `<machine>:control`, `<machine>:<org>:control`,
  `<machine>:<org>:<project>`. The org slug is chakrit's short name (`datawow`).
- **No ACE dependency.** The skill works for users without ACE or its save skill.
- **No script configuration.** The script finds its registry from the folder layout,
  talks to the tmux server it runs in, and hard-codes Claude Code's commands. An agent
  starts another by typing the harness the registry names.
- **After setup, agents shouldn't need to load the skill.** Setup writes each agent's
  instruction file with the standing grant and a pointer to its level's policy file.
  Small context means each agent loads only what it needs and should.
- **Policies:** one file per level plus `memory.md`, loaded whole, governance only, in
  `~/Documents/control/policies/`. Machine control owns and amends them on chakrit's
  rulings. Individual-agent rules stay in that agent's own files.
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
- **Files versus engram.** What an agent must follow every time, and durable state
  such as registries, lives in files loaded by path. What an agent recalls when
  relevant lives in engram, which is searched and so never guarantees a rule applies.
  The memory rules are themselves a policy file, `policies/memory.md`. Repo-only
  knowledge follows the repo's own docs convention; none is set up without chakrit's
  permission.
- **Saving names one preference:** save before a clear or handoff, prefer engram's
  `mem_session_summary`, report what was saved and where.
- **`human.html` is chakrit's control center and the only task tracker,** a static
  page opened in a local browser. It holds what is owed to chakrit, so task tracking
  lives there too; there is no separate task ledger. Each org control's shows what
  needs chakrit, its tasks and what is going on. Machine control's holds the same
  for machine-wide work, links to the org pages and shows the machine registries.
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
