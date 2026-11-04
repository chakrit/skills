# Task ledger

One entry per task: every task chakrit asks, everything this control infers, and every
agent report. Newest first. Move finished entries older than a week to
`tasks-archive.md` so this file stays short.

`scripts/` reads task IDs from the headings: keep the `## <task-id> — <agent>` form,
with a lowercase hyphenated ID and an em dash.

Entry format:

```text
## <task-id> — <agent name>
Status: open | dispatched | done | blocked | dropped
Opened: <date>
Provenance: chakrit: "<verbatim words>" | inferred by <agent> | reported by <agent>
Evidence: <commit, PR, pane capture path, checkpoint path>
Next: <next action>
```
