---
name: retro
description: Review an agent's instruction files against friction from real work and
  propose targeted edits, from a single wrong rule up to a missing or drifted
  principle. TRIGGER only when the user invokes `/retro` or `$retro`, or asks to "run
  a retro on the instructions" or "retro the agent setup". DO NOT TRIGGER for tracing
  one confusion to one instruction, a sprint or team retrospective, code review, or
  routine end-of-session saves.
argument-hint: "[focus area or evidence to look at]"
---

# retro

Print `## retro` as the first line.

`/retro` runs one operation: review the instructions an agent works under, find the
patterns behind friction in recent work, and propose the smallest edits that remove
them. The user rules on every proposal. Nothing changes until they agree.

Forward work only adds instructions. A retro is the look back that cuts, replaces and,
when the evidence demands it, names the principle the instructions are missing.

## Terms

- **Instruction files:** everything that tells the agent how to work and loads in its
  sessions: the user-level instruction file (for example `~/.claude/CLAUDE.md` or
  `~/.codex/AGENTS.md`), the repository's `CLAUDE.md` or `AGENTS.md`, and the skills
  the agent loads.
- **Philosophy section:** a section titled `## Philosophy` in an always-loaded
  instruction file. It holds the purpose and the principles in the fixed form in
  `references/formats.md`. Only the user changes it.
- **Ledger:** the retro's own memory, `docs/retro.md` in the repository, in the format
  in `references/formats.md`. If the repository's docs conventions name another place
  for agent records, use that place. Only `/retro` reads the ledger.

## Phases

1. **Load.** Read the ledger, if it exists, in full. Read every philosophy section and
   every instruction file that loads in this repository's sessions. If the user gave a
   focus, note it; it narrows step 2, not step 1.

2. **Analyze.** Collect observations of friction. Use only these sources:
   - the current session;
   - files, transcripts or messages the user points to in the invocation;
   - `observed` and `proposed` entries in the ledger.

   An observation is one concrete event: the user corrected the agent, work was redone,
   something was built and then cut, a rule was ignored, or two rules pulled opposite
   ways. Write each one as what happened, where (file and line, or the quoted turn),
   and the user's words if there were any. Drop anything you cannot cite.

3. **Think.** Group observations into patterns. For each pattern, find the instruction
   text that produced it: read the text cold, as the agent did, and show how it leads to
   the observed behaviour. Then name the lowest level that explains it:
   - **Rule:** one instruction is wrong, missing or stale.
   - **Structure:** two instructions collide, a rule sits where it never loads, or rules
     have piled up around one subject.
   - **Philosophy:** the purpose or a principle is missing or has drifted, so the agent
     keeps making the same kind of wrong call in different situations.

   Raise a pattern to a higher level only when at least two observations from different
   situations are not removed by any edit at the lower level. With fewer, keep the lower
   level, or record the pattern as `observed` in the ledger and propose nothing for it.
   Check each pattern against `killed` ledger entries and drop it if it matches one.

4. **Distill.** Turn each remaining pattern into one edit:
   - the smallest span that removes the pattern, shown as a diff against the exact lines;
   - cut or replace before adding; keep one recommended path; describe the general shape,
     not the incident;
   - a philosophy edit is one principle in the fixed form, one or two sentences, in the
     philosophy section of the file whose scope matches the pattern (user-level for
     patterns across repositories, the repository file for one repository).

   If no edit removes a pattern because two of the user's requirements truly conflict,
   say so, name the conflict, and name the one relaxation that would allow a fix.

5. **Propose.** Present the patterns ranked by how much friction each caused. For each:
   level, the cited observations, the instruction text at fault, and the diff. Keep the
   whole report short. Walk the proposals one at a time when there are three or more.
   **Wait** for the user's ruling on each.

6. **Apply and record.** Apply only the edits the user agreed to, in the files the diffs
   name. Update the ledger in the same change:
   - an applied edit becomes `settled`, with the user's words, the date and the file it
     landed in;
   - a rejected proposal becomes `killed`, with the user's words;
   - a pattern below the threshold stays `observed`, with its new observations added;
   - add a run line: the date, the focus, and the count of patterns per status.

   Commit when the repository's instructions allow commits.

## Completion

The run is complete when the report has been presented, every proposal has the user's
ruling or is explicitly left open, agreed edits are applied, and the ledger records the
outcome of each pattern and the run line. End with the files changed and, when a commit
was made, its hash.

If the ledger cannot be written (no repository, or the user declines), say that the
run's outcome will not be remembered and give the user the entries to keep elsewhere.
