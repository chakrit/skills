# Jason Santa Maria: synthesis

Written from the three notes files alone: `notes/work.md` (pages P1 to P13),
`notes/words.md` (his writing, cited by section) and `notes/accounts.md` (sources S1 to
S15). Citations name the file and the page, section or source inside it. "Stated" means
he said it; "reported" means another person said it; "observed" means a studied page
shows it.

The pages studied are his own sites, his practice's site and one client page: the
current jasonsantamaria.com (P1, P2, live 2026), v5 (P3, P5, 2011 to 2022), v4 (P6 to
P8, P10 to P12, 2008 to 2011), v3 (P9, 2004 to 2008), Loud Room (P4, live 2026) and the
Megazoid microsite for David Jonathan Ross's typeface (P13, 2025), the one live client
page studied. On P13 only the block credited "designed by Loud Room" is his; the header,
licence cards, buy panel and footer belong to DJR's site (work P13). P13's motion and
hover were read from its CSS and script, not watched.

## Order of work

What he says he does, in the order the sources give it.

1. **Learn the client's message and its customers' expectations.** Discovery comes
   first: what message the client wants to convey and what its customers expect.
   Research is "the most important part of the design phase"; for Comhaltas, an Irish
   music organisation, the team sat in Irish pubs, then studied traditional motifs and
   colours and threw out the leprechaun and shamrock clichés (words: Process; accounts
   S5, 2007, stated via Joe Clark's liveblog).
2. **Gather references.** He works among books, objects and physical "morgue files" of
   old ads, photos, matchbooks and textures (words: Process; accounts S5, 2007). For the
   Megazoid microsite he and the type designer first gathered references both liked:
   retro packaging, VHS and cassette, Polaroid, Trapper Keepers, calculators, game
   controllers (words: Process, 2025). For A List Apart he looked at "things that had a
   lot of content", McSweeney's and H.G. Wells books (accounts S5).
3. **Make many ugly ideas, and push to extremes.** "I want a big sprawling mass of ugly
   ideas because it helps get past the most obvious ones" (words: Process, 2014).
   Drawing a typeface he pushed shapes "toward an extreme" to find "too much", then
   pulled back (words: Process, 2025). For the WordPress logo, about 30 variations
   (words: Process; accounts S5).
4. **Choose type from mood words, text face first.** He writes words for the mood and
   finds faces that carry them; for his studio Mighty the words were "stable, powerful,
   industrial, boxy, angular, geometric, machined, blue collar" and the result a bold
   condensed Proxima Nova set large in caps (words: Process, book ch. 4, 2014). "I like
   to start by picking a text face for body copy, as this is what a reader will spend
   the most time looking at" (words: Process, 2009). He tests candidates in dummy HTML
   pages across browsers and devices and leaves with two or three faces (words:
   Process, 2014).
5. **Audit the elements, then set a hierarchy.** List the site's elements by semantics
   (h1, h2) and by job (captions, block quotes), then keep the rules consistent (words:
   Process, book ch. 5).
6. **Grey box before colour.** Between the sketch and the full comp comes a comp "with
   no colour and focussing on hierarchy and layout"; going straight from sketch to
   Photoshop leaves him "too caught up in the details" (words: Process; accounts S5,
   2007).
7. **Three directions, then rounds.** Three broad comps, each on its own idea; the
   client picks one and is asked not to "Frankenstein" them; later rounds refine, the
   second round on typography. "It's much easier to revise than create" (words:
   Process; accounts S5, S13).
8. **Settle details in the browser.** On A List Apart 4.0, hover styles were worked out
   "playing with live XHTML and CSS", and the issue stamp "came about during CSS
   programming" (accounts S2, 2005). Type is "judged optically first, not by the
   numbers"; a scale is "my starting point ... but I rarely adhere to it" (words:
   Reasons, 2012, 2014).

Two further accounts of order, from particular projects:

- **A system first, then each piece inside it (v4, 2008).** He built "a basic eight
  column grid, a few typefaces", a fixed masthead and utility information, and left
  typefaces, colours, images, backgrounds, columns and layout open per post, "much the
  same way one would approach the design of a magazine" (words: Process). "What you're
  looking at isn't the design so much as the plan for design" (accounts S10).
- **Start with one piece, in public (Slate, 2016 to 2018).** One weekly Cover Story as a
  deliberately incomplete sandbox, tested with readers, then grown into the brand
  (words: Process).

He also says some projects follow an ordered path set by fixed constraints and others
are "like working with clay" (words: Process, book ch. 6).

## Moves

One entry per move in `notes/work.md` (Comparison: Moves). Pages that show each move are
listed by number.

### 1. Content starts one column in; the first column holds labels or nothing

- **Looks like:** the text block does not start at the left edge of the layout. A
  narrow left band runs the length of each section, empty except for a section name, a
  date or a portrait.
- **Built:** P1 and P2: a 1240 px box, four equal columns of 277.6 px with 43.2 px
  gutters; every section body spans columns 2 to 4 (919 px); column 1 holds only the
  section label (40/52 px bold condensed caps), the circular headshot (exactly one
  column, 278 px) or the post date (mono, right-aligned against the gutter, level with
  the top of the figure). P4: six columns of 183.3 px with 20 px gutters, 1200 px max;
  title across all six, body in columns 3 to 6, columns 1 and 2 empty for the rest of
  the page. P3: a 58 px date column before every title. P5: a 604 px text column set
  156 px in from the left of its 916 px area, so not centred. P11: the quote starts
  120 px in, the opening quotation mark hung in that space. P7: the left ~560 px given
  to a photo, text in a 290 px column at the right.
- **Default it replaces:** one centred column, or content across the full container.
- **Reason:** not stated for the empty or label column. His book says that on his own
  site a column grid inside horizontal bands "spaces elements and separates content
  types" (words: Reasons, ch. 6); that covers the grid, not why the first column is
  left empty.
- **Used / not used:** used on P1, P2, P3, P4, P5, P7, P11. Not on P6, P8, P9, P10, P12,
  where content starts at the layout's left edge, or on P13, where specimens are centred
  and the one text section splits `1fr 1.25fr`, image left and text right, with no label
  column.
- **Phone:** P1 keeps a 4-column grid (73.5 px columns, 16 px gaps, 24 px margins) and
  stacks each label above its text; the headshot stays one column wide (74 px). P2 moves
  the date above the image. P3 moves the date above the title on one line. P4 runs the
  body full width (350 px).
- **Pages:** P1, P2, P3, P4, P5, P7, P11.

### 2. A serif for reading; a condensed or narrow sans in caps for labels and titles

- **Looks like:** running text in a serif; nav, dates, section labels, footer heads and
  often the title in a condensed or narrow sans, in capitals.
- **Built:** current: Roslindale for intro and body, HEX Franklin bold condensed for
  labels, headings, nav and footer, VCTR Mono for dates, captions and prev/next (P1,
  P2). v5: Chaparral Pro for titles and text, narrow letter-spaced caps for nav, months
  and footer heads (P3, P5). v4 and v3: Georgia for text; condensed caps in title
  lettering, header and spine (P6, P9, P10), and narrow letter-spaced caps for footer
  heads (P6, P11, P12).
- **Default it replaces:** one sans family, Inter or similar, for everything.
- **Reason:** stated for the sans side: sans serifs "pack tighter", so more characters
  and a larger size fit a line, and in UI every bit of space counts (words: Reasons, ch.
  5). Slightly condensed headline faces absorb varying headline lengths without awkward
  breaks (words: Reasons, ch. 5, about news sites). Pair by distinction and harmony, not
  two serifs or two sans, because faces too alike weaken hierarchy (words: Reasons, ch.
  4; 2009). A separate caption face "can signal a different speaker" (words: Reasons).
  For the serif text face itself: he wants "a touch of personality (and I mean ever so
  little)" (words: Reasons). Why a serif rather than a sans for text is not stated.
- **Used / not used:** P1 to P3, P5 to P12. Not on P4, where everything is HEX Franklin
  with a hairline title and mono italic nav, or on P13, which has no serif: running
  text in Input Mono, display in the client's typeface Megazoid (the caps nav on that
  page is DJR's site, not his).
- **Phone:** the faces stay; sizes change (move 9).
- **Pages:** P1, P2, P3, P5, P6, P7, P8, P9, P10, P11, P12.

### 3. Large body text

- **Looks like:** text that reads as larger than a typical web page's.
- **Built:** body 24/36 px on P1 and P2 (about 76 to 79 characters a line), 20/30 px
  on P5 (about 69), 40/48 px on P4 (about 42). The P1 intro is 50.4/60 px.
- **Default it replaces:** 16 to 18 px body.
- **Reason:** stated in general terms for base size: reading distance from a desktop is
  greater than from print, so the base is larger; "When in doubt, make it bigger"
  (words: Reasons, ch. 5). For the AIGA article page: "Nice big reading column, nice
  big text", so the page "can feel full all the way down to the bottom" rather than
  "adrift in a sea of nothingness" (accounts S5; words: Reasons).
- **Used / not used:** P1, P2, P4, P5, all from 2011 on. Not on P6 to P12 (14 px
  Georgia) or P9 (13 px), all before 2011, nor on P13 (Input Mono 18 px at 1440 px,
  light, condensed, line-height 1.7, about 60 characters a line; 14 px on phone).
- **Phone:** P1 and P2 body 16/24, intro 28/34.4; P4 body 20/24; P5 18/27; P3
  excerpts 18/24.
- **Pages:** P1, P2, P4, P5.

### 4. Book and print conventions in the text

- **Looks like:** a page set like a book or magazine rather than a blog.
- **Built:**
  - drop caps: a black drop cap about three lines tall opening every post (P9); a red
    drop cap about 100 px tall in a heavy rounded sans, overlapping the top-left of the
    text column and hanging out to its left (P7); a drop cap 5.7em high built from two
    stacked styles of the display face in teal and aqua, the rest of the first word in
    caps (P13);
  - quotation marks hung outside the text edge: the pull quote's opening mark (P10); 80
    px grey Georgia marks around the quote, the opening one in the space to the left
    (P11);
  - a byline centred over a short rule, small red letter-spaced caps, and a pull quote
    in 24/30 semibold italic opening the left column (P10);
  - paragraphs indented 24 px with no space between, the first paragraph flush (P5);
  - hyphenation on (P1 and P2 at phone width, P3, P5);
  - the site as a book object: a pulp-paperback cover with a black spine down the left
    edge, a "COMPLETE AND UNABRIDGED / 40¢" price badge and "Volume three in a series"
    (P9); past site versions listed like editions, v1 to v5 (P1).
- **Default it replaces:** block paragraphs with space between, no hyphenation, no drop
  caps, quotation marks inside the text block.
- **Reason:** for drop caps: "a drop cap to pull people in" (AIGA, accounts S5). For a
  bookish identity: A List Apart is "read religiously, not skimmed", and "we produce
  these as issues, not just updating our blog" (accounts S5; words: Reasons). Indents:
  web paragraphs are "chunked", so a 1 em indent or a blank line can separate them
  (words: Reasons, ch. 5). Smart quotes: bad quotes show more in big type (words:
  Refuses). Hung quotation marks, hyphenation and the P9 paperback: reason not stated.
- **Used / not used:** P1, P2, P3, P5, P7, P9, P10, P11, and on P13 the drop cap only:
  its running text has block paragraphs with 1.5em between, no indents and no
  hyphenation. Not on P4, P8 or P12.
- **Phone:** P5 keeps indents and no paragraph space, with heavy hyphenation; P1, P2
  turn hyphenation on at phone width; P3 hyphenates heavily. P13 shows no hyphenation.
- **Pages:** P1, P2, P3, P5, P7, P9, P10, P11, P13 (drop cap).

### 5. Dates and meta set apart in another face, in a margin or a ruled cell

- **Looks like:** the date is not a grey line under the title; it sits in its own
  place, in its own face.
- **Built:** P2: VCTR Mono 19.2 px grey rgb(106,118,135), right-aligned in column 1
  level with the figure; the caption and "Prev/Next" labels in the same mono. P3: month
  in small caps over the day, in a 58 px column. P5: narrow caps in a full-width light
  grey meta bar with tags and prev/next arrows. P6, P7, P10, P11, P12: a row of boxed
  cells divided by vertical rules, with small letter-spaced labels ("2008 / Aug 08",
  "COMMENTS 28"). P9: olive letter-spaced caps above the title.
- **Default it replaces:** a grey date line under the title in the body face.
- **Reason:** small type at about 80% of the base "signals a change in tone, like
  lowering your voice", and a separate caption face can signal a different speaker
  (words: Reasons, ch. 5). Why the date goes in a margin or a ruled cell: not stated.
- **Used / not used:** P2, P3, P5, P6, P7, P9, P10, P11, P12. Not on P1 (no dates), P4
  or P13 (no dates). P13 does set its captions and specimen labels in mono.
- **Phone:** P2 date moves above the image, caption 12.8 px mono, prev and next stack;
  P3 date goes above the title on one line.
- **Pages:** P2, P3, P5, P6, P7, P9, P10, P11, P12.

### 6. Rules as structure

- **Looks like:** sections and entries divided by drawn lines and bars, not by space or
  boxes.
- **Built:** P1, P2: full-width bars 18 px thick in a dark grey-teal between sections
  (12 px on phone). P3: 1 to 2 px dark full-width rules between entries. P5 to P8, P10
  to P12: double rules under titles and vertical rules between meta cells. P9: dashed
  olive rules inside posts, a solid dark rule between posts.
- **Default it replaces:** whitespace or card containers.
- **Reason:** not stated. His book describes his site as horizontal bands stacked down
  the page that "lead the reader along one message" and collapse into one column on
  small screens (words: Reasons, ch. 6); it does not speak of the rules between them.
- **Used / not used:** P1 to P3, P5 to P12. P4 has only a 1 px footer rule. P13 has
  no rules between sections: they are divided by full-bleed colour fields and
  horizontal stripe bands, and rules appear only as cell borders in its glyph grid
  (1.5 px pink) and stylistic-set grid (1 px grey gaps).
- **Phone:** P1 bars go from 18 to 12 px.
- **Pages:** P1, P2, P3, P5, P6, P7, P8, P9, P10, P11, P12.

### 7. Colour held to a ground, a text colour and one or two accents; the rest from images

- **Looks like:** flat type colour; any richer colour on the page is in a photograph or
  cover.
- **Built:** P1, P2: near-black ground rgb(23,25,29) over almost the whole page, body
  light grey rgb(206,210,216), intro and labels white, dates grey rgb(131,142,158),
  links underlined in a grey-blue rule; no accent in the type; colour only in the
  headshot, font thumbnails, book cover and specimen image. P4: exactly two colours per
  view, ground and text (seen: blue rgb(18,54,224) with teal rgb(50,224,201); mint
  rgb(143,223,209) with purple rgb(138,37,176); blue rgb(34,76,161) with mint
  rgb(121,226,200)). P3, P5: white, dark grey text rgb(68,68,68), one red
  rgb(223,71,71) for feature titles, the active-nav marker and one button; black footer
  about a fifth of the page height. P6, P7: one accent per entry taken from the
  entry's photo (yellow rgb(248,183,36) from the book cover; red #bb3a38 from the
  table). P10: ground #1a1a1a, text #ccc, light blue #8dbece for title and links, red
  only in the candy, the string and the byline. P11: #f5f5f5, #333, one red-orange
  #c30. P12: white, black, one red-orange; colour otherwise only in the photo. P9:
  cream rgb(255,253,223), rust rgb(153,51,0), olive rgb(136,136,68), black.
- **Default it replaces:** a brand colour plus several accents, tints and gradients.
- **Reason:** for one accent: the WordPress 2.5 orange was "something really punchy to
  offset everything else, so that when you needed a color it was going to be
  distinct"; "little bits of orange would really pop off the page" (words: Reasons,
  2014). Text colour #333 and a "medium gray" typographic colour so running text is not
  too high in contrast (words: Reasons, ch. 6). Loud Room: a randomising palette, each
  checked for basic contrast, enjoying "the bit of chaos when a garish palette shows
  up" (words: Reasons, 2026). On one colour that did not match the links: "sometimes a
  different color I'm using works better" (work P10). Why the accent is taken from the
  photo: not stated.
- **Used / not used:** P1 to P12 hold to it; P9 has two accents (rust, olive) on cream
  with black text. Not on P13: fourteen named colours (purple, pink, orange, yellow,
  green, blue, light blue, navy, indigo, cream, red, teal, aqua, tan) as full-bleed
  section fields, a hero of six diagonal stripes drawn as a hard-stop gradient at 46°,
  stripe bands between sections, a perspective-grid image fading through a gradient,
  and coloured type on coloured fields. For that page he says the colours go "right up
  to the line of 'clashing'" (work P13; words: Reasons, 2025).
- **Phone:** unchanged.
- **Pages:** P1 to P12.

### 8. Per-article art direction

- **Looks like:** individual entries on the same site look different from each other:
  their own ground, accent, link colour and title treatment, with the masthead and
  footer kept.
- **Built:** P6, P7, P10, P11 each load their own stylesheet (`css/entry/<slug>.css`)
  on top of the site sheet and change the page ground (white, textured light grey,
  #1a1a1a, #f5f5f5), the link colour and the title. Titles become image lettering
  (P6 condensed caps about 90 px in two colours; P10 heavy italic condensed caps about
  130 px, the two words stepped), a quote in American Typewriter 51/60 px (P11), or
  almost nothing (P7, an 11 px letter-spaced line). P6, P7, P10 build the entry around
  one photo of the subject; P11 has no image and is carried by the typeface. Each entry
  ends with "Design tags" naming its typeface and colours ("Photo, Titling Gothic,
  White, Yellow"; "Photo, Red, Soho"; "Blue, Grey, Photo, Proxima Nova, Red";
  "American Typewriter, Black, Grey, Red").
- **Default it replaces:** one template for every post.
- **Reason:** stated. In 2008 he was "disillusioned" that design had become "a bit
  player rather than a worthy partner to that content", so he built "a system" with
  fixed parts and per-post typefaces, colours, images, backgrounds, columns and layout,
  "much the same way one would approach the design of a magazine" (words: Process,
  Refuses). "Offhandedly dumping text into a column on a webpage used to pass for an
  article" (words: Refuses, 2014). On A List Apart, a colour scheme per issue and an
  illustration per article to be "not quite so templated" (accounts S5, S11). Reviewers:
  differences between his posts are "sometimes just subtle changes in background or
  typography" and sometimes "radical, but every one still has an element of
  'Jason-ness.' The header and footer are usually consistent" (accounts S9).
- **Used / not used:** P6, P7, P10, P11. Not on P1, P2, P3, P5, P9 (one template per
  site) or P12 (the v4 photo template). P1 calls the v4 entries "early experiments in
  online art direction" (work: Moves 8). P13 is a single client page, not one of a
  series, but is built the same way from its subject: retro packaging (VHS and cassette
  tapes, Polaroid, Trapper Keepers) and analog devices (calculators, keyboards, game
  controllers), gathered with the client as references (work P13; words: Process).
- **Phone:** none on v4, which does not adapt.
- **Pages:** P6, P7, P10, P11; P13 as a single page built from its subject.

### 9. Display type far larger than the text, kept large on phones

- **Looks like:** one piece of type, a title, label or quote, much larger than anything
  else.
- **Built:** P2: title HEX Franklin bold condensed 84/84 px over 24 px body, ratio 3.5.
  P4: title 147/147 px at weight 100 (hairline), letter-spacing -4.8 px, over 40 px
  body, ratio 3.7. P11: 51 px quote over 14 px text, about 3.6. P10: title lettering
  about 130 px over 14 px text. P1: section labels 40 px over 24 px body; the largest
  element is the 50.4 px intro, and version buttons are 55.2 px (ratio 2.3). P3: 70 px
  red feature titles over 16 px excerpts (4.4). P13: specimen words in the client's
  typeface up to `clamp(3rem, 14vw, 18rem)`, about 200 px over 18 px text (about 11),
  several running past both window edges; a statement in 115 px display type.
- **Default it replaces:** a modest heading scale that shrinks evenly on phones.
- **Reason:** "I usually work in simple math, doubling or tripling the body text size",
  then by eye; a small headline "can flatten your hierarchy" (words: Reasons, ch. 5).
  Very large type is "a picture of type that anchors a layout", like a movie poster or
  book cover, and a one-off decorative face can fit there, with line breaks tailored
  per screen size (words: Reasons, ch. 5). Contrast is "the most crucial tenet"; the
  most important thing need not be largest, only most distinct (words: Beliefs). Why it
  stays large on phones: not stated.
- **Used / not used:** P1, P2, P3, P4, P10, P11, P13. Not on P7 (11 px title) or P9
  (23 px titles over 13 px text).
- **Phone:** P1 labels stay 40 px while the intro drops to 28, so labels become larger
  than the intro. P2 title 56/56 over 16 px body, ratio 3.5 kept. P4 title 50 px over
  20 px body (2.5). P3 feature titles 30 px. P13 display words
  `clamp(4rem, 18vw, 16rem)`, about 70 px over 14 px text (5), the hero word split
  "Mega / zoid" over two lines. P10, P11 have no phone layout.
- **Pages:** P1, P2, P3, P4, P10, P11, P13.

### 10. A picture or letter that crosses the page's own structure

- **Looks like:** an object breaks out of its column, over a rule or past the layout's
  edge.
- **Built:** P7: the drop cap hangs out of its column; the Polaroid photo is the
  background of the entry area, anchored bottom-left, fading into the page ground at
  top and right, and running past the 910 px layout to the page edge. P10: a photo of
  a red Life Saver hangs on a white string from the nav bar, sits between and over the
  two title words, and overlaps the double rule and the meta row; at the end of the
  essay the same string, stained red, runs across the full 910 px and ends in a loop.
  P13: display words run past both window edges and are cut off
  (`overflow-x: hidden`), and a calculator drawn in CSS sits over the field of letter
  shapes.
- **Default it replaces:** images contained in their own frame.
- **Reason:** not stated for these pages. For Slate (with the firm Gretel) the stated
  direction was to show the story-making process, "allowing elements to overlap and pile
  on top of one another" (words: Reasons, 2018). Commenters on P7 praised how the photo
  was "integrated" with the write-up (work P7, reported).
- **Used / not used:** P7, P10, P13. On the other ten pages images stay inside their
  boxes and columns.
- **Phone:** P7 and P10 have no phone layout. On P13 the display words stay large at
  phone width (move 9).
- **Pages:** P7, P10, P13.

## What varies from project to project, and what decides it

- **Typefaces follow what the web allowed at the time** (work: What changes). Georgia
  and Lucida Grande with display faces as lettering images or sIFR (2004 to 2011);
  Typekit faces Chaparral, Proxima Nova, Facit (2011 to 2022); Roslindale, HEX Franklin,
  VCTR Mono (now). His shortlist of favourite faces "changes every so often" (words:
  Changed his mind). Monospace grows from dates, captions and nav (VCTR Mono on P1, P2,
  P4) to all the running text on P13 (Input Mono), where the display face is the
  client's typeface itself.
- **Ground and palette change per site, and on v4 per entry:** cream paper (P9), white
  with red (P3, P5), near-black (P1, P2), a two-colour pair chosen at random on each
  load (P4; words: Reasons; accounts S15).
- **The accent and the image follow the entry's subject** where there is art direction:
  yellow with the yellow book (P6), red with the red table and a photo of the camera
  written about (P7), a candy on a string for an essay about candy (P10). P11 sets a
  writer's quote in a typewriter face; reason not stated (work: What changes).
- **The personal sites carry a themed metaphor; the practice site does not:** P9 a
  paperback, P1 versions as editions; P4 sans text, hairline title, mono nav, two flat
  colours (work: What changes). Loud Room is "less a portfolio and more a statement of
  purpose", a few paragraphs he accepts as "a small amount of friction" (words:
  Reasons).
- **The client's subject sets the references and the mood words:** Mighty's
  industrial words to a bold condensed sans (words: Process); Megazoid's attic-box
  references to a subtle paper texture and colours "right up to the line of
  'clashing'", with almost everything reacting to hover or touch, "because this is the
  very place to have fun with web design" (words: Reasons, 2025); A List Apart's
  bookish standing to issue numbers, stamps, banners and a laurel wreath (accounts S5,
  S11). On P13 the texture is a paper image laid over the whole page with
  `mix-blend-mode: multiply`, and the code shows depth and stroke sliders, glyph cells
  that show the glyph at 80vh on hover, stylistic-set blocks that switch on hover or
  tap, letters that appear on scroll and a working calculator (work P13). A textured
  paper ground also appears on P7 and P9; a reason is given only for P13.
- **The one client page against his own sites** (work: What changes, P13). P13 keeps
  the drop cap, display type about ten times the text and kept large on phones, a page
  built from its subject's references, a paper texture, letters breaking the page's
  frame, and mono type. It drops serif text, the label column, rules and boxed meta as
  structure, the restraint to one or two accents, large body text, hyphenation and
  indents. It adds what none of his own pages show: many colours with gradients and
  stripes, a rendered object (the calculator), interactive specimen controls, keycap
  boxes (white, 1 px grey border, rounded corners) for letters named in the text,
  specimen words stacked as echoes at stepped sizes and offsets, and pill-shaped
  buttons. Which of these come from the brief and which from him cannot be separated
  from these sources; he says the brief for such sites is to show what the font can do
  and "have fun with it" (work P13, from P2).
- **Phone handling follows the period** (work: What changes): v3 and v4 do not adapt;
  v5 collapses to one column, drops link-post photos and shrinks titles; the current
  sites P1, P2, P4 keep their grid on phones and keep labels large; P13 goes to one
  column, cuts section padding to 2rem and keeps its display type large.

## Refusals

What he says he will not do, or dislikes (words: Refuses; accounts: Refusals).

- Helvetica or Arial as a default choice: "a generic default" used out of "the fear of
  making a bad choice".
- Dumb (straight) quotes; `<br><br>` for spacing.
- Baseline grids on the web: images, forms and rendering throw them out of phase, CSS
  lacks the controls, and their print purpose is moot on screen.
- Designing by the numbers: "It's very easy to become bound to the numbers instead of
  what looks appropriate."
- More than one display or script face in a design; text faces with too much
  personality; free fonts with poor kerning and hinting; Caslon on screen; icon fonts.
- Content dropped into a template with design as "a bit player".
- Clichés of the client's category (leprechauns for Irish music) and piggybacking on a
  trend: "This makes us look like anybody else."
- Over-decorated skeuomorphism ("stitching, leather, torn pages. Blech.") and "flat"
  treated as more than a veneer.
- Concern with the fold: "I actually don't really concern myself too much with the
  fold."
- Grid frameworks: "I'm not big on frameworks"; the Loud Room site uses none.
- Design by committee where every opinion weighs the same.
- Generic machine-made design; models trained without consent.

## Mismatches

What he says that the pages studied do not show:

- **Base size.** He gives 16 to 18 px as the base (words: Reasons, ch. 5, 2014). The
  current pages set body at 24 px (P1, P2) and 40 px (P4); the pre-2011 pages at 13 to
  14 px. P13 (18 px at 1440 px) falls inside it.
- **Headline ratio.** He says he doubles or triples the body size. Pages run 3.5 (P2),
  3.6 (P11), 3.7 (P4), 4.4 (P3), about 9 (P10 lettering) and about 11 (P13 specimen
  words); only P1 (2.3) falls in his range.
- **Measure.** He gives 45 to 75 characters. P1 runs about 79, P2 about 76, P9 about 150
  at 1440 px. P13 (about 60) falls inside it.
- **Number of typefaces.** He writes that "the more typefaces I use in a design, the
  weaker the design becomes" and describes his site as two families (words: Reasons,
  2014). P1 and P2 use three (Roslindale, HEX Franklin, VCTR Mono); P3's CSS names
  three (Chaparral Pro, proxima-nova, Facit); P11 uses American Typewriter, Georgia and
  Lucida Grande. P13's own block uses two (Megazoid and Input Mono).
- **Collapsing to one column.** He says a hierarchical grid stacks into one column on
  small screens (words: Clients and phones). P3, P5 and P13 do; P1 keeps a 4-column
  grid at 342 px.
- **An eight-column grid on v4.** He describes v4 as "a basic eight column grid"
  (words: Process, 2008). The work notes found no column system on P6 to P12 beyond the
  sidebar and content split and the two text columns on P6 and P10 (work: Looked for
  and not found).
- **Logos.** In 2014 he said he tries to avoid designing logos; in 2026 he "had a blast
  creating the logo" for Loud Room, without calling it a change of mind (words: Changed
  his mind).

What the pages show that no source explains:

- Taking the entry's accent colour from its photograph (P6, P7).
- Hanging quotation marks outside the text edge (P10, P11).
- Keeping the P1 section labels at 40 px on phones, so they outgrow the intro.
- The 18 px bars between sections (P1, P2).
- Pinning the v4 layout to the left edge of the window instead of centring it (P6), and
  setting the P5 text column off-centre in its area.
- Setting a writer's quote in American Typewriter (P11).
- The pulp-paperback treatment of v3 (P9).
- The weight-100 hairline title at 147 px on Loud Room (P4).
- Mono for dates, captions and prev/next on the current site (P2), beyond the general
  statement that a caption face can signal a different speaker.
- The Daily Photo reused as a thin cropped band ("MEDA") in every v4 footer (P12).
- On P13: keycap boxes for letters named in the text, specimen words stacked as echoes
  at stepped sizes and offsets, the calculator rendered in CSS, the 46° stripe hero, and
  pill-shaped buttons at the bottom edge of a hero at least 90vh high. The stated brief
  ("have fun with it", colours up to "clashing") covers the page's spirit, not these
  particular choices.

Where the notes differ: the work notes could not establish what sets Loud Room's colour
pair (work P4); his own post says it is a randomising palette checked for contrast
(words: Reasons) and Rob Weychert calls it "procedurally-generated ... every time it
loads" (accounts S15). His statement that almost everything on the Megazoid site reacts
to hover or touch (words: Reasons) agrees with P13's CSS and script, which hold hover,
tap, scroll and slider behaviour (work P13); that behaviour was read from the code, not
watched.

## Gaps

No source covers:

- motion, hover and transitions as seen in a browser on any studied page (P13's are
  known only from its code);
- how he crops or places photographs in a layout (words: Looked for and not found),
  beyond what the pages show;
- how he chooses colour in general, beyond the WordPress orange, the Slate maroon,
  Megazoid and Loud Room;
- live client sites other than P13 (clients named on P1 and P4 were not checked), and
  the Loud Room shop, so no shop or product page of his;
- a written rationale for the v5 or current jasonsantamaria.com design, or for the Loud
  Room logo;
- non-Latin scripts, including Thai and Japanese;
- what he argued for on the A List Apart 5.0 strategy team.
