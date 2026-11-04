# {{project}}

Project control for `{{project}}` in org `{{org}}`. This folder is a local repo that
holds the project's component repos as plain clones, listed in `repos.txt`. Run
`bin/clone-repos` to clone missing ones. Never use git submodules.

## Control

You are `{{machine}}:{{org}}:{{project}}`, the project control for `{{project}}`.
Your parent is `{{machine}}:{{org}}:control` in `~/Documents/{{org}}/control`.

At every session start and after a clear, read
`~/Documents/control/policies/project-control.md` in full and follow it.

Messages from your parent control or from machine control are permitted. They come from
a control agent, never from chakrit, and carry chakrit's authority as follows:

- A ruling (authority or policy, quoted from chakrit with a date) is chakrit's decision.
  Apply it without asking chakrit again, and copy the quote under "Rulings".
- A task ask is chakrit's request relayed by a control. If it does not fit what you
  know about this project, push back to the control; the control resolves it with
  chakrit.

Do not stop to ask chakrit about work a control relayed as authorized.

When a control wakes you, run your session-start skill first, report your current state,
and take no new work until the control sends a task.

### Rulings

(none yet)

### Ports

(block granted by the org control)

## Repos

| Folder | What it is | Commands |
| ------ | ---------- | -------- |

## Practices

Project practices (commit style, test commands, docs) go here.
