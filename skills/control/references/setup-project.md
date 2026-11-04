# Set up a project control

Creates `~/Documents/<org>/<project>`, a local project repo that holds the project's
component repos as plain clones, and its agent `<machine>:<org>:<project>`. The project
control owns the project's context and may do hands-on work in its clones.

## Steps

1. **Check.** The org control must exist at `~/Documents/<org>/control`; if not, run
   `references/setup-org.md` first. If the project folder exists and already has
   `AGENTS.md`, stop and use `references/initiation.md` instead.
2. **Confirm the names.** `<project>` is chakrit's short name for the project. Ask him
   for it and for the list of component repos, unless he already gave both.
3. **Create the repo.**

   ```sh
   mkdir -p ~/Documents/<org>/<project>
   cd ~/Documents/<org>/<project>
   git init
   ```

   The project repo stays local. Never add a remote unless chakrit asks.
4. **Copy templates,** replacing placeholders (`{{machine}}`, `{{org}}`,
   `{{project}}`, `{{date}}`):

   | Source                                      | Destination        |
   | ------------------------------------------- | ------------------ |
   | `templates/instructions/project-control.md` | `AGENTS.md`        |
   | `templates/gitignore`                       | `.gitignore`       |
   | `templates/project/repos.txt`               | `repos.txt`        |
   | `templates/project/clone-repos`             | `bin/clone-repos`  |

   Then `ln -s AGENTS.md CLAUDE.md` and `chmod +x bin/clone-repos`.
5. **List the clones.** Write one line per component repo in `repos.txt`:
   `<repo-name> <clone-url>`. The folder name is the exact GitHub repo name. Never use
   git submodules.
6. **Clone.** Run `bin/clone-repos`. It clones missing repos with remote `gh` and adds
   each folder to `.gitignore`.
7. **Set up ACE.** Run `ace setup` with the org's school. Ask chakrit if unsure.
8. **Memory.** Follow "Set up a level's engram project" in `references/memory.md`
   with project name `<org>-<project>`.
9. **Register with the org control.** Message it (wake it up first if needed) asking it
   to add the project to its `registries/projects.md` and to allocate a port block.
   Write the granted block into `AGENTS.md` under "Ports".
10. **Commit,** naming the skill revision.
11. **Start the agent** ("Start an agent" in `references/operations.md`) and rename its
    session to `<machine>:<org>:<project>`.

## Done when

The completion list in `SKILL.md` holds, every repo in `repos.txt` is cloned and
ignored, and the org control's projects registry lists the project.
