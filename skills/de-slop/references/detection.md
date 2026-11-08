# How AI detection works — and why de-slop isn't evasion

Background for principle 8 ("de-slop is not anti-detection"). Read this to reason about
the signals behind the tells and about false-positive risk — not to game a detector.

## The signals reduce to one thing: too predictable, too uniform

- **Perplexity — the root signal.** How "surprised" a reference model is by each next
  word. LLMs generate by sampling near the high-probability path, so their output is
  inherently low-perplexity — that *is* the tell. Humans reach for the unexpected word,
  the odd construction, the domain term the model wouldn't rank first, spiking perplexity.
  Nearly every other signal is a proxy for this.
- **Burstiness — the variance signal.** Variance of sentence length/complexity across a
  passage. Humans burst: a long winding sentence, then three words. AI holds a
  near-constant level. It's a *second-order* metric (variance of the signal, not the
  signal), which is why humanizers can't easily fake it.
- **Probability curvature (DetectGPT, ICML 2023).** The rigorous form of "low perplexity":
  AI text sits at a *local maximum* of the model's log-probability surface — perturb it
  slightly and log-prob almost always drops; human text moves both ways. The cleanest
  statement of the whole phenomenon: **AI writes from the peak of the distribution; humans
  from its slopes.**
- **Vocabulary distribution & n-gram predictability.** The "delve/underscore/tapestry"
  excess and the connective/hedging tics are the same low-perplexity core showing up in
  word choice.
- **Stylometric over-consistency.** Human writing drifts in voice and cadence; AI is
  eerily uniform. *Too consistent* is itself a tell.
- **Watermarking (SynthID, *Nature* 2024).** Not emergent — deliberately embedded at
  sampling time by biasing token choice. Strong when present, but opt-in (only a
  cooperating model marks its output), strippable by paraphrase, and orthogonal to
  quality. It certifies *provenance*, never *whether the text is good*.

## Reliability: statistical, not forensic

- Only research-grade tools (Pangram, Binoculars) approach low error rates in controlled
  tests; most commercial tools sit ~1% false-positive and free tools (ZeroGPT) throw 20%+
  on verified human text. OpenAI **retired its own classifier** in July 2023 (caught 26%
  of AI, mislabeled 9% of human) — the honest baseline for how hard this is.
- **Load-bearing false-positive caveat.** Detectors disproportionately flag **non-native
  English writers** (a 2023 Stanford study: 61%+ of non-native essays misclassified as AI,
  near-zero for native) — because ESL writing is often lower-perplexity and less bursty.
  Turnitin at ~1% FPR across university-scale volumes means hundreds of false accusations;
  Vanderbilt disabled it in 2023. **Never treat a detector score as proof.**

## Why evasion ≠ de-slop

Humanizers (paraphrasers → structural rebuilders) don't win. The decisive result — DAMAGE
(arXiv:2501.03437, 2025): a humanizer is *itself an LLM*, so it stamps its own model's
fingerprint while erasing the source's — it **substitutes** one distributional signature
for another and adds zero information. Aggressive settings that beat multiple detectors do
so by flattening text into generic, low-information prose — trading the "AI fingerprint"
tell for a "vague and empty" tell. You cannot *hide* the tell, only displace it.

The only move that defeats the root signal is the one a humanizer can't make: **add a
fact, a stance, or a particular the model never had.** That's de-slop. It targets
authorship; evasion targets a meter. Conflating them is the mistake humanizer marketing is
built on.

## Sources

- Mitchell et al., *DetectGPT*, ICML 2023 — https://arxiv.org/abs/2301.11305
- Kobak et al., *Delving into LLM-assisted writing… excess vocabulary*, Science Advances
  2025 — https://arxiv.org/abs/2406.07016
- Dathathri et al., *Scalable watermarking…* (SynthID-Text), Nature 2024 —
  https://www.nature.com/articles/s41586-024-08025-4
- Greenbaum et al., *DAMAGE: Detecting Adversarially Modified AI Generated Text*, 2025 —
  https://arxiv.org/pdf/2501.03437
- Jabarian & Imas, *Artificial Writing and Automated Detection*, BFI/UChicago 2025 —
  https://bfi.uchicago.edu/insights/artificial-writing-and-automated-detection/
- Liang et al. (Stanford), 2023 — GPT detectors biased against non-native English writers.
- GPTZero, *perplexity & burstiness* (vendor; bands are directional) —
  https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
