# Initiate an agent

Brings an existing agent under control: it gets the standing grant and the rule-entry
pointers, so it works from its own instruction file without this skill. In a team repo
(a single-repo project's folder cloned from a remote) with engram, the grant goes to
engram and the instruction file keeps only a marker pointing to it. If its folder is
not fully set up, the setup for its level runs first.

The procedure is the section "Initiate an agent" in `templates/rules/handling-agents.md`,
which machine setup seeds as engram entry `rule/handling-agents`, so controls run it
without loading this skill. Follow that section. Its setup check sends you to
`references/setup-org.md` or `references/setup-project.md`; those put the folder in
place without editing existing files, then return you to initiation, where the agent
takes over its files. For an org control, its last step hands
the org control "Plan downstream controls" in `references/operations.md`, which the org
control runs itself.
