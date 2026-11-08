# Design tells — web/UI & imagery de-slop catalogue

Catalogue of visual tells that mark a site or UI as AI-generated (v0 / Lovable / Bolt /
generic-Tailwind / shadcn output), each with a fix direction and the sibling tell not to
substitute in. Severity 1–5 (5 = screams AI).

Provenance: the typographic/layout/motion sections are **battle-tested** — derived from a
real de-slop pass on a production site, these fixes shipped. The palette/font/component
and imagery sections are corroborated by practitioners and toolmakers (Anthropic's
frontend-design skill, prg.sh, Rauno Freiberg, Hany Farid/CAI — see Sources).

## Root cause: median of corpus

Every design dimension left unspecified collapses to the training median — purple
gradient, Inter, mid `border-radius`, 0.1 shadow, 200ms `ease`, 3-card grid,
hero→features→testimonial→CTA. (The purple descends literally from Tailwind's 2019
`indigo-500` default → tutorial saturation → training median.) So de-slopping is **making
an explicit choice on every axis the model defaulted** — font, color anchor, radius,
elevation, motion curve, section order, imagery — not decorating the output. Enumerate the
defaulted axes; set each deliberately.

## How to read a fix

"Fix" is the de-slop direction. "Avoid" flags a sibling tell — a replacement from the same
family that just trades one machine mannerism for another. Check every replacement against
this whole catalogue before it ships. The trap runs at the **aesthetic scale** too:
fleeing generic Tailwind into bento / glassmorphism / neobrutalism mints new slop — those
are reflexive swap-ins, not considered choices. Check the replacement *aesthetic*, not
just the replacement element.

## Typographic

- **Eyebrow / kicker label above headings** [5]. Tiny uppercase letter-spaced label
  (letter-spacing ≥ 0.2em, `text-transform: uppercase`, small px, accent color), often
  with a leading hairline rule/dash, over a heading. Worse when bilingual (English kicker
  over a non-English heading). The tell is *ubiquity* — one named kicker is brand voice,
  an eyebrow on every section is AI grammar. Fix: delete it; let the heading carry the
  section, a note-line under it if needed.

- **Italic-serif keyword emphasis in headings** [5]. One word per heading wrapped in
  italic + accent color, applied mechanically to *every* heading. Fix: drop the italic;
  emphasize via weight or a hand-drawn ink/highlighter underline swipe (bespoke SVG), on
  ~⅓ of headings. Avoid: leaving it italic "but smaller"; and note the
  oversized-italic-serif hero (Instrument Serif) is now itself a tell — swapping to the
  fashionable serif re-slops.

- **Inter / Roboto / Geist / Space Grotesk as the whole type system** [4]. One of these as
  body *and* display, no pairing, no display face with character — "the safest answer when
  no typography direction exists." Anthropic's own frontend skill now bans Inter, Roboto,
  Arial, system fonts, and Space Grotesk *by name*. Fix: choose a face that carries a
  feeling; pair a display face with a workhorse body.

- **Gradient text on the entire H1** [4]. `background-clip:text` gradient across the whole
  headline — the v0/Bolt hero default, unreadable and unmistakably generated. Fix: solid
  headline; if any accent, one word only (and check against the italic-serif-accent tell
  above).

- **Native-language brand with an English display hero** [4]. All-caps English headline at
  display size fronting a brand whose actual voice is another language. Fix: lead the hero
  in the brand's language; demote English to a small secondary line.

- **Middot `·` connectors** [4]. Interpunct joining label fragments, taglines, meta,
  signatures — pervasive. Fix: line breaks, wider spacing, real connective words, or one
  consistent delimiter. **Avoid: em dash as the replacement.**

- **Em-dash `—` connectors** [tell in its own right]. Em dash as a connector/aside joiner.
  Fix: separate sentences, a colon, parentheses, or a line break.

- **Micro-caps tracked label system** [4]. The eyebrow treatment copy-pasted into many
  label classes; `uppercase` appears 10+ times. Fix: de-track and de-uppercase;
  sentence-case labels. Falls with the eyebrow.

- **Zero-padded `01/02/03` numbering as decoration** [4]. Sequential 0N counters on things
  that aren't sequences. Fix: remove where nothing is ordered; where order is real,
  restyle as hand-stamped/off-axis marks, not clean CSS badges.

- **Weightless headline copy** [4]. "Build faster. Ship smarter." / "Unleash your
  potential." — rule-of-three, two smart-sounding words, sayable by any product. Fix: a
  line only your product could say — concrete, specific, unswappable. Avoid:
  synonym-swapping the same template ("Accelerate. Simplify.").

## Layout / structure

- **The card** [5]. Uniform rounded-rectangle with fill/border/shadow holding icon(or
  number)+title+blurb, in an equal grid — the single loudest UI tell. Fix, in preference
  order: (a) replace with a domain-native pattern where the content itself is the block (a
  contact sheet where the photo *is* the cell, a spec sheet, a ruled editorial list, a
  numbered filmstrip); (b) if keeping the layout, strip the card chrome (no
  fill/border/radius/shadow) and separate content with hairline rules on the base. Keep
  color as accent marks or full-bleed bands, not card fills.

- **Symmetric `repeat(N,1fr)` feature grids** [4]. Equal-column grids as the default
  primitive; the 3-col circle-number + title + blurb block is the purest instance. Fix:
  break symmetry — one featured oversized cell + a supporting list, off the metronome.

- **The fixed IA stamp** [4]. hero → 3-feature grid → testimonial → logo strip → CTA →
  footer, the same section *kinds* and order regardless of product — the median
  landing-page skeleton. Fix: let the product's real story drive section order; cut
  sections that exist only because the template has them. Avoid: reordering the same
  blocks — remove or replace kinds.

- **Duplicated pasted bands** [4]. A full styled section copy-pasted byte-identical across
  routes. Fix: extract to a component *and* differentiate per placement so it never reads
  twice.

- **Centered-hero formula** [4]. Centered eyebrow + gradient-text headline + one-line
  subhead + two-button CTA (filled + ghost), often over a faint radial glow. Fix: commit
  to an asymmetric or editorial hero that states the actual offer; kill the gradient text
  and the reflexive two-button pair.

- **"Trusted by" logo strip** [3]. A row of muted client / "as seen in" logos under the
  hero, often placeholder or fabricated. Fix: drop if you lack real ones; if real,
  integrate as earned proof (named case, attributed quote), not a decorative belt. Avoid:
  the same logos as a scrolling marquee.

- **Bento grid reflex** [3]. The Apple-style mixed-size rounded-tile mosaic used as the
  default "make it modern" layout. Fix: use only when content genuinely has heterogeneous
  weights. Avoid: bento is itself the swap-in people reach for to escape the 3-card grid.

- **Glassmorphism reflex** [3]. Frosted-blur / translucent panels as a default surface.
  Fix: reserve for true stacking/overlay; otherwise flat. Avoid: neobrutalism as "the"
  anti-AI swing is the next reflexive escape.

- **Default shadcn/ui look** [4]. Gray cards with subtle borders, left sidebar, center
  data table, top-right button group, bottom-corner toast — the app-UI equivalent of the
  purple landing page. Fix: restyle tokens (radius, color, density, type) away from the
  defaults, or diverge structurally.

- **Uniform section vertical rhythm** [3]. Every section the same padding token,
  metronomic. Fix: vary section rhythm intentionally.

## Motion / interaction

- **Blanket fade-up-on-scroll** [4]. The same reveal on every element entering the
  viewport (or, the opposite failure, no coordinated motion at all). Fix: choreograph by
  element role; one intentional signature motion beats a blanket reveal. Avoid: swapping
  fade-up for a blanket slide-in-from-left is the same reflex. (Absence of blanket reveal
  is strong evidence of a human build — motion is choreographed or it's slop.)

- **Uniform lift-on-hover** [3]. `translateY(-Npx)` as the hover for nearly every surface.
  Fix: vary by element role; directional/character motion, not the reflex lift.

- **No easing character** [2–3]. Every transition the same duration on default `ease`, no
  custom cubic-bezier/spring. Craft baseline (Rauno Freiberg): interaction animations
  ≤200ms, scale within ~0.8–0.96 (not 0→1). Fix: give motion a deliberate curve; vary by
  role.

- **Reduced-motion gaps** [2]. `prefers-reduced-motion` honored for some ambient animation
  but not hover transforms / `scroll-behavior`. Fix: complete the coverage.

## Color / surface / iconography

- **Indigo→purple hero gradient** [5]. Blue-to-violet gradient on the hero (often
  as/behind the H1) on white — the single most-named tell. Fix: derive one dominant ink
  from brand meaning; if a gradient survives, make it non-default or drop it for a flat
  committed color. Avoid: purple → teal/emerald gradient is the same reflex, new hue.

- **Timid, evenly-distributed palette** [4]. 4–6 colors at similar saturation, none
  dominant, no anchor ink — "the design equivalent of plain oatmeal." Fix: commit one
  dominant color + 1–2 disciplined accents; keep the canvas restrained so the accent means
  something. Avoid: adding *more* colors to look "designed."

- **Soft shadow + rounded-corner reflex everywhere** [3]. `box-shadow` ~0.1 opacity and a
  uniform mid radius on every surface (the shadcn/Tailwind default). Fix: make radius and
  elevation *mean* something (flat editorial blocks vs. one genuinely-raised surface).
  Avoid: globally setting radius to 0 (neobrutalism) is its own reflex.

- **Solid white / light-gray field, no texture** [3]. Flat `#fff`/`#f9fafb`, zero grain or
  material — the null background, nothing chosen. Fix: intentional surface (grain, tint,
  real material) tied to brand. Avoid: carpeted gradient-mesh + noise blobs.

- **Emoji as UI icons** [3]. Emoji standing in for iconography (👁 ☑ 🗂). Fix: a real inline
  SVG set. (Generic thin-line Lucide/Heroicons on every feature card is the higher end of
  the same reflex — use icons only where they disambiguate.)

- **Pastel cycling by `i % N`** [3]. Card tint by index modulo to fake variety. Fix:
  hand-assign tone by item character.

- **Organic "blob" frames** [2]. `border-radius: 46% 54% …` blobs as hero frames.
  Mitigated when framing real art + grain; consider torn-paper / registration frames.

## Functional slop (below the visual template)

- **Missing states: no validation, error, focus, ARIA** [3]. Forms without
  error/empty/loading states, no keyboard nav, focus rings that ignore `border-radius`.
  The generator shipped the happy-path visual and nothing else. Fix: implement the full
  state matrix. Positive craft counter-set (Rauno): focus via box-shadow (respects
  radius), no font-weight change on hover (prevents layout shift), `@media (hover:hover)`
  so touch doesn't stick hovers, `tabular-nums` in tables, ≥16px inputs to stop iOS zoom.
  *Presence* of these is strong human signal.

## Imagery & media

Two tiers. **Forensic** signals are durable because diffusion models render appearance
with no 3D world model; **slop-look** signals aren't proof but are exactly the "replace
this asset" smell — the higher-value tier for de-slop. The 2023 anatomy heuristics (six
fingers, garbled text, waxy skin) are **largely defeated** on 2025–26 flagship models:
their presence is strong evidence, their absence proves nothing.

Forensic (durable — Hany Farid / Content Authenticity Initiative):
- **Inconsistent shadows / impossible light** [4]. Under one light, object-to-shadow-tip
  lines should converge at a vanishing point; contradictory directions or shadows detached
  from their caster = synthesis. (A real multi-light studio shoot legitimately has several
  directions — the tell is *impossible* geometry, not "more than one shadow.")
- **Reflections that don't correspond** [4]. In mirrors/water/glass/eyewear, points and
  their reflections should meet at a vanishing point; AI reflections show wrong or absent
  scene content.
- **Broken perspective / vanishing points** [4]. Parallel real-world lines (tiles,
  mullions, building edges) must converge consistently; AI bends or fails them — the
  single most reliable current tell. (Deliberate flat/isometric illustration has no
  perspective by design — not a tell.)

Slop-look (practitioner/design-critic — highest value for replace-decisions):
- **Midjourney / diffusion "sheen"** [4]. Glossy, over-smooth, airbrushed, dramatic
  volumetric light, poreless skin, "cinematic" grade regardless of subject. Fix: real
  photography carries incidental imperfection — uneven skin, dull light, boring corners.
  (High-end retouched beauty work is also glossy — the sheen compounds with other tells;
  alone it's weak.)
- **Generic corporate illustration** [4]. The Corporate-Memphis successor: soft 3D
  "clay"/inflated figures, pastel gradients, isometric mini-scenes, gradient-mesh blobs —
  interchangeable across every SaaS site (AI tools ship "Clay"/"3D"/"Gradient" presets
  everyone reaches for). Fix: commission illustration with a point of view, or a
  consistent in-house style.
- **Auto-traced AI vector/icon sets** [3]. AI "SVG" is usually a raster auto-traced to
  vector: bloated irregular paths, nodes off-grid, inconsistent stroke widths within a
  set, members not sharing grid/corner/stroke. Fix: established human-authored systems
  (Lucide, Phosphor, Tabler) or draw on a real grid. Judge sets at the *system* level, not
  glyph by glyph.
- **No brand specificity / stock-interchangeable hero** [3]. A hero that could belong to
  any company in the vertical — diverse team laughing at a laptop, glowing abstract
  network, hands over a globe. Fix: real product/team/workspace photos — mundane and
  specific beats polished and generic, and can't be prompted by a competitor.

Detection tooling (weak — treat as priors, never verdicts): provenance (C2PA Content
Credentials, Google SynthID) confirms *positively* only — absence proves nothing (metadata
stripped on re-encode; SynthID only marks Google-tool output). Third-party image detectors
are unreliable — NewsGuard 2026 found 3 of 5 leading tools misclassified real news photos
(worst flagged 40% of authentic images as AI). Never accuse a real photo on a detector
score.

## Anti-tells (preserve — evidence of a human build)

Bespoke illustration; real product/review photography; film grain; hand-authored on-brand
SVG; a real embedded map; a de-tuned palette (not one uniform saturation); no decorative
gradients/orbs; the *absence* of blanket scroll-reveal and uniform hover-lift; and craft
micro-decisions (focus rings that respect radius, no hover-weight layout shift,
`hover:hover` gating, tabular numerals, full form-state coverage). When audit finds these,
they are the assets — fixes touch the scaffolding around them, never these.

## Sources

- Anthropic frontend-design skill (`anthropics/skills`) — Prithvi Rajasekaran & Alexander
  Bricken, Oct 2025. Toolmaker/primary source (277k+ installs); bans
  Inter/Roboto/Arial/system/ Space Grotesk + purple-on-white by name.
- prg.sh, *Why Your AI Keeps Building the Same Purple Gradient Website*, Oct 26 2025 —
  https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website
  (median-of-corpus mechanism).
- 925studios — *AI-slop web design guide* / *AI slop design tells*, 2026.
  https://www.925studios.co/blog/ai-slop-web-design-guide
- Impeccable — *Slop* guide. https://impeccable.style/slop/
- Rauno Freiberg (design engineer, Vercel), `raunofreiberg/interfaces` —
  https://github.com/raunofreiberg/interfaces (craft baseline: motion ≤200ms, focus,
  hover, tabular-nums).
- Hallmark — Ramsis Hammadi, May 2025.
  https://dev.to/rams901/hallmark-stop-ai-generated-ui-slop-in-one-command-in-2026-3p9n
  (65 deterministic detection gates; "predictable IA" as a first-class gate).
- Hany Farid / Content Authenticity Initiative — *Photo forensics from lighting shadows
  and reflections* / *for AI-generated faces*.
  https://contentauthenticity.org/blog/photo-forensics-from-lighting-shadows-and-reflections
- NewsGuard, 2026 — *Leading AI Image Detection Tools Mislead Online Users.*
  https://www.newsguardtech.com/special-reports/leading-ai-image-detection-tools-mislead-online-users-often-declaring-authentic-content-fake/
