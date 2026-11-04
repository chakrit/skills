# Memory

Engram (Gentleman-Programming/engram) is the shared memory for all three levels. Each
level has its own engram project; all of them live in one SQLite store per machine,
`~/.engram/engram.db`.

The rules agents follow live in `templates/policies/memory.md`, which machine setup
copies to `~/Documents/control/policies/memory.md`. Its first section is the rule that
decides between files and engram: what an agent must follow every time, and durable
state such as registries, goes in files loaded by path; what an agent recalls when
relevant goes in engram.

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
