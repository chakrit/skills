# Chakrit Skills

This repository, `chakrit/skills`, publishes Chakrit's personal skills. It uses ACE
school tooling to import other skill repositories. Agents editing this repository
use the separate `prod9/school` workflow.
`CLAUDE.md` is a symlink to this file; maintain one shared instruction source.

## Two separate roles

- `ace.toml` configures the agent environment for EDITING this repository. Keep
  `school = "prod9/school"`. Do not change it to `"."` to make this repository a school.
- `school.toml` defines the PUBLISHED collection and its upstream `[[imports]]`.
  It imports kien-thai and kode-thai from `chakrit/kien-thai`, lowfat-pantry
  from `chakrit/lowfat-pantry`, and smoke from `chakrit/smoke`.
- `skills/` contains the published packages. `.agents/skills/` contains generated
  links to the editing workflow. Identical names in these directories do not mean
  identical ownership or content: `.agents/skills/fact-check/` resolves into PROD9,
  while `skills/fact-check/` is this repository's maintained source.
- Using PROD9's authoring and review procedures does not make PROD9 the destination
  for this repository's skill edits or feedback. Do not copy its workflow skills
  into the published collection or add PROD9 as an import to solve editing setup.

## Editing and feedback routing

Before editing or preparing feedback, identify the exact skill, its source repository,
and the target file. Resolve symlinks before writing. Read this repository's actual
`skills/<name>/` content when reviewing its published packages, even if a skill with
that name is already loaded through PROD9.

- **fact-check, learn, note-taker, safety-audit, 1-by-1, wrap-up, and control:** edit their
  directories under `skills/` here.
  Route feedback and proposed changes to `chakrit/skills`, including feedback about
  copies loaded through PROD9. Former standalone repositories and copies extracted
  from PROD9 are ingestion sources, not the ongoing maintenance destinations.
- **kien-thai and kode-thai:** the local directories are imported copies. Route
  feedback and fixes to `chakrit/kien-thai`, then refresh the declared import after
  an authorized upstream change. Do not patch the imported copies as a lasting fix.
- **lowfat-pantry:** route feedback and changes to `chakrit/lowfat-pantry` and
  refresh the import. Keep its bundled plugins, templates, scripts, and docs intact.
  Its nested instruction and configuration files describe the upstream package;
  they do not change this repository's editing environment or grant upstream writes.
- **smoke:** the skill lives beside the SMOKE CLI it documents. Route feedback and
  changes to `chakrit/smoke` and refresh the import; the import copies only
  `skills/smoke/`, not the CLI source.
- **PROD9 workflow skills:** feedback about PROD9-owned editing procedures belongs
  to `prod9/school`. A request to edit this repository does not authorize changing
  that separate checkout. For any imported skill in PROD9, establish its actual
  upstream owner rather than treating the loaded copy as its source.
- **Unclear target:** ask which skill or repository the user means before writing;
  do not default to the school returned by `ace paths school`.

Feedback requests authorize findings or a draft, not sending messages, opening issues
or PRs, pushing, or editing another repository. Obtain explicit authorization for
those actions and name the destination before executing them.

## Ownership and layout

- `skills/fact-check/`, `skills/learn/`, `skills/note-taker/`,
  `skills/safety-audit/`, `skills/1-by-1/`, `skills/wrap-up/`, and `skills/control/` are
  maintained
  directly in this repository.
- `skills/kien-thai/` and `skills/kode-thai/` are imported from chakrit/kien-thai.
  Follow the upstream ownership and command-target checks in this file.
- `skills/lowfat-pantry/` is imported from chakrit/lowfat-pantry.
- `skills/smoke/` is imported from chakrit/smoke.
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

Run `ace` for recurring work. `ace skills`, `ace config`, and `ace paths school`
describe the editing environment; resolving PROD9 is expected and is not a broken
configuration. `ace link` refreshes the generated editing links.

Use Git in this checkout to inspect this repository's changes. Do not substitute
`ace diff` output from PROD9 for a review of `chakrit/skills`.

Before `ace import`, `ace school pull`, or another school mutation, verify the exact
checkout the command will modify. Running a command from this directory alone is not
proof that it targets this collection. For collection imports, target this checkout
explicitly using a supported mechanism verified against the installed CLI. If that
mechanism is unavailable or unclear, report the missing targeting capability; do not
switch `ace.toml`, mutate PROD9, or guess command flags to get past it.

A verified targeting method is a temporary project under `.ace/import-project/`
whose `ace.toml` selects this checkout by absolute path. Run `ace paths school`
there first; continue with `ace school pull` and `ace school validate` only when
it resolves this collection. Keep this temporary config ignored and leave the
repository-root editing config unchanged.

Before committing a direct skill ingestion, compare its SKILL.md and references
against the recorded source revision, check relative links, and inspect the full diff.
No repository-wide build or model evaluation is required for package ingestion.

Use `ace-skill` for authored skill revisions and `ace-school` for school reviews.
Use the workflow skills supplied by the selected PROD9 editing school. Load `code` and
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

## Merging pull requests

When a pull request is merged, merge it first as it stands, then do any follow-up work
as new commits on top of `main`. Rebase-merge when possible; fall back to another merge
method only when a rebase fails. Reworking the PR branch or replacing the PR with a new
commit hides what the author proposed and what the follow-up changed; separate commits
keep both reviewable. If local `main` has unpushed commits, rebase them onto the merged
`main` before continuing. Each merge still needs chakrit's authorization.
