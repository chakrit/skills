# Orgs

Org controls on this machine. Updated by machine control only. Org is the user's short
org slug; its control lives in `~/Documents/<org>/control`. Status is `initiating` from
the row's first write during "Initiate an agent", and `initiated` once you accept the
agent's report that everything is done. `scripts/control-agents` does not read this
file; it finds each agent's pane by its `@agent` tmux tag.

| Org | Status |
| --- | ------ |

## GitHub orgs

One line per org: `- <org slug> → <GitHub org>`.
