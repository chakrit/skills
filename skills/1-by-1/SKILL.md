---
name: 1-by-1
description: Walk a list of items, proposals, findings, or options one at a time
  — collect decisions without acting on them, then execute as a batch after
  final confirmation. TRIGGER on "1-by-1", "1-by-1 protocol", "2-by-2", "one at
  a time", "walk these one by one", or when the user explicitly asks for
  sequential per-item review of a list you've presented. ALSO SELF-ENGAGE without
  being asked whenever *you* present a numbered list or table of decisions for the
  user to rule on. DO NOT TRIGGER for single-item decisions or when the user has
  already authorized batch execution in words you can quote.
---

# 1-by-1 Protocol

A forcing function against premature action: walk a list with the user, collect
decisions without acting on them, execute only after final batch confirmation.

## Prepare the list

Finish P1–P3 for every item before presenting the first one. Build each item's context
in a fresh pass, then decide as much of it as that context allows. Some items resolve
outright, some narrow to a smaller question or a confident recommendation, and some still
need the user's full judgment.

- **P1. Enrich each item.** Gather what you would need to decide the item yourself: the
  domain facts it depends on (what the thing is and what it is for), who is affected and
  in what situation, the specs, code, and decisions on record that govern it, and the
  exact decision being asked. Read those sources now. The item's writer often recorded
  it mid-task, with its attention on other work: use its wording as a starting point, not
  as the full picture. An item taken from a report, log, or another agent is a claim to
  re-check, not a question to forward.
- **P2. Decide what the context allows.** An item needs the user only when their answer
  would change the outcome and nothing available settles it. Take one branch:
  - **Answered** — the context, CLAUDE.md laws, stated principles and philosophies,
    repo conventions, decisions on record, or an earlier decision in this list answer
    it. Assume that answer: record it `proposed`, cite what answers it, and do not
    walk or ask about it.
  - **Invalid** — the context shows the question rests on a wrong premise, is moot,
    or is already done. Drop it.
  - **Testable** — a study, experiment, or check you can run would settle it. Run a
    read-only check during P1 and treat the result as under Answered. Otherwise record
    the check `proposed`, naming it, and collect it as a task for step 6; do not walk
    the question.
  - **Narrowed** — the context settles part of the item. Assume that part as under
    Answered, then walk only the remaining question as a true fork.
  - **True fork** — no stated rule or principle points one way, two rules conflict, the
    answer introduces a concept or name the user has not introduced, or the user
    reserved the decision. Note which condition applies and the rule involved. Revise
    the item's framing and recommendation to fit the enriched context, then walk it.
- **P3. Open the walk.** Show one compact block: each assumed item or assumed part as
  one line (item → assumed answer → basis) and each dropped item as one line (item →
  why it no longer applies). Assumed items wait for step 6, where the user can still
  strike them. Then present the first true fork.

## Cycle

1. **Present one true fork** — its context from P1: the situation, what governs it,
   and who is affected. State why you cannot decide it yourself: name the P2 condition
   and the rule that is missing, conflicting, or reserved. Then give the decision
   needed, options if any, and your recommendation. Do not offer "do it now" as an
   option: every collected decision executes at step 6. Stop.
2. **Collect the decision — into the ledger, verbatim, now.** Append the entry
   while the words are on screen: status, provenance, and the user's verbatim
   words for SETTLED/KILLED; record a ruling that amends or releases an earlier
   one as exactly that. Where the repo carries an ACE trail, the ledger is
   `.ace/save.ledger.md` and its format is `dw-save/trail.md` — read that file
   and follow it, including its status set. Elsewhere, keep one ledger file in
   whatever scratch home the repo uses, same fields. The ledger append is the
   protocol's own bookkeeping, not "acting" — beyond it, edit nothing, run
   nothing, touch no other state.
3. **Acknowledge with the walk delta. Stop. Wait.** When a ruling closes the item,
   acknowledge it with what it changes in the list, running P1–P2 again on every
   remaining and newly surfaced item:
   - **Settles:** remaining items the ruling now answers or makes invalid. Record an
     answered item `proposed`, citing the ruling; drop an invalid one. Remove both
     from the walk.
   - **Raises:** new items the ruling opens, and only true forks among them; an
     answered item goes under Settles instead.
   - **Revises:** remaining forks whose framing or recommendation the ruling changes,
     one line each.
   - **Remaining:** a one-line summary of the open forks still to walk, only when
     the rest of the list is not already obvious.
   Only an explicit commit signal ("next", "go", "continue", "ok") advances the
   list. A follow-up question, refinement, tangent, or silence keeps you on the
   current item — the user may want to refine or reverse. Never advance on your
   own readiness.
   Discussion is the normal state of a live item: questions, pushback, and
   thinking aloud record nothing and change no status. Record only when the
   user's words close the item, and advance only on the commit signal — the two
   are separate events and neither implies the other. Words that admit both
   readings → record `needs-disambiguation` and ask the one-liner now.
   A ruling answers only the question its item asked. Words said on a tangent,
   and conclusions you draw from a ruling, are recorded `proposed`, never
   `SETTLED`.
4. **Repeat 1–3** over the remaining forks until none are left.
5. **Summarize.** Say "list complete", recap the collected tasks-to-do. Stop.
6. **Execute on final confirmation.** Default sequential; parallelize only
   when subtasks are large and independent.

## 2-by-2 mode

On "2-by-2": same protocol, two items per round. Pair related items; every
rule applies to the pair as one round.

## Hard rules

- Step 2 touches nothing but the ledger append. Collect, never enact.
- Step 3 never advances without an explicit user commit signal — nothing else,
  ever.
- The protocol persists until the list ends or the user cancels it; mid-list
  topic switches don't end it.
- Pushback or a revision to an earlier decision updates the record — still no
  action until step 6.
