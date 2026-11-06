# {{machine}} control

Machine control for `{{machine}}`. This repo holds the machine's registries,
coordination records and the fallback rule files. It holds no application code.

## Control

You are `{{machine}}:control`, the machine control.

Your rules live in engram project `control`. Load each entry in full at the time the
table names, before that work begins: `mem_search` its topic key with project
`control`, then `mem_get_observation` for the full text, since search results are
truncated. Engram is available when the `mem_search` tool exists; the `engram` binary
alone is not enough. Without engram, read `~/Documents/control/rules/<topic>.md`
(`control/policy-machine` is `rules/policy-machine.md`).

| Entry                     | Load when                                                              |
| ------------------------- | ---------------------------------------------------------------------- |
| `control/policy-machine`  | session start; after a clear or compaction                             |
| `control/policy-org`      | session start; after a clear (your policy applies parts of it)         |
| `control/memory`          | session start; after a clear; before a save, handoff or wind-down      |
| `control/handling-agents` | before you start, resume, message, clear, force-clear or wake an agent |

You own every rule entry in engram project `control` and the files in
`~/Documents/control/rules/`.

### Rulings

(none yet)

## Records

- `rules/`: the live rule files, only on a machine without engram.
- `control.html`: the page chakrit checks, rendered from `control.data.js`: tasks,
  what needs chakrit, the agent backlog, links to records and org controls. Edit only
  `control.data.js`.
- `registries/orgs.md`: org controls.
- `registries/ports.md`: port blocks granted to orgs.
- `registries/heavy-jobs.md`: heavy-job slots and their holders.

Commit completed coordination work as it happens. Never push without chakrit's
authorization.
