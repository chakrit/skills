# Andy Clarke design model: working synthesis

Turns the stream notes into a design model for AppBaoBao; the general model drawn from
it is this skill's `SKILL.md`. Each point cites the stream note it rests on (`talks`,
`accounts`, `idd`, `own`, `clients`, all in `notes/` beside this file), so detail can be
recovered from there.

All five streams read in full: `accounts`, `talks`, `idd`, `clients`, `own`. `own`
includes the free 28-page sample of *Standout Designs for the Web* that he published
himself, so it is a public source; the paid book and its Client Interview Guide are not.
`clients` §0 holds a per-client table (26 clients: trade → concept source → what it
became), the single most useful artefact for our use case.
Per-issue and per-demo detail behind `idd` is in `digests/idd-digest-A.md` to
`idd-digest-E.md`. Screenshots cited as `shots/...` are local only, in
`tmp/andy-clarke/shots/` (trust the `v`/`h`/`-top` first-screen shots; the tall ones
exaggerate `vh` space).

## 0. The problem in one paragraph

An AI-made small-business site is assembled from known parts: centred hero, three
feature cards, testimonials, CTA band, one 12-column grid with equal gutters, stock or
generated photos, one sans-serif, the same rhythm in every section. Each part is
reasonable; the sum has no idea in it, so it says nothing about *this* business. Clarke's
whole body of work attacks this from one direction: **find what the content means, then
make the design carry that meaning**. Variation in layout is a consequence of having an
idea, not a goal in itself. Random asymmetry without an idea reads as random (talks 1.1).

## 1. What Clarke's work actually rests on (thinking, before any layout)

Ordered as he works. This is the part a generic generator lacks, and the part to
encode most carefully.

1. **Find the meaning first.** Art direction is distilling "an essential, precise
   meaning or purpose" from content and conveying it better through design (talks §2).
   For a business: what does it mean in people's lives, beyond the facts?
2. **One truism, one line.** List truths about the business, cut to the one that is
   uniquely theirs and hard to argue with, write a line from it. This happens before
   layout and is part of art direction, not copywriting after the fact (talks 1.17).
   Copy comes before design; he writes placeholder copy himself rather than design
   against lorem ipsum (accounts §2).
3. **Single-word principles.** Agree three or four single words ("bold, clear,
   intentional, reassuring"), then collect references for what each word means to this
   client; the words turn into concrete visual and behavioural choices ("reassuring" →
   warm neutrals and pulsing placeholders) (talks §2). Stephen Hay's funnel: values →
   moods and metaphors → concept → visual language → design.
4. **One concept that dramatises the real promise.** Not "show the product" but a
   metaphor that carries what they actually sell: Codeboxx printheads → famous
   paintings rebuilt from QR-code textures ("keeping production lines moving is an
   art"); EPD property → skylines drawn only from the logo's circles; Lockrose energy →
   one mid-century-magazine-cover landscape (accounts 1.1, talks 1.13). The concept came
   from the content audit and from reframing the problem ("the problem was trust, not
   organisation").
5. **Borrow from outside the web, by principle, not pastiche.** Print magazines (Brody's
   *The Face*, Brodovitch's *Harper's Bazaar*), comics (*Watchmen*, McCloud), record
   sleeves (Steinweiss), cartoons (Hanna-Barbera), advertising (Boddingtons, Guinness),
   posters. Understand *why* the source works, then translate the principle (talks §2).
   **His concrete practice is one reference per design**: take one print piece, name its
   two to four "distinctive design threads", keep its skeleton (band, beam, giant
   letter, horizon, cascade, mosaic) nearly intact, swap in the client's subject. He
   never blends sources in one design (idd C8, §2). His control experiment proves the
   point: the same Vespa copy art-directed five ways, the same DS three ways; the
   content stays fixed and the reference supplies the concept. **This is the most
   directly transferable procedure in the whole corpus** and the natural engine for
   giving each client a different site: a library of references, each reduced to its
   threads, chosen per client.
5a. **Mundane subjects can be made glamorous.** The Trabant, "the worst car ever made",
   is the point of the Huber issue (idd §2). Small-business subjects (a noodle shop, a
   laundry, a printer) are exactly this case.
6. **Turn constraints into style.** No budget for animation → Hanna-Barbera's cheap
   limited-animation tricks become the look (accounts 1.2, talks 1.14).
7. **Structure in black and white, colour late, decoration last.** Typographic and
   layout structure are "the same thing"; texture and decoration are the most
   negotiable layer (accounts 1.4).
8. **Judge by feeling, after living with it.** Feedback in feeling words ("doesn't feel
   like us"); leave the design open overnight, judge it fresh (accounts 1.4, talks §2).
9. **Keep familiar mechanics familiar.** Pricing tables, CTAs and mental models stay
   conventional; everything brand-facing is reinvented (accounts 1.6, talks §3 values).

## 1b. Where the per-client concept comes from (the engine)

From 26 client sites (clients §0, 1.1–1.5), the concept always comes from one of five
mines. All are available for a Thai small business in a single intake conversation.

| Mine                                                             | Question to ask                                                   | His examples (clients §0)                                                                                                      |
|------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| A. What the client already owns                                  | What logo, card, cover, sign, name, place do you have?            | Lockrose triangle → all art; village names → hero tower; business card → orange column; dentist surname → toothpaste-tube logo |
| B. The detail the owner keeps returning to                       | What do you love, read, collect, keep mentioning?                 | tape machines → audio players; Asimov → SF paperbacks; Saul Bass → poster pages; "it's an art" → QR paintings                  |
| C. What the customer really buys                                 | What do people buy from you, one level above the product?         | trust not property (no buildings shown); belonging not videos; "building confidence" in every heading; movement not planning   |
| D. The trade's own mechanics, taken literally                    | What does your product physically do? Say your tagline literally. | printers print codes → paintings from QR; "sound of your world" → world that plays sounds; a duck → duck machines              |
| E. A field outside the sector that already made people feel this | Who else made people feel what you need them to feel?             | protest and gig posters for youth politics; Graphis covers; Cubism/De Stijl for balance; '90s cartoons                         |

Working rules he states or shows:

- **Listen for repetition.** The concept is what the client keeps coming back to, not
  what the designer likes (clients 1.1).
- **Competitors are studied only to find clichés to avoid**; he rarely researches the
  sector (clients 1.4, 3b; accounts 1.6).
- **One test question per project**, from mine C: "Does this make Portico feel more
  trustworthy?" Every decision must pass it (clients 1.3).
- **The concept also decides what not to show**: no buildings for property, no people
  when the team refused photos, no product shots for printheads (clients 1.11).
- **Translate qualities, not surfaces**: from Saul Bass take confidence, simplicity,
  economy, not his shapes (clients 1.4).
- **Mundane trades are the best briefs**: "there are stories to tell about every
  business" (clients §3).

Small-business pattern across his local clients (clients 3a): the name or trade object
becomes the mark; illustration replaces stock in a style fitted to the client; two or
three colours, often on a dark ground, photos duotoned into the palette; type as image
(rotated slogans, name towers, the phone number as display type, giant numerals); **an
asymmetric main column plus a narrow utility rail** (hours, phone, treatments) instead
of equal three-card rows; a small visitor toy (palette switcher, hidden theme); jobs of
two weeks to a month.

## 1a. The stance that keeps this from becoming a new cliché (own 13, 6, 5)

The most important nuance in the corpus, stated in his newest public writing:

- **Familiar patterns are not the enemy; unchosen ones are.** "There's nothing
  inherently boring about a twelve-column grid, a hero banner, a row of cards"; the
  problem is choosing them "simply because they're familiar". "Even a conventional grid
  can feel distinctive when it's used with intent" (own 13).
- **Proof:** in his unsolicited redesigns he keeps the client's grid, typeface, colours
  and content (Labour: 12 columns, Poppins, the existing icons) and still makes it
  distinctive. Distinctiveness comes from **hierarchy, scale, crop, type and
  composition decisions**, not exotic components (own 13).
- **So the model must not become a checklist of "weird" moves.** Every move needs a
  reason tied to the client's concept. A model that always reaches for compound grids
  and rotation would only produce a new, recognisable house style.
- **Symmetry and asymmetry carry meaning** (own 5): symmetry reads stable and
  reassuring, asymmetry energetic and opinionated; a steep type hierarchy reads
  unapologetic, a shallow one calm. **Ask per client: reassuring (clinic, accountant)
  or energetic (street food, gym)?** Parent grids have personalities too: 3 columns
  editorial and informal, 4 tighter and serious, 5 rare and tense; mixing 4 and 5 lets
  one section feel tense and the next settled (the RSPCA puppy: sad story on 5, happy
  ending on 4).
- **Not every page needs art direction**; some only need better typography (own §2).
  "When everything is loud, nothing gets heard" (own 8).

## 1c. Where the art direction sits on the page (concentration)

A finding that changes how we build (clients 1.10, 1.15, 3a):

- **The concept is concentrated, not spread.** It lives in the first screen, one or two
  signature controls skinned in the concept's materials (tape-deck track keys, a
  ketchup-bottle form, a stone-tablet menu; clients 1.7), the section headings, and
  type as image. Below the hero, Codeboxx, Lockrose, Mountain Duck and Portico settle
  into ordinary rows and FAQs. **One strong moment plus consistent details, not every
  section reinvented.** This contrasts with idd, where every page is a showpiece; for
  client sites, client practice wins.
- **On phones the one signature element always survives** (reel, bracelet, character,
  name tower), reordered or re-set: Llanasa re-sets its tower as two justified columns.
  Secondary ornaments (arrows, word columns, extra interactions) are cut (clients 1.15).
  Confirms the phone rule in §5.
- **The art direction lives in bespoke assets, not the grid.** Neurodiverse Training's
  site, rebuilt on another platform without his assets, fell straight back to the
  textbook AI default (centred hero, gradient word, logo strip, equal cards; clients 3a).
  **For AppBaoBao: the per-client concept assets (mark, illustration set, type lockups,
  palette with roles) are the product, and they must be first-class, stored, and reused
  by the system, not one-off decoration.**
- **Keep familiar controls usable**: "buttons still needed to look clickable", but a
  generic rounded button "would have felt imported from another website" (clients 1.7).

## 1d. My own read of key screenshots (spot checks)

Looked at directly, to check the streams' claims and draw my own conclusions:

- **Llanasa Council** (`shots/clients/sb-llanasa-council-live-1400.png`): the grid is
  just two halves split by a thin orange vertical rule. All the distinction comes from
  (a) the left half being one type object, the 13 village names width-fitted in two
  alternating golds under the wreath, and (b) **practical information set as display
  type**: "Next meeting / 19:15 / Tuesday" is poster-sized. A plain grid, a dark ground,
  two colours and a serif. **Utility info as display type (opening hours, the phone
  number, the next date) is the most portable small-business move in the corpus**, and
  it costs nothing.
- **Tristan Jakob-Hoff** (`tristan-jakob-hoff-1400.png`): the navigation *is* the hero
  lockup, a narrow column of mixed-weight condensed caps top left. The rest of the first
  screen is empty red paper; a cut-out portrait with a torn white outline sits bottom
  right with two bars shooting toward it. The reading path is a diagonal from small
  dense type to large image. **Emptiness is the main material; the menu doubles as
  typography.**
- **Abergele Dental** (`sb-abergele-dental-live-1400.png`, partly covered by a modal):
  centre illustration of the family, rotated script "Love your smile" overlapping its
  bottom edge, a right rail of hours, the phone number in display numerals, a quote and
  the treatments list. Confirms the main column plus utility rail pattern.
- **Demo 37** (`shots/idd/demo37v-1400.png`): a whole grid of mixed lockups (letter
  block, spaced small caps, condensed name, rules) rotated as one unit inside a thick
  asymmetric frame. Each item is a different lockup; together they read as one poster.
- **His 2022 site at 390** (`shots/own/wb-2022-390.png`): the gorilla-and-headline hero
  is one composed image that scales as a unit; then "25 YEARS' WEB DESIGN EXPERIENCE. NO
  JOKE" becomes a full-width four-line display block bigger than anything on the desktop
  page. **On the phone the scale contrast increases, not decreases.** Confirms the phone
  rule.

## 2. Structural moves (layout and composition)

Each is the replacement for a specific default. All need an idea behind them.

| Move                                                                                      | Replaces                                   | Source       |
|-------------------------------------------------------------------------------------------|--------------------------------------------|--------------|
| Compound grid (e.g. 6 over 4 → `3fr 1fr 2fr 2fr 1fr 3fr`)                                 | one equal 12-col grid                      | talks 1.1    |
| Skinny column kept mostly empty                                                           | symmetric layout, full-width bands         | talks 1.2    |
| Column widths from ratios (golden, √2, Fibonacci); odd column counts                      | guessed 8/4 splits                         | talks 1.3    |
| Modular grid fixes image formats, captions as composed elements                           | grey caption under photo                   | talks 1.4    |
| Each section its own composition, chosen for its story beat                               | every band the same layout                 | talks 1.6    |
| Panel size = dwell time; borderless and edge-bleed = emphasis                             | size by content amount; boxes for emphasis | talks 1.7    |
| Headline as a composed object (stacked, off-edge, placed after a prologue)                | headline on top, centred                   | talks 1.8    |
| Standfirst, pull quote, drop cap as layout tools                                          | default typographic hierarchy              | talks 1.9    |
| Text shaped by the picture: V, Z, diagonal, staggered margins, rotated composition        | text block beside image                    | talks 1.10   |
| Overlap and depth in one grid cell, blend modes                                           | flat side-by-side cells                    | talks 1.11   |
| Elements breaking out of the grid                                                         | everything inside its row                  | accounts 1.3 |
| Even grid, deliberate large holes (a whole column or a quarter left empty)                | every track filled, centred                | idd G3       |
| One odd track: skinny column, `6rem` headline column, margin tracks in the grid           | blocks on 1–4 of 12 equal columns          | idd G1       |
| Staircase starts: headline, standfirst, body each on a different line                     | one flush left edge                        | idd G4       |
| Offset gutters: images on halves, text on thirds                                          | image and text sharing gutters (card look) | idd G5       |
| Modular grid with unequal zones and visible rules; pacing by module size                  | uniform card grid; the three-card row      | idd G6       |
| Visual order ≠ document order; header/footer anywhere                                     | header top, footer bottom                  | idd G7       |
| Text takes the picture's outline                                                          | image box beside rectangular text          | idd C1       |
| One big structural shape instead of a hero (slab, beam, giant mark, letter mask, horizon) | photo hero, centred headline, button       | idd C2       |
| Rotate a whole group, never singles; diagonals from empty modules                         | everything orthogonal                      | idd C3       |
| Bleed and crop until abstract; whole view elsewhere                                       | whole product centred with padding         | idd C4       |
| Scale contrast, always relative (giant against tiny)                                      | gentle type scale, medium images           | idd C5       |
| Mirror or invert two halves across a seam                                                 | zig-zag image-left/right rows              | idd C6       |
| Overprint flat hues so overlaps make a third colour                                       | drop shadows, glassy cards                 | idd C7       |
| Captions beside images, rules, thick asymmetric frames                                    | caption under image, shadowed cards        | idd C9       |

Additional moves from `own`:

| Move                                                                                                                                   | Replaces                                            | Source |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--------|
| Dethrone the hero banner: put the key message or proof in that space, narrow the image, or fuse image and message into one composition | full-width banner as filler ("an invasive species") | own 6  |
| The page becomes a printed object from the client's world (magazine cover, teen magazine, pulp cover, title card, tabloid)             | a neutral page that could be anyone's               | own 7  |
| Numerals and data as display type, with brand pictograms instead of charts                                                             | the four-tile stats strip                           | own 9  |
| Extreme crops (to the eyes), growing image sequences, cut-outs standing in front of type                                               | medium photo in a card                              | own 10 |
| One personality thread, many looks: each page its own layout, stitched by palette, type, grid, mascot                                  | one template repeated                               | own 11 |
| Varied lockups for parallel items (badge numeral, script phrase, condensed stack)                                                      | four identical icon-title-text cards                | own 8  |
| Designed panels in each item's own colours instead of screenshots                                                                      | screenshot gallery                                  | own 16 |

His house grid is the 4+6 compound `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr` (idd G2). But the
40 weekly demos show the cheaper truth: nearly all use a plain `repeat(6|8|12, 1fr)` and
get asymmetry from **holes and uneven spans** (idd G3). The compound grid earns its keep
only on pages with many related element widths; on a three-element hero it is overkill.

His reading-speed ladder (idd G6): one module per screen is slowest, many tiny modules
fastest. Choose module size by how long the reader should stay.

Notes on applying them:

- **Diagonals are rare on the web** and he uses them on purpose (talks 1.10); a cheap,
  strong differentiator for a hero.
- **Story beats** suit our one-page sites directly: problem, offer, proof, calm close,
  each with a different composition (talks 1.6). Order restored = calm justified
  columns; tension = huge image and eye lines.
- **Don't reduce art direction to the decoration list.** He warns against equating it
  with hanging pull quotes (talks 1.9). The structural moves only work when they serve
  the concept from §1.

## 3. Surface moves (atmosphere: colour, image, type, motion)

- **Atmosphere is designed separately from layout** and survives everywhere, including
  phones (talks 1.15). This is his only real small-screen answer.
- **One accent colour tying a word to a picture** (red "Deadly" ↔ red dress); greys and
  one hot accent recur in his decks (talks 1.12). Colour as uneven hierarchy, not equal
  swatches (talks 1.16).
- **Ownable illustration built from the brand mark or product** instead of stock
  photography (talks 1.13, accounts 1.1). Strongest single lever for small businesses.
- **A world to explore** for personality-led clients: mascot, toys, illustrated scene,
  hover sounds (accounts 1.2). Clients praise recognisability ("tells my story").
- **Ambient motion**: slow, looped, real-world motion that adds mood; dial back
  whatever draws the eye; easter eggs (talks 1.14).
- **Display type chosen to evoke the subject's era or world** (talks 1.8).
- **Type as the image** (idd T1): giant numerals with a small light unit replace the
  icon-card stats row; vertical type as a column or stripe; letters as structure or
  masks; text as the object. Strongest move for businesses with little photography.
  "Expressive typography needn't need fancy fonts": one family, black and light weights,
  tight tracking and leading.
- **Magazine anatomy as the content model** (idd T2): running head, headline, standfirst,
  lede, caption, pull quote, body. Write content for these slots, not for "hero /
  features / CTA". Indented paragraphs with no spacing give solid blocks.
- **Three hues, one accent per story** (idd K1): dominant, supporting, accent, plus
  neutrals; per-story accent sampled from that story's photograph while layout and type
  stay fixed. His recurring palette: mustard, crimson, black, off-white, one blue.
- **Drawn subjects, not photos**: almost every design in the series uses line drawings or
  flat silhouettes of the subject, which is what makes overprint, shape-wrap and
  structural shapes possible (idd C7).
- **Accepted reading cost for impact**, mitigated rather than avoided (idd §3).

### Thai-script cautions (our inference, from idd)

- Vertical Thai reads poorly: keep vertical type to Latin numerals, dates, short brand
  words.
- Thai has no spaces between words: justified text wrapped around shapes will gap badly;
  use ragged edges.
- Giant numerals (prices, years, counts) work in any script and are the safest
  type-as-image move.

## 4. System shape for AppBaoBao (how this scales to many clients)

His own answer to "many sites from one system" fits our product almost exactly:

- **Fixed foundation, separate switchable layers**: layout templates, theme (headline,
  quote, button styles), colour scheme, all independent on one CSS base (So Foot,
  talks 1.5). A fixed house system with a different feel per story (ProPublica,
  accounts 1.7).
- **"Your boring design system, not somebody else's"**: the foundation carries *this*
  client's personality; a tweaked framework carries someone else's (talks 1.5).
- **Risk he names**: the system becomes the end and nobody designs outside its edges.
  For us: the per-client concept (§1) must be allowed to break the system's templates.

### His working order (recent client work, clients §2)

1. Conversation about the business and the person, allowed to wander into interests.
2. Content audit, rewritten copy (in the proposed voice), "storyboards": what someone
   discovers in what order.
3. **Type first**: shortlist faces, ask the client how each *feels*, choose himself;
   test with the client's name, numerals and the client's language. Rejects ubiquitous
   faces (Lato, Poppins) as "horribly generic".
4. Palette as a system with roles; rebuild weak brand kits; no pure black or white.
5. Pencil sketch → flat vector → details → SVG with moving parts separated.
6. Rough graphics shown early as talking points; expect to lose favourites (Scoring Arts
   went through five concepts).
7. Design in the browser; hand over a working prototype.
8. Extend to print and merch when the system is strong.
9. AI as scrapbook and corrector while he directs; never to write or invent the idea.

### Briefs and intake (own §2)

- A brief states goals, challenges, opportunities and dreams, never solutions.
- Treat a "sites we like" list like haircut photos on a barber's wall: don't act on it.
  The client hires you to solve their problem, not to copy someone else's solution.
- Ask "why" of any prescriptive brief.
- Ask the client for concrete objects (Moonwalk's toys) and build the concept from them.
- "Solve a different problem": look at how other fields solved analogous problems
  (DVD menus for navigation, car climate controls for checkout steps) (own §2, 2007).

### Sales move (clients 1.13)

He won Count Binface by publishing an unsolicited redesign built from the candidate's
own personality. For AppBaoBao: a free one-page concept for a named shop, made from
their own story, is a proven way in. This matches our free one-page tier.

## 5. Gaps and cautions so far

- **Small screens: he states a method, his quick demos don't follow it.** Stated
  (idd S1–S7): storyboard 320/768/1280 before building; horizontal scroll strips instead
  of shrinking; art-directed image swaps (different crop or drawing per size, never a
  scaled copy); keep the *ratio* of scale contrast with `vh`/`vw`; carry a token of the
  device when the device can't fit (slabs → three palette circles; overlapping squares →
  one square behind each block); small layouts can still have columns; each breakpoint
  its own composition. Built (idd S8): in the 40 demos rotation, vertical type, overlap,
  masks and beams mostly appear only at 48–64em, and below that is a plain stack.
  Designs built as SVG type art or `vw`-proportional columns survive whole. **Rule for
  us:** pick the one device that must survive on a phone and build it phone-native
  (strip, swap, token, ratio, SVG); letting it vanish at a breakpoint is the failure
  case. Our customers are seen mostly on phones, so this rule must lead, not trail.
  From `own` 15: he works fluid rather than mobile-first; sets breakpoints by the
  content (the width of each dancing character), not by device; a hero built as one SVG
  scales as a unit and keeps its composition; a side column of display type can become
  a full-width headline on the phone, so scale contrast *grows*; parallel lockups become
  a horizontal scroller; the hero crops to its central group rather than shrinking.
- **Editorial bias**: his book examples are editorial; his small-business client work
  is the better model and works through concept and illustration (accounts §4).
- **Code-first design drifts boxy**: critics' point, which he partly conceded. For
  agents this is critical: an agent writing HTML directly is the extreme case. The
  model must force a composition step (sketch or described layout with an idea) before
  any code (accounts 1.5).
- **Publication constraint (chakrit, 2026-11-09)**: the finished skill will be
  published. It uses only freely published material (no paid books, PDF issues or
  members-only transcripts) read directly. Book ideas are fine when they reach us
  through public channels: reviews, others' blog posts, or his own blogs, articles,
  talks and interviews. It is written in our own words with short attributed
  quotes, and it describes his moves as principles rather than reproducing his specific
  designs. Any paid material chakrit supplies later goes into a separate, unpublished
  place and never into this model.
- **His ratio arithmetic has slips** (own 4, idd G2): copy the methods, recompute any
  numbers.
- **Characters can be re-dressed over time** (seasonal scenes on his own hero, own 12):
  a cheap way to keep a small client's site alive.
- **Thai display type**: name towers and type-as-hero need a Thai display face with
  enough weights (clients 1.8). This is an open question for our type stack.
- **Illustration cost**: bespoke drawing is his main lever; we need a way to produce
  ownable imagery per client (drawn motif from logo, generated with constraints, or
  simple geometric construction like EPD's circles).
