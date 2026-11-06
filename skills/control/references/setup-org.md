# Set up an org control

Creates the org folder's control structure: the org root's instruction files in
`~/Documents/<org>/`, the org control repo `~/Documents/<org>/control` and its agent
`<machine>:<org>:control`. An org control tracks tasks and keeps project controls in
line. It does not hold project details; project controls own those.

## Steps

1. **Check.** Machine control must exist at `~/Documents/control`; if not, run
   `references/setup-machine.md` first. If `~/Documents/<org>/control` already exists,
   do only the steps whose result is missing and never replace an existing file. If it
   already has `AGENTS.md` or `CLAUDE.md`, never write or link either file: "Initiate an
   agent" sends the `## Control` section, since the agent writes its own instructions.
   When this setup runs for "Initiate an agent" and writes a missing `AGENTS.md`, leave
   out its `## Control` section, down to the next `##` heading, for the same reason.
2. **Work out the names.** `<org>` is the user's short name for the org and maps to a
   GitHub org that may be named differently. The user's request usually holds both
   ("set up fi/ to manage my Forward Insight stuff"); otherwise find them from the
   environment (the org's repos and their remotes, `gh`). Flag the user only when you
   cannot settle one. Then follow "Record the environment" in
   `references/operations.md` for the org.
3. **Create the repo.**

   ```sh
   mkdir -p ~/Documents/<org>/control
   cd ~/Documents/<org>/control
   git init
   ```

4. **Copy templates,** replacing placeholders (`{{machine}}`, `{{org}}`,
   `{{github_org}}`, `{{date}}` as `YYYY-MM-DD`, `{{home}}` with the home folder path
   such as `/Users/chakrit`, and `{{title}}` with `<org> Control`):

   | Source                                  | Destination                |
   | --------------------------------------- | -------------------------- |
   | `templates/instructions/org-control.md` | `AGENTS.md`                |
   | `templates/control.html`                | `control.html`             |
   | `templates/control.data.js`             | `control.data.js`          |
   | `templates/gitignore`                   | `.gitignore`               |
   | `templates/registries/projects.md`      | `registries/projects.md`   |
   | `templates/registries/ports-org.md`     | `registries/ports.md`      |

   Then `ln -s AGENTS.md CLAUDE.md`. Do not copy rule files; the instruction file
   points to the engram entries machine control keeps. In `control.data.js`, under
   links, link
   `../../control/control.html` as "Machine control". Follow "Point the control page at
   PragmataPro" in `references/operations.md`.
5. **Org root.** Copy `templates/instructions/org-root.md` to
   `~/Documents/<org>/AGENTS.md` with the same placeholders and the Environment
   placeholders, and run `ln -s AGENTS.md CLAUDE.md` there. The org root is not a git
   repo; never run `git init` in it.
6. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
7. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<machine>-<org>`, once in `~/Documents/<org>/control` and once in
   `~/Documents/<org>/`. Both folders share the org's memory.
8. **ACE.** Follow "Onboard into ACE" in `references/operations.md` for the org control
   and the org root.
9. **Register with machine control.** The org needs a row and a `## GitHub orgs` line
   in machine control's `registries/orgs.md`, a link in machine control's
   `control.data.js`, and a port block. If you are machine control, add them yourself
   and commit in `~/Documents/control`. Otherwise ask machine control (see "Reach a
   parent" in `references/operations.md`). Record the block in `registries/ports.md`.
   When this setup runs for "Initiate an agent", add only the row, the GitHub orgs line
   and the link; initiation grants the block.
10. **Register existing projects.** For each project folder under `~/Documents/<org>/`
    that has an agent, add a row to `registries/projects.md`, with Window and Agent
    pane filled when you see its pane and empty otherwise. Read
    `references/registries.md` for how registries and nested resources work. When this
    setup runs for "Initiate an agent", skip this step: the org control keeps its own
    registry, and its planning task registers what is missing.
11. **Lodge downstream planning.** Add an Agent Backlog row to `control.data.js` (group
    `todo`): item "Plan downstream controls (`control` skill,
    `references/operations.md`)", agent `<machine>:<org>:control`, source the user's
    request, next "after first start". When this setup runs for "Initiate an agent",
    skip this step; initiation sends the planning as a task.
12. **Commit** what this setup wrote, naming the skill revision.
13. **Start the agent.** When this setup runs for "Initiate an agent", skip this step;
    initiation starts, wakes and tasks the agent. If you are machine control, follow
    "Wake up an agent" in `rule/handling-agents` (it starts the agent and renames its
    session to `<machine>:<org>:control`), then send "Plan downstream controls" as its
    task ("Give a task"). Otherwise add to the completion report: "Start the org
    control: in a tmux window, `cd ~/Documents/<org>/control`, start a new session the
    way you start agents in this org, then `/rename <machine>:<org>:control`. Then ask
    it to run its backlog row 'Plan downstream controls'."

## Done when

The completion list in `SKILL.md` holds, `~/Documents/<org>/AGENTS.md` exists with
`CLAUDE.md` linked to it, and machine control's `registries/orgs.md` lists the org.
Outside initiation, machine control's `registries/ports.md` also lists its port block.
