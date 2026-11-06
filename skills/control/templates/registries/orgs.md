# Orgs

Org controls on this machine. Updated by machine control only. `scripts/` parses the
table: keep its four columns. Org is the user's short org slug; Checkout is relative to
`~/Documents`, e.g. `datawow/control`; Window and Agent pane are the last-known tmux IDs
(`@12`, `%34`), empty when none is recorded. The user starts and moves agents too, so
they can be stale: use them as they are, and only when `scripts/control-agents` refuses
the pane or the cells are empty, find the agent's pane in tmux and correct the row.

| Org | Checkout | Window | Agent pane |
| --- | -------- | ------ | ---------- |

## GitHub orgs

One line per org: `- <org slug> → <GitHub org>`.
