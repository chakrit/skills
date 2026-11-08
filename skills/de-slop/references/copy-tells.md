# Copy / prose tells — de-slop catalogue

The words, phrasings, structures, and rhetorical patterns that mark prose as
LLM-generated, each with a fix direction and the sibling tell not to substitute in. Prose
only (marketing, articles, docs, essays) — not code.

Provenance: mostly research-derived. Tags per tell — **Empirical** (measured
word-frequency study), **Curated** (community-codified, e.g. Wikipedia), **Practitioner**
(named editor/writer), **Convergent** (many independent sources agree), **Field**
(shipped-in-anger counts from real audits, like the design catalogue). The load-bearing
empirical anchor is Kobak et al. 2025 (*Science
Advances*): ~280 "excess words" measured across 14M+ PubMed abstracts, a post-2022 spike
larger than COVID's, ~66% verbs, almost none content-bearing.

Severity 1–5 is *diagnostic strength* (5 = screams AI on its own), not how bad the writing
is. No single tell proves AI — the signal is clustering and density (SKILL.md principle
3).

## 1. Vocabulary fingerprints

| Tell                                    | Signal                                                                | Sev | Prov                                                               |
| --------------------------------------- | --------------------------------------------------------------------- | :-: | ------------------------------------------------------------------ |
| **delve / delve into**                  | "Let's delve into…" — the canonical tell                              |  5  | Empirical (excess ratio ≈25, the single most overrepresented verb) |
| **underscore(s)** (verb)                | "This underscores the importance of…"                                 |  4  | Empirical (top-3 excess verb)                                      |
| **showcase / showcasing**               | "showcasing its versatility"                                          |  4  | Empirical                                                          |
| **testament (a testament to)**          | "stands as a testament to…"                                           |  4  | Curated                                                            |
| **boasts** (= "has")                    | "the city boasts a vibrant…"                                          |  4  | Curated                                                            |
| **tapestry** (abstract)                 | "a rich tapestry of cultures"                                         |  4  | Curated                                                            |
| **realm / landscape** (abstract)        | "the evolving landscape of…"                                          |  3  | Convergent                                                         |
| **crucial / pivotal / vital**           | "plays a crucial role"                                                |  4  | Empirical                                                          |
| **intricate / intricacies**             | "the intricate interplay of…"                                         |  3  | Empirical                                                          |
| **meticulous(ly)**                      | "meticulously crafted"                                                |  3  | Curated                                                            |
| **robust / comprehensive**              | filler adjectives, stacked                                            |  3  | Empirical                                                          |
| **unveil / unleash**                    | "unveiling new possibilities"                                         |  3  | Convergent                                                         |
| **garner / foster / bolster / enhance** | Latinate inflation over get/build/improve                             |  3  | Curated                                                            |
| **leverage / utilize / harness**        | "leverage the power of…" — inflation over plain "use"                 |  3  | Curated                                                            |
| **navigate / navigating**               | "navigating the complexities of…"                                     |  3  | Convergent                                                         |
| **Empty intensifiers**                  | "absolutely", "actually", "truly", "really", "simply" padding a claim |  3  | Convergent                                                         |

**Fix:** downgrade to the plain word (*delve into* → *look at*; *boasts* → *has*), or
prefer the concrete noun over the metaphor (*the landscape of X* → *X*). Most improve by
deletion. **Sibling trap:** don't swap one flagged Latinate verb for another ("utilize"
for "leverage") — you moved the tell, not removed it. Same for intensifiers: "absolutely"
→ "definitely" keeps the tell — delete the intensifier or state the evidence that earns
the emphasis. And don't thesaurus-scrub repeats into rarer synonyms: "elegant variation"
(never repeating a word) is itself a documented tell. Repeating a plain word is more human
than varying it.

## 2. Phrasal tics (formulaic openers & connectors)

| Tell                                                 | Example                                                                                             | Sev | Prov                                      |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------- | :-: | ----------------------------------------- |
| **"In today's fast-paced world…"**                   | opener                                                                                              |  5  | Empirical (~107× in detector corpora)     |
| **"It's not just X, it's Y" / negative parallelism** | "not just a tool, a philosophy"                                                                     |  5  | Curated                                   |
| **Contrast as default frame**                        | "Unlike traditional X…", "The difference? …", "It's not about A. It's about B." opening every point |  3  | Convergent                                |
| **"plays a crucial/pivotal role in shaping"**        | claim                                                                                               |  5  | Empirical (~182×, strongest phrasal tell) |
| **"Let's dive into / explore…"**                     | section opener                                                                                      |  4  | Convergent                                |
| **"Navigating the landscape/complexities of…"**      | stacked journey+landscape cliché                                                                    |  4  | Convergent                                |
| **"stands as / serves as a testament to"**           | wrap                                                                                                |  4  | Curated                                   |
| **"aims to explore" / "notable works include"**      | framing                                                                                             |  4  | Empirical (~50× / ~120×)                  |
| **"When it comes to X…" / "At its core…"**           | pseudo-depth pivot                                                                                  |  3  | Convergent                                |
| **"It's important to note that…"**                   | hedge-opener                                                                                        |  3  | Convergent                                |
| **Rhetorical-question pivot**                        | "But here's the thing:", "The result?", "So what does this mean?"                                   |  3  | Convergent                                |
| **"the world of X"**                                 | vague scoping filler                                                                                |  2  | Convergent                                |
| **Throat-clearing announcement**                     | "Here's the thing:", "It turns out", "The uncomfortable truth is"                                   |  4  | Practitioner                              |
| **Emphasis crutches**                                | "Full stop.", "Let that sink in.", "Make no mistake"                                                |  4  | Practitioner                              |
| **Meta-commentary on the piece**                     | "Plot twist:", "The rest of this essay explains…", "As we'll see…"                                  |  3  | Practitioner                              |
| **Rhetorical setup**                                 | "What if [reframe]?", "Think about it:", "And that's okay."                                         |  3  | Practitioner                              |
| **Faux-insight setup**                               | "What nobody tells you", "The part everyone misses"                                                  |  4  | Practitioner                              |
| **Colon reveal**                                     | "The best part: it learns." — dramatic reveal after a noun phrase                                  |  3  | Practitioner                              |

**Fix:** cut the opener, start on the claim — most of these prefix a sentence stronger
without them. For contrast frames, state the thing directly; keep contrast only where the
comparison *is* the point. Throat-clearing, crutches, and setups all delete cleanly — the
sentence after them is the real opening. **Sibling trap:** "dive into" → "explore" →
"unpack" is lateral; all three narrate the act of writing. Stop narrating and make the
point. Same for openers: "Here's the thing:" → "The truth is," is one announcement traded
for another.

## 3. Structural tells

| Tell                                        | Signal                                                                                                                         | Sev | Prov         |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | :-: | ------------ |
| **Rule of three, everywhere**               | triads in nearly every sentence                                                                                                |  4  | Curated      |
| **Uniform paragraph rhythm**                | every paragraph ~3–4 similar-length sentences (low burstiness)                                                                 |  4  | Empirical    |
| **Every section a mini-essay**              | intro → body → tidy wrap, per H2                                                                                               |  3  | Practitioner |
| **Over-signposting**                        | "Firstly… Moreover… In conclusion…"                                                                                            |  3  | Convergent   |
| **Verbatim-clause restatement**             | same crafted phrase (≥5-word run or coined phrase) stamped twice in-page or across a click path                                |  4  | Field        |
| **Sibling-template stamp**                  | same sentence shape in the same slot on sibling pages ("We kept the architecture minimal" / "The architecture stayed minimal") |  3  | Field        |
| **Listicle bloat**                          | bullets where prose would flow; padded to round numbers                                                                        |  3  | Curated      |
| **Inline-header bullets**                   | "• **Header**: sentence" down a list                                                                                           |  3  | Curated      |
| **"Challenges and Future Directions" wrap** | formulaic closing section                                                                                                      |  3  | Curated      |
| **Excessive boldface**                      | multiple bolded phrases per paragraph                                                                                          |  3  | Curated      |
| **Title Case Every Heading**                | all main words capitalized                                                                                                     |  2  | Curated      |
| **Negative listing**                        | "Not a manifesto. Not a roadmap. A promise." — buildup by naming what it isn't                                                 |  3  | Practitioner |
| **Dramatic fragmentation**                  | "[Noun]. That's it. That's the [thing]." / "X. And Y. And Z." — fragments as profundity                                        |  4  | Practitioner |
| **Wh-opener habit**                         | "What makes this hard is…", "Why this matters is…" opening sentence after sentence                                             |  2  | Practitioner |

**Fix:** break the grid — merge some sections, let others be one line; convert padded
lists back to prose; delete visible scaffolding; cut boldface to the one thing that
matters per screen. For restatement, delete the weaker instance — facts, enumerations,
and locked brand phrases repeat freely; it's crafted phrasing that may not. **Sibling
trap:** don't fix uniform paragraphs by making them uniformly *short* — that's a new
uniformity. Burstiness is genuine variance: a 40-word
sentence next to a 4-word one. Don't swap rule-of-three for a mechanical rule-of-two; say
the number of things the point actually has. Negative listing and fragmentation both
resolve the same way: state the final term and delete the runway. For wh-openers, lead
with the subject — "What makes this hard is the migration" becomes "The migration is the
hard part", or better, name what's hard about it.

## 4. Punctuation tells

| Tell                                    | Signal                                                     | Sev | Prov                      |
| --------------------------------------- | ---------------------------------------------------------- | :-: | ------------------------- |
| **Em-dash-as-connector overuse**        | multiple per paragraph, standing in for comma/colon/parens |  4  | Convergent                |
| **Curly quotes in plain-text contexts** | typographic "  '  — where surrounding text is straight     |  4  | Curated (paste artifact)  |
| **Decorative emoji in headers/bullets** | ✅ 🚀 as section marks                                       |  3  | Curated                   |
| **Flawless punctuation uniformity**     | perfectly consistent serial commas/dashes throughout       |  2  | Convergent (humans drift) |

**Fix:** keep the em dash that earns a hard break; convert the rest to
periods/commas/parens *chosen by function*. Normalize curly quotes to the destination's
convention. **Sibling trap (the important one):** replacing every em dash with a semicolon
just makes "semicolon overuse" your signature. It's not which mark — it's variety and fit.
And injecting typos to "look human" is a different artificial signal; aim for natural
variance, not manufactured sloppiness.

## 5. Rhetorical / tonal tells

| Tell                                          | Signal                                                         | Sev | Prov                                   |
| --------------------------------------------- | -------------------------------------------------------------- | :-: | -------------------------------------- |
| **"I hope this helps!" / assistant register** | chatty sign-off, "Great question!", "Feel free to…"            |  5  | Curated                                |
| **Servile positivity / empty enthusiasm**     | everything "exciting / powerful / game-changing"               |  4  | Practitioner                           |
| **Moralizing / tidy wrap-up**                 | "Ultimately, X reminds us that…"                               |  4  | Convergent                             |
| **Significance inflation**                    | "marks a pivotal moment", "leaves an indelible mark"           |  4  | Curated                                |
| **Vague authority**                           | "experts argue…", "studies show…" with no name                 |  4  | Curated                                |
| **Sanded-off specifics**                      | "a leading platform", "various stakeholders"                   |  4  | Practitioner ("blurry generic sketch") |
| **Reflexive hedging / over-qualification**    | "it's worth noting", "generally", stacked on low-stakes claims |  3  | Convergent                             |
| **False balance**                             | "while X has benefits, consider Y" on every point              |  3  | Convergent                             |
| **False agency**                              | "the decision emerges", "the data tells us"                    |  4  | Practitioner                           |
| **Narrator-from-a-distance**                  | "Nobody designed this", "People tend to…"                      |  3  | Practitioner                           |
| **Vague declaratives**                        | "The implications are significant" — never named               |  4  | Practitioner                           |
| **Interpretive metadiscourse**                | "The key point is", "As you can see", "That last part matters" |  3  | Practitioner                           |
| **Weasel attribution**                        | "Experts agree", "Studies show" without a named source         |  4  | Curated                                |
| **Synonym cycling**                           | Rotating clear repeated nouns into agent/assistant/tool         |  3  | Practitioner                           |
| **Fake-strong verb**                          | "serves as a hub" where "tracks" states the action             |  3  | Practitioner                           |

**Fix:** take a position; cut hedges on claims you can stand behind; replace vague
authority with a named source or delete it; kill the moralizing final paragraph (end on
the last real point); restore specifics — names, numbers, dates, the one weird true
detail. For false agency, name the human who acted — "the team shipped it that Friday"
beats "the decision emerges"; where no specific person fits, "you" seats the reader in it.
Replace a vague declarative with the implication it gestured at, or cut the sentence.
**Sibling trap:** don't overcorrect enthusiasm into uniform flatness or contrarian snark —
equally fake. "Studies show" → "research indicates" keeps the tell; the fix is a real
citation or nothing. And hunting false agency by flipping clauses to the passive is the
same evasion in another grammar — the repair is a named actor, not a rearranged sentence.

## 6. Register mismatch

| Tell                                             | Signal                                               | Sev | Prov         |
| ------------------------------------------------ | ---------------------------------------------------- | :-: | ------------ |
| **Corporate-neutral over a personal context**    | LinkedIn polish on a casual note / hobby blog / bio  |  4  | Convergent   |
| **Uniform voice across a whole piece**           | no idiolect, quirks, in-jokes, or roughness anywhere |  3  | Practitioner |
| **Explaining the obvious to the wrong audience** | defining terms the real reader already knows         |  3  | Convergent   |

**Fix:** pin the register to the real audience and relationship, then let voice through —
contractions, an aside, a strong opinion, a specific reference. One genuinely personal
sentence breaks the spell faster than any word swap. **Sibling trap:** "add personality"
prompts produce their own slop — forced folksiness, "Let's be real…", performative
casualness. Voice is specificity and commitment, not a costume.

## Sources

**Empirical (word-frequency studies):**
- Kobak, González-Márquez, Horvát, Lause (2025). *Delving into LLM-assisted writing in
  biomedical publications through excess vocabulary.* Science Advances 11(27).
  https://www.science.org/doi/10.1126/sciadv.adt3813 · preprint
  https://arxiv.org/abs/2406.07016 (DOI 403'd on fetch; figures verified via arXiv HTML +
  secondary coverage — published numbers may differ slightly.)
- Juzek & Ward (2025). *Why Does ChatGPT "Delve" So Much?* COLING 2025.
  https://aclanthology.org/2025.coling-main.426/ — tests the RLHF-annotator-dialect
  hypothesis.
- GPTZero, *Top 10 Most Common Words Used by AI.*
  https://gptzero.me/news/most-common-ai-vocabulary/ — vendor multipliers
  (182×/120×/107×), directionally corroborated, exact figures not independently
  reproducible.

**Curated:**
- Wikipedia, *Signs of AI writing.*
  https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing — the richest single curated
  catalogue (negative parallelism, significance inflation, vague authority, servile
  positivity, formatting tells).

- blader, *humanizer* (MIT, 2025–26).
  https://github.com/blader/humanizer — claim preservation, source-bound rewriting,
  writer-sample precedence, and checks for chatbot residue, false alternatives, and
  unsupported objections. The local skill adopts those boundaries, not its separate
  pattern list or blanket punctuation rules.

**Practitioner:**
- Folta, J. *Here's a handy guide to help you spot AI writing.* Literary Hub.
  https://lithub.com/heres-a-handy-guide-to-help-you-spot-ai-writing/ — "servile
  positivity", the "blurry generic sketch" mechanism.
- Pandya, H. *Stop Slop.* https://github.com/hardikpandya/stop-slop — pattern lists for
  throat-clearing, false agency, narrator-from-a-distance, and vague declaratives. Its
  blanket bans (no em dashes, no adverbs, never three items) are not adopted: SKILL.md
  principle 3 holds that density and uniformity are the signal, never the token.
