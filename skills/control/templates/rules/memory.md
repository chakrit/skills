# Rules: memory

Engram entry `control/memory` in project `control` (fallback file
`~/Documents/control/rules/memory.md`). Memory rules for every control agent at every
level. Machine control owns this entry. Load it in full at session start and after a
clear.

## Where things go

Engram first. Use files only for what must be read by path or shown on a page.

| What                                                       | With engram (recommended)             | Without engram                            |
| ---------------------------------------------------------- | ------------------------------------- | ----------------------------------------- |
| Rules: level policies, these memory rules, handling agents | engram entries in project `control`   | `~/Documents/control/rules/<topic>.md`    |
| Knowledge and findings an agent recalls when relevant      | engram, the level's project           | `memory/<topic>.md` in the level's folder |
| Decisions and their reasoning, beyond the quoted ruling    | engram, the level's project           | `memory/<topic>.md`                       |
| Agents' wake-up and state reports                          | engram, the reporting agent's project | `memory/<topic>.md`                       |
| Done tasks, once they leave `control.data.js`              | engram, the control's project         | `memory/tasks-done.md`                    |
| Registries (ports, heavy-job slots, members)               | files in `registries/`                | files in `registries/`                    |
| Live tasks and Needs Attention                             | `control.data.js`                     | `control.data.js`                         |
| About one component repo                                   | that repo's own docs tree             | that repo's own docs tree                 |

A component repo's docs travel with its clone, so knowledge about one repo goes in that
repo's docs, following the repo's own convention (`ace-docs` where ACE is available).
If the repo has no docs tree, ask chakrit before setting one up. If chakrit declines,
save it in the project's engram project with topic key `<repo>/<subject>`, or in
`memory/<repo>-<subject>.md` without engram.

Check once per session whether engram is available: the `mem_search` tool exists, or
`command -v engram` prints a path. Use one way for the whole session.

## Engram projects

Each level has its own engram project; all of them share one store per machine.

| Level           | Engram project    |
| --------------- | ----------------- |
| Machine control | `control`         |
| Org control     | `<org>`           |
| Project control | `<org>-<project>` |

Save at the narrowest level the knowledge applies to. To read another level's
knowledge, search all projects instead of copying it into your own.

## Loading a rule entry

An instruction file or a wake message names the rule entries to load. Load each in full
before the work it governs:

1. `mem_search` with the topic key (for example `control/policy-org`) and project
   `control`.
2. `mem_get_observation` with the result's ID. Search results are truncated; a rule
   read from a search result alone is incomplete.
3. If nothing is found, read the fallback file the pointer names, and tell machine
   control the entry is missing.

## Session

1. At session start and after compaction, call `mem_context` for your own project, or
   read your `memory/` folder's file list without engram. Nothing injects context
   automatically.
2. Before concluding something is new, `mem_search` with the area and identifiers
   (search all projects when the subject may belong to another level), or search
   `memory/` with `grep -rn` without engram.

## Saving

Save before a clear or handoff, preferring engram's `mem_session_summary`, and report
what you saved and where. Save deliberately; nothing saves on its own. Use engram's MCP
tools and CLI only; never install an engram plugin or hooks.

- **Search before saving.** Amend the existing entry or file on a subject instead of
  writing a second one.
- **Give it a topic key** of the form `<area>/<subject>`: `ports/allocation`,
  `api/auth-flow`. Without engram, the file name is the topic key with `/` replaced by
  `-`: `memory/ports-allocation.md`.
- **Lead the title with search terms** (repo, environment, identifiers) and end the
  body with a `Keywords:` line of synonyms, Thai and English terms and error strings.
  Search matches substrings only.
- **Cite sources** by repo-relative path or commit hash.

## Amending a rule entry

Only machine control amends rule entries, for a ruling from chakrit or a proposal
chakrit approves. Save under the same topic key so the entry is replaced, not
duplicated, and put chakrit's quoted ruling with its date at the end of the entry.
Without engram, edit the fallback file and commit it with the quoted ruling in the
message.

## Engram itself

If an engram release puts export of the store behind a paid tier, tell chakrit before
upgrading.
