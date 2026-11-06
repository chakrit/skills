# Set up an org control

Creates `~/Documents/<org>/control` and its agent `<machine>:<org>:control`. An org
control tracks tasks and keeps project controls in line. It does not hold project
details; project controls own those.

## Steps

1. **Check.** Machine control must exist at `~/Documents/control`; if not, run
   `references/setup-machine.md` first. If `~/Documents/<org>/control` exists, stop
   and tell chakrit.
2. **Confirm the names.** `<org>` is chakrit's short name for the org. Ask chakrit for
   it and for the GitHub org it maps to, unless chakrit already said both.
3. **Create the repo.**

   ```sh
   mkdir -p ~/Documents/<org>/control
   cd ~/Documents/<org>/control
   git init
   ```

4. **Copy templates,** replacing placeholders (`{{machine}}`, `{{org}}`,
   `{{github_org}}`, `{{date}}`, `{{home}}` with the home folder path such as
   `/Users/chakrit`, and `{{title}}` with `<org> Control`):

   | Source                                  | Destination              |
   | --------------------------------------- | ------------------------ |
   | `templates/instructions/org-control.md` | `AGENTS.md`              |
   | `templates/control.html`                | `control.html`           |
   | `templates/control.data.js`             | `control.data.js`        |
   | `templates/gitignore`                   | `.gitignore`             |
   | `templates/registries/projects.md`      | `registries/projects.md` |
   | `templates/registries/ports-org.md`     | `registries/ports.md`    |

   Then `ln -s AGENTS.md CLAUDE.md`. Do not copy rule files; the instruction file
   points to the engram entries machine control keeps. In `control.data.js`, under
   links, link `../../control/control.html` as "Machine control".
5. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
6. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<machine>-<org>`.
7. **Register with machine control.** Ask machine control to add the org to
   `registries/orgs.md`, to link this org's `control.html` from its own, and to
   allocate a port block (see "Reach a parent" in `references/operations.md`). Record
   the block it grants in `registries/ports.md`.
8. **Register existing projects.** For each project folder under `~/Documents/<org>/`
   that has an agent, add a row to `registries/projects.md`. Read
   `references/registries.md` for how registries and nested resources work.
9. **Commit,** naming the skill revision.
10. **Start the agent** ("Start an agent" in `templates/rules/handling-agents.md`) and
    rename its session to `<machine>:<org>:control`.
11. **Plan downstream.** Follow "Plan downstream controls" in
    `references/operations.md` for project candidates under `~/Documents/<org>/`,
    including existing project agents that need initiation.

## Done when

The completion list in `SKILL.md` holds, and machine control's `registries/orgs.md`
lists the org with its port block.
