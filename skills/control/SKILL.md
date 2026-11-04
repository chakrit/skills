---
name: control
description: >-
  Set up chakrit's three-level control-agent structure on one machine: a machine
  control, org controls and project controls that coordinate coding agents in tmux,
  with central policies, registries and engram memory. TRIGGER on "/control", "set up
  control", "set up machine control", "set up an org control", "bootstrap this
  project for agents", "add this project to control", "initiate this agent", or when
  creating a folder under ~/Documents/<org>/ that agents will manage. DO NOT TRIGGER
  for day-to-day control work after setup (agents follow their local instructions and
  policies), for single-repo ACE onboarding (ace-init), or for editing an existing
  control's policies.
---

# control

Sets up control agents. After setup, every agent works from its own instruction file
and the policy file it points to; no agent needs this skill again for daily work.

## Concepts

Use these names exactly, in every file and message.

| Term            | Meaning                                                                                |
| --------------- | -------------------------------------------------------------------------------------- |
| Machine control | `~/Documents/control`, agent `<machine>:control`. Machine-wide tasks only.             |
| Org control     | `~/Documents/<org>/control`, agent `<machine>:<org>:control`. One org's tasks.         |
| Project control | `~/Documents/<org>/<project>`, agent `<machine>:<org>:<project>`. One project's work.  |
| Level           | One of the three above. There are exactly three. Never define a fourth.                |
| Parent          | Project control → its org control → machine control.                                   |
| `<machine>`     | Lowercase short hostname: `hostname -s`, lowercased (`lz49`).                          |
| `<org>`         | chakrit's short org name (`datawow`, not `datawowio`).                                 |
| Policy          | Governance rules for one level, in `~/Documents/control/policies/<level>.md`.          |
| Registry        | A file a control keeps to track shared things (ports, heavy-job slots, members).       |
| Ruling          | chakrit's decision on authority or policy, relayed by a control.                       |
| Task ask        | Work chakrit asked a control to hand to an agent.                                      |
| Waiting page    | `human.md` in a control repo: everything waiting on chakrit.                           |
| Task ledger     | `tasks.md` in a control repo: every task, its status, provenance and evidence.         |
| Wake-up         | Starting a stopped agent so it can receive a message.                                  |

## Menu

| Operation                 | Read                              | Use when                                          |
| ------------------------- | --------------------------------- | ------------------------------------------------- |
| Set up machine control    | `references/setup-machine.md`     | `~/Documents/control` does not exist yet          |
| Set up an org control     | `references/setup-org.md`         | `~/Documents/<org>/control` does not exist yet    |
| Set up a project control  | `references/setup-project.md`     | a project folder needs an agent and its clones    |
| Initiate an agent         | `references/initiation.md`        | an existing agent lacks the standing grant        |

Read only the file for the chosen operation. It names the sections of the shared
files it needs: `references/operations.md`, `references/registries.md` and
`references/memory.md`.

Set up levels top-down. Before an org control, machine control must exist. Before a
project control, its org control must exist. If a parent is missing, set it up first
and tell chakrit you did.

## Rules for every operation

1. Run on one machine only. Never write cross-machine sync steps.
2. Never install software or change global configuration (Homebrew, `~/.claude*`,
   shell profiles, MCP registrations). Write the steps for chakrit instead.
3. Copy templates, then replace every `{{placeholder}}`. A file with a leftover
   `{{` is not done.
4. Keep policy and instruction files short. Agents skip long instructions.
5. Commit each finished setup in the new repo with the `gh` remote convention; never
   push.

## Completion

A setup is done when:

- every file the setup reference lists exists, with no `{{` left (`grep -rn '{{' .`
  prints nothing);
- the agent's instruction file contains the standing grant and the policy pointer;
- the parent's registry lists the new control (org and project controls);
- the work is committed in the new repo.

Report the folder, the agent name, the commit hash and any steps left for chakrit.
