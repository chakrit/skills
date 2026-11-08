# Memory

Engram (Gentleman-Programming/engram) is the shared memory for all three levels. Each
level has its own engram project; all of them live in one SQLite store per machine,
`~/.engram/engram.db`.

Engram comes first. Every rule set agents follow is an engram entry in the machine's
rules project, `<machine>-control-rules`, seeded from `templates/rules/<topic>.md` under
topic key `rule/<topic>`; each instruction file points to the entries it must load and
when. The memory rules themselves are the entry `rule/memory`
(`templates/rules/memory.md`); its first section decides what goes in engram and what
stays in files. With engram, engram is the only copy of the rules. Without engram,
setup copies the seeds to `~/Documents/control/rules/` as the live rules, and
`memory/` folders hold what engram would.

Every engram project name starts with the machine, like agent names, so stores from
two machines never share a project name.

| Engram project              | Holds                                   | Created by                                        |
| --------------------------- | --------------------------------------- | ------------------------------------------------- |
| `<machine>-control-rules`   | the five rule entries and a rules index | "Seed the rule entries"                           |
| `<machine>-control`         | machine control's memory                | `engram init` in `~/Documents/control`            |
| `<machine>-<org>`           | one org control's memory                | `engram init` in the org control                  |
| `<machine>-<org>-<project>` | one project control's memory            | `engram init` in the project folder               |

Only the rules project needs seeding. The other projects exist once their folder is
pinned and the first save lands; their topic keys are conventions in `rule/memory`.

## Seed the rule entries

Machine setup runs this once, after "Set up a level's engram project" for machine
control.

1. If engram's MCP tools are not available (no `mem_save` tool), copy this skill's
   `templates/rules/*.md` to `~/Documents/control/rules/` and stop; those files are the
   live rules. With engram, write no `rules/` folder: engram is the only copy.
2. Create the rules project with one CLI save. `mem_save` refuses a project engram does
   not know yet, and the rules project has no folder to pin it:

   ```sh
   engram save "rules index: <machine>-control-rules" "Rule entries for control agents: rule/policy-machine, rule/policy-org, rule/policy-project, rule/memory, rule/handling-agents. Load each by exact topic key, then mem_get_observation." --project <machine>-control-rules --type config
   ```

3. For each file in this skill's `templates/rules/`, call `mem_save` with project
   `<machine>-control-rules`, topic key `rule/<file name without .md>` (for example
   `rule/policy-org`), title `rule/<topic> — <the file's first heading>`, type
   `config`, `capture_prompt: false`, and the whole file as the content.
4. Check each entry: `mem_search` its topic key with project `<machine>-control-rules`,
   take the result whose `topic_key` equals it, and `mem_get_observation` that ID. The
   full text must match the file.
5. Saves in one project raise "conflict review pending" against similar entries. Leave
   these reviews; unjudged reviews are harmless.

## Set up a level's engram project

Machine setup runs this for machine control. Org and project controls pin their own
folders when they are initiated, as the initiation message in `rule/handling-agents`
says. Use the project name the setup reference gives you.

1. Check whether engram is installed: `command -v engram`.
2. If it prints nothing, do not install it. Report this line in the setup's completion
   report to the user: `engram pin pending: run engram init <name> in <folder>`. Then
   continue the setup.
3. If engram is on PATH, run at the folder root:

   ```sh
   engram init <name>
   ```

   This writes `.engram/config.json`. Commit it with the rest of the setup, except in
   a component repo: a single-repo project's folder, or a clone in a wrapper.
4. Always pin. An unpinned folder takes its name from its `origin` remote or, without
   one, from its directory, and collides with same-named folders elsewhere.
5. In a component repo, add `.engram/` to its `.git/info/exclude` instead. Never commit
   `.engram/` into a component repo. If a session ever starts inside a clone in a
   wrapper, pin that clone with the wrapper's name the same way.
6. Do not use engram project aliases. They do not affect project resolution.

## Install steps for the user

Agents never run these. Never install or register engram, and never change
`~/.claude.json`, `~/.claude/settings.json`, shell profiles, Homebrew, or global MCP
registrations. Give the user this list when the user asks how to install engram:

```text
1. Install the engram binary (a single Go binary; no server, no Postgres).
2. Register an MCP server in each harness that runs `engram mcp` over stdio per
   session. It opens ~/.engram/engram.db directly.
3. Set ENGRAM_NO_UPDATE_CHECK=1 in that server's environment to disable the
   release check, its only default network call.
4. Do NOT run `engram setup claude-code`. It installs hooks and a plugin and offers
   to rewrite ~/.claude/settings.json.
5. For each "engram pin pending" line a setup reported, run `engram init <name>` in
   the named folder, then commit .engram/config.json there, except in a component
   repo, where .engram/ goes in .git/info/exclude.
```
