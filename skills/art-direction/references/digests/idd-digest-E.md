# IDD digest, group E: demos 27-31, 33-40 (2020 "52 weeks" series)

Demos: https://stuffandnonsense.co.uk/inspired-design-decisions/<N>/
Blog posts:
- 27-31 share one catch-up post:
  https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-27-32/
  (the per-number URL pattern 404s for 27-31).
- 33-40: https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-<N>-<slug>/

Raw material: raw/idd/demoE/ (demo HTML, blog HTML and .txt, css<N>.txt = the demo's own
CSS and markup pulled out of the page). Extraction scripts: scripts-idd/E/.

## Read this first: what the sources do and do not contain

- **The blog posts say nothing about the design decisions.** [observed] Each post is a
  short biography of the designer, a preview image, and a magazine plug. The Substack
  mirror of #38 is the same (checked). The catch-up post for 27-32 says only that he fell
  behind after a July holiday and "I'm making up for lost time". So almost every claim
  below about intent is [observed]. Nothing about these demos is [stated], apart from
  which designer he names.
- **Each demo page adds one quote from the source designer**, not from Andy: Bass on
  making beautiful things "even if nobody cares", Garland's First Things First brief,
  Aicher's "Good art inspires; Good design motivates", Bill's "Everything has beauty, but
  not everyone sees it", Scher's "raise the expectation of what design can be", and so on.
  These show which attitude he chose to pair with each design. They are [reported]
  quotes, not his own reasoning.
- **Subject matter is fixed; only the designer changes.** [observed] Every demo here is a
  fact sheet for a classic vehicle: Citroën DS (27, 29, 30), Trabant (28, 31), Vespa (33,
  34, 36, 38, 39), Ford Transit (35), Mini (37), Fiat 500. The same Vespa facts ("looks
  like a wasp", "pressed steel unibody", "manufactured by Piaggio") appear five times in
  five different art directions. This is the most useful lesson in the group: **the same
  content, art-directed five ways.** The copy stays the same; the concept changes.
- **Every demo sits on a 6-column 1fr grid at 64em**, with two exceptions: 38 uses
  5 columns, and 40 uses `7.5vw repeat(4,1fr) 7.5vw`. [observed in CSS] The grid itself is
  the default. The art direction lives in which columns he leaves empty, what he
  overlaps, and what he rotates.
- **The demo box has `min-block-size: 90vh`.** [observed] My first shots used tall
  windows (2400 px desktop, a 4800 px iframe), so they show stretched empty space. The
  `demoNNv` shots (1400x1000, 390x844) show the real first screen. Webfonts sometimes
  failed to load in the 390 iframe (Helvetica fallback), so the type looks off in some
  of those shots.

---

## 27: Saul Bass (Citroën DS)

1. **Source.** Bass's film posters and title sequences [stated in bio]: flat colour
   fields, cut-paper silhouettes, hand-lettered type. Andy took the flat
   two-colour split and the silhouette that holds the text [observed].
2. **Layout moves** [observed]
   - **Two-field split.** At 64em the design is `grid-template-columns: 1fr 1fr` with a
     white gutter that reads as a stripe: teal `#0f776d` on the left, orange `#f7b44f` on
     the right. There is no hero, no image box and no card. The page is two coloured
     planes, like a Bass poster.
   - **Silhouette as text container.** The black rear view of a DS carries the headline
     "NEW STANDARDS IN RIDE QUALITY" in white hand-cut capitals, inside the car body.
     Image and type are one object.
   - **Logo pinned to the corner.** The header is its own `1fr 1fr 1fr` grid. The
     Citroën chevrons sit in column 3 with `align-self: end`, so they land at the bottom
     right of the teal field, far from the heading. The mark is a sign-off, not a
     masthead.
   - **The spec list is the display type.** The right field holds a centred stack of the
     car's facts (front engine, front wheel drive, 1955 TO 1975, SEDAN, WAGON...) in big
     uneven hand-lettered capitals. The facts are set as the poster's typography, not as
     a bullet list.
   - The default would have been a car photo hero, a headline, and a specs table.
3. **Small screens** [observed]: the two fields stack, teal header above orange main.
   The chevrons move to the right, next to the car. The flat two-colour poster survives
   as two bands.
4. **Quotes.** None from Andy. The page pairs it with Bass on making beautiful things
   "even if nobody cares" [reported].
5. **Shots.** `demo27-1400/390` (tall, stretched), `demo27v-1400` (real first screen:
   the two fields at about 50/50).

## 28: Ken Garland (Trabant)

1. **Source.** Garland's modernist graphics; the bio cites First Things First [stated].
   He borrowed repetition and the Swiss info-graphic plainness [observed].
2. **Layout moves** [observed]
   - **Repeated, cropped mark as hero.** The desktop `header-lg.svg` shows the Trabant
     "S" badge at full size, then four copies, each cropped tighter and smaller, receding
     to the right like an echo or speed lines. Pale grey `#ededef` on charcoal `#262626`.
     One logo becomes a rhythm.
   - **Asymmetric caption.** A tiny caption, "Sparkplug with a roof", sits at the bottom
     left of a huge dark field. The contrast in scale (tiny line, giant mark) is the
     point.
   - **Stats on a measuring rule.** The main area is a 6-column grid. The `ul` spans
     columns 2-5 as 4 equal columns. Each stat (6.3gal, 40mpg, 7,450ddm, 3,096,999) sits
     under a 15 px black rule with a 15 px square tick at its start (`li:before`), so the
     row reads like a ruler or gauge. Column 1 is empty. The Trabant wordmark sits in
     column 6, top-aligned, off the rule's end.
   - The default would have been four stat cards with icons.
3. **Small screens** [observed]: a `<picture>` swaps in `header-sm.svg`, a single
   centred badge with no echoes. The stats drop to a 2-column grid with thick rules
   above each. The echo motif is deliberately dropped on phones; the rule-and-number
   motif is kept.
4. **Quotes.** None from Andy.
5. **Shots.** `demo28-1400/390`, `demo28v-1400` (repeating badges fill the first
   screen), `demo28v-390` (single badge and caption).

## 29: Saul Bass (Citroën DS)

1. **Source.** As for 27. The difference is a Bass title card: black ground, one
   centred title lockup, one emblem [observed].
2. **Layout moves** [observed]
   - **Narrow centred column on a 6-column grid.** `main` is `grid-column: 3 / 5`, the
     middle third. Columns 1-2 and 5-6 are left black except for the logo. The page is
     like a film title card: "CITROËN / DS¹⁹ (huge teal) / 1955-1975", in a quirky
     hand-cut face.
   - **Image escapes its column.** The white front view of the DS uses
     `margin-inline: -5vw` and `translateY(var(--spacing-l))`, so it is wider than the
     text column and drops toward the footer.
   - **Emblem low and far left.** The teal chevrons sit in column 1, row 1,
     `align-self: end`, at the bottom-left corner.
   - **Footer as a credit roll.** A full-width white strip holds the facts as one line
     of inline uppercase items with wide gaps (CITROËN DS · FRONT ENGINE · ...), like
     end credits.
3. **Small screens** [observed]: everything centres in one column. The chevrons move
   below the car. The credit roll wraps to 2-3 items per line. It still reads as a title
   card.
4. **Quotes.** None from Andy.
5. **Shots.** `demo29-1400/390`, `demo29v-1400/390`.

## 30: Otl Aicher (Citroën DS)

1. **Source.** Aicher's Munich 1972 pictograms and his corporate systems [stated in
   bio]. Andy took one silhouette used at several scales, and lowercase text [observed].
2. **Layout moves** [observed]
   - **One silhouette at three scales and crops.** There are three images of the same
     car: a small full front view in columns 2-3; a huge side crop in columns 4-6, rows
     2-4, bleeding off the right edge; and a small side crop in column 1, rows 3-4,
     bleeding off the left edge. The big crop is so large it reads as an abstract black
     shape with two white headlamp dots.
   - **Template rows give a fixed top band.** The grid is
     `grid-template-rows: 12rem auto auto auto` with
     `header, main, aside { display: contents }`, so every child is placed straight on
     the page grid. The title sits in columns 4-5, row 1. The logo sits in column 3 with
     a fixed 85 px width.
   - **All lowercase body.** `text-transform: lowercase` on paragraphs, an Ulm-school
     habit. A small caption sits in column 1 and a larger standfirst in columns 2-3,
     row 3.
   - **Overlap.** At 1400 the big crop sits over the end of the subtitle "futuristic
     design, innovative technology", cutting it off. This may be a bug or a deliberate
     image-over-text clash; I cannot tell.
   - The default would have been one product image with copy beside it.
3. **Small screens** [observed]: one column in source order: logo, title, subtitle, side
   crop, standfirst, front view, caption, small crop. The three scales survive as a
   sequence, and each crop still bleeds to the column edge.
4. **Quotes.** None from Andy.
5. **Shots.** `demo30-1400/390`, `demo30v-1400/390`.

## 31: Ken Garland (Trabant)

1. **Source.** Garland's repeat-pattern posters and Galt Toys work [my inference, not
   stated] [observed].
2. **Layout moves** [observed]
   - **Banded repeat with colour inversion.** Below a header there are three full-width
     bands. Each holds a row of identical Trabant side views. The bands alternate red
     band with orange car, orange band with red car, red band with orange car: a
     two-colour palette, `#f7b44f` and `#ab4337`, inverted on alternate rows, like
     wallpaper or a production line. Fittingly, the copy says "3,096,999 manufactured".
   - **Horizontal scroll strips.** Each band is `display: flex; overflow-y: scroll`
     with `cursor: move` and `title="Scroll"`, so the rows invite sideways dragging.
     Content reads as a conveyor belt.
   - **Header off-centre on the 6-column grid.** The logo is in column 2. The text
     block spans columns 3-6: the company name in large red bold, then
     "3,096,999 MANUFACTURED", then "'57-'90".
3. **Small screens** [observed]: the logo stacks above the text. The bands keep one car
   each, still alternating colour. The motif survives intact.
4. **Quotes.** None from Andy.
5. **Shots.** `demo31-1400/390`, `demo31v-1400/390`.

## 33: Tibor Kalman (Vespa)

1. **Source.** Kalman's Colors magazine: wit, a provocative headline, image and word
   playing off each other. The bio says he aimed at "creating unpredictable work"
   [stated in bio].
2. **Layout moves** [observed]
   - **Labels as insect legs.** A top-down Vespa sits in the centre column. Three facts
     on its left are rotated 30°, 15° and 0° and offset ±50 px. Three on its right are
     rotated -30°, -15° and 0°. They fan out like antennae or wings, so the scooter
     reads as a wasp. The text layout is the visual pun.
   - **Headline overprints the image.** "LIKE / A WASP" at 90 px is set with
     `line-height: .75`, so the two lines nearly touch, and with
     `mix-blend-mode: multiply`. It sits on columns 2-5, in front of the scooter's tail,
     with `z-index: 2` and `translateY(20px)`.
   - **Inner 5-column grid.** `main` spans columns 2-6 of the 6-column grid and is
     itself `repeat(5,1fr)`. The text sits in columns 1-2 and 4-5, the image in
     column 3.
   - **One-line statement masthead.** A full-width sentence with the key phrase in
     red: "...known for their *painted, pressed steel unibody*".
3. **Small screens** [observed]: everything centres. The rotations are removed (they
   live only inside the 64em query). The labels become two plain centred lists above a
   large scooter. The headline sits above the image, not overprinted. The pun is lost
   on phones; only the words remain.
4. **Quotes.** None from Andy. Kalman quote on the page: "having power (you are 50)
   and knowing nothing (you are 9)" [reported].
5. **Shots.** `demo33-1400/390`, `demo33v-1400` (the fan of labels and overprint in
   the first screen).

## 34: Max Bill (Vespa)

1. **Source.** Max Bill: Bauhaus-trained Swiss concrete art, ruled typographic
   structure [stated in bio]. Andy took heavy rules and a tabular build, set against
   one organic shape [observed].
2. **Layout moves** [observed]
   - **Organic blob over a ruled grid.** A sepia photo of a 1940s Vespa is masked in a
     cream, egg-like blob. It spans columns 1-4, rows 1-7, behind everything. Over it,
     a hard Swiss structure: 6-column grid, rows `200px repeat(6, auto)`, black rules
     3 px and 6 px thick, a 20 px black left bar on the table. The soft shape against
     the hard rules is the composition.
   - **Mixed type sizes in one ruled block.** The second fact is set at `2xl` between a
     3 px top rule and a 6 px bottom rule, spanning columns 2-6. "50cc-150cc" is set at
     `2xl`, right-aligned, columns 4-6, with a 20 px left bar. Two small facts sit side
     by side on one rule (columns 2-3 and 4-6). "Italian brand of scooter" is reversed
     out of a black bar.
   - **A data table used as a design element.** A history table with 3 px and 6 px
     borders and an empty row-spanning first column, so that column is just a black
     bar. A second, smaller blob photo sits partly behind the table (footer, column 5).
   - **Logo low left** (column 2, row 6) and the h1 "Looks like a wasp" top right.
   - **Frame.** A 10 px cream border around a red `#ab4337` ground.
3. **Small screens** [observed]: logo, blob photo, headline, the facts as a plain list,
   the table, second blob. The rules and the bold table survive. The overlap of type
   on photo is lost.
4. **Quotes.** None from Andy. Bill quote: "Everything has beauty, but not everyone
   sees it." [reported]
5. **Shots.** `demo34-1400/390`, `demo34v-1400/390`.

## 35: Paula Scher (Ford Transit)

1. **Source.** Scher's maximal, constructivist-influenced typography: type as
   architecture, condensed caps, mixed sizes that collide [stated in bio: "distinctive
   typographic style", Russian constructivism].
2. **Layout moves** [observed]
   - **Vertical giant word as a column.** "TRANSIT", in huge black condensed capitals
     rotated 90° (inside `header-lg.svg`), fills column 1 top to bottom, with "FORD" in
     a light cream face at its foot.
   - **Tilted images.** Three illustrated vans in column 2, rotated -10°, +10° and -10°
     (they swap on hover), stacked like a zig-zag.
   - **2-column modular fact grid.** A `section` spans columns 3-6 as `1fr 1fr`, with a
     40 px inset. The first and last articles span both columns, and each article has a
     10 px black top rule. Each article is its own Scher lockup: "MK1" huge with a cream
     "1"; "GEN ONE 1"; a rotated "MARK II" with body text; "MK4" with a rotated
     "4TH GENERATION"; and a full-width "8,000,000" that bleeds past the right edge.
     Size jumps are extreme: about 24 px captions next to about 160 px numerals.
   - **Skewed slogan.** "MORE VAN MORE VALUE", tilted about 8°, with VALUE in cream and
     overflowing the right edge.
   - **Footer logo bleeds.** A huge Ford oval crops off the right edge. A small text
     block sits in column 1.
   - Palette: coral `#f7604f`, charcoal, cream `#f7d299`. One condensed family (Fira
     Sans Extra Condensed).
   - The 1400 headless render shows overlapping glyphs inside some SVG lockups
     ("ENGINEIN", "DESIGNEIBY"). This looks like a font-loading artifact inside the SVG
     text, not intent [observed]; the 390 render is clean.
3. **Small screens** [observed]: `<picture>` swaps to `header-sm.svg`: "FORD" and
   "TRANSIT" set horizontally over one van. The three vans become a horizontal scroll
   strip (`figure` is flex with `overflow-x: auto`). The fact lockups stack one per row,
   keeping their own rotations and size contrast because they are SVG. Most of the art
   direction survives, because the type compositions are images.
4. **Quotes.** None from Andy.
5. **Shots.** `demo35-1400/390`, `demo35v-1400` (vertical TRANSIT, tilted vans,
   slogan).

## 36: David King (Vespa)

1. **Source.** King's agitprop posters: Constructivist photomontage, bold condensed
   capitals, exclamation [stated in bio: Soviet/Constructivist, political posters].
2. **Layout moves** [observed]
   - **Full-bleed texture photo as ground.** An aerial photo of a car park (endless rows
     of cars), toned dark brown and gold, fills the frame (`background-size: cover`).
     The crowd of cars is a pattern, a Constructivist mass image.
   - **Diagonal swarm.** Coral scooter silhouettes drawn as wasps (antennae, legs) fly
     up and right at about 30°, in four sizes. Each carries a label: "34 VERSIONS",
     "50CC-150CC", "LOOKS LIKE A WASP" on the largest, and the Vespa logo. The diagonal
     is King's and Rodchenko's dynamic axis.
   - **Header overlaps main.** `header { margin-block-end: -3rem; z-index: 2 }`, so the
     swarm sits over the text.
   - **Display type with doubled exclamation.** Bottom right: "The Vespa scooter !" and
     "MANUFACTURED BY PIAGGIO". The main text has `padding-inline-end: 4em`, and an
     absolutely placed "!!" at 125 px fills that space, the second "!" dropped `.5em`.
     The punctuation becomes a graphic.
   - **Thick frame.** A 30 px cream border.
   - Everything is pushed to the bottom: `align-items: end` on a 6-column grid where
     every child spans `1 / -1`. The grid exists only to bottom-align.
3. **Small screens** [observed]: `header-sm.svg` stacks the logo and three wasps
   diagonally at the top. The text stacks in large capitals. The "!!" shrinks to a tiny
   mark. The texture continues. The diagonal energy is kept, at a smaller scale.
   Intermediate step: at 48em the h1 grows from 58 px to 92 px and the p from 32 px to
   62 px, before the 64em layout (h1 125 px).
4. **Quotes.** None from Andy.
5. **Shots.** `demo36-1400/390`, `demo36v-1400` (the swarm over the car-park texture).

## 37: Paula Scher (Mini)

1. **Source.** Scher again: dense typographic lockups, mixed condensed faces, stencil
   bars, tilted compositions.
2. **Layout moves** [observed]
   - **Rotate the whole grid.** At 64em the `main` grid is
     `transform: rotate(20deg) scale(.85)`. Ten SVG type lockups ("AUSTIN MINI",
     "COOPER", "MARK VII", "20TH CENTURY", "MARK I / MARK II / CLUBMAN / MARK III",
     "1965", "TRANSVERSE ENGINE", "2000", "FRONT-WHEEL DRIVE LAYOUT", "LONGBRIDGE") tilt
     together as one poster.
   - **Named-area modular grid with holes.**
     `grid-template-areas: ". g1 g1 g1 g2 g2" "g3 g3 g4 g4 g5 g5" ". g6 g7 g8 g5 g5"
     "g9 g9 g7 g10 g10 ."`, 6 columns. The `.` cells leave deliberate gaps. g5 (the
     MARK list) spans 2x2. Alignment alternates: end on row 1, center on row 2, start
     below. This is the most explicit "compound grid with empty cells" in the group.
   - **Each lockup is a mini-poster.** Each one combines a spaced small cap line, a
     reversed yellow-on-black or red bar line, a big condensed word, and a thick
     underline rule; some are rotated 90° (1965, TRANSVERSE ENGINE, 2000).
   - **Asymmetric frame from gradients.** Red 40 px bars on the top and left, charcoal
     on the right and bottom (four `linear-gradient`s), a print-like offset frame on a
     cream `#fdf5e7` ground.
   - The 48em to 64em step is animated (`transition: all .5s`).
3. **Small screens** [observed]: below 48em it is a plain stack, no grid and no
   rotation. The lockups stack vertically, and the big initial blocks of the first three
   (M, I, N) line up down the left edge, spelling "MIN..." as an acrostic. That
   acrostic is invisible in the rotated desktop layout, where M, N and I scatter. The
   phone layout gets a reading the desktop does not have. The 48em query uses the area
   grid without rotation, which gives a tablet middle step.
4. **Quotes.** None from Andy.
5. **Shots.** `demo37-1400/390`, `demo37v-1400`, `demo37v-390` (acrostic visible).

## 38: Saul Bass (Vespa)

1. **Source.** Bass's torn and cut-paper mosaics (for example the Anatomy of a Murder
   and Vertigo-era poster textures) [my inference] [observed].
2. **Layout moves** [observed]
   - **Mosaic of tiles as hero.** The header is an 8x8 CSS grid of 64 empty `span`s.
     Each has a paper-texture photo (`bg.jpg`) with `background-blend-mode: luminosity`
     over one of five colours (red, mauve, mustard, olive, slate), chosen by
     `nth-child` formulas (2n+1, 3n+2, 5n+3, 7n+5) so the pattern looks random. Some
     tiles are rotated -5° (they rotate +5° on hover), like hand-pasted paper squares.
   - **Silhouette multiplied over the mosaic.** A dark top-down Vespa
     (`mix-blend-mode: multiply`, opacity .9) sits in header columns 4-5 of 8, rows 2-3.
     The tiles show through it.
   - **4:1 split on a 5-column grid.** The header spans columns 1-4, a narrow text
     column is column 5, `align-self: center`. One wide image field and one narrow
     column of text, not 50/50.
   - **Book-style text.** The narrow column has a hand-drawn display lede ("VESPA IS AN
     ITALIAN BRAND OF SCOOTER MANUFACTURED BY PIAGGIO.") in a Bass-like wobbly face,
     then small paragraphs with `text-indent: 2ch` on `p + p` instead of paragraph
     spacing. A "LOOKS LIKE A WASP" mark sits bottom left and the Vespa logo bottom
     right.
   - Ground: red `#ab4337`, cream text `#fcf8d4`.
3. **Small screens** [observed]: the mosaic shrinks to a small square at the top (still
   8x8 with the scooter) and the text follows it in full width. The art survives as a
   thumbnail, so it is not lost, but it loses its scale.
4. **Quotes.** None from Andy.
5. **Shots.** `demo38-1400/390`, `demo38v-1400/390`.

## 39: Milton Glaser (Vespa)

1. **Source.** Glaser's optical, psychedelic posters (Dylan) and stripe work [stated in
   bio: the Dylan poster].
2. **Layout moves** [observed]
   - **Pattern on pattern, all in CSS.** The outer ground is 45° diagonal stripes in
     10 px bands (`repeating-linear-gradient(-45deg ...)`): mostly black and white, with
     occasional blue, olive, yellow and red bands. Inside, the main area has horizontal
     10 px black and white stripes. Down the middle runs a vertical column of
     multicolour horizontal stripes (`main:before`). Three stripe directions are layered.
     It is an op-art poster.
   - **Letters placed in grid cells, split around a gutter.** "VESPA" is split into
     five spans on a 3-column grid, `auto 10vw auto` (15vw at 48em, 20vw on phones).
     V, S and A sit in column 1, rows 1-3, left-aligned; E and P sit in column 3,
     right-aligned. The word zig-zags across the coloured centre column, reading
     V-E / S-P / A, at 200 px in white extended capitals. The type is the layout.
   - **Object in the corner.** A red line-drawn Vespa sits in column 3, row 3, pushed
     right with `translateX`, at the bottom right.
   - **Heavy frame.** A 40 px charcoal border plus 80 px padding at 48em.
   - The narrowing middle column is animated (`transition: grid-template-columns 1s`).
3. **Small screens** [observed]: the same composition, scaled: letters at 100 px, a
   20 px padding frame, the centre column at 20vw, and the scooter spanning the full
   width at the bottom. This is one of the few demos where the phone shows the whole
   art direction, not a stacked fallback, because it is built from proportional
   columns and pattern, not placed images.
4. **Quotes.** None from Andy.
5. **Shots.** `demo39-1400/390` (tall: the stripes stretch), `demo39v-1400` (real
   first screen: V E / S P).

## 40: David King (Fiat 500)

1. **Source.** King's political posters: lists of slogans in condensed caps, red,
   yellow and black, a lightning-bolt motif [stated in bio: Anti-Nazi League,
   Rock Against Racism].
2. **Layout moves** [observed]
   - **Gutter columns in vw.** `grid-template-columns: 7.5vw repeat(4, 1fr) 7.5vw`.
     Narrow, fluid outer margins are written into the grid itself, not added as
     padding.
   - **Slogan column.** The aside (columns 2-3) is a black slab. Every Fiat fact
     ("FIAT 500", "TOPOLINO", "REAR-ENGINED" ... "181,036") is a centred line of yellow
     condensed capitals, each followed by a "⌾" bullet that alternates red and green
     (`li:nth-of-type(even):after`). It reads like a placard or a protest chant.
   - **Stacked block wordmark.** The main area (columns 4-5, `align-self: center`) has
     the "FIAT / 500" logotype in red, the blue Fiat badge overlapping the "T" and the
     "0", then a black bar caption, an all-caps paragraph with key words in red
     condensed bold, and a red bar footer.
   - **Lightning bolt.** A black bolt SVG in the top-right corner (`background-size:
     25%`, no-repeat), a King motif.
   - **Source order is not visual order.** `main` comes first in the HTML but is placed
     in columns 4-5; the `aside` comes second but sits left in columns 2-3. Phones read
     the story first, and desktops see the slogan slab first.
3. **Small screens** [observed]: the wordmark and story come first, then the black
   slogan slab, full width. The bolt stays at the top right. The palette and type carry
   the art direction.
4. **Quotes.** None from Andy.
5. **Shots.** `demo40-1400/390`, `demo40v-1400/390`.

---

## Cross-issue patterns seen in this group

All [observed] unless marked.

- **Same content, new concept.** Five Vespa pages (33, 34, 36, 38, 39) and three DS
  pages (27, 29, 30) differ completely while sharing copy. The design idea comes from
  the source designer's signature device, not from the content: Bass's flat fields and
  silhouettes, Garland's repetition, Aicher's scaled pictogram, Kalman's visual pun,
  Bill's rules, Scher's lockups, King's diagonal and slogans, Glaser's stripes.
- **An ordinary 6-column 1fr grid, used unevenly.** Nearly every demo uses
  `repeat(6, 1fr)`. The asymmetry comes from:
  - empty columns (1 and 6 in 28; 1-2 and 5-6 in 29; the `.` cells in 37);
  - 1-column-against-4 splits (38's 4:1; 40's 2:2 inside vw gutters);
  - `display: contents`, which places nested children straight on the page grid
    (30, 31, 33, 35).
  The non-default part is placement, not exotic track ratios.
- **Treat the content as one object, not a list of elements.** Text is put inside a
  silhouette (27), labels become insect legs (33), letters fill grid cells (39), facts
  become placards (40) or credits (29). There is not one card component in the group.
- **Rotation as energy.** Whole grid at 20° (37); ±10° images (35); 30° and 15° label
  fans (33); a diagonal swarm (36); -5° tiles (38). Rotation is almost always removed
  below 64em (33, 37), except when it is baked into SVG artwork (35, 36, 37 lockups).
- **Overlap and blend.** `mix-blend-mode: multiply` on a headline over an image (33)
  and on a silhouette over a mosaic (38); negative margins (29's image, 36's header);
  image over text (30).
- **Bleed off the edge.** Cropped marks and images run off the frame (28's echoes,
  30's crops, 35's VALUE, 8,000,000 and Ford oval). This deliberately breaks the
  "everything fits in its box" default.
- **Pattern made in CSS.** Stripes (39), gradient frames (37), an nth-child colour
  mosaic (38), repeated rows (31). Texture without photos, cheap to build.
- **Frames.** Thick, often asymmetric borders (34 cream 10 px, 36 cream 30 px,
  37 red top and left with black bottom and right, 39 charcoal 40 px) make each page
  read as a printed poster.
- **Small screens: three strategies, chosen per design.**
  1. Swap the art: `<picture>` with header-sm and header-lg (28, 35, 36). The concept
     is redrawn for the phone, not scaled.
  2. Keep it proportional: 39's vw columns and stripe patterns scale whole, and the
     phone gets the full art direction.
  3. Fall back to a stack: 33, 34, 38. Here the pun or overlap is lost and only the
     palette and type remain.
  Several demos have a 48em middle step (36's type sizes, 37's unrotated area grid,
  39's frame and letter sizes).
- **Contradictions and tensions.**
  - 33's whole idea (labels as wasp legs) disappears on phones, against the "keep the
    art direction small" aim. 37's phone layout gains an acrostic the desktop hides.
  - Heavy use of SVG text lockups (35, 37) keeps the art on phones but puts copy inside
    images. 35's desktop render even shows glyph collisions in headless Chrome. This is
    a fragility and an accessibility trade-off.
  - 30's overlap of image on subtitle looks unintended.
  - Source order and visual order diverge (40), which is fine for reading order on
    phones but would need care with keyboard focus.
- **How deep the reasoning goes.** These 2020 weekly pieces are sketches made at a pace
  of one a week, with no written rationale. Treat them as a catalogue of moves, not as
  his argued method; the Smashing IDD articles (other groups) carry the argument.
