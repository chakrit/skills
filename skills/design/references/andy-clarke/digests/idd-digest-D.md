# IDD digest, group D: 52-weeks demos 6, 8, 10, 12, 13, 23, 24, 25, 26, 32

Scope: Alvin Lustig (6), Lester Beall (8, 26), Ladislav Sutnar (10), Armin Hofmann (12,
32), David Carson (13), Herbert Matter (23), Dan Friedman (24), Erik Nitsche (25).

## Read this first: what the sources can and cannot support

- **The blog posts carry no design reasoning.** Each "52 weeks" post is one paragraph:
  "I've committed to designing 52 designs", a short designer biography, and the preview
  image. Not one sentence explains a layout choice. I checked the 2020 Wayback copy of
  #13; it was equally thin [observed]. #32 has no post of its own; it is part of
  https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-27-32/ (the
  same biography-only treatment). Anything in this digest about *why* is my inference
  from the work and is marked [observed]. The only [stated] material is the brief
  "Inspired by" text on each demo page, plus his choice of which source image to show
  next to the demo.
- **Every demo pairs one source image with one web layout.** Each demo page shows the
  design, then "Inspired by <designer> #N", a bio, a quote from or about the designer,
  and `inspiration.png` (the print piece he worked from). I downloaded every
  `inspiration.png` (the print source) and every `preview.png` (his own 1440x1024 render
  of the design) to `raw/idd/img/insp-NN.png` and `raw/idd/img/preview-NN.png`. Most of
  the analysis below compares those two images.
- **The live pages are partly degraded.** The demos now sit inside the 2024+ Stuff &
  Nonsense site shell, and some fonts and CSS variables have drifted:
  - #12 uses `grid-template-columns: var(--grid-compound-6-4)`, which no current
    stylesheet defines.
  - #10's italic serif is gone, so its vertical text now collides with the headline.
  - Several `#design` blocks size to the viewport, so my tall screenshots show long
    empty bands. That comes from my screenshot method, not from his design.
  - #12's type is `4vmax`, so the 390 shot, taken in a 2200 px tall iframe, inflates
    it to about 88 px. On a real 390x844 phone it would be about 34 px.

  Where the live render and `preview.png` disagree, I treat the preview as the intended
  design [observed].
- **The extracted CSS includes breakpoints.** Per-demo CSS, with each rule's media
  query, is in `raw/idd/D/css-NN.txt`. The breakpoints are 48em (768 px) and 64em
  (1024 px).

Raw files: `raw/idd/D/blog-*.txt`, `raw/idd/D/demoNN.txt` (page text, URL first line),
`raw/idd/D/*.html`. Extraction scripts: `scripts-idd/html2txt-D.py`,
`scripts-idd/css-D.py`.

A shared subject runs through the group [observed]. Every demo sells a classic European
vehicle (Vespa, Mini, Fiat 500, Citroën DS, Ford Transit) using drawn vector art and
short factual copy. The same subject is redrawn in the idiom of different designers:
Vespa in 6 and 10, Mini in 8, 12, and 32, Citroën in 23 and 24, Transit in 25 and 26.
Because the content stays constant, the variable is purely art direction, and that is
the point of the exercise.

---

## #6 Alvin Lustig: Vespa

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/6/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-6-alvin-lustig/

1. **Source.** Lustig's cover for *World Inventors Exposition* (insp-06.png): mustard
   ground, a black band crossing the lower-left, a pale head that breaks up out of the
   band, a red square and a cream square locked together at the right edge, and
   three-line italic serif type in white, red, and black stacked down the left [observed].
   The page text [stated] credits only Lustig's book covers and his New Directions work.
   What Andy took [observed]:
   - the whole block composition, almost one-for-one;
   - the three-colour type stack, with each line in a different colour;
   - the object breaking out of a flat colour band.
2. **Layout moves** [observed unless noted]:
   - **Colour-block scaffold made of empty grid items.** Empty `.bg-black`, `.bg-white`,
     and `.bg-red` divs are placed on the grid as solid rectangles. At 64em the layout
     uses `grid-template-columns: repeat(6, 1fr)` and
     `grid-template-rows: repeat(6, 1fr)`:
     - the black slab spans columns 1–5, rows 3–5 (4 of 6 columns, about 2/3 of the
       width, two rows);
     - the white square is column 5, row 5;
     - the red block is column 6, row 4.
     The white and red blocks touch only at a corner, exactly like the Lustig squares.
     The default would be a photo hero with a heading laid over it.
   - **Illustration breaks out of the band.** The cream side-view Vespa sits in columns
     1–5, rows 1–4, aligned to the end of its area, so its seat and headlamp rise above
     the black slab into the yellow while the wheels sit inside the black.
   - **Second view as a texture element.** A thin red outline top-view of the scooter
     stands upright in column 5, rows 1–5, filling the vertical gap. It echoes Lustig's
     wire "lung" form.
   - **Logo straddles a colour boundary.** The Vespa wordmark spans columns 5 to the
     end of the grid in row 5, so it begins on the white square and runs out onto the
     yellow.
   - **Type stacked as three separate grid items.** The three sentences ("Vespa is an
     Italian brand of scooter" / "Manufactured by Piaggio" / "The name means wasp in
     Italian.") are three `<span>`s in rows 4, 5, and 6 (columns 1–3). They are coloured
     white (on black), red, and black, at `--font-size-xl`, in a light serif. The text
     is left-aligned with a lot of air; there is no paragraph.
   - **Palette:** `#f2c867` mustard, `#000`, `#fff`, `#a73448` crimson. This crimson and
     mustard pair recurs across the whole series.
3. **Small screens.**
   - Below 48em the grid is dropped: everything is centred in a single column in this
     order: logo, scooter, the three sentences run together as one centred paragraph,
     then the outline top-view.
   - The three colour blocks become three 60 px circles in a row, a palette swatch
     (demo06-390). This keeps the colour story as a token instead of trying to squeeze
     the composition.
   - **Intermediate step at 48em:** a three-column version (`repeat(3, 1fr)`) with the
     black slab across columns 1–2, then six columns from 64em.
4. **Quotes.**
   - Page epigraph (Lustig): "I make solutions that nobody wants to problems that don't
     exist." [stated, demo page]
   - No reasoning in the post.
5. **Shots.**
   - demo06-1400: the 64em composition; the top band is empty because of the 6×1fr rows
     in a tall window.
   - demo06-390: the centred stack with three circles. The long yellow tail below is a
     viewport artefact.
   - preview-06.png is the intended composition.

## #8 Lester Beall: Mini and *The Italian Job*

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/8/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-8-lester-beall/

1. **Source.** Beall's Rural Electrification Administration poster "A Turn of the Hand"
   (insp-08.png): a red sky, a band of blue-and-white horizontal stripes, a cut-out
   black-and-white photo of a farmer, and the title on a tilted banner [observed]. The
   page text [stated] names his bright primary colours, bold lines and shapes, and
   photomontage.
2. **Layout moves** [observed]:
   - **Diagonal section edges via `clip-path`.**
     - The crimson header is clipped with `polygon(0 0, 100% 0, 100% 50%, 0% 100%)`, so
       its bottom edge slopes up to the right.
     - The blue `main` is clipped with `polygon(0 0, 100% 20%, 100% 100%, 0 100%)`, so
       its top edge slopes down to the right.

     The two slopes do not match. The wedge between them shows the grey ground (#e6e6e6)
     and the stripe image. The default would be flat horizontal section breaks.
   - **Cut-out photomontage crossing both diagonals.** A black-and-white cut-out of
     Michael Caine and Benny Hill (from *The Italian Job*) sits on blue/white stripes,
     right-aligned, with `margin-block: -100px` top and bottom. It therefore overlaps
     the header and the main panel, and heads sit over the headline "They said it would
     never sell".
   - **One retro display face for everything.** Cooper Black is used for the headline,
     the subhead, and even the 2-column body text (`column-count: 2`). A small
     Mini Cooper laurel badge is absolutely positioned in the column gutter
     (`translateX(-35px)`), like a pull-ornament.
   - **Palette:** crimson #a73448, sky blue #4697cd, and the white stripes.
3. **Small screens.**
   - Below 48em the clip-paths are removed, so the sections become plain rectangles.
   - The photo keeps a smaller negative margin (−50px), so it still overlaps the
     headline. The montage survives (demo08-390).
   - The body becomes one column and the badge drops to the end.
4. **Quotes.**
   - Page quote (Herb Lubalin on Beall): "taking American graphic design of the 1930s
     out of its mundane, tasteless form" [stated, demo page]
   - No reasoning in the post.
5. **Shots.**
   - demo08-1400: the full composition.
   - demo08-390: the stacked version with the overlap kept.

## #10 Ladislav Sutnar: Vespa

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/10/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-10-ladislav-sutnar/

1. **Source.** Sutnar's spread for Furniture Forum and Knoll (insp-10.png). It contains:
   - a yellow light-beam wedge falling from the top onto an Eames chair;
   - a black square at the top;
   - a red elliptical shadow under the chair;
   - vertical captions running up beside images;
   - a pale yellow panel holding two stacked photos.

   [observed] The page text [stated] calls Sutnar an information-design pioneer who
   made large amounts of data accessible.
2. **Layout moves** [observed; from preview-10.png and the CSS, because the live page
   is degraded]:
   - **Rigid modular grid with fixed row heights:** `grid-template-columns:
     repeat(6, 1fr)` and `grid-template-rows: repeat(8, 110px)`, making a 6×8 module
     sheet. The default would be content-height rows.
   - **The light-beam wedge** is a yellow div in column 3, rows 1–3, with a tapering
     shape; it points down onto the scooter. The black Vespa-logo square in column 4,
     rows 1–3, sits beside it. Together they form a hard top edge.
   - **Shadow as ground.** The crimson scooter sits on a flat crimson ellipse, Sutnar's
     red shadow.
   - **Three captions set vertically.** `writing-mode: vertical-rl` plus
     `rotate(180deg)` makes them read bottom to top, Sutnar-style. They sit in column 1
     (rows 2–8), column 4 (rows 5–8), and column 6 (rows 2–8). The text becomes thin
     vertical rules that frame the illustration. The default would be captions under
     the images.
   - **Grey panel behind the photos.** A `#design::after` panel (#eaeaea, columns 5–6,
     rows 3–8) sits behind two stacked black-and-white detail photos (`figure`,
     columns 5–6, rows 4–8). It echoes Sutnar's yellow panel.
   - **Ornament and background.** A small red wheel-disc ornament sits in column 4,
     row 4, and a huge pale grey wheel is a background image bottom-left.
   - **Type:** a single italic headline, "It looks like a wasp!", in a light face at
     top-left, plus small italic serif captions. White space dominates the left half.
3. **Small screens.**
   - The grid is applied only from 64em. Below that, everything stacks: black logo
     block, headline, scooter, the captions as horizontal paragraphs, photos, then the
     disc (demo10-390).
   - The beam, the vertical text, and the panel all disappear. The art direction is
     effectively lost, leaving a clean article.
4. **Quotes.**
   - Page epigraph (Sutnar): "With function, flow, and form as basis, design is
     evaluated as a process" [stated, demo page]
5. **Shots.**
   - demo10-1400 and demo10b-1400: the live page, where vertical text now overlaps the
     wrapped headline because of a font fallback.
   - demo10-390: the stacked view.
   - preview-10.png: the intended composition.

## #12 Armin Hofmann: Mini

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/12/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-12-armin-hofmann/

1. **Source.** Hofmann's "Herman Miller Collection" poster (insp-12.png). Black chair
   silhouettes cascade diagonally from top-right to bottom-left. The red sans-serif text
   is ragged and stacked, with some lines outdented ("Verkauf ab / 9. März" hang left of
   the rest), plus a single footer line at bottom-right [observed].
2. **Layout moves** [observed]:
   - **Compound grid.** He uses `grid-template-columns: var(--grid-compound-6-4)`; items
     use lines up to 9, so it is an 8-track compound grid. The site's current sibling
     `--grid-4-6` is `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`. A 4+6 compound gives uneven
     tracks, not 12 equal ones. This is a Layout ❤︎ grid.
   - **Rotated, repeated object as a cascade.** Four copies of the same Mini front-view
     SVG are placed in different cells at different sizes:
     - columns 5, 6–9, 5–8, and 2–5;
     - rotated +15°, −15°, 0°, and −15°;
     - nudged with `translate(2.5vw, -10vh)`.

     They tumble from small at top-centre to large at bottom-left, mirroring Hofmann's
     chair cascade. White abstract shapes behind them, a background image at the right
     bottom, stand in for movement.
   - **Hanging indent in display type.** The text block "Icon / of the / 1960s /
     produced by / British / Motor / Corporation / 1959–2000" is set in a bold grotesk
     (sk-modernist-bold) at `4vmax`, line-height 1, crimson. One span ("produced by")
     gets `margin-inline-start: -5vw`, so it hangs out to the left of the stack: a
     direct copy of Hofmann's outdented line. The default would be a centred headline.
   - **Footer line.** A second text line, "The said it would never sell" (sic), sits
     bottom-right like the poster's footer.
   - **Palette:** off-white #ecede9, black, and crimson type only.
3. **Small screens.**
   - The grid applies only from 64em. Below that the order is: badge, the text stack,
     then one car only (demo12b-390); the cascade is reduced to a single image.
   - Viewport-relative type (`4vmax`) is meant to scale the headline. In my
     tall-iframe shot it overflows.
4. **Quotes.**
   - Page epigraph (Hofmann): "a poster does more than simply supply information on the
     goods it advertises; it also reveals a society's state of mind." [stated, demo page]
   - Page text: "His Graphic Design Manual is still a fabulous reference for graphic and
     web designers." [stated]
5. **Shots.**
   - demo12-1400: the tall window inflates the vmax type.
   - demo12b-1400: closer to intended, but columns are degraded because the variable is
     undefined.
   - demo12-390 and demo12b-390: the stacked view.
   - preview-12.png: the intended composition.

## #13 David Carson: Fiat 500

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/13/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-13-david-carson/

1. **Source.** Carson's *Ray Gun* spread on Jane's Addiction (insp-13.png). The left
   page is white:
   - a huge all-caps condensed justified standfirst with distressed, broken letterforms;
   - band names in bold within it;
   - dense two-column body text below.

   The right page is a full-bleed colour photo with distressed type across it
   [observed].
2. **Layout moves** [observed]:
   - **Two halves, two moods.** At 64em the layout is `grid-template-columns: 1fr 1fr`.
     Main (text) goes in column 1 and header (image) in column 2. This is a plain
     symmetrical split; the energy comes from texture, not from the grid.
   - **Distressed type via CSS mask.** The standfirst and the h1 are Oswald all-caps at
     3–4rem with `mask-image: url(mask.png)`, a scratchy texture that eats into the
     letters. Key words (`<b>`: "Cinquecento", "city car", "Fiat", "1957–1975") are
     coloured magenta-pink #bf78af, like Carson's bold band names. The default would be
     clean display type.
   - **Body text at whisper size.** The body is a two-column text block at 11 px under
     the 3rem standfirst. The contrast in type size (roughly 4.5:1) is the composition.
   - **Layered, tilted panels on the image side:**
     - a magenta ground (#bf78af) with a brush-stroke texture;
     - a translucent pink polygon (`clip-path: polygon(15% 0, 50% 10%, 100% 10%,
       100% 100%, 70% 90%, 0 100%)`);
     - a translucent pink card rotated −5°;
     - a car outline SVG rotated +10°.

     On hover, the card and the SVG straighten to 0°, a small piece of play.
   - **Headline type on the image side.** "L'evoluzione del mito" is set in a light
     face.
3. **Small screens.**
   - Below 64em the image panel comes first (source order puts the header first; the
     desktop grid swaps it to the right), then the distressed standfirst, then body text
     in one column (demo13b-390).
   - The mask, the rotation, and the colour keywords all survive. This is one of the
     best-preserved small-screen versions in the group.
4. **Quotes.**
   - Page epigraph (Carson): "Graphic design will save the world right after rock and
     roll does." [stated, demo page]
5. **Shots.**
   - demo13-1400 and demo13b-1400: the split.
   - demo13-390 and demo13b-390: image first, then distressed type.
   - preview-13.png: matches.

## #23 Herbert Matter: Citroën DS

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/23/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-23-herbert-matter/

1. **Source.** Matter's Knoll ad for the Bertoia chair (insp-23.png):
   - a black ground;
   - a giant white wire-mesh chair drawing;
   - a huge blue "K" monogram running behind it top to bottom;
   - a small chair photo at right;
   - right-aligned body text bottom-right;
   - a centred footer line.

   [observed] Page text [stated]: Matter was known for photomontage in commercial art.
2. **Layout moves** [observed]:
   - **Brand mark scaled up as structure.** The Citroën double chevron, in blue #3a7fb0,
     is drawn huge behind a white-line front-view DS. It is the background image at
     `background-position: 50% 100px`, crossing the car's headlights, just as the "K"
     runs through the chair. The default would be a small logo in the header.
   - **Line drawing on black.** Line art over a solid brand shape gives the layered,
     transparent montage effect without photography.
   - **12-column grid used asymmetrically.** He uses `repeat(12, 1fr)`:
     - banner (front view) in columns 4–10, a centred 6/12 block;
     - aside (rear view) in columns 1–4, aligned to the bottom;
     - main text in columns 9–12, row 2, right-aligned;
     - a full-width footer of bullet-separated keywords in bold extended caps.

     The rear view (bottom-left) and the text (right) make a diagonal counterweight
     around the central car. This is one of the few demos using a plain 12-column grid,
     but no column holds a "card".
   - **Right-aligned body text.** Body copy is `text-align: right`, matching Matter's
     ragged-left text block.
   - **Type:** moderna-sans; the heading is in a bold extended uppercase cut.
3. **Small screens.**
   - The order is: front view with chevrons, side view, heading, body text (still
     right-aligned), rear view, keyword footer (also right-aligned) (demo23b-390).
   - The chevron montage survives because it is attached to the background of the
     stacked image.
4. **Quotes.**
   - Page epigraph: "If you love something, the work will be just fine." [stated, demo
     page]
5. **Shots.**
   - demo23-1400 and demo23b-1400: chevron montage.
   - demo23-390 and demo23b-390: the stacked view.
   - preview-23.png: the full intended layout. Its alt text in the post wrongly says
     "Emmett McBain".

## #24 Dan Friedman: Citroën DS

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/24/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-24-dan-friedman/

1. **Source.** Friedman's Yale Symphony Orchestra poster (insp-24.png):
   - the whole poster is one giant black "B";
   - a halftone cloud fills the top of the B;
   - a small white "B" and other content sit inside the black letter;
   - small sans-serif text blocks are scattered in the counters.

   [observed]
2. **Layout moves** [observed]:
   - **The page is a letter.** At 64em the entire `#design` box is masked with
     `mask-image: url(bg.png)` and `mask-size: 100% 100%`, a giant "D" shape. The
     component's outline is a letterform, not a rectangle (demo24b-1400). The default
     would be a rectangular hero.
   - **A second letter inside the first.** A big white "S" sits inside the D, so the
     composition literally spells "DS".
   - **Halftone as texture.** A halftone-dot photo of the car, as a pseudo-element
     spanning all columns in row 1, fills the top of the D like Friedman's halftone
     cloud.
   - **Scattered text on a 12-column grid:** `repeat(12, 1fr)`.
     - The badge (chevrons) is in column 10, nudged down with `translateY(5vh)`.
     - Main text is in columns 5–10 with a 7vw inline indent, so the heading and the
       paragraph are offset from each other.
     - Small text blocks are in columns 2–4 (rows 2 and 3).
     - The keyword footer is in columns 6–9.

     Text blocks sit in the D's counter at irregular positions, as in the poster.
   - **Type:** small bold extended uppercase labels; all text is small, and the letters
     are the display type.
3. **Small screens.**
   - The D mask applies only from 64em. Below it, the result is a black rectangle: the
     halftone strip, the chevrons, the heading, the text, and the keyword footer, all
     left-aligned (demo24b-390). The giant S is gone.
   - The letterform concept does not survive. The small-screen view keeps only black
     plus halftone as the mood.
4. **Quotes.**
   - Page epigraph (Friedman): "Bridge the boundaries that separate us from other
     creative professions and unexpected possibilities" [stated, demo page]
5. **Shots.**
   - demo24-1400 and demo24b-1400: the D mask, cut off at the top.
   - demo24-390 and demo24b-390: the rectangle.
   - preview-24.png: the intended composition.

## #25 Erik Nitsche: Ford Transit

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/25/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-25-erik-nitsche/

1. **Source.** Nitsche's General Dynamics ad "atom city… under the sea!" (insp-25.png):
   - a city drawing at top projects a perspective beam, made of horizontal bands, down
     to a submarine at the bottom;
   - the text block is set with a slanted left edge that follows the beam;
   - a tracked-out sans wordmark is at the bottom.

   [observed] Page text [stated]: Nitsche's "meticulous attention to details of page
   composition".
2. **Layout moves** [observed]:
   - **Perspective beam as the spine.**
     - A `#design::before` pseudo-element (#dfdfe3) is clipped to `polygon(0 0, 50% 0,
       100% 100%, 0 100%)`, a trapezoid widening downward over columns 3–5, rows 1–6.
     - It has a horizontal stripe background in two different stripe densities
       (`background-position: 0 0, 0 245px`).
     - It runs from the front-view van (top, column 3) to the side-view van (bottom,
       columns 3–5).

     The default would be two images in separate sections.
   - **Text shaped to the beam.** The body text (columns 4–5, row 3) uses a
     `p::before` float with `shape-outside: polygon(0 0, 150px 700px, 0 700px)`, so its
     left edge is a diagonal. Each line starts further right than the one above,
     matching the beam's slant. This is the most direct print-to-CSS translation in the
     group.
   - **Headings offset across the beam.** "MORE VAN, MORE VALUE" spans columns 2 to the
     end of the grid, so it starts left of the beam. "FORD TRANSIT" spans columns 4 to
     the end, below the van.
   - **Grid and images.** The grid is `repeat(6, 1fr)` with a large row gap. Images get
     a −30px inline margin so they overhang their columns slightly.
   - **Type and colour:** condensed bold uppercase headings (italic in the preview). The
     palette is greys plus van-grey; it is monochrome.
3. **Small screens.**
   - Below 64em it is a plain stack: van front, heading, text (straight left edge), van
     side, "FORD TRANSIT" (demo25b-390).
   - The beam and the shaped text are lost.
4. **Quotes.**
   - Page text: Nitsche's "hallmarks were clarity, vibrant colors, smart typography"
     [stated, demo page]
5. **Shots.**
   - demo25-1400 and demo25b-1400: beam and slanted text.
   - demo25-390 and demo25b-390: the stack.
   - preview-25.png: matches.

## #26 Lester Beall: Ford Transit

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/26/
Post: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-26-lester-beall/

1. **Source.** Beall's REA "Wash Day" poster (insp-26.png):
   - a blue sky over a mustard ground, divided by a hard horizon at about 55% height;
   - a black house silhouette containing a white washing machine;
   - five white arrows converging on it from the right;
   - a centred title, and bottom text in condensed caps.

   [observed]
2. **Layout moves** [observed]:
   - **Two-colour horizon split.** The blue #2c6185 `#design` area holds the headline
     and the image. The mustard #f2c867 `main` spans full width below, with the text.
     The hard horizontal edge between them is the composition. The default would be
     sections of equal visual weight.
   - **Silhouette within silhouette.** A black Transit silhouette contains a white
     small-van silhouette (the message: more van). The image is in columns 1–6 of a
     6-column grid, inset by `--spacing-l`.
   - **Converging arrows as an attention device.** Five white arrows come from
     `#design::after` (columns 4–6, row 2, translated by spacing-l and spacing-xl).
     They overlap the van's nose and cross the horizon into the mustard area, pointing
     at the product exactly as in Beall's poster. Arrows that cross a section boundary
     tie the two bands together.
   - **Type:** the headline "MORE VAN, MORE VALUE" is 72 px condensed bold mustard
     caps, centred. Body text is small uppercase condensed, in multi-column flow
     (`column-width: 22em`).
3. **Small screens.**
   - The order is: blue band with the headline, then the silhouette pair; the arrows
     are dropped (they apply only from 64em); then the mustard band with one-column
     caps text (demo26b-390).
   - The horizon split and the two-colour palette survive; the arrows do not.
   - **Intermediate step:** from 48em the grid and the 72 px headline apply; from 64em
     the arrows are added.
4. **Quotes.**
   - Same Lubalin quote as #8 [stated, demo page].
   - The post's only addition is a bio line on Beall's "distinctive use of
     photomontage".
5. **Shots.**
   - demo26-1400 and demo26b-1400: the composition.
   - demo26-390 and demo26b-390: the stacked view.
   - preview-26.png: matches.

## #32 Armin Hofmann: Mini

Demo: https://stuffandnonsense.co.uk/inspired-design-decisions/32/
Post (shared): https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-27-32/

1. **Source.** Hofmann's Kunsthalle Basel poster for Henry Moore and Oskar Schlemmer
   (insp-32.png): two giant abstract black forms fill the sheet. A small red sans-serif
   text block is rotated about 15° and wedged into the narrow waist where the forms
   touch [observed].
2. **Layout moves** [observed]:
   - **Extreme crop as abstraction.** The header's background image is a huge close-up
     of the Mini's headlamp and wing: black bodywork and white glass filling 4/6 of the
     width, cropped until the car is almost abstract. This is the equivalent of
     Hofmann's sculpture forms. The default would be the whole car, centred.
   - **Small rotated text in the waist of the form.** The red text block "Icon of the
     1960s / produced by / British Motor Corporation / 1959–2000" is:
     - in grid column 3 of a nested 4-column header grid (`grid-template-columns:
       repeat(4, 1fr)` inside columns 1–5);
     - rotated 15°;
     - placed where the headlamp ring meets the body;
     - set with a 2rem indent and an outdented span (`margin-inline-start: -2rem`).

     Tiny type against enormous form.
   - **Page split.** The 6-column page puts the header (the crop) in columns 1–5,
     column 5 left empty as grey breathing space, and the text in a narrow column 6
     under a Mini Cooper badge. The ratio is about 4:1:1, so the text gets a sixth of
     the width.
3. **Small screens.**
   - The crop is replaced by the whole Mini front view, centred, with the headline text
     centred below it, unrotated.
   - The badge floats left inside the body text with `shape-outside: circle()` and
     `shape-margin: 10px`, so the text wraps round it (demo32b-390).
   - So on small screens he swaps the image crop rather than scaling the desktop crop
     down. This is a deliberate art-directed image change, and he adds a different
     flourish (text wrapped round a circle) in place of the rotation.
4. **Quotes.** Same Hofmann epigraph as #12 [stated, demo page].
5. **Shots.**
   - demo32-1400 and demo32b-1400: crop, rotated type, and a narrow text column.
   - demo32-390 and demo32b-390: the full car and the circle-wrap.
   - preview-32.png: matches.

---

## Cross-issue patterns seen in this group

All [observed] unless marked.

- **Copy one print piece's skeleton, then swap in the client's subject.** Every demo
  keeps the source's composition nearly intact: the band, beam, letter, horizon, or
  cascade. Only the subject matter changes. He does not blend sources; one demo, one
  reference. Comparing insp-NN.png with preview-NN.png is the clearest evidence of his
  method.
- **The same content redrawn in different idioms.** Vespa ×2, Mini ×3, Citroën ×2,
  Transit ×2. This proves the layout, not the content, carries the personality. It is a
  useful exercise for us: one client brief, several source-led directions.
- **A big structural shape behind or around the subject:**
  - a light beam (10);
  - a perspective beam (25);
  - a brand chevron (23);
  - a giant letter mask (24);
  - a colour slab (6);
  - a horizon split (26).

  These shapes are made with pseudo-elements, `clip-path`, `mask-image`, or empty grid
  items, not images. This shape is what replaces the "hero section".
- **Text treated as shape.**
  - vertical captions (10);
  - a slanted text edge via `shape-outside` (25);
  - rotated small text (32);
  - outdented hanging lines (12, 32);
  - distressed type via mask (13);
  - a stacked three-colour sentence (6).

  In each case body copy is short and becomes part of the picture.
- **Extreme scale contrast.** Huge forms (crop, letter, chevron) against tiny type:
  11 px body under a 3rem standfirst (13), 4/6 crop versus a 1/6 text column (32).
- **Diagonals and rotation from one or two moves:** a clip-path slope (8), ±15° rotation
  (12, 32), −5° and +10° tilt (13), converging arrows (26).
- **Grids are a means, not a look.**
  - Fixed modular rows: `repeat(8, 110px)` (10).
  - A compound 4+6 grid (12).
  - A nested 4-column header grid (32).
  - Plain `repeat(12, 1fr)` or `repeat(6, 1fr)` elsewhere, but with asymmetric spans
    and deliberately empty tracks: column 5 in #32, the empty yellow rows in #6.

  Even on 12 columns, nothing reads as equal cards.
- **Recurring palette:** mustard #f2c867 and crimson #a73448 recur (6, 8, 10, 12, 26,
  32), with black, off-white, and one blue. These are flat colours only, with no
  gradients except the subtle panel in #10.
- **Small screens: concept-level fallback, not shrinking.** Most demos (6, 10, 12, 24,
  25) turn the grid on only at 64em and fall back to a simple centred or left stack.
  The showpiece device is often dropped entirely: beam, letter mask, arrows, vertical
  text. What survives is colour, the montage overlap, and the display type. The
  better-kept cases are worth copying:
  - **#32 swaps the image** (full car instead of the crop) and **adds a different
    flourish** (`shape-outside: circle()` wrap).
  - **#13 reorders** so the image comes first and keeps every texture.
  - **#6 reduces the colour slabs to a swatch row of circles.**
  - **#8 keeps a smaller negative-margin overlap.**

  Intermediate 48em steps exist in #6 (three columns) and #26 (grid on, arrows off).
- **Contradictions and tensions.**
  - #13 uses a plain 50/50 split and #23 a centred 12-column composition. These are
    symmetry choices, so asymmetric grids are not a fixed rule; the source decides.
  - Several demos lose most of their art direction under 64em, so these weekly sketches
    are weaker evidence for his small-screen method than the Smashing articles (other
    groups). Treat #32's art-directed image swap and #13's reorder as the transferable
    small-screen moves.
  - The blog posts give no reasons, so any claim about his intent from this group is
    inference.
