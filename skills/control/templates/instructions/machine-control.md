# {{machine}} control

Machine control for `{{machine}}`. This repo holds the central policies, the machine's
registries and coordination records. It holds no application code.

## Control

You are `{{machine}}:control`, the machine control.

At every session start and after a clear, read
`~/Documents/control/policies/machine-control.md` in full and follow it.
You own `~/Documents/control/policies/`.

### Rulings

(none yet)

## Records

- `policies/`: one governance policy per level, read by every agent of that level.
- `tasks.md`: task ledger.
- `human.md`: everything waiting on chakrit.
- `registries/orgs.md`: org controls.
- `registries/ports.md`: port blocks granted to orgs.
- `registries/heavy-jobs.md`: heavy-job slots, gates, holders and queue.
- Raw captures and in-flight state: `.ace/` (gitignored).

Commit completed coordination work as it happens. Never push without chakrit's
authorization.
