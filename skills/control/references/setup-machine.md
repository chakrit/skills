# Set up machine control

Creates `~/Documents/control`, the machine control repo, and its agent
`<machine>:control`. Machine control holds the least context: machine-wide tasks, the
rule entries every level loads, and the machine's shared resources.

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

   | Source                                      | Destination                |
   | ------------------------------------------- | -------------------------- |
   | `templates/instructions/machine-control.md` | `AGENTS.md`                |
   | `templates/control.html`                    | `control.html`             |
   | `templates/control.data.js`                 | `control.data.js`          |
   | `templates/gitignore`                       | `.gitignore`               |
   | `templates/registries/orgs.md`              | `registries/orgs.md`       |
   | `templates/registries/ports-machine.md`     | `registries/ports.md`      |
   | `templates/registries/heavy-jobs.md`        | `registries/heavy-jobs.md` |

   Then `ln -s AGENTS.md CLAUDE.md`. In `control.data.js`, under records, link
   `AGENTS.md` and each file in `registries/`.
4. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
5. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `control`, then "Seed the rule entries" in the same file.
6. **Register existing orgs.** For each folder `~/Documents/<org>/control` that
   already exists, add a row to `registries/orgs.md` and a link to its
   `control.html` under links in `control.data.js`. Read `references/registries.md`
   for how registries and nested resources work.
7. **Commit.** Commit everything with a message naming the skill revision
   (`git -C <this skill's repo> rev-parse --short HEAD`).
8. **Start the agent.** Follow "Start an agent" in `templates/rules/handling-agents.md`,
   then rename its session to `<machine>:control`.
9. **Plan downstream.** Follow "Plan downstream controls" in
   `references/operations.md` for org candidates under `~/Documents/`.

## Done when

The completion list in `SKILL.md` holds. With engram, each of the five rule entries is
found by `mem_search` in project `control` and no `rules/` folder exists. Without
engram, `rules/` holds the five rule files.
