# IDD digest, group B: Feitler, Brody, Storch, Lubalin (type as image, text shaped by pictures)

Scope: Smashing articles bea-feitler (issue 5), neville-brody (6), otto-storch (7),
herb-lubalin (8); demo pages 1 (Storch), 2, 9, 15 (Lubalin), 3 (Feitler), 20 (Brody) and
their "52 weeks" blog posts.

Tags: [stated] Andy says it; [observed] I saw it in a screenshot, article image, or the
demo's inline CSS; [reported] someone else says it.

Material saved (all under tmp/andy-clarke/):

- Article text: raw/idd/inspired-design-decisions-{bea-feitler,neville-brody,otto-storch,
  herb-lubalin}.txt (already present).
- Article images (1000 px): raw/idd/img/{storch,feitler,brody,lubalin}-*.png|jpg, 64 files,
  fetched by scripts-idd/fetch-imgs-B.sh.
- Demo inspiration images: raw/idd/img/demo01-inspiration.jpg, demo02/03/09/15/20-
  inspiration.png.
- Demo HTML, text, and extracted layout CSS: raw/idd/demos-B/demo{1,2,3,9,15,20}.html,
  .txt, .css.txt (scripts-idd/blogtext-B.py, scripts-idd/demo-css-B.py).
- Blog posts: raw/idd/demos-B/blog{2,3,9,15,20}.html/.txt and blog-index.* (the series
  launch post, which covers #1; the "-1-otto-storch" URL 404s).
- Screenshots: shots/idd/demo01, demo02, demo03, demo09, demo15, demo20 (-1400, -390).

A general note on the "52 weeks" blog posts: each one is a two-sentence announcement plus
a preview image ("My design this week was inspired by ..."). They carry no design
reasoning [observed]. The reasoning lives on the demo page's short "Inspired by" text and
in the Smashing articles. The demo page frames each design in a white box with a large
fixed min-height, so the shots show empty white below the design; that is page chrome,
not the design [observed].

---

## 1. Otto Storch (Smashing, March 2020; demo #1, 6 Jan 2020)

https://www.smashingmagazine.com/2020/03/inspired-design-decisions-otto-storch/
https://stuffandnonsense.co.uk/inspired-design-decisions/1/

### Source

- McCall's art director (1950s-60s), a Brodovitch student. Andy takes from him: type
  carved into the shape of the picture, pictures that sit on or sink into running text,
  the gutter used as part of the design, mirrored verso/recto spreads [stated].
- Spreads he recreated and shows: "Forty-winks reducing plan" (model lies on the text,
  whose top lines bend and sag under her weight), "Teen-age marriages" (one graphic spans
  three of four columns), "Girls are silly / Aren't boys awful" (two faces forehead to
  forehead across the gutter; the two poems ranged right and left, against each other),
  "Fresh as paint" (text block fits a paintbox compartment), "The First to Know" (text set
  in a circle echoing a phone dial), "By a Stroke of Beauty" (brushes laid at angles
  across two justified columns), parfait glass copy, McCall's Patterns black/red mirror
  spread, "On the cob or off" (corn cob lying across both pages above two text columns)
  [observed in storch-02..06, -08, -13, -20, -25].
- Andy's reading of his ethic: ideas matter as much as pictures and words, even in
  unglamorous commercial publishing; "Good art direction does not come from an uncertain
  person" (Storch quote he uses) [stated].

### Layout moves

1. **Angled objects bite into two plain columns** (article "Do More With Shapes"; demo 1).
   Structure is deliberately boring: two symmetrical columns, `grid-template-columns: 1fr
   1fr` at 64em, each holding one justified-looking text block with `10vw` (article) or
   `12vw` (demo) margins on both sides [stated/observed]. All the energy comes from four
   brightly coloured vehicles (Beetles in the article, Vespas top-down in the demo) placed
   at about 20-30 degrees, floated alternately left/right, with polygon `shape-outside` so
   the text edge follows the scooter outline [observed in demo01-1400, demo1.css.txt].
   Result: text blocks get a ragged, diagonal-notched edge on one side and a clean edge on
   the other; one picture per column sits at the top-left, the other mid-column on the
   opposite side, so the eye zig-zags. He says whitespace is 40% of the layout [stated].
   Default instead: images in their own boxes above or beside text, upright, text
   rectangular.
2. **Text sculpted into the subject's shape** ("Make Text Look Delicious"). Centred,
   uppercase condensed copy carved between two invisible floated shape images so the
   paragraph takes the front silhouette of a Beetle; uppercase chosen because solid
   capitals make the silhouette read [stated]. Medium: 2x2 grid with the sculpted text as
   one of the four cells next to the cars it imitates (storch-14) [observed]. Large: a
   horizontally scrolling 4-column band, `repeat(4, minmax(400px, 1fr))`, plus a grey
   "road" strip and reflections [stated].
3. **Mirror symmetry, two colour fields** ("Mirror Symmetry"). Two full-height halves,
   charcoal and red; each holds a top-down Beetle, a red and a white one, nose to tail
   across the centre with a VW roundel on the seam; text lines are wrapped one per span
   and the first/last six lines rotated +/-10-15 degrees so the column fans out like
   Storch's curving caption text (storch-20, -24) [observed]. Large grid: body `1fr 1fr`,
   each half `1fr 1fr 1fr`, picture across two of three columns, text in the third; main
   and aside mirror each other (picture `2 / -1` vs `1 / 3`) [stated].
4. **Big picture resting on two text columns** ("Span Columns"). Large header headline in
   a narrow stacked centre column (`1fr auto 1fr`), a full-width yellow Beetle side view
   sitting on two columns of running text; the wheels are separate floated pseudo-elements
   with `shape-outside`, so the text wraps around the wheels as if the car sinks into the
   copy (storch-25, -28) [observed/stated]. Medium: a deliberately narrow text column with
   `25vw` margins "to emphasise the vertical axis" [stated].

### Small screens

- Demo 1 at 390 [observed, demo01-390]: the art direction survives. The vehicles are
  re-cropped versions (picture element swaps in `-sm` images) rotated to near horizontal,
  bleeding off the left or right edge, each with its own polygon so text still wraps the
  outline. Sequence alternates left-bleed / right-bleed down the page. Columns become one,
  but the diagonal notch in the text edge stays. Side effect: where a scooter takes 60% of
  the width, the remaining text column is 3-5 words wide with justified gaps.
- Article small-screen images (storch-09, -21, -26) [observed]: crops are cut to the
  screen edge, so only a half of each car shows; the mirror design keeps both colour
  fields as stacked full-viewport panels (`min-height: 100vh`), each car cropped at the
  panel edge so the halves still read as a mirror; the yellow Beetle is shown front-half
  only inside an `overflow-x: scroll` figure with a progress bar under it.
- He states: "Instead of resizing images, so they fit within a narrow viewport, I often
  allow them to spread beyond it and add a horizontally scrolling panel" and calls it one
  of his favourite small-screen devices [stated]. Intermediate breakpoints get their own
  composition (2x2 grid, vertical-rl text at 48em, narrow 25vw column) rather than a
  scaled version [stated]. He storyboards each design across sizes before coding
  [stated].

### Quotes

- "Storch understood that ideas are as essential to effective communication as pictures
  and the written word." (Storch article)
- "I rarely see layouts with this kind of energy online" (Storch article, on the angled
  Beetles)
- "Before implementing any design, I make a storyboard to decide how to rearrange
  elements as screen sizes change." (Storch article)
- "Shapes offer so much more than simple text wrapping" (Storch article, conclusion)

### Screenshots

- shots/idd/demo01-1400.png: two columns, four angled top-down Vespas (blue, purple,
  red, gold) notching the text blocks.
- shots/idd/demo01-390.png: single column, four near-horizontal Vespas alternating
  left/right bleed, text still wrapping their outlines.

---

## 2. Bea Feitler (Smashing, issue 5; demo #3, 20 Jan 2020)

https://www.smashingmagazine.com/2019/10/inspired-design-decisions-bea-feitler/ (URL as
given on line 1 of the .txt) and https://stuffandnonsense.co.uk/inspired-design-decisions/3/

### Source

- Harper's Bazaar co-art director with Ruth Ansel (1960s), later Ms., Rolling Stone,
  Vanity Fair. Andy takes: flow and rhythm across pages, extreme scale contrast, pop-art
  colour (green on neon pink), mixing photo with comic art and pattern, the 11pm Day-Glo
  helmet cut-out as an emblem of intuitive decisions [stated].
- Demo 3 source: Harper's Bazaar "Beauty Scrapbook", a typographic spread of nine
  self-contained boxed stories, each a big serif headline (light line over heavy line)
  with hairline rules on both sides, scattered at different heights on a loose grid
  (demo03-inspiration.png) [observed]. Andy on the demo page: he is drawn to how she
  "combined typography with deconstructed grids" [stated].

### Layout moves

1. **Deconstructed typographic grid, no images** (demo 3) [observed, demo03-1400,
   demo3.css.txt]. Four blocks on an 8-column grid, `repeat(8, 1fr)`: header `3 / 7`
   centred-left near the top; article 1 `1 / 3` (narrow, hard left, low); article 2
   `2 / 5` further down; article 3 `5 / -1` pulled up 15rem with `translateY(-15rem)` so it
   rises beside article 2 instead of under it. Each block: small uppercase serif kicker,
   then a huge bold serif word ("NEVER SELL", "MINI", "MONTE CARLO", "ICON") at roughly 3-5x
   the kicker size, a short grey centred rule, then text whose first line is set larger
   in a sans (`::first-line` font-size up). Vertical 3px blue rules on both sides of each
   block (`border-inline-start/end`) copy the source's hairlines. Single colour (blue
   #4697CD) on white. Big empty white fields (top right, middle left) are part of the
   composition. Default would be a centred heading and one even text column, or a 3-card
   row.
2. **Hard-split colour header** (article "50/50 Image To Text"): a two-stop gradient with
   both stops at 50% makes a dark/white split behind a Beetle that is half full-colour,
   half line drawing (feitler-08) [stated/observed]. Landscape vs portrait is switched by
   `orientation` media query, not width; portrait gets a top-down car instead of a shrunk
   side view (feitler-10) [stated/observed].
3. **Scale contrast as the concept** ("Emphasize Scale", from "The Foot and the Ferrari"):
   a giant wheel crop fills half the screen, a tiny whole Beetle sits on a grey road strip
   beside one narrow text column (feitler-13). Grid: his "6+4 compound grid",
   `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`, rows `1fr 155px 155px`; wheel `5 / -1` across all
   rows, car `1 / 4` in row 2, text `4` only [stated]. "Largeness must be relative to the
   size of other elements" [stated].
4. **Reversed colour pair**: deep red and yellow fields swapped on the two halves, each
   with a big wheel crop entering from an edge and a bold display serif "Bitten by the
   bug" (feitler-19) [observed]; large screens stack figure/text vertically per half with
   `column-reverse` on one side so the halves mirror [stated]; a faint SVG pattern breaks
   the flat colour [stated].
5. **Pattern and texture**: half-tone dots from radial gradients sized in vw, circles
   clipped from photos, greyscale + opacity filters; 2-col `4fr minmax(260px, 1fr)`
   [stated]. He frames this as a reaction to flat design's "regrettable uniformity"
   [stated].
6. **Depth by size progression** (from "Cross-Country News"): six Beetles from tiny black
   at the back to a large red in front on an 8x12 modular grid of 16:9 modules (16x12 on
   large), with SVG horizontal motion blur stronger in the foreground (feitler-31, -33,
   -35) [stated/observed].

### Small screens

- Demo 3 at 390 [observed, demo03-390]: the grid is dropped but its stagger survives as
  alternating side margins: articles 1 and 3 indented on the right, article 2 indented on
  the left (`margin-inline-start/end: var(--spacing-l)`), so blocks step left-right down
  the page. Source order differs from desktop position (ICON comes before MONTE CARLO on
  the phone). Display words keep their dominance (MINI and MONTE CARLO fill the column
  width); the double vertical rules survive. Lost: the large empty fields and the
  upward overlap.
- Article: "maintain a similar contrast in scale on small screens" before designing large
  ones; the wheel header is fixed at `33vh` with `33vh` of space below so the ratio holds
  [stated]. Header image capped at `75vh` so text still starts on the first screen
  [stated]. Six cars in a `row-reverse` horizontally scrolling strip at 80% basis, so the
  front of each car points into the scroll and hints there is more [stated]. Small-screen
  images (feitler-16, -21) show giant crops kept giant, not scaled down [observed].
- "Shrinking a landscape image to fit a portrait orientation decreases its visual weight
  and impact." [stated, caption]

### Quotes

- "Sheer size is rarely enough on its own" (Feitler article, scale section)
- "When you use images to add drama, make sure their effect is dramatic on all screen
  sizes." (Feitler article, caption)
- "With little to differentiate their designs, products and websites have adopted a
  regrettable uniformity" (Feitler article)
- Feitler, quoted by Andy: "You can't look at one page alone, you have to visualize what
  comes before and after." [reported]

### Screenshots

- shots/idd/demo03-1400.png: four staggered blue serif blocks on white, large empty fields.
- shots/idd/demo03-390.png: blocks stacked, alternately indented left/right.

---

## 3. Neville Brody (Smashing, issue 6; demo #20, 18 May 2020)

https://www.smashingmagazine.com/2020/03/inspired-design-decisions-neville-brody/ (per
.txt line 1) and https://stuffandnonsense.co.uk/inspired-design-decisions/20/

### Source

- The Face (1981-86). Andy grew up in Corby during the steel closures; The Face was part
  of his teenage music/politics world [stated]. Takes from Brody: question every page
  element, structure as the visible feature, wide letter-spacing that slows reading,
  vertical and diagonal lines of type, bleeding images and type off the page edge,
  alternatives to drop caps, a simple 2-3 column grid used flexibly [stated].
- Demo 20 source: "New Order" spread: a huge condensed headline running vertically up the
  left edge, two small diamond-bulleted kicker lines vertical beside it, two justified text
  columns, the facing page one bleeding cropped photo (demo20-inspiration.png) [observed].

### Layout moves

1. **Vertical headline as the column** ("Vertical Text For Impact"): header grid
   `1fr 6rem`, the 6rem column holds the headline in `writing-mode: vertical-lr` rotated
   180 degrees to read bottom-up, with `mix-blend-mode: multiply` so the background shows
   through it; drop cap via `initial-letter: 2`, indented paragraphs, standfirst between
   two thick rules (brody-08) [stated/observed]. He calls the rotate hack a hack
   [stated].
2. **Bleed off the top and left**: header that bleeds off the viewport "implies there's
   more to see outside", while a margin "acts as a boundary which stops the eye"
   (brody-10 caption) [stated].
3. **Rotated image across a compound grid** ("Responsive Grids And Rotation", from "Ital
   Style"): large grid `1fr 1fr 1fr 6rem 1fr`, rows `repeat(6, auto)`; elements share
   cells to overlap; the car rotated `-20deg` crosses modules, over a black "Get a
   Capri... if you're quick" block (brody-17, -19) [stated/observed]. The narrow 6rem
   track appears again as a deliberate odd column [observed].
4. **Blends and texture**: monochrome chaotic background image multiplied with colour
   (`background-blend-mode: multiply`), double text-shadow, spark-plug silhouette behind a
   narrow text column (padding `8rem 20vw`) (brody-05) [stated].
5. **Zig-zag clip-paths** on figures and around the standfirst; display face at `7vmax`
   (brody-14) [stated].
6. **Demo 20** [observed, demo20-1400, demo20.css.txt]: 6-column grid. Left column `1 / 2`
   holds a header grid of two narrow tracks: the date "1962-1983" and two kicker lines
   ("UK's best-selling car", "During the 1970s", each with a blue diamond bullet and a
   dotted leader) set vertical (`writing-mode: vertical-lr` plus 180 degree rotation),
   reading bottom-up; the horizontal title "Ford Cortina" and a Ford oval sit beside them.
   Text `2 / 4` in two narrow multi-columns (`column-width: 12em`), first-line indents,
   no paragraph spacing. Right half `4 / -1` is a near-black panel with a cropped blue
   line drawing of the Cortina's front, cut by the panel's top and left edges, plus a
   60px blue `border-inline-end` bar on the far right. A clutch-plate drawing sits under
   the text. Note: unlike the source, the main title is not set vertically and not huge;
   the vertical move is carried by the small kickers only [observed].

### Small screens

- Demo 20 at 390 [observed, demo20-390]: the dark image panel moves to the top as a
  full-width banner (crop kept); title, then the kickers turn horizontal and read as a
  bulleted pair with the date on a dotted leader; text becomes one column; clutch plate at
  the end. All vertical type is lost; colour and the cropped-image entry survive.
- Article storyboards (brody-13, -19) [observed]: small screen stacks the headline
  horizontally; medium sets it on one line; only large turns it vertical. The Ital Style
  design uses a grid from the start on phones: `3rem 1fr 3rem`, with a backdrop division
  in the centre column spanning two rows behind a full-width header, so the phone still
  gets layering [stated].
- "I've always thought of responsive design not as a challenge, but as a chance to be
  creative." [stated]

### Quotes

- "On the web, we're told to not make someone look more than once ... But, one of the
  reasons I find Brody's work so fascinating is it makes people look twice." (Brody
  article; two sentences, trimmed)
- "Each breakpoint provides an opportunity to make designs which make the most from every
  screen size." (Brody article)
- "a system for design ... should support a design, not define, nor dictate the end
  result." (Brody article, trimmed)
- Brody, quoted: "Our golden rule was to question everything." [reported]

### Screenshots

- shots/idd/demo20-1400.png: left vertical kickers and title, two narrow text columns,
  right dark panel with cropped car drawing, blue edge bar.
- shots/idd/demo20-390.png: banner image on top, horizontal kickers, single column.

---

## 4. Herb Lubalin (Smashing, issue 8; demos #2 13 Jan, #9 2 Mar, #15 13 Apr 2020)

https://www.smashingmagazine.com/2020/04/inspired-design-decisions-herb-lubalin/ (per
.txt line 1); https://stuffandnonsense.co.uk/inspired-design-decisions/2/, /9/, /15/

### Source

- Lubalin: "expressive typography", type cut with a scalpel to fit, words that look like
  what they say; process by layered tissue sketches with typographic notes [stated].
  Andy also cites film poster type (Bass, Caroff) as a source he loves [stated].
- Demo 2 source: a quotation page: big black quote marks top-left and bottom-right; a
  column of author names in heavy condensed caps alternating blue / grey / black; each
  name paired with a quote in a matching colour and style, separated by thick and thin
  rules; the name column switches from left to right halfway down
  (demo02-inspiration.png) [observed].
- Demo 9 source: Carr's July 4th ad: a car seen from behind at the top, the copy below it
  set as a road in perspective, lines widening and type growing toward the bottom
  (demo09-inspiration.png) [observed].
- Demo 15 source: "The next war will determine not what is right but what is left": a
  tight block of heavy white caps on black, cockroaches inside the last word
  (demo15-inspiration.png) [observed].

### Layout moves

1. **Pre-formatted display block** (article): black and light weights of one family
   (Montserrat), negative tracking, tight leading, explicit line breaks that only take
   effect at 64em (`white-space: pre`), red bold lines over white light lines
   (lubalin-06) [stated/observed]. Variety from one family's weights/widths rather than
   many fonts [stated]. Page: 5 equal columns, main `1`, aside `3 / -1`, leaving column 2
   as an empty white-space column [stated].
2. **Rotated headline with an empty-cell diagonal** (from "Castrated" jacket): header on
   `repeat(4, 1fr)`; headline across all four, lower paragraph `2 / -1`, upper paragraph
   (moved first with `order: -1`) `1 / 4`, so the empty corners make a diagonal;
   headline `rotate(-30deg)` from the bottom-left origin; hover eases to -25 degrees
   (lubalin-08, -11) [stated/observed].
3. **Vertical tri-colour headline packed against a list** (from Graphis / American
   Showcase): three words in red/white/blue each in its own column of a `repeat(3,
   min-content)` grid, set `vertical-lr` and rotated 180 degrees, with the Mark I-V list
   sitting on the headline's baseline as one solid block (lubalin-12, -13) [stated].
4. **Images inside letters**: SVG letter paths filled with blueprint patterns (lubalin-23);
   `background-clip: text` with a brake disc image [stated].
5. **Giant type as background**: "MADE IN BRITAIN 1962-1983" in huge condensed red caps
   filling the page behind white running text and a smaller white "Ford Cortina" heading;
   grid `1fr 1fr 1fr` x `repeat(5, 1fr)`, header `1 / 3`, text `2 / 4`, leaving empty
   columns "to lead someone's eye around the composition" (lubalin-25) [stated/observed].
   `backdrop-filter` keeps text readable [stated].
6. **Demo 2 (quotation page reworked)** [observed, demo02-1400, demo2.css.txt]: two
   sections each on a 4-column grid; section 1 puts the VW logo and pale grey bold
   headline in column 1 and three paragraphs in `2 / -1`; section 2 flips it: text
   `1 / 4`, Fiat logo and headline in column 4. Each paragraph differs in style (blue
   serif, grey uppercase between 8px grey rules, black roman), separated by thick and thin
   rules in grey or near-black, copying the source's alternating rule rhythm. The
   headline is light grey and modest; the source's heavy black names are not reproduced
   at that weight.
7. **Demo 9 (text as a road in perspective)** [observed, demo09-1400, demo9.css.txt]:
   centred stack: Ford oval, short intro, big script "Cortina" wordmark, a full-width
   side-view line drawing (`max-width: 60vmax`), then a narrow text column
   (`max-width: 20vmax`) tilted with `perspective(40vmax) rotateX(20deg) translateZ(5rem)`
   at 48em and `rotateX(30deg) translateZ(8rem)` at 64em, so the italic copy reads as a
   road widening toward the viewer under the car. Hover transition on the transform. It is
   a symmetrical, centred layout; the art direction is the text block itself.
8. **Demo 15 (dotted marquee headline)** [observed, demo15-1400, demo15.css.txt,
   lubalin-17]: black page; 5-column grid, main `1 / 3`, aside `3 / -1`; aside a nested
   grid with areas `"a a" "b c" "d e"` (car + intro across the top, four Mark entries in
   pairs below, each with a script "Mark" label over an underlined date). The headline
   "'70s best-selling Cortina British car" is SVG text with a dotted stroke
   (stroke-dasharray, round caps) imitating marquee bulbs; hover thickens the stroke. In
   my headless Chrome render the dotted outline barely shows (headline reads as near-black
   on black), so the shot under-represents it; lubalin-17 shows the intended white dots.

### Small screens

- Demo 9 at 390 [observed]: perspective tilt is removed (it is set only at 48em+); the
  stack (logo, wordmark, car, text) stays centred; the car scales to the column. The core
  idea (text as road) is lost on phones.
- Demo 15 at 390 [observed]: single column, headline first, then logo, car, text, Mark
  entries; the grid of areas collapses to one column.
- Demo 2 at 390 [observed]: logo, headline, then the ruled paragraphs; section 2 puts
  headline and Fiat logo before its text (source order), so the left/right flip is lost
  but the rule rhythm and colour alternation stay.
- Article small images (lubalin-11, -13) [observed]: rotated and vertical headlines
  become horizontal stacked blocks on phones, keeping colour, weight, and the tight block;
  rotation is a large-screen layer. On small viewports the pre-formatted headline "reads
  like a sentence" because line breaks only apply at 64em [stated]. The `picture` element
  serves a whole car to phones and a half car to large screens (lubalin-27) [stated].

### Quotes

- "Expressive typography needn't need fancy fonts." (Lubalin article)
- "It's unusual to see rotated text elements on the web, but when you do, they're often
  memorable" (Lubalin article)
- "Leaving columns around my header and text division empty creates negative space which
  helps to lead someone's eye around the composition." (Lubalin article)
- "There's no doubt that Herb Lubalin had a masterful ability to make type talk." (Lubalin
  article)

### Screenshots

- shots/idd/demo02-1400.png / -390.png: VW and Fiat sections, flipped columns, ruled
  paragraphs; phone stacks them.
- shots/idd/demo09-1400.png / -390.png: Cortina side view over perspective-tilted text;
  phone shows flat text.
- shots/idd/demo15-1400.png / -390.png: black page, faint dotted headline left, car and
  Mark grid right; phone single column.

---

## Cross-issue patterns seen in this group

- **Plain structure, energetic content** [stated/observed]. The grids are mostly
  symmetrical (`1fr 1fr`, `repeat(4/5/8, 1fr)`); energy comes from what sits on them:
  angled objects, rotated or vertical type, giant crops, spans that leave cells empty.
  Brody: the system supports, it does not dictate. This contradicts the instinct that
  "art-directed" needs an exotic grid; the exceptions are deliberate odd tracks (6rem
  headline column, `2fr 1fr 1fr 2fr` compound grid).
- **Type and picture share one outline**: text wrapped around an object's polygon
  (Storch, demo 1), text carved into the object's silhouette (Beetle, parfait), pictures
  inside letters (Lubalin), text as the object (road in demo 9). The text edge is drawn
  by the picture, never a rectangle beside it.
- **Empty cells and space as composition**: empty column 2 in Lubalin's 5-column layout,
  empty corners creating a diagonal, Feitler-style white fields in demo 3, 40% whitespace
  in the Storch Beetles.
- **Scale contrast relative, not absolute**: giant wheel vs tiny car; huge display word
  vs small kicker (demo 3 at roughly 4-5x); stated rule that largeness must be relative.
- **Bleed and crop to imply more**: images cut by viewport or panel edges (Brody header,
  demo 20 car, Feitler wheel crops, Storch half-cars); horizontally scrolling strips on
  phones with the next item's front showing.
- **Mirroring and reversal**: Storch black/red mirror, Feitler reversed red/yellow,
  Lubalin demo 2 flipping the heading column between sections; repetition with a flip
  gives rhythm across sections.
- **What survives at 390**: scale contrast, colour fields, crops, rules, and text-wrap
  around shapes survive (he designs small first and re-crops images). Rotation, vertical
  writing, perspective, and overlap are mostly large-screen layers: demo 9's road, demo
  20's vertical kickers, Lubalin's rotated headlines, Brody's vertical headline all go
  horizontal/flat on phones. Exceptions where the phone keeps the idea: demo 1 (rotated,
  bleeding scooters with wrap) and Ital Style (`3rem 1fr 3rem` layered grid from the
  start).
- **Intermediate breakpoints get their own composition** (2x2 grid, vertical-rl text,
  narrow 25vw column, orientation queries), not a scaled version [stated].
- **Tension with readability** [observed]: shape wrapping on phones produces 3-5 word
  lines with wide justified gaps (demo 1); demo 15's dotted headline is near-invisible in
  a plain render; demo 2's headline is pale grey. Andy accepts some reading cost for
  "look twice" impact (Brody section), but adds `backdrop-filter`, drop shadows, and
  `@supports` guards as mitigations [stated].
- **The demos are thinner than the articles** [observed]: the weekly demos often take one
  move from the source (demo 2's rule rhythm, demo 20's vertical kickers) and leave the
  boldest part (heavy black names, the huge vertical title) at modest size. The articles'
  designs are the stronger evidence of his judgement.
