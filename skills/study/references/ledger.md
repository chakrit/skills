# Study ledger

Keep the decision trail in plain files that survive the chat and agent application.

## 1. Establish the record

Use the repository's work-record location. Without one, use
`study/<study-name>/plan.md` and `study/<study-name>/ledger.md` inside the repository.
Tell the user these paths. Keep drafts in the repository's scratch location, or
`tmp/study/<study-name>/` when none exists.

The plan holds the current state. Append events to the ledger; never erase a ruling
because a later round replaces it. Record the user's words separately from agent
interpretations. Keep settled requirements in the project's authoritative spec when
that convention exists; the ledger retains their source and links to the spec.

Put user-stated working rules in the project's `AGENTS.md` or `CLAUDE.md` in the same
pass. Record the exact rule and its destination in the ledger. Update running builders'
briefs so their next work follows it. Keep these rules within the user's study scope.

Evidence: record paths, scope, and the user's authorization quoted in full.

## 2. Record each transition

Append an event when planning, assigning, integrating, checking, ruling, pausing, or
handing off. Include only fields that describe that event:

```text
## <date/time> · <slug> · <event>
Phase and round: <operation/phase>, <round number>
Instructions read: <selected reference files>
User words: <exact request or ruling; retain all qualifications>
Interpretation: <agent reading, distinct from the quotation>
Branch: <condition and chosen action>
Options: <active letters; references; next unused letter>
Questions: <open IDs; answered IDs; next unused number>
Notes: <active IDs; next unused number>
Work: <owner, allowed paths, worktree, branch, base, commits>
Evidence: <artifact path or command/check result>
Cost: <actual spend, or zero; name unknown costs as unknown>
Next: <next operation, dependency, or blocker and needed answer>
Handoff: <pending/applied; target paths and authorization>
```

Do not invent evidence to fill a field. Record a failed check and its consequence.
Keep open visual questions attached to their next options; their existence does not
block building. Record nonvisual exceptions with the user's justification.
Store lengthy outputs once and link them; quote the decisive result. Use the same
event ID in the plan when a summary needs its source.

Evidence: each changed state has an event with its cause and next action.

## 3. Resume from evidence

Read the plan, latest event for the named preview, and earlier rulings it depends on.
Check that the current files and commits match the record. A mismatch returns work
to the earliest phase that can repair it. Do not infer approval or verification from
an unchecked plan box.

When user input unblocks work, record the answer before continuing that action. At a
handoff, report decisive evidence and the next action in ordinary prose.

Evidence: the resumed branch and prerequisites are recorded before work continues.
