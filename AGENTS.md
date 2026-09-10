# Chakrit Skills

This repository is Chakrit's ACE school for personally published agent skills.
`school.toml` declares this school's imports. `ace.toml` selects `prod9/school`
for the workflow used to maintain this repository.
`CLAUDE.md` is a symlink to this file.

## Ownership and layout

- `skills/fact-check/` and `skills/learn/` are maintained directly in this repository.
- `skills/kien-thai/` and `skills/kode-thai/` are imported from chakrit/kien-thai.
  Make changes upstream and refresh them with `ace school pull`.
- Each published skill keeps its runtime references in `references/` and supporting
  documentation in `docs/` within its own directory. Preserve relative references,
  source attribution, and the root MIT license. README.md is the catalog and source record.
- Kien-thai's research docs, corpus, and evaluation tooling remain upstream; links
  are in README.md. Do not migrate them into this school as part of a skill refresh.
- `.agents/skills/` contains generated links. Edit owned packages through `skills/`.
- `.ace/` holds ignored local session records and temporary source checkouts.

Keep skill packages usable independently of the agent application used to maintain
this school. Preserve the sibling relationship between kien-thai and kode-thai.

## Commands and checks

Run `ace` for recurring work. Use `ace skills` and `ace config` to inspect the
workflow configuration. `ace link` links the selected PROD9 workflow into this project.
Before using `ace school pull` for this repository, confirm that `ace paths school`
resolves this checkout rather than PROD9. Refresh and validate only the intended school.

Before committing a direct skill ingestion, compare its SKILL.md and references
against the recorded source revision, check relative links, and inspect the full diff.
No repository-wide build or model evaluation is required for package ingestion.

Use `ace-skill` for authored skill revisions and `ace-school` for school reviews.
Keep `ace` and `ace-save` available with the ACE Home workflow. Load `code` and
`architect` before designing or editing code; the PROD9 school is an authorized
source for those skills when absent from this school's active set.

Use the current branch and the `gh` remote. Wrap prose at 90 columns where practical,
align Markdown table pipes, and always capitalize PRODIGY9.

## Durable documentation

Skill documentation belongs alongside its package. No repository-wide docs tree is
established. Use `ace-docs` before creating the first repository-wide architecture,
domain, or design document.

## Git checkpoints

Commit coherent, completed slices autonomously after completing the checks required for
that work. Do not ask for permission to make a local commit. A local commit does not
authorize pushing, publishing, merging, releasing, deploying, or any other change to
shared or external state; each requires separate user authorization.
