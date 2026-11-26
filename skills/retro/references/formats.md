# retro formats

## Philosophy section

Place it near the top of an always-loaded instruction file, so every session reads it.
Create it only when the user agrees to its first entry.

```markdown
## Philosophy

<Purpose: what this work exists for, in two or three sentences.>

- **<Principle, one sentence in the imperative or as a plain statement.>**
  <Optional second sentence that says where it applies.>
  (<user name>, <yyyy-mm-dd>: "<the user's words that settled it>")
```

- Every principle carries the user's quoted words and the date. A principle without
  them is not settled; keep it in the ledger as `proposed`.
- One principle per bullet. Replace a principle that drifted; do not stack a second
  one beside it.
- Rules that follow from a principle stay in the ordinary sections of the file.

## Ledger

`docs/retro.md` unless the repository's docs conventions name another place.

```markdown
# Retro ledger

Read in full at the start of every `/retro` run. Only `/retro` edits this file.

## Patterns

### <short name of the pattern>

- **Status:** observed | proposed | settled | killed
- **Level:** rule | structure | philosophy
- **Observations:**
  - <yyyy-mm-dd> <what happened>, <where: file:line or quoted turn>, "<user's words>"
- **Instruction at fault:** <file:section>, "<quoted text>"
- **Outcome:** <for settled: file it landed in, user's words, date>
  <for killed: user's words, date>

## Runs

- <yyyy-mm-dd> focus: <focus or "none">; settled N, killed N, observed N, open N
```

- `observed`: below the threshold for its level; carried to the next run.
- `proposed`: presented and left open by the user.
- `settled`: the user agreed and the edit landed. The instruction file now carries the
  rule; the entry stays so later runs can see the history.
- `killed`: the user rejected it. Never propose it again unless the user reopens it.
