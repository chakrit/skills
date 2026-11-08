# Registries

A registry is a Markdown file a control keeps to track something shared: who exists,
which ports are taken, who holds a heavy-job slot. Agents read it; scripts do not. A control creates a registry when it has something shared to track; the
templates in `templates/registries/` are starting points, not a required set.

## Rules

1. Keep registries under `registries/` in the owning control repo.
2. Hold coordination facts only. Knowledge goes where `templates/rules/memory.md`
   says.
3. Update the registry in the same commit as the change it records. Never copy
   registry contents into the control page.
4. A child asks its parent to change the parent's registry. It never edits it directly.

## Examples

| Registry        | Owner           | Tracks                                                       |
| --------------- | --------------- | ------------------------------------------------------------ |
| `orgs.md`       | machine control | org slug and initiation status; GitHub orgs                  |
| `ports.md`      | machine control | port blocks granted to org controls                          |
| `heavy-jobs.md` | machine control | heavy-job slots and the project holding each                 |
| `projects.md`   | org control     | project slug and initiation status                           |
| `ports.md`      | org control     | port blocks granted to projects, single service reservations |

Registries record who exists, not live state, and no script reads them. Status says
whether the parent has accepted the agent's initiation report (`initiating`,
`initiated`). `scripts/control-agents` finds a running agent's pane by its `@agent`
tmux tag, which the control sets at start and the agent sets again at every session
start.

## Nested resources

- **Ports nest the way the levels do.** The user's open range is 8000–9000. Machine
  control grants each org control a block; the org control grants each project a
  smaller block from it and reserves single service ports inside that. Example sizes:
  100 ports per org, 20 per project.
- **Heavy-job slots stay with machine control.** Only machine control keeps a
  `heavy-jobs.md`; it records the holder as `<org>:<project>`. An org control relays a
  project's request to machine control, passes the grant on, and relays the done
  report. No org control keeps a copy.

A project asks its org control. An org control asks machine control. Nobody skips a
level; see "Reach a parent" in `references/operations.md`.
