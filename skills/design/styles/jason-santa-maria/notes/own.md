# Jason Santa Maria: his own sites and writing (stream `own`)

Evidence labels: **[stated]** he says it; **[observed]** seen in the work (markup, CSS,
image files); **[reported]** someone else says it. No browser was available: visual
judgements rest on CSS values, markup, alt text, and the image assets themselves (titles,
backgrounds, mastheads), which were downloaded and viewed one by one. Where a judgement
needs the rendered page, the note says so.

Browser check, 2026-11-23: about 20 v4 and v5 posts, the v5 home page and the current home
page were opened in Chrome (v4 and v5 are still live at their subdomains) at a 1014px
CSS viewport. Claims confirmed by eye carry "seen 2026-11-23"; corrections say so; new
points are marked "observed (seen)".

Raw files: `/tmp/jsm/raw/own/` (URL on line 1 of each). Working extracts:
`/tmp/jsm/work/`.

## Sources

| Source                                                                     | Date      | What it gave                                                    |
|----------------------------------------------------------------------------|-----------|-----------------------------------------------------------------|
| https://jasonsantamaria.com/ and `/assets/css/styles.css`                  | 2026      | Current site: fixed frame, Roslindale/HEX Franklin/VCTR Mono    |
| https://v1.jasonsantamaria.com/                                            | 2000–2002 | "Design for Hire" Flash-era portfolio; sliced-image layout      |
| https://v2.jasonsantamaria.com/                                            | 2003–2004 | Early blog, image headers; little design signal                 |
| https://v3.jasonsantamaria.com/ + `css/screen.css`, masthead, spine images | 2004–2008 | Whole site dressed as a pulp paperback                          |
| https://v4.jasonsantamaria.com/ + `css/master.css`, `i/grid-bg.png`        | 2008–2011 | The art-direction system: base frame and 8-column grid          |
| v4 articles index and 29 monthly archives                                  | 2008–2011 | Full list of 63 posts                                           |
| All 63 v4 posts, 44 per-post stylesheets `css/entry/<slug>.css`            | 2008–2011 | Per-post fonts, colours, column widths, image use, design tags  |
| v4 per-post assets: royal-bg, sketch-page, five title images, teasers      | 2008–2011 | Type set as image, full-bleed photo backgrounds                 |
| v4 "A New Day" (+120 comments)                                             | 2008-06   | His launch rationale for per-post art direction                 |
| v4 "Variation Within Constraints"                                          | 2008-07   | His definition of art direction; experiment over robustness     |
| v4 "A Real Web Design Application"                                         | 2010-07   | His process (sketch, grey boxes, comps) and tool wishlist       |
| v4 "The Death Throes of Print", "Explain Yourself", "My First Website"     | 2008–2009 | Print vs web; graphic designer identity; preserving old designs |
| v4 "If You Were a Typeface", "Change of Heart", "On Good", "Pretty Sketchy"| 2008–2010 | Type taste (Trade Gothic, Tschichold), Rand quote, sketchbooks  |
| v5 site, 47 posts, `screen.css`, 4 per-post styles (details below table)   | 2011–2022 | Fixed frame, four art-directed posts, 14 essays                 |
| *On Web Typography* (free download, CC BY-NC-ND 4.0, from his home page)   | 2014      | Full book read; his type method and numbers                     |
| https://alistapart.com/article/how-we-read/                                | 2014      | Chapter 1 of the book as published on A List Apart              |
| https://slate.com/briefing/2018/01/jason-santa-maria-on-how-slate-...      | 2018-01   | His write-up of the Slate "Redux" redesign                      |

The book was downloaded from his own site, where he offers it "Download for free"; the
zip's LICENSE.txt is CC BY-NC-ND 4.0. Book findings in full:
`/tmp/jsm/work/owt-findings.md`.

v5 (https://v5.jasonsantamaria.com/, 2011–2022) was fetched by a sub-agent:
`c/screen.css`,
five Typekit kit files (as data), and 47 of 90 article pages. Art-directed posts:
`scenes-from-brimfield` (2011-09-16, photo essay), and three Candygram guest essays —
`chunky-in-fury` (Mike Monteiro, 2011-10-07), `monkey-nuts-barmbrack-and-apples`
(Jeremy Keith, 2011-10-21), `chocolate-is-for-girls` (Jessica Hische, 2011-10-28). His
essays read in full: `five-and-ten` (v5 launch, 2011-08), `baseline-grids-on-the-web`
(2012-10), `the-space-between-the-notes` (2013-06), `discourse-in-web-design`,
`take-a-breath` (2014-01/02), `whats-next`, `i-wrote-a-book`, `interludes-in-design`,
`size-specific-adjustments-to-type-designs`, `drafting`, `ode-to-a-table`,
`correspondence-with-an-ex-designer`, `piles-of-ideas` (2014), `saved` (2015-02).
Full per-post table and frame values: `/tmp/jsm/work/v5-findings.md`.

## 1. Moves

### M1. Design the system, then art-direct the piece

What: build a fixed brand frame (masthead, navigation, utility text, footer, base grid,
base type) and a set of per-piece "hooks"; then give each post whatever its content
calls for inside that frame.

Where: v4 launch post "A New Day" (2008-06-17) [stated]: he had grown disillusioned
because sites drop content into a template, "reducing the design to more a bit player";
so "instead of designing one look for a site, I designed a system". He names the fixed
parts — an eight-column grid, a few typefaces, masthead and utility information — and
the variable ones: typefaces, colours, images, background, columns and layout. The model
is the magazine: one system, each story with its own look. He cites A List Apart issues
(per-issue colour and illustration) and A Brief Message as precedents. [stated]

Mechanism [observed]: every v4 post page links one extra stylesheet,
`css/entry/<slug>.css`, loaded after `master.css`. Of 63 posts, 44 have one; 19 use the
default design (tag "Default"). The per-post sheets are 6–12 KB, mostly overrides of the
same selectors (`body`, `#logo`, `#nav-*`, `.post-head`, `#col1`, `#col2`, `.lead`,
`#content p`, `blockquote`), with a trailing block commented "Don't need to be changed"
for the comment form. So the frame is a stable set of named hooks; each post restyles the
same hooks.

Default it replaces: one template for every post, design fixed at the site level.

When it fits: a site or page set where pieces differ in tone (essay, quote, photo,
guest piece, announcement) but must read as one publication.

### M2. Not every piece gets the treatment: a plain default is part of the system

He planned a no-frills default so posting never waits on design: "I didn't want to make
a system where posts had to be art directed in order to be published", and "just because
I can make these look any way I want, doesn't mean they all have to be crazy" (comment
on "A New Day"). [stated] In v4, link posts, announcements, interviews and housekeeping
(e.g. "Listening Between the Leading", "Leaving Happy Cog", "Introducing Typedia") stay
on the default; personal essays, quotes, guest pieces and photo posts get bespoke
designs. [observed] He calls art direction "more times than not, … a practice of
restraint" ("Variation Within Constraints", 2008-07). [stated]

Default it replaces: either a uniform template, or (the AI failure) maximal styling on
everything.

### M3. Tag the design, not only the topic

Each v4 post carries "Design Tags" next to its topic categories: colours, typefaces and
treatment, e.g. "Photo, Titling Gothic, White, Yellow" (Responsive Web Design), "Beige,
Black, Hand-drawn Type, Illustration" (Pretty Sketchy), "American Typewriter, Black,
Grey, Red" (Deadlines). [observed] He says the point was to let readers sort by "design
attributes like color, layout, typefaces". [stated, "A New Day"] For an agent this is a
usable discipline: name each piece's palette, faces and treatment explicitly as a short
spec before designing it. The tag vocabulary shows his per-post palette is usually one
typeface plus two to four colours. [observed, from tag counts]

### M4. The fixed frame is re-tinted, never removed

The masthead logo, logo "bug", and navigation stay in place on every v4 post, but each
post supplies recoloured versions: image files named by colour, such as
`logo-type-985214.png`, `logo-bug-617375.png`, `nav-985214-617375.png` ("On Good"),
`logo-type-666.png` ("Royal", "Deadlines"), `logo-bug-fcf2ce.png` ("To Sweet
Hereafter"). The black utility band (`#sub-outer { background: #000 }`) stays black
across posts. [observed] So identity survives even when the page is flooded orange or
yellow: position and shape are constant, colour follows the post.

The one exception proves the rule: "Pretty Sketchy" (a post about keeping a sketchbook)
replaces logo and nav with hand-drawn versions (`logo-type-sketchy.png`,
`nav-sketchy.png`, `sketch-comment.png`) on a cream paper texture. [observed] Even
there the frame keeps its place; only its rendering changes. [seen 2026-11-23: logo and
nav are hand-lettered caps on pale yellow paper; the meta strip (date, comments, category)
stays in the normal set type.]

Small UI glyphs follow too: the comment icon becomes a skull (`comment-skull-bk.png`)
on the Poe post "Haunted". [observed]

Default it replaces: a header that either never changes or disappears in a "special"
layout.

### M5. Pick the typeface from the subject

Per-post faces in v4 track the content's era or object [observed, from design tags and
CSS]:

| Post                             | Subject                               | Face(s)                          |
|----------------------------------|---------------------------------------|----------------------------------|
| Deadlines                        | Douglas Adams quote on deadlines      | American Typewriter, 51px quote  |
| Haunted                          | Poe's "The Conqueror Worm"            | Franklin Caslon                  |
| Mathematics of the Tootsie Pop   | retro candy (Liz Danzico, guest)      | Cooper Black + Adobe Caslon      |
| If You Were a Typeface           | "I am Trade Gothic"                   | Trade Gothic                     |
| All Things Nice (Mandy Brown)    | candy cigarettes                      | Bodoni-style title, red/blue     |
| Pretty Sketchy                   | sketchbooks                           | hand-drawn title, cream paper    |
| Cheesesteak Crawl                | Philly food walk                      | Gotham, yellow, illustration     |
| Jackpot (John Gruber)            | Halloween house                       | FF Quadraat + Spookhouse, purple |
| On Good                          | Rand/Mies "be good, not original"     | Proxima Nova, 80px caps          |
| Simple                           | Rand quote on simplicity              | Gotham italic, teal              |
| Solutions                        | Bertrand Russell quote                | Auto italic, dark greens         |

All rows seen 2026-11-23; the face identifications match by eye (Cooper Black title,
American Typewriter quote, condensed fat-face Didone for "All Things Nice", Trade Gothic
Bold Condensed caps, italic Franklin Caslon verse, Proxima Nova caps). The last two rows
are observed (seen), from the posts and their design tags.

Further detail, seen 2026-11-23 [observed (seen)]: "All Things Nice" puts a huge red disc
behind the black title, overlapping the masthead bar, with one wide text column and a big
black drop cap below. "If You Were a Typeface" is otherwise a default post until "I AM
TRADE GOTHIC" in bold condensed caps breaks out wider than the text column, followed by a
bio of the face between heavy black rules with a portrait of its designer, like a
specimen-book entry. "Cheesesteak Crawl" pairs a white text panel (big brown Gotham lead)
with a line-drawn diagram of a cheesesteak's parts (roll, cheeses, steak) on the yellow
ground.

In the book he states the method behind this: appropriateness through origin (a face's
time, place and purpose carry meaning), word association to find faces, and avoiding
"ready-made" novelty fonts whose design is baked in. [stated, *On Web Typography* ch4]
Note the line he draws: Cooper Black for 1970s candy or American Typewriter for a writer's
quote are period faces, not novelty fonts; the typesetting does the work. [inferred
from the two sources together]

Default it replaces: one sans for everything, or a "themed" novelty font.

### M6. Type as image when the face cannot be served

In 2008–2010 most of these faces were not available as web fonts, so post titles were
drawn as images and hidden-text replaced: `title.png`/`title.gif` with
`text-indent: -9999px` appears in about 30 of the 44 sheets. [observed] Viewed directly:
"ALL THINGS NICE" in a condensed fat-face Didone; "PRETTY SKETCHY" in hand-drawn
outlined capitals; "Cheesesteak Crawl" in Gotham. [observed; seen 2026-11-23] In "Pretty
Sketchy" the whole body text is hand-lettered too, with a shaded block drop cap and a
hand-drawn star beside the pull quote; the HTML text is hidden. [observed (seen)] Other
title images, seen: "Sugar Smack" in heavy italic condensed caps with a red Life Saver
photo hanging on a string between the two words; "Pixy Stix" and "All For Me" in
casual script faces matched to the candy. [observed (seen)] Drop caps were also images
(`drop-s.gif`, `drop-o.gif`, `drop-t.png`...). He fought sIFR for Trade Gothic and gave
up, using system fonts "to approximate" ("A New Day"). [stated] Once Typekit arrived
(v4 loads a Typekit kit), later v4 sheets call web fonts directly: `chaparral-pro`,
`skolar`, `proxima-nova`, `ff-speak-web`, `p22-franklin-caslon`. [observed] The lesson
for today is the book's: treat big headline type "in the same way you might a
photograph", hand-tuned. [stated, ch4–5]

### M7. Flood the page with one colour for a short piece

Quote posts become posters: the whole `body` takes one saturated colour and the quote is
set enormous. "On Good": body `#e37b1e` orange, text `#65360d` brown, accent `#c3e7ec`
pale blue, quote in Proxima Nova 80px/78px uppercase. "The Candy Parenthesis": body
`#fee101` yellow, a centred 82px Chaparral lead in white, three 287px columns. "Simple":
teals `#4a6a67`–`#85bdb7`, 80px quote. "Solutions": dark greens `#02120c`–`#9bbe6e`.
[observed] Palettes are tonal: one hue in four to six steps plus one contrast accent,
not a rainbow. [observed, colour lists per sheet in `/tmp/jsm/work/v4-compact.txt`]
Text colour is a dark shade of the background hue (brown on orange, `#725900` links on
yellow), not black. [observed]

Seen 2026-11-23: "On Good", "Simple" and "Solutions" share one composition: huge hanging
quotation marks in a darker or brighter step of the hue, the quote at about three
quarters of the page width, a short attribution line, then the meta strip; only face,
case and palette change. "On Good" sets its pale-blue caps over a brown offset shadow,
and the comment area below takes the same flood colour. [observed (seen)] "The Candy
Parenthesis" is not a quote poster but a guest essay: two giant black parentheses frame
the byline across the full width, so the title is acted out, then the white italic lead
and three columns follow. [observed (seen)]

Default it replaces: white page, black text, one brand accent.

When it fits: a short text (quote, announcement, epigraph) that should be read as one
image.

### M8. The photograph is the page, and the text is in the photograph

"Royal" (2009-07), on his blood-orange Royal typewriter: the body background is a
1600×1408 photo of the typewriter on a grey wall, and the paper in the typewriter carries
the post's own text, typed on that machine. [observed, image viewed; seen 2026-11-23]
Correction (seen 2026-11-23): there is no readable HTML column beside the machine. The
post's paragraphs are hidden with `text-indent: -9999px`, so the reader reads the whole
post on the typed sheet in the photo; the red typewriter sits on an olive U.S. Army
crate, and the page scrolls through one long photo before the black comment area. The
earlier reading of a `margin-left: 505px` column beside the machine was wrong. In the
comments he apologises for "the small type" — he accepted a cost for the idea. [stated]
"Oh Snap" (Polaroid SX-70): the camera photo sits large at lower left, a red display S
drop cap opens a narrow text column at right. [seen 2026-11-23] "The Death Throes of
Print" sets a cut-out photo of a newspaper stack at top left with the 36/44 Georgia lead
under it, book-style paragraph indents, and a narrow right column of short subheaded
notes ("Momentum", "Potential") running beside the photo. [observed; seen 2026-11-23]

Other photo-led posts, seen 2026-11-23: "Haunted" sets Poe's stanza in white italic
Franklin Caslon, alternate lines indented as verse, over a full-bleed rust-tinted night
photo of chimneys and a moon with a ragged dark vignette. "Jackpot" crops a vintage
plastic vampire mask photo off the left edge of the page, beside a lime-yellow lead on
deep purple. "All For Me" floats two crossed chocolate bars on a peach ground that
matches the page, so the photo has no visible edge. [observed (seen)]

Default it replaces: a hero image above the text, cropped to a 16:9 band.

### M9. An asymmetric reading column on a visible grid

v4 base [observed, `master.css`, `grid-bg.png`]: 910px page, 8 columns of 100px with
10px gutters (the diagnostic grid image is 910×20, so it also marks a 20px vertical
unit). Body text Georgia 14px/20px. The default text column is not centred: paragraphs
sit at `margin: 0 120px 20px 230px`, a 520px measure pushed right, leaving a wide left
margin for meta and hanging elements. UI text is Lucida Grande 12px; labels are Trebuchet
uppercase, 2px letter-spacing; some headings Proxima Nova Extra Condensed. Per-post
sheets then move the column: 540+320 two-column splits, 430+420, three 287px columns,
or a 120px inset both sides for quotes. [observed]

Default it replaces: one centred column of the same width on every page.

### M10. The whole site as a printed object (v3)

v3 (2004–2008) dressed the site as a pulp paperback [observed, images viewed]: the
masthead is a worn orange book cover strip reading "JASON SANTA MARIA … COMPLETE AND
UNABRIDGED" with a "40¢" price roundel; a black-and-yellow book spine runs down the left
edge ("ACTION SCIENCE ADVENTURE", "JSM03", "Volume three in a series of inconsequential
observations and humorous asides"); cream page `#fffddf`, a coffee-stain background
image, Georgia text, Baskerville italic accents, image drop caps. The version number
lives in the metaphor (JSM03 = v3). This is the idea from print taken literally: borrow
a specific printed artifact, with its wear, price and series copy, not a generic
"paper texture". [inferred]

### M11. Restraint in the current frame: a mounted print

The current site [observed, `styles.css`]: the white page sits inside a light warm-grey
border (`--deco-02 #f2f2ef`, 2rem wide) like a print in a mat; a 4-column CSS grid at
max 57.5rem; the root font size jumps to 150% above 70em so the whole design scales up
on large screens rather than spreading wider. Roslindale (a variable serif, optical size
set) for text, HEX Franklin for headings, VCTR Mono for meta. Palette is only warm greys
(`#f9f9f8` to `#9b938a`) and #333 text; links #333 with a thick (0.15rem) pale-grey
underline offset 3px. The footer names the typefaces with links to their foundries — a
colophon. [observed] "The Candy Parenthesis" in v4 also ends with a two-part colophon
in 11px Lucida. [observed]

Seen 2026-11-23 in a browser set to dark mode: the site has a full dark scheme
(`prefers-color-scheme: dark`), near-black page in a dark-grey mat, white headings, the
same layout. The home page has a "My Book" block with the red *On Web Typography* cover
(black numbered circle, condensed caps title) and a "Download for free" link, confirming
the free download. [observed (seen)]

### M12. Preserve each design with its content

He archives each version at its own subdomain (v1 to v5) instead of migrating old posts
into the new design: "the design the content was written for" ("A New Day"); "When we
change that, we break the context" ("My First Website"). [stated] For art direction
this matters: a piece and its design are one work, so a redesign is not a reason to
restyle old pieces. [stated]

### M13. v5: a strong fixed frame, art direction as the exception

v5 kept "exploring design on a per-article basis" [stated, "Five and Ten"] but in
practice only four of 90 posts got custom CSS and a per-post font kit, all within two
months of launch; later features use one default template. [observed] His reason for
loosening: custom design had made him feel a post "couldn't be short" — "a design trap I
unknowingly set for myself". [stated] So the mature form of M1/M2 is: one stream for
every length, two headline treatments (feature vs short post), art direction only when a
piece earns it.

The v5 frame [observed, `screen.css`]: centred 916px page (his first centred layout
since v2, which he flags himself [stated]), twelve 58px columns with 20px gutters. One
reading column of eight columns (604px) inset two columns (156px) each side; quotes,
lists, h2s and normal images share the same inset, so one measure governs everything.
Chaparral body 20px/1.5 in #444; feature headlines Chaparral light 66–70px; Proxima Nova
for short-post titles and h2s; Proxima Nova Extra Condensed for nav and dates; FacitWeb
for captions and meta — four faces, each with one job. Hand-picked size steps (11 … 20,
22, 30, 36, 50, 66/70px): small steps at text sizes, jumps at display sizes; sizes
adjust once web fonts load. Book-style paragraphs (1.2em indent, no gap). One red,
#df4747, for every accent; greys otherwise; black footer band. A feature ends with his
signature image at 40% opacity. Nav marks the current section with a 5px red rule above
the word, like a tab. [observed] Seen 2026-11-23: the home page is a stream of large red
Chaparral light headlines, tiny date at left, one-sentence excerpt, hairline between
items; a short post has a red Proxima title and indented Chaparral paragraphs. On the
art-directed posts the logo square and the nav tab rule take the post's colour (green,
orange), so v5 re-tints the frame as v4 did (M4); the red is the default, not fixed.
[observed (seen)]

### M14. One display face per story, plus the house text face

Each v5 art-directed post loads one extra font kit holding a single display family:
Ambroise (antiques-market photo essay), FF Basic Gothic Black (Chunky chocolate), Adobe
Caslon (Irish Halloween memoir), League Gothic (fruity candy). The house text face
(Chaparral) mostly stays. [observed] Same principle as M5, now with real web fonts.

### M15. The title as an object; the hierarchy inverted

"Chunky in Fury": the 220px Basic Gothic Black title is set twice — a white copy with a
32px stroke under a red copy — both skewed, so it reads as a slanted, outlined wrapper
logo; the text begins 500px down. [observed; seen 2026-11-23: the title runs uphill
across the full width, red with a thick white outline, on a pale grey ground with faint
horizontal lines] "Monkey Nuts": the title shrinks to 30px italic tracked caps and the
first sentence of the story becomes the 61/75px italic display line. [observed]
Correction (seen 2026-11-23): that line is not centred on the page; it heads the left of
the two columns in grey italic Caslon, and the right column starts level with it.
Default replaced: title biggest, always.

### M16. Ornament, colour and surface taken from the text

"Monkey Nuts" uses a picture of a nail as the divider under the byline; a nail above the
kitchen door matters in the story. [observed] "Chocolate Is for Girls" links each candy
named in the text in that brand's colour (Swedish Fish #fb2e4f, Fun Dip #1c91c7 …) and
stripes the League Gothic title in two greens per letter. [observed; seen 2026-11-23]
Its lead image is a bar chart built from candy: stacks of Swedish Fish, candy corn,
Necco wafers and a column of lavender sugar standing on ruled graph paper, one short
chocolate as the lowest bar, so the data joke is made with the subject itself.
[observed (seen)] Backgrounds evoke the material: parchment #ede7da with an inset
vignette and grey-brown text for the memoir; chocolate-brown #683f1a body text for
Chunky; black for the photo essay. [observed; seen 2026-11-23: the parchment's dark
vignetted edges read like an old page]

### M17. The gutter sets the tone; the series shares a kit

Each Candygram breaks the house single column into two, but with a different split:
443+30+443 (Hische), 398+120+398 (Keith, a quiet letter-like page), 365+30+365 offset
78px (Monteiro). [observed; the reading of each is inference] What stays across the
series: a centred, tracked Proxima byline in the post's accent, a lowercase italic "by"
on a short rule, a footer pair with series note and author bio, and the end signature
switched off because a guest wrote it. [observed] Series identity lives in the byline
and footer kit; each issue varies everything else.

The series began in v4, not v5 (seen 2026-11-23): Candygram ran in October 2009 and 2010
("Mathematics of the Tootsie Pop" by Liz Danzico, "Jackpot" by John Gruber, "All Things
Nice" by Mandy Brown, "Sugar Smack" by Kristina Halvorson, "Pixy Stix" by Jeffrey
Zeldman, "All For Me" by Erin Kissane, "The Candy Parenthesis" by Robin Sloan). The v4
kit is the same idea: a centred tracked-caps byline with italic "by", and a full-width
footer band in the post's colour holding a Candygram badge, the series note and the
author's photo and bio (red for Tootsie Pop, cyan for All Things Nice). [observed (seen)]

### M18. Photo essay paced by scale alone

"Scenes from Brimfield": no prose, a light tracked caps title in Ambroise, twelve photos
on black alternating 916px full-width frames with 448+448 pairs. [observed; seen
2026-11-23 for the title and first full-width frame, a crowd of white glove moulds]

### M19. Interludes: recurring devices as a chorus

He names, in "Interludes in Design" (2014), a move for long articles: drop caps, big
photos, colour splashes that share size, colour and placement and recur "almost like the
chorus of a song" to hold a mood; his praised example trims its drop caps to echo the
story's subject. [stated] It complements M9: the long page gets rhythm from repeated
devices, not from a baseline grid.

## 2. Process and thinking

- **Experiment first, robustness second, on his own site.** Professionally he designs
  for the majority first and engagement second; on his site he reverses it ("Variation
  Within Constraints"). He let a sIFR overlap bug stand in some browsers rather than
  rework the layout. [stated] An agent should not copy this risk tolerance into client
  work; the transferable part is the order of questions on expressive pieces.
- **Art direction defined.** Bringing visual design "into the fold as an equal partner
  to the content, while maintaining a consistent overall identity" — like a newspaper
  flexing layout, imagery or type for a special feature to evoke the writing's mood.
  [stated, "Variation Within Constraints"]
- **Sketch, grey boxes, then comps.** His web process ("A Real Web Design Application",
  2010): rough sketches and grey boxes, then high-fidelity comps revised to sign-off,
  little layout decided in code, because it "helps me focus on the story I'm trying to
  tell". He wanted per-document grids ("Different designs require different grids"),
  CSS-like linked type styles ("make h2s 200% the base"), font stacks to preview
  fallbacks, fluid canvases. [stated] By 2014 the book moves type choice into throwaway
  browser "type sketches". [stated, ch4]
- **Sketchbooks are for thinking.** "Sketchbooks are not about being a good artist,
  they're about being a good thinker"; a page a day, fidelity irrelevant ("Pretty
  Sketchy"). [stated]
- **Type method** (book): sort needs into type "for a moment" and type "to live with";
  word association; deconstruct a familiar face to find a fresher one; pair by
  distinction and harmony, never two serifs or two sans; few faces, rich palette from
  size, colour, spacing, caps, italics; hierarchy from combined contrast; scales are a
  start and the eye finishes; no baseline grid on the web. Numbers: body 16–18px,
  measure 45–75 characters, line-height 1.2–1.8, headlines 2–3× body, small text about
  80%, #333 over black. [stated, ch3–6; details in `/tmp/jsm/work/owt-findings.md`]
- **Design the way the team works, not only the page.** At Slate he framed the redesign
  as "Redux", a Trojan horse: one experimental article design, published outside the
  CMS, used as a sandbox to change how editorial, design, development, product and sales
  work together; brand by Gretel with visual cues of "story-making" (materials
  overlapping, the editor's hand as marginalia); Retina for text, Register for
  headlines; a deepened maroon plus bright supporting colours; distinct cues per
  vertical. [stated, Slate 2018]

- **Piles of ugly ideas.** He wants "a big sprawling mass of ugly ideas" to get past the
  obvious ones; ideas evolve rather than explode ("Piles of Ideas", 2014). Drafts are
  sketches in their "preferred state: ugly" ("Drafting"). [stated]
- **Optics over numbers.** Type must be judged "optically first, not by the numbers";
  baseline grids on the web are knocked "out of phase" by images, forms and browsers;
  grids are for "organization and improvisation, not a formula" ("Baseline Grids on the
  Web", 2012). [stated] The v5 scale bears this out. [observed]
- **Story first.** Text "offhandedly" dumped into a column no longer passes for an
  article; design should follow the story's "ebb and flow" ("Interludes in Design").
  [stated]
- **Less.** v5's headline feature was "less"; he removed comments ("Five and Ten").
  [stated]

## 3. Taste

- **Print as the measure of the web.** Publishers "dump their prized content into a
  lifeless shell of a site" while their print editions are remarkable ("Death Throes of
  Print", 2008). [stated] He calls himself a graphic designer, not a web designer
  ("Explain Yourself"). [stated]
- **Good over original.** "On Good" quotes Rand paraphrasing Mies ("Don't try to be
  original, just try to be good") and warns that originality for its own sake falls into
  "stylistic tropes". [stated]
- **Sturdy, honest type.** He identifies with Trade Gothic: "sturdy and simple with
  little flourish or fuss", plays well with others, an anchor for structure ("If You
  Were a Typeface"). [stated] Book favourites: Chaparral, Proxima Nova, FF Meta Serif, FF
  Quadraat, Calluna, Caslon, News Gothic, Garamond Premier Pro. [stated] He gravitates
  to "simple and sturdy sans serifs and book serifs". [stated, book]
- **Collecting artifacts.** Typewriters, type drawers, cameras, posters, books: "artifacts
  of creation" that show where his influences come from ("Royal"). [stated] Recurring
  subjects in v4: candy, Halloween, Philadelphia, film cameras, sketchbooks. [observed]
- **Tschichold's reversal** — from New Typography sans to classical book serifs —
  featured as a quote post set in Palatino/Helvetica ("Change of Heart"). [observed]
- **Dislikes** (book): Helvetica/Arial as fearful defaults, faux bold/italic, dumb
  quotes, ready-made novelty fonts, high-contrast faces for body text, hiding text until
  fonts load, clients who treat whitespace as space to fill. [stated]

- **Style labels are not substance.** Calling a design "flat" is like calling a
  musician "loud"; heavy skeuomorphism ("stitching, leather, torn pages") gets a
  "Blech", yet any surface can be good ("The Space Between the Notes", 2013). [stated]
  Note the tension with his own v3 pulp-paperback look and v4 paper textures: he uses
  material references when the content calls for them, not as an interface style.
  [inferred]
- **The web is not a poster.** He asks why a website would be judged "on the same
  scale as a poster", cites Glaser, Scher, Vignelli and Emigré as print reading, and
  WIRED, Praystation and k10k as web landmarks ("Discourse in Web Design"). [stated]
- **One foot in the past.** He loves books and hand-set type but calls the nostalgia a
  "fetishization"; his constant themes are "Art. Drawing. Color. Type. Rhythm." ("What's
  Next", 2014). [stated]
- **Innovation by iteration.** "Trying to be innovative, just like trying to be cool,
  usually fails" ("The Space Between the Notes"). Matches "On Good" in v4. [stated]

## 4. Open questions

- Rendered look of v4 posts: about 20 were seen 2026-11-23 (listed in the moves above);
  the other v4 art-directed posts are still judged from CSS and assets only.
- Which v4 title images use which exact face: matched by eye on screen 2026-11-23; not
  verified against font metadata.
- Several asset URLs (e.g. the Tootsie Pop title) returned tiny files, likely errors;
  not all titles were viewed.
- v1 and v2 were Flash/sliced-image era sites with little design signal in markup; not
  analysed further.
- Talks and interviews linked from his home page (CreativeMornings, Build, SVA, Offscreen,
  The Great Discontent) belong to other streams and were not read here.

- v5: 43 of 90 posts were not fetched; the category index suggests none has custom CSS,
  unconfirmed. The four v5 art-directed posts were seen 2026-11-23 (top of page only for
  Brimfield and Chunky); textures further down those pages were not viewed.
- Whether the v5 archive screenshots (`/i/archive/`) show variants of the designs was not
  checked.
