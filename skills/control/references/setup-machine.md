# Set up machine control

Creates `~/Documents/control`, the machine control repo, and its agent
`<machine>:control`. Machine control holds the least context: machine-wide tasks, the
policies, and the machine's shared resources.

## Steps

1. **Check.** If `~/Documents/control` exists, stop and tell chakrit; do not overwrite.
   Get `<machine>` with `hostname -s`, lowercased.
2. **Create the repo.**

   ```sh
   mkdir ~/Documents/control
   cd ~/Documents/control
   git init
   ```

3. **Copy templates.** Copy from this skill's directory, replacing placeholders
   (`{{machine}}`, `{{date}}`):

   | Source                                   | Destination                        |
   | ---------------------------------------- | ---------------------------------- |
   | `templates/instructions/machine-control.md` | `AGENTS.md`                     |
   | `templates/policies/machine-control.md`  | `policies/machine-control.md`      |
   | `templates/policies/org-control.md`      | `policies/org-control.md`          |
   | `templates/policies/project-control.md`  | `policies/project-control.md`      |
   | `templates/human.md`                     | `human.md`                         |
   | `templates/tasks.md`                     | `tasks.md`                         |
   | `templates/gitignore`                    | `.gitignore`                       |
   | `templates/registries/orgs.md`           | `registries/orgs.md`               |
   | `templates/registries/ports-machine.md`  | `registries/ports.md`              |
   | `templates/registries/heavy-jobs.md`     | `registries/heavy-jobs.md`         |

   Then `ln -s AGENTS.md CLAUDE.md`.
4. **Copy scripts.** Follow "Install scripts" in `references/operations.md` with
   level `machine`.
5. **Set up ACE.** Run `ace setup` in the folder and pick the school chakrit names.
   If you cannot tell which school, ask him.
6. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `control`. If engram is installed, also save the sections "Where
   knowledge goes" and "Saving a memory" of `references/memory.md` as one `spec`
   memory in project `control`, topic key `policies/memory`, title "policies memory:
   engram types, topic keys, titles, keywords". Every policy points agents to it.
7. **Register existing orgs.** For each folder `~/Documents/<org>/control` that
   already exists, add a row to `registries/orgs.md`. Do not create org controls.
   Read `references/registries.md` for how registries and nested resources work.
8. **Commit.** Commit everything with a message naming the skill revision
   (`git -C <this skill's repo> rev-parse --short HEAD`).
9. **Start the agent.** Follow "Start an agent" in `references/operations.md`, then
   rename its session to `<machine>:control`.

## Done when

The completion list in `SKILL.md` holds, and `policies/` contains all three policy
files.
