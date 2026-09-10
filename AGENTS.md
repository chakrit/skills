# Personally published skills

This repository collects Chakrit's personally published agent skills. The initial
consolidation sources are chakrit/kien-thai, chakrit/fact-check, and chakrit/learn.

## Repository layout

Publish each skill as a real directory under skills/<name>/ with a SKILL.md entry
point and its supporting resources. Keep runtime references in skills/<name>/references/ and
skill-local explanatory documents in skills/<name>/docs/ when needed. Keep
maintenance documentation under docs/skills/<name>/ after the docs gate is
established. Keep relative references valid and preserve
source licenses and attribution during consolidation. These packages must remain
usable independently of the agent application used to maintain this repository.

The .agents/skills/ directory contains ACE-managed workflow links into the ACE Home
school. Edit this repository's published skills under skills/, not through those
links. Changes to the ACE Home school are a separate task.

## Working commands and conventions

Run ace to start or resume work. Run ace skills and ace config to inspect the active
workflow configuration, ace paths to locate it, and ace link after approved changes
to the workflow selection.

The shared workflow selection is ace, ace-audit, ace-docs, ace-init, ace-save, and
ace-skill. The inherited user selection also activates ace-afk and ace-school.
Use ace-skill when authoring or revising published skills.

No project build or test command is established yet. During migration, preserve and
inspect source checks before documenting runnable commands. Load the code and
architect skills before designing or editing code; report a missing required skill.

Use the current branch by default and the gh remote. Wrap prose at 90 columns where
practical and align Markdown table pipes. Always capitalize PRODIGY9.

## Durable documentation

The planned durable documentation root is docs/. It has not been scaffolded yet.
Use ace-docs to establish its gates before creating durable architecture, domain,
or design documents. Keep the public skill catalog and installation guidance in
README.md when the skill packages are consolidated.

## Git checkpoints

Commit coherent, completed slices autonomously after completing the checks required for
that work. Do not ask for permission to make a local commit. A local commit does not
authorize pushing, publishing, merging, releasing, deploying, or any other change to
shared or external state; each requires separate user authorization.
