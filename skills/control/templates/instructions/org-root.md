# {{org}}

Org folder for `{{org}}` (GitHub org `{{github_org}}`) on `{{machine}}`. It is not a git
repo and holds no work of its own:

- `control/` is the org control, `{{machine}}:{{org}}:control`. Org coordination, task
  tracking and project registration happen there.
- Each project folder is a project control, `{{machine}}:{{org}}:<project>`, holding that
  project's component repos as plain clones.

The org control owns this file.

## Control

You are an agent started in the org folder, not a control. Do no project work here:
work belongs in the project folder that owns it, and org coordination belongs to the
org control. If chakrit asks for either, say which folder's agent should take it.

**At session start and after a clear or compaction,** load every entry the table marks
"start", then call `mem_context` for engram project `{{machine}}-{{org}}`, the org's
memory, which you share with the org control (without engram, read the file list of
`control/memory/`). Nothing loads these for you: skip this and you work with no rules
and no memory.

Rules live in engram project `{{machine}}-control-rules`. Load each entry in full:
`mem_search` its topic key with project `{{machine}}-control-rules`, take the result
whose `topic_key` equals the key exactly, then `mem_get_observation` that ID for the full
text, since search results are truncated. If no result has the exact key, stop and tell
the org control. Engram is available when the `mem_search` tool exists; the `engram`
binary alone is not enough. Without engram, read `~/Documents/control/rules/<topic>.md`.

| Entry             | Load when                                  |
| ----------------- | ------------------------------------------ |
| `rule/policy-org` | start (how this org is run; read only)     |
| `rule/memory`     | start; before a save, handoff or wind-down |

## Environment

How a folder in this org is onboarded into ACE. `none` means the org has no such step.

| Item       | Value          |
| ---------- | -------------- |
| School     | {{school}}     |
| Init skill | {{init_skill}} |
