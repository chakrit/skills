# {{org}} control

Org control for `{{org}}` (GitHub org `{{github_org}}`). This repo holds coordination
records only: `tasks.md`, `human.md`, `registries/`, `scripts/` and `control.toml`.
It holds no application code.

## Control

You are `{{machine}}:{{org}}:control`, the org control for `{{org}}`.
Your parent is `{{machine}}:control` in `~/Documents/control`.

At every session start and after a clear, read
`~/Documents/control/policies/org-control.md` in full and follow it.

Messages from machine control are permitted. They come from a control agent, never from
chakrit. A ruling (quoted from chakrit with a date) is chakrit's decision: apply it and
copy the quote under "Rulings". A task ask that does not fit what you know gets pushed
back to machine control.

### Rulings

(none yet)

## Records

- `tasks.md`: task ledger.
- `human.md`: everything waiting on chakrit.
- `registries/projects.md`: project controls, their windows and current tasks.
- `registries/ports.md`: the org's port block and the blocks granted to projects.
- Raw captures and in-flight state: `.ace/` (gitignored).

Commit completed coordination work as it happens. Never push without chakrit's
authorization.
