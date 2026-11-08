# Set up a project control

Puts the project folder `~/Documents/<org>/<project>` in place for its agent
`<machine>:<org>:<project>`. Setup only creates the folder and copies templates; the
agent takes over its own files when it is initiated. A single-repo project's folder is
that repo. A project with several repos gets a local wrapper repo that holds them as
plain clones.

## Steps

1. **Check.** The org control must exist at `~/Documents/<org>/control`; if not, run
   `references/setup-org.md` first. Never replace or edit an existing file in the
   project folder.
2. **Work out the names.** `<project>` is the user's short name for the project.
   The user's request usually holds it and the project's repos; otherwise find them
   from the environment (the folder's repos and their remotes, `gh`). Flag the user
   only when you cannot settle one.
3. **Get the folder.** If it exists, use it, and run `git init` in it when it is not a
   git repo. Otherwise, for a single-repo project, clone the repo to
   `~/Documents/<org>/<project>`. For a project with several repos, create the wrapper:

   ```sh
   mkdir -p ~/Documents/<org>/<project>
   cd ~/Documents/<org>/<project>
   git init
   ```

   The wrapper repo stays local. Never add a remote unless the user asks.
4. **ACE.** Follow "Onboard into ACE" in `references/operations.md`.
5. **Copy templates as they are.** Fill in nothing: the agent replaces the template
   values when it is initiated.

   | Source                                      | Destination       | When                                               |
   | ------------------------------------------- | ----------------- | -------------------------------------------------- |
   | `templates/instructions/project-control.md` | `AGENTS.md`       | the folder has neither `AGENTS.md` nor `CLAUDE.md` |
   | `templates/gitignore`                       | `.gitignore`      | several repos, when missing                        |
   | `templates/project/repos.txt`               | `repos.txt`       | several repos, when missing                        |
   | `templates/project/clone-repos`             | `bin/clone-repos` | several repos, when missing                        |

   When you copied `AGENTS.md`, run `ln -s AGENTS.md CLAUDE.md`. For a wrapper, run
   `chmod +x bin/clone-repos`.
6. **Initiate.** If you came here from "Initiate an agent", return there. If you are
   the org control, follow "Initiate an agent" in `rule/handling-agents`. Otherwise add
   to the completion report: "Ask `<machine>:<org>:control` to initiate
   `<machine>:<org>:<project>` in `~/Documents/<org>/<project>`."

## Done when

The completion list in `SKILL.md` holds.
