# Scott Kellum: synthesis

The design model behind `style.md`, drawn from four research streams. Citations name the
note and its section: `own 1.3` is move 1.3 in `notes/own.md`, `own §2` its "Process and
thinking" section; `work 1.1` and `work table` refer to `notes/work.md`; `talks 1.4` to
`notes/talks.md`; `accounts` sections by heading.

Evidence marks: **(seen)** means the point was checked by eye in a browser on 2026-11-23,
on his live sites or a client's; **(CSS)** means it rests on stylesheets, markup or slide
source and was not judged by eye; **(said)** means it is his stated view, or another
person's report of it, with no visual claim.

## 1. The core idea: a website is a design space, not a set of artboards

He trained as a type designer at Darden Studio, and he designs a website the way a type
designer builds a variable family (talks §2 "Typeface design as the model"; accounts §2
"The type designer's eye") (said):

- A typeface is a design system. The designer draws a few **masters** (the lightest and
  the heaviest, the smallest and the largest optical size) and the font **interpolates**
  every instance between them. He says masters are "a lot like breakpoints" (talks §2)
  (said).
- A website has dimensions in the same way: container width, height, light and dark mode,
  the reader's preferred font size, scroll depth. A viewport is one slice through it;
  "extrude" the site to see all the slices at once. Scale "behaves more like time than
  space" (talks §2 "Websites are multidimensional objects"; accounts §2) (said).
- So the designer's job is to set the ends and the curve between them, not to draw a
  phone, a tablet and a desktop and leave the in-between to chance. Figma's fixed
  artboards mean "designers can't see what they're doing" (talks §2 "Design where you can
  see it move"; accounts §2 "Fluid canvas instead of artboards") (said).

Matthew Carter's line, that a typeface is "a beautiful group of letters, not a group of
beautiful letters", is his test for components too: "a beautiful group of components, not
a group of beautiful components" (talks §2; accounts §2) (said). A page is judged by how
its parts sit together across every size, not by any single part at any single size.

Two consequences shape the rest:

- **There is no separate phone design.** The phone is the narrow master of the same
  system, and it gets as much design attention as the wide one (talks 1.3, 1.4) (said).
- **Know the press.** He learned CSS as a print designer learns how ink moves through a
  press (talks §2 "Know the press"; own §2 "Know the medium") (said). His design ideas
  are often ideas about the medium itself: type scrubbed by width, a 14kb site, a font's
  design space made navigable (own 1.1, 1.8; work 1.7) (CSS, seen).

## 2. Typography: one rule per role, driven by its container

This is the bulk of his public thinking; the talks repeat it (talks, intro note).

- **The typographic map.** Take every instance of one role (all headlines, all product
  names), plot size against the width of its container, fit a curve, and express it as
  one rule. Every headline in every slot comes from it (talks 1.1) (said). The idea came
  from plotting a printed newspaper front page: wider headlines get bigger type (talks
  1.1; accounts "Size changes along a curve") (said).
- **What it replaces.** Vox's home page had 4 article types × 6 placements × 3
  breakpoints = 72 headline styles, "typesetting for each individual context" (talks 1.1;
  accounts "Typeset once for every context"; work table) (said). A type scale is "a
  laundry list of options" that does not say which size to use, his own Modular Scale
  included (talks 1.1) (said).
- **Curves, not straight lines.** `clamp()` and `vw` formulas scale linearly; he wants
  eased curves per property. Headlines stay modest through mid widths and grow fast late;
  body text is "as big as possible as soon as possible" and shrinks only at the very
  small end (talks 1.3; accounts "Size changes along a curve") (said).
- **Hierarchy contrast scales with the screen.** Big chunky headlines over small text on
  a wide screen; toward 1:1 on a phone, or the headline runs "one character per line".
  The ratio is what interpolates (talks 1.4) (said). Body stays near a fixed comfortable
  size with a 16px floor; the headlines do the scaling (accounts "Scale headlines; keep
  body steady") (said).
- **Line height follows line length.** Longer lines get more leading; headlines tight,
  text loose. "If your typography looks off, it's probably your line height" (talks 1.5;
  accounts "Scale headlines") (said). His slides set `max-width: 60ch`, root
  `line-height: 1.4` (talks 1.5) (CSS).
- **Every axis follows the space.** Weight, width, optical size and grade interpolate
  with size: condensed and heavy in narrow slots, wider in wide ones; a face may gain
  serifs as it grows (talks 1.6; accounts "Every axis") (said). His demos use Obviously
  for its width and weight range (talks 1.6) (said).
- **Type says what a thing is.** At SB Nation readers should know an article from a fan
  post from a feature "from the type, without a hundred labels" (talks 1.2) (said). Each
  role keeps its "thread" at every size. He wanted to keep the whole range of styles,
  not cut it down (talks 1.2) (said).
- **Proportion over measurement.** He avoids the 8pt grid ("serves the designer more than
  the reader") and baseline grids (a "fragile mess"), keeping a baseline only for
  side-by-side text columns (own §2; talks 1.7; accounts "Proportion over fixed
  measurements") (said). A modular scale is "just a ruler"; the golden ratio will not
  make type beautiful (talks §2 "Proportion as guideline") (said). Size in ems so the
  whole page rescales from the root (own §2 "Pixels are not stable") (said).
- **On his own site** every size is keyframed by container width: root 0 to 125% across
  0 to 50em, page heads 2rem to 6rem, headings 1.5rem to 3rem, lede 1.1rem to 1.5rem,
  with `text-wrap: balance` on heads and lede (own 1.1) (CSS; rescaling seen).

## 3. Choosing faces

- **Utility first, then aesthetic.** Narrow by optical-size range, width range, weight
  range, spacing, languages, axes, quality and budget; only then by character
  (professional or casual, trendy or classic) (own §2 "Choosing fonts") (said).
- **Character helps reading.** From Joshua Darden: more character in letterforms can
  improve legibility. He admires Omnes's rounded terminals and Turnip's top-weighted
  forms (talks 1.9; accounts §2) (said). His dyslexia made him read letters as "designed
  objects" (talks §2) (said). Legibility ("can I read it") and readability ("do I want
  to") are separate jobs (talks §2 "Voice and utility") (said).
- **Independent foundries, variable families.** Darden Studio, DJR, MCKL, Okay Type, OH no
  Type Co: Gamay, Roslindale, Fern, Zenith, Redaction, Harriet, Obviously, Recursive
  (own §3; work §3; talks §3) (seen, said). He works with foundries and organises fonts
  "like music" (own §2) (said).
- **Serifs lead.** Across the client table the text or brand voice is more often a serif:
  Harriet, Fern, Frances, Redaction, Libre Caslon, Roslindale, Sentient (work §3; own
  1.7) (said, seen).
- **A three-voice system.** On his site: a variable text serif (Sentient), a
  variable-width condensed display sans (Gamay), a mono (Arnold) (own 1.7) (CSS). The
  2022 version was "full monospaced" (accounts §3) (said); the 2016 one was Georgia and
  Verdana only, to fit 14kb (own 1.8) (seen, Wayback).
- **Choose a serif to outlast redesigns.** Harriet at Vox, "news-worthy" yet contemporary,
  survived a decade (work 1.10) (said).
- **Open values in licensing.** A New Social needed an OFL face (work §2) (said).

## 4. Where ideas come from

- **Branding is talk therapy.** Work out what the business is now and what it should
  become, and do not judge a logo or type choice without knowing the stakeholders'
  reasons (own §2 "Branding as conversation") (said).
- **Content before brand.** Ishmael's guides got a home first; branding came second (work
  §2) (said). At Mariana Tek every project began with customer interviews and
  whiteboard sessions to separate needs from wants (work §2) (said).
- **Take the opposite of the category.** List the colours and faces competitors use and
  take the other side: bright colours and pixel-distressed serifs for a tech publication
  that would otherwise be blue sans (work 1.5) (said).
- **One specific source.** Margret and H. A. Rey's star diagrams for A New Social; art
  deco and museum wall colours for an art-tour company (work 1.6) (said).
- **Split the jobs.** For Ishmael the mark carries expression, a rigid grid carries
  competence, colour carries optimism (work 1.3) (said; mark seen).
- **Fonts and type as material.** To launch fonts he made objects with them: a pronoun
  slider pin, packing tape reading "CONTAINS MULTITUDES" (work 1.8) (said). A specimen
  site turned the type designer's diagram of the design space into an object you move
  through (work 1.7) (said; page seen).
- **Each redesign changes the medium.** Screenprint texture (2012), a 14kb Georgia and
  Verdana site (2016), a flat teal sheet (2018), a dark variable-font site (now) (own
  1.8) (seen, Wayback). "Stop redesigning, keep designing" (own 1.8) (said, excerpt).

## 5. Composition

His grid thinking is quieter than his type thinking; the moves come from his own sites
and client work.

- **The lede is the opening.** His home page and Typetura's open on a paragraph of serif
  text at about 30 to 37px filling the first screen: no image, no headline, no button
  (own 1.2) (seen). It fits where the voice is the product.
- **Draw the grid.** Hairline rules one step off the background mark column edges and run
  past the content to the viewport edges, crossing at section joins like construction
  lines; boxes on typetura.com carry dashed inner column guides (own 1.3) (seen). Body
  grid `1fr min(50rem, 90%) 1fr` with subgrids (own 1.3) (CSS).
- **Unequal columns as ratios.** Singularity, his Sass grid system with Sam Richard, set
  columns as ratios (2:4:3, a 2:8:2 triptych) and allowed a different grid per range
  (accounts "Proportion over fixed measurements") (said).
- **A map of where you are.** For a large body of text, a persistent left rail lists
  every section grouped by phase under coloured labels, like the thickness of a book
  under the thumb (work 1.1) (said, seen on HCD Guides).
- **Loud brand, quiet reading page.** The brand colour floods the home and index; article
  pages drop to plain black on white in a characterful text face (work 1.2) (said).
- **One item per row.** Featured posts on his home page: four, one per row, each a square
  collage with two opposite corners rounded at 4rem (`border-radius: 0.1px 4rem`), its
  title beside it in a heavy condensed face sitting on a hairline, a short serif summary
  under it (own 1.5) (seen, CSS).
- **A diagonal colour split** between brown and black that shifts on scroll, giving
  motion with no moving object (own 1.4) (seen).
- **Navigation as a small floating pill** over a blurred, lightened shape that grows in on
  scroll; a vertical phrase runs up the right margin (own 1.6) (seen, CSS). On HCD Guides
  a floating bottom pill holds the two actions (work 1.1) (seen).
- **Specimen moves.** Single long words at display size run off the right edge, each
  labelled in tiny spaced capitals; sections colour-blocked in teal, black and butter
  yellow; one word set so large its descender drops into the text (work 1.7) (seen).

## 6. Colour

- **Strong single colours as fields.** Gold, yellow, deep green, brown, magenta, teal,
  each flooding a whole page or section (work §3; own 1.8) (seen).
- **Warm darks.** His site is brown and near-black with pale pink type (#ffd5ce) and a hot
  orange accent; rules are #522200 on #371506; Typetura is deep green (own 1.3, 1.5, §3)
  (seen, CSS). He prefers warm dark grounds to pure black and white (own §3) (seen).
- **Shape carries identity, colour is free.** For a mark that must live in other apps he
  drops fixed colour so light and dark modes can take opposite palettes, warm oranges in
  light, cool blues and purples in dark (work 1.4) (said).
- **Width as input to colour.** His unit-division demo turns container width into a hue;
  any animatable property can follow width, scroll or cursor (own §2 "Width as raw
  material"; accounts "Width as a general input") (said).
- **Print collapses colour** to black on white, drops the sticky nav and fixes heading
  sizes (own 1.9) (CSS).

## 7. Imagery and motion

- **Collage, overprint, glitch.** Thumbnails are saturated montages with mesh
  distortions, magenta, cyan and yellow, overprinted pattern (own 1.5, §3) (seen).
- **Period illustration over stock.** Star diagrams, deco, engraving-style trees (work
  1.6, §3) (said, seen; tree attribution uncertain).
- **Organic motion from primes.** Stack animations with prime-number durations so they
  "almost never converge" and read as random (talks 1.8 "Cicada principle") (said).
- **Honest parallax.** Real 3D perspective, so near layers pass faster than far ones;
  never scroll hijacking (talks 1.8) (said). His résumé lists CSS parallax (own sources)
  (said).
- **Responsive as zoom.** He singles out Lynn Fisher's site, which zooms a whole drawn
  scene as the window resizes (talks 1.8; accounts "Width as a general input") (said).
- **Expressive axes.** "A website about balloons ... inflating a bubble font headline from
  thin to black" (talks 1.6) (said).

## 8. Process and craft

- **Design abstractions.** Components are a design practice; an Atomic system replaced
  mockups pieced from utility classes (own §2; work §2) (said).
- **Scope where it matters.** Vox launched in nine weeks: reuse the scaffold, spend new
  effort on the explainer and the home page (work §2) (said).
- **Small and fast.** A site built to fit 14kb; "no resets, sensible defaults" (own 1.8,
  §3) (seen, said excerpt).
- **Iterate on fit.** A New Social's first warm, illustrated round stood out too much on
  other platforms; he tightened the mark (work §2) (said).
- **Metrics.** His case studies report traffic, velocity and revenue (work §3) (seen).
- **Teach the order.** His class runs: balance line length, size and leading; units and
  hierarchy; fluid sizing; font selection; variable fonts; text effects (gradient,
  outline, long shadow, SVG displacement, colour fonts); UI type (own §2) (said).

## 9. Taste summary

Likes: independent variable faces with character; serifs for voice; warm dark grounds and
single flooding colours; pale type on dark; collage and overprint; period illustration;
type specimens; visible construction; small fast pages; Stripe's growing headline, The
Atlantic, Heath Ceramics (talks §3; own §3; work §3).
Dislikes: breakpoint snapping; linear `vw` ramps; type scales that only list sizes;
oversimplified type; golden-ratio mysticism; baseline-grid perfectionism; the 8pt grid;
scroll jacking; blue and purple tech branding (talks §3; accounts §3; work 1.5).

## Cautions and gaps

- **Ban conflicts.** Some of his moves meet `../../references/bans.md`; `style.md` keeps
  them only in a safe form:
  - The tiny italic kicker above his home-page lede ("Scott Kellum — Human-centered...",
    own 1.2) is a label stamped above the opening, an eyebrow sibling. `style.md` drops
    it; the name and line go in the navigation or the foot of the lede.
  - The tiny spaced capitals beside specimen words (work 1.7) and the coloured phase
    labels in a section rail (work 1.1) are captions and navigation, not section stamps;
    `style.md` keeps them on that condition.
  - "Keep Scrolling, there's so much more!" (own 1.6) is copy with empty enthusiasm;
    `style.md` keeps the vertical margin line but asks for a plain fact in it.
  - His leaf-cornered tiles are one per row with unboxed text beside them (own 1.5);
    `style.md` keeps them as images in a ruled list and never boxes the text.
- **The talks are about type only.** The talks stream says nothing about colour, imagery,
  grid or layout (talks §4); those rest on his own sites and client case studies, where
  several live sites may since have been altered by clients (work §4).
- **Not seen.** Vox.com at launch, SB Nation and the Vox headline system (work §4); his
  2013 and 2014 sites (own §4); the Roslindale "horn" interaction was not exercised
  (work §4). The 2013 to 2015 posts were read as excerpts only (own §4).
- **Attribution.** His share of Vox's visual design is stated only by him (work §4).
- **His curves are Typetura's.** He sells the tool that does this. The style needs only
  the method (two ends and an eased curve per role); a page can carry it in plain CSS.
- **Critique on record.** Readers worried that many sizes and weights on one page look
  cluttered, and called the approach too complex (accounts "Typeset once"); denkwerk warns
  that fluid sizing must be tested with screen magnifiers (accounts §3) (said).
