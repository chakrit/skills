# Rob Weychert: synthesis

The design model behind `style.md`, drawn from four research streams in `notes/`.
Citations name the note and the section or move heading: `own "Weight runs inverse"` is
that move in `notes/own.md`; `work table` is the project table in `notes/work.md`;
`talks 1.2` is move 1.2 in `notes/talks.md`; `accounts "Let the empty space"` is that
move in `notes/accounts.md`; `§2` and `§3` are each note's process and taste sections.

Evidence marks follow the notes: **(said)** he states it, or someone else reports it;
**(seen)** the point was checked by eye in a browser on 2026-11-23; **(code)** it rests
on HTML, CSS or JS read without rendering. The `talks` and `accounts` streams used no
browser, so nothing visual rests on them alone.

## 1. The core idea: a system with room for the hand

He is a print-trained editorial designer who builds a small set of rules, lets the rules
generate the page, and then overrides them by eye where the result looks wrong. He calls
it making "space for the spontaneous within the systematic" (own §2) (said). Almost every
piece of his work can be described as a few variables and the values he chose for them:

- one **interval** that sets type sizes, weights, grid proportions and colour rotations
  (own "One interval governs", "Weight runs inverse") (said; code);
- one **grid** defined by four ratios rather than handed down by a framework (talks 1.5;
  work "A small set of spatial parameters") (said);
- one **hue** that every colour role derives from, often keyed to a date (own "Colour
  keyed to the date") (said; seen);
- a **rule set** that produces every variation, shown in full (work "Enumerate every
  case") (said; seen).

The system "is the foundation" but "doesn't have the final say": he bumped V6's smallest
size from 12 to 13.5 px because it looked better (own "One interval governs") (said).
Sometimes "you just have to eyeball it" (own §2) (said).

## 2. Method: the convention, then where it fails this content

His stated method, in order (talks 1.1; accounts §2) (said):

1. Name the problem.
2. Apply "the most conventional way of solving that problem": flow the text into a
   standard layout, list the items in a plain list.
3. Read it as a reader and ask "how is that convention insufficient" for this story.
4. Add or subtract until the design answers "the very specific problem to be solved as
   opposed to the category of problem".

Two consequences:

- **The deviation is small and single.** The rape investigation kept the single text
  column and only moved it right and left with the story's two states, "a dead simple
  minor deviation from a well-worn convention" (talks 1.2; work "Bend one convention")
  (said). One variable carries the structure.
- **Frameworks outsource the thinking.** Bootstrap layouts and generic pattern libraries
  hand the work to someone who does not know the problem; his complaint is that people
  skip finding "what makes the thing that they're working on unique" (talks 1.1, §3;
  accounts "House type scale") (said).

Before any of this comes an **inventory**: every kind of text on V6 listed by frequency
(own "Reduce text roles"), every field a concert-goer scans for (work "Listings designed
for scanning"), reader-survey goals ranked by stakeholders before The Markup mockups
(work "Mission first") (said). "The content is the arbiter of the layout" (own §2)
(said).

## 3. Where ideas come from

- **Visual thinking from outside the discipline.** The Lost Mothers dot grid came from the
  dot-grid floor of ProPublica's elevator: "Oh! That could be an interface" (talks §2;
  accounts "Let the empty space") (said). He values this "visual thinking acumen" above
  cultural literacy (talks §2) (said).
- **Printed vernacular and midcentury graphics.** Gig handbills (the Trocadero's
  photocopied monthlies), screen-printed gig posters, Reid Miles's Blue Note covers, Saul
  Bass, Sol LeWitt, Chris Ware, Lego instructions, technical drawing, horror posters,
  VHS, zines (own §3; work §3) (said).
- **Music.** He compares a type scale to a musical key (own "One interval governs"); a
  title sequence started from a drum track he wrote (work "Title sequences") (said).
- **Constraints chosen up front.** Haiku in 5-7-5, 48-hour films, only League of Moveable
  Type fonts for Zaly9, one 16:9 screen for Once in a Lifetime (talks 1.7; work §2)
  (said). A ten-lane highway without lane lines would be a nightmare (talks 1.7) (said).
- **Paper before the browser.** The 149 grid partitions "can't be designed in the
  browser"; cube variations were drawn by hand until a formula showed (own "Make variety
  from combinatorics"; work §2) (said). He admits diving into code too early and wants a
  middle ground between wireframe and finished piece (talks §2; accounts §2) (said).

## 4. Type

- **Weight inverse to size: two technical pens.** On V7 all type should look drawn with a
  thin pen or a thick one, after the Rapidograph pens of his college years. Size =
  base × interval^step and weight = base weight ÷ interval^step, so large type is light
  and small type heavy: on a 24 px base with a 1⅓ interval, 42.7 px is weight 225 and
  18 px captions weight 533 (own "Weight runs inverse") (said; code: home page intro 39 px
  at 225, name 70 px at 700 as the thick pen). Border width is 1/16 rem, matched to the
  face's stem, and icons are stroke-only on a 16 grid with the same inverse scaling
  (said). The page reads calm, as if headline, body and rules were cut from one material
  (seen).
- **Few roles, two voices.** V6 found nearly all text could use two sizes plus two rare
  ones (own "Reduce text roles") (said). Faces are paired by job: "left brain" structure
  (nav, metadata, labels, headings) in a slightly condensed geometric sans, "right brain"
  authored prose in a transitional serif reserved "exclusively for when I'm speaking
  directly to the reader" (said; V6 Ciutadella + Freight Text, code and seen). V7 moves to
  one low-contrast sans, Degular, "less sterile than a geometric" (said; seen).
- **Scale named from the body.** Steps are `--scale0` (body), `--scale1`, `--scale-1`, so
  he always knows the distance from body text (own "One interval governs") (said).
- **Variable width to fit the cell.** Tinnitus Tracker headliners use a variable font
  whose width axis is matched to each cell, tested against the longest name (own "Make
  variety from combinatorics") (said).
- **Print craft, translated.** 66-character measure, 2.1 em indents with none on the first
  paragraph, a drop cap, real small caps never beside faux ones, a letterspaced capital
  date line (own "Print typography") (said; V4 seen). Indents suit short web texts; long
  ones need space between paragraphs (said).
- **Type is core.** He stayed in Illustrator because Sketch handled type badly (talks §3;
  accounts §2) (said).
- **Rem from a percentage root** so a reader's larger default font scales the design;
  px "very rarely" (own §2) (said).

## 5. Grid and layout

- **A grid you define.** Column Setter: four ratios (outer margin, column, gutter,
  padding; e.g. 4 : 4 : 2 : 1) and named breakpoints with column counts (4 / 8 / 12)
  (talks 1.5) (said). No grid classes in the HTML, no 960 grid to "shoehorn your stuff
  into" (talks 1.5; accounts "House type scale") (said). On V6 the grid came from the
  type interval: padding 12, gutter 27, column and margin 40.5 (own "One interval
  governs") (said).
- **Layout as a few spatial parameters.** ProPublica's article framework: text in the
  centre 8 of 14 columns; a figure is a size (1–14 columns or full bleed), a position
  (left, right, centre, pushed in or pulled out up to three columns), a wrap, and
  responsive overrides; 616 presentations (work "A small set of spatial parameters")
  (said). Size and position "can be just as communicative as their content": a small
  off-centre image in wide white space tells a different story than a large establishing
  shot (said).
- **Listings for scanning, no single focal point.** Each scanned field gets a fixed place
  and style: images in a left column, headliners large and bold, a calendar-like date
  block in its own column, genre as thin stripes that double as separators, price as a
  button, venue in small caps. He accepts "no obvious focal point" because readers isolate
  the pattern they want; he rejects centred lists because each line starts somewhere new
  (work "Listings designed for scanning") (said).
- **Partitions from combinatorics.** For lists of 2 to 9+ items he drew all partitions of
  2×2, 3×2 and 4×2 grids, picked long repeating patterns so the repeat is rarely noticed,
  kept whitespace per cell roughly equal, and gave a prime count's first item full width
  (own "Make variety from combinatorics") (said). A table had been "all head and no heart"
  (said).
- **Long reading pages need places to breathe**, "where you pause and resume" (accounts
  "Long reading first") (reported, Sleight).
- **Mission first.** The Markup homepage: one sentence of purpose with inline links to the
  four pillars, then a section per pillar with a label column on the left and up to four
  stories on the right, dotted rules between (work "Mission first") (said; seen in a 2023
  capture).

## 6. Information takes whatever shape you need

His SND 2018 talk, after Eric Meyer: "Design doesn't care what you think information looks
like" (talks 1.3) (said).

- **Restyle the plain element.** A plain HTML table of his most-shared topics becomes a
  bar chart because the data is ordered by frequency; the Lost Mothers grid is "just a
  regular old bullet list" under the styles (talks 1.3; work "Bend one convention")
  (said). Keep the semantic markup; let the form follow what the data is for.
- **Show the absence.** Lost Mothers drew all ~800 slots for an estimated 700–900 deaths
  and filled only the ~134 identified, so "the vast majority of it is empty and that sort
  of the point". The aim was not to shock but to show "how little is really known"
  (talks 1.4; accounts "Let the empty space") (said). Known cases are filled, those with a
  vignette outlined in red; the grid is also the navigation and collapses to a
  chronology bar while reading (said; black page, grey dots, a band of faces, seen).
- **Enumerate every case and show all of them.** Incomplete Open Cubes Revisited keeps
  4,094 variations; Plus Equals defines one system per issue, finds every permutation,
  explains the thinking, shows every result (work "Enumerate every case") (said; seen).
  Each issue opens with its number drawn in its own system, then an essay with numbered
  figure references beside a gallery of coded pieces (e.g. PE04-A01B04C01) (seen).
- **Two voices, two image languages.** One story from two sides, each in its own visual
  language (accounts "Two voices") (reported; the idea is Sleight's, his part not
  described).

## 7. Colour

- **Black and white, then grey, then hue.** Layout in pure black and white; grayscale for
  a second layer of contrast; only then map hues onto the greys (own "Grayscale first";
  talks 1.6) (said). "Color is usually the final detail to be dealt with" (talks 1.6)
  (said).
- **Roles, not swatches.** Six roles: text, inverse, background, background alt, accent 1
  (metadata), accent 2 (links, used sparingly) (own "Grayscale first") (said).
- **One hue, fixed rotations.** All roles derive from one base hue by rotations (a triad
  at ±120°), so one variable recolours the site (own "One interval governs") (said). V7
  takes the accent hue from the date (`300 − month × 30 − day`), tints all accents from
  it in OKLCH, and gives the neutrals the complementary hue (code); the same templates
  show pink, orange and blue on different pages (seen).
- **Equal luminance across hues.** Tinnitus Tracker solved lightness to a target
  luminance so contrast stayed equal whatever the hue, and faded older years toward grey
  (own "Colour keyed to the date") (said).
- **Strong limited palettes** for clients and art: black and white for PhilaMOCA and Plus
  Equals; black with vivid figures and white type for Beyond Tellerrand (work §3) (said;
  seen). He calls colour his weakest skill; V5 used one dark grey (own "Grayscale
  first") (said; code).
- **Palettes from collected images** (painters, illustrators) or the RYB wheel (own
  "Grayscale first") (said).

## 8. Surface, imagery and motion

- **Overprint.** He named "Overprint" as V7's aesthetic basis; V6's portrait is a duotone
  photo masked by a pink and olive scribble (own "Generative texture") (said; seen).
- **Generative texture behind a strict page.** V7's background is a randomly generated
  ribbon of 120 parallel stripes on a 12-cell grid, a faint moiré behind the dark page;
  the bio is assembled from random phrases (own "Generative texture") (code; seen).
- **Line drawing.** Plus Equals: white line on black, isometric projection ("a beautiful
  lie"); Beyond Tellerrand 2024: connect-the-dots letters on graph paper (work "Title
  sequences", "Enumerate every case") (said; seen).
- **Genre costume, built natively.** Each Robtober post dresses in one period of horror
  marketing, made in CSS and SVG rather than images, and fitted to any aspect ratio
  (work "Each year, a genre costume") (said; seen). He accepts genre cliché when the
  piece "was meant to participate in a fairly specific tradition" (work "Direct the
  hand-made") (said).
- **Motion as an animator.** Keyframes counted in frames; transitions built from a rule
  (eight ways a square enters a square); film dust so it does not go stiff (work "Title
  sequences") (said). Motion sits behind `prefers-reduced-motion: no-preference` (work
  "Each year, a genre costume") (said).
- **Unadorned base, occasional experiment.** "Here's the stuff. Here's the imagery. Here
  are the colors and the shapes and the type"; he distrusts the "superficially forward
  thinking" and wants a base layer of the thing unadorned (talks 1.8; accounts "The thing
  itself") (said). "Guide your users; don't smother them" (talks 1.8) (said).

## 9. Subtraction and slowness

"I tend to keep taking pieces away until the thing breaks, and then put the last one back
in" (own §2) (said). He builds by hand with few dependencies, judging each by complexity,
comprehensibility and reliability (own §2) (said). V7 took six years with long pauses
that let ideas "percolate" (said).

## 10. Phones and the reader's terms

Responsive design let the web reconcile flexibility with line length; he likes thinking
about how a piece reads in RSS or a read-later app, "coming to people on their terms"
(talks §2; accounts "Long reading first") (said). Designers still "fetishize" big-screen
layouts while phones remain "tall stacked thin", the unsolved storytelling problem
(talks §2; accounts §2) (said). Practical evidence: Column Setter's column counts per
breakpoint (talks 1.5), ProPublica figures with phone overrides such as full width or an
alternate crop (work "A small set of spatial parameters"), Robtober 2022 re-stacking its
title by aspect ratio (work "Each year, a genre costume") (said).

## 11. Taste summary

Likes: systems you can state in a sentence; print craft; handbills, gig posters, horror
posters, VHS, zines; midcentury record covers and title sequences; conceptual art and
isometric drawing; strong limited palettes; calm, contextual reading interfaces (De
Correspondent's sidenotes); identities whose every choice comes from the client's own
world (Open's ACLU work) (own §3; work §3; talks §3). Form "looked at rather than
through"; the web needs "more lowriders" against "cookie-cutter, vibe-coded, careless
slop" (own §3) (said). Humour runs through the work and its voice: Windhammer, haiku,
self-deprecating bios (talks §3; accounts "Humour") (said; reported).

Dislikes: Bootstrap layouts and prescriptive frameworks; centred blobs of text; faux small
caps beside real caps; rules without reasons; style that "overwhelms the substance";
pixel-perfect comps as a goal; committee design where "nobody's needs are met on the
user's side"; social silos and broken links (own §3; talks §2, §3) (said).

## Cautions and gaps

- **Ban conflicts.** Some of his moves meet `../../references/bans.md` and `style.md`
  bounds them:
  - *Partition grids* (own "Make variety from combinatorics") sit close to the bento
    mosaic sibling of the card ban. `style.md` allows them only as type set in cells of
    a shared grid, with no fill, border, radius or shadow per cell; separation comes from
    rules that run the full grid, as on a printed handbill.
  - *The Plus Equals index* of white-framed square covers (work "Enumerate every case")
    is kept as a contact sheet: images only, no per-item box of title and blurb.
  - *The ransom-note title* (work "Each year, a genre costume") gives each letter a
    different source. `style.md` keeps per-letter costume only when every letter gets
    its own treatment evenly; no word may stand apart from the rest of the headline.
  - *Small-cap venue and date lines* (work "Listings designed for scanning"; own "Print
    typography") are utility text inside a listing, not stamps above section headings,
    and stay on that condition. The Markup's left label column is the section heading
    itself, set beside its stories, so it is not an eyebrow.
- **His client work and his own work diverge.** Client pages stay restrained; personal
  pages are themed and animated (work §3) (seen). In 2026 he wrote that function had
  "flattened" form and that he wants form back (own §3) (said). `style.md` keeps the
  unadorned base as the default and the costume for pieces that are themselves events.
- **Phones are thin evidence.** Beyond the items in §10, no phone layout of his was
  studied; the phone guidance in `style.md` extends Column Setter and the ProPublica
  overrides.
- **Not seen.** V5 (code only); the V7 posts on layout, colour and the generative ribbon
  he promised were not found, so the reasons for V7's dark ground are unknown (own §4).
  Title sequences were judged from one or two paused frames (work §4). The two SXSW
  talks were joint with Jason Santa Maria and do not say who said what (talks §4).
- **Attribution.** Faces credited on his ProPublica features (Acumin, FF Tisa, Miller,
  Utopia, JAF Bernina Sans) are shared credits, not proof of his choice (accounts §3).
  The two-voices art direction is Sleight's idea by Sleight's account (accounts "Two
  voices").
- **Numbers differ.** Lost Mothers' identified count is about 130, 134 or over 160
  depending on the source and date (accounts §4).
