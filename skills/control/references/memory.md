# Memory

Engram (Gentleman-Programming/engram) is the shared memory for all three levels. Each
level has its own engram project; all of them live in one SQLite store per machine,
`~/.engram/engram.db`.

Engram comes first. Every rule set agents follow is an engram entry in project
`control`, seeded from `templates/rules/<topic>.md`, and each instruction file points to
the entries it must load and when. The memory rules themselves are the entry
`control/memory` (`templates/rules/memory.md`); its first section decides what goes in
engram and what stays in files. Without engram, the copies in
`~/Documents/control/rules/` are the live rules and `memory/` folders hold what engram
would.

## Seed the rule entries

Machine setup runs this once; machine control runs it again for a rule entry chakrit
approves changing.

1. If engram is not available, skip this section. The files setup copied to
   `~/Documents/control/rules/` are the live rules.
2. For each file in `~/Documents/control/rules/`, call engram's `mem_save` MCP tool
   with project `control`, topic key `control/<file name without .md>` (for example
   `control/policy-org`), the file's first heading as the title and the whole file as
   the content. The CLI's `engram save` takes no topic key, so use the MCP tool.
3. Check each entry: `mem_search` its topic key in project `control` and
   `mem_get_observation` the result. The full text must match the file.

## Set up a level's engram project

Use the project name the setup reference gives you.

1. Check whether engram is installed: `command -v engram`.
2. If it prints nothing, do not install it. Report this line in the setup's completion
   report to chakrit: `engram pin pending: run engram init <name> in <folder>`. Then
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

## Install steps for chakrit

Agents never run these. Never install or register engram, and never change
`~/.claude.json`, `~/.claude/settings.json`, shell profiles, Homebrew, or global MCP
registrations. Give chakrit this list when chakrit asks how to install engram:

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
6. For each "engram pin pending" line a setup reported, run `engram init <name>` in
   the named folder, then commit .engram/config.json there.
```
