---
name: de-slop
description: >-
  Detect and strip the telltale markers of AI-generated work — in website/UI design and in
  written copy — then fix toward genuinely human output. Use whenever the user wants to
  "de-slop", "remove AI tells", make something "not look/sound AI-generated", "humanize"
  text, audit whether a site or document reads as AI slop, or audit repeated em-dashes /
  eyebrow labels / card grids / "delve"-vocabulary, or asks "does this look like
  ChatGPT/AI made it". DO NOT TRIGGER for detecting AI to accuse or grade a third party —
  this is for
  improving your own work.
---

# de-slop

De-slopping is subtraction before addition, then fixing toward a concrete human register —
not toward "unique." AI output is generic because it averages; the fix is specificity and
intentional variance, not synonym-swapping or a fresh coat of mannerisms.

Two catalogues carry the detail; read the one(s) the task touches:

- **`references/design-tells.md`** — website/UI tells (typographic, layout, motion,
  color). Battle-tested from a real de-slop pass.
- **`references/copy-tells.md`** — prose tells (vocabulary, phrasing, structure,
  punctuation).

Load both when the task spans a site *and* its copy.

## The method

Six operating heuristics. They apply to design and prose alike.

1. **Assets human, scaffolding machine.** Separate the artifacts a person actually made
   (bespoke illustration, real photography, a hard-won sentence, a specific anecdote) from
   the template accreted around them. The smell is almost always the scaffolding, not the
   assets. Audit finds the seam; fixes only touch the scaffolding.

2. **A fix must not import a sibling tell.** The loudest trap is replacing one tell with
   another from the same family — middot `·` → em dash `—` is not a fix (both are tells);
   every-em-dash → every-semicolon is just a new uniformity. Check every replacement
   against the catalogue before it ships.

3. **Separate the locked intent from the tell geometry.** When a fix seems to violate a
   constraint you must keep, the constraint usually protects an *intent* while the tell
   lives in a *form*. Keep the intent, kill the form. (A brand's "color accenting" intent
   survives; its "rounded card with icon+title+blurb" geometry dies.) Most apparent
   collisions are between the constraint and the fix's literal form, not its goal.

4. **Fix toward a concrete register, not toward "unique."** Generic de-slopping produces
   new generic. Name the real-world register the work belongs to — a print house (proof
   marks, spec sheets, ink swatches), a field journal, a specific person's voice — and
   pull every fix toward it.

5. **Audit through independent lenses.** Run separate passes — for a site: layout,
   typography, motion, color/imagery; for prose: vocabulary, sentence rhythm, structure,
   stance. Each lens catches the others' blind spots and they converge on the root
   pattern. Rate every finding severity 1–5 (5 = screams AI).

6. **The tells cluster into one compound template, not N independent items.** Fixing the
   template (the repeated section stamp, the reflexive paragraph shape) kills most
   findings at once. Rank by loudness-per-effort. The first phase is usually pure
   *subtraction* — delete mannerisms — which is high-signal and low-risk; earn the
   additive fixes after.

## Content integrity

Preserve every source claim while changing its expression. You may merge, split, shorten,
or reorder sentences when the meaning survives; structure is not sacred, information is.

Never invent a name, number, date, quote, citation, event, or personal detail. If a useful
sentence needs a missing fact, ask for it or write the simpler supported sentence. Fiction
is the exception when invention is the stated task.

Read a supplied writing sample before rewriting. Match its rhythm, word choice,
punctuation, and deliberate quirks; the sample outranks the catalogue's defaults. Without
a sample, choose the register from the artifact: personal and opinion writing may retain
personality, while technical, reference, legal, and factual prose stays plain and neutral.

When editing a file, change prose only. Leave code, data, frontmatter, link targets, and
quoted source text intact unless the user explicitly includes them in the rewrite.

## Workflow

Run the numbered cycle until `Verify` is clean. A clean audit has no unaddressed tell after
the false-positive checks, no integrity failure, and no protected-region change. Do not stop
because one pass found fewer problems than the last.

1. **Protect** — identify the source text, writer sample, and regions excluded from prose
   editing: code, data, frontmatter, link targets, and quoted source text. Preserve every
   source claim and record missing facts instead of filling them.
2. **Audit** — run the passes the *lenses* heuristic defines; log severity and recurrence
   per finding; find the *compound template*.
3. **Rank** — order the findings the way the *compound-template* heuristic ranks fixes.
4. **Subtract** — ship the deletions, honoring the *assets/scaffolding* seam.
5. **Rebuild** — fix the remainder per the *register* heuristic, gating every replacement
   through the *sibling-tell* check.
6. **Verify** — grep for each fixed tell elsewhere (batch fixes miss a few), excluding the
   protected regions; confirm the de-slop artifact itself commits none of the tells. Compare
   the final text with the source for lost claims, invented details, changed links, and a
   register that no longer belongs to the writer or artifact.
   - **Clean:** close the de-slop pass and return the artifact.
   - **Findings remain:** record the new findings and return to **Protect** with the original
     source, current artifact, and protected regions. Re-audit the whole artifact after the
     next rebuild.

## Severity rubric

- **5** — screams AI; present on nearly every instance (eyebrow-on-every-section, card
  grid, "delve"/"it's not just X, it's Y").
- **4** — strong tell, widely recognized (middot/em-dash connectors, symmetric feature
  grids, rule-of-three everywhere).
- **3** — noticeable in aggregate (uniform hover-lift, listicle bloat, emoji icons).
- **1–2** — mild; only reads as a tell alongside others (frozen transitions, Oxford-comma
  uniformity).

## Principles

Every tell is a symptom of one cause: AI writes from the **center of the distribution** —
averaged, predictable, uniform (measurable as low perplexity + low burstiness; the
"decorative not referential" vocabulary is the same thing in words). Humanness lives in
the tails. The method above is how to run a pass without breaking things; these are what
you aim the fixes at — the tails, reached *on purpose and with content*, never by random
jitter or by gaming a detector. Ranked by leverage.

1. **Specificity is the strongest anti-tell.** A real, checkable particular — a name, a
   number, a date, a lived detail the model couldn't have guessed — is off-distribution by
   construction and breaks the spell in one stroke. Surface specifics already present in
   the source or supplied by the writer; never manufacture them. Every vague noun ("a
   leading platform", "various stakeholders") is a place to request a fact or cut the
   claim. If a sentence survives being made specific, keep it; if it evaporates, it was
   filler.

2. **Write from the slopes, not the peak.** Machines pick the expected token. Within the
   writer's register, choose the second-best word when it's truer, the odd-but-right
   collocation, or an existing example that isn't first to mind. Earned unpredictability —
   not randomness.

3. **Density and uniformity are the signal, not any single word.** One em dash, one triad,
   one "delve" is nothing — humans do all three. The tell is *many at once, applied
   mechanically*. Edit to reduce density and break patterns; do not ban tokens or chase a
   word list (it's a lagging indicator — the vocabulary shifts within months).

4. **Burstiness must have a cause.** Vary sentence and section length because the
   *thought* varies, not to hit a metric. A humanizer's random jitter is a second-order
   uniformity a reader still smells. Let a sentence run long because the idea is long; cut
   to three words when it lands.

5. **Cut decorative rigor; keep referential.** "delve / meticulous / underscore /
   testament" gesture at depth and significance without naming anything. Delete them and
   put the specific thing they pointed at — or nothing. Sounding thoughtful and
   demonstrating a thought are opposites here.

6. **Take a stance with a cost when the source and register call for one.** RLHF sands
   text toward agreeable hedging, false balance, and tidy moralizing wrap-ups. In
   personal,
   persuasive, or opinion writing, cut qualifiers on claims the writer can stand behind,
   voice the real preference and the actual "no", and end on the last real point. Keep
   technical, reference, legal, and factual prose neutral.

7. **Preserve the author's edge.** Keep distinctive vocabulary, cadence, humor,
   uncertainty, profanity, digressions, and deliberate roughness when they carry voice.
   Make the minimum effective edit; do not tidy every paragraph into the same shape.

8. **Use the portability and actor tests.** If a sentence could move unchanged to another
   subject, replace it with a fact, mechanism, consequence, or judgment specific to this
   subject. Prefer active voice with a human subject, and name the source behind claims
   such as “experts agree” or “studies show”; if no source exists, record the missing fact
   and write the simpler supported sentence or cut the claim.

9. **Show the point instead of announcing it.** Replace commentary that labels a point
   important, surprising, or subtle with the fact, action, example, or consequence that
   earns that judgment. Replace weak verb phrases with direct verbs when the source
   supports it.

10. **The sibling tell scales.** Heuristic 2 catches element-level swaps; the same trap
   runs at the *aesthetic* scale — fleeing generic-Tailwind into bento / glassmorphism /
   neobrutalism is new slop, not a fix. It's also why humanizers fail: every mechanical
   substitution mints a new signature (or empties the text) instead of adding information.
   Aim for variety and fit, never a different single rule.

11. **De-slop is not anti-detection.** The goal is work that *is* authored, not work that
   dodges a classifier; a passing score is a side effect, never the target. Never treat a
   detector score as proof — see `references/detection.md` for the mechanics (perplexity,
   burstiness, watermarking) and the false-positive evidence.
