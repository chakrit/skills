# Andy Clarke: synthesis

Written from the four files in `notes/` and nothing else. Citations point into them:

- `work P1` to `work P14`: the pages studied in `notes/work.md` (P1 to P6 are his own
  site, stuffandnonsense.co.uk; P7 to P14 are client sites).
- `words S1` to `words S30`: the sources in `notes/words.md`.
- `words-2 [ID]`: the sources in `notes/words-2.md`.
- `accounts`: `notes/accounts.md`, with the person named.

Each file gives the URL and date of every source. "Stated" means Clarke said it,
"observed" means a page shows it, "reported" means someone else said it.

## Order of work

The words and accounts describe this order. The sources do not agree on what comes
first after the story; both versions are recorded.

1. **The business's story, before any visual decision.** He audits the content and the
   site's structure "to understand the story it needs to tell" before he thinks about
   illustration, layout or typography (stated, words S5). The story is "a combination of
   your experience, expertise, and values, plus the reasons people choose you", and his
   job "is to uncover yours", not invent one (stated, words S4). He starts by listening
   and asking questions, looking for "why you or your organisation is different from
   everyone else's" (stated, words S4, S2; words-2 [HELP]). A client reports that he
   brings "creative ideas and perspectives that we hadn't considered" (reported,
   accounts, Paul Bradley).
2. **Reframe the brief.** He states the real problem in other words than the client's:
   Codeboxx was about trust, not organisation; the Academy of Scoring Arts was a
   community, not an educational platform; Portico "didn't need pictures of property, it
   needed a strong visual language" (stated, words-2 [PCB], [PSA], [PPI]).
3. **One idea particular to this client.** He builds the identity on one thing the client
   loves or is: Begoña Pereda's cassette decks and tape machines, Michael Baugh's 1950s
   and 1960s science-fiction paperbacks, Tristan Jakob-Hoff's interest in Saul Bass, a
   story character (Orango Jones) for Mike Worth, so "the story shaped the experience
   from the beginning" (stated, words-2 [PBP], [PMB], [PTJ], [PMW]). Moonwalk Audio sent
   him cardboard scenery, pencils, a plastic dragon and vintage toys, which became the
   illustration (stated, words S8; observed, work P4). He does not start from websites in
   the client's sector (stated, words-2 [PBP], [PCM]); he looks to magazines, posters,
   comics, album covers and the art directors he names (see "Sources of ideas" below).
4. **Content path and wireframes as storyboards.** Mountain Duck began by "mapping the
   Mountain Duck content and simplifying the path between the home and download pages",
   then "wireframes and content planning before moving onto illustration and animation"
   (stated, words S7). Lockrose: content audit and structure, then "Once that journey
   felt right, I began sketching ideas for a visual language" (stated, words S5).
   Wireframes are "storyboards rather than diagrams of boxes" that decide "what someone
   should discover, in what order" (stated, words-2 [PMW]).
5. **Pencil sketches, then vector artwork.** Every Lockrose illustration "began life as a
   pencil sketch before I redrew it as scalable vector artwork, animated using SVG and
   CSS" (stated, words S5); Moonwalk Audio started with pencil sketches (stated, words
   S8). The Moonwalk Audio article shows the sequence: photograph of the real objects,
   line drawings of them, finished illustration, mascot poses, final scene (observed,
   work P4). Layout ideas are explored "in black and white" with "cursive typefaces"
   (stated, 2021, words-2 [G45]).
6. **Type, or colour.** In 2026: "I always start with type, because it sets the tone for
   everything else" (stated, words-2 [SHI]). His 2022 Zombie Hunt series, which he calls
   a walk through "my process and the decisions I make", runs colour, then dark and light
   themes, then grid, then small screens, then code (stated, words-2 [Z1] to [Z5]). He
   does not comment on the difference (words-2, "Where he changed his mind").
7. **The home page illustration sets the visual language.** "The Moonwalk Audio homepage
   illustration established a visual language I could use throughout the website"
   (stated, words S8).
8. **Into code early.** "After just one or two rounds of creative concepts made using
   Sketch, I switch to code as quickly as possible" (stated, 2022, words-2 [Z5]). In 2026
   he builds an interactive Eleventy prototype instead of static mock-ups or Figma files
   (stated, words-2 [PPI], [PVK]). Foundation styles, "colors and typography", come first
   in code (stated, words-2 [BT]); markup is chosen from "the most appropriate elements
   which describe my content" (stated, words-2 [D18]). He designs and builds his own
   sites and does not build other designers' (stated, words S4).
9. **Show, explain, drop what does not work.** He shows type shortlists and asks which
   "felt right", but does not let the client choose: "that's my job" (stated, words-2
   [SHI]). Concepts get rejected and replaced: Lockrose started with photography plus
   bold graphics, the team "weren't convinced" and did not want photographs of people,
   so he went "back to the drawing board" (stated, words S6); the Shared Homeland bird
   concept gave way to maps (stated, words-2 [SHI], [PSH]); Scoring Arts went through
   "dozens of sketches and banner concepts" (stated, words-2 [PSA]). He explains "the
   thinking behind every design decision" (stated, words S2, S3; words-2 [HELP]) and
   refuses a "big reveal" (stated, words S23; words-2 [CB]).

Clients report following the work while it developed (reported, accounts, Jas
Dosanjh) and being shown ideas before the build (reported, accounts, Count Binface).

## Moves

One entry per move in `notes/work.md`. Counts are out of the fourteen pages studied. Of
the seven client home pages (P7 to P11, P13, P14), P13 (Codeboxx) and P14 (Shared
Homeland) show the fewest of the moves; they are named under "Where not" wherever they
depart.

### 1. An eight-track mirrored grid

- **Looks like:** on article, case-study and inner pages, a wide reading column ending
  near the page centre, an empty band, then a narrow sidebar or call-to-action box at
  the right. Elsewhere, rows start and stop on unequal tracks.
- **Built:** eight tracks whose widths mirror around the centre, with 30 px gaps. The
  usual ratio is 4:1:3:2:2:3:1:4: for 1355 px of content at a 1440 px window, 229,
  57.25, 171.75, 114.5, 114.5, 171.75, 57.25 and 229 px, with 40 px side margins. The
  other ratio is 2:1:1:2:2:1:1:2 (191.2, 95.6, 95.6, 191.2 ... px on P9). On article,
  case-study and inner pages the text takes tracks 1 to 5 (about 807 px), track 6 stays
  empty, and a sidebar of about 316 px takes tracks 7 and 8 (observed, work P3, P4, P6,
  P12). On P7 the hero repeats 4:1:3:2:2:3:1:4 across the whole 1440 px window with no
  gaps, so the illustration meets the window edge (observed, work P7). Rows of equal
  items sit on a separate 12-column grid on the same pages (see "Equal-column rows"
  below). How much of a page sits on the eight tracks varies: on P13 only the header,
  a centred FAQ column (tracks 2 to 7) and the footer do; the hero (two halves) and the
  feature row (three equal columns) sit on 12 columns, so its first screen shows no
  eight-track rhythm (observed, work P13). P14 has no eight-track grid at all (see
  "Where not").
- **In the CSS:** the stylesheets of his own site and Lockrose define the templates as
  custom properties, identical on both sites (observed, work move 1, "In the CSS"):
  - `--grid-4-5: [a1] 4fr [b2] 1fr [a2] 3fr [b3] 2fr [a3] 2fr [b4] 3fr [a4] 1fr [b5] 4fr [a5]`
    is the 4:1:3:2:2:3:1:4 grid. Its `a` lines fall at 0, 5, 10, 15 and 20 of 20 (four
    equal columns) and its `b` lines at 4, 8, 12 and 16 (five equal columns): a 4+5
    compound.
  - `--grid-4-6: [a1] 2fr [b2] 1fr [a2] 1fr [b3] 2fr [a3 b4] 2fr [b5] 1fr [a4] 1fr [b6] 2fr [a5]`
    is the 2:1:1:2:2:1:1:2 grid: `a` lines at 0, 3, 6, 9, 12 of 12 (four columns), `b`
    lines at 2, 4, 6, 8, 10 (six columns).
  - `--grid-3-4: [a1] 3fr [a2] 1fr [b2] 2fr [a3] 2fr [b3] 1fr [a4] 3fr [a5]` is defined
    but not seen on any page studied; `--grid-12-col: repeat(12, 1fr)` is the 12-column
    grid.

  `.layout` applies `--grid-4-5` only inside `@media screen and (width>=64em)`;
  `[data-grid="3-4"]`, `[data-grid="4-5"]` and `[data-grid="4-6"]` swap the template.
  Children are placed on named lines through `data-layout` attributes named after cities
  (22 on his site). `athens` puts its first child on `a1/b4` (0 to 12 of 20, tracks 1
  to 5) and its second on `a4/a5` (15 to 20, tracks 7 and 8), which gives the 807 px
  column, the empty track 6 and the sidebar on P3 and P4. Other placements on P7:
  `madrid` (`a1/a3`, `b4/a5`), `paris` (`a1/b3`, `a3/a5`), `stockholm` (`a1/b4`,
  `a4/a5`), `tallinn` (`a1/a2`, `b3/a5`); `amsterdam` spans `a1/a5`. Lockrose's hero
  band takes `grid-template: var(--grid-4-5)`. Column gap
  `clamp(1.6875rem, 1.6223rem + .3261vi, 1.875rem)`, row gap
  `clamp(1rem, calc(.89rem + .54vw), 1.31rem)`. Mountain Duck (P9) and Codeboxx (P13)
  hold `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr` under the name `--grid-4-5` (on P9 with the
  comment `/* 4+6 grid system */`), with no named lines, placing children by line
  numbers; P13's hero and feature layouts use `--grid-12-col` (observed, work move 1,
  "In the CSS"). Shared Homeland's stylesheet (P14) defines only `--grid-12-col` and no
  eight-track template. The P8, P11 and P12 stylesheets were not fetched.
- **Default replaced:** twelve equal columns, or one centred column (work, move 1).
- **Reason:** twelve symmetrical columns "led to a generation of homogenous layouts and
  uninspiring designs" (stated, words S18); with twelve even columns "the rhythm is
  monotonous" (stated, words-2 [Z3]); starting from twelve columns would not have "forced
  the break from conventional thinking" (stated, words-2 [CG]); two overlaid grids are
  "more interesting than one grid used in isolation" (stated, words-2 [G45]). Unequal
  modules set "visual pacing": "People naturally spend longer looking at larger spacial
  zones" (stated, words S18). Narrow columns serve to offset a headline, widen an image
  by one narrow width, indent images and pull quotes, and give "precise amounts of
  whitespace" between main and supplementary content (stated, words-2 [CG]); an empty
  narrow column between standard ones makes "a structured layout feel more dynamic"
  (stated, words-2 [AV]). Higher ratios between column widths "add drama ... for designs
  with a strong purpose"; lower ones suit "academic or editorial content" (stated,
  words-2 [RA]). A pull quote whose edge aligns to grid lines feels "part of the story"
  (stated, words S18).
- **Where used:** 4:1:3:2:2:3:1:4 on P1 to P8 and P12 (9 of 14); 2:1:1:2:2:1:1:2 on P9,
  P11 and P13 (3), where P11 runs it across the full width with no outer margin and
  gives the left four units to a sidebar, and P13 uses it only for header, FAQ column
  and footer.
- **Where not:** P10, twelve equal columns only, hero split four columns to eight; P13's
  hero and feature row; P14, twelve equal columns, with a hero of three mirrored columns
  `1fr 1.5fr 1fr` pulled to the window edges by negative inline margins (observed, work
  P14).
- **Phone:** one column with 18 px margins on his own site, P12, P13 and P14, 27 px on P9
  and P10 (observed, work). In the CSS of his site, Lockrose, Mountain Duck and Codeboxx the
  eight-track template applies only from 64em up (observed, work move 1, "In the CSS").
  He says he keeps the compound grid on small screens with fewer columns (stated, 2022,
  words-2 [Z4]).

### 2. A commissioned illustrated scene as the hero

- **Looks like:** the first screen is a drawn scene that turns the business's subject
  into a world with characters or a mascot: cartoon outlaws in a desert (P1), a sheriff's
  office (P6), a painted noir fist-fight (P5), a low-poly energy landscape of pylons,
  turbines, a dam and a nuclear plant (P7), a toy-box world with an astronaut whose head
  is a microphone (P8), a steampunk machine that processes files (P9), a 1970s
  reel-to-reel tape machine (P11) (observed, work).
- **Built:** full width or bleeding off at least one edge: P1's scene is 1440 by 550 px
  and ends in a ragged line of flowers and ground, not a straight cut; a hand on P5
  reaches below the hero into the content; P7's 864 by 749 px landscape and P9's 900 px
  machine run to the right edge; P11's reels are cut by the top and right edges (observed,
  work). Each project has its own illustration style (flat low-poly, black-outlined
  cartoon, painted comic, steampunk, 1970s flat) and the illustration's palette is the
  site's palette (observed, work). Built as layered SVG: P8 from at least eight layered
  SVGs (observed, work P8). The headline sits under the scene (P1) or beside it (P7, P9,
  P11) (observed, work).
- **Default replaced:** a stock photograph, a product screenshot, an abstract gradient or
  a generic vector (work, move 2).
- **Reason:** for property and software he rejects "faded stock photos of generic city
  skylines or ethnically diverse people shaking hands" (stated, words-2 [AA2]); Portico
  "didn't need pictures of property, it needed a strong visual language" (stated,
  words-2 [PPI]); Codeboxx product photos were "dull" (stated, words-2 [PCB]). "Every
  illustration on a website has a job to do" (stated, words-2 [PCB]); Lockrose's
  illustrations "don't simply decorate the website—they reinforce its central idea"
  that "successful projects develop through clearly defined stages" (stated, words
  S6). On Lockrose the client did not want photographs of people (stated, words S6).
  Full-width banners "aren't inherently bad, but using them as filler or
  because everyone else has them is" (stated, words-2 [EL2]). A mascot from the logo
  "appears in different poses across the site" (stated, words S8) and guides visitors
  "while adding warmth and humour" (stated, words S7). Disparate objects are made one
  world with "black outlines, geometric shading, and a limited colour palette", kept
  imprecise because "making everything too precise would've taken away the playfulness"
  (stated, words S8). Lockrose's style came from vintage Graphis issues, "Flat colours.
  Strong shapes. Clear compositions", built on intersecting triangles that echo the
  company's identity (stated, words S6). The illustration crossing the edge of the
  window or its own box: reason not stated.
- **Where used:** P1, P5, P6, P7, P8, P9, P11 (7 of 14): three pages of his own site and
  four of the seven client home pages. P3 shows the same kind of illustration as a 525 px
  square video; P2 and P4 show illustrations as content.
- **Where not:** P10 uses a blue duotone photograph of the composer in the same place;
  P12, an inner page of the P7 site, leads with a documentary photograph inside the
  article column and has no illustration; P13's hero is one portrait at a time, about
  545 by 610 px, built from small teal squares with QR-code finder squares in three
  corners, switched by five numbered buttons between redrawn famous paintings (Van
  Gogh, The Scream, Mona Lisa, Marilyn, Girl with a Pearl Earring). It sits inside the
  margins in the left half, reaches no window edge and has no characters in a scene.
  P13's other artwork is one isometric product box drawn once and recoloured four times
  (observed, work P10, P12, P13). P14's hero is a full-bleed raster map texture in dark
  teal, with raster images of overlapping flat rectangles in teal, cyan and pale grey in
  the two outer columns, blended over it with `mix-blend-mode: screen` at opacity .8; no
  drawn scene, no characters (observed, work P14). For Shared Homeland he says his bird
  concept was rejected by the client in favour of topographical and pre-1948 maps
  (stated, words-2 [SHI], [PSH]); that speaks to the map. P10, P12, P13 and P14's
  rectangles are not explained (see Mismatches).
- **Phone:** see move 7.

### 3. Small ambient loops inside the illustration, with a way to stop them

- **Looks like:** parts of the scene move slowly and independently while the rest is
  still.
- **Built:** separate SVG parts on long loops: clouds 240 s (P1); turbine blades 10 s
  and a pulsing nuclear dome 4.8 s (P7); about 90 stars at 7.7 to 13.9 s and pencils
  swaying at 10 to 12 s (P8); about 40 cogs at 14 to 24 s, some counter-rotating, a
  conveyor at about 8 s, pipes glowing at 9 s (P9); reels at 9 s and a 60 s tape transfer
  (P11) (observed, work). P1 has a "Pause animations" button on the illustration; every
  page whose CSS was counted (P1, P4 to P14) has 2 to 11 `prefers-reduced-motion` rules
  (observed, work). He chooses what moves by asking "Does this thing have weight?", "Is
  it flexible?", "Would it move in real life?"; feathers swing "three degrees"; "longer
  durations", ease-in-out or relaxed cubic Béziers, seamless loops; several subtle
  animations layered "like building a sound mix" (stated, words S16).
- **Default replaced:** a static hero, or fade-in-on-scroll (work, move 3).
- **Reason:** motion that adds "atmosphere without stealing the show" (stated, words
  S16); "If someone's eyes are drawn to it, it's probably too much, so I dial back the
  animation" (stated, words-2 [AA2]); "reserve the most obvious animations for elements
  that I need to create the biggest impact" (stated, words S16); animation "works best
  when it adds character and atmosphere rather than movement for its own sake" (stated,
  words-2 [PMW]). Lockrose's turbines and glow are there "without being a distraction"
  (stated, words S5).
- **Where used:** P1, P7, P8, P9, P11 (5 of 14): five of the seven pages with a drawn
  scene in the hero; P5 and P6 have scenes without recorded loops.
- **Where not:** P2 to P6 have only a 1 s nav fade and a 2.5 s wobbling sign; P10 has two
  CSS animations and an audio player; P12 has none; P13 has a logo colour shift, a
  footer-logo bounce, a fade when the portrait is switched and a 5 px hover lift on the
  product boxes, and no ambient loops; P14 has a logo fade on load and view-transition
  zooms, and no ambient loops (observed, work).
- **Phone:** not recorded.

### 4. One family for the whole site, body text included

- **Looks like:** a single typeface sets logo, headings and body.
- **Built:** Obviously on his own site (P1 to P6), Commissioner on Lockrose (P7, P12),
  Alexandria (P8), Zalando Sans SemiExpanded (P9), Fido (P11), Space Grotesk (P13),
  Bankside Sans VF (P14; its tall condensed title is an SVG logotype, not a second face)
  (observed, work). No serif face on any page studied (observed, work).
- **Default replaced:** a display face for headings paired with a neutral text face
  (work, move 4).
- **Reason:** he chose Obviously "because it has plenty of styles and weights" (stated,
  words S10). Expressive headlines can come from one family: black and light weights,
  negative tracking and tight leading make "a block of type which demands attention";
  "Expressive typography needn't need fancy fonts" (stated, words-2 [HL]).
- **Where used:** P1 to P9, P11 to P14 (13 of 14).
- **Where not:** P10 pairs Delirium, an ultra-condensed display face, with Fira Sans
  Condensed Light for text (observed, work). Not explained.
- **Phone:** the same family; see move 5 for sizes.

### 5. The one family set as a characterful display face

The work notes split move 4 here: one family (move 4 above) on 13 pages, these display
settings on 12.

- **Looks like:** the family's own extremes carry the personality: a width axis,
  uppercase headings at very light or very heavy weights, or a hand-cut face.
- **Built:** Obviously with headings at width 90 and weight 500 over body at width 100
  and weight 400 (P1 to P6); Commissioner with uppercase headings at weights 200 to 300
  over body at weight 200 (P7, P12); Alexandria with weight 900 uppercase headings over
  weight 300 body (P8); Zalando Sans SemiExpanded at 300, 500 and 900 (P9); Fido, an
  irregular hand-cut-looking face, including centred body copy (P11); Bankside Sans VF
  with headings at `"wght" 600, "wdth" 80` over body at `"wght" 400, "wdth" 100`,
  paired in custom properties such as `--font-bold-condensed`, and an uppercase condensed
  standfirst (P14) (observed, work).
- **Default replaced:** a neutral sans for everything (work, move 4).
- **Reason:** he gave Lockrose "typography with more personality than the generic
  typeface used previously" (stated, words S5); Mountain Duck got "custom typography" in
  place of "generic framework components" (stated, words S7); "Financial businesses often
  hide behind conservative typography ... I don't think that's true" (stated, words-2
  [PPI]). He picks type from a shortlist set in "type sheets" with real copy and the
  organisation's name, judging its "tone of voice" and its numerals and special
  characters (stated, words-2 [SHI]).
- **Where used:** P1 to P9, P11, P12, P14 (12 of 14).
- **Where not:** P10 (two families); P13, whose Space Grotesk headings are in sentence
  case with hierarchy by size and weight only: no width axis, no uppercase display
  setting (observed, work P13).

### 6. Big display type over small body text

- **Looks like:** headlines several times the body size, body text small.
- **Built:** body 14.4/23.04 px on his own site and P10, 16 to 18 px on the other client
  sites; H1 48.8 to 72 px. H1 to body ratios: 5.0 (P1, P10), 4.8 (P4), 4.0 (P8), 3.8
  (P13, from the CSS), 3.6 (P7, P12), 3.05 (P9, P11). Client H1s are often set solid,
  line height 1.0 (P7, P8, P10, P12), 1.1 on P13; his own at 1.2. His article H1 runs in
  five short lines (P4); Lockrose's in five (P7); P13's in four (observed, work).
  Headings use `text-wrap: balance` (observed, work P4, P13).
- **Default replaced:** 16 to 18 px body with an H1 two to three times larger (work,
  move 5).
- **Reason:** "Bold type projects confidence, and a steep typographic hierarchy, weighted
  towards large type, is unapologetic. Small type and a shallow hierarchy are less
  challenging" (stated, words-2 [EL1]). Size must be "relative to the size of other
  elements" (stated, words S19). The small body: reason not stated.
- **Where used:** P1 to P13 (13 of 14).
- **Where not:** P14, where the H1 is visually hidden and the visible title is an SVG
  logotype about 280 px wide at both widths (observed, work P14).
- **Phone:** client H1s drop to about 35 to 40 px and his own to 48.5 px; body stays at
  or near desktop size (14.1 to 14.4 px) (observed, work). He sets type "readable on
  every screen and rarely increase[s] them as screens get bigger" (stated, words-2
  [Z4]). On P14 the two text sizes move in opposite directions on the phone: body
  `clamp(1rem, 1.1761rem + -0.2273vw, 1.125rem)` grows from 16 px at 1440 px to 18 px
  at 390 px, and smaller text shrinks from about 14.6 px to about 10.3 px; the SVG title
  keeps its desktop width (observed, work P14).

### 7. One or two groups become a horizontal scroll-snap row on phones

- **Looks like:** on a phone, a group that sat side by side on desktop scrolls sideways,
  one item at a time, with the next item showing at the edge. The page's other groups
  stack.
- **Built:** service items (P1), filter pills (P2), thumbnails and related projects (P3),
  shop items (P4), the life-and-work timeline at one year per screen (P6), testimonials
  (P8, P9); often a progress bar under the row; P4 with mandatory snap. It is one or two
  groups per page; the other groups stack (for example P1's portfolio items and blog
  list, P9's feature columns) (observed, work). He describes the same build: below a
  container width of `48rem`, two columns become a sideways scroller, each item `85%`
  wide so part of the next shows (stated, words S14).
- **Default replaced:** stack every item vertically (work, move 6).
- **Reason:** one-column collapse makes rhythm "monotonous" and turns pages into "content
  feeds"; a scroller gives "grouped content its own stage, the way a magazine spread
  might" (stated, words S14); a partly visible next item "hints that there's more to
  see" (stated, words S14); a snapping sequence "slows someone's reading speed by making
  each swipe an intentional action" (stated, words S14); six images in a sideways panel
  are not shrunk, and people do not scroll past all six before reaching the content
  (stated, 2019, words S19). "There's no need to fall back on predictable, single-column
  designs for small screens" (stated, words-2 [ER]).
- **Where used:** P1, P2, P3, P4, P6, P8, P9 (7 of 14).
- **Where not:** P5, P7, P10, P11, P12, P13 and P14 stack every group; P13's product boxes
  become a two-by-two grid (observed, work). He also says "many of my Zombie Hunt page
  designs use a single column on small screens" (stated, 2022, words-2 [Z4]).

### 8. A different image for the phone, or the image moved

- **Looks like:** the phone shows another crop of the hero, or the illustration above the
  headline instead of beside it.
- **Built:** a separate `<picture>` source: P1's hero becomes a 390 by 546 px portrait
  crop with the characters larger, P5's a 390 by 354 px crop with the lettering still
  readable, P6's a portrait crop of the gang. On P7 and P9 the illustration moves above
  the H1 (390 by 338 px; 333 by 280 px). On P8 it becomes a boxed 348 by 201 px crop
  inside the margins. On P11 the machine stays, cut at the right edge, and the
  full-height stripes collapse into a five-swatch block (observed, work).
- **Default replaced:** the same image scaled down, below or behind the headline (work,
  move 7).
- **Reason:** crop large illustrations "with `picture` or clip-path rather than shrink
  them" (stated, 2022, words-2 [Z4]); a wide banner squeezed into a narrow column "loses
  its position in the visual hierarchy" (stated, 2012, words-2 [HI]).
- **Where used:** P1, P5, P6, P7, P8, P9, P11 (7 of 14), the pages with a drawn scene.
- **Where not:** P12, whose photograph is already above the H1 and only scales down;
  P13, whose portrait comes before the H1 in source order and is scaled to the content
  width; P14, which keeps the map background and hides the rectangle images on the
  phone (`data-visibility="large"`, `display: none`) rather than recropping or moving
  them (observed, work).

### 9. Hand-made lettering as image

- **Looks like:** titles drawn as artwork, usually a script line over heavy condensed
  capitals ("Design a new / WEBSITE OR PRODUCT"; "Andy Clarke's / STANDOUT DESIGNS FOR
  THE WEB").
- **Built:** images of lettering on his four service blocks (305 by 217 px, white on
  navy), the book title inside the P5 hero, product lettering in the shop row; lettered
  logos on client sites (Begoña Pereda's jostled letters, Ryan Knaggs's outlined
  condensed lockup; Shared Homeland's tall condensed SVG logotype with a teal box behind
  its middle line, used in place of a visible H1) (observed, work P1, P4, P5, P10, P11,
  P14). A display face used once per
  page can be converted to SVG outlines (8 kB against 17 kB for the WOFF2) with hidden
  accessible text (stated, words-2 [Z5]).
- **Default replaced:** live text in the heading font (work, move 8).
- **Reason:** for outlining a once-used display face, file size (stated, words-2 [Z5]).
  For lettering as such: reason not stated. His book covers draw on pulp detective
  magazines (stated, words S11).
- **Where used:** P1, P4, P5, P10, P11, P14 (6 of 14).
- **Where not:** P12: the Lockrose logo is a plain wordmark and titles are live text;
  P13: titles are live text and the logo is a geometric wordmark with a hexagon mark
  (observed, work).
- **Phone:** P5's lettering stays readable in the phone crop (observed, work).

### 10. Pages of one site re-themed to their subject

- **Looks like:** one page of a site changes its colours to suit its subject while grid,
  type and header stay.
- **Built:** his navy site (`oklch(0.284 0.057 269)`) turns near-black violet
  `rgb(23, 20, 31)` with burgundy `rgb(144, 36, 63)` buttons and tan `rgb(205, 178, 150)`
  labels on the hard-boiled book's shop page (P5), and very dark green `rgb(22, 29, 26)`
  with sage `rgb(142, 164, 155)` on the about page (P6) (observed, work).
- **Default replaced:** one colour theme across every page (work, move 9).
- **Reason:** said of articles, not of these pages: accent colours sampled from each
  article's images give it "its own distinctive style" while grid and foundation styles
  keep consistency (stated, words-2 [ER]). He built per-post custom designs into his blog
  (stated, 2025, words-2 [CP]).
- **Where used:** P5, P6 (2 of his 6 pages). **Where not:** P1 to P4 keep the navy.
- **Phone:** not recorded.

## What varies from project to project, and what decides it

| What varies              | How it varies (observed, work)                                     | What decides it (per the notes)                                           |
|--------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------|
| Illustration subject     | Pylons and turbines; toy-box world; file machine; tape machine     | The client's business and one thing particular to it (words-2 [PBP] etc.) |
| Illustration or not      | Scene on 4 of 7 client home pages; P13 portraits; P14 map          | P14's maps were the client's choice (words-2 [SHI]); otherwise not stated |
| Illustration style       | Low-poly, black-outlined cartoon, painted comic, steampunk, 70s    | A named reference: Graphis covers for Lockrose (words S6); not given else |
| Palette                  | Teal and orange (P7, P12, P13); teal on teal (P14); slate and red  | Comes with the client and its illustration; method below                  |
| Number of accents        | One on 8 pages, two on P5 and P13, more on P8 to P11               | Not stated                                                                |
| Typeface                 | A different family on every project studied (moves 4 and 5)        | Type sheets judged for tone of voice (words-2 [SHI])                      |
| Heading case             | Uppercase on P7, P8, P10, P11, P12; sentence case elsewhere        | Not stated                                                                |
| Grid ratio               | 4:1:3:2:2:3:1:4 on most; 2:1:1:2:2:1:1:2 on P9, P11, P13; 12 only  | Higher ratios for drama, lower for editorial (words-2 [RA]); not mapped   |
| Share on eight tracks    | Most on his site and Lockrose; P13 header, FAQ, footer; P14 none   | Not stated                                                                |
| Ground                   | Dark on 10 of 14; light on P7, P14 (dark bands), P11, P12          | Not stated                                                                |
| Sound                    | Pressable sounding objects and cue players on P8, P10, P11         | Audio clients: to make people "explore rather than scroll" (words S8)     |
| Photography              | P10 (the composer), P12 (the client's project)                     | Not stated; on Lockrose the client refused photos of people (words S6)    |
| Inner page vs home page  | P12 drops P7's hero band, illustration and motion                  | Not stated                                                                |
| Alignment                | P11 centred; P14 hero centred; others left, centred quotes, CTAs   | Not stated                                                                |

Within one client site, typeface, case and colours carry from home page to inner page
(observed, work P7, P12).

**Equal-column rows.** Most pages also have plain rows of equal columns on the 12-column
grid: two rows of four on P1, four feature columns and four quotes on P5, a two-by-two of
testimonials on P6, a two-by-two of values and four sector columns on P7, four-by-two
project items on P8, three feature columns and a two-by-two of screenshots on P9, three
project items on P10, a two-by-two of services on P11, three feature columns on P13, two
rows of three on P14 (every section below its hero). On P1, P7, P13 and P14 a thin
vertical rule separates the columns; on P1 it is drawn by
`data-divider="true"`, a 1 px rule (observed, work "What changes"). Reason not stated.

**Disclosure lists.** Two of fourteen pages use `<details class="item-faq">` lists: P5's
five chapters and P13's ten FAQs. On P5 his stylesheet hides the browser marker
(`.item-faq summary::marker {content:""}`) and gives the summary its own 8 px marker
column; on P13 the browser's default triangle shows. P13's FAQ fills about 30 percent of
the desktop page (observed, work "What changes"). Reason not stated.

**Colour method.** Pick a base colour, derive others from the colour wheel (split
complementary, double split, triadic), then adjust by eye: "colour theory is a starting
point, not a set of hard and fast rules" (stated, words-2 [Z1]). He often works with "a
limited colour palette" (stated, words S8) and "so often gravitate[s] towards
monochromatic color schemes", with an accent that "acts as a counterpoint" (stated,
words-2 [GP]). On the pages, the number of accent colours beyond ground and text is one
on P1 to P4 (blue, with red only in the logo badge), P6 (sage), P7 and P12 (orange
`rgb(255, 119, 0)`); two on P5 (burgundy and tan) and P13 (teal `#2db7b8` for logo,
links, buttons and rules, orange `#fe5d26` for the active button, nav separators and
link underlines, plus four product-box fills); P8 has red with slate-blue nav pills and
tan braces; P9 yellow with blue frames and orange rules; P10 blue with a green-to-navy
cue strip; P11 five stripe colours; P14 one mid teal against dark teal text, with cyan
only in the hero's rectangle images and no contrasting hue (observed, work "What
changes"). Accents can be
sampled from images (stated, words-2 [ER]). Darker shades for borders, lighter tints for
highlights; in dark mode raise lightness and saturation; tints and shades by multiply
and screen blends (stated, words-2 [GP], [Z2], [CPAL]). Contrast is checked during
design, not at the end (stated, words-2 [Z1]). He avoids pure complementary pairs
"unless I aim for a very high impact" (stated, words-2 [Z1]).

**Dark themes.** Off-black and off-white rather than pure, because pure black and white
"make text trickier to read" (stated, words-2 [Z1], [Z2]); in dark themes a lighter
weight, small text raised from 14 px to 14.5 to 16 px, a little tracking and word
spacing; one colour can swap role between dark and light themes (stated, words-2 [Z2]).
On the pages, dark grounds are tinted on P1 to P6, P8 and P9 (navy, violet-black,
green-black, slate) and near-black on P10 (`rgb(2, 3, 7)`) and P13
(`oklch(13.07% .0033 325.76)`) (observed, work "What changes"). The light-ground
P14 has dark teal hero and section bands and a moon icon in the footer for a dark theme
(observed, work P14).

**Measure.** Start at `--measure: 60ch` and adjust by eye; `55ch` for captions and short
blocks; `80ch` for introductions, headings and hero sections; layout follows the
measure, as in `minmax(0, var(--measure)) 1fr`; breakpoints come from the measure with
container queries, not from devices (stated, 2025, words S13). The pages run body text
at 73 to 85 characters per line on his own site and 91 to 103 on P12 (observed, work;
see Mismatches).

**Phones overall.** Every page stacks most groups; P1 to P4, P6, P8 and P9 turn one or
two groups into horizontal scrollers, and P5, P7 and P10 to P14 stack everything
(observed, work "What changes").

## Refusals

- Websites that look alike, where swapping "the logo, colours, and photographs would be
  enough" to turn one company's site into another's (stated, words S9).
- Framework defaults in layout, button styles or type hierarchy (stated, words S17);
  "Nothing visitors see was inherited from a framework" (stated, words S7); "The danger
  comes when the framework starts making creative decisions on your behalf" (stated,
  2026, words-2 [PMD]). The 12-column grid as a template that "should dictate how every
  website looks" (stated, words S9).
- Templates and trends (stated, words S4); "Templates begin with generalisations"
  (stated, words-2 [PBP]).
- Difference for its own sake (stated, words S22, S6).
- Personality at the cost of clarity: "Every illustration, animation, and interaction
  needs to support a user's journey and not distract from it" (stated, words S7).
- Pastiche: "inspiration and imitation are very different things" (stated, words-2
  [PMW], [RR]).
- Stock photography of skylines and handshakes (stated, words-2 [AA2]).
- Conservative typography as a credibility shortcut (stated, words-2 [PPI]).
- Lorem ipsum in type tests (stated, words-2 [SHI]).
- Pure complementary pairs, except for very high impact (stated, words-2 [Z1]).
- Small-screen layouts that squeeze elements without regard to hierarchy (stated,
  words-2 [HI]).
- Static visuals as sign-off artefacts and the "big reveal" (stated, words S23; words-2
  [MDC], [CB]).
- "Sites we like" sections and solutions written into briefs (stated, words-2 [BR]).
- Conventions are not refused: "Conventions exist because they work ... The problem
  begins when convention turns into imitation"; he kept Mountain Duck's feature, edition
  and download journey (stated, words-2 [PMD]). Not every site "needs to be unusual or
  experimental" (stated, words S9).

## Sources of ideas

Magazines and their art directors: Alexey Brodovitch, Bea Feitler, Ruth Ansel, Neville
Brody, Paul Rand, Bradbury Thompson, Emmett McBain, Giovanni Pintori, Max Huber, Herb
Lubalin, Otto Storch, Karl Gerstner, Wolfgang von Wersin, Saul Bass, Erik Nitsche;
magazines Pressing Matters, Avaunt, Ernest Journal, Harper's Bazaar, Ms., Rolling Stone,
The Face; vintage Graphis; pulp detective magazines; comics and cartoons (Hanna-Barbera,
Charlton Comics, DuckTales, Batman: The Animated Series); protest and gig posters (CND,
Red Wedge, Rock Against Racism); mid-century science-fiction paperbacks; '90s cartoons
and websites; the client's own objects (stated, words S6, S8, S11, S12, S18, S20;
words-2 [AB], [NB], [OS], [HL], [GP], [EM], [BT], [RA], [PTJ], [PSA], [PCM], [PMB],
[RR]). "Literally everywhere other than the web" (stated, words-2 [MEMO]). He does not
ask readers to mimic earlier work "but to understand their thinking" (reported,
accounts, Smashing launch text).

## Mismatches

What he says that the pages studied do not show:

- **Sentence case.** His rules for AI coding tools ask for sentence case in headings and
  interface copy (stated, words S26). Five of fourteen pages set headings in uppercase
  (observed, work P7, P8, P10, P11, P12).
- **Measure.** He starts text at 60ch and keeps 80ch for introductions (stated, words
  S13). Body text runs 73 to 85 characters on his own site and 91 to 103 on P12
  (observed, work P3, P4, P12). In 2012 he set no max-width on purpose (stated, words-2
  [LL]).
- **Off-black.** He avoids pure black (stated, words-2 [Z1], [Z2]); P10's ground is
  `rgb(2, 3, 7)` and P13's `oklch(13.07% .0033 325.76)`, both near-black (observed, work
  "What changes").
- **Full-width header.** His 2021 home page "avoids the conventional full-width header"
  (stated, words-2 [G45]); his current home page opens with a 1440 px full-bleed
  illustration (observed, work P1).
- **Named compounds against observed ratios.** He names 4+5 as giving `6|1|4|3|3|4|1|6`
  (stated, words-2 [Z3], [CG], [G45]) and 4+6 as giving `2|1|1|2|2|1|1|2` (stated, words
  S18); one article also gives `6|1|4|3|3|4|1|6` for "four columns with five" in a
  passage that otherwise names 4+6 (words S18, recorded as written). His stylesheets
  name 4:1:3:2:2:3:1:4 `--grid-4-5`, built from four and five equal columns, and
  2:1:1:2:2:1:1:2 `--grid-4-6` (observed, work move 1, "In the CSS"). The CSS agrees
  with his written 4+6; it does not agree with his written 4+5 figures,
  `6|1|4|3|3|4|1|6`. On Mountain Duck and Codeboxx the 4+6 ratio is stored under the
  name `--grid-4-5` (observed, work P9 and P13 CSS).
- **Codeboxx product graphics.** He says Codeboxx's product photos were "dull", so he
  made animated graphics per product category (stated, words-2 [PCB]). P13 shows one
  isometric box with the same path data in four fills, with a fade and a 5 px hover
  lift (observed, work P13). Only the home page was studied.
- **Hover colour.** Moonwalk Audio's monochrome objects "turn full colour on hover"
  (stated, words S8); hover was not examined on the pages (work, "Looked for").
- **Mascot throughout.** The Mountain Duck character "appears throughout the site"
  (stated, words S7); the one Mountain Duck page studied shows the duck app icon and
  duck yellow, and no character is recorded (observed, work P9).

What the pages show that nobody explains:

- Photography in the hero place on P10 and at the head of P12.
- P13's switchable QR-pixel portraits of famous paintings in place of a drawn scene,
  boxed in the left half.
- The client inner page (P12) dropping illustration, hero band and motion.
- Two type families on P10 against one everywhere else.
- P13's type without width or uppercase display settings.
- Uppercase headings on some client sites and not others.
- Centred body copy in Fido on P11.
- The choice between 4:1:3:2:2:3:1:4, 2:1:1:2:2:1:1:2 and twelve columns, and how much
  of a page goes on the eight tracks.
- Dark grounds on 10 of 14 pages; light on P7, P11, P12, P14.
- The number of accent colours.
- Equal-column rows and the vertical rules between them on P1, P7, P13, P14.
- P14's abstract rectangles in the hero's outer columns, its `1fr 1.5fr 1fr` hero, and
  its smaller text shrinking to about 10.3 px on the phone.
- The browser's default disclosure marker on P13 against a custom one on P5.
- The small body size (14.4 px) on his own site and P10.
- The illustration crossing a window edge or its own box.
- Hand-made lettering in place of live text.

## Gaps

- No source gives a type scale, a body size rule or heading sizes; the numbers above are
  observed only (words, "Looked for"; words-2 [Z4]).
- No numeric colour rule beyond the method above (words, "Looked for").
- Paragraph treatment on the pages: he says he mostly uses first-line indents with no
  space between paragraphs (stated, words-2 [QT]); the work notes do not record how the
  pages separate paragraphs.
- Vertical spacing between sections: not recorded.
- Motion on phones, hover states, reduced-motion behaviour, and what the scroll-timeline
  rules do: not examined (work, "Looked for").
- Inner pages of client sites beyond one (P12).
- What decides whether a client gets a drawn scene (four of seven client home pages do).
- What he shows a client at a review in 2025 and 2026, step by step (words and words-2,
  "Looked for").
- The colour reasoning in his B-movie poster and other Envato articles: unread (words,
  "Looked for").
- Any account by a client written outside his own site; every client quote was chosen
  by him (accounts, "Looked for").
- When he does not use a compound or modular grid, beyond "Single columns ... suitable
  for long passages of running text" (words-2 [Z3]).
