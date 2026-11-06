---
name: control
description: >-
  Set up the user's three-level control-agent structure on one machine: a machine
  control, org controls and project controls that coordinate coding agents in tmux,
  with rules and memory in engram, and registries. TRIGGER on "/control", "set up
  control", "set up machine control", "set up an org control", "bootstrap this
  project for agents", "add this project to control", "initiate an agent", or when
  creating a folder under ~/Documents/<org>/ that agents will manage. DO NOT TRIGGER
  for day-to-day control work after setup (agents follow their local instructions and
  policies), for single-repo ACE onboarding (ace-init), or for editing an existing
  control's policies.
---

# control

Sets up control agents. After setup, every agent works from its own instruction file
and the rule entries it points to; no agent needs this skill again for daily work.

## Concepts

Use these names exactly, in every file and message.

| Term            | Meaning                                                                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Machine control | `~/Documents/control`, agent `<machine>:control`. Tasks no single org owns.                                                                   |
| Org control     | `~/Documents/<org>/control`, agent `<machine>:<org>:control`. One org's tasks.                                                                |
| Org root        | `~/Documents/<org>/`. Not a level or a repo; its instruction file, owned by the org control, maps the folder and loads the org's memory.      |
| Project control | `~/Documents/<org>/<project>`, agent `<machine>:<org>:<project>`. One project's work.                                                         |
| Level           | One of the three above. There are exactly three. Never define a fourth.                                                                       |
| Parent          | Project control → its org control → machine control.                                                                                          |
| `<machine>`     | Lowercase short hostname: `hostname -s`, lowercased (`lz49`).                                                                                 |
| `<org>`         | The user's short org name (`datawow`, not `datawowio`).                                                                                       |
| Policy          | Governance rules for one level: engram entry `rule/policy-<level>`.                                                                           |
| Rule entry      | A rule set in engram project `<machine>-control-rules`, seeded from `templates/rules/`; files in `~/Documents/control/rules/` without engram. |
| Environment     | Table in machine control's and each org root's instruction file: the school and init skill that onboard folders there.                        |
| Registry        | A file a control keeps to track shared things (ports, heavy-job slots, members).                                                              |
| Ruling          | The user's decision on authority or policy, relayed by a control.                                                                             |
| Task ask        | Work the user asked a control to hand to an agent.                                                                                            |
| Standing grant  | The `## Control` section of an agent's instruction file: who it is, its parent, which messages it accepts and the rule entries it loads.      |
| Wind-down       | Save, clear, exit the harness and its shell. The user's "stop" for an agent means this.                                                       |
| Control page    | `control.html` in a control repo, rendered from `control.data.js`; see `rule/policy-org`.                                                     |
| Wake-up         | Readying an agent before any task. Controls wake below; the user wakes a parent.                                                              |
| Task-give       | Sending a woken agent a task ask, after checking it fits the agent's reported state.                                                          |

## Menu

| Operation                | Read                          | Use when                                       |
| ------------------------ | ----------------------------- | ---------------------------------------------- |
| Set up machine control   | `references/setup-machine.md` | `~/Documents/control` does not exist yet       |
| Set up an org control    | `references/setup-org.md`     | `~/Documents/<org>/control` does not exist yet |
| Set up a project control | `references/setup-project.md` | a project folder needs an agent and its clones |
| Initiate an agent        | `references/initiation.md`    | an existing agent lacks setup or the grant     |

Read only the file for the chosen operation. It names the sections of the shared
files it needs: `references/operations.md`, `references/registries.md`,
`references/memory.md` and `templates/rules/handling-agents.md`.

Set up levels top-down. Before an org control, machine control must exist. Before a
project control, its org control must exist. If a parent is missing, set it up first
and tell the user you did.

## Rules for every operation

1. Run on one machine only. Never write cross-machine sync steps.
2. Never install software or change global configuration (Homebrew, `~/.claude*`,
   shell profiles, MCP registrations). Write the steps for the user instead.
3. Copy templates, then replace every `{{placeholder}}`. A file with a leftover
   `{{` is not done.
4. Keep policy and instruction files short. Agents skip long instructions.
5. Commit each finished setup in the new repo; never push.

## Completion

A setup is done when:

- every file the setup reference lists exists, with no `{{` left: in the new repo,
  `git grep --untracked -n '{{'` prints nothing (it skips the ignored clones), and for
  an org, `grep -n '{{' ~/Documents/<org>/AGENTS.md` prints nothing;
- the agent's instruction file contains the standing grant and the rule-entry pointers;
  when the setup runs for "Initiate an agent", the agent adds them itself and the
  initiation's acknowledgment meets this item;
- for an org, the org root has its instruction file with `CLAUDE.md` linked to it;
- every folder given an instruction file is onboarded as its Environment table says
  ("Onboard into ACE" in `references/operations.md`), or its school is `none`;
- the parent's registry lists the new control (org and project controls);
- for a machine or org control, its `control.data.js` has an Agent Backlog row "Plan
  downstream controls" for the new control, except when the setup runs for "Initiate
  an agent", which sends the planning as a task;
- the work is committed in the new repo.

Report the folder, the agent name, the commit hash and any steps left for the user.
