# Control operations

Shared procedures the setup references call. The procedures controls run on agents
every day (start, message, clear, wind down, wake, give a task, initiate) live in
`templates/rules/handling-agents.md`, which machine setup seeds as engram entry
`rule/handling-agents`.

## Install scripts

Copy this skill's `scripts/` into the control repo as `scripts/`. Project controls
skip this; they reach their parent through messages. To refresh later, copy the
skill's `scripts/` again and review the diff before committing.

## Point the control page at PragmataPro

`control.html` loads PragmataPro from its font files with `file://` URLs, because
Safari does not let a page use a user-installed font by name. The template's four
`@font-face` URLs name the files of one install; check them on this machine after
copying the page. Never copy font files into the control repo or the skill.

1. List the installed files: `ls ~/Library/Fonts /Library/Fonts`, and look for names
   starting with `PragmataPro`.
2. If they are installed, set each `@font-face` URL in `control.html` to the matching
   file's absolute `file://` path: regular and bold of PragmataPro, regular and bold
   of PragmataPro Mono. File names carry a version (`PragmataProR_09.ttf`), so match
   the installed version.
3. If PragmataPro is not installed, delete the four `@font-face` rules; the page falls
   back to Iosevka Charon.

## Plan downstream controls

Run after a machine control or an org control is set up or initiated. It finds the
folders one level down that should get their own control, so the structure is complete
rather than set up one folder at a time.

1. **Scan** the new control's level:
   - **Machine control:** every folder `~/Documents/<name>/` except `control`. A
     folder is an org candidate when it has no `control/` subfolder and holds git
     repos (`find ~/Documents/<name> -maxdepth 3 -name .git`). Suggest the folder
     name as `<org>` and the GitHub org from its repos' `gh` remotes.
   - **Org control:** every folder `~/Documents/<org>/<name>/` except `control`.
     Classify each one:

     | Folder holds                                    | Candidate for                     |
     | ----------------------------------------------- | --------------------------------- |
     | `AGENTS.md` with a `## Control` section         | nothing; register it if missing   |
     | `AGENTS.md` or `CLAUDE.md` without that section | `references/initiation.md`        |
     | several git clones and no `AGENTS.md`           | `references/setup-project.md`     |
     | one git repo at its top level                   | ask chakrit which project owns it |

     For a project candidate, suggest the folder name as `<project>` and its clones'
     `gh` remotes as `repos.txt` lines.
   - Skip folders without git repos and list them as skipped.
2. **Check authorization.** If chakrit already asked for downstream setup ("set up
   all the orgs", "do the projects too"), quote those words and continue. Otherwise
   send chakrit the candidate list with the suggested names, and ask which to set up.
   Wait for chakrit's answer. Never move or rename a folder chakrit has not named.
3. **Lodge.** Add one Agent Backlog entry per approved candidate in the new control's
   `control.data.js`, with chakrit's quoted words as the source. Commit.
4. **Do.** Run the setup or initiation for each approved candidate, one at a time.
   Each org control set up this way runs this section again for its own projects.
   Mark each backlog entry done with its commit hash.

## Reach a parent

Messages run downward through `scripts/control-agents`; nothing runs upward. An agent
that needs its parent (for a port, a heavy-job slot, a ruling) uses the harness's own
agent messaging when it reaches the parent. Otherwise it asks chakrit to start the
parent and relay the message, for example: "We need a port for the XYZ server and the
org control is not running; can you start it and pass this on?" A child never starts
its parent or runs the parent's scripts.

Machine control that needs a project pane while the org control is down manages that
pane directly; it starts the org control first only when that is faster or the work
needs org context.

## Onboard into ACE

ACE is optional. Run this for every folder a setup gives an instruction file: machine
control, the org root, the org control and each project control.

1. Check whether ACE is installed: `command -v ace`. If it prints nothing, skip this
   section; the setup is complete without it.
2. Find the school. For an org's folders it is the org's school; ask chakrit for it
   with the org names unless chakrit already said it. For machine control, use the
   school chakrit names; if none is known, ask chakrit.
3. In the folder, run `ace setup <school>` in a visible tmux pane, since it may ask for
   authentication; tell chakrit which pane waits for input.
4. Run the `ace-init` skill in that folder to finish onboarding. Commit the files it
   writes where the folder is a repo; the org root is not one.
