# Set up machine control

Creates `~/Documents/control`, the machine control repo, and its agent
`<machine>:control`. Machine control holds the least context: machine-wide tasks, the
rule entries every level loads, and the machine's shared resources.

## Steps

1. **Check.** If `~/Documents/control` exists, stop and tell the user; do not overwrite.
   Get `<machine>` with `hostname -s`, lowercased.
2. **Create the repo.**

   ```sh
   mkdir ~/Documents/control
   cd ~/Documents/control
   git init
   ```

3. **Copy templates.** First follow "Record the environment" in
   `references/operations.md` for machine control. Copy from this skill's directory,
   replacing placeholders (`{{machine}}`, `{{date}}` as `YYYY-MM-DD`, `{{home}}` with
   the home folder path such as `/Users/chakrit`, `{{title}}` with `<MACHINE> Control`
   in capitals, such as `LZ49 Control`, and the Environment placeholders):

   | Source                                      | Destination                |
   | ------------------------------------------- | -------------------------- |
   | `templates/instructions/machine-control.md` | `AGENTS.md`                |
   | `templates/control.html`                    | `control.html`             |
   | `templates/control.data.js`                 | `control.data.js`          |
   | `templates/gitignore`                       | `.gitignore`               |
   | `templates/registries/orgs.md`              | `registries/orgs.md`       |
   | `templates/registries/ports-machine.md`     | `registries/ports.md`      |
   | `templates/registries/heavy-jobs.md`        | `registries/heavy-jobs.md` |

   Then `ln -s AGENTS.md CLAUDE.md`, and follow "Point the control page at
   PragmataPro" in `references/operations.md`.
4. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
5. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<machine>-control`, then "Seed the rule entries" in the same file.
6. **Register existing orgs.** For each folder `~/Documents/<org>/control` that
   already exists, add a row and a `## GitHub orgs` line to `registries/orgs.md` and a
   link to its `control.html` under links in `control.data.js`. Find out each org's
   GitHub org, and flag the user only when you cannot. Read `references/registries.md`
   for how registries and nested resources work.
7. **ACE.** Follow "Onboard into ACE" in `references/operations.md`.
8. **Lodge downstream planning.** Add an Agent Backlog row to `control.data.js` (group
   `todo`): item "Plan downstream controls (`control` skill, `references/operations.md`)",
   agent `<machine>:control`, source the user's request, next "after first start".
9. **Commit.** Commit everything with a message naming the skill revision
   (`git -C <this skill's repo> rev-parse --short HEAD`).
10. **Leave the start to the user.** Machine control has no parent control to start it.
    Add to the completion report: "Start machine control: in a tmux window, `cd
    ~/Documents/control`, start a new session the way you start agents on this machine,
    then `/rename <machine>:control`. Then ask it to run its backlog row 'Plan downstream
    controls'."

## Done when

The completion list in `SKILL.md` holds. With engram, each of the five rule entries
loads by exact topic key from project `<machine>-control-rules`, and no `rules/` folder
exists. Without engram, `rules/` holds the five rule files.
