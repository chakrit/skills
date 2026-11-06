# Projects

Project controls in this org. Updated by the org control only. `scripts/` parses the
table: keep its four columns. Project is a lowercase slug; Checkout is relative to
`~/Documents/<org>`; Window and Agent pane are the last-known tmux IDs (`@12`, `%34`),
empty when none is recorded. chakrit starts and moves agents too, so they can be stale:
use them as they are, and only when `scripts/control-agents` refuses the pane or the
cells are empty, find the agent's pane in tmux and correct the row.

| Project | Checkout | Window | Agent pane |
| ------- | -------- | ------ | ---------- |
