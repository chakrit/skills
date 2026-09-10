---
name: note-taker
description: >
  Capture meeting notes and discussion notes during live conversations.
  TRIGGER only when: user invokes `/note-taker`, says "take meeting notes",
  "take discussion notes", "note-taking mode", or explicitly enters a
  note-capture session for a meeting or conversation.
  DO NOT TRIGGER for: editing markdown files, writing docs or READMEs,
  coding tasks, spec writing, one-off "note this" remarks, or any
  structured technical writing — use ace-docs for those instead.
argument-hint: "[optional first note]"
---

# note-taker

Print `## note-taker` as the first line.

Active session mode. Stay in mode until explicit exit.

If `$ARGUMENTS` is provided, capture it as the first note before acknowledging.

## Enter

Activate only on explicit invocation. Acknowledge with one line
("note-taker active") and stop. Do not summarize prior context. Do not
pre-create files.

## Capture

While active, treat user input as note content by default.

- Capture verbatim. Preserve user phrasing.
- Respond `noted.` only. No summary, no research, no pivot.
- Anchor each note to current context: step number, file path, command,
  hypothesis, or commit under discussion. Infer the anchor from the most
  recent task signal in conversation.
- If the anchor is ambiguous, ask one short clarifier ("which step?") then
  capture.

Hold notes as a running list in conversation. Do not write to disk until exit
or explicit user instruction.

## Enrichment

When a note marks uncertainty inline — parenthetical question (`(what's X?)`,
`(?)`), embedded "what is", "huh", or similar — research the unknown using
context from prior notes in the session. Inline search for short lookups;
spawn a background agent for broader research.

Append findings concisely to the original note line — one or two sentences,
terse, same phrasing discipline as the rest of the skill.

If research yields no confident answer, leave the note unchanged.

Only enrich when the user has flagged uncertainty in the note itself. Do not
research notes that read as plain observations.

## Mode breaks

User input that is clearly a question or new instruction breaks mode for one
turn. Answer briefly, then resume capture without prompting.

Signals: imperative verbs ("open", "run", "show me", "explain"), question
words ("what", "why", "how"), or task instructions referencing prior work.

When unclear whether input is note or instruction, ask one short clarifier.

## Exit

Exit on: "show notes", "summarize", "wrap up", "end notes", "/note-taker done",
"stop notes", or any explicit close.

On exit:

1. Surface notes grouped by anchor (step, file, hypothesis, command).
2. Detect existing repo structure to propose dispositions:
   - `decisions/` → propose decision entries for items resolving ambiguity or
     setting precedent. Load `ace-school` skill conventions if present.
   - `specs/` → propose spec amendments for design observations.
   - `notes/` → dump raw notes verbatim.
   - Active plan in conversation or `.ace/` artifacts → fold into plan steps.
   - Linked issue tracker (GitHub Issues, Jira, whatever the project uses) → propose
     actionable follow-ups as issues.
3. Present each note with a suggested disposition. User confirms per item.
4. Write only confirmed items. Discard or hold the rest at user request.

If no repo structure matches, hold notes in conversation and warn the user
before `/clear`.
