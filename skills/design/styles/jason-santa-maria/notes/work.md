# Jason Santa Maria: work notes

Stream: `work`. Pages studied in a browser at 1440 px (desktop) and 390 px (phone),
2026-11-24. Numbers come from the rendered pages; computed CSS was read only to put a
number on something seen in a screenshot. P13 was studied from full-size screenshots
taken earlier and from its HTML and stylesheets fetched with `curl`.

Marks: **[O]** observed in the work, **[S]** stated by the designer, **[R]** reported by
someone else. Each claim's URL is the page it sits under (P1 to P13 below); claims in the
comparison sections cite those page numbers.

Screenshots (not committed) are in `/tmp/design-research/jason-santa-maria/shots/`, named
`NN-page-desktop-*` and `NN-page-phone-*` in page order. For P1 to P9, desktop shots at
1440 px are taken as a left tile (x 0 to 1054) and a right tile (x 386 to 1440) per row;
files ending in `a` or with no letter are left tiles, `b-right` are right tiles. For P10
to P12 each desktop file is one full 1440 px wide viewport (`.png`). Phone shots place two
consecutive 390 px viewports side by side in one image (left = first, right = next).
P13's screenshots are in `/tmp/design-research/jason-santa-maria/set-aside/megazoid-*`
(desktop rows 0 to 33 as left and right tiles 771 px high, rows 34 to 36 as single
1440 px captures; phone images 835 px high), and its fetched source is in
`/tmp/design-research/jason-santa-maria/megazoid-src/`.

## Sources

| #   | URL                                                            | Date                         | What it is                                                       |
|-----|----------------------------------------------------------------|------------------------------|------------------------------------------------------------------|
| P1  | https://jasonsantamaria.com/                                   | live; footer © 2026          | Current personal home page and about page in one                 |
| P2  | https://jasonsantamaria.com/blog/new-work-megazoid-microsite   | Oct 03, 2025                 | Current-site blog post with a full-width image                   |
| P3  | https://v5.jasonsantamaria.com/                                | v5 = 2011–2022 (P1)          | Previous personal site, home / article list                      |
| P4  | https://loudroom.com/                                          | live; footer © 2026          | Home page of his design practice, Loud Room                      |
| P5  | https://v5.jasonsantamaria.com/articles/ode-to-a-table/        | Sep 15, 2014                 | v5 article template, text only                                   |
| P6  | https://v4.jasonsantamaria.com/                                | 2008–2011; entry 2011-06-07  | v4 home, showing the latest entry in its own art-directed layout |
| P7  | https://v4.jasonsantamaria.com/articles/oh-snap/index.html     | Aug 08, 2008                 | v4 art-directed article with its own stylesheet                  |
| P8  | https://v4.jasonsantamaria.com/portfolio/typekit/index.html    | v4 era; shows Typekit c.2009 | v4 portfolio case page; screenshots of client work (Typekit)     |
| P9  | https://v3.jasonsantamaria.com/                                | 2004–2008; entry 2008-04-24  | v3 home / blog                                                   |
| P10 | https://v4.jasonsantamaria.com/articles/sugar-smack/index.html | Oct 22, 2010                 | v4 art-directed guest essay (Candygram series), dark ground      |
| P11 | https://v4.jasonsantamaria.com/articles/deadlines/index.html   | May 11, 2009                 | v4 art-directed quote post, no image                             |
| P12 | https://v4.jasonsantamaria.com/dailyphoto/                     | Dec 07, 2010                 | v4 daily photo page: one photograph, template layout             |
| P13 | https://djr.com/megazoid                                       | 2025 (P2 dated Oct 03, 2025) | Client work: specimen microsite for DJR's typeface Megazoid      |

Version dates for v3 to v5 come from the "Past versions" list on P1 [S].

## Pages

### P1 Current home (jasonsantamaria.com)

- Grid [O]: dark outer band, inner content box from x 100 to 1340 (1240 px). Four equal
  columns of 277.6 px with 43.2 px gutters (CSS grid). Column 1 holds only section labels
  and the headshot; every section body runs across columns 2 to 4 (919 px, x 421). The
  nav starts on column 2; a script "jsm" monogram sits at the right end of column 4. The
  headshot is a circle exactly one column wide (278 px). The book cover (300 px wide)
  sits in column 4 beside its text in columns 2 to 3. Sections are divided by full-width
  bars 18 px thick in a dark grey-teal, not hairlines. The grid stays the same in every
  section.
- Type [O]: Roslindale (serif) for intro and body; HEX Franklin for nav, section labels,
  headings and footer; VCTR Mono appears on posts (P2). Footer names all three [S].
  Sizes: intro 50.4/60 px, body 24/36 px, section labels 40/52 px bold condensed caps,
  version buttons 55.2 px, dates 19.2 px. Largest to body 55.2 / 24 = 2.3. Body line
  about 79 characters ("I currently work on a contract basis through my design
  practice, Loud Room, for"); intro about 45. Everything left-aligned, ragged right.
- Colour [O]: near-black ground rgb(23,25,29) covers almost the whole page. Body text
  light grey rgb(206,210,216); intro and labels white; dates grey rgb(131,142,158);
  links underlined with a grey-blue rule. No accent colour in the type; colour comes
  only from images (headshot, two font thumbnails in cream/black and pink/navy, red book
  cover).
- Imagery [O]: circular headshot; two 144 px square font thumbnails with a thin border;
  book cover with a border. All sit on column lines.
- Composition [O]: the 50 px intro is the largest element; the eye meets headshot and
  intro first. Column 1 is empty below each label for the whole length of each section.
  Text, images and rules all align to the four columns; nothing breaks the grid.
- Motion [O]: not checked (no hover or scroll testing done on this page).
- Phone [O]: box 342 px with 24 px margins; still a 4-column grid (73.5 px, 16 px gaps).
  Headshot shrinks to one column (74 px). Intro 28/34.4, body 16/24. Section labels stay
  40 px, so on phone they are larger than the intro. Labels stack above their text. Bars
  12 px. Hyphenation on ("every-one"). Footer items stack.

### P2 Blog post "New Work: Megazoid Microsite"

- Grid [O]: same four columns. Title, figure, body, subheads and prev/next all span
  columns 2 to 4 (919 px). Column 1 holds only the date, right-aligned against the
  gutter, set level with the top of the figure.
- Type [O]: title HEX Franklin bold condensed 84/84 px; subhead HEX Franklin 28.8 px
  weight 900; body Roslindale 24/36, about 76 characters a line; date, caption and
  "Prev/Next" labels in VCTR Mono 19.2 px grey rgb(106,118,135). Title to body 84 / 24 =
  3.5.
- Colour [O]: as P1. The only colour is the specimen image (yellow ground, cream
  letters, green extrusion).
- Imagery [O]: one specimen image the full width of columns 2 to 4 (919 × 705), square
  corners, no border; mono caption under it.
- Composition [O]: title, then image, dominate the first screen; column 1 stays empty
  apart from the date. "Next →" is right-aligned to the column-4 edge, "← Prev" left.
- Motion [O]: not checked.
- Phone [O]: title 56/56 on two lines; ratio to 16 px body stays 3.5. Date moves above
  the image. Caption 12.8 px mono. Prev and Next stack, labels in a narrow mono column.

### P3 v5 home (2011–2022)

- Grid [O]: fixed 916 px content (x 262 to 1178) centred at 1440. Each entry is a row: a
  58 px date column, then a title column from x 340 (838 px). "Feature" entries use the
  whole 838; short "link" entries split into a 370 px text column and a 448 px photo
  column at x 730. Entries are separated by 1 to 2 px dark full-width rules.
- Type [O]: CSS names Chaparral Pro (serif), proxima-nova and Facit (Typekit; footer
  credits a "Typekit colophon"). Feature titles Chaparral light 70/72 px in red; their
  deks Chaparral light 30/36 grey; link-post titles a sans 22 px semibold with a circled
  arrow; excerpts Chaparral 16/21. Nav, date months and footer headings in narrow
  uppercase letter-spaced caps. Title to dek 70 / 30 = 2.3; title to excerpt 70 / 16 =
  4.4.
- Colour [O]: white page; text dark grey rgb(68,68,68); one red rgb(223,71,71) for
  feature titles, active-nav marker and "More articles" button; footer band black,
  about a fifth of the page height.
- Imagery [O]: photos only on link posts, cropped to wide bands (448 × 143) flush to the
  right edge of the content.
- Composition [O]: the red 70 px titles are the largest things and set the rhythm; the
  date column is mostly empty. Footer: black band with modules in four columns.
- Phone [O]: one 350 px column, 20 px margins; logo above a row of small caps nav; date
  moves above the title on one line ("JUL 27"); feature titles drop to 30 px; excerpts
  18/24 with heavy hyphenation ("us-ing", "document-ed"); link-post photos are dropped;
  footer modules stack.

### P4 Loud Room home (loudroom.com)

- Grid [O]: 6 columns of 183.3 px, 20 px gutters, 1200 px max (x 120 to 1320). Logo over
  columns 1 to 2; nav stacked vertically in column 6. Title spans all six columns. Body
  paragraphs run columns 3 to 6 (793 px, x 527); columns 1 and 2 are empty below the
  title. Footer: a 1 px rule across the full width, links from column 3.
- Type [O]: HEX Franklin throughout plus VCTR Mono italic for nav and footer. Title
  "A funsized design consultancy" 147/147 px at weight 100 (hairline), letter-spacing
  -4.8 px, two lines. Body 40/48 px regular, about 42 characters a line ("I'm Jason Santa
  Maria, and Loud Room is my"). Nav mono italic 20 px. Title to body 147 / 40 = 3.7. In
  effect two sizes plus mono.
- Colour [O]: exactly two colours per view, ground and text. Seen: blue rgb(18,54,224)
  with teal rgb(50,224,201); mint rgb(143,223,209) with purple rgb(138,37,176); blue
  rgb(34,76,161) with mint rgb(121,226,200). The pair differed between page loads; the
  footer has a "Theme link" with a palette icon. What sets the pair was not established.
- Imagery [O]: none besides the logo: "LOUD ROOM" built from rows of short rounded
  horizontal dashes (288 × 159). Icons (Mastodon, LinkedIn, envelope) in the text colour.
- Composition [O]: the hairline title fills the width; then large text hangs from
  column 3, leaving a two-column empty band on the left for the rest of the page.
- Motion [O]: colour pair changes between loads; hover not checked.
- Phone [O]: header becomes two columns (logo 165 px, nav 2 × 2 mono italic); title 50 px
  hairline over three lines; body 20/24 full width (350 px), 20 px margins; no
  hyphenation seen. Ratio 50 / 20 = 2.5.

### P5 v5 article "Ode to a Table" (2014)

- Grid [O]: one text column 604 px (x 418 to 1022), offset 156 px in from the left of the
  916 px content area, so it is not centred in it. Below: a full-width light grey meta
  bar (date in narrow caps, tags, prev/next arrows), then the black footer from P3.
- Type [O]: title Chaparral 70 px light, dark grey (not red, unlike P3 titles). Body
  Chaparral Pro 20/30, about 69 characters a line. First paragraph flush; every later
  paragraph indented 24 px with no space between paragraphs; `hyphens: auto`. Italics
  for emphasis; one tight-set phrase "justthisclose". Closing note in a grey
  rgb(244,244,244) box in italic with a small monogram at the end. Title to body 3.5.
- Colour [O]: white page, grey text, red only for the note's link; black footer.
- Imagery [O]: none in the article.
- Phone [O]: title 30 px; body 18/27; indents kept, no paragraph space; heavy
  hyphenation ("apart-ment", "appli-ances").

### P6 v4 home (2008–2011)

- Grid [O]: fixed 910 px layout pinned to the left edge, not centred; at 1440 the right
  530 px is blank apart from the full-width nav band and footer band. Entry meta sits in
  a row of boxed cells divided by vertical rules (date 100 px, comments 100 px,
  "published in", prev). Body in two text columns of about 410 px; footer in three
  columns.
- Art direction [O]: the home shows the latest entry ("Responsive Web Design") in its own
  layout. The page loads `css/entry/responsive-web-design.css` on top of the site sheet.
  The nav band is yellow rgb(248,183,36), the yellow of the book cover in the photo. The
  title is image lettering in condensed caps, "RESPONSIVE" grey and "WEB DESIGN" yellow,
  about 90 px tall. A wide photo of a stack of the books spans 870 px. Deck Georgia
  20/30 in orange rgb(207,125,49); body Georgia 14/20, about 58 characters a line. The
  entry ends with "Design tags: Photo, Titling Gothic, White, Yellow": the entry is
  tagged by its typeface and colours.
- Footer [O]: black band, modules headed in narrow letter-spaced caps (Proxima Nova per
  CSS, rendered narrow), orange links.
- Phone [O]: no viewport meta tag; the 910 px layout does not adapt. In a 390 px frame
  it is cropped. How a phone browser renders it was not tested.

### P7 v4 article "Oh, Snap" (2008)

- Art direction [O]: own stylesheet `css/entry/oh-snap.css`, whose header comment says
  the code is copyrighted and may not be used for your site's design. The page ground is
  a light grey textured image. A photo of a Polaroid SX-70 on a red table is the
  background of the entry area, anchored bottom-left, filling the left ~560 px and fading
  into the page ground at its top and right; it also runs past the 910 px layout to the
  page edge. Text sits in a narrow column at the right (x 585 to 875, about 290 px,
  about 42 characters a line), Georgia 14/20. A red drop cap "S", about 100 px tall in a
  heavy rounded sans, overlaps the top-left of the text column and hangs out to its
  left. The entry title is not a headline: "OH, SNAP" in 11 px red letter-spaced caps
  above the meta row. Link colour #bb3a38, a red like the table in the photo. Design
  tags: "Photo, Red, Soho".
- Comments [O]: black section, three columns (author 210 px, comment 520 px, avatar);
  the author's own comments get a red top rule instead of grey.
- Comments on this page praise the layout [R]: Sara Flemming, "Love the layout of this
  entry"; Patrick Haney, "I love how you integrated the photo of the camera with the
  write-up"; Kurt Cruse, "This post really makes the new design shine" (Aug 2008).
- Phone [O]: no viewport meta; layout cropped at 390, text column falls outside the
  view.

### P8 v4 portfolio: Typekit

- Template [O]: title Georgia about 50 px; double rule; 642 px main column with a
  bordered screenshot of the work; a details row (Details / Role: Design, Identity /
  Type: Website / red "View project" button); 185 px sidebar with "Project types" list
  in red letter-spaced caps and two-up 85 × 70 project thumbnails. Black nav band with a
  red-orange rgb(204,51,0) active tab.
- The work, as shown in the screenshot [O]: Typekit's home headline set in one condensed
  family (caption in the image: "FF Dax Compact Web Pro") at three sizes and two weights,
  "The easiest way to use / REAL FONTS / ON YOUR WEBSITE", with "REAL FONTS" heaviest,
  largest and orange, the other lines light and brown; green buttons; a three-column
  feature row under a rule. A second screenshot shows a font page led by large type
  samples (Skolar) with small UI around them.
- Phone [O]: as P6, not adapted.

### P9 v3 home (2004–2008)

- Styling [O]: a pulp-paperback cover. Rust-red distressed header with "JASON SANTA
  MARIA" in condensed caps and a "COMPLETE AND UNABRIDGED / 40¢" price badge. A black
  book spine about 50 px wide runs down the left edge with the name vertical in yellow
  condensed caps, "ACTION SCIENCE ADVENTURE", "JSM03" and "Volume three in a series of
  inconsequential observations and humorous asides". Cream ground rgb(255,253,223) with
  a stain texture at top right.
- Grid [O]: fluid main column (980 px at 1440, narrower in smaller windows; page minimum
  743 px) and a sidebar of about 210 px modules headed by white caps on black boxes.
- Type [O]: Georgia throughout. Titles 23.4 px rust rgb(153,51,0); dates small
  letter-spaced caps in olive rgb(136,136,68) above titles; body 13/19.5 black, about
  150 characters a line at 1440. Every post opens with a black drop cap about three
  lines tall, often beside a bordered thumbnail (146 × 84) floated left. Dashed olive
  rules between parts of a post; solid dark rule between posts.
- Phone [O]: no viewport meta; fixed parts (spine, header) stay; main column narrows,
  the rest is cropped.

### P10 v4 article "Sugar/Smack" (2010)

- Context [S]: a guest essay by Kristina Halvorson in the "Candygram" series; the page
  says Candygrams are odes to candy by guest authors during October. The layout is on his
  site with its own stylesheet (`css/entry/sugar-smack.css`).
- Art direction [O]: the entry turns the v4 page dark: ground #1a1a1a, text #ccc, links
  light blue #8dbece. The title is image lettering in heavy italic condensed caps, light
  blue, "SUGAR" upper left and "SMACK" stepped down and right, about 130 px tall. A photo
  of a red Life Saver hangs on a white string from the nav bar, sits between and over the
  two words, and overlaps the double rule and the meta row below them. At the end of the
  essay a photo of the same string, stained red, runs across the full 910 px and ends in
  a loop at the right. Design tags: "Blue, Grey, Photo, Proxima Nova, Red".
- Grid and type [O]: byline centred, "by KRISTINA HALVORSON" in small red letter-spaced
  caps over a short rule. Two text columns of about 400 px (x 40 to 440 and x 470 to 870),
  Georgia 14/20, about 60 characters a line. The left column opens with a pull quote in
  Proxima Nova 24/30 semibold italic, light blue, with the opening quotation mark hung
  outside the text edge. Title to body: lettering about 130 px against 14 px. Footer of
  the essay: a red "CANDYGRAM" badge with the series line, and the author's photo and bio.
- Comments [O]: light text on the dark ground; his own comments keep a red top rule
  while links are blue. Asked about it, he wrote that he does not always match it to the
  link colour, "Because sometimes a different color I'm using works better" [S] (comment,
  Oct 24 2010). Commenters praised the red-stained string, the palette and light-on-dark
  comments (Dave Rau) and the "witty design" (Erin Kissane) [R].
- Phone [O]: no viewport meta; the fixed layout is cropped at 390 px.

### P11 v4 article "Deadlines" (2009)

- Kind [O]: a post that is only a quotation (Douglas Adams), filed under "Quotes", with
  its own stylesheet (`css/entry/deadlines.css`).
- Art direction [O]: ground light grey #f5f5f5, text #333, links red-orange #c30. The
  quote is set in American Typewriter 51/60 px in red-orange, in a 630 px block starting
  at x 140 (120 px in from the content edge). Large Georgia 80 px quotation marks in grey
  hang outside it: the opening mark in the space to the left of the text, the closing
  mark after the last word. Attribution in Lucida Grande 18 px grey, with the life dates
  in italic. No image. Design tags: "American Typewriter, Black, Grey, Red".
- Ratio [O]: 51 px quote against 14 px comment text, about 3.6.
- Display type method [S]: replying to a commenter on this page he says he has "sIFR
  working well enough" and would like to move to Cufón when he has time (May 11 2009).
  A commenter called it a "Lovely and adequate use of American Typewriter" [R].
- Phone [O]: no viewport meta; the quote runs off the right edge at 390 px.

### P12 v4 Daily Photo ("Gold Medal", 2010)

- Kind [O]: the v4 photo section, one photograph per entry in the standard v4 template,
  no entry stylesheet. White ground, black nav band with the active tab in red-orange,
  title "Gold Medal" in Georgia about 50 px, the boxed meta row, then the photo.
- Imagery [O]: one photo 850 × 566 at x 30, inside the 910 px layout: the red neon "GOLD
  MEDAL FLOUR" sign at night against deep blue, filling the left two thirds, with the
  mirror-reversed back of the sign dark at the right. The same photo, cropped to a thin
  band showing "MEDA", is the "Daily photography" module in the black footer of every v4
  page seen (P6, P7, P8, P10, P11).
- Phone [O]: no viewport meta; the photo is cropped at 390 px.

### P13 Megazoid microsite (djr.com/megazoid, client work, 2025)

- Authorship and scope: P2 says he made the microsite with David Jonathan Ross for the
  typeface Megazoid, gathering retro packaging (VHS and cassette tapes, Polaroid, Trapper
  Keepers) and analog devices (calculators, keyboards, game controllers) as references,
  with colour that goes "right up to the line of 'clashing'", a paper texture, sci-fi
  sample text and Atari catalogue descriptions, and "lots of little moments of motion and
  play" where letters react to hover or touch [S]. The page's credits say "This webpage
  was designed by Loud Room" [O]. In the HTML that credit closes a `div id="megazoid"`
  styled by its own `megazoid-microsite.css`. The site header (DJR wordmark, nav), the
  licence cards, the buy panel and the three-column footer sit outside that block and
  are styled by DJR's site stylesheet, so they are the host site's, not his [O]. The
  "Are You Ready?" heading above the licences is styled in the microsite sheet [O].
- Structure [O]: a stack of full-bleed sections, each its own colour field, with 12rem
  top and 8rem bottom padding on desktop. In order: hero; a statement in 115 px display
  type on indigo; a stack of specimen words on pink; outlined specimen words with
  extrusions on yellow; a text section; a styles section on navy; a field of coloured
  letter shapes with a calculator; an italic paragraph on purple; a "ROADWAY" image on
  yellow; lowercase words on blue; a stylistic-set grid; a block of caps over echoes on
  purple; an outlined "MEGAZOID" stack; "SUPER BREAKOUT" on navy; a glyph grid; credits.
  There is no column grid running through the page. Content is centred, with display
  words up to `clamp(3rem, 14vw, 18rem)` (about 200 px at 1440 px), several of which run
  past both window edges and are cut off (`overflow-x: hidden`).
- Text section grid [O]: two columns at `1fr 1.25fr` with a 3rem gap inside a container
  of at most 1200 px; the image (a Radio Shack logo, a 1970 Photo-Lettering booklet) in
  the narrower left column with a mono caption, the text in the wider right one, about
  640 px, about 60 characters a line.
- Type [O]: no serif anywhere in the microsite. Display in Megazoid and its layered
  styles (Left/Right, Shade, Fill); running text in Input Mono at
  `clamp(0.875rem, 2.5vw, 1.125rem)` (18 px at 1440 px), condensed (`wdth 80`), light
  (`wght 300`), line-height 1.7, paragraphs separated by 1.5em of space, no indents, no
  hyphenation rule. The text opens with a layered drop cap 5.7em high, built from two
  stacked Megazoid styles in teal and aqua, with the rest of the first word in caps.
  Letters named in the text are set as keycaps: white boxes with a 1 px grey border and
  rounded corners. Specimen labels ("Regular, for general typesetting") in mono. Largest
  display to text: about 200 / 18 = 11.
- Colour [O]: fourteen named colours in the stylesheet (purple, pink, orange, yellow,
  green, blue, light blue, navy, indigo, cream, red, teal, aqua, tan). The hero is
  six diagonal stripes drawn as a hard-stop gradient at 46° (pink, orange, yellow, green,
  blue, purple); horizontal stripe bands of the same colours divide sections; a
  perspective grid image in pink lines on navy fades through a gradient into pink. Type
  is coloured on coloured fields. A paper texture image is laid over the whole page with
  `mix-blend-mode: multiply`.
- Imagery and objects [O]: a calculator drawn in CSS with bevels (gradients, inset and
  drop shadows, a 2 px press offset) showing "1985", overlapping the field of letter
  shapes; the two reference images; the "ROADWAY" echo image.
- Repetition [O]: specimen words repeated as stacked echoes: "SUPER" and "BREAKOUT"
  each repeated four more times at stepped sizes and offsets; "MEGAZOID" stacked in
  outline above one filled line; "ROADWAY" echoes; caps lines over shadow layers.
- Interaction [O, from CSS and script]: depth and stroke sliders and a "Link layer
  depth" checkbox on the shade styles; glyph cells that on hover show the glyph at 80vh
  in pink, multiplied over the page; stylistic-set blocks that switch on hover or tap;
  letters that appear on scroll; a working calculator; hero buttons. Pill-shaped buttons
  (TRY, BUY, TYPESET, PDF; `border-radius: 2rem`) sit at the bottom edge of the hero,
  which is at least 90vh high. Motion itself was not watched; it is read from the code.
- Rules [O]: none between sections. Rules only inside the glyph grid (1.5 px pink cell
  borders) and the stylistic-set grid (1 px grey gaps).
- Phone [O]: one column; the text section stacks text then image; section padding drops
  to 2rem; display words drop to `clamp(4rem, 18vw, 16rem)` (about 70 px at 390 px)
  over 14 px text, so the display stays large; the hero splits "Mega / zoid" over two
  lines; no hyphenation seen in the running text.

## Comparison

### Moves

A move recurs across the pages and is not what a typical designer or AI model does by
default.

1. **Content starts one column in; the first column is kept for labels or left empty.**
   P1 and P2: four equal columns, body always in columns 2 to 4, column 1 holds only a
   section label, the headshot or the date. P4: body in columns 3 to 6 of six, columns
   1 to 2 empty under the title. P3: a 58 px date column before every title. P5: text
   column set 156 px in from the left of its area. P7: left ~560 px given to the photo,
   text at the right. P11: the quote starts 120 px in, with the opening mark hung in that
   space. Not on P6, P8, P9, P10, P12 (content from the left edge of the layout) or
   P13 (centred specimens and a 1fr : 1.25fr image-and-text split, no label column).
   Default: one centred column, or content across the full container.
2. **A serif text face for reading, a condensed or narrow sans in caps for labels.**
   Serif body: P1, P2 (Roslindale), P3, P5 (Chaparral Pro), P6, P7, P8, P9, P10, P11,
   P12 (Georgia). Condensed or narrow caps for labels, nav, dates or titles:
   P1 (section labels 40 px HEX Franklin bold condensed caps), P2 (84 px condensed
   title), P3 and P5 (nav, dates, footer heads), P6 (title lettering and footer heads),
   P8 (nav, sidebar; and the Typekit work itself), P9 (header and spine), P10 (italic
   condensed title lettering), P11 and P12 (nav and footer heads). Not on P4 (sans body,
   hairline title, mono nav) or P13 (no serif; Input Mono text, Megazoid display; the
   caps nav on that page is the host site's). Default: one sans family (Inter or similar)
   for everything.
3. **Large body text.** Body 24 px on P1, P2; 20 px on P5; 40 px on P4. Line lengths of
   about 42 (P4), 69 (P5) and 76 to 79 (P1, P2) characters. Not on P6, P7, P8, P10, P11,
   P12 (14 px Georgia) or P9 (13 px), all from before 2011, nor on P13 (18 px mono at
   1440 px, 14 px on phone). Default: 16 to 18 px body.
4. **Book and print conventions in the text.** Drop caps: P9 (every post), P7 (100 px
   red drop cap hanging outside the column), P13 (a 5.7em drop cap of two layered
   Megazoid styles, first word in caps). Quotation marks hung outside the text edge:
   P10 (pull quote), P11 (80 px marks around the quote). A magazine-style byline centred
   over a short rule and a pull quote: P10. Indented paragraphs with no space between:
   P5. Hyphenation on: P1 and P2 at phone width, P3, P5. Book-object metaphors: P9
   (spine, price badge, "volume three"), P1 (site versions listed as v1 to v5). Not on
   P4, P8 or P12. P13 has the drop cap but not the rest: block paragraphs with 1.5em
   between, no indents, no hyphenation. Default: block paragraphs with space between,
   no hyphenation, no drop caps, quotation marks inside the text block.
5. **Dates and meta set apart in a different face, in a margin or a ruled cell.** P2:
   VCTR Mono, right-aligned in column 1 level with the figure. P3: month in small caps
   over the day, in its own column. P5: narrow caps in a full-width meta bar. P6, P7,
   P10, P11, P12: boxed cells with small letter-spaced labels ("2008 / Aug 08",
   "COMMENTS 28"). P9: olive letter-spaced caps above the title. Not on P1 (no dates),
   P4 or P13 (no dates). Default: a grey date line under the title in the body family.
6. **Rules as structure.** P1, P2: full-width bars 18 px thick (12 px on phone) between
   sections instead of space or cards. P3: full-width dark rules between entries. P5,
   P6, P7, P8, P10, P11, P12: double rules under titles and vertical rules between meta
   cells. P9: dashed rules inside posts, solid between posts. P4: only a 1 px footer
   rule. P13: no rules between sections, which are divided by full-bleed colour fields
   and stripe bands; rules only as cell borders in the glyph and stylistic-set grids.
   Default: whitespace or card containers.
7. **Colour held to a ground, a text colour and at most one or two accents; the rest of
   the colour comes from images.** P1, P2: near-black ground, grey and white text, no
   accent; colour only in images. P4: exactly two colours per view. P3, P5: white, grey,
   one red, black footer. P6, P7: one accent per entry taken from the entry's photo
   (yellow from the book cover, red from the table). P10: dark grey ground, light grey
   text, light blue for title and links, red only in the candy, string and byline. P11:
   light grey, dark grey and one red-orange; no image. P12: white, black and one
   red-orange; colour otherwise only in the photo. P9: cream, rust, olive, black. The v4
   "Design tags" name the colours per entry (P6 "White, Yellow"; P7 "Red"; P10 "Blue,
   Grey, Red"; P11 "Black, Grey, Red") [S]. Not on P13: fourteen colours as fields,
   diagonal stripes, bands, coloured type and gradients; P2 says its colours go "right up
   to the line of 'clashing'" [S]. Default: a brand colour plus several accents, tints
   and gradients.
8. **Per-article art direction.** P6, P7, P10 and P11 each load their own stylesheet,
   change the page ground (white, textured light grey, #1a1a1a, #f5f5f5), link colour
   and title treatment to suit the entry, and tag the entry with its typeface and
   colours ("Design tags"). The display face changes per entry: Titling Gothic (P6),
   Proxima Nova (P10), American Typewriter (P11), named in their tags [S]. P6, P7, P10
   build the entry around one photo of the subject; P11 has no image and is carried by
   the typeface alone. Not on P1, P2, P3, P5, P9 (one template per site) or P12 (the v4
   photo template). P13 is a single client page, not a series, but is built the same
   way from its subject: P2 lists the retro packaging and devices it was drawn from [S].
   P1's text calls these "early experiments in online art direction" [S]. Default: one
   template for every post.
9. **Display type far larger than the text, and kept large on phones.** P1: section
   labels 40 px against a 24 px body; on phone they stay 40 px while the intro drops to
   28. P2: 84 px title, ratio 3.5 kept on phone. P4: 147 px title, 40 px body. P10:
   title lettering about 130 px over 14 px text. P11: 51 px quote over 14 px text (about
   3.6). P13: specimen words about 200 px over 18 px text (about 11), and about 70 px
   over 14 px on phone. Not on P7 (11 px title) or P9 (23 px titles over 13 px text); P10
   and P11 have no phone layout. Default: a modest heading scale that shrinks evenly on
   phones.
10. **A picture or letter that crosses the page's own structure.** P7: the drop cap
    hangs out of its column and the photo fades behind the text and past the layout's
    edge. P10: the Life Saver photo hangs from the nav bar over the title and through the
    rule and meta row, and its string returns across the full width at the end of the
    essay. P13: display words run past both window edges and are cut off, and the
    calculator sits over the field of letter shapes. Not on the other ten pages, where
    images stay inside their boxes and columns. Default: images contained in their own
    frame.

### What changes from one project to the next

- **Typefaces follow the period's means [O].** Georgia and Lucida Grande on P6 to P12
  (2004 to 2011), with display faces as lettering images or by sIFR (P11 [S]); Typekit
  faces (Chaparral, Proxima Nova, Facit) on P3, P5 (2011 to 2022, "Typekit colophon" in
  the footer); Roslindale, HEX Franklin and VCTR Mono on P1, P2 and HEX Franklin and
  VCTR Mono on P4 (now). Monospace grows from meta and nav (VCTR Mono on P1, P2, P4) to
  all the running text on P13 (Input Mono), where the display face is the client's
  typeface itself.
- **Ground and palette change per site, and on v4 per entry [O].** Cream pulp paper
  (P9), white with red (P3, P5), near-black (P1, P2), a two-colour pair that changes
  between loads (P4). On v4 the ground changes per entry: white (P6, P12), textured light
  grey (P7), #1a1a1a (P10), #f5f5f5 (P11).
- **The personal sites carry a themed metaphor; the practice site does not [O].** P9 is
  a paperback cover; P1 lists its versions like editions. P4 (Loud Room) has no
  metaphor: sans text, hairline title, mono nav, two flat colours.
- **Accent colour and imagery follow the subject of the entry, where there is art
  direction [O].** P6 yellow with the yellow book; P7 red with the red table and a photo
  of the camera written about; P10 a photo of a candy on a string for an essay about
  candy, red with the candy. P11 sets a writer's quote in a typewriter face; the reason
  is not stated. His own words on one colour choice: a different colour "works better"
  sometimes (P10 [S]).
- **Phone handling follows the period [O].** P6 to P12 (v3, v4) have no viewport tag
  and do not adapt. P3 and P5 adapt (one column, smaller titles, photos dropped on link
  posts). P1, P2, P4 keep their grid on phones and keep labels large; P13 goes to one
  column and keeps its display type large.
- **The one client page, P13, against his own sites [O].** It keeps: a drop cap (P7,
  P9); display type an order of magnitude larger than the text, kept large on phone (P1,
  P2, P4); a page built from its subject's references (P6, P7, P10, P11; named for P13
  in P2 [S]); a paper texture laid over the page (P7's textured ground, P9's stained
  paper); a picture or letter breaking the page's frame (P7, P10); mono type (P1, P2,
  P4). It drops: serif text, the label column and one-column-in layout, rules and boxed
  meta as structure, the restraint to one or two accents, large body text, hyphenation
  and indents. It adds what none of his own pages show: many colours with gradients
  and stripes, a rendered object (the calculator), interactive specimen controls,
  keycap boxes for letters named in the text, specimen words stacked as echoes, and
  pill-shaped buttons. Which of these come from the brief and which from him is not
  separable from these sources; P2 says the brief for such sites is to show what the
  font can do and "have fun with it" [S].

### Default-level features left out

Left-aligned ragged-right text, a top nav, a logo top-left and footer link lists appear
on most pages and are also the default, so they are not recorded as moves.

## Looked for and not found

- **Other live client sites.** P13 is the one live client page studied; the rest are
  his own sites, his practice, and screenshots of client work inside the v4 portfolio
  (P8). Clients named on P1 and P4 (AIGA, Chicago Tribune, PBS, WordPress and others)
  were not checked as live pages.
- **Loud Room shop (shop.loudroom.com).** Its product pages refuse to load in a frame,
  so they could not be shot at 1440 px in this browser; not studied.
- **Motion and hover.** Not tested in a browser on any page. P4's colour pair changes
  between page loads; P13's hover, slider, scroll and calculator behaviour is read from
  its CSS and script, not watched.
- **What sets P4's colour pair**, and what the footer "Theme link" does: not
  established.
- **A grid on P6 to P12** beyond fixed column widths: no column system beyond the
  sidebar and content split, and the two text columns on P6 and P10, was found.
- **v4 entries without art direction.** Of the v4 archive, P12 (daily photo) uses the
  plain template; plain v4 articles were not studied.

## Set aside (step 8; not studied)

- https://v4.jasonsantamaria.com/articles/the-death-throes-of-print/index.html (a v4
  article picked from the archive list):
  `/tmp/design-research/jason-santa-maria/set-aside/v4-death-throes-of-print-*`
