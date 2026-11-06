# Initiate an agent

Brings an existing agent under control: it gets the standing grant and the rule-entry
pointers, so it works from its own instruction file without this skill. If its folder
is not fully set up, the setup for its level runs first.

The procedure is the section "Initiate an agent" in `templates/rules/handling-agents.md`,
which machine setup seeds as engram entry `rule/handling-agents`, so controls run it
without loading this skill. Follow that section. Its setup check sends you to
`references/setup-org.md` or `references/setup-project.md`; those references fill in
only the missing parts of an existing folder.

After initiating an org control, run steps 1–2 of "Plan downstream controls" in
`references/operations.md` for its org folder, and send the approved candidates to the
org control as a task ask ("Give a task"); the org control initiates or sets up each
one itself.
