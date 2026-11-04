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
- **After setup, agents never load the skill.** Setup writes each agent's instruction
  file with the standing grant and a pointer to its level's policy file. Small context
  means each agent loads only what it needs and should.
- **Policies:** one file per level, loaded whole, governance only, stored only in
  `~/Documents/control/policies/`. Machine control owns and amends them on chakrit's
  rulings. Individual-agent rules stay in that agent's own files.
- **Registries** are a building block: files a control keeps to track shared things.
  The templates are examples, not a required set.
- **Resources nest.** Machine control grants port blocks and heavy-job slots to org
  controls; org controls sub-allocate to projects.
- **Two message classes.** Rulings (authority, policy) are chakrit's decisions and are
  applied as given. Task asks may be misread in relay; the receiving agent pushes back
  and the control resolves it with chakrit.
- **Wake-up runs upward.** An agent that needs its parent starts it. Machine control
  manages project panes directly when the org control is down, unless waking the org
  control is faster or needs its context.
- **Visible processes.** chakrit's global "leave server startup to me" is exempt in this
  setup; every long-running process runs in a visible tmux pane instead.
- **No submodules.** Projects keep `repos.txt` and `bin/clone-repos`; clones are plain
  and gitignored.
- **Engram-first memory** at all levels; files only for policies, registries, the task
  ledger and the waiting page. Repo-only knowledge goes to the repo's ace-docs, which
  is never set up without chakrit's permission.
- **Single machine.** No sync content anywhere; chakrit manages cross-machine state.
- **Scripts:** one canonical copy here, copied into each control and customized
  locally. Refreshing is a merge against the revision recorded in `scripts/SOURCE`.

Decision provenance (chakrit's words) was recorded during design in this repository's
ignored session ledger, not in the published package.

## Lineage

Conventions and scripts come from chakrit's Data Wow control repo on lz49
(`~/Documents/datawow/control`, commit `ea49ab4`), the most mature control at the time.
Earlier variants: gz44 `~/Documents/control`, gz44 `~/Documents/appbaobao/control`,
lz49 `~/Documents/ircp-sso/control`. The manifest and clone script follow gz44
`~/Documents/naxon-ai` (`repos.txt`, `bin/clone-repos`). Engram rules generalize the
naxon-ai engram decisions.
