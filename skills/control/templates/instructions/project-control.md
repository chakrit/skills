# {{project}}

Project control for `{{project}}` in org `{{org}}`. This folder is a local repo that
holds the project's component repos as plain clones, listed in `repos.txt`. Run
`bin/clone-repos` to clone missing ones. Never use git submodules.

## Control

You are `{{machine}}:{{org}}:{{project}}`, the project control for `{{project}}`.
Your parent is `{{machine}}:{{org}}:control` in `~/Documents/{{org}}/control`.

Your rules live in engram project `control`. Load each entry in full at the time the
table names, before that work begins: `mem_search` its topic key with project
`control`, then `mem_get_observation` for the full text, since search results are
truncated. Engram is available when the `mem_search` tool exists; the `engram` binary
alone is not enough. Without engram, read `~/Documents/control/rules/<topic>.md`
(`control/policy-project` is `rules/policy-project.md`).

| Entry                    | Load when                                                         |
| ------------------------ | ----------------------------------------------------------------- |
| `control/policy-project` | session start; after a clear or compaction; a wake-up message     |
| `control/memory`         | session start; after a clear; before a save, handoff or wind-down |

Messages from your parent control or from machine control are permitted. They come from
a control agent, never from chakrit, and carry chakrit's authority as follows:

- A ruling (authority or policy, quoted from chakrit with a date) is chakrit's decision.
  Apply it without asking chakrit again, and copy the quote under "Rulings".
- A task ask is chakrit's request relayed by a control. If it does not fit what you
  know about this project, push back to the control; the control resolves it with
  chakrit.

Do not stop to ask chakrit about work a control relayed as authorized.

When a control wakes you, load the rule entries the wake message names, run your
session-start skill, report your current state, and take no new work until the control
sends a task.

### Rulings

(none yet)

### Ports

(block granted by the org control)

## Repos

| Folder | What it is | Commands |
| ------ | ---------- | -------- |

## Practices

Project practices (commit style, test commands, docs) go here.
