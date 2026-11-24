# Frank Chimero: synthesis

Written from the three notes files alone: `notes/work.md` (pages studied, cited as
"work p1" to "work p9" for its numbered pages and "work move N" for its comparison),
`notes/words.md` (cited by the short source name used there, such as "RWD 2017" or
"SoD 03-improvisation-and-limitations") and `notes/accounts.md` (cited by source). The
URLs are in the notes.

Pages 1 to 8 and 11 in the work notes are his own sites: frankchimero.com home (p1), an
essay (p2) and the Dust collage page (p3); his 2021 portfolio index (p4) and its Info
page (p11); the 2025 Studio Frank splash (p5) and 2020 studio info page (p6); The Shape
of Design book landing (p7) and online chapter (p8). Pages 9 and 10 are client marketing
home pages, moderntreasury.com (p9) and dropmark.com (p10). Both live pages have changed
since the dates their credits give (p9's content since 2023 and his 2025 departure;
p10's assets are versioned May 2023, its footer reads "Made by Oak Studios", against a
2019 credit), and which parts of either are his is not known (work, Sources caveat and
p10). They are reported here, but no move rests on them.

## Order of work

As his words describe it; the accounts add little (accounts, Process).

1. **Objectives, then put them away.** He starts by asking Why: "What are the objectives
   of the project?" and "What are we actually building this for?", answered "before any
   design begins" (words: Print 2015). Then "put those objectives in a drawer" so they do
   not crush early ideas, and bring them back later as the rudder (words: SoD
   03-improvisation-and-limitations). He prefers an objective ("Realign our company")
   to a task ("redesign our letterhead") (words: why-vs-how 2013).
2. **The one or two true things.** On the web his job is to "identify and express the one
   or two uniquely true things about their project or company, then enhance it through a
   memorable design with a light touch" (words: everything-easy 2018). He picks the one
   thing a piece should do and spends a long time choosing it (words: ten-principles
   2009). For illustration, "All the effort is front-loaded" into the concept (accounts:
   PRINT 2010).
3. **Limits before starting**, sorted into content, structure and tone: "Saying no
   beforehand allows yes to be said unequivocally while working" (words: SoD
   03-improvisation-and-limitations). He re-examines the defaults of message, tone and
   format at the start of each project (words: SoD 04-form-and-magic).
4. **Start from the most limiting environment** and let its rules spread to the rest of
   the system; for the book that was the e-reader (words: designing-in-the-borderlands
   2014).
5. **Phone width first.** Every layout starts at phone width, which reduces the problem
   to the order of elements in one stack and settles hierarchy; wider layouts "inherit"
   it (words: RWD 2017). Sketch arrangements of elements, then put the box around them
   (words: the-webs-grain 2015).
6. **A canvas tool only for colours side by side, the typeface, relative type sizes and
   hierarchy**, then markup "as soon as I can"; breakpoints and the measure of the type
   are felt out in markup (words: RWD 2017). Ethan Marcotte reports web fonts and
   performance are "a very early aesthetic question" for him (accounts: RWD 2017).
7. **Every state of the content**: "What does the page look like if it is empty? If it
   is full?" (words: super-hi-foreword 2017). For responsive work he delivers "sets of
   rules for how content can adapt", not one artifact (words: RWD 2017).
8. **Show it early and incomplete**, in loops that are "tight and open" (words:
   on-iteration 2010); accept every contribution early and edit late (words: SoD
   03-improvisation-and-limitations); stay open longest, since "Two-thirds through is
   where the good surprises tend to happen" (words: work-looks-back 2018).
9. **Edit.** "If it isn't spectacular, it gets cut" (words: ten-principles 2009). When
   stuck on screen, print it out and move it around on paper (words: advice 2010).

He leans on content more than looks: "a great photo, memorable illustration, or
pitch-perfect sentence does most of the work" (words: everything-easy 2018), and "the
more input I have in the content and strategy of the project, the less burden I place on
the aesthetics" (words: plainness-and-sweetness 2017).

## Moves

One entry per move in the work notes (work moves 1 to 10).

### 1. The screen split in two, one half held still

- **Looks like:** at 1440 px the viewport is cut at the centre. The left half (720 px)
  is dark and holds the site header and navigation; the right half is the page's
  content (work p1–p3). On the book chapter the left half is an empty textured panel
  holding one small drawing, with the text on the right (work p8).
- **Built:** left half sticky or fixed at full viewport height; right half scrolls in
  its own box (`overflow-y: scroll`, height 100dvh), padding calc(3vw + 1rem) ≈ 57 px,
  text column max 36rem (504 px) centred in that half (work p2). Book: fixed 98 px bar,
  then a fixed panel x=70–720 (50vw − 5rem), text from x=769, max 30em (work p8). On the
  home page the right half is simply empty (work p1).
- **Default it replaces:** one centred column under a horizontal top bar (work move 1).
- **Reason:** for a side navigation column on the 2017 version of his site, he says the
  site had many pages and he did not want hidden navigation, and admits it looks "very,
  very reminiscent of 90's frames" (words: RWD 2017). The page studied is a later
  version. For the fixed image panel on the book (p8), reason not stated.
- **Used:** p1, p2, p3, p8. Pages 6 and 11 split at the centre line (text starts at
  x≈731–733), but nothing holds still; both halves scroll. **Not used:** p4, p5, p7,
  p9, p10.
- **Phone:** the halves stack. The fixed half becomes a band on top (dark, ~315 px,
  full nav visible; p2) or a near-full screen of its own (390×772) holding the drawing
  before the text (p8).

### 2. One text size; hierarchy by colour and weight

- **Looks like:** titles at body size, set bold or in an accent colour; secondary lines
  at the same size in a dimmer tint.
- **Built:** p1: Courier 13 px / 19.5 px for every word, titles #eeeeee, descriptors
  #717d78. p2–p3: 14 px / 21 px body; title 14 px bold centred, date under it in dim
  #828b87; captions and footer 13 px. p8: Lyon Text 20 px / 27 px; the chapter title is
  the same 20 px in rust #b95b23. p6: labels the same 17 px as the text in pale green,
  one heading at 23.8 px (1.4×). Ratio of largest to body: 1.0 (p1, p2, p8), 1.4 (p6).
- **Default it replaces:** an H1 2.5–4× body with a size step per level (work move 2).
- **Reason:** for The Shape of Design he gives one: all the type at one size, with
  negative space and capitals making hierarchy, so "all the book's text retains its
  hierarchy, regardless of the user's settings" on e-readers (words:
  designing-in-the-borderlands 2014). For his personal site, reason not stated.
- **Used:** p1, p2, p3, p6, p8. **Not used:** p4 (names 4.1× body), p5 (2.6×), p9
  (2.9×), p10 (3.0×), p11 (running biography in a serif at 36 px against 14 px sans
  labels, 2.6×; the largest size is the running text). Page 7 has no running text.
- **Phone:** sizes do not change: 13 and 14 px on p1–p3, 20 px on p8 (about 35–37
  characters a line); p6 goes from 17 to 16 px.

### 3. Two-line labels: a name, a dimmer line under it at the same size

- **Looks like:** "Studio Frank" over "My design practice"; "Frank Chimero / Design
  stuff / 2007–2021"; "Chapter One" (dim, mono) over "How and Why".
- **Built:** item title on one line, a descriptor, date or number on its own line under
  it in the dim colour; no size change, no icons (work move 3; p1 nav descriptors such
  as "Book · 2012").
- **Default it replaces:** one-line links in a horizontal bar; larger headings.
- **Reason:** reason not stated.
- **Used:** p1–p3 nav, p4 and p11 header, p6 ("Frank the Office" over its paragraph),
  p7–p8 table of contents. **Not used:** p5, p9, p10.
- **Phone:** kept, as part of the stacked nav list (p1–p3).

### 4. Navigation as a short vertical list on a grid column, visible on phone

- **Looks like:** two to six links stacked one per line, starting at a column line
  rather than right-aligned in a bar.
- **Built:** x=360 in a `1fr 1fr` header (p1); x=707, column 7 of 12 (p4); x≈731–733,
  the page's centre line (p6, p11; on p11 the current item is dark, the other at 40%).
- **Default it replaces:** a horizontal bar right-aligned, hamburger on phone.
- **Reason:** for phones, his site has few items: "let's just put seven words up on the
  screen for you to tap on" (words: RWD 2017). He dislikes hiding mobile navigation
  behind a show/hide panel (words: RWD 2017).
- **Used:** p1, p2, p3, p4, p6, p11. **Not used:** p7, p8 (menu button in a left bar),
  p9 (horizontal bar, hamburger), p10 (horizontal right-aligned bar ending in a filled
  "Sign up" button; a "Menu" text button on phone). Page 5 has no navigation.
- **Phone:** the same list stays on the page, no menu button (p1–p3); between 500 and
  999 px p1's list becomes two columns; p4 and p11 keep their two-column header.

### 5. A large empty field, often half the screen

- **Looks like:** a measured block of nothing beside or above a small amount of type.
- **Built (measured):** p1, the right half empty, 720×891 (50% of the screen); p4,
  ~390 px of black between header and list (header margin 140 px plus first row
  25vh), 44% of the first screen; p5, the top ~600 of 891 px is only sky, the sentence
  low and left of centre; p8, a 650×891 panel holding a ~140×190 drawing, about 5%
  filled; p11, ~200 px of empty ground under the header (~24% of the first screen) and
  columns 1–2 left empty beside the portrait. Smaller: p2–p3 have ~84 px above and below
  a centred title.
- **Default it replaces:** content filling the width, a hero with an image beside the
  text.
- **Reason:** reason not stated.
- **Used:** p1, p4, p5, p8, p11; smaller on p2, p3. **Not used:** p6, p9, p10 (sections
  packed in sequence).
- **Phone:** p5 stays bottom-anchored; p8's drawing takes its own near-full screen; the
  notes do not record what p1's, p4's and p11's empty fields become.

### 6. A monospace or typewriter face as the working voice

- **Looks like:** monospace for navigation, labels, dates and metadata; on the personal
  site, for every word including long essays.
- **Built:** `Courier, mono` 13–14 px for everything (p1–p3), essay lines about 57–60
  characters; Pitch 14 px / 24 px for quotes, labels, next-chapter label and footer,
  with a serif for reading (p7–p8); mono for labels, numbers and code (p9).
- **Default it replaces:** one sans family for UI and text.
- **Reason:** reason not stated.
- **Used:** p1, p2, p3, p7, p8, p9. **Not used:** p4 and p11 (system sans), p5 (Söhne),
  p6 (system sans), p10 (two sans families, no mono).
- **Phone:** same faces and sizes.

### 7. Oldstyle numerals on

- **Built:** `font-variant-numeric: oldstyle-nums proportional-nums` (p1–p3); `onum`,
  tabular for the year column (p4); `onum` (p11); `onum` and `kern` (p7–p8).
- **Default it replaces:** lining figures.
- **Reason:** reason not stated.
- **Used:** p1–p4, p7, p8, p11. **Not used:** p5, p10. Not checked: p6, p9.

### 8. Hand-made or found imagery, one piece at a time

- **Looks like:** archival photographs collaged (p3); a small black engraving-style
  drawing, a candle lit by another candle (p8); a single-weight hand-drawn line
  portrait in the text colour and a hand-lettered logotype (p6); the book cover shot as
  an object with four stacked soft shadows to the lower left (p7).
- **Built:** one image per row or per panel, never a grid of thumbnails. p3: 21 square
  collages, each 504×504 at the text column's width, one per row, 56 px apart, no
  captions; old black-and-white and sepia photographs, torn paper edges, flat geometric
  shapes (semicircles, arches, rings), thin hand-drawn lines, one ochre/rust accent, on
  a warm grey paper ground. p6: the drawing ~476×425, centred in the left column. p8:
  ~140×190 centred in a 650×891 panel. p2's video stills follow the same placement:
  column width 504, radius 2 px, 56 px above and below, centred 13 px dim caption.
- **Default it replaces:** product screenshots or stock photos in a card grid.
- **Reason:** for his illustration, flat vector "Looks computerish… We need to get some
  hands in to this" (words: Grain Edit 2009); PRINT describes geometric vector
  illustration "humanized by hand-tracing the outlines and rescanning" (accounts: PRINT
  2010). For the book, line-etching illustration because it looked best on a Kindle's
  e-ink screen (words: designing-in-the-borderlands 2014). Dust says its collages
  "gather old, forgotten images from public archives" (work p3); that says what, not
  why.
- **Used:** p3, p6, p7, p8. **Not used:** p1, p4 (no images), p2 (borrowed video
  stills), p5 (sky photograph), p9 (UI mocks and diagrams), p10 (flat vector
  illustration, card carousel, logo strip), p11 (one black-and-white portrait
  photograph cropped to a circle, max 18rem, multiplied into the ground: one image set
  small beside empty columns, but a photograph, not made or found).
- **Phone:** images take the column width (339 px square on p3); p6's drawing comes
  first, centred, 274 px; p7's cover 210 px wide centred; p8's drawing gets its own
  screen.

### 9. A muted single-hue palette with at most one accent

- **Built:** one family of tints for field and text, plus one accent used only for
  links, hover or one element.
  - p1–p3: dark grey-green #3d4340 field (the left half, 50% of the screen on p2), light
    #eeeeee reading half, text #2f3432, dim #717d78 / #828b87; hover green #5e786d.
  - p6: cream #F9F7EA field, olive #515F44 text and drawing line, pale green #A5AF9B
    labels and link underlines. Nothing else.
  - p7–p8: grey #dfdfdf with a 100 px tiled paper texture multiplied over it, text #333,
    rust #b95b23 for the chapter title and link and button hover.
  - p4: black #000, white names, 40% white metadata, rules 1 px at 12% white.
- **Default it replaces:** white background, one bright brand blue for buttons.
- **Reason:** reason not stated. (For an illustration he said "you can't put an orange
  on the train if the whole train is orange" (words: Grain Edit 2009), and PRINT reports
  a two-or-three-pastel illustration palette from screen-printing (accounts: PRINT
  2010); both concern illustration, not these pages.)
- **Used:** p1–p4, p6, p7, p8. **Not used:** p5 (saturated sky blue with pure yellow
  #ffee00), p9 (several pale tints plus a green brand), p10 (six saturated hues,
  including purple #9163f9), p11 (black text on a pale ground, hsl(…, 70%, 90%), that
  moves through every hue in turn, including lavender and periwinkle: one ground colour
  at a time, but not one hue).

### 10. Motion limited to hover colour and page fades

- **Built:** 0.2–0.3 s colour or opacity transitions on links and buttons (p1 title
  fades to the dim colour 0.2 s; p2 link hover to green 0.2 s; p4 header links 40% to
  white 0.2 s; p5 button yellow to black 0.3 s; p6 opacity 0.3 s, background 0.6 s);
  whole-page fades out 500 ms / in 300 ms, easeInOutCirc (p4, p11); a menu slide 0.3 s
  (p7); an arrow that moves 1rem right on hover, 0.2 s (p8). No page has
  scroll-triggered reveals, parallax or custom cursors.
- **Default it replaces:** fade or slide-in on scroll.
- **Reason:** he dislikes "fancy animations and transitions" in his web work and
  marketing "whizzbangery" (words: RWD 2017); "no razzle-dazzle" (words:
  everything-easy 2018). In 2013 he listed functional motion: animated scrolling to keep
  context, stateful toggles, sticky labels, progressive disclosure (words:
  what-screens-want 2013).
- **Used:** p1, p2, p4, p5, p6, p7, p8, p11. **Exceptions:** p7's buy buttons rotate
  continuously on hover; p11's whole background moves through the hue circle by itself,
  hsl(160 → … → 60, 70%, 90%) over 130 s, endlessly, after a 2 s delay; p9 animates its
  rail diagram; p10 animates its illustration in on load (pieces 0.5 s each, staggered
  0–1.2 s), advances a card carousel every 3 s and scrolls a logo strip without end.
- **Phone:** the notes do not record motion at phone width.

## What varies from project to project, and what decides it

- **The medium's conventions.** The book site takes print book setting: serif reading
  face, unspaced paragraphs indented 1.5em after the first, hyphenation, chapter
  openers, paper texture, the cover shown as an object (work p7–p8). The personal site
  takes the typewriter: Courier for everything at one size (work p1–p3). What he says
  about it: start from the most limiting environment and let its rules spread (words:
  designing-in-the-borderlands 2014), and re-examine the defaults of message, tone and
  format each time (words: SoD 04-form-and-magic).
- **Typefaces change every project.** Courier (p1–p3); Newsreader and system sans (p4,
  p11); Signifier Light and Söhne (p5); system sans only (p6); Lyon Text and Pitch
  (p7–p8); a custom grotesk, sans and mono (p9); two custom-named sans families (p10).
  No face repeats across projects; within a project the pairing holds (p4 and p11)
  (work, What changes). He redesigns his own site every year (words: RWD 2017;
  accounts: Marcotte, Eden). "Consistent voice is more important than consistent
  style" (words: ten-principles 2009).
- **Within one site the faces can swap roles.** On p4 the serif is for short project
  names at 4vw (57.6 px) and the sans for running descriptions; on p11 the serif is the
  running biography at 36 px and the sans is for lists and labels at 14 px. What decides
  this is not stated.
- **The ground changes:** dark grey-green (p1–p3), black (p4), photograph (p5), cream
  (p6), textured paper (p7–p8), white (p9), white and warm off-white (p10), a pale ground
  cycling through the hues (p11). Within one site it can change by page: p4 black, p11
  moving pastel.
- **Studio pitch versus his own writing.** The 2025 studio splash is the only own page
  with a large headline (Signifier 36 px, yellow, three balanced lines), saturated
  colour and a full-bleed photograph; the pages for his writing and archive (p1–p4, p8)
  keep sizes flat and colour muted. The 2021 about page (p11) sets its biography large
  (36 px) but keeps to one pale ground at a time and black text. What decides this is
  not stated by any source.
- **Client marketing pages (p9, p10)** both follow the conventional software marketing
  order (hero with two buttons, illustration or diagram, feature cards, logo strip,
  stats, form or footer sitemap), with cards or rounded panels and saturated or
  multiple tints; none of his own sites do. Both live pages have changed since the
  dates their credits give, so whether this is his choice or later edits is not known.

## Refusals

From his words unless marked.

- Simplicity and seamlessness as goals; he wants clarity: "Simple things are weak… What
  I truly want is clarity… Make me things that are full of seams" (only-openings 2014;
  also the-cloud-is-heavy 2013, the-webs-grain 2015).
- Sites that work against the web ("bicycle bear websites"; Apple's Mac Pro page as
  "fragile, willfully esoteric") (the-webs-grain 2015); Flash-style immersive pieces
  (what-screens-want 2013); marketing "whizzbangery" (RWD 2017).
- Hiding mobile navigation behind a show/hide panel; fancy animations and transitions
  (RWD 2017).
- Complex toolchains for small sites; illegible source, "the legibility of the source is
  one of the most important properties of the web" (everything-easy 2018).
- Claiming a flat or skeuomorphic look because of the screen: "Screens are aesthetically
  neutral" (what-screens-want 2013).
- Things made to look special: "Special things demand attention for the wrong reasons"
  (Jasper Morrison, quoted in plainness-and-sweetness 2017). Helvetica and Times as
  plain choices, because of their associations (same).
- Minimalism "without cause"; "Stop trying to be cool" (advice 2010). Purple: "It's
  hard to make purple work in a design" (advice 2010).
- Showmanship, gimmick delight, imitation without purpose, iterating only on existing
  forms (SoD 01, 02, 04, 09). Cold, "excessively composed" work (SoD 09).
- Design that generates desire rather than meeting it; dark patterns and commodified
  attention (the-long-hard-stupid-way 2011; SoD 10; what-screens-want 2013).
- Working under a generative model, "the model's limits become your own"; the "pull of
  the averaging effect" (beyond-the-machine 2025).
- A crutch "in the way that things look" (Format 2015).
- "I love ideas more than prettiness" (accounts: PRINT 2010).
- Yearly-renewal web font licences, "a web tax" (accounts: TypeDrawers 2020).

## Mismatches

What he says he does that the pages studied do not show:

- **The book's type.** He says the book uses one typeface at one size, Quadraat, with
  negative space and capitals for hierarchy (words: designing-in-the-borderlands 2014);
  Fonts In Use lists Quadraat, Quadraat Sans and Trade Gothic for the website and online
  edition (accounts, 2012). The live chapter uses Lyon Text 20 px and Pitch 14 px, and
  marks the chapter title with rust colour, not capitals (work p8). Who changed it and
  when is not stated.
- **His site's typefaces.** Fakt and Arnhem in 2017 (words: RWD 2017); a 2021 blog saw
  "three boxes on the homepage" (accounts: Yaguara). The live site is Courier in two
  halves, no boxes (work p1). He redesigns yearly, so these describe earlier versions.
- **Untitled Sans and Untitled Serif** as studio staples (words: plainness-and-sweetness
  2017): no page studied uses them; the studio pages use system sans (p6, 2020) and
  Signifier and Söhne (p5, 2025).
- **Navigation always visible on phones** (words: RWD 2017): true of p1–p4, p6 and
  p11; the book pages put it behind a menu button (p7–p8), p9 uses a hamburger and p10 a
  "Menu" button.
- **No fancy animation** (words: RWD 2017; "no razzle-dazzle", everything-easy 2018):
  p7's buy buttons spin continuously on hover, and p11's whole background moves through
  the hue circle on its own, endlessly, over 130 s. On the client pages, p10 animates
  its illustration in on load, auto-advances a carousel and scrolls a logo strip
  without end; p9 animates a diagram.
- **Flat colours and simple gradients**, because they scale to unknown proportions
  (words: the-webs-grain 2015, super-hi-foreword 2017): p7–p8 use a tiled paper texture
  and p5 a full-bleed photograph.
- **Purple.** "It's hard to make purple work in a design" (words: advice 2010, advice to
  students): his own p11 passes its ground through lavender and periwinkle (hues 250–300
  at 70% saturation, 90% lightness) as part of its cycle; the client p10 uses purple
  #9163f9 among six hues.

What the pages show that nobody explains: Courier for every word on the personal site
(p1–p3); one text size there; the two-line labels; the empty half screen (p1) and the
other measured empty fields; the right half scrolling in its own box while the left
holds still on p2–p3; oldstyle numerals; the single-hue palettes; the 2025 splash's
large yellow headline over sky and its two 1 px hairlines drawn over the photo at the
column edges (p5); vertical spacing in multiples of the line height (p6); the Dust
collages' make-up (p3); p11's ground cycling through every hue with the portrait
photograph multiplied into it, and the serif and sans swapping roles between p4 and
p11.

## Gaps

No source covers:

- A grid he uses in his own words: column counts, gutters, margins (words, Looked for).
  The only grid numbers are measured: p4's and p11's 12 columns with 14 px gaps and
  28 px outer padding, p1's `1fr 1fr` header, p6's `1fr 1fr` with a four-column lower
  section.
- Type numbers in his own words: body size, scale, line length, line height.
- A palette or colour proportions in his own words for web or brand work.
- A live case study, in his words or a client's, of any client project (Wikipedia, NPR,
  Modern Treasury, Fictive Kin, Studio Frank, Dropmark); what he shows a client at each
  stage of a brand project; how a client design changes along the way.
- Which parts of today's moderntreasury.com are his, and whether the live dropmark.com
  home is the October 2019 page he designed (its assets are versioned May 2023;
  Dropmark's own post on the redesign returned 403).
- An essay or talk by him still live as its own designed page: What Screens Want, The
  Web's Grain, Everything Easy is Hard Again, The Good Room and Beyond the Machine are
  all in the frankchimero.com template now, and the standalone What Screens Want address
  returns 404 (work, Looked for).
- How he treats phones beyond phone-first stacking and visible navigation; a third-party
  account beyond Marcotte's remark that his sites "feel at home" on different screens.
  Dropmark's phone treatment was not recorded.
- A critical review of his web or print design work.
- His writing from 2022 to mid-2025.
