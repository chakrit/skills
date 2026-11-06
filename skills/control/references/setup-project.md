# Set up a project control

Creates `~/Documents/<org>/<project>`, a local project repo that holds the project's
component repos as plain clones, and its agent `<machine>:<org>:<project>`. The project
control owns the project's context and may do hands-on work in its clones.

## Steps

1. **Check.** The org control must exist at `~/Documents/<org>/control`; if not, run
   `references/setup-org.md` first. If the project folder already exists, this setup
   runs for "Initiate an agent": do only the steps whose result is missing, never
   replace an existing file, and leave the `## Control` section to the initiation
   message, since the agent writes its own instructions.
2. **Confirm the names.** `<project>` is chakrit's short name for the project. Ask
   chakrit for it and for the list of component repos, unless chakrit already gave both.
3. **Create the repo.**

   ```sh
   mkdir -p ~/Documents/<org>/<project>
   cd ~/Documents/<org>/<project>
   git init
   ```

   The project repo stays local. Never add a remote unless chakrit asks.
4. **Copy templates,** replacing placeholders (`{{machine}}`, `{{org}}`, `{{project}}`):

   | Source                                      | Destination       |
   | ------------------------------------------- | ----------------- |
   | `templates/instructions/project-control.md` | `AGENTS.md`       |
   | `templates/gitignore`                       | `.gitignore`      |
   | `templates/project/repos.txt`               | `repos.txt`       |
   | `templates/project/clone-repos`             | `bin/clone-repos` |

   Then `ln -s AGENTS.md CLAUDE.md` and `chmod +x bin/clone-repos`.
5. **List the clones.** Write one line per component repo in `repos.txt`:
   `<repo-name> <clone-url>`. The folder name is the exact GitHub repo name. Never use
   git submodules.
6. **Clone.** Run `bin/clone-repos`. It clones missing repos and adds each folder to
   `.gitignore`.
7. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<machine>-<org>-<project>`.
8. **ACE.** Follow "Onboard into ACE" in `references/operations.md`.
9. **Register with the org control.** The project needs a row in the org control's
   `registries/projects.md` and a port block. If you are the org control, add the row,
   grant the block in your `registries/ports.md`, and commit in your repo. Otherwise ask
   the org control (see "Reach a parent" in `references/operations.md`). Write the
   block into `AGENTS.md` under "Ports".
10. **Commit,** naming the skill revision.
11. **Start the agent.** If you are the org control, follow "Start an agent" in
    `rule/handling-agents` and rename its session to `<machine>:<org>:<project>`.
    Otherwise add to the completion report: "Start the project control: in a tmux
    window, `cd ~/Documents/<org>/<project>`, type the resume command from the org
    root's Environment table, then `/rename <machine>:<org>:<project>`."

## Done when

The completion list in `SKILL.md` holds, every repo in `repos.txt` is cloned and
ignored, and the org control's projects registry lists the project.
