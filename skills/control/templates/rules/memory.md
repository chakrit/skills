# Rules: memory

Engram entry `rule/memory` in project
`<machine>-control-rules` (without engram, the file
`~/Documents/control/rules/memory.md`). Memory rules for every control agent at every
level. Machine control owns this entry. Load it in full at session start and after a
clear.

## Where things go

Engram first. Use files only for what must be read by path or shown on a page.

| What                                                       | With engram (recommended)                | Without engram                            |
| ---------------------------------------------------------- | ---------------------------------------- | ----------------------------------------- |
| Rules: level policies, these memory rules, handling agents | engram project `<machine>-control-rules` | `~/Documents/control/rules/<topic>.md`    |
| Knowledge and findings an agent recalls when relevant      | engram, the level's project              | `memory/<topic>.md` in the level's folder |
| Decisions and their reasoning, beyond the quoted ruling    | engram, the level's project              | `memory/<topic>.md`                       |
| Agents' wake-up and state reports                          | engram, the reporting agent's project    | `memory/<topic>.md`                       |
| Done tasks, once they leave `control.data.js`              | engram, the control's project            | `memory/tasks-done.md`                    |
| Registries (ports, heavy-job slots, members)               | files in `registries/`                   | files in `registries/`                    |
| Live tasks and Needs Attention                             | `control.data.js`                        | `control.data.js`                         |
| About one component repo                                   | that repo's own docs tree                | that repo's own docs tree                 |

A component repo's docs travel with its clone, so knowledge about one repo goes in that
repo's docs, following the repo's own convention (`ace-docs` where ACE is available).
If the repo has no docs tree, ask chakrit before setting one up. If chakrit declines,
save it in the project's engram project with topic key `<repo>/<subject>`, or in
`memory/<repo>-<subject>.md` without engram.

Check once per session whether engram is available: the `mem_search` tool exists. The
`engram` binary alone is not enough; rules load only through the MCP tools. Use one way
for the whole session.

## Engram projects

All projects share one store per machine. Every name starts with the machine, like
agent names, so two machines' stores never share a project name.

| Project                     | Holds                                   | Writers              |
| --------------------------- | --------------------------------------- | -------------------- |
| `<machine>-control-rules`   | the five rule entries and a rules index | machine control      |
| `<machine>-control`         | machine control's memory                | machine control      |
| `<machine>-<org>`           | one org control's memory                | that org control     |
| `<machine>-<org>-<project>` | one project control's memory            | that project control |

The project says where an entry lives; the topic key names it inside the project. Save
at the narrowest level the knowledge applies to. To read another level's knowledge,
search all projects instead of copying it into your own.

## Loading a rule entry

An instruction file or a wake message names the rule entries to load. Load each in full
before the work it governs:

1. `mem_search` with the topic key as the query (for example `rule/policy-org`) and
   project `<machine>-control-rules`.
2. Take the result whose `topic_key` equals the key exactly. Other results that merely
   mention the key are not the rule.
3. `mem_get_observation` with that result's ID. Search results are truncated; a rule
   read from a search result alone is incomplete.
4. If no result has the exact key, stop the work the entry governs and tell machine
   control the entry is missing. A machine with engram has no rule files to fall back
   to; never work from what you remember of a rule.

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
- **Give it a topic key** from this table. A save under an existing key replaces that
  entry, so pick the key for what should be replaced and what should not. Without
  engram, the file name is the topic key with `/` replaced by `-`:
  `memory/ports-allocation.md`.

  | Kind                                               | Topic key                   | Type        |
  | -------------------------------------------------- | --------------------------- | ----------- |
  | Knowledge and findings                             | `<area>/<subject>`          | any fitting |
  | Knowledge about a repo with no docs tree           | `<repo>/<subject>`          | any fitting |
  | A decision and its reasoning                       | `decision/<subject>`        | `decision`  |
  | The reasoning behind one repo's decision           | `<repo>/decision-<subject>` | `decision`  |
  | An agent's latest state report (replaces the last) | `status/<agent-name>`       | `manual`    |
  | A done task (never re-saved)                       | `done/<yyyy-mm>/<slug>`     | `manual`    |

- **Never use a `rule/` key** outside the rules project. `rule/` names rule entries
  only.
- **Lead the title with search terms** (repo, environment, identifiers) and end the
  body with a `Keywords:` line of synonyms, Thai and English terms and error strings.
  Search matches substrings only.
- **Cite sources** by repo-relative path or commit hash.

## Amending a rule entry

Only machine control amends rule entries, for a ruling from chakrit or a proposal
chakrit approves. Find the entry's ID as "Loading a rule entry" describes, then call
`mem_update` with that ID and `expected_project: <machine>-control-rules`. Append
chakrit's quoted ruling with its date to the entry's "Rulings" section, adding the
section at the end if it is missing. Never re-save a rule by topic key: a mistyped key
or project creates a second entry instead of replacing the rule. Without engram, edit
the file in `~/Documents/control/rules/` and commit it with the quoted ruling in the
message.

## Engram itself

If an engram release puts export of the store behind a paid tier, tell chakrit before
upgrading.
