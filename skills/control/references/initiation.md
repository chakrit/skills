# Initiate an agent

Brings an existing agent under control: it gets the standing grant and the rule-entry
pointers, so it works from its own instruction file without this skill. If its folder
is not fully set up, the setup for its level runs first.

The procedure is the section "Initiate an agent" in `templates/rules/handling-agents.md`,
which machine setup seeds as engram entry `rule/handling-agents`, so controls run it
without loading this skill. Follow that section from the agent's parent control:
machine control for an org control, the org control for a project control. In any
other session, ask the parent to initiate the agent ("Reach a parent" in
`references/operations.md`) and stop. Its setup check sends you to
`references/setup-org.md` or `references/setup-project.md`; those references fill in
only the missing parts of an existing folder. For an org control, its last step hands
the org control "Plan downstream controls" in `references/operations.md`, which the org
control runs itself.
