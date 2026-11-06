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
is complete rather than set up one folder at a time. Setup lodges it as an Agent
Backlog row in the new control's `control.data.js`; a parent that set up or initiated
an org control sends it as a task after the wake, and chakrit asks machine control.

1. **Scan** the new control's level:
   - **Machine control:** every folder `~/Documents/<name>/` except `control`.
     Classify each one:

     | Folder holds                                          | Candidate for                   |
     | ----------------------------------------------------- | ------------------------------- |
     | `control/AGENTS.md` with a `## Control` section       | nothing; register it if missing |
     | `control/AGENTS.md` or `control/CLAUDE.md` without it | `references/initiation.md`      |
     | git repos and no `control/`                           | `references/setup-org.md`       |

     Find git repos with `find ~/Documents/<name> -maxdepth 3 -name .git`. For an org
     candidate, suggest the folder name as `<org>` and the GitHub org from
     its repos' remotes.
   - **Org control:** every folder `~/Documents/<org>/<name>/` except `control`.
     Classify each one:

     | Folder holds                                    | Candidate for                     |
     | ----------------------------------------------- | --------------------------------- |
     | `AGENTS.md` with a `## Control` section         | nothing; register it if missing   |
     | `AGENTS.md` or `CLAUDE.md` without that section | `references/initiation.md`        |
     | several git clones and no `AGENTS.md`           | `references/setup-project.md`     |
     | one git repo at its top level                   | ask chakrit which project owns it |

     For a project candidate, suggest the folder name as `<project>` and its clones'
     remotes as `repos.txt` lines.
   - Skip folders without git repos and list them as skipped.
   - List every other folder that matches no row as unclassified, with what it holds,
     and ask chakrit about it in step 2.
2. **Check authorization.** If chakrit already asked for downstream setup ("set up
   all the orgs", "do the projects too"), quote those words and continue. Otherwise
   send chakrit the candidate list with the suggested names, and ask which to set up.
   Wait for chakrit's answer. Never move or rename a folder chakrit has not named.
3. **Lodge.** Add one Agent Backlog entry per approved candidate in the new control's
   `control.data.js`, with chakrit's quoted words as the source. Commit.
4. **Do.** Run the setup or initiation for each approved candidate, one at a time.
   An org control set up or initiated this way gets this section as its task. Mark each
   backlog entry done with its commit hash.

## Reach a parent

Messages run downward through `scripts/control-agents`; nothing runs upward. An agent
that needs its parent (for a port, a heavy-job slot, a ruling) uses the harness's own
agent messaging when it reaches the parent. Otherwise it asks chakrit to start the
parent and relay the message, for example: "We need a port for the XYZ server and the
org control is not running; can you start it and pass this on?" A child never starts
its parent or runs the parent's scripts.

## Record the environment

ACE is preferred where it exists and never required. An environment may wrap it: an
org's school can ship its own launcher and init skill in place of `ace` and `ace-init`.
Never assume the plain ACE names. Run this once for machine control and once per org;
its values fill the Environment placeholders of `machine-control.md` or `org-root.md`.

1. Find the values in the org's school, the instruction files already in the org's
   folders, or chakrit's words. Ask chakrit when any value is unclear.

   | Placeholder          | Value                                                       |
   | -------------------- | ----------------------------------------------------------- |
   | `{{school}}`         | the ACE school, or `none` without ACE                       |
   | `{{resume_command}}` | what to type to resume the folder's last session            |
   | `{{new_command}}`    | what to type to start a new session                         |
   | `{{start_skill}}`    | the skill that loads a session's context, or `none`         |
   | `{{init_skill}}`     | the skill that onboards a folder, or `none`                 |
   | `{{save_skill}}`     | the skill that saves a session before a clear, or `none`    |

2. Without ACE, use the plain harness: for Claude Code, `claude --continue` and
   `claude`; for Codex, `codex resume --last` and `codex`.

## Onboard into ACE

Run this for every folder a setup gives an instruction file: machine control, the org
root, the org control and each project control. Use the Environment table that governs
the folder: machine control's own, or the org root's for every folder in the org.

1. If the school is `none`, skip this section; the setup is complete without ACE.
2. In the folder, set up the school in a visible tmux pane with the environment's
   school-setup command (`ace setup <school>` for plain ACE; for a wrapped environment,
   find it as "Record the environment" finds its values, and ask chakrit when unclear),
   since it may ask for authentication; tell chakrit which pane waits for input.
3. If the init skill is `none`, skip this step. In the same pane, start a session with
   the New session command from the Environment table and ask it to run the init
   skill, so the skill onboards that folder. When it finishes, quit that session. Commit the files it writes where the folder is a repo;
   the org root is not one.
