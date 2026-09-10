# Reasoning About Hard Data

Read this when a claim has a quantitative or record-based backbone. For *where* to find
the primary source per beat, see `references/source-registers.md`; this file covers the
harder half — how to reason about a number once you have it, and how to cross-check an
official figure you can't take on faith. The goal throughout: reach a number or record
whose publisher is accountable for it — audited, penalty-bearing, or methodologically
transparent — and confirm you're reading the primary publisher, not an aggregator
restating it.

## Reasoning about the number
Finding the primary figure is half the job; a real, accurately-reported number is
routinely used to support a false claim. Before accepting that a number proves the claim,
run these:

**What's actually counted**
- **Count or rate?** A raw count is meaningless without its denominator — per how many,
  over what period? Demand the rate.
- **Base rate.** A subgroup's share of an outcome reflects its share of the population.
  ("Most who caught it were vaccinated" is expected when most people are vaccinated.)
- **Absolute vs relative.** "Doubles the risk" can mean 1-in-a-million → 2-in-a-million.
  Relative change inflates; insist on the absolutes too.
- **Same definition?** When a figure moves, check whether the world changed or the
  *definition/methodology* did (who counts as unemployed, what counts as a "case").

**Whether the data was cherry-picked**
- **Time window.** A start point at a local min or max manufactures a trend. Test
  sensitivity to the baseline; read the full series, not the framed slice.
- **Sampling.** Who's in the data — self-selected, convenience, survivors-only? Online
  polls and "verified buyers" aren't the population. Watch survivorship.
- **Aggregation.** An aggregate trend can reverse inside every subgroup (Simpson's
  paradox); a mean can hide a skewed distribution — prefer the median and the spread.

**Whether the inference holds**
- **Correlation is not causation.** Check for confounders, reverse causation, and common
  causes before accepting a causal claim built on a correlation.

**Whether the number itself is sound**
- **Trace it to origin.** Follow "studies show" and oft-repeated figures back to source —
  many trace to a single advocacy estimate or to nothing. Beware circular sourcing.
- **Sanity-check magnitude.** Does it survive a rough order-of-magnitude and unit check?
  False precision ("73.6%") from a soft method is a tell, not a virtue.

## Cross-checking official figures with independent proxies
When the only direct source is an official figure whose independence you can't verify (see
"Calibrate to evidence" in `SKILL.md`), don't treat it as unfalsifiable — test it against
proxies the publisher doesn't control:
- **Output / GDP** — satellite nighttime-lights intensity; authoritarian growth figures
  tend to run ahead of what the lights imply.
- **Inflation** — independent price-basket indices against official CPI.
- **Death tolls** — excess mortality (all-cause deaths vs the historical baseline) against
  official counts, for pandemics and conflicts alike.
- **Trade** — mirror statistics: a country's reported exports vs its partners' reported
  imports; large gaps flag mis-reporting.
- **Activity** — shipping, electricity use, and job postings as a check on official
  economic claims.
When proxy and official diverge, that gap is itself the finding — report it.
