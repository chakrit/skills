# retro skill

Status: draft

The design of `skills/retro/` (not yet written), for agents editing that skill. Agents
running the skill never read this file; every rule they follow will live in its
`SKILL.md` and `references/`.

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

## Testing

A matrix test runs Claude and Codex against a few scenarios and checks levels, the
guard, memory across runs, and recall in a fresh session.

- Scenarios come from chakrit's Claude conversation history; frustration (curse words)
  marks candidate incidents.
- Each scenario is reduced to a small conversation. Long-context recall failures are
  out of scope.
- A scenario's failure is reproduced repeatably on the unfixed instructions before it
  is used to test the skill.
