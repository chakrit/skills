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

- `policies/`: one governance policy per level, and `memory.md` for every level.
- `tasks.md`: task ledger.
- `human.html`: chakrit's view of this machine: what needs chakrit, open tasks, links
  to org controls, registries.
- `registries/orgs.md`: org controls.
- `registries/ports.md`: port blocks granted to orgs.
- `registries/heavy-jobs.md`: heavy-job slots and their holders.

Commit completed coordination work as it happens. Never push without chakrit's
authorization.
