# Set up a project control

Creates `~/Documents/<org>/<project>`, a local project repo that holds the project's
component repos as plain clones, and its agent `<machine>:<org>:<project>`. The project
control owns the project's context and may do hands-on work in its clones.

## Steps

1. **Check.** The org control must exist at `~/Documents/<org>/control`; if not, run
   `references/setup-org.md` first. If the project folder already exists, do only the
   steps whose result is missing and never replace an existing file. If it already has
   `AGENTS.md` or `CLAUDE.md`, never write or link either file, including their
   `## Repos` rows and Ports: "Initiate an agent" sends the `## Control` section, since
   the agent writes its own instructions. When this setup runs for "Initiate an agent"
   and writes a missing `AGENTS.md`, leave out its `## Control` section, down to the
   next `##` heading, for the same reason.
2. **Work out the names.** `<project>` is chakrit's short name for the project.
   chakrit's request usually holds it and the component repos; otherwise find them
   from the environment (the folder's existing clones and their remotes, `gh`). Flag
   chakrit only when you cannot settle one.
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
   git submodules. Add one row per repo to the `## Repos` table in `AGENTS.md` with only
   the Folder cell filled; the project control fills the rest.
6. **Clone.** Run `bin/clone-repos`. It clones missing repos and adds each folder to
   `.gitignore`.
7. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<machine>-<org>-<project>`.
8. **ACE.** Follow "Onboard into ACE" in `references/operations.md`.
9. **Register with the org control.** The project needs a row in the org control's
   `registries/projects.md` and a port block. If you are the org control, add the row,
   grant the block in your `registries/ports.md`, and commit in your repo. Otherwise ask
   the org control (see "Reach a parent" in `references/operations.md`). Write the
   block into `AGENTS.md` under "Ports". When this setup runs for "Initiate an agent",
   add only the registry row; initiation grants the block.
10. **Commit,** naming the skill revision.
11. **Start the agent.** When this setup runs for "Initiate an agent", skip this step;
    initiation starts and wakes the agent. If you are the org control, follow "Start an
    agent" in `rule/handling-agents`. Otherwise add to the completion report: "Start the
    project control: in a tmux window, `cd ~/Documents/<org>/<project>`, start a new
    session the way you start agents in this org, then
    `/rename <machine>:<org>:<project>`."

## Done when

The completion list in `SKILL.md` holds, every repo in `repos.txt` is cloned and
ignored, and the org control's projects registry lists the project.
