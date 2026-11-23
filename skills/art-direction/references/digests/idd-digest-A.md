# IDD digest, group A: Avaunt, Pressing Matters, Ernest Journal, Brodovitch (+ demos 4, 21)

Marks: [stated] Andy says it; [observed] I saw it in an image, screenshot, or the page
CSS; [reported] someone else says it. Article images are in `raw/idd/img/` with prefixes
`av-`, `pm-`, `ej-`, `br-`; demo page text, CSS and blog text are in `raw/idd/pages/`.

Sources:

- AV https://www.smashingmagazine.com/2019/06/inspired-design-decisions-avaunt-magazine/
- PM https://www.smashingmagazine.com/2019/07/inspired-design-decisions-pressing-matters/
- EJ https://www.smashingmagazine.com/2019/08/inspired-design-decisions-ernest-journal/
- BR https://www.smashingmagazine.com/2019/09/inspired-design-decisions-alexey-brodovitch/
- D4 https://stuffandnonsense.co.uk/inspired-design-decisions/4/ (27 Jan 2020)
- D21 https://stuffandnonsense.co.uk/inspired-design-decisions/21/ (25 May 2020)
- B4 https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-4-alexey-brodovitch/
- B21 https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-21-alexey-brodovitch/

(The first line of each AV/PM/EJ/BR text file holds its URL; month segments above are
from those files' URL lines.)

---

## 1. Avaunt magazine (issue 1): skinny columns and modular grids

### Source

- Avaunt (adventure/culture/style quarterly; launch art direction Matt Willey). What drew
  him [stated]: diverse use of colour, layout and type while keeping a consistent feel;
  a stencil serif (Avaunt Stencil, A2-TYPE) plus a geometric sans (MFred), with a strict
  black/white/red palette and Antwerp for running text holding the variety together.
- Contents page on a four-column modular grid "keeps content ordered within spacial zones
  but maintains energy by making each zone a different size" [stated].
- "Cold War Design" spread (issue 7, Jan 2019) [observed, `av-cold-war-design.png`]: the
  verso has a narrow text column on the left (intro, headline "Cold War Design", body,
  numbered index list in red), and to its right a 2-wide stack of object modules. The
  recto is a 3-column module grid in which the Tokamak object takes a 2x2 zone. Every
  module has a hairline rule above and below it, and each module carries a small centred
  number. He notes that the modules on the verso fuse into a single text column, but the
  module proportions still set the positions inside it [stated].
- Giant initial: a red stencil "O" that fills the full width of the text column and about
  60% of its height, then running text starts under it; a full-bleed dark portrait takes
  the rest of the spread [observed, `av-avaunt-magazine-spread.png`]. He names "giant
  initial caps which fill the width of a column" as a move [stated].
- Takeaways he names [stated]: modular grid without static feel; a fixed set of
  foundation styles allows diverse pages; rhythm across a sequence of pages.

### Move A1: Skinny ("bastard") column

- What [stated]: add one extra narrow column to an otherwise conventional column grid.
  In print it is a "bastard column/measure"; he renames it "skinny".
- Construction: the skinny column is exactly half a standard column [stated: "Splitting
  the final column, then adding half its width to another"]. The large-screen grid is
  `grid-template-columns: 1fr repeat(4, 2fr)` (skinny first), or
  `2fr 1fr 2fr 2fr 2fr` (skinny second). The grid is 4.5 standard columns wide, so the
  skinny column is 1/9 of the width [observed from the values].
- What it is used for, each shown as a Mini Cooper layout on grey column stripes
  [observed, `av-examples-of-skinny-columns.png`, `av-skinny-column*.png`]:
  1. Image sizing: one column is too light and two are too heavy; one standard column
     plus the skinny one (1.5 units) "creates the perfect space for my image" [stated].
     The figure shows three rows of the same 4-col layout: the image at 1 column, at 2,
     and at 1.5, with the caption pushed into the leftover half column.
  2. Element sizing: the Mini Cooper logo is exactly the skinny column's width
     (`av-skinny-column.png`: light-grey skinny column at far left with the logo; headline
     in a large serif spanning columns 3 to 5; standfirst wide; body in 1 column; caption
     in column 2; car front view in columns 4 and 5).
  3. Measure: standard plus skinny gives a better line length for running text
     (`av-skinny-column-2.png`: logo, headline, standfirst and body text all in skinny
     plus first standard column, 3 lines of headline; three car views in the remaining 3
     columns, side view across 3, top view across 2, front view in 1).
  4. Empty skinny column as white space and asymmetry: an empty skinny column placed
     between two standard columns "allows the eye to roam" and makes the layout "more
     dynamic and energetic" [stated] (`av-skinny-column-6.png`: logo and a large
     standfirst in column 1, then an empty light-grey skinny column, then headline and
     three text columns).
  5. Carved gutter: an empty skinny column forms a wide gutter that confines text to one
     column whose height echoes a tall portrait image (`av-skinny-column-4.png`: a large
     top view of the Mini filling the left three columns, an empty pale skinny column,
     then all text in the last column).
- Default it replaces: equal 12/4/3-column framework grids where blocks snap to 1, 2,
  3 or 4 columns [stated: "one, two, three, or four block arrangements of content became
  the norm"].
- Same HTML, recomposed: he moves the header, figure and article around the same 5-track
  grid to get a "more structured" alternative, with skinny column second and the article
  as 3 CSS multi-columns (`column-count: 3`) [stated].

### Move A2: Modular grid with spacial zones

- Construction [stated]: 6 symmetrical columns by 4 rows at large size; modules bound
  together into "spacial zones". Final large layout (`av-modular-grid-design.png`,
  `av-modular-grid-3.png`) [observed]: column 1 is a full-height sidebar (intro paragraph,
  bold 5-line stacked headline "They said it would never sell", body text, a bold-year
  model list) separated by a vertical hairline; columns 2 to 6 hold 14 blueprint modules.
  Row 1: logo, front, rear, side view (2 wide). Row 2: top view (2 wide), a 2x2 top view
  (columns 4 and 5, rows 2 and 3), front view. Rows 3 and 4 continue the pattern. Each
  module has a heavy rule above and below, and a bold centred year label (the same device
  as Avaunt's numbered modules).
- CSS shape [stated]: `grid-template-columns: repeat(6, 1fr)`; sidebar at
  `grid-column: 1; grid-row: 1 / -1`; items placed with `nth-of-type` and `span 2`. An
  alternative uses `grid-template-areas`, with `.` for an empty module and repeated names
  for zones.
- He keeps the markup to an `article` plus an `ol` ("blueprints are in date order") and
  uses `display: contents` [stated]. He warns that `grid-auto-flow: dense` reorders the
  view against the source, which may affect accessibility [stated].
- Default it replaces: a uniform card grid. The point is unequal zone sizes inside a
  strict module set, with boundary rules making the structure visible.

### Small screens (Avaunt)

- Below 48em: no grid; normal flow, single column [observed from the code: every grid is
  inside `min-width: 48em` or `64em`].
- 48em: a symmetrical 3-column grid with no skinny column; the header spans all columns;
  the article is set in 3 CSS columns; the image takes columns 2 to 3 and the caption
  column 1 (`av-skinny-column-5.png`: headline across all 3, logo centred in column 2,
  text in 3 columns, large car front view lower right with its caption bottom-left)
  [stated + observed]. The skinny column arrives only at 64em [stated].
- Modular grid, 48em: 3 columns; the article spans the full width at the top (headline in
  one line, 2-column text, the list in 2 columns), then the modules, with some spanning 2
  columns and one spanning 2 rows. `dense` fills the holes (`av-modular-grid.png`,
  `av-modular-grid-2.png`) [observed]. At 64em the article becomes the full-height
  sidebar [stated]. `av-modular-grid-4.png` shows the medium and large versions side by
  side [observed].
- Media-query-free version [stated]: body becomes a flex container with wrap; the article
  `flex-grow: 1` plus a flex-basis, and the list `flex-grow: 999; min-width: 60%`, so
  the sidebar drops above the list when the list would go below 60%. Inside the list:
  `repeat(auto-fill, minmax(10rem, 1fr))` plus `dense` and the same span rules. He calls
  this closest to "a truly responsive web" [stated].

### Quotes (AV)

- "For what feels like an eternity, there's been very little innovation in grid design
  for the web." [stated]
- "An empty skinny column adds whitespace which allows the eye to roam around a design."
  [stated]
- "When you use modular grids thoughtfully, they can fill your designs with energy."
  [stated]

---

## 2. Pressing Matters (issue 2): compound grids, rhythmic patterns, pacing

### Source

- Pressing Matters (printmaking magazine; creative director John Coe). Taken [stated]: a
  limited palette in which headline colours are picked from nearby prints ("a design
  which feels connected"). Layout patterns build a rhythm through the magazine: "differently
  sized modules speed you past pages packed with prints, then the pace slows" on large
  reproductions. He found a layered 2+3 compound grid running through it, and ties layered
  grids to layered ink [stated].
- `pm-05-pressing-matters.png` [observed]: the verso is a 3-column top band (an
  illustration tile, a red block with a stacked 3-line headline "MATCH BOX MAGIC", a
  photo), a 2-column running-text band below on beige with a drop cap, then a photo across
  2/3 with a credit panel in the last 1/3. The recto is a masonry of matchbox labels in 3
  columns with uneven heights. So the text runs on 2 columns while the images run on 3,
  which is the 2+3 compound grid.
- Karl Gerstner's 1962 Capital "mobile grid": 58 units, from which the page can be divided
  into 1, 2, 3, 4, 5 or 6 columns and rows with constant gutters. He decodes it division
  by division: 1 module is full width; 2 is "reassuring symmetrical"; 4 is "formal ...
  serious"; 5 with a flowline "feels more technical"; 6x6 gives the most variety
  [stated]. `pm-26-pressing-matters.png` shows 1x1 to 6x6 red module grids [observed].
- Capital's large facing images slow reading down [stated].

### Move A3: Compound grid (layered)

- Definition [stated]: two or more grids of any type on one page, occupying separate
  areas or overlapping. The column tracks you get are the union of both grids' lines.
- How the patterns come about [observed: the arithmetic checks out for 2+3, 3+4 and 4+6]:
  - 2+3 on 6 units: lines at 0, 2, 3, 4, 6 give **2|1|1|2**, so
    `grid-template-columns: 2fr 1fr 1fr 2fr` [stated].
  - 3+4 on 12 units gives **3|1|2|2|1|3**, so `3fr 1fr 2fr 2fr 1fr 3fr` [stated].
  - 4+6 on 12 units gives **2|1|1|2|2|1|1|2**, so `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`
    [stated]. "Of all the possible grid combinations ... the one I use most often"
    [stated]. In the Brodovitch issue he calls the same grid "6+4" [stated].
  - 4+5: he gives **6|1|4|3|3|4|1|6** [stated]. The arithmetic does not support it: 4+5
    on 20 units gives 4|1|3|2|2|3|1|4 [observed]. His numbers sum to 28 and are not
    symmetric to either grid. In `pm-22-pressing-matters.png` the stripes look like 8
    columns with two very narrow ones, consistent with the 20-unit version. Treat his
    pattern as a typo.
- He states that the narrow 1-unit columns are "perfect for informing the size of
  typographic elements including this bold drop cap" (the same idea as the skinny
  column).
- Rhythm framing [stated]: equal columns are an even beat ("tap twelve of them on your
  desk"); compound patterns are a syncopated rhythm, which changes the mental model.
- Default it replaces: the Bootstrap 12-column grid; nine in ten of his students draw 12
  equal columns when asked to sketch a grid [stated]. `pm-07-pressing-matters.png`
  shows the "unimaginative Bootstrap" strawman [observed].

### The worked layouts (all one Jaguar E-Type story, grey stripes show the columns) [observed]

- `pm-18` 2+3: headline (heavy black grotesque, 2 lines), standfirst and body text in
  columns 1 and 2 (half the page). The car side view across columns 3 and 4. The three
  Series boxes (bold italic years) in column 4 only, which is a third of the page. The
  car "crosses the remaining space" to connect the two halves [stated].
- `pm-19` 2+3 "movement" version: the car at top left, a one-line italic headline across
  the full width, the standfirst starting at line 2 (one third in), body text starting
  at line 3 (half), and the Series list in column 1. The left edges step diagonally to
  the right, a staircase. Italics carry speed [stated].
- `pm-20` 3+4: the car starts at the left edge of the stripes, the headline starts at a
  4-grid line, the standfirst further right, body text further right again. The pull
  quote sits bottom-left in bold italic. Another staircase: the standfirst starts on the
  3-col grid and the body text on the 4-col grid [stated].
- `pm-21` 3+4: the text column width is made of units from both grids so that it matches
  the width of a tall vertical image [stated].
- `pm-22` 4+5: the main text is in two columns whose widths combine 4 and 3 units; a
  bold drop cap sits in a 1-unit column; a narrow Series sidebar on the far right
  [stated + observed].
- `pm-23` 4+5: three text columns, each starting on a different grid; the supporting
  Series info is on the 5-col widths with hairline dividers; a rear view of the car in
  the corner [observed].
- `pm-24` 4+6: the car image fills almost the whole width; a "solid block" of text sits
  under its wheels, its width taken from both grids [stated].
- `pm-25` 4+6: the car sits in the centre and the running text wraps around it on both
  sides (CSS-Shapes-like). The standfirst is limited to the left half, leaving the top
  right empty to form a "dynamic diagonal" [stated]. "It's not necessary to fill every
  grid module with content" [stated].
- `pm-27` 4+6: a pull quote one 6-grid column wide "feels disconnected"; aligning its
  edge to 6-grid lines fixes it [stated].
- `pm-34` final coded 4+6 [observed + stated values]: headline, standfirst and main are
  at `grid-column: 4 / 8`. On the 12-unit scale that spans units 4 to 10, half the page,
  starting a third in and stopping one 2-unit column short of the right edge. The car
  is at `2 / -1` (from unit 2 to the edge, a bleed-right image wider than the text). The
  aside is at `1 / 3` (the first quarter) with `align-self: end`, so the Series list
  hangs at the bottom-left beside the body. Gaps are `2vw` columns and `2vh` rows. The
  first line of the first paragraph is styled and later paragraphs are indented, both
  via selectors, with no classes.

### Move A4: Stacked grids to separate stories

- When a page holds two stories, give each its own grid [stated]. `pm-28`: E-Type story
  on 4 columns on a pale band, Le Mans story below on 6 columns over grey, separated by a
  rule; the second story uses paragraph spacing instead of indents [stated + observed].
  `pm-29`: a 4-column story above a modular grid of a 6x2 Le Mans timeline, with years as
  bold italic module heads [observed].
- Default it replaces: one grid for the whole page, with stories separated only by
  headings.

### Move A5: Pacing with module size

- "Repeating smaller modules speeds up the movement, while larger ones slow it down"
  [stated]. Use a large zone at chosen moments in a journey to make people stop
  [stated]. This applies across pages as well as within one page.

### Small screens (PM)

- Not discussed. The compound grid sits inside `min-width: 48em` "as I don't want these
  styles applied at smaller screen sizes" [stated], so small screens get normal-flow
  single column [observed from the code]. There is no intermediate collapse of 8 to 4
  columns: the article shows no 2-col or 4-col tier.

### Quotes (PM)

- "Does Bootstrap create unimaginative designs? No, people do." [stated]
- "Think of each column as a beat and tap twelve of them on your desk." [stated]
- "Remember, it's not necessary to fill every grid module with content." [stated]
- "People naturally spend longer looking at larger spacial zones" [stated]

---

## 3. Ernest Journal (issue 3): connected variety on a plain 12-column grid

### Source

- Ernest Journal (small-format "journal for enquiring minds"). Taken [stated]: "simple,
  but not minimal"; most value from few assets (Freight Big Pro high-contrast serif and
  Gill Sans Nova); mostly 2 and 3 columns, "thoughtful use" keeps it connected; per-
  story accent colour picked from that story's photo/graphic.
- Magazine anatomy as component names [stated]: running head, folio, headline,
  byline/credits, standfirst (deck, intro or kicker), lede, caption, pull quote, body,
  sub-head. He maps each to an HTML element or class.

### Move A6: Use the framework grid with imagination, and vary the layout story to story

- Framing [stated]: "Bootstrap doesn't create unimaginative designs. Lazy designers do."
  Ernest's grid can be reproduced with 12 framework columns; what makes the difference is
  a system for using 1, 2 and 3 columns. His terms [stated]: 1 column looks "classical",
  2 "orderly", and 3 or more with white space "editorial".
- Worked designs (Fiat 500 story) [observed]:
  - `ej-6`: a dark panel with the image takes 8/12 columns and bleeds off the page edge,
    with a huge condensed all-caps headline stacked 5 lines inside it and a standfirst at
    the bottom. Running text is in a 4/12 column on the right with a large drop cap, a
    model list and a pull quote. The 4-column standfirst width echoes the text column to
    balance the asymmetry [stated]. Panels "will have more impact when you allow them to
    bleed off the edges of the page" [stated].
  - `ej-7`: a tall top-view image at 6/12 and full height (left half), running text in
    2/12 in the centre, a darker supporting panel on the right whose content stays 2/12
    wide inside a wider box. Sans-serif type and a different background separate the
    supporting content [stated].
  - `ej-9`: three text columns, images in two halves. `ej-10`: two text columns, images
    in thirds. Rule [stated]: pick a system per publication, e.g. 3 columns for text and
    2 for images, or the reverse; repeating 3 image shapes "helps a composition to feel
    more dynamic".
  - `ej-11`: an image across 2/3 plus an image in 1/3 above 2-column text. "Image
    proportions are not nearly as interesting as the position of the gutter between
    images, and how it offsets the gutter between running text columns below" [stated].
    Offset gutters are the point: the image gutter falls at 1/3 while the text gutter
    falls at 1/2.
- Gerstner-style variants on the same 12 columns [observed]: `ej-13` uses a single
  module, with a quarter of the composition left as white space "to give this design a
  feeling of luxury" [stated]; the car front view is huge and text is in a narrow right
  block. `ej-14` uses 2x2 modules, one car per module, with headline and paragraph starts
  staggered by one gutter/column ("use gutters to stagger the start") [stated]. `ej-15`
  uses 3 columns in two ways. `ej-16` is an odd 5x5 modular grid of line-icon tiles with
  the title block occupying a 2x1 zone; he describes it as a rhythm interrupter "so
  different from other pages" [stated].

### Move A7: Reading-rhythm ladder (also a mobile rule)

- Six speeds on a phone [stated + observed `ej-17`..`ej-22`]: slowest = one module that
  fills the screen (a card of top view, title and deck); slower = 2 equal modules;
  slow = 3; fast = small modules; faster = 5 visible; fastest = many tiny modules, which
  is "ideal for mobile navigation" (the Wheel Man menu list).

### Move A8: Accent colour sampled from the story's image

- One accent, or tints of it, per article, sampled from the dominant image, applied to
  headline, standfirst, timeline dates, drop cap, pull quote and panel background
  [stated]. `ej-26`: warm brown sampled from a suitcase in the photo drives a large
  display headline, drop cap, pull quote and a full-height dark-brown timeline panel; the
  photo takes the centre third of the spread [observed]. He also changes the full-page
  background colour per article while keeping layout and type fixed [stated]. Foundation
  styles (block quotes, dates, drop caps, borders, image treatments) are the constant;
  colour and type variation is the per-story variable [stated]. He flags contrast
  checking [stated].

### Small screens (EJ), the most explicit in this group

- "Proportionately narrow columns of text don't make sense when space is limited, so I
  use the entire screen width" [stated].
- Rotate the tall image and scroll it sideways: "instead of asking people to flick past a
  tall image, I place the Fiat 500 on its side within a horizontal scrolling panel"
  [stated]. `ej-8` [observed]: phone view with the top view turned 90 degrees to
  landscape inside a dark panel with a visible scroll indicator, then drop-cap text full
  width; the second screen keeps the dark supporting panel as a full-width block.
- `ej-12` [observed]: at medium, 3 images in 3 columns over 2 text columns (the offset
  gutters survive). On the phone, the images become a horizontal scroll strip (with a
  scroll bar), and the running text is indented by a narrow empty column on the left, so
  white space survives even at 390.
- "There's no need to fall back on predictable, single-column designs for small screens"
  [stated].
- Reading-rhythm ladder above is framed as equally valid on mobile [stated].

### Quotes (EJ)

- "Bootstrap doesn't create unimaginative designs. Lazy designers do." [stated]
- "There's no need to fall back on predictable, single-column designs for small
  screens." [stated]
- "It's just as important to create a connected experience across screen sizes as it is
  across media." [stated]

---

## 4. Alexey Brodovitch (issue 4) and demos 4 and 21

### Source

- Brodovitch (Harper's Bazaar 1934 to 1958, Portfolio 1949 to 1951). Taken [stated]: his
  precision in bringing photos and text together; unexpected crops; off-centre placement
  and bleeds "to create compositions which were full of energy and movement"; text shaped
  by forms in the photograph; bold colour blocks; sketching layouts, then laying spreads
  on the floor to pace the magazine; "astonish me"; intolerance of mediocrity. He calls
  Brodovitch "the most substantial influence on the work I make for the web" [stated].
- Sources shown [observed]: `br-04` (1934 "Fine Figger of a Woman"), `br-10` (1954 "This
  Spring", Lillian Bassman), `br-12` (1938 "If you don't like full skirts"), `br-14`
  (1936 "Consensus of Opinion", Man Ray), `br-16` (Portfolio Pollock spread), `br-17`
  (Portfolio William Steig). D4 inspiration (`demo04-inspiration.jpg`): a Bazaar spread
  where two strips of dance photos (a vertical film strip plus a diagonal one) form a
  tilted "Y" and the text block is rotated with them; a huge cut-out dancing couple is
  turned 90 degrees on the facing page. D21 inspiration (`demo21-inspiration.png`): the
  Steig "Sleepwalker / Tough guy" spread, a black block lower-left with a white-line
  figure, a translucent magenta rectangle laid over each figure's head, and a white
  right page.

### Move A9: Scattered pictures (playing-card scatter)

- Four differently sized images, rotated and nudged, "deliberately placed" [stated]. Large
  screens: body on the 4+6 grid (`2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`); the figure spans
  `1 / -1` in row 2 and has its own grid `1fr 2fr 3fr 4fr` (each image larger than the
  last); items are aligned to the end and rotated -20, -5, 10 and -20 degrees, with
  translates up to 80 px [stated]. `br-09` Vespa Elettrica [observed]: on black, three
  narrow justified text columns at top, a thin condensed headline in white and cyan, and
  four photos with white borders overlapping and fanning to the right, growing in size,
  with a paint splatter behind.
- Medium: images scattered vertically to keep hierarchy in portrait orientation; large:
  horizontally [stated] (`br-06`, `br-07`).
- Small: "I turn my group of images into a horizontally scrolling panel", rotating the
  images alternately inside it, using `display: flex`, `overflow-x: scroll` and
  `max-width: 100vw` [stated]. The scatter survives as a swipeable strip rather than
  stacking [observed in `br-06`, which also shows a scroll bar].
- Process: "To help me design a consistent experience across screen sizes, I form a
  storyboard from a short series of sketches" [stated]; he repeats this for the Steig
  design (`br-19`, a three-width storyboard) [stated + observed].

### Move A10: Mirror the two halves (spread as a playground)

- `br-11` [observed]: the viewport is split 50/50. The left half is white with a red line
  drawing of a scooter's top view and grey all-caps text with very loose leading. The
  right half is red with the same drawing in white, flipped 180 degrees. A two-tone
  Vespa logo is centred on the seam, half red on white and half white on red. Colour and
  form invert across the axis.
- Grid [stated]: large `[main] 1fr [aside] 1fr`. Medium uses a 4-track inner grid
  `2fr 1fr 1fr 2fr` (he labels it the "6+4", but the values are the 2+3 pattern
  [observed]) with rows `10rem 200px 10rem auto`, each half `min-height: 100vh`.
  The logo is positioned at `left: 50vw` and shifted to straddle the split. A `picture`
  element swaps in the two-tone logo only at large size [stated].
- Small: normal flow with foundation colour styles, the aside inverted [stated].

### Move A11: Carve text into shapes that echo the image

- `br-13`: a 50/50 layout, the photo on the left, running text whose left edge follows
  the image's curves via `shape-outside: url(mask.svg)` on a floated pseudo-element
  [stated].
- `br-15` [observed]: based on "Consensus of Opinion". The 4+6 grid gives a header at
  `1 / 5` and main at `5 / 9` (halves) [stated]. The line drawing of the scooter is
  rotated 20 degrees; the right-hand text block becomes a slanted parallelogram (both
  edges sheared to match the rotation) via two floated SVG masks, left and right,
  `height: 100vh` [stated]. The red all-caps lead-in sits at the top of the slant.
- Small: a portrait image, swapped to landscape via `picture` when layout styles apply;
  text in normal flow [stated].

### Move A12: Full-height stripes and clipped images (Portfolio)

- Pollock-inspired `br-16` [observed]: the left page is black and cream vertical stripes
  with paint marks. In his web version: logo plus a narrow text column (`1 / 3`, a
  quarter), then an aside at `3 / -1` painted with a 3-stripe gradient (red, white, red);
  three copies of a line-drawn scooter, each clipped with `clip-path` to a third, so the
  drawing changes colour as it crosses each stripe; text overlaps the stripes via
  z-index [stated]. "It retains its personality from small screens to larger ones"
  [stated].
- Steig-inspired `br-17`/`br-19`: black and white columns made with a gradient, clipped
  scooter images, and a circle with `mix-blend-mode: darken` that tints whatever is
  beneath it [stated]. Grid `[main] 1fr [footer] 1fr` at 48em, then `2fr 3fr` at 64em
  [stated]. Storyboard (`br-19`) [observed]: small has logo, scooter, italic serif
  headline, text, then the striped panel with the circle below. Medium is the same stack
  with a larger headline and a bigger panel. Large puts content on the left and the
  stripes plus circle as a full-height right column. The stripes and circle exist at
  every size, and only their position changes.

### Demo 4 (27 Jan 2020): tilted scooter contact sheet

- Live page, 1400 [observed, `demo04b-1400.png`]: inside a white frame, a 12-column grid.
  The left composition sits at columns `1 / 7`, the right panel (pale grey `#F4F4F6`) at
  `6 / -1`, so they overlap by one column and the left sits above (z-index 2). The left
  composition is an inner 5-column grid
  (`repeat(5, 1fr)`, 6 auto rows, 4 px / 2 px gaps) **rotated -15 degrees as a whole**:
  a vertical column of five cropped scooter tiles (column 2) meets a horizontal row of
  three tiles (row 2), forming a tilted "L"/"Y" like the inspiration's film strips. The
  serif body text sits in the crook (columns 3 to 4, rows 3 to 5), rotated with the grid;
  an all-caps sans caption is bottom-left. Each tile is a tight crop of part of a scooter
  (wheel, mudguard), not the whole object. The right panel holds two huge top-view
  scooters, one rotated -15 degrees, the other 70 degrees, crossing like a "T" and
  bleeding off the right and bottom edges. The tiles extend past the left frame edge. The
  colours are pastel (purple, blue, red, mustard) on white and pale grey [observed in CSS
  + shot].
- The live render matches the blog preview (`demo04-preview.png`) [observed].
- Medium, 900 [observed, `demo04c-900.png`]: the tilted tile grid is kept full width; the
  big-scooter panel drops below it. Rotation survives here because the 48em query holds
  the rotate and only the 64em query adds the 12-column split.
- Small, 390 [observed, `demo04b-390.png`]: no rotation. The tiles become a plain 2-up
  grid of cropped fragments (`flex: 1 0 45%`), then the caption in all-caps, the text,
  then the grey panel with the two top-view scooters lying horizontal and stacked. The
  cropping keeps a little of the character, but the composition (diagonal, overlap,
  bleed) is lost. It reads as a gallery.
- Note: the composition depends on viewport height. In a 4000 px tall window
  (`demo04-1400.png`), the frame stretches and the tiles scatter down a very tall white
  column [observed]. That is a capture artefact, but it shows that the design is tuned
  to one screen height.

### Demo 21 (25 May 2020): Steig colour-block overlay, Fiat 500

- Intended design, from the blog preview (`demo21-preview.png`) [observed]: on a 6-column
  grid with rows `340px 1fr`, the header (a black block containing a white-line Fiat side
  view that bleeds off the left) is at `1 / 4` in row 2, so it starts 340 px down and
  leaves the top-left empty. A translucent pink (#BF77AF, `mix-blend-mode: lighten`,
  opacity .5) rectangle is laid over the car's windows. Main is at `4 / -1` across both
  rows, with its own 3-column grid: a solid pink block at `4 / -1` in row 1 behind the
  black-line rear view of the car (the car's roof sits in the pink, its lower half on
  white). The Fiat laurel logo and a small Montserrat caption are in the last column
  only, low down. The small all-caps title "L'EVOLUZIONE DEL MITO" sits above the black
  block. This is the inspiration's structure (black block lower-left, colour rectangle
  over a drawn head, white right page) translated one-for-one.
- Live render, 1400 [observed, `demo21b-1400.png`]: the solid pink block behind the rear
  view is missing (its pseudo-element has `z-index: -1` under the white `#design`
  background), and the title is not visible (the CSS targets `h1`, the markup has `h2`).
  Only the translucent rectangle over the side view shows. Read the design from the
  preview image, not the live page.
- Medium, 900 [observed, `demo21c-900.png`]: no grid below 64em; the black block runs
  full width, then the rear view stacks below.
- Small, 390 [observed, `demo21b-390.png`]: a plain stack of the black side-view block,
  the rear view, a full-width Fiat logo and the caption. The colour-block overlap that
  defines the design is not present (the mobile pink band is again behind the
  background). This is effectively the default stacked mobile layout.
- Blog posts B4 and B21 hold only a sentence and the preview image; they explain nothing
  beyond the Smashing article [observed].

### Quotes (BR)

- "Graphic design principles matter as much to a digital medium as they do for print."
  [stated, BR]
- "Diverse and interesting designs stand out whichever medium you choose to deliver
  them." [stated, BR]
- "To help me design a consistent experience across screen sizes, I form a storyboard
  from a short series of sketches." [stated, BR]

---

## 5. Screenshots taken (all in `shots/idd/`)

| File               | Shows                                                                 |
|--------------------|-----------------------------------------------------------------------|
| `demo04-1400.png`  | D4 at 1400x4000; stretched by the tall viewport (vh artefact)         |
| `demo04-390.png`   | D4 phone view in an 8000 px iframe; same stack as 04b                 |
| `demo04b-1400.png` | D4 at 1400x1000: rotated tile grid over the overlapping scooter panel |
| `demo04b-390.png`  | D4 phone: 2-up cropped tiles, text, horizontal scooters, no rotation  |
| `demo04c-900.png`  | D4 at 900: tilt kept, panel stacked below                             |
| `demo21-1400.png`  | D21 at 1400x4000; stretched by the tall viewport                      |
| `demo21-390.png`   | D21 phone, tall iframe                                                |
| `demo21b-1400.png` | D21 at 1400x1000: black block lower-left, rear view top-right         |
| `demo21b-390.png`  | D21 phone: plain stack                                                |
| `demo21c-900.png`  | D21 at 900: full-width stack                                          |

Supporting downloads: `raw/idd/img/demo04-preview.png`, `demo21-preview.png`,
`demo04-inspiration.jpg`, `demo21-inspiration.png`; demo CSS in
`raw/idd/pages/demo04-css.txt` and `demo21-css.txt`.

---

## Cross-issue patterns seen in this group

- **Grids built from ratios, not equal tracks** [observed]: skinny `1fr repeat(4, 2fr)`;
  compound `2fr 1fr 1fr 2fr`, `3fr 1fr 2fr 2fr 1fr 3fr`, `2fr 1fr 1fr 2fr 2fr 1fr 1fr
  2fr`; Brodovitch `1fr 2fr 3fr 4fr`, `2fr 3fr`. The 4+6 eight-track grid is his house
  grid: it reappears in issues 2 and 4 [stated].
- **A narrow unit sizes the small things**: the skinny column sizes a logo, the 1-unit
  compound column a drop cap, and an empty narrow column on a phone indents text [stated
  across AV, PM, EJ].
- **Empty space is placed, not leftover**: an empty skinny column, an unfilled module that
  creates a diagonal, a quarter of a page left empty "for luxury", the D21 top-left void
  [stated + observed].
- **Staggered starts / staircases**: headline, standfirst and body text each begin on a
  different grid line (PM 2+3, 3+4; EJ 2x2) [observed].
- **Visible structure**: hairline or heavy rules above and below modules (Avaunt contents,
  Cold War, the Mini modular grid), a vertical rule separating the sidebar, stripes as a
  graphic element (Pollock, Steig) [observed].
- **Bleed and overlap**: panels bleed off the page edge (EJ), images overlap the
  neighbouring column (D4 overlap of one column, D21 header bleeding off the left), and
  rotated groups break the frame [observed].
- **Pacing by module size**, both within and across pages, including mobile (PM, EJ)
  [stated].
- **Per-story accent colour sampled from the image** over fixed foundation styles (PM, EJ)
  [stated].
- **Small screens**: what he writes (EJ, BR) is to keep the art direction by turning
  galleries and tall images into horizontally scrolling strips, rotating images to
  landscape, keeping an indent column, and storyboarding small to large first [stated].
  What he builds in this group's code and demos is mostly normal-flow single column below
  48em, and the art direction arrives at 48em or 64em (AV, PM, D4, D21) [observed]. This
  contradicts the EJ line "no need to fall back on predictable, single-column designs";
  D21 at 390 in particular is a default stack, and D4 at 390 drops all rotation.
- **Intermediate breakpoint** as its own composition, not a squeezed large layout: the
  symmetrical 3-column tier at 48em (AV), vertical scatter at medium (BR), and the D4
  tilt kept at 900 with the panel stacked [stated + observed].
- **Inconsistencies to note**: the 4+5 pattern in PM is arithmetically wrong; "6+4" in BR
  sometimes labels the 2+3 values; the D21 live page has lost its main colour block, so
  use the preview image as the reference [observed].
