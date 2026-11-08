# Chakrit Skills

Chakrit's personally published agent skills, distributed as an ACE school and as
ordinary skill directories.

| Skill           | Purpose                          | Maintained here |
| --------------- | -------------------------------- | --------------- |
| `fact-check`    | Verify claims and assess reviews | Yes             |
| `learn`         | Adaptive technical tutoring      | Yes             |
| `note-taker`    | Meeting and discussion notes     | Yes             |
| `safety-audit`  | Software trust and safety audits | Yes             |
| `1-by-1`        | Walk decisions one at a time     | Yes             |
| `wrap-up`       | Close a work session cleanly     | Yes             |
| `control`       | Set up control-agent hierarchy   | Yes             |
| `study`         | Visual decision studies          | Yes             |
| `de-slop`       | Strip AI tells from design, copy | Yes             |
| `gh-admin`      | GitHub org admin via OpenTofu    | Yes             |
| `lowfat-pantry` | Command-output filter pantry     | Imported        |
| `kien-thai`     | Natural Thai writing             | Imported        |
| `kode-thai`     | Iterative Thai writing audits    | Imported        |
| `smoke`         | Command-output snapshot testing  | Imported        |

## Use the skills

Copy a complete directory from `skills/` into the skill directory supported by your
agent. Keep its references and scripts together. Install `kien-thai` alongside
`kode-thai`, which depends on it.

For ACE, subscribe another project to this school:

```sh
ace setup chakrit/skills
```

## Maintain the school

`school.toml` imports the two Thai skills, lowfat-pantry, and smoke. `ace.toml`
selects PROD9 as the workflow school used to maintain this repository; those
workflow skills are not published here.

`ace paths school` normally resolves PROD9 here because it describes the editing
environment. Keep that selection. Before refreshing this collection's imports,
verify a supported way to target this checkout explicitly; do not run a school
mutation against PROD9 or change `ace.toml` to select this collection.
`ace link` updates the editing links supplied by PROD9.

[AGENTS.md](AGENTS.md) defines the editing boundaries, command-target checks, and
feedback destinations. Feedback for fact-check, learn, note-taker, safety-audit,
1-by-1, wrap-up, control, study, de-slop, and gh-admin belongs in `chakrit/skills`. Feedback for the Thai skills
belongs in `chakrit/kien-thai`; lowfat-pantry feedback belongs in
`chakrit/lowfat-pantry`; smoke feedback belongs in `chakrit/smoke`, beside the
SMOKE CLI it documents.

Edit the directly maintained skills here. Changes to imported packages belong
upstream; a later import refresh brings those changes into this collection.

## Documentation and references

Each skill owns its `references/`. Notes for agents editing a skill live in this
repository's [`docs/spec/`](docs/spec/), not in the published package.
Kien-thai's [research and maintenance docs](https://github.com/chakrit/kien-thai/tree/main/docs),
[corpus](https://github.com/chakrit/kien-thai/tree/main/corpus), and
[evaluation tooling](https://github.com/chakrit/kien-thai/tree/main/tests) remain
upstream; ACE imports the skill packages, not that development workspace.

## Sources

The direct ingestions started from these revisions:

- `fact-check`: `chakrit/fact-check` at
  `a88af9a75e06297a15c728d2907882a3e379eefe`.
- `learn`: `chakrit/learn` at
  `4a35557ed7b1fa330f184f9f15899fffb1714d67`.
- `note-taker` and `safety-audit`: the corresponding directories under `skills/`
  in `prod9/school` at `55d913f56df00ff7548eab329d4c56b91489d89d`.
- `1-by-1` and `wrap-up`: Chakrit's personal agent configuration
  (`claude/.claude/skills/` in `chakrit/dotfiles`), including its uncommitted edits
  as of 2026-11-03.
- `study`: `skills/study/` in `appbaobao/school` at
  `269553d88af3ab70cc06850867f3a93c865e9471`.
- `de-slop`: `skills/de-slop/` in `appbaobao/school` at
  `269553d88af3ab70cc06850867f3a93c865e9471`, identical to the copies in
  `prod9/school` and `datawowio/school`.
- `gh-admin`: `skills/gh-org-admin/` in `prod9/school` at
  `f804ec5a07868ca42a0ffdef137943751ff5a7f9`, renamed, with the secret files committed
  encrypted with git-crypt (`terraform.tfstate` always, `terraform.tfvars` when the repo
  commits it).

These skills are maintained here after ingestion and are not refreshed by
`ace school pull`.
The Thai packages, lowfat-pantry, and smoke are refreshed through `school.toml`
imports. Smoke was first extracted from `prod9/school` with the skills above, then
switched to an import of `skills/smoke/` from `chakrit/smoke` at
`689f85ce1a22a42cf58a9b712555ae2472adbd05`, whose copy was identical. The import
copies only that directory, not the SMOKE CLI source.
Lowfat-pantry was initially imported from `chakrit/lowfat-pantry` at
`e9d7d942297e7b76bd01e2a7b6e29ffe0b9a3ad8`, including its plugins, templates,
scripts, and documentation.

## License

[MIT](LICENSE) applies throughout this repository. Include the root license when
redistributing individual skill packages.
