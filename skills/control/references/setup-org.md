# Set up an org control

Creates the org folder's control structure: the org root's instruction files in
`~/Documents/<org>/`, the org control repo `~/Documents/<org>/control` and its agent
`<machine>:<org>:control`. An org control tracks tasks and keeps project controls in
line. It does not hold project details; project controls own those.

## Steps

1. **Check.** Machine control must exist at `~/Documents/control`; if not, run
   `references/setup-machine.md` first. If `~/Documents/<org>/control` already exists,
   this setup runs for "Initiate an agent": do only the steps whose result is missing,
   and never replace an existing file.
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

   | Source                                  | Destination                |
   | --------------------------------------- | -------------------------- |
   | `templates/instructions/org-control.md` | `AGENTS.md`                |
   | `templates/control.html`                | `control.html`             |
   | `templates/control.data.js`             | `control.data.js`          |
   | `templates/gitignore`                   | `.gitignore`               |
   | `templates/registries/projects.md`      | `registries/projects.md`   |
   | `templates/registries/ports-org.md`     | `registries/ports.md`      |
   | `templates/registries/heavy-jobs.md`    | `registries/heavy-jobs.md` |

   Then `ln -s AGENTS.md CLAUDE.md`. `registries/heavy-jobs.md` starts with every
   holder `none`; it records the project holding a slot machine control granted the
   org. Do not copy rule files; the instruction file points to the engram entries
   machine control keeps. In `control.data.js`, under links, link
   `../../control/control.html` as "Machine control". Follow "Point the control page at
   PragmataPro" in `references/operations.md`.
5. **Org root.** Copy `templates/instructions/org-root.md` to
   `~/Documents/<org>/AGENTS.md` with the same placeholders, and run
   `ln -s AGENTS.md CLAUDE.md` there. The org root is not a git repo; never run
   `git init` in it.
6. **Copy scripts.** Follow "Install scripts" in `references/operations.md`.
7. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<machine>-<org>`, once in `~/Documents/<org>/control` and once in
   `~/Documents/<org>/`. Both folders share the org's memory.
8. **ACE.** Follow "Onboard into ACE" in `references/operations.md` for the org control
   and the org root.
9. **Register with machine control.** Ask machine control to add the org to
   `registries/orgs.md`, to link this org's `control.html` from its own, and to
   allocate a port block (see "Reach a parent" in `references/operations.md`). Record
   the block it grants in `registries/ports.md`.
10. **Register existing projects.** For each project folder under `~/Documents/<org>/`
    that has an agent, add a row to `registries/projects.md`, with Window and Agent
    pane empty unless it is running. Read `references/registries.md` for how
    registries and nested resources work.
11. **Commit,** naming the skill revision.
12. **Start the agent.** If you are machine control, follow "Start an agent" in
    `rule/handling-agents` and rename its session to `<machine>:<org>:control`.
    Otherwise add to the completion report: "Start the org control: in a tmux window,
    `cd ~/Documents/<org>/control`, run the harness, then type
    `/rename <machine>:<org>:control`."
13. **Plan downstream.** Once the org control runs, it follows "Plan downstream
    controls" in `references/operations.md` for project candidates under
    `~/Documents/<org>/`, including existing project agents that need initiation.

## Done when

The completion list in `SKILL.md` holds, `~/Documents/<org>/AGENTS.md` exists with
`CLAUDE.md` linked to it, and machine control's `registries/orgs.md` lists the org with
its port block.
