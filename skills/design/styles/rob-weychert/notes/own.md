# Rob Weychert: his own sites and writing

Stream `own`. Raw copies are in `/tmp/designers/rob-weychert/raw/own/`, one file per
source, URL on the first line (`.txt` is text extracted from the `.html` beside it). All
seven versions of his site are still online on subdomains (`v1` to `v7`), so no Wayback
was needed for them. Browser check, 2026-11-23: v7 home, v7 project pages, v6 home, v4,
v3 and v2 were opened in Chrome and screenshotted; v5 was refused by the browser's site
permission and was read from HTML and CSS only.

Claim markers: **[stated]** he says it; **[observed, seen]** seen in the browser;
**[observed, code]** read from HTML, CSS or JS only; **[reported]** someone else says it.

## Sources

| Source                                                             | Date       | What it gave                                                                |
|--------------------------------------------------------------------|------------|-----------------------------------------------------------------------------|
| v7.robweychert.com (home, about, projects), main.css, main.js      | 2025–2026  | Current site: Degular, OKLCH tokens, date-based hue, generative ribbon      |
| /blog/2026/01/v7-typographic-scales-and-technical-pens/            | 2026-01-04 | "Technical pen" type: weight inverse to size, borders and icons at 1/16 em  |
| /blog/2025/09/v7-launch-day/                                       | 2025-09-09 | V7 as "collector's edition box set"; browsing pathways; six years of pauses |
| /blog/2020/01/v7-introduction/                                     | 2020-01-01 | Redesign in public from bare HTML; "Overprint" named as the aesthetic       |
| /blog/2020/03/v7-timeline-taking-shape/                            | 2020-03-03 | Small/large post binary; sketches, wireframes, prototype before style       |
| /blog/2020/06/v7-on-dependency/                                    | 2020-06-24 | Complexity, comprehensibility, reliability; hand-made over frameworks       |
| /blog/2022/11/v7-renewed-purpose/                                  | 2022-11-25 | Leaving Twitter; RSS "Following" page                                       |
| /blog/2017/09/v6-the-archive/                                      | 2017-09-11 | V6 rationale: own your archive, per-post custom layouts                     |
| /blog/2017/11/v6-typography-proportions/                           | 2017-11-28 | 1.5 scale; "left brain, right brain" pairing; grid from the type scale      |
| /blog/2018/02/v6-color/                                            | 2018-02-27 | Black-and-white, then grayscale, then hue; six-role palette; random schemes |
| /blog/2019/12/a-modern-typographic-scale/                          | 2019-12    | Scale as music: named steps --scale0, --scale-1; calc() interval            |
| /blog/2019/03/css-grid-sophisticated-partitioning/                 | 2019-03-10 | Tinnitus Tracker: Troc handbill grid, divisor classes, variable-width type  |
| /blog/2019/12/dynamic-color-javascript-hsl/                        | 2019-12    | Date-based colour: month hues as keyframes, luminance matching, age fade    |
| /blog/2018/03/design-doesnt-care/ (SND talk text)                  | 2018-03-25 | "Information can take whatever shape you need"; bifurcated story layout     |
| /blog/2007/03/bridging-type-divide/ (book chapter)                 | 2007-03-19 | Georgia, 66-char elastic measure, indents, drop cap, small caps             |
| /blog/2012/10/inefficiency-by-design/ (Pastry Box)                 | 2012-10-19 | Laborious hand-edited site makes each post feel consequential               |
| /blog/2012/11/obstruction-by-design/ (Pastry Box)                  | 2012-11-22 | Should design ever get in the way? Quay Brothers' anamorphosis              |
| /blog/2012/12/loss-of-matter/ (Pastry Box)                         | 2012-12-24 | Physicality, volume, touch lost to glass                                    |
| /blog/2014/02/beyond-pixels/ (net magazine)                        | 2014-02-25 | "Spontaneous within the systematic"; invisible work vs Windhammer           |
| /blog/2026/06/moving-on/                                           | 2026-06-03 | Form was the goal, function the compromise; "looked at rather than through" |
| /blog/2025/10/lowriders-and-websites/, /2026/06/ethan-marcotte-…   | 2025–2026  | Praise for craft and for considered-but-not-overworked sites                |
| /blog/2026/05/typography-analogical-force-geometric-love/          | 2026-05-04 | Admires lettering "unburdened by legibility"                                |
| /blog/2005/07/immortal-gutenberg/, /new-renaissance/, /halcyon-…   | 2005       | Early Pixelworthy essays: print's life, generalists, standards              |
| /blog/2006/12/typography-commandments/, /2011/10/moving-the-edges/ | 2006, 2011 | Short reviews: rules need reasons; a logo as frames from an animation       |
| v6.robweychert.com (home, CSS)                                     | 2017–2025  | Freight Text + Ciutadella; overprint portrait; tinted project tiles         |
| v5.robweychert.com/writing/ (HTML, CSS)                            | 2011–2014  | Museo Slab and Minion; one dark gray; sortable table of writing             |
| v4.robweychert.com                                                 | 2005–2008  | Blackletter masthead, Victorian ornament, red small-cap dates               |
| v3.robweychert.com                                                 | 2005       | Holding page: a hand-drawn comic about scrapping 24 designs                 |
| v2.robweychert.com                                                 | 2002–2003  | Blackletter, angled photo collage, stars, saturated red/yellow              |

## 1. Moves

### Weight runs inverse to size, so every stroke is one pen

He wants all the type on V7 to look drawn with one of two technical pens, a thin one and
a thick one, after the Rapidograph pens he used in college **[stated]**
(/v7-typographic-scales-and-technical-pens/). Larger sizes get lighter weights and
smaller sizes heavier ones, using the same interval as the size scale but divided instead
of multiplied: size = base × interval^step, weight = base weight ÷ interval^step. On a
24 px base with a 1⅓ interval, 42.7 px type is set at weight 225 and 18 px captions at
533 **[stated]**. The live home page confirms it: the 39 px intro sits at weight 225, the
70 px name at 700 as the bold pen, small headings at 533 **[observed, code]**. He then
extends the pen to everything linear: border width is 1/16 rem because Degular's stem
measures about 1/16 of its size, and the 32 icons are drawn stroke-only on a 16 grid,
with stroke width scaled the same inverse way **[stated]**. The result looks calm:
headline, body and hairline rules feel cut from one material **[observed, seen]**.

- Default replaced: Regular for text, Bold for headings, and borders picked by eye.
- Why: a busy, text-heavy site needs fewer variables; limiting stroke widths extends the
  idea of a limited type scale **[stated]**. He chose Degular because it is low-contrast
  but less sterile than a geometric sans, with "selective contrast" only in the
  lowercase joints **[stated]**. Jason Santa Maria suggested it **[stated]**.
- When it fits: a variable font with a weight axis; a site whose personality should come
  from evenness rather than display contrast.

### One interval governs type, columns and colour

On V6 he chose an interval of 1.5 (for the site's 15th anniversary) and used it for the
four type sizes and for the grid: padding 12, gutter 27, column 40.5, margin 40.5, so
the layout and the type "speak the same language" **[stated]**
(/v6-typography-proportions/). He names scale steps relative to body text,
`--scale0`, `--scale-1`, `--scale1`, so he always knows how many steps he is from the
body **[stated]** (/a-modern-typographic-scale/). He compares a scale to a musical key:
a song in a minor scale sounds sad, and he once found he had written a song in B-flat
major without knowing it **[stated]**. Colour on V6 follows the same thinking: all six
roles derive from one base hue by fixed rotations (a triad at ±120°), so turning one
variable re-colours the site **[stated]** (/v6-color/).

- Default replaced: ad-hoc sizes and a 12-column framework unrelated to the type.
- He breaks the system when the eye says so: he bumped the smallest size from 12 to
  13.5 px because "it looks better", and says the system is the foundation but "doesn't
  have the final say" **[stated]**.
- When it fits: any multi-page site; especially editorial ones with many text roles.

### Reduce text roles to a short inventory before choosing type

Before picking faces for V6 he listed every kind of text on the site by how often it
appears (body, metadata, captions, mid headings, labels, top headings, low headings) and
found almost everything could use two sizes, with two more for rare emphasis
**[stated]**. He then paired faces by what the text does: "left brain" structural text
(metadata, labels, headings) in Ciutadella, a slightly condensed geometric sans, and
"right brain" text in his own voice in Freight Text, a transitional serif with ball
terminals **[stated]**; the V6 CSS confirms those two families **[observed, code]**.
Freight is reserved "exclusively for when I'm speaking directly to the reader"
**[stated]**. V6 sets nav in Ciutadella capitals and the intro in large Freight
**[observed, seen]**.

- Default replaced: one sans everywhere, or serif headings over sans body for contrast's
  sake.
- When it fits: any site where navigation and authored prose sit side by side.

### Grayscale first, then hue

His colour process starts with the layout in pure black and white (size, shape,
position), then grayscale for a second layer of contrast, and only then maps hues onto
the grays **[stated]** (/v6-color/). The grays become named roles: text, inverse,
background, background alt, accent 1 (metadata), accent 2 (links, used sparingly)
**[stated]**. He calls colour his weakest skill and says V5 avoided it entirely
**[stated]**; the V5 stylesheet indeed uses almost only one dark gray, `#303639`
**[observed, code]**. Palettes come from images he collects (Colossal, painters,
illustrators) or from the RYB wheel **[stated]**.

- When it fits: whenever colour must survive arbitrary hue changes; it guarantees the
  hierarchy works before hue is added.

### Colour keyed to the date

Tinnitus Tracker (his concert diary, 2019) gave every day of 30 years its own colour:
twelve month hues placed round the wheel like animation keyframes (cool in winter, warm
in summer), days interpolated between them, accent at +120°, lightness solved to a
target luminance so contrast stays equal across hues, and older years faded with
`grayscale()` up to 0.9 **[stated]** (/dynamic-color-javascript-hsl/). He wanted the
browsing to feel like a wall of screen-printed gig posters, and credits Shaun Inman's
2006 date-based colour **[stated]**. V7 keeps a simpler version: `--accentHue` is
`300 − month × 30 − day`, taken from the post's own date or today, and all accents are
OKLCH tints of it with a complementary base hue (+180°) for the neutrals
**[observed, code]**. In the browser, the same templates show a pink accent on the home
page, orange on the 2022 Beyond Tellerrand page and blue on another project page
**[observed, seen]**.

- Default replaced: one brand accent everywhere.
- When it fits: archives, diaries, event listings, anything with a date per page.

### Make variety from combinatorics, not from randomness

For Tinnitus Tracker's show lists he drew all 149 ways he could find to partition 2×2,
3×2 and 4×2 grids, then picked repeating patterns for list lengths divisible by two to
nine **[stated]** (/css-grid-sophisticated-partitioning/). Rules: keep whitespace in
each cell roughly equal (narrow cells next to wide ones span two rows); a pattern looks
random when it repeats rarely, so use long patterns; treat a prime count as one less and
give the first cell full width **[stated]**. Headliners are set in Nick Sherman's
variable Curvature, with the width axis matched to the cell width, tested against the
longest name, "DISMEMBERMENT" **[stated]**. The source is the Trocadero's photocopied
monthly handbills, "dense and a little chaotic", which he got as a teenager **[stated]**.
He says this cannot be designed in the browser; it has to be planned on paper first
**[stated]**.

- Default replaced: a uniform card grid, or a table, which he tried first and found
  "all head and no heart" **[stated]**.

### Generative texture behind a strict page

V7's background is a randomly generated ribbon of 120 parallel stripes curving down a
12-cell grid, tiled vertically, drawn in a pattern fill each load **[observed, code]**;
on screen it reads as a faint moiré swoosh behind the dark page **[observed, seen]**.
V6 did the same job with a portrait in which a pink and olive scribble masks a duotone
photo **[observed, seen]**; he named "Overprint" as V7's aesthetic basis at the start
**[stated]** (/v7-introduction/). The short bio on V7 is also assembled from random
phrase options **[observed, code]**.

### Archive structure as the design problem

He frames V6 and V7 as archives: everything he has posted on any service comes home to
his domain, each item keeps a link to its original context, and old versions stay live
on subdomains so links never break **[stated]** (/v6-the-archive/, /v7-launch-day/).
V7's blog is "a collector's edition box set" (a friend's phrase) with many browsing
paths: highlights, media, creators, locations, film, music, concert and reading
diaries, topics, dates, series **[stated]**. He designed the timeline as a binary: a
small post (under 100 words, up to four images) shows whole; a large one is truncated
**[stated]** (/v7-timeline-taking-shape/). V6 let any single post swap in its own
layout file **[stated]**, which is what made the yearly custom Robtober posts possible
(see `work`).

### Print typography, translated rather than copied (2007)

In a 2007 book chapter he built a page for Poe in Georgia alone: a 66-character measure
held by an elastic em-based layout; paragraph indents of 2.1 em, which carve a square,
and no indent on the first paragraph; a six-line drop cap later replaced by a drawn
Bodoni-like versal; an all-caps date line letterspaced 0.13 em in Times New Roman
because Georgia has only text figures; a first line in small caps, lowercased so faux
small caps never sit next to real capitals **[stated]** (/bridging-type-divide/). He
adds that indents suit short web texts best, since long ones need blank lines for rest
**[stated]**. V4 (2005–2008) shows these habits: red small-cap dates hanging in a
left column, small-cap section labels, a blackletter masthead framed by Victorian
ornament **[observed, seen]**.

## 2. Process and thinking

- **Structure and content before style.** V7 started as bare HTML published in public,
  with content priorities, inventories, sketches, Sketch wireframes and a working filter
  prototype before any visual design **[stated]** (/v7-introduction/,
  /v7-timeline-taking-shape/). V6 type began with an inventory of 15 years of real posts
  **[stated]**. "The content is the arbiter of the layout" **[stated]**.
- **Subtract until it breaks.** "I tend to keep taking pieces away until the thing
  breaks, and then put the last one back in" **[stated]** (about page). He links this to
  years in a tiny Brooklyn apartment **[stated]**.
- **Systems with room for the hand.** He makes "space for the spontaneous within the
  systematic" **[stated]** (/beyond-pixels/), and says sometimes "you just have to
  eyeball it" **[stated]** (/v6-typography-proportions/).
- **Slow, with gaps.** V7 took nearly six years; stepping away for months let ideas
  "percolate" and made the vision both bigger and more refined **[stated]**
  (/v7-launch-day/).
- **Hand-made, few dependencies.** He judges a dependency on complexity (who pays for
  it), comprehensibility (does he understand it) and reliability (will it last); he
  rejects React and Bootstrap, CDNs and hosted font services for his own site, and
  starts from a boilerplate HTML file **[stated]** (/v7-on-dependency/). He found a
  laborious hand-edited site made each post "more consequential" **[stated]**
  (/inefficiency-by-design/).
- **Respect the reader's settings.** Sizes in rem from a percentage root so a user's
  larger default font scales the whole design; he "very rarely" uses px **[stated]**.
  Motion sits behind `prefers-reduced-motion` **[stated]** (see `work`).
- **Writes up the making.** Nearly every project gets a long how-it-was-made post with
  the formulas and code **[observed, seen]**.

## 3. Taste

- **Function flattened form, and he wants form back.** In 2026 he wrote that he entered
  graphic design to make visual things; over time function "flattened" form, and his
  old talk title "From Self-Centered to User-Centered" now seems a false dichotomy
  **[stated]** (/moving-on/). He wants work "looked at rather than through" **[stated]**.
  In 2014 he contrasted his invisible day job with his air-guitar persona, Windhammer,
  who is "designed to be noticed" **[stated]** (/beyond-pixels/).
- **Design may obstruct.** He asked in 2012 whether design should sometimes make the
  reader work, citing the Quay Brothers' film on anamorphosis **[stated]**
  (/obstruction-by-design/). He praises lettering "almost entirely unburdened by
  legibility" on Analogical Force sleeves **[stated]**.
- **Physical matter.** He misses touch, weight and volume in a life of glass screens
  **[stated]** (/loss-of-matter/); he praised a magazine printed as a wall poster
  **[stated]** (/immortal-gutenberg/).
- **Craft over "functional absolutism".** He agrees that the web needs "more lowriders"
  against "KPI-obsessed, cookie-cutter, vibe-coded, careless slop" **[stated]**
  (/lowriders-and-websites/). He praises Ethan Marcotte's site for being "thoughtfully
  considered without being overworked" **[stated]**.
- **Influences he names:** Sol LeWitt, Reid Miles, Saul Bass, M.C. Escher, Chris Ware,
  Lego instructions, technical drawing, gig handbills, horror posters, VHS, post-punk,
  zines, music theory, Bringhurst, Eric Meyer **[stated]** (across own and work posts).
- **Dislikes:** over-engineered web stacks, centred blobs of text, faux small caps
  next to real caps, rules given without reasons, social silos, broken links
  **[stated]**.
- **Range across versions.** V2 (2002) is loud: blackletter wordmark, a tilted photo
  collage, stars, saturated red and yellow **[observed, seen]**. V4 is ornate print
  pastiche; V5 near-monochrome slab serif; V6 warm serif with overprint art; V7 dark,
  one sans, generative texture **[observed, seen; V5 from code]**. He calls the early
  work "manic self-expression" and later work "straightforward clarity" **[stated]**.

## 4. Open questions

- The V7 typography, layout, colour and generative-pattern posts he promised in the
  launch post were not found beyond the technical-pen post; the reasoning behind
  Degular Mono, the dark background and the ribbon is unverified.
- V5 was not seen in the browser (site permission refused); its look is inferred from
  CSS.
- Only about 35 of roughly 900 posts tagged "design" were read; most of the rest are
  imported tweets and link posts.
- Whether the V7 accent is fully date-driven on every page type (the home page uses
  today's date) was read from code, not tested across dates.
