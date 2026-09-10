# Worked Examples

Illustrative end-to-end runs of both modes, using placeholder subjects so they don't age.
They show the *shape* of a finished check — field structure, citation discipline, and how
confidence is calibrated to evidence, not to suspicion. Real runs cite live URLs (see
`SKILL.md` §5); sources here are shown as types for illustration.

## News / claim mode

**Input.** "Country X's exports to Country Y jumped 40% last quarter — proof the new trade
deal is working." (Loaded framing: it embeds a conclusion. Restate neutrally before
checking — see "Answer the claim, not the framing".)

**Restated claim.** Country X's goods exports to Country Y rose ~40% quarter-on-quarter in
the most recent quarter.

**Check.**
- Primary: Country X's national customs portal — reports +38% QoQ in local currency.
- Cross-check (proxy): Country Y's customs *mirror* data (its reported imports from X) —
  shows +22%, not ~40%.
- Currency effect: X's currency fell ~12% against Y's over the quarter, inflating the
  local-currency figure; in USD the rise is ~24%.
- Coverage: two trade outlets repeat "40%", but both trace to X's government press release
  (circular, single origin).

**Verdict (format per `SKILL.md` §5):**
- **Claim** — X's exports to Y rose ~40% QoQ last quarter.
- **Confidence** — Moderate.
- **Verdict** — Likely True that exports rose, but the *magnitude is overstated*.
- **Data check** — Primary customs +38% local-currency; partner mirror data +22%;
  currency-adjusted ~24%. The headline 40% is the least independence-checked figure.
- **Sources** — X customs (Official/Primary); Y customs mirror (Official/Primary, and
  independent of X); 2 trade outlets (Trade tier, but circular to X's release). 2 tiers,
  yet the corroboration for "40%" is single-origin.
- **Key corroboration** — Both customs bodies agree exports rose materially.
- **Key discrepancies** — Magnitude: 22–24% vs the claimed 40%; the gap is currency plus a
  single-sourced headline.
- **Official vs independent** — X's own figure runs ahead of the partner-mirror
  cross-check — the classic tell to downweight a sole-source official number.
- **Caveats** — "Proof the deal is working" is causal framing the data doesn't establish;
  the rise may predate the deal or have other causes.

Why not "High": the rise is real and primary-sourced, but the headline magnitude fails the
mirror cross-check and the causal claim is unsupported. The evidence supports a
*qualified* verdict, not the framing's.

## Review / recommendation mode

**Input.** "Find me reviews showing the Brand Z earbuds are great." (Loaded — answer the
product's actual standing, not the requested conclusion.)

**Restated question.** What is the authentic consensus on Brand Z earbuds?

**Check (trust inverted — see `references/reviews.md`):**
- Rejected as evidence: Brand Z's site ("most trusted audio brand" — self-label, zero
  weight) and three affiliate "best earbuds 2026" listicles all routing to one checkout.
- Weighted: an independent teardown lab with disclosed methodology; a 600-comment
  subreddit thread; long-term-use reports at 6–12 months.
- Manipulation signals: a burst of 200 five-star reviews in three days, generic praise
  ("great sound, fast shipping"), default avatars — downweight that body.

**Verdict (format per `references/reviews.md`):**
- **Subject** — Brand Z earbuds.
- **Consensus** — Polarized.
- **Confidence** — Moderate (good vendor-uncontrolled volume, but recent astroturfing
  muddies the signal).
- **What users consistently praise** — sound quality for the price; comfort.
- **What users consistently criticize** — connection dropouts after ~6 months; poor
  warranty support.
- **Vendor claims vs independent reality** — "industry-leading battery" not reproduced in
  the independent teardown (measured ~15% below spec).
- **Manipulation signals seen** — review burst, generic uniform praise,
  affiliate-saturated search results, on-site self-labels.
- **Caveats** — the long-term-failure pattern is recent; pre-2025 reviews may not reflect
  current units.

One detailed independent teardown plus a long dissenting forum thread outweigh the
200-review five-star burst.
