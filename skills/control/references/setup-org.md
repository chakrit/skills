# Set up an org control

Puts the org control repo `~/Documents/<org>/control` in place for its agent
`<machine>:<org>:control`. Setup only creates the folder and copies templates; the
agent takes over its own files when it is initiated. An org control tracks tasks and
keeps project controls in line. It does not hold project details; project controls own
those.

## Steps

1. **Check.** Machine control must exist at `~/Documents/control`; if not, run
   `references/setup-machine.md` first. Never replace or edit an existing file in
   `~/Documents/<org>/control`.
2. **Work out the names.** `<org>` is the user's short name for the org and maps to a
   GitHub org that may be named differently. The user's request usually holds both
   ("set up fi/ to manage my Forward Insight stuff"); otherwise find them from the
   environment (the org's repos and their remotes, `gh`). Flag the user only when you
   cannot settle one.
3. **Get the folder.** If it exists, use it, and run `git init` in it when it is not a
   git repo. Otherwise:

   ```sh
   mkdir -p ~/Documents/<org>/control
   cd ~/Documents/<org>/control
   git init
   ```

4. **ACE.** Follow "Onboard into ACE" in `references/operations.md`.
5. **Copy templates as they are,** each only when its destination is missing. Fill in
   nothing: the agent replaces the template values when it is initiated.

   | Source                                  | Destination              |
   | --------------------------------------- | ------------------------ |
   | `templates/instructions/org-control.md` | `AGENTS.md`              |
   | `templates/control.html`                | `control.html`           |
   | `templates/control.data.js`             | `control.data.js`        |
   | `templates/gitignore`                   | `.gitignore`             |
   | `templates/registries/projects.md`      | `registries/projects.md` |
   | `templates/registries/ports-org.md`     | `registries/ports.md`    |

   Copy `AGENTS.md` only when the folder has neither `AGENTS.md` nor `CLAUDE.md`, then
   run `ln -s AGENTS.md CLAUDE.md`. Do not copy rule files; the instruction file points
   to the engram entries machine control keeps.
6. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
7. **Initiate.** If you came here from "Initiate an agent", return there. If you are
   machine control, follow "Initiate an agent" in `rule/handling-agents`. Otherwise
   add to the completion report: "Ask `<machine>:control` to initiate
   `<machine>:<org>:control` in `~/Documents/<org>/control`."

## Done when

The completion list in `SKILL.md` holds.
