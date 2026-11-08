# Control operations

Shared procedures the setup references call. The procedures controls run on agents
every day (start, message, clear, wind down, wake, give a task, initiate) live in
`templates/rules/handling-agents.md`, which machine setup seeds as engram entry
`rule/handling-agents`.

## Install scripts

Copy this skill's `scripts/` into the control repo as `scripts/`. Project controls
skip this; they reach their parent through messages. To refresh later, copy the
skill's `scripts/` again and review the diff before committing.

The script runs through `uv`. Check `command -v uv`. If it prints nothing, do not
install it; add this line to the completion report: `uv missing: install uv before
using scripts/control-agents`.

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

The new machine or org control runs this itself, after its setup or initiation. It
finds the folders one level down that should get their own control, so the structure
is complete rather than set up one folder at a time. Machine setup lodges it as an
Agent Backlog row in machine control's `control.data.js`, and the user asks machine
control to run it; machine control sends it to an org control as a task after
initiating it.

1. **Scan** the new control's level:
   - **Machine control:** every folder `~/Documents/<name>/` except `control` that
     holds git repos (`find ~/Documents/<name> -maxdepth 3 -name .git`). Its org
     control is `~/Documents/<name>/control`.
   - **Org control:** every folder `~/Documents/<org>/<name>/` except `control` that is
     a git repo or holds git repos. Each one is a project.
   - Classify each by your own registry (`registries/orgs.md` or
     `registries/projects.md`), never by the folder's files: a row with Status
     `initiated` needs nothing; anything else is a candidate for "Initiate an agent",
     which runs the setup first when the folder needs it.
   - Suggest the folder name as `<org>` or `<project>`. For an org, suggest the GitHub
     org from its repos' remotes; flag the user only when you cannot find it. For a
     folder holding several repos, suggest their remotes as `repos.txt` lines.
   - Skip folders without git repos and list them as skipped.
2. **Check authorization.** If the user already asked for downstream setup ("set up
   all the orgs", "do the projects too"), quote those words and continue. Otherwise
   send the user the candidate list with the suggested names, and ask which to set up.
   Wait for the user's answer. Never move or rename a folder the user has not named.
3. **Lodge.** Add one Agent Backlog entry per approved candidate in the new control's
   `control.data.js`, with the user's quoted words as the source. Commit.
4. **Do.** Run "Initiate an agent" for each approved candidate, one at a time.
   An org control set up or initiated this way gets this section as its task. Mark each
   backlog entry done with its commit hash.

## Reach a parent

Nothing runs upward: `scripts/control-agents` only types into agents below. An agent
that needs its parent (for a port, a heavy-job slot, a ruling) uses the harness's own
agent messaging when it reaches the parent. Otherwise it asks the user to start the
parent and relay the message, for example: "We need a port for the XYZ server and the
org control is not running; can you start it and pass this on?" A child never starts
its parent or runs the parent's scripts.

## Onboard into ACE

Run this in every control a setup creates. ACE is preferred where it exists and never
required. An environment may use its own CLI and init skill in place of `ace` and
`ace-init`, so never assume the plain ACE names: use the school and init skill your own
environment uses, from your instruction file, your school or the user's words. Ask the
user when either is unclear.

1. If your environment has no school, skip this section; the setup is complete without
   ACE.
2. In the folder, set up the school in a visible tmux pane with the command your
   environment uses for it; prefer ACE's own where `ace` is installed. It may ask for
   authentication; tell the user which pane waits for input.
3. For machine control, run the init skill in its folder to finish onboarding and
   commit the files it writes. An org or project control runs its own init skill when
   it is initiated, since the init skill writes the agent's instructions; the
   initiation message names it.
