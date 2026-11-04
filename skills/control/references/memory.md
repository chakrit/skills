# Memory

Engram (Gentleman-Programming/engram) is the shared memory for all three levels. Each
level has its own engram project; all of them live in one SQLite store per machine,
`~/.engram/engram.db`.

| Level           | Folder                         | Engram project      |
| --------------- | ------------------------------ | ------------------- |
| Machine control | `~/Documents/control`          | `control`           |
| Org control     | `~/Documents/<org>/control`    | `<org>`             |
| Project control | `~/Documents/<org>/<project>`  | `<org>-<project>`   |

## Where knowledge goes

Knowledge is engram-first. When unsure, treat it as machine-local working knowledge and
save it to engram at the narrowest level it applies to.

| Kind of knowledge                              | Where it goes                                                    |
| ---------------------------------------------- | ---------------------------------------------------------------- |
| Machine-wide (ports, tools, policies context)  | engram project `control`                                         |
| Org-wide (org conventions, cross-project)      | engram project `<org>`                                           |
| Project-wide (spans repos, ops, vendors)       | engram project `<org>-<project>`                                 |
| About one component repo, repo has ace-docs    | that repo's `docs/`, through its ace-docs gate                   |
| About one component repo, no ace-docs          | ask chakrit to set up ace-docs; never set it up yourself         |
| Same, and chakrit declines ace-docs            | engram project `<org>-<project>`, topic key `<repo>/<subject>`   |
| Policies                                       | `~/Documents/control/policies/<level>.md`                        |
| Registries                                     | the control's `registries/`                                      |
| Task ledger                                    | the control's `tasks.md`                                         |
| Waiting on chakrit                             | the control's `human.md` (waiting page)                          |
| Agent in-flight state, raw captures            | the agent's gitignored `.ace/`                                   |

Write no other knowledge files. To read another level's knowledge, use engram's
all-projects search instead of copying it into your own project.

## Set up a level's engram project

Use the project name the setup reference gives you.

1. Check whether engram is installed: `command -v engram`.
2. If it prints nothing, do not install it. Add this line to the control's `human.md`:
   `engram pin pending: run engram init <name> in <folder>`. A project control has no
   `human.md`; message its org control to add the line to the org's `human.md`. Then
   continue the setup.
3. If engram is on PATH, run at the folder root:

   ```sh
   engram init <name>
   ```

   This writes `.engram/config.json`. Commit it with the rest of the setup.
4. Always pin. Clones use the remote `gh`, and engram reads only a remote named
   `origin`, so an unpinned folder resolves to its directory name and collides with
   same-named folders elsewhere.
5. If a session ever starts inside a component clone, pin that clone with the same
   name and add `.engram/` to the clone's `.git/info/exclude`. Never commit `.engram/`
   into a component repo.
6. Do not use engram project aliases. They do not affect project resolution.

## Session protocol

1. At session start and after context compaction, call `mem_context` for your own
   project. Then read the `spec` memories for the area you will work on. Nothing
   injects context automatically.
2. Before concluding something is new, `mem_search` with the area and identifiers.
   Search all projects when the subject may belong to another level.
3. When something is learned, decided, or fixed, save it (see "Saving a memory").
4. Keep in-flight task state in `.ace/` (ACE's `ace-save`), not in engram.

## Saving a memory

Access engram through its MCP tools and its CLI only. Never install an engram plugin or
hooks in any harness. Save only deliberately; nothing saves on its own.

| Type                              | Meaning                                                   | Authority                     | Shape                                                    |
| --------------------------------- | --------------------------------------------------------- | ----------------------------- | -------------------------------------------------------- |
| `spec`                            | Our own design, surface, conventions, decisions: truth    | binding; read before work     | one memory per subject, upserted in place by `topic_key` |
| `guide`                           | How-to or runbook (deploy, rotate secrets)                | follow unless a spec differs  | one per task                                             |
| `vendor`                          | Third-party reference, trimmed to what we use             | reference                     | one per tool or topic; cite the version checked          |
| `plan`                            | Active initiative with status and next step               | working                       | one per initiative, upserted; retired when done          |
| `scratch`                         | Unsettled exploration                                     | none                          | opens with "not spec because ___"; last resort           |
| `discovery`, `bugfix`, `learning` | Observations made while working                           | lead; verify before relying   | short: What / Why / Where / Learned                      |
| `session_summary`                 | End-of-session summary (`mem_session_summary`)            | lead                          | engram-native                                            |

Rules:

- **Classify, first match wins:** third-party lookup → `vendor`; a how-to → `guide`;
  our own design or surface → `spec`; an initiative → `plan`; unsettled → `scratch`.
  Observations made while working take the working types.
- **`spec` is binding.** Read it before working and comply. If one is wrong, raise it
  with chakrit, then amend it.
- **Everything settled is a `spec` amendment:** an instruction, an agreed approach, a
  chosen library, a fixed convention. Write the rule as given, without justification
  or alternatives. There is no decisions log.
- **Search before saving.** Amend the existing memory on a subject; never write a
  second one. When promoting a working memory to a `spec` or `guide`, update the old
  memory in place to a one-line pointer naming the new `topic_key`.
- **Leads are not sources.** Verify working-type memories against code or specs before
  acting on them.
- **`topic_key` = `<area>/<subject>`.** Specs, guides, vendor entries and plans always
  have one. Example areas: machine level `machine`, `ports`, `policies`; org level
  `org`, `<project>`; project level each component repo name, `project`, `ops`,
  `vendor`. Examples: `ports/allocation`, `api/auth-flow`, `ops/environments`.
- **Titles lead with search terms:** repo, component, environment, identifiers.
  "api prod: login returns 502 after proxy bump", not "Fixed login issue".
- **End every memory with a `Keywords:` line.** Be generous: synonyms, Thai and English
  terms, service and environment names, error strings, file names. Search matches
  substrings only; a synonym matches only if it is written down.
- **Bodies cite sources:** repo-relative paths, commit hashes, other memories' topic
  keys. Never cite numeric memory IDs.
- **Size:** content is capped at 50,000 characters and truncated beyond that. Split
  long specs by subject.

## Install steps for chakrit

Agents never run these. Never install or register engram, and never change
`~/.claude.json`, `~/.claude/settings.json`, shell profiles, Homebrew, or global MCP
registrations. Give chakrit this list when he asks how to install engram:

```text
1. Install the engram binary (a single Go binary; no server, no Postgres).
2. Register an MCP server in each harness that runs `engram mcp` over stdio per
   session. It opens ~/.engram/engram.db directly.
3. Set ENGRAM_NO_UPDATE_CHECK=1 in that server's environment to disable the
   release check, its only default network call.
4. Do NOT run `engram setup claude-code`. It installs hooks and a plugin and offers
   to rewrite ~/.claude/settings.json.
5. Before every upgrade, back up ~/.engram/engram.db. Migrations run automatically
   and downgrade is untested.
6. Resolve each "engram pin pending" line in human.md files by running
   `engram init <name>` in the named folder, then commit .engram/config.json there.
```
