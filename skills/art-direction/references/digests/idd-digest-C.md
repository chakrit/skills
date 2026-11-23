# IDD digest, group C: Huber, Pintori, McBain, Thompson

Scope: Smashing "Inspired Design Decisions" issues 9 to 12 (Max Huber, Giovanni Pintori,
Emmett McBain, Bradbury Thompson) and the 2020 demo pages 7, 11, 14 (Huber), 16, 18, 19
(Pintori), 22 (McBain), 5, 17 (Thompson) with their "52 weeks" blog posts.

Markers: [stated] Andy says it; [observed] I saw it in a screenshot, article image, or the
demo's inline CSS; [reported] someone else says it.

Sources:

- Huber: https://www.smashingmagazine.com/2020/05/inspired-design-decisions-max-huber/
- Pintori: https://www.smashingmagazine.com/2020/06/inspired-design-decisions-giovanni-pintori/
- McBain: https://www.smashingmagazine.com/2020/07/inspired-design-decisions-emmett-mcbain/
- Thompson: https://www.smashingmagazine.com/2020/08/inspired-design-decisions-bradbury-thompson/
- Demos: https://stuffandnonsense.co.uk/inspired-design-decisions/N/ (N = 5, 7, 11, 14, 16,
  17, 18, 19, 22). Each demo page shows the print piece it came from ("inspiration.png").
  I saved them as raw/idd/img/demoNN-inspiration.png.
- Blog posts: stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-N-<designer>/.
  All nine resolve. Each holds one or two sentences of biography and a preview image, with
  no design reasoning (raw/idd/blog/blogN.txt). The text on demo page 5 is about Alvin
  Lustig even though the page title says Thompson; it looks like a copy-paste slip.

Screenshot caveat [observed]: shoot.sh makes a 1400x3000 window and a 390-wide iframe
6000 px tall, so `vh` units grow to 3000 or 6000 px. Several demos size themselves in vh:
`#design { min-block-size: 90vh }` on every demo, `max-height: 100vh` on demo 7, and
`background-size: cover` on demo 22. In those shots the grid rows stretch into large empty
bands. To get realistic views I added two scripts:

- scripts-idd/shoot1400v.sh: 1400x900 window, cropped to the design area
  (`*-1400v.png`).
- scripts-idd/shoot390h.sh: 390x844 iframe (`*-390h.png`).

I also cropped every 390 shot to its top 1900 px (`*-390-top.png`). Judge composition
from the -1400v, -390h and -390-top files. Use the full-height -1400 shots only for the
order of the content.

---

## 1. Max Huber (Smashing issue 9, demos 7, 11, 14)

### Source

- Swiss designer working in Milan, known for La Rinascente work, Monza race posters, and
  record covers [stated]. Andy credits him with these signature elements: "bold blocks of
  color, iconic shapes, photographic manipulation, and strong typography" [stated].
- Huber cut photographs out of their backgrounds and mixed them with blocks of colour and
  flat shapes (arrows, circles, swirls), with "colorful strips" for movement [stated].
- Huber set type at angles and in perspective while keeping a strict hierarchy on grids
  [stated].
- Article images I looked at:
  - magazine covers built from overlapping translucent circles and rectangles;
  - the Museum Bellerive poster: a white circle on violet, with glassware photos inside
    it;
  - the "Voci e immagini del 1958" record sleeve: a giant pale "5" and a red "8" behind
    everything, words in a ring, and type upside-down and rotated in many directions;
  - the Burattini poster: a rainbow vertical gradient, an engraving overlaid, and huge
    mixed-case serif display type at the bottom
  [observed].
- Andy's general lesson is that a mundane subject can become exciting visual
  communication [stated]. His derived designs present the Trabant, which he calls "the
  worst car ever made", as a glamorous subject [stated].

### Layout moves (article designs, issue-9-04, -12, -16, -14)

1. **A logo circle over a cut-out photo, blended.** In design 1, the header stacks three
   things in one grid cell (`grid-column:1; grid-row:1`):
   - a square box built with padding-top 100%;
   - the round Trabant SVG emblem;
   - a car photo.

   `mix-blend-mode: overlay` fuses the photo into the circle [stated]. At 82em the header
   takes the left half of a 6-column grid (`grid-column: 1 / 4; grid-row: 1 / 4`), so the
   circle bleeds off the left edge of the page [stated/observed]. This is Huber's
   circle-plus-photo (Bellerive) on the web. The default design would have used a
   rectangular hero photo.

2. **An asymmetric result from a symmetric grid.** Design 1 uses
   `repeat(6, 1fr)`, `column-gap 2vw`, `row-gap 2vh` [stated]:
   - the headline sits in columns 4 to the end, row 1, at 6.5rem;
   - the paragraphs sit in columns 5 to the end;
   - column 4 is left empty in row 2, and the footer goes there in row 3.

   Andy says outright that the design "appears asymmetrical" while its grid has six even
   columns [stated]. The banner uses `display: contents` so that its children land on the
   page grid directly [stated].

3. **Two-tone headline and a modular type scale.** The headline is right-aligned with
   tight leading, and an accent-coloured `<span>` creates the two tones [stated]. Sizes
   move up a fixed scale (1rem, 1.266, 1.424, 2.027, then 4.875, 6.5 or 8rem) at each
   breakpoint [stated]. A second paragraph is shrunk with `:nth-of-type` to make it
   recede [stated].

4. **Numerals as the image (design 3, "57").** Two overlapping SVG numerals "5" and "7"
   are set at lower opacity with `mix-blend-mode: multiply` [stated]. A vertical
   generated word "Duroplast" (`writing-mode: vertical-rl` plus `rotate(180deg)`, 7rem,
   then 10rem) is blended with overlay, and later with difference, across them
   [stated/observed]. Text on a curved SVG path circles the numerals [stated]. This is
   lifted directly from Huber's "58" record sleeve [observed]. The grid is
   `repeat(6,1fr)` with `repeat(4, auto)` rows; the numerals span columns 1 to the end
   and rows 2 to 4 behind everything [stated]. Andy: "leaving some columns empty creates
   an unusual asymmetrical design" [stated].

5. **Micro-type as ornament.** The currency code "DDM" after the price 7,450 is set
   vertically and rotated so it sits beside the large numeral [stated/observed in
   issue-9-12]. Numerals are oversized (4.5rem) and letter-spaced to show the typeface's
   character [stated]. The visual order of label and value is flipped with
   `column-reverse` so that the number comes first [stated].

6. **A line drawing as the background plane.** In design 2, a Trabant blueprint outline
   sits behind a linear gradient at `background-position: 50vw 2rem`. The headline is
   capped at `max-width: 50vw` so that it occupies the empty half [stated]. The default
   would have been a photo with a dark overlay.

Demo 7 (Vespa; source: Huber's *Coppa la Rinascente-Upim* cycling poster, a yellow ground
with white horizontal strips and three overlapping translucent cyclists in red, blue and
grey):

7. **Horizontal colour strips as the grid** [observed + CSS]. At 48em the page is a
   12-column grid whose named rows have uneven heights:
   `[header] 2fr [p-1] 1fr [p-2] 1.5fr [p-3] 1fr [empty] 1fr [p-4] 1.5fr [p-5] 1fr 2fr`.
   - Each sentence is a full-width `<span>` on its own row band. Its background is either
     white or a yellow/white hard-stop `linear-gradient` (`#f2c867 45%, #fefaf8 45% 55%`),
     which recreates Huber's white strips.
   - Each sentence starts at a different horizontal indent (`padding-inline-start` of
     30vw, 40vw, 30vw, 10vw, 25vw), so the reading line zig-zags down the strips.
   - Three scooter silhouettes (orange, red, mauve) have `opacity .75` and
     `mix-blend-mode: multiply`. Their positions are:
     - columns 1 to 7, rows 2 to 5, pushed `translateX(-10vw)` past the left edge;
     - columns 1 to 8, rows 5 to 7;
     - columns 6 to the end, rows 5 to 7.
   - The second and third silhouettes overlap, and the overlap darkens to a deep brown,
     as in the poster.
   - The default would have been a product photo above a bulleted feature list.
8. Headline "Looks Like a Wasp!" sits as a small three-line stack beside the script
   logo, at the scale of a caption rather than a hero [observed].

Demo 11 (Vespa; source: Huber's Le Corbusier book cover: a giant pale "LC" monogram over
blue/green bands, with a line drawing scrawled across):

9. **Monogram plus line drawing over colour bands** [observed + CSS]. The whole design is
   one element with three stacked backgrounds:
   - a logo SVG with `soft-light` blend;
   - a scooter line drawing with `multiply` blend;
   - a hard-stop gradient: purple `#804671` 0 to 40%, yellow `#f2c867` 40 to 90%, purple
     again.

   The "Vespa" script logo is set at 80% width and pale. It crosses the colour boundary,
   so its lower half reads differently over yellow. That is exactly the Le Corbusier
   cover's LC over the blue/green split. The body text uses
   `mix-blend-mode: luminosity`. On the web this layout has no grid at all; the
   background planes are the layout.

Demo 14 (Trabant; source: Huber's Gulf Italia data poster: an oil-pump silhouette, a
giant "1400000", stacked percentages divided by rules, and a ruled box of yearly
figures):

10. **A data poster as the page** [observed + CSS]. The grid is `repeat(8,1fr)`:
    - the 3,096,999 block runs from column 3 to the end at 10rem, with a red rule under
      it;
    - the stats list runs from column 5 to the end, each a huge numeral plus a light unit
      ("6.3gallon", "40mpg", "7,450ddm"), with red rules between them, as in the
      poster's percentages;
    - the history text sits in a red-ruled box in columns 1 to 4, mirroring the
      poster's boxed table;
    - the car rides up the slanted "Trabant" script logo, so the logotype becomes the
      road.

    The default would have been a stats row of three equal cards.

### Small screens

- Andy storyboards first: "I make a simple storyboard to demonstrate how my elements will
  flow across a selection of screen sizes" [stated, Huber]. The storyboard image
  (issue-9-14) shows the same design at roughly 320, 768 and 1280 px. The headline,
  outline car and specs persist at every size; only the arrangement changes [observed].
- The Trabant header "dominates my design on even the smallest screens" [stated]. On the
  phone, the circle emblem and photo fill the full width at the top [observed in
  issue-9-04 right].
- "Space on small screens may be at a premium, but that doesn't mean we can't be bold with
  our typography" [stated]. In design 3 the 57 numerals and vertical "duroplast" survive
  on the phone [observed, issue-9-16 right]. The curved text-on-path is hidden below 48em
  [stated].
- He gives micro-type equal care on small screens: "I put as much thought into designing
  type for small screens as I do into a layout for larger ones" [stated].
- Breakpoints: 48em adds simple grids; 64em or 82em moves to 6-column placements [stated].
- Demo 7 at 390 [observed, demo07-390-top]:
  - the strips and the zig-zag are dropped, leaving a yellow panel with logo, headline,
    and the five sentences as a block;
  - the scooters become a 200 px high horizontally scrolling strip (`flex: 1 0 90%`,
    `overflow-x: scroll`), and only the first is visible;
  - the overlap and multiply effect is lost on the phone.
- Demo 11 at 390 [observed, demo11-390h]:
  - the purple field with the pale script logo behind the headline survives;
  - the scooter drawing and the yellow band sit at the bottom of a 90vh block, below the
    first screen;
  - the art direction holds as colour and logo, not as the drawing.
- Demo 14 at 390 [observed, demo14-390-top]:
  - logo plus car stay small at the top;
  - the numerals stay big (about 60 px), with red rules between them;
  - the poster's hierarchy (numeral, unit, label, rule) fully survives, and only the
    side-by-side placement is lost.

### Quotes (Huber URL)

- "Despite being built on a symmetrical grid, leaving some columns empty creates an
  unusual asymmetrical design."
- "To me, every typographic element — no matter how small — is an opportunity to
  experiment with interesting type treatments."
- "Supersizing a headline is a fabulous way to showcase the intricate details in many
  modern typefaces."
- "My confident typography choices demand I'm also courageous with my choice of layout
  for larger screens."

### Screenshots

- shots/idd/demo07-1400.png: full height, strips and multiply scooters (rows stretched by
  vh).
- shots/idd/demo07-1400v.png: realistic 900-high view. Rows are compressed and the
  scooters overlap the text strips more.
- shots/idd/demo07-14-1400v-pair.png: demos 7 and 14 first screens stacked.
- shots/idd/demo07-390-top.png: phone; strips dropped, scooter scroller.
- shots/idd/demo11-1400.png: purple/yellow bands, pale logo, line-drawn scooter.
- shots/idd/demo11-390h.png: phone first screen; purple field and logo.
- shots/idd/demo11-390-top.png: vh-inflated, an empty purple column (artifact).
- shots/idd/demo14-1400.png: data poster; empty bands are a vh artifact.
- shots/idd/demo14-390-top.png: phone; stacked numerals with rules.
- Article images: raw/idd/img/montage-C/huber-src.png (Huber covers, Bellerive, "58"
  sleeve), huber-designs.png (Andy's three Trabant designs, desktop plus phone),
  huber-story.png (storyboard plus Burattini poster).

---

## 2. Giovanni Pintori (Smashing issue 10, demos 16, 18, 19)

### Source

- Art director at Olivetti for 31 years [stated]. Pintori used "bright colors from minimal
  color palettes" and shapes, and his shapes "suggested the benefits of using a product
  rather than describe its features literally" [stated].
- Article images I looked at [observed]:
  - Lettera 22: letters on coloured arcs bouncing like a fountain above the machine;
  - Numbers: a field of multicoloured numerals on black;
  - Graphika: key-circles wired by coloured lines;
  - Tetractys: a tree of coloured arrows;
  - the Lettera 22 brochure: outlined squares in blue, yellow and magenta overlapping a
    ship and the typewriter.
- Andy pairs Pintori with Miró and Jasper Johns, which is an art-world framing [stated
  captions].
- The article's lessons are colour palettes and how colour leads the eye; lines and shapes
  add structure [stated in the standfirst].

### Colour rules (stated)

- "my palettes rarely contain more than three hues; a dominant color, secondary or
  supporting color, and an accent", plus neutrals for backgrounds, borders and text.
- He adds shades and tints of each hue: darker shades for borders such as button edges,
  lighter tints for highlights [stated]. The palette image (issue-10-05) shows each hue
  as a big disc with a small darker and a small lighter disc. Beside it, rectangles show
  percentage use: one large dominant, one medium, one thin accent [observed].
- He often goes monochrome, or monochrome plus one accent, "because they make achieving a
  visually cohesive look quite simple" [stated]. He also says colour is the hardest part
  of design for him [stated].
- Complementary pairs clash when adjacent, so use their tints and tones or a split
  complementary [stated].
- In dark mode he brightens rather than inverts: raise lightness and saturation about 10%
  (`filter: saturate(1.5) brightness(1.1)`) and use off-white rather than white text
  [stated].

### Layout moves (article designs)

1. **Offset overlapping outlines (design 1, Morris Traveller).** The header grid is
   `270px 1fr 270px` / `100px 1fr 100px` [stated]:
   - one car outline spans columns 2 to 4, row 1, scaled to .85 for perspective;
   - the second spans columns 1 to 3, rows 2 to 4, with a higher z-index;
   - the result is two line drawings in red and green offset diagonally, like a
     misregistered print [observed].

   At 64em he uses a **6+4 compound grid**, `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`. The main
   text is right-aligned against the figure "to create a solid block of content in the
   centre" [stated].
2. **Narrowing toward the bottom.** At the 6-column medium size [stated]:
   - the header is full width;
   - main spans columns 2 to 6;
   - figure and footer span columns 3 to 5.

   This forms a funnel of decreasing widths. "Even a seemingly mundane even-ratio grid
   can result in an original layout when a design includes plenty of whitespace to help
   lead the eye" [stated].
3. **A modular panel grid (design 2).** It uses seven empty divs plus h1 and p
   [stated]:
   - 3x3 areas with `minmax(300px, 1fr)` rows;
   - one area name "d" repeated so that the panel spans two cells;
   - each panel is a Pintori-like abstraction of a car part: hub cap over blue/white/
     black stripes, horn grille, bumper chevrons, hard-stop gradient stripes.

   "It's rare to find designs online which are based on a modular grid" [stated]. A
   monochrome version (all one hue, issue-10-13 left) sits beside the full-colour one
   [observed]. The default would have been a features grid of identical icon cards.
4. **Header and footer moved to the sides.** In design 3, on 8 columns at 72em
   [stated]:
   - the footer image fills columns 1 to 4, the header image columns 5 to the end, both
     on rows 1 to 3;
   - the banner and text sit in a 160px row between them.

   "Despite their names, you needn't place a header or footer element at the top and
   bottom of a layout" [stated]. Overlapping blueprints of the Traveller come in
   complementary colours [observed].
5. **Rotated outline squares with multiply (design 4, the source of demo 16).** The
   shapes are presentational rectangles placed on an 8x8 grid [stated]:
   - blue: columns 2 to 4, rows 2 to 4, `rotate(-30deg)`;
   - yellow: columns 4 to 8, rows 2 to 5;
   - red: columns 3 to 5, rows 4 to 6;
   - green: column 4, row 6, `rotate(5deg)`.

   `mix-blend-mode: multiply` darkens where they overlap (the blue/yellow overlap turns
   green) [stated/observed]. The car outlines sit on the same grid with
   `rotate(-20deg) translateX(-12rem)` and scale 1.1 or 1.25 [stated]. This translates
   the Lettera 22 brochure almost literally [observed].

Demo 16 (Trabant; source: the same Lettera 22 brochure): a web build of design 5
[observed + CSS]:

- an 8-column grid of `auto` rows;
- the profile outline rotated -20deg inside the rotated blue square;
- the front view inside the yellow square;
- red and lime squares lower down;
- the text block in columns 5 to 8, rows 5 to 7, with a dotted-leader spec list
  ("Two-stroke fuel tank. . . . . 6.3gal");
- the header logo hidden on desktop.

The blue/yellow overlap turns dark green, as in the print.

Demo 18 (Fiat 500; source: Pintori's Lettera 22 poster made of coloured rectangles, each
a room or window with an object):

- **A Mondrian-like flex/grid of colour panels** [observed + CSS]. It is a 2x2 grid
  (`1fr 1fr / 1fr 1fr`) at 64em; each quadrant subdivides with flex into panels of
  `flex: 1` or `flex: 2`.
- Each panel holds one flat white or colour abstraction of a Fiat part: bumper, mirror,
  tail-lights, seat.
- The panels are separated by thick borders and stripes (`border-inline-end: 100px
  solid`, `border-block-start: 40px solid`), as the print uses black bars.
- One panel has a diagonal two-colour split (`linear-gradient(to bottom right, #000 50%,
  #401332 50%)`) behind the "FIAT nuova 500" mark.
- The palette is aubergine, mauve, black, yellow and off-white.
- `order: 4` moves the first div to the end on large screens.

Demo 19 (Fiat 500; source: Pintori's Lettera 22 ad with a multicoloured alphabet inside a
typewriter-case silhouette):

- **Type inside a product silhouette** [observed]. "L'evoluzione del mito" is set in a
  heavy wide sans in three colours (red, yellow, blue), packed tight inside a pale-grey
  case/car shape. This is Pintori's coloured "abcd" inside the case.
- The 8-column grid places the header in columns 1 to 6. Main is in columns 6 to the end
  and reordered with flex `order`, so the h1 comes third.
- The aside is boxed in columns 2 to 5.
- The FIAT roundel floats with `shape-outside: circle()` so the text wraps around it.

### Small screens

- "Flexbox transforms my header into a horizontally scrolling panel, one of the most
  effective ways to maintain visual hierarchy in a small screen design" [stated]. He uses
  this twice in issue 10 (images `flex: 1 0 640px`) and again in Thompson.
- CSS Grid reorders content on the phone so that the logo and car-front panels come
  first, above the h1 (`#panel-d{grid-row:1}` and so on) [stated].
- In design 3, `<picture>` swaps in a single-car image on small screens and a two-car
  image when there is room [stated].
- In design 4, the coloured squares are applied on the phone as **background images
  stacked down the page**, centred, one behind each content block. On larger screens he
  removes them and places real elements on the grid [stated]. Demo 16 at 390
  [observed, demo16-390h]:
  - the blue square frames the logo;
  - the yellow square frames the car profile;
  - the red square sits behind the headline.

  The overlap and rotation are lost, but the shape-and-colour vocabulary is kept, one
  shape per block.
- Demo 18 at 390 [observed, demo18-390-top]:
  - the panels stack, the Fiat-nuova panel moves first, and the logo follows;
  - the three-column flex sub-panels survive at phone width (black, navy, yellow
    strips);
  - flaw: the off-white page background is only set at 64em, so on the phone the "Fiat
    500" caption is dark text on the site's navy and nearly invisible.
- Demo 19 at 390 [observed, demo19-390-top]: the type-in-silhouette is kept at full
  width, followed by text, the floated roundel, and the boxed aside. The poster survives
  intact because it is one SVG.

### Quotes (Pintori URL)

- "The colors we choose should tell a story about a company, product, or service as
  eloquently as our layout or typography."
- "I like to keep my colors simple, and my palettes rarely contain more than three hues."
- "It's rare to find designs online which are based on a modular grid."
- "Despite their names, you needn't place a header or footer element at the top and
  bottom of a layout."

### Screenshots

- shots/idd/demo16-1400.png: rotated outline squares, multiply overlap, outline cars;
  the vertical gaps are vh-stretched.
- shots/idd/demo16-390h.png: phone; squares as stacked background frames.
- shots/idd/demo18-1400.png: full modular panel composition.
- shots/idd/demo18-390-top.png: phone stacking, plus the invisible-caption flaw.
- shots/idd/demo19-1400.png, demo19-1400v.png: type in silhouette, roundel with
  shape-outside.
- shots/idd/demo19-390-top.png: phone.
- Article images: raw/idd/img/montage-C/pintori-src.png (Miró, Lettera 22 arcs, Johns,
  numbers, Graphika, Tetractys), pintori-designs1.png (overlapping outlines; modular
  panels in colour and monochrome), pintori-designs2.png (complementary blueprints;
  rotated squares; palette and percentage swatches).

---

## 3. Emmett McBain (Smashing issue 11, demo 22)

### Source

- Black American designer and art director who co-founded Burrell-McBain [stated]. He
  designed about 75 record covers by age 24 [stated].
- Andy admires McBain's colour and "the ways he deconstructed and rebuilt type" [stated].
  The covers he shows (issue-11-03) [observed]:
  - JAZZ in multicoloured blocky letters on purple/black stripes;
  - Bill Harris Jazz Guitar: a giant lowercase "jazz" with an orange-red stencil
    "GUITAR";
  - The Legend of Bix: tall, irregular, slightly tilted vertical slabs of black, purple,
    red and orange on cream;
  - Guitars Woodwind & Bongos: vertical black stripes with stacked coloured circles;
  - CARAVAN: big letters tumbling in different colours;
  - "max max max": the word repeated as a stacked slab.
- Andy's personal theme in this article is selling and speaking to your audience. A
  design must resonate with the people it is for [stated].

### Layout moves (article designs, Citroën DS)

1. **Vertical stripes and circles (design 1, from Guitars Woodwind & Bongos).**
   - Black vertical rules come from `border-left/right` on the paragraph and table,
     plus a centre rule from the cell border, with no extra elements [stated].
   - From 48em the paragraph between the rules turns vertical (`writing-mode:
     vertical-rl; rotate(180deg)`), so the text itself becomes a stripe [stated].
   - Coloured circles holding car fronts (crimson, blue, black, purple, yellow) are
     generated content placed in grid columns 1 and 3 of `repeat(3,1fr)`, with the
     vertical text and the table in column 2 [stated/observed].
   - At 64em main and aside sit side by side (`1fr 1fr`) [stated].
   - A variant swaps the circles for colourful car portraits [observed, issue-11-08].
   - The data table is right-aligned with lining, tabular numerals [stated].
2. **Irregular colour slabs (design 2, from The Legend of Bix).**
   - It uses only header and main [stated].
   - The slabs are one data-URI image on `body::before`, placed in grid columns 1 to 4
     of `repeat(8,1fr)`.
   - The dark header (columns 4 to 7) uses negative horizontal margins (-1.5vw) so it
     overlaps the slabs.
   - Main is in columns 7 to the end.
   - At 82em, a "tweakpoint" adds columns (`repeat(12,1fr)`). Slabs span columns 1 to 8,
     the header 7 to 10, main 9 to the end, all on `grid-row: 1`, so they overlap. A
     second floated slab image (10vw) sits beside the main text [stated].
   - Andy shows a monochrome and a full-colour version side by side: "The monochrome
     version … has an entirely different feeling" [stated, issue-11-11 caption]. In my
     view the colour version carries the jazz [observed].
   - The tilted slab header panel is itself skewed [observed].
3. **A deconstructed type-image (design 3, from CARAVAN).** "Champion de France" is an
   SVG [stated]:
   - outlined words plus individually coloured letters (each with an id), tumbling at
     angles;
   - the DS profile has classed paths so its colours change with the theme.

   At 48em the whole graphic gets `scale(.85) translateY(-4rem) rotate(-20deg)`; "the
   order of these transforms is important" [stated]. The grid is
   `repeat(12,1fr)`, with the header in columns 1 to 8 and main in 8 to the end, "an
   asymmetrical layout from a symmetrical grid" [stated]. The text panel is purple to
   match the car [stated]. A small variant uses `:nth-letter`-style span wrapping (the
   Lettering.js idea without the script) for a multicoloured heading [stated].
4. **A typographic slab plus a reversed aside (design 4, from Bill Harris Jazz
   Guitar).** It is red and black [observed]:
   - a huge lowercase "champion" and an uppercase "DE FRANCE" set as SVG text with tspan
     x/y pairs, to make "a solid slab of text" [stated];
   - paragraphs indented by 2ch with no bottom margins [stated];
   - an aside reversed (dark ground, red text) spanning columns 10 to the end and rows 1
     to 6 of a 12-column grid, a full-height dark band [stated];
   - the car header in columns 3 to span 4; the banner and main in columns 1 to span 8
     [stated];
   - at 48em, two different multicolumn rules: `column-count: 2` for the main text and
     16em-wide columns for the aside [stated].

Demo 22 (Morris Traveller; source: The Legend of Bix cover, observed in
demo22-inspiration.png):

- A red banner holds a slab-serif "TRAVELLER" plus the logo, in the place of the cover's
  "STEREO" band.
- Below it, a full-bleed background SVG of tall irregular slabs (black, purple, crimson
  on blush cream) uses `background-size: cover` from the bottom.
- An 8-column grid at 64em places main in columns 5 to 7, row 2.
- Main is a **black clip-path trapezoid** (`polygon(5% 0, 95% 0, 100% 100%, 0 95%)`)
  holding uppercase red text and the yellow car front, so it reads as one more slab, as
  the cover's text sits inside a black slab.
- At a realistic 900 px height (demo22-1400v) the slabs fill the viewport like the
  cover. In the 3000 px shot, `cover` crops them into a few giant shapes [observed].

### Small screens

- "Those brightly coloured blocks would dominate the limited space available on a small
  screen. Instead, I add the same bright colours to my header" [stated]. The header is
  clipped with `clip-path: polygon(…)`, so the irregular shape survives at every size
  [stated/observed, issue-11-10: a blue tilted panel with the slabs reduced to a few
  coloured bars at the bottom].
- On the phone, design 1 moves the circle motif to the bottom of the page [stated].
  Vertical text appears only from 48em [stated].
- Design 4: "Most of my styling is visible to people who use even the smallest screens"
  [stated].
- He calls small adjustments between breakpoints "tweakpoints", crediting Jeremy Keith
  [stated].
- "I've always viewed the challenge of responsive design as an opportunity to be
  creative and to make the most of every screen size" [stated].
- Demo 22 at 390 [observed, demo22-390-top]:
  - the background slabs are not applied below 64em;
  - what remains is the red banner, then the black trapezoid with text and car on plain
    cream;
  - so the phone keeps one slab, the content slab.

### Quotes (McBain URL)

- "The bright colours and irregular shapes of blocks in this next design are as
  unexpected as the jazz which inspired Emmett McBain's original."
- "Attention to even the smallest details of typography lets people know that every
  aspect of a design has been carefully considered."
- "Elements needed to develop a design needn't be in HTML."
- "I used to think using SVG to render text was as inappropriate as setting text within
  images but having used SVG more, I realize I was wrong."

### Screenshots

- shots/idd/demo22-1400.png: slabs, vh/cover-distorted.
- shots/idd/demo22-1400v.png: realistic; slabs and trapezoid content slab.
- shots/idd/demo22-390-top.png: phone; banner plus a single black trapezoid.
- Article images: raw/idd/img/montage-C/mcbain-1.png (12 covers; the stripes-and-circles
  designs), mcbain-2.png (slab designs, phone version, mono vs colour), mcbain-3.png
  (type-image designs; red/black slab design).

---

## 4. Bradbury Thompson (Smashing issue 12, demos 5, 17)

### Source

- Westvaco *Inspirations* (no budget, so he borrowed plates), Mademoiselle, and Yale
  [stated].
- Andy's reading of Thompson [stated]:
  - pure process colours (C, M, Y, K) separated into different areas of the composition
    and overprinted for depth;
  - historical engravings combined with geometric forms;
  - repeated silhouettes, as in Rain, Rain, Rain: one figure printed five times in
    colours;
  - mirrored line and solid versions, as in Futural.
- Article images I looked at [observed]:
  - Victory: CMY concentric targets overlapping, with engraved arrows flying across
    them;
  - Futural: a line-work aeroplane on the verso and CMYK solid planes overprinting on
    the recto;
  - R Stands for Righteous: giant R and B letterforms in blue/magenta/yellow, cropped by
    the page edges, mirrored and overprinted;
  - W is for War: a big blue W initial with scattered coloured planes.
- The final issue sums up the series. Andy says it made him "more thoughtful in my
  approach to page layout and to the ways a page and its content adapt to different
  screen sizes" [stated].

### Layout moves (article designs, Ford Transit)

1. **CMYK targets behind a cut-out vehicle (design 1).**
   - Darkened CMY tints for the screen: to make a process colour in RGB, set two
     channels to maximum and add black if it is harsh [stated].
   - Big yellow and magenta ring arcs plus a cyan ring overlap behind a magenta van; the
     van/ring overlaps go red [observed, issue-12-08/12].
   - At 48em, an "unusual five-column symmetrical grid" (`repeat(5,1fr)`), with the
     first column left empty so that main and aside are indented [stated].
   - At 64em, a compound grid overlapping 4 and 6 columns, `2fr 1fr 1fr 2fr 2fr 1fr 1fr
     2fr` ("a rhythmic pattern of 2|1|1|2"), rows `100px 14rem 14rem auto`,
     `min-height: 100vh` [stated]. The grid overlay image (issue-12-11) shows the
     uneven column rhythm with the van crossing many columns and the text in columns 7
     to 8 [observed].
   - The headline overlaps the van with a raised z-index [stated].
   - Captions sit beside images rather than under them ("I immediately give designs the
     look of a magazine"), bottom-aligned with `flex-end` and aligned in opposite
     directions [stated].
   - Paragraphs are indented with no spacing, making "solid blocks" of running text
     [stated].
   - The same layout is shown in monochrome (grey rings) and split-complementary
     versions [observed, issue-12-13].
2. **A modular colour header (design 2).**
   - Nine separate van images in complementary colour outlines, rather than one image,
     "to develop various arrangements for different screen sizes" [stated].
   - At 48em they form a 3x3 grid with `grid-auto-flow: column` [stated].
   - At 64em, a magazine spread: `[verso] 1fr [recto] 1fr`. The header fills the verso
     (rows 1 to 4); main and aside stack on the recto [stated]. The verso/recto names
     come from the Latin for facing pages.
   - At 72em the running text goes multicolumn (10em columns) [stated].
   - A named-line content grid of `1fr [svg] 1fr 1fr 1fr` puts the exploded-parts
     illustration in its own narrow track [stated].
   - The headline is moved visually **below** its text (grid-row 2) [stated].
3. **Repeating text masked into a silhouette (design 3).**
   - SVG text of "FORD TRANSIT" repeated in red/yellow/blue/white is clipped to a van
     outline (`clipPath`, `mask-image`) [stated/observed].
   - Below it sits a heavy condensed sans slab, tracked -2px, one colour per line via
     `:nth-of-type` on tspans [stated].
   - At 64em the masked graphic is floated at 65vw with `shape-outside:
     url(mask.svg)`, so the paragraph wraps along the van's silhouette [stated].
4. **Split symmetry with vertical text (design 4).**
   - A 4-column header with rows `100px auto 100px`: the logo sits in the centre columns
     2 to 4, and the headline spans the bottom row [stated].
   - The image fills all cells behind them with a low z-index [stated].
   - In main, the same full-cover image sits behind a paragraph turned vertical
     (`vertical-rl`, `line-height: 3vw`) in columns 2 to 4 with `mix-blend-mode:
     difference` "which also increases the legibility of this text where it appears
     over the graphic" [stated].
   - The image shows translucent yellow, red, blue and grey vans rotated around a
     centre, overprinted where they overlap, like Rain, Rain, Rain [observed,
     issue-12-25].
   - Andy's grid advice: "If you want a framework-based design to be more interesting,
     start by streamlining twelve narrow columns into eight wider ones" [stated, image
     caption].

Demo 5 (Vespa; source: Rain, Rain, Rain, observed in demo05-inspiration.png):

- **Repeated silhouettes with vertical text over them** [observed + CSS].
  - At 72em the page is `1fr 1fr`. The left half is black with the logo and a stacked
    "It looks like a wasp!" headline. The header is a sub-grid `10vw 1fr 1fr 1fr`; the
    h1 is `vertical-lr` in the source but renders horizontally in my shot.
  - The left half also holds one cream top-down scooter: Thompson's single white figure
    on dark.
  - The right half is cream. Four identical top-down scooters in yellow, blue, red and
    black overlap side by side, and the overlapping handlebars mix into green and
    purple.
  - The figcaption runs as ten lines of **vertical uppercase text** (`vertical-rl`)
    directly over the scooters, with `mix-blend-mode: difference`, so it shifts colour
    as it crosses each scooter. Thompson's spread has vertical text over the walking
    figures.
  - Default: a single product shot and a paragraph.

Demo 17 (Fiat 500; source: Thompson's "The Bauhaus Tradition and the New Typography"
spread: a giant black B sliced by a strip of orange Kandinsky images, with italic
captions and rules):

- **A giant letterform sliced by a colour strip** [observed + CSS].
  - At 48em the grid is `repeat(6,1fr)`. The aside takes columns 1 to 4 with an inner
    `1fr 1fr` grid; it becomes `repeat(3,1fr)` at 64em.
  - The narrow text column sits on the left under a short black rule.
  - Next comes a full-height crimson strip with the FIAT roundel, a rear-view outline
    car, and the nuova-500 mark, with pale bands between them, as the B is cut by a
    strip of images.
  - A **huge dark "A"** emerges from behind the strip, cropped by it.
  - The main text is in columns 4 to the end under a long black rule.
  - The heading "L'evoluzione del mito" sits in a medium-weight sans with indented
    paragraphs.

### Small screens

- "On even the smallest screens, some space needs to remain empty. This allows the eye to
  flow around content" [stated].
- Graphics are shrunk deliberately on phones (`max-width: 25vw`, `50vw`) "to add
  white-space and visual interest" [stated]. This is the opposite of the default
  full-bleed image.
- "Before implementing any design, I often make a storyboard" [stated].
- In design 2 the phone gets layout from the start: the nine vans become a horizontal
  scroller. Main and aside each get a small two-column grid (`[content] 1fr [svg] 100px`,
  mirrored as `[svg] 100px [content] 1fr` in the aside), so the illustration column swaps
  sides between sections. "It's sometimes beneficial to use more than a single-column
  layout for small screens" [stated].
- Design 3: "Applying an alternative mask image preserves the visual weight of this
  masked header on smaller screens" [stated]. This is a different silhouette crop for
  the phone, not a scaled-down copy.
- Demo 5 at 390 [observed, demo05-390-top]:
  - a `<picture>` swaps the vertical scooter for a **horizontal (rotated) one** under the
    centred headline;
  - the four coloured scooters stay as one overlapping group at reduced scale;
  - the vertical caption becomes a horizontal uppercase navy block;
  - the overprint survives, the vertical-text device does not.
- Demo 17 at 390 [observed, demo17-390h]:
  - the crimson strip becomes a crimson panel with the roundel, then the headline and
    text;
  - the giant cropped "A" and the rules are gone;
  - the phone keeps colour and emblem but loses the letterform idea.

### Quotes (Thompson URL)

- "Using a compound grid—two or more overlapping or stacked grids—on one page can create
  eye-catching compositions."
- "When I place captions on either the left or right of an image, I immediately give
  designs the look of a magazine."
- "While vertical text won't suit every design, it can turn a short passage into a strong
  visual statement."
- "Learning how people interact with a website or use a product shouldn't dictate a
  design but instead provide a platform on which to develop engaging, entertaining, and
  ultimately more memorable experiences."

### Screenshots

- shots/idd/demo05-1400.png: black/cream halves, overprinted scooters, vertical captions.
- shots/idd/demo05-390-top.png: phone; rotated scooter, horizontal caption block.
- shots/idd/demo17-1400.png, demo17-1400v.png: crimson strip slicing the giant "A",
  rules, text columns.
- shots/idd/demo17-390h.png: phone first screen.
- shots/idd/demo17-390-top.png: vh-inflated red panel (artifact).
- Article images: raw/idd/img/montage-C/thompson-src.png (W is for War, America at War,
  Victory, Futural, R Stands for Righteous), thompson-1.png (CMYK van design, mono
  variant, compound-grid overlay), thompson-2.png (modular van header, verso/recto,
  grid overlay), thompson-3.png (masked repeating type, split-symmetry vans, 8-column
  grid overlay).

---

## Cross-issue patterns seen in this group

Recurring moves:

- **A small saturated palette with overlap made visible.** Four of the four issues use
  `mix-blend-mode: multiply` (or overlay, difference, luminosity, soft-light) so that the
  overlap of two flat shapes produces a third colour:
  - Huber's cyclists, as Vespa silhouettes;
  - Pintori's squares, as Trabant frames;
  - Thompson's CMY rings and repeated figures;
  - McBain's slabs, by contrast, rely on adjacency rather than overprint.

  This is the web stand-in for print overprinting. It works only with 3 to 4 flat,
  saturated hues plus a dark and a light neutral [stated + observed].
- **One product, many outline drawings.** Every design depicts the subject (Trabant,
  Morris, Citroën, Ford, Vespa, Fiat) as line drawings or flat silhouettes, repeated,
  offset, recoloured, rotated or overlapped. Photos are rare: only Huber design 1, where
  it is blended into a circle. Flat vector art is what lets colour and overlap carry the
  composition [observed].
- **Symmetric grid, asymmetric placement.** Andy repeats it in three issues: an even
  `repeat(n,1fr)` with deliberately empty columns or uneven spans gives the asymmetry
  [stated]. Compound grids (`2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`, the 6+4 and 4+6
  overlaps) appear twice [stated]. Odd counts (5 columns) and 8 rather than 12 columns
  are explicit advice [stated].
- **Type as image.** Examples:
  - giant numerals (57, 3,096,999, 6.3, 40, 7,450) with a small light unit;
  - vertical text (`vertical-rl` plus `rotate(180deg)`) as a stripe or a caption over
    imagery;
  - deconstructed multicoloured letters;
  - repeated words masked into a silhouette;
  - a giant cropped letterform.

  Text set in SVG is accepted as accessible [stated].
- **A full-height colour strip or slab as a structural element.** Examples:
  - McBain's stripes as borders and slabs as a clip-path trapezoid;
  - Thompson's crimson strip in demo 17;
  - Huber's horizontal white strips in demo 7;
  - Pintori's thick border bars in demo 18.
- **Source fidelity.** Each 52-weeks demo maps one specific print piece almost 1:1
  (composition, palette, device) onto a new subject. The concept comes from transplanting
  the source's single dominant device, not from a brief [observed].
- **Small screens: keep the vocabulary, drop the overlap.** Across nine demos the phone
  keeps:
  - the palette;
  - one or two signature shapes (a clipped panel, a single square frame, the slab);
  - the big-numeral or type-image hierarchy.

  It loses multi-element overlap, rotation, and vertical text [observed]. Andy's own
  tools for this:
  - horizontally scrolling image strips (four times in this group);
  - `<picture>` art direction, which swaps the crop or orientation;
  - moving a decorative shape into the header's colour or clip-path;
  - alternate mask images;
  - small two-column grids on the phone;
  - grid reordering so that the brand and image come first;
  - deliberately shrunk graphics for white space [stated].

  Type-image SVGs (demos 14 and 19, the McBain type-image) survive best at 390
  [observed].
- **Colour is tested in variants.** Issues 10, 11 and 12 each show the same layout in
  monochrome and in full or split-complementary colour, to show that colour changes the
  feeling [stated/observed]. Dark mode brightens colours by about 10% rather than
  inverting them [stated].

Tensions and contradictions:

- Andy says he gravitates to monochrome because colour is hard [stated], yet every demo in
  this group is strongly multicoloured. Monochrome appears only as a comparison variant.
- The strongest compositions (demos 7, 16, 22, 5) depend on layering at desktop width.
  At 390 they degrade to stacked blocks, and demo 7's scroller hides most of the
  overlap. His claim that the phone keeps the art direction holds for type-led designs,
  less for overlap-led ones [observed].
- Several demos tie heights to `vh` and `cover`, which makes the composition fragile
  across viewport heights (visible in my shots). Demo 18 also has a phone-only contrast
  bug [observed].
- Pseudo-elements and data URIs carry the "design" while the HTML stays minimal
  [stated]. That is good practice, but it means the decorative layer is invisible in
  content management. A small-business site maintained by others would need these
  shapes as named, reusable components instead [my inference].
