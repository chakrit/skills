# Policy: memory

Memory rules for every control agent at every level. Machine control owns this file.

## Files or engram

| What                                                     | Where          |
| -------------------------------------------------------- | -------------- |
| Rules an agent must follow every time                    | files, by path |
| Durable coordination state: registries, `tasks.md`       | files, by path |
| What an agent recalls when relevant: knowledge, findings | engram         |

Engram is searched, so a memory is the best knowledge found, not a rule guaranteed to
apply. A rule that must hold every time belongs in a policy or instruction file.

Each level has its own engram project; all of them share one store per machine.

| Level           | Engram project    |
| --------------- | ----------------- |
| Machine control | `control`         |
| Org control     | `<org>`           |
| Project control | `<org>-<project>` |

If engram is not installed, skip every engram step.

## Where knowledge goes

Save knowledge at the narrowest level it applies to.

| Kind of knowledge                          | Where it goes                                                  |
| ------------------------------------------ | -------------------------------------------------------------- |
| Machine-wide (tools, resource history)     | engram project `control`                                       |
| Org-wide (org conventions, cross-project)  | engram project `<org>`                                         |
| Project-wide (spans repos, ops, vendors)   | engram project `<org>-<project>`                               |
| About one component repo with a docs tree  | that repo's docs, following the repo's own docs convention     |
| About one component repo with no docs tree | ask chakrit before setting one up                              |
| Same, and chakrit declines a docs tree     | engram project `<org>-<project>`, topic key `<repo>/<subject>` |
| Things needing chakrit's attention         | the org control's `human.html`; projects report to it          |

Write no other knowledge files. To read another level's knowledge, search all engram
projects instead of copying it into your own.

## Session

1. At session start and after compaction, call `mem_context` for your own project.
   Nothing injects context automatically.
2. Before concluding something is new, `mem_search` with the area and identifiers.
   Search all projects when the subject may belong to another level.

## Saving a memory

Use engram's MCP tools and CLI only; never install an engram plugin or hooks. Save
deliberately; nothing saves on its own.

- **Search before saving.** Amend the existing memory on a subject instead of writing a
  second one.
- **Give it a `topic_key`** of the form `<area>/<subject>`: `ports/allocation`,
  `api/auth-flow`.
- **Lead the title with search terms** (repo, environment, identifiers) and end the
  body with a `Keywords:` line of synonyms, Thai and English terms and error strings.
  Search matches substrings only.
- **Cite sources** by repo-relative path or commit hash.

## Engram itself

If an engram release puts export of the store behind a paid tier, tell chakrit before
upgrading.
