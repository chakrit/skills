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
   (`{{machine}}`, `{{date}}`, and `{{title}}` with `<MACHINE> Control` in capitals,
   such as `LZ49 Control`):

   | Source                                      | Destination                   |
   | ------------------------------------------- | ----------------------------- |
   | `templates/instructions/machine-control.md` | `AGENTS.md`                   |
   | `templates/policies/machine-control.md`     | `policies/machine-control.md` |
   | `templates/policies/org-control.md`         | `policies/org-control.md`     |
   | `templates/policies/project-control.md`     | `policies/project-control.md` |
   | `templates/policies/memory.md`              | `policies/memory.md`          |
   | `templates/control.html`                    | `control.html`                |
   | `templates/gitignore`                       | `.gitignore`                  |
   | `templates/registries/orgs.md`              | `registries/orgs.md`          |
   | `templates/registries/ports-machine.md`     | `registries/ports.md`         |
   | `templates/registries/heavy-jobs.md`        | `registries/heavy-jobs.md`    |

   Then `ln -s AGENTS.md CLAUDE.md`. In `control.html`, under Records, link
   `AGENTS.md`, each file in `policies/` and each file in `registries/`.
4. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
5. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `control`.
6. **Register existing orgs.** For each folder `~/Documents/<org>/control` that
   already exists, add a row to `registries/orgs.md` and a link to its
   `control.html` under Links in `control.html`. Read `references/registries.md` for
   how registries and nested resources work.
7. **Commit.** Commit everything with a message naming the skill revision
   (`git -C <this skill's repo> rev-parse --short HEAD`).
8. **Start the agent.** Follow "Start an agent" in `references/operations.md`, then
   rename its session to `<machine>:control`.
9. **Plan downstream.** Follow "Plan downstream controls" in
   `references/operations.md` for org candidates under `~/Documents/`.

## Done when

The completion list in `SKILL.md` holds, and `policies/` contains the three level
policies and `memory.md`.
