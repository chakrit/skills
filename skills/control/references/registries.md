# Registries

A registry is a Markdown file a control keeps to track something shared: who exists,
which ports are taken, who holds a heavy-job slot. Other agents and the control scripts
read it. A control creates a registry when it has something shared to track; the
templates in `templates/registries/` are starting points, not a required set.

## Rules

1. Keep registries under `registries/` in the owning control repo.
2. Hold coordination facts only. Knowledge goes where `templates/rules/memory.md`
   says.
3. Update the registry in the same commit as the change it records. Never copy
   registry contents into the control page.
4. A child asks its parent to change the parent's registry. It never edits it directly.
5. If a script parses a registry, keep the columns its template states.

## Examples

| Registry        | Owner           | Tracks                                                       |
| --------------- | --------------- | ------------------------------------------------------------ |
| `orgs.md`       | machine control | org slug, checkout, window, pane, backend, task; GitHub orgs |
| `ports.md`      | machine control | port blocks granted to org controls                          |
| `heavy-jobs.md` | machine control | heavy-job slots and the project holding each                 |
| `projects.md`   | org control     | project slug, checkout, window, pane, backend, task          |
| `ports.md`      | org control     | port blocks granted to projects, single service reservations |

`orgs.md` and `projects.md` are parsed by `scripts/`; their templates state the
columns to keep. An agent that is not running keeps its row with Window and Agent pane
empty; the script lists it and refuses to type into it.

## Nested resources

- **Ports nest the way the levels do.** chakrit's open range is 8000–9000. Machine
  control grants each org control a block; the org control grants each project a
  smaller block from it and reserves single service ports inside that. Example sizes:
  100 ports per org, 20 per project.
- **Heavy-job slots stay with machine control.** Only machine control keeps a
  `heavy-jobs.md`; it records the holder as `<org>:<project>`. An org control relays a
  project's request to machine control, passes the grant on, and relays the done
  report. No org control keeps a copy.

A project asks its org control. An org control asks machine control. Nobody skips a
level; see "Reach a parent" in `references/operations.md`.
