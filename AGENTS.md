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

## Personal instructions are not skill requirements

chakrit's user-level instructions (`~/.claude/CLAUDE.md` and its equivalents) govern
how an agent works with chakrit while editing this repository. They say nothing about
what the published skills should contain: those skills run for other agents, on other
machines and setups, under their own rules. Do not copy those preferences into a skill,
and do not report a skill as conflicting with them. Judge a skill against its own
`SKILL.md`, its spec in `docs/spec/` and chakrit's rulings on that skill. A personal
preference enters a skill only when chakrit asks for it in that skill. When a skill
conflicts with chakrit's personal instructions, leave the conflict alone: chakrit rules
on it when invoking the skill.

## The control setup running this agent is not the control skill

The agent editing this repository usually runs as a controlled agent in chakrit's own
control setup: a control agent wakes it, relays tasks and rulings, and it loads live
rules from engram project `<machine>-control-rules` (or `~/Documents/control/rules/`
without engram). Machine control installed those rules from an earlier version of the
`control` skill and amends them on its own, so they and `skills/control/` drift apart in
both directions. Mixing the two either leaves a warranted skill change unmade or edits
the skill to match one machine's live setup.

- Follow the live rules for your own conduct as a controlled agent: messaging,
  reporting, resources, memory. They do not tell you what the skill says or should say.
- Judge a change to `skills/control/` only against the skill's own files, its spec and
  chakrit's rulings on the skill, as for any skill. A live rule that already holds a
  change (for example, refusing to type into a pane with typed input) does not make
  the skill change unnecessary. When chakrit and you agree a change is warranted, make
  it in the skill whether or not the live rules carry it.
- A skill change does not update the live rules, and you never edit them: machine
  control owns them. When they differ from a landed skill change, tell your control.

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

## Context setup before a skill discussion or edit

A skill is a small system: its files have roles, readers, owners and loading rules, and
its spec records the design. A proposal that answers only the request at hand tends to
break a rule written elsewhere in the skill, and each later fix breaks another. Before
proposing, discussing or editing a change to a skill, build that model first:

1. Read the skill's `SKILL.md`, its spec (`docs/spec/<skill>.md`, when it has one), and
   every file the change touches or names.
2. Write down, for yourself, the skill's layout model: which files exist and what each
   may hold, who reads each one, when it is loaded (whole at session start, a section
   on demand, only during setup), who owns and amends it, and where installed copies
   live on the machine.
3. For each file the change touches, name the agent that reads it first and what that
   agent is doing at that moment (in the control skill: a control starting an agent, a
   project control just woken, a setup running in another org's environment). Write
   only what that agent needs for that task and cannot already get from its own
   context: its instruction file, the instructions and skills its environment loads,
   its harness. A fact the reader already gets from its environment does not belong in
   the skill; a copy goes stale and contradicts the source.
4. List the skill's stated constraints on structure and content, with `file:line`
   (for example "governance only", "one file per level", "loaded whole").
5. Check every proposal against that model and those constraints before presenting it.
   When a request conflicts with one, say so and quote the rule; do not choose silently.
6. When the user corrects a proposal, recheck the next one against the whole model, not
   only against the correction.

## Audits and fix loops on a skill

An audit checks a skill's integrity against what already exists: its own files and
chakrit's rulings on it, recorded with chakrit's words in `.ace/control-rulings.md`
(frozen) and, for later rulings, `.ace/save.ledger.md`. A fix makes the skill agree
with itself and with those rulings. It never adds a requirement, step, check, branch or
stop condition that no ruling asked for, and never widens or narrows a ruling. The tempting failure is to fill each gap an audit finds with a
plausible new step and cite a general ruling ("align all layers", "ask chakrit when
unclear") as its basis. Each addition is new surface for the next audit, so the loop
never converges, and chakrit has to find and undo work nobody asked for.

- Fix only text that contradicts other text in the skill or a ruling, or a step that
  cannot be followed as written. Make the smallest change that removes the conflict;
  prefer rewording or deleting over adding a step.
- A gap that no ruling covers is a finding, not a fix. Bring it to chakrit as a
  question, or drop it when it needs several unusual conditions at once.
- A general ruling does not settle a specific gap. Cite a ruling as the basis only when
  its words decide that case.
- When briefing an audit agent, ask for contradictions and steps that cannot be
  followed, not for "gaps", and tell it not to propose new steps.
- An audit-fix loop ends when a pass finds no contradiction. Remaining questions go to
  chakrit in one `1-by-1` walk, not into another loop.

## Ownership and layout

- `skills/fact-check/`, `skills/learn/`, `skills/note-taker/`,
  `skills/safety-audit/`, `skills/1-by-1/`, `skills/wrap-up/`, and `skills/control/` are
  maintained
  directly in this repository.
- `skills/kien-thai/` and `skills/kode-thai/` are imported from chakrit/kien-thai.
  Follow the upstream ownership and command-target checks in this file.
- `skills/lowfat-pantry/` is imported from chakrit/lowfat-pantry.
- `skills/smoke/` is imported from chakrit/smoke.
- A published skill's folder holds only what agents running the skill need: `SKILL.md`,
  `references/`, and its own templates, scripts and tests. It has no `docs/`; material
  for agents editing the skill goes in this repository's `docs/`. Preserve relative
  references, source attribution, and the root MIT license. README.md is the catalog
  and source record.
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

## Durable artifacts

`docs/` holds this project's durable record.

**`docs/spec/` is authoritative — read the relevant spec before working, and comply.**
It owes no justification: a rule that departs from mainstream practice, from what you
would have picked, or from what you expected is not grounds to escalate, annotate, or
re-open it. If a spec is wrong, raise it with the user and amend the spec.

**Everything settled is a `docs/spec/` amendment** — an instruction you were given, an
approach that was agreed, a library that was picked, a convention or preference that
was fixed. Write it there as it was given: the rule, at the length it was given, with
no note of what it was chosen over and no reason supplied, unless a normal agent would
take the rule for a mistake without one; then give the shortest reason that stops it
from being "fixed" or reopened. A one-sentence rule — "use RESTful routes" — is a
complete entry. There is no decisions log.

File new material by the gate, first match wins: our own design or surface → `spec/`.

**Before writing under `docs/`, read `docs/README.md`, then the destination folder's
`README.md`.** The root file defines the routing gate. The folder file defines its
filing test, filename format, and lifecycle rules. Both are binding.

**`docs/spec/README.md` indexes every spec file — keep it current.** Read the index
before adding a spec file, so you amend the existing doc on a subject instead of
writing a second one. Adding, renaming, or retiring a file updates its row in the same
change.

## Git checkpoints

Commit coherent, completed slices autonomously after completing the checks required for
that work. Do not ask for permission to make a local commit.

Push this repository's current branch to `gh` without asking, once its commits are
complete and their checks pass (chakrit, 2026-11-08: "you have push autonomy for this
repo"). This covers plain pushes only, never a force-push. Merging, releasing, opening
issues or PRs, editing other repositories, and every other change to shared or external
state each still require separate user authorization.

## Merging pull requests

When a pull request is merged, merge it first as it stands, then do any follow-up work
as new commits on top of `main`. Rebase-merge when possible; fall back to another merge
method only when a rebase fails. Reworking the PR branch or replacing the PR with a new
commit hides what the author proposed and what the follow-up changed; separate commits
keep both reviewable. If local `main` has unpushed commits, rebase them onto the merged
`main` before continuing. Each merge still needs chakrit's authorization.
