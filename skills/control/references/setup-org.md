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
   `{{github_org}}`, `{{date}}`, and `{{title}}` with `<org> Control`):

   | Source                                  | Destination              |
   | --------------------------------------- | ------------------------ |
   | `templates/instructions/org-control.md` | `AGENTS.md`              |
   | `templates/control.html`                | `control.html`           |
   | `templates/gitignore`                   | `.gitignore`             |
   | `templates/registries/projects.md`      | `registries/projects.md` |
   | `templates/registries/ports-org.md`     | `registries/ports.md`    |

   Then `ln -s AGENTS.md CLAUDE.md`. Do not copy policy files; the instruction file
   points to the central one. In `control.html`, under Records, link `AGENTS.md`,
   `../../control/policies/org-control.md`, `../../control/policies/memory.md` and each
   file in `registries/`. Under Links, link `../../control/control.html` as
   "Machine control".
5. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
6. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<org>`.
7. **Register with machine control.** Ask machine control to add the org to
   `registries/orgs.md`, to link this org's `control.html` from its own, and to
   allocate a port block (see "Reach
   a parent" in `references/operations.md`). Record the block it grants in
   `registries/ports.md`.
8. **Register existing projects.** For each project folder under `~/Documents/<org>/`
   that has an agent, add a row to `registries/projects.md`. Do not create projects.
   Read `references/registries.md` for how registries and nested resources work.
   Existing project agents without a "Control" section get `references/initiation.md`
   once the org control is running.
9. **Commit,** naming the skill revision.
10. **Start the agent** ("Start an agent" in `references/operations.md`) and rename
   its session to `<machine>:<org>:control`.

## Done when

The completion list in `SKILL.md` holds, and machine control's `registries/orgs.md`
lists the org with its port block.
