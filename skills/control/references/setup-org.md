# Set up an org control

Creates `~/Documents/<org>/control` and its agent `<machine>:<org>:control`. An org
control tracks tasks and keeps project controls in line. It does not hold project
details; project controls own those.

## Steps

1. **Check.** Machine control must exist at `~/Documents/control`; if not, run
   `references/setup-machine.md` first. If `~/Documents/<org>/control` exists, stop
   and tell chakrit.
2. **Confirm the names.** `<org>` is chakrit's short name for the org. Ask him for it
   and for the GitHub org it maps to, unless he already said both.
3. **Create the repo.**

   ```sh
   mkdir -p ~/Documents/<org>/control
   cd ~/Documents/<org>/control
   git init
   ```

4. **Copy templates,** replacing placeholders (`{{machine}}`, `{{org}}`,
   `{{github_org}}`, `{{date}}`):

   | Source                                  | Destination              |
   | --------------------------------------- | ------------------------ |
   | `templates/instructions/org-control.md` | `AGENTS.md`              |
   | `templates/human.md`                    | `human.md`               |
   | `templates/tasks.md`                    | `tasks.md`               |
   | `templates/gitignore`                   | `.gitignore`             |
   | `templates/registries/projects.md`      | `registries/projects.md` |
   | `templates/registries/ports-org.md`     | `registries/ports.md`    |

   Then `ln -s AGENTS.md CLAUDE.md`. Do not copy policy files; the instruction file
   points to the central one.
5. **Copy scripts.** Follow "Install scripts" in `references/operations.md` with
   level `org`.
6. **Set up ACE.** Run `ace setup` with the org's school. Ask chakrit if unsure.
7. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<org>`.
8. **Register with machine control.** Send machine control a message (see
   "Message an agent" in `references/operations.md`) asking it to add the org to
   `registries/orgs.md` and to allocate a port block. Wake it up first if it is not
   running. Record the block it grants in `registries/ports.md`.
9. **Register existing projects.** For each project folder under `~/Documents/<org>/`
   that has an agent, add a row to `registries/projects.md`. Do not create projects.
   Read `references/registries.md` for how registries and nested resources work.
   Existing project agents without a "Control" section get `references/initiation.md`
   once the org control is running.
10. **Commit,** naming the skill revision.
11. **Start the agent** ("Start an agent" in `references/operations.md`) and rename
    its session to `<machine>:<org>:control`.

## Done when

The completion list in `SKILL.md` holds, and machine control's `registries/orgs.md`
lists the org with its port block.
