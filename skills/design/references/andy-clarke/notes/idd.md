# Andy Clarke, "Inspired Design Decisions": notes (stream `idd`)

Marks: **[stated]** Andy says it; **[observed]** seen by us in his designs, demo pages,
screenshots or their CSS; **[reported]** someone else says it (usually a designer he
quotes). Detail for every claim below is in the five group digests, which hold the
per-issue analysis, the grid values and the screenshot index:

- `references/andy-clarke/digests/idd-digest-A.md`: Avaunt, Pressing Matters, Ernest Journal,
  Brodovitch, demos 4 and 21
- `references/andy-clarke/digests/idd-digest-B.md`: Storch, Feitler, Brody, Lubalin, demos 1, 2, 3,
  9, 15, 20
- `references/andy-clarke/digests/idd-digest-C.md`: Huber, Pintori, McBain, Thompson, demos 5, 7, 11,
  14, 16, 17, 18, 19, 22
- `references/andy-clarke/digests/idd-digest-D.md`: demos 6, 8, 10, 12, 13, 23, 24, 25, 26, 32
- `references/andy-clarke/digests/idd-digest-E.md`: demos 27-31, 33-40

Screenshots: `tmp/andy-clarke/shots/idd/demoNN-1400.png` and `demoNN-390.png` for all 40
demos, plus realistic first-screen shots (`demoNN-1400v`, `demoNNv-1400`, `-390h`,
`-390-top`). The 390 images from `shoot.sh` are 600 px wide: the left 390 px is the phone
view in an iframe. Many demos size themselves in `vh`, so the tall full-page shots show
stretched empty bands; judge composition from the `v`/`h`/`-top` shots. Article images
(print sources and his derived desktop and phone designs) are in `raw/idd/img/`.

## Sources covered

The series has three layers: 12 Smashing articles (2019-2020, each with a members-only
webinar), 40 weekly demo pages on his own site (2020, "52 weeks", stopped at 40), and the
issues sold as PDF magazines.

| #  | Smashing article (URL)                                                                 | Date        | Print source and theme                                        |
|----|----------------------------------------------------------------------------------------|-------------|---------------------------------------------------------------|
| 1  | https://www.smashingmagazine.com/2019/06/inspired-design-decisions-avaunt-magazine/    | 13 Jun 2019 | Avaunt magazine: skinny columns, modular grids                |
| 2  | https://www.smashingmagazine.com/2019/07/inspired-design-decisions-pressing-matters/   | 11 Jul 2019 | Pressing Matters, Gerstner: compound grids, pacing            |
| 3  | https://www.smashingmagazine.com/2019/08/inspired-design-decisions-ernest-journal/     | 8 Aug 2019  | Ernest Journal: 12 columns used with a system, accent colour  |
| 4  | https://www.smashingmagazine.com/2019/09/inspired-design-decisions-alexey-brodovitch/  | 5 Sep 2019  | Harper's Bazaar, Portfolio: scatter, shaped text, mirroring   |
| 5  | https://www.smashingmagazine.com/2019/10/inspired-design-decisions-bea-feitler/        | 3 Oct 2019  | Bazaar, Ms., Rolling Stone: scale contrast, pop colour        |
| 6  | https://www.smashingmagazine.com/2020/03/inspired-design-decisions-neville-brody/      | 2 Mar 2020  | The Face: vertical type, bleed, rotation, question everything |
| 7  | https://www.smashingmagazine.com/2020/03/inspired-design-decisions-otto-storch/        | 23 Mar 2020 | McCall's: type carved around and into pictures                |
| 8  | https://www.smashingmagazine.com/2020/04/inspired-design-decisions-herb-lubalin/       | 13 Apr 2020 | Expressive typography: rotated, vertical, giant type          |
| 9  | https://www.smashingmagazine.com/2020/05/inspired-design-decisions-max-huber/          | 22 May 2020 | Swiss/Milan posters: circles, numerals, colour strips         |
| 10 | https://www.smashingmagazine.com/2020/06/inspired-design-decisions-giovanni-pintori/   | 26 Jun 2020 | Olivetti: three-hue palettes, modular panels, overprint       |
| 11 | https://www.smashingmagazine.com/2020/07/inspired-design-decisions-emmett-mcbain/      | 28 Jul 2020 | Record sleeves: slabs, stripes, deconstructed type            |
| 12 | https://www.smashingmagazine.com/2020/08/inspired-design-decisions-bradbury-thompson/  | 18 Aug 2020 | Westvaco Inspirations: CMYK overprint, series wrap-up         |

Other sources:

- https://stuffandnonsense.co.uk/inspired-design-decisions/ (index) and `/1/` to `/40/`,
  6 Jan to 5 Oct 2020. One web design per week, each "Inspired by <designer> #N", with the
  print piece it came from shown on the page. Designers: Storch, Lubalin (2, 9, 15),
  Feitler, Brodovitch (4, 21), Thompson (5, 17), Lustig, Huber (7, 11, 14), Beall (8, 26),
  Sutnar, Hofmann (12, 32), Carson, Pintori (16, 18, 19), Brody, McBain, Matter, Friedman,
  Nitsche, Bass (27, 29, 38), Garland (28, 31), Aicher, Kalman, Max Bill, Scher (35, 37),
  David King (36, 40), Glaser. All 40 screenshotted at 1400 and 390.
- https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-<N>-<name>/
  (2020): one post per demo, though 27-32 share a catch-up post. Each is a biography line
  plus a preview image, with no design reasoning [observed].
- https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions/ (3 Jan 2020):
  launches the weekly project. It was prompted by Dan Davies' "Print to CSS".
- https://stuffandnonsense.co.uk/blog/my-new-inspired-design-decisions-series-of-articles-and-webinars-for-smashing-members/
  (9 Apr 2019): the series format, "examine, teach the principles, apply, describe the
  code".
- https://stuffandnonsense.co.uk/inspired-design-decisions/shop/: the issues sold as PDF
  magazines with example files (£3.99 each). Not bought.
- https://stuffandnonsense.co.uk/blog/chock-full-of-design-inspiration-part-1 (17 Sep
  2018): his bookcase and the magazines and design books he values.
- https://www.smashingmagazine.com/smashing-tv/inspired-design-decisions (and the other
  Smashing TV pages): the webinar descriptions. The transcripts sit behind a members'
  login, so they were not used.
- The book: no Smashing book titled "Inspired Design Decisions" exists on the Smashing
  books list or his shop [observed]. The Thompson article mentions "the book which will
  follow it" [stated]. His shop now offers *Standout Designs for the Web*, with pre-orders
  opening 12 November. Nothing paywalled was read.

---

## 1. Moves

Moves are grouped as grid, composition, type, colour, and small screens. The last group
gets its own section because what he says about phones and what he builds differ.

### Grid

#### G1. Add one odd track to an ordinary grid (the "skinny column")

- **What:** take a conventional column grid and split one column, giving half its width to
  a neighbour. The print term is a "bastard column"; he renames it "skinny" [stated, #1].
  The track values are `1fr repeat(4, 2fr)` or `2fr 1fr 2fr 2fr 2fr` [stated].
- **Used for** [stated, #1]:
  - sizing an image at 1.5 columns, where one is too light and two too heavy;
  - sizing a logo exactly to the narrow track;
  - widening a text measure;
  - an empty strip of white space that "allows the eye to roam";
  - a wide carved gutter.
- **Same idea elsewhere** [observed]:
  - a `6rem` headline column in Brody's header (`1fr 6rem`) and in the Ital Style grid
    (`1fr 1fr 1fr 6rem 1fr`);
  - a narrow `[svg]` track in Thompson design 2 (`1fr [svg] 1fr 1fr 1fr`);
  - `7.5vw` gutter tracks written into the grid in demo 40
    (`7.5vw repeat(4,1fr) 7.5vw`).
- **Default instead:** blocks that snap to 1, 2, 3 or 4 of 12 equal columns. "One, two,
  three, or four block arrangements of content became the norm" [stated, #1].
- **Fits:** any page where one element (logo, portrait image, pull quote) looks wrong at
  every whole-column width. It is cheap and invisible to the reader. **Does not fit**
  below about 64em; he drops the skinny column at 48em and uses a plain 3-column grid
  [stated, #1].

#### G2. Compound grid: overlay two grids and use every line

- **What:** two grids drawn over the same width; the column tracks are the union of their
  lines [stated, #2].
  - 2+3 gives `2fr 1fr 1fr 2fr`.
  - 3+4 gives `3fr 1fr 2fr 2fr 1fr 3fr`.
  - 4+6 gives `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`, "the one I use most often" [stated]. He
    reuses it in #4, #5, #10 and #12 and demo 12 [observed]. It is his house grid.
  - His printed 4+5 pattern is arithmetically wrong; it should be 4|1|3|2|2|3|1|4
    [observed, digest A].
- **How he uses it:**
  - Text lives on one grid and images on the other. Pressing Matters runs text on 2
    columns and images on 3 [observed].
  - The narrow 1-unit tracks size drop caps and small elements [stated, #2].
  - Elements start on lines from different grids (see G4).
- **His framing:** equal columns are an even beat, while compound patterns are syncopated
  [stated, #2]. He also says, "Does Bootstrap create unimaginative designs? No, people
  do." [stated, #2]
- **Variant, stacked grids:** when one page holds two stories, give each its own grid,
  for example 4 columns above 6 [stated, #2].
- **Fits:** long-form or multi-element pages (about, story, menu with notes) where several
  element widths need to relate. On a 3-element hero it is overkill.

#### G3. Even grid, uneven placement: empty columns as composition

- **What:** keep `repeat(n, 1fr)`, but leave chosen columns or cells empty and give
  neighbours uneven spans. "Despite being built on a symmetrical grid, leaving some
  columns empty creates an unusual asymmetrical design" [stated, #9]. The same point
  appears in #8, #10, #11 and #12 [stated].
- **Evidence:** nearly all of the 40 demos use `repeat(6,1fr)`, `repeat(8,1fr)` or
  `repeat(12,1fr)`. The asymmetry comes from holes [observed, digests D and E]:
  - #29 leaves columns 1-2 and 5-6 black around a centre-third title card;
  - #32 splits the page 4:1:1, with one empty grey column before the text;
  - #37 uses named areas with `.` holes;
  - #38 is a 4:1 split on 5 columns;
  - Lubalin's 5-column page has an empty column 2 [stated, #8].
- **Default instead:** every track filled, content centred, equal cards.
- **He also advises** "streamlining twelve narrow columns into eight wider ones" [stated,
  #12], and 5 columns "unusual" and good [stated, #12].
- **Fits:** everywhere; this is the cheapest move in the series. The hole has to be
  deliberate and large: a whole column or a quarter of the page, which he says he left
  empty "for luxury" in #3 [stated].

#### G4. Staircase starts

- **What:** headline, standfirst and body each begin on a different grid line, so the
  left edges step diagonally across the page [observed, #2 designs pm-19 and pm-20]. A
  related move staggers starts by one gutter in a 2x2 layout ("use gutters to stagger the
  start") [stated, #3].
- **Echoes** [observed]:
  - demo 7 indents each sentence on its own strip by 30vw, 40vw, 30vw, 10vw and 25vw, a
    zig-zag reading line;
  - demo 3 staggers four type blocks and pulls one up with `translateY(-15rem)` so it
    sits beside its neighbour;
  - demo 24 offsets the heading from the paragraph with a 7vw indent.
- **Default instead:** every text element flush to one left edge.
- **Fits:** text-led sections with three or more text levels. Pointless for a single
  paragraph.

#### G5. Offset gutters between images and text

- **What:** images on halves over text on thirds, or the reverse, so the image gutter
  does not line up with the text gutter. "Image proportions are not nearly as interesting
  as the position of the gutter between images" [stated, #3]. Pick one system per
  publication: 3 columns for text and 2 for images, or 2 and 3 [stated, #3].
- **Default instead:** image grid and text grid share gutters (the card look).
- **Fits:** gallery-plus-text sections (portfolio, menu, product page).

#### G6. Modular grid with unequal zones and visible structure

- **What:** a sheet of equal modules (6x4 in #1, 3x3 in #10, 6x8 with fixed `110px` rows
  in demo 10) grouped into "spacial zones" of different sizes. Modules may be empty, and
  rules sit above and below each module [stated + observed, #1].
  - "It keeps content ordered within spacial zones but maintains energy by making each
    zone a different size" [stated, #1].
  - "It's rare to find designs online which are based on a modular grid" [stated, #10].
  - Demo 37 is the clearest web example: `grid-template-areas` with `.` holes, one 2x2
    zone, and alignment that changes row by row [observed].
- **Pacing ladder:** "Repeating smaller modules speeds up the movement, while larger ones
  slow it down" [stated, #2]. In #3 he lays out six reading speeds on a phone, from one
  module per screen (slowest) to many tiny modules (fastest, "ideal for mobile
  navigation") [stated + observed, #3].
- **Default instead:** a uniform card grid, all cells equal, no rules.
- **Fits:** catalogues, menus, timelines, spec lists and contents pages: anything with
  many items of unequal importance. This is the direct replacement for the
  three-card row.

#### G7. Visual order is not document order; header and footer need not sit top and bottom

- "Despite their names, you needn't place a header or footer element at the top and
  bottom of a layout" [stated, #10]. In Pintori design 3 the footer and header images
  sit side by side with the text between them [stated].
- Other examples [stated + observed]:
  - the headline placed visually below its text (Thompson design 2);
  - demo 40 puts `main` first in the HTML but places it right, so phones read the story
    first and desktops see the slogan slab first;
  - grid reordering puts brand and image first on phones (#10).
- He flags the accessibility risk of `grid-auto-flow: dense` reordering [stated, #1].

### Composition

#### C1. Text takes the picture's outline

- **What:** the text edge is drawn by the image, never a rectangle beside it [observed,
  digest B].
  - Angled objects bite into plain columns via `shape-outside` polygons (#7, demo 1).
  - A paragraph is sculpted into the subject's silhouette, set in uppercase so the shape
    reads (#7).
  - Text runs along the curve of a photo (#4).
  - A text block is sheared into a parallelogram to match a 20° rotated drawing (#4).
  - The left edge slants to follow a perspective beam (demo 25).
  - Text wraps a van's silhouette (#12 design 3).
  - Type is packed inside a product outline (demo 19).
  - Text lines sag under a model lying on them [observed in Storch's "Forty-winks",
    #7].
- **Why:** "Shapes offer so much more than simple text wrapping" [stated, #7]. He also
  says Storch understood ideas matter as much as pictures and words [stated, #7].
- **Default instead:** image box above or beside a rectangular text block.
- **Fits:** short copy (2-6 short paragraphs) next to an object with a strong silhouette:
  a product, a dish, a tool, a mascot. **Cost:** at 390 the wrapped column shrinks to 3-5
  words a line with justified gaps (demo 1) [observed]. For Thai, which has no spaces
  between words, justified wrap around shapes will look worse; ragged edges are safer
  [our inference].

#### C2. One big structural shape instead of a hero

- **What:** a single large flat form carries the page, and the subject sits in, on or
  across it [observed, digests C, D and E]. Examples:
  - a colour slab (demo 6);
  - a light beam (10) and a perspective beam (25);
  - a giant brand mark (23: the Citroën chevrons drawn huge behind the car);
  - a letterform used as the page mask (24: the page is a giant "D");
  - a horizon split (26);
  - a circle over a cut-out photo (Huber #9);
  - full-height colour stripes with images clipped per stripe (#4);
  - irregular slabs (#11, demo 22);
  - CMY targets (#12).
- These shapes are built from pseudo-elements, `clip-path`, `mask-image`, gradients or
  empty grid items, not images [observed].
- **Default instead:** photo hero with centred headline and button.
- **Fits:** home and landing first screens. The shape should come from the subject or
  brand (logo geometry, product silhouette, a local motif), which is how he picks it
  [observed: the chevron, the "DS", the Vespa wasp].

#### C3. Rotate a group, and make diagonals from empty modules

- **What:** rotation is applied to a whole composition or to a handful of related items,
  never to random singles [observed]:
  - a whole 5-column tile grid at −15° (demo 4);
  - a whole lockup grid at 20° (demo 37);
  - four images fanned −20/−5/10/−20° (#4 scatter);
  - a headline at −30° (#8);
  - labels fanned ±30/15/0° like insect legs (demo 33);
  - Mini cascades at ±15° (demo 12).
- A diagonal can also come from leaving the top-right modules empty: "it's not necessary
  to fill every grid module with content" [stated, #2].
- "It's unusual to see rotated text elements on the web, but when you do, they're often
  memorable" [stated, #8].
- **Default instead:** everything orthogonal.
- **Fits:** one rotated group per page at most, as the accent. **Small screens:** he
  almost always removes rotation below 48-64em (see S8).

#### C4. Bleed and crop to imply more; crop until it is abstract

- **What:**
  - panels and images run off the page edge: "more impact when you allow them to bleed"
    [stated, #3]; a bleeding header "implies there's more to see outside" while a margin
    "stops the eye" [stated, #6];
  - wheel crops entering from an edge (#5);
  - extreme crops that turn the product into an abstract shape (demo 32's Mini headlamp
    at 4/6 of the width; demo 30's black side crop) [observed].
- **Default instead:** the whole product, centred, with padding around it.
- **Fits:** strong for a product or place with a recognisable detail. Needs a second,
  whole view somewhere on the page (demo 32 swaps in the whole car on phones) [observed].

#### C5. Scale contrast, always relative

- "Largeness must be relative to the size of other elements"; "sheer size is rarely
  enough on its own" [stated, #5].
- Examples [stated + observed]:
  - a giant wheel against a tiny whole car (#5);
  - display words at about 4-5x their kicker (demo 3);
  - an 11 px body under a 3rem standfirst (demo 13);
  - a tiny caption in a huge dark field (demo 28);
  - 24 px captions next to 160 px numerals (demo 35).
- **Default instead:** a gentle type scale where H1 is about 2.5x body and every image is
  medium.
- **Fits:** everywhere. The contrast has to be visible on phones too (see S4).

#### C6. Mirror or invert two halves

- **What:** a spread split 50/50 where colour or form inverts across the seam [observed]:
  - #4: a red drawing on white facing a white drawing on red, with a two-tone logo
    straddling the seam;
  - Storch's black/red halves with nose-to-tail cars (#7);
  - Feitler's red/yellow fields swapped (#5);
  - demo 31's rows inverting orange and red;
  - demo 2 flipping the heading column between sections.
- He calls the spread a playground [stated, #4 heading as reported in digest A].
- **Default instead:** alternating image-left/image-right "zig-zag" feature rows, which
  is the weak cousin of this move.
- **Fits:** two-part content: before/after, two branches, his and hers, lunch and dinner.
  On phones he stacks the halves as two full-height panels, keeping the inversion [stated
  + observed, #7].

#### C7. Overprint: overlap flat hues so the overlap makes a third colour

- **What:** flat, saturated shapes or silhouettes overlapping with `mix-blend-mode:
  multiply` (or difference, overlay), standing in for print overprinting
  [stated + observed,
  #9, #10, #12, demos 5, 7, 16]. Examples:
  - Huber's translucent cyclists become Vespa silhouettes (demo 7);
  - Pintori's rotated outline squares turn green where blue meets yellow (demo 16);
  - Thompson's repeated figure printed four times in four colours (demo 5).
- **Prerequisite:** drawn subjects, not photos. Almost every design in the series uses
  line drawings or flat silhouettes of the subject [observed, digest C].
- **Default instead:** drop shadows and glassy cards.
- **Fits:** brands with flat illustration (AppBaoBao's own mascot style is a candidate).
  It needs a 3-4 hue palette (see K1).

#### C8. Copy one print piece's skeleton, swap in the client's subject

- **What:** every weekly demo takes one specific print piece and keeps its structure
  nearly intact (the band, beam, giant letter, horizon, cascade, mosaic), then replaces
  the subject [observed, digests C, D and E]. He does not blend sources; it is one
  reference per design.
- **The control experiment:** the same Vespa fact copy is art-directed five different
  ways (33, 34, 36, 38, 39), the Citroën DS three ways, and the Mini three ways
  [observed]. The content stays fixed; the source supplies the concept.
- **Default instead:** generic section templates filled with the client's content.
- **Fits:** our method directly. For each client, pick one print reference whose
  dominant device suits the business, and translate that device.

#### C9. Captions beside images, rules, frames: the magazine object

- **Captions:** "When I place captions on either the left or right of an image, I
  immediately give designs the look of a magazine" [stated, #12].
- **Rules:** hairlines or heavy rules above and below modules (#1), vertical rules
  bracketing type blocks (demo 3), rules under stats like a gauge (demos 14, 28)
  [observed].
- **Frames:** thick and sometimes asymmetric poster frames (demo 34 cream 10 px, 36
  cream 30 px, 37 red top and left with charcoal bottom and right, 39 charcoal 40 px)
  [observed].
- **Default instead:** caption under the image, cards with shadows, no rules.

### Type

#### T1. Type as the image

- **Giant numerals with a small light unit** (6.3gallon, 40mpg, 7,450ddm, 3,096,999),
  with the unit sometimes set vertically beside the numeral (#9, demo 14, demo 28)
  [stated + observed]. It replaces the stats row of icon cards.
- **Vertical type as a column or stripe:**
  - Brody's headline in a 6rem column, reading bottom-up (#6);
  - Lubalin's tri-colour vertical words packed against a list (#8);
  - McBain's paragraph turned into a stripe between rules (#11);
  - Thompson's vertical caption over overlapping figures with `difference` (#12, demo
    5);
  - Sutnar captions as thin vertical rules framing the image (demo 10).

  "While vertical text won't suit every design, it can turn a short passage into a
  strong visual statement" [stated, #12].
- **Letters as structure:**
  - V-E / S-P / A split across a striped gutter (demo 39);
  - a giant cropped "A" sliced by a colour strip (demo 17);
  - the page masked as a letter (demo 24);
  - a vertical "TRANSIT" filling a column (demo 35);
  - images inside letter shapes (#8).
- **Text as the object:** copy tilted in 3D to become a road under the car (demo 9); text
  inside a silhouette (demo 27); repeated words masked into a van (#12).
- **Pre-formatted display blocks:** one family in black and light weights, negative
  tracking, tight leading, explicit line breaks applied only on large screens (#8).
  "Expressive typography needn't need fancy fonts" [stated, #8].
- "Every typographic element, no matter how small, is an opportunity" [stated, #9,
  shortened].
- **Fits:** strongest move for businesses with little photography. For Thai: vertical
  Thai script reads poorly and is rarely used, so vertical type should be Latin
  numerals, dates or short brand words [our inference]. Giant numerals (prices, years,
  counts) work in any script.

#### T2. Magazine anatomy as the content model

- **Components:** running head, folio, headline, byline, standfirst, lede, caption, pull
  quote, body and subhead, each mapped to an element [stated, #3]. Content is written
  for those slots, not for "hero / features / CTA".
- **Recurring text habits** [stated + observed]:
  - indented paragraphs with no paragraph spacing, giving "solid blocks" (#6, #11, #12,
    demo 38);
  - a styled first line (`::first-line`);
  - drop caps (`initial-letter`) and giant initials that fill a column width (#1);
  - italics for speed (#2);
  - justified narrow columns.
- "Attention to even the smallest details of typography lets people know that every
  aspect of a design has been carefully considered" [stated, #11].

### Colour

#### K1. Three hues, tints and shades, one accent per story

- "My palettes rarely contain more than three hues; a dominant color, secondary or
  supporting color, and an accent", plus neutrals, with darker shades for borders and
  lighter tints for highlights [stated, #10].
- **Per-story accent sampled from that story's photograph:** applied to headline, drop
  cap, pull quote, dates and panel, while layout and type stay fixed [stated, #2 and
  #3]. Foundation styles are the constant; colour is the per-story variable [stated, #3].
- **Variants:** he shows the same layout in monochrome and in full or split-complementary
  colour to show how the feeling changes (#10, #11, #12) [observed].
- **Process colour on screen:** to make a process colour in RGB, set two channels to
  maximum and add black if it is harsh [stated, #12].
- **Dark mode:** brighten about 10%, use off-white text, do not invert [stated, #10].
- **His recurring palette** across the demos: mustard `#f2c867`, crimson `#a73448` or
  `#ab4337`, black, off-white, one blue (`#4697cd`) [observed, digest D].
- "The colors we choose should tell a story about a company ... as eloquently as our
  layout or typography" [stated, #10].

### Small screens

His statements and his builds disagree here, so both are recorded.

#### S1. Storyboard small to large before building

- "To help me design a consistent experience across screen sizes, I form a storyboard
  from a short series of sketches" [stated, #4]. He repeats it in #7, #9 and #12
  [stated].
- The storyboards show the same elements at about 320, 768 and 1280 px, with only the
  arrangement changing [observed, #4 br-19, #9].

#### S2. Horizontal scroll strip instead of shrinking or stacking

- "Instead of resizing images, so they fit within a narrow viewport, I often allow them
  to spread beyond it and add a horizontally scrolling panel", one of his favourite
  devices [stated, #7].
- Used in #3, #4, #5, #7, #10 and #12, and in demos 7, 31 and 35 [stated + observed]:
  - a tall image rotated on its side inside the strip (#3);
  - the scatter kept as a swipeable strip with alternating tilts (#4);
  - `row-reverse` so each car's nose points into the scroll (#5).
- **Fits:** galleries, menus and product ranges on phones. A visible next item or scroll
  bar signals there is more [stated, #5].

#### S3. Art-directed image swap, not a scaled copy

- `<picture>` swaps in a different crop, orientation or drawing per size
  [stated + observed]:
  - a re-cropped scooter that bleeds off alternate sides (demo 1);
  - portrait versus landscape chosen by an `orientation` query (#5);
  - a whole car for phones and a half car for desktops (#8);
  - the whole Mini replacing the abstract crop (demo 32);
  - a single badge replacing the echo row (demo 28);
  - a horizontal "TRANSIT" over one van (demo 35);
  - an alternative mask "preserves the visual weight" (#12);
  - a rotated scooter (demo 5).
- "Shrinking a landscape image to fit a portrait orientation decreases its visual weight
  and impact" [stated, #5].

#### S4. Keep the ratio, not the size

- To "maintain a similar contrast in scale on small screens", the wheel header is fixed
  at `33vh` with `33vh` of space below it, and the header image is capped at `75vh` so
  text starts on the first screen [stated, #5].
- "When you use images to add drama, make sure their effect is dramatic on all screen
  sizes" [stated, #5].
- In #12 he does the opposite: graphics shrunk to 25vw or 50vw "to add white-space and
  visual interest", because "some space needs to remain empty" even on phones [stated].

#### S5. Carry a token of the device when the device cannot fit

- The colour slabs become three palette circles (demo 6) [observed].
- Pintori's overlapping squares become one square behind each stacked block (#10, demo
  16) [stated + observed].
- McBain's slabs move into the header's colour and clip-path: "those brightly coloured
  blocks would dominate the limited space ... Instead, I add the same bright colours to
  my header" [stated, #11].
- The mirrored halves become two stacked full-height panels (#7) [observed].

#### S6. Small layouts can still have columns

- An empty narrow column keeps text indented at 390 (#3) [observed].
- A `3rem 1fr 3rem` phone grid gives layering from the start (#6) [stated].
- Mini two-column grids alternate the illustration side between sections (#12): "It's
  sometimes beneficial to use more than a single-column layout for small screens"
  [stated].
- "There's no need to fall back on predictable, single-column designs for small
  screens" [stated, #3].
- Demo 3 keeps its stagger as alternating left and right margins [observed].

#### S7. Each breakpoint is its own composition

- 48em is not a squeezed desktop. Examples [stated + observed]:
  - a symmetrical 3-column tier with no skinny column (#1);
  - a vertical scatter for portrait (#4);
  - a 2x2 grid with vertical text (#7);
  - the grid on but the arrows off (demo 26);
  - the area grid without rotation (demo 37).
- He uses "tweakpoints" for small in-between fixes, crediting Jeremy Keith [stated, #11].
- "Each breakpoint provides an opportunity" [stated, #6]. "Responsive design not as a
  challenge, but as a chance to be creative" [stated, #6 and #11].

#### S8. What his builds actually do below 48em

- **What gets dropped:** in the 40 demos, most of the showpiece device is added only at
  48em or 64em. Below that the page is a plain stack, and these are lost [observed,
  digests A to E]:
  - rotation (demos 4, 33, 37);
  - vertical type (10, 20, Lubalin);
  - perspective (9);
  - overlap and multiply (7, 16);
  - letter masks (24);
  - beams (10, 25);
  - arrows (26).
- **What survives at 390:** palette, display type, crop and bleed, rules, scale contrast,
  and text wrapping round shapes (demo 1). Designs built as SVG type art or as
  proportional `vw` columns keep everything: demos 14, 19, 35, 36 and 39 [observed].
- **Contradiction:** this clashes with his stated "no need to fall back on predictable,
  single-column designs" [stated, #3]. The Smashing articles, where he designs the phone
  version deliberately, are better evidence of his small-screen method than the weekly
  demos, which read as sketches made at one a week [observed].
- **Lesson for us:** decide which single device must survive on phones, then build it in
  a phone-native form (S2 to S5, or SVG art, or vw-proportional tracks). Leaving it to
  vanish at 64em is the failure case [our inference].

---

## 2. Process and thinking

- **Why the series exists:** he says his interest in web design waned; the web had
  "stagnated, predictability had replaced creativity, and ideas seemed less important
  than data" [stated, #1]. Working with newspaper designer Mark Porter got him into art
  direction and editorial design, and studying magazines brought his enthusiasm back
  [stated, #1].
- **How he collects:**
  - He buys varied magazines, rarely two issues of one title, and photographs pages of
    magazines he does not buy [stated, #1 and the bookcase post].
  - He decides within "a few page turns" whether a magazine has an exciting layout, an
    inspiring typographic treatment, or an innovative image-text combination [stated, #1].
- **The four-step method** [stated, launch post]:
  1. Examine an influential designer or piece.
  2. Teach the principles that make it exceptional.
  3. Apply those principles to the web.
  4. Describe the code.

  In practice each issue names two to four "distinctive design threads" in the source
  (for Avaunt: a stencil serif with a geometric sans, black/white/red, modular contents
  page), then turns each into one web move [observed].
- **Fixed foundation, varied surface:** a well-defined set of foundation styles (body
  type, rules, drop caps, captions, image treatments) is what lets pages vary in colour,
  layout and display type and still feel like one publication [stated, #1 and #3]. "It's
  just as important to create a connected experience across screen sizes as it is across
  media" [stated, #3].
- **Pacing across pages:** he cites Brodovitch laying spreads on the floor to pace the
  magazine [stated, #4] and Feitler: "You can't look at one page alone, you have to
  visualize what comes before and after" [reported, #5]. He wants page-to-page rhythm,
  "which I very rarely see online" [stated, #1].
- **Constant subject, variable art direction:** across 40 demos the subject is always a
  classic European vehicle (Vespa, Mini, Fiat 500, Citroën DS, Trabant, Ford Transit,
  Morris Traveller), with the same fact copy reused. This isolates art direction as the
  only variable [observed]. Turning "the worst car ever made" (the Trabant) into a
  glamorous subject is the point of the Huber issue: mundane subjects can become exciting
  visual communication [stated, #9].
- **Sketch, storyboard, then code:** sketches first, then a small-to-large storyboard,
  then semantic HTML with minimal markup; decoration goes into pseudo-elements, generated
  content, SVG and data URIs. "Elements needed to develop a design needn't be in HTML"
  [stated, #11]. He changed his mind on SVG text: "I was wrong" to think it
  inappropriate [stated, #11].
- **Attitude:**
  - "Graphic design principles matter as much to a digital medium as they do for print"
    [stated, #4].
  - "Learning how people interact with a website ... shouldn't dictate a design but
    instead provide a platform" for memorable experiences [stated, #12].
  - He quotes Pintori: "logic and imagination in equal measure" [reported, #12].
  - He quotes Brody: "question everything" [reported, #6].
  - He quotes Ruth Ansel: "step outside of what is expected" [reported, #12].
  - On Brody: "we're told to not make someone look more than once ... [his work] makes
    people look twice" [stated, #6, trimmed].
- **Audience:** in the McBain issue a design must resonate with and sell to the people
  it is for; art direction is framed as social equity [stated, #11].
- **Client process:** not covered in this series. It is about translating sources, not
  about client discovery [observed].

## 3. Taste

- **Heroes** [stated]:
  - Brodovitch, "the most substantial influence on the work I make for the web" (#4);
  - Feitler and Ruth Ansel; Lubalin; Brody and The Face (which he grew up with in Corby,
    #6);
  - Storch, whom he wants more web designers to know (52-weeks launch post);
  - Aaron Draplin ("a personal idol"), House Industries and Mondo posters (bookcase
    post).
- **Reading** [stated, bookcase post]:
  - Eye (#96 "Anatomy of a Magazine"), BranD, Lagom;
  - corporate standards manuals (NASA, British Rail, NYCTA, CBC), which he links to
    design systems;
  - Magma bookshop.
- **Dislikes** [stated]:
  - framework sameness: "Bootstrap doesn't create unimaginative designs. Lazy designers
    do." (#3);
  - flat design's "regrettable uniformity" (#5);
  - one-to-four-block layouts (#1);
  - complex build tools that displaced the "simple pleasure of writing HTML and CSS"
    (#1);
  - data and usability being allowed to dictate design (#12).
- **Recurring look** [observed]:
  - flat vector drawings and line art of objects rather than photography;
  - mustard and crimson with black, off-white and one blue;
  - heavy condensed caps and stencil or high-contrast serifs;
  - justified narrow columns with indented paragraphs;
  - rules and thick frames;
  - mid-century and modernist sources (1930s-1980s), with British mod and scooter
    culture as a personal thread (Vespa, Mini, The Italian Job).
- **Humour** [observed]:
  - the Trabant presented as glamorous;
  - labels fanned out as wasp legs (demo 33);
  - "!!" set as a graphic (demo 36);
  - a hover that straightens tilted cards (demo 13);
  - Michael Caine pasted over a Mini headline (demo 8).
- **Colour:** he says colour is the hardest part of design for him and that he leans to
  monochrome plus one accent [stated, #10]. His demos are nonetheless almost all strongly
  multicoloured [observed].
- **Accepted costs:** some reading cost for impact. Examples are very short wrapped
  lines, a pale-grey headline (demo 2), a near-invisible dotted headline (demo 15), and
  copy inside SVG lockups (demos 35, 37). He mitigates with `backdrop-filter`, text
  shadows and `@supports` [stated + observed, digest B].

## 4. Open questions

- **The book:** no Smashing book named "Inspired Design Decisions" could be found. The
  #12 article promised "the book which will follow it". Whether that became the PDF
  magazine set, *Art Direction for the Web*, or *Standout Designs for the Web* is
  unverified.
- **Webinar transcripts:** the 11 transcripts on Smashing TV are behind a members' login.
  They likely hold his spoken reasoning and Q&A answers (process, client work) but were
  not read. The PDF magazine issues (£3.99) were not bought either.
- **CodePen:** no CodePen collection for the series turned up. The demos live on his own
  site. A CodePen account (handle presumably "malarkey") was not checked pen by pen.
- **Live demos have drifted:** the demos now run inside the current Stuff & Nonsense site
  shell, and some fonts and CSS variables have changed or broken:
  - demo 12's compound-grid variable is undefined;
  - demo 10's vertical text collides with the headline;
  - demo 21 has lost its main pink block;
  - demo 30's image covers its subtitle, and we cannot tell if that is deliberate;
  - demo 18's phone caption is invisible;
  - demo 5's text is about Lustig.

  Where a live page and his own `preview.png` disagree, the digests describe the
  preview, so some descriptions rest on a 1440x1024 still image rather than a working
  page.
- **Viewport-dependent compositions:** many demos size in `vh` (`min-block-size: 90vh`,
  `background-size: cover`). Our tall screenshots exaggerate empty space; the realistic
  first-screen shots should be trusted instead. We did not verify each demo at a true
  390x844 phone.
- **Weak reasoning for the weekly demos:** the 52-weeks posts carry no reasoning, so any
  intent attributed to demos 6-40 beyond what the Smashing articles say is our
  inference.
- **Stated versus built on phones:** we cannot tell from public material whether he sees
  the demo phone fallbacks as acceptable sketches or as his real practice. Client sites
  (other streams) would settle it.
