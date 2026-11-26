# retro skill

Status: implemented

The design of `skills/retro/`, for agents editing that skill. Agents running the skill
never read this file; every rule they follow lives in its `SKILL.md` and
`references/`. chakrit locked in the skill's content on 2026-11-26 ("perrfect, lock in
the skill ocntent please").

## What it is

The user invokes `/retro` manually, every once in a while, when they think the
instructions need adjusting. It reviews an agent's instructions against friction from
real work and proposes targeted edits, including edits that come from higher-level
patterns such as a missing or changed philosophy, without turning every run into a
philosophical session.

It keeps the gist of the style chakrit worked out with `ga42:prod9:internal-tools` on
2026-11-25 and nothing of its implementation in `prod9/tx`: forward work only adds, so
instructions need a periodic look back, and they amend themselves around a fixed anchor
of purpose, philosophy and the user's rulings.

## Construction

1. **Purpose.** Keep an agent's instructions converging on how the user actually wants
   work done, instead of only growing.
2. **Evidence.** Friction observed in real work: corrections, rework, rules ignored or
   colliding. Every finding cites its evidence.
3. **Levels.** Each pattern is explained at the lowest level that fits: rule (one
   instruction wrong or missing), structure (rules collide, sit in the wrong place, or
   pile up), philosophy (a principle is missing or drifted).
4. **Guard.** A pattern rises a level only when repeated evidence cannot be fixed one
   level down. Even then it ends in a targeted edit.
5. **Memory across runs.** Patterns accumulate evidence and carry a status; a killed
   pattern stays killed.
6. **Sanctioned form.** Philosophy entries follow one fixed shape, like the ACE ledger:
   the principle, the user's words, the date. The user owns them; rules stay adaptive.
7. **Recall.** What is settled lands where every session already loads it. Retro's own
   memory is read only by `/retro`. Without this, a retro's output is ignored by later
   sessions.
8. **Output.** Proposals the user rules on. Nothing is applied until the user agrees.

The flow of a run is analyze, think, distill, output; the output may be instruction
edits.

## Locked-in choices

- Evidence comes only from the current session, what the user points to, and the
  ledger's open entries.
- The guard's threshold: two observations from different situations that no
  lower-level edit removes.
- The philosophy section is `## Philosophy` in an always-loaded instruction file; it
  starts with a purpose, and each principle carries the user's quoted words and date.
- The ledger is `docs/retro.md` unless the repository's docs conventions name another
  place; statuses are `observed`, `proposed`, `settled`, `killed`.
- Edits may target the user-level instruction file, with the user's agreement like any
  other edit. Three or more proposals are walked one at a time.

## Testing

A matrix test runs Claude against a few scenarios and checks levels, the guard, memory
across runs, and recall in a fresh session. Codex is out for now (chakrit, 2026-11-26:
"i don't have codex subscriptioin anymore, just focus on claude only for now").

- Scenarios come from chakrit's Claude conversation history; frustration (curse words)
  marks candidate incidents.
- Each scenario is reduced to a small conversation. Long-context recall failures are
  out of scope.
- A scenario's failure is reproduced repeatably on the unfixed instructions before it
  is used to test the skill.
