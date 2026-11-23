# Frank Chimero: his own sites and writing (stream `own`)

Evidence labels: **[stated]** he says it; **[observed]** seen in the work (browser, CSS,
markup); **[reported]** someone else says it. "(Wayback)" marks anything seen only in an
Internet Archive capture; those were viewed in Chrome on 2026-11-23 before the research
was told to stop using Wayback, and nothing further was fetched from it. Live pages were
seen in Chrome on 2026-11-23 at a 1280px-wide window.

Raw files: `/tmp/designers/frank-chimero/raw/own/` (URL on line 1 of each). Text
extracts and CDX lists: `/tmp/designers/frank-chimero/work/`. *The Shape of Design*
was read in full by a sub-agent from the free online edition (CC BY-NC-SA); its
findings are folded in below with chapter names.

## Sources

| Source                                                                    | Date      | What it gave                                                        |
|---------------------------------------------------------------------------|-----------|---------------------------------------------------------------------|
| https://frankchimero.com/ + `/styles.css`                                 | 2025–2026 | Current site: split screen, all Courier, one template for all posts |
| https://frankchimero.com/blog/ (Post Archive)                             | 2009–2025 | Full post list; ruled list, dates right                             |
| https://frankchimero.com/about/                                           | live      | Career, roles, clients                                              |
| https://frankchimero.com/projects/dust/                                   | 2017–2020 | Collage series from archive images                                  |
| /blog/2013/what-screens-want/ (live) + 2013 original (Wayback, HTML+CSS)  | 2013-11   | "Flux"; the art-directed essay system (section bands, gradient breaks) |
| /blog/2015/the-webs-grain/ (live) + 2015 original (Wayback, HTML+CSS)     | 2015-02   | "Grain", "edgelessness", Hockney joiners; reuse of the 2013 kit     |
| /blog/2018/everything-easy/ (live)                                        | 2018-02   | Simplicity, legibility, "change the design, not the toolchain"      |
| /blog/2014/designing-in-the-borderlands/                                  | 2014-04   | Articulation; print/digital translation; Shape of Design system     |
| /blog/2017/plainness-and-sweetness/                                       | 2017-03   | Vanilla design; new plain materials (Untitled Sans/Serif)           |
| /blog/2014/massimo-and-me/                                                | 2014-05   | Design as a fight for beauty                                        |
| /blog/2009/ten-principles/                                                | 2009-02   | Voice over style; one thing per piece; cheap paper; edit            |
| /blog/2025/beyond-the-machine/                                            | 2025-10   | Tool vs instrument; image plates on the current site                |
| /blog/2014/only-openings/                                                 | 2014      | Fetched, skimmed only                                               |
| https://shapeofdesignbook.com/ (12 chapters, CSS, about)                  | 2012      | Book read in full; book site layout                                 |
| Wayback captures of frankchimero.com home                                 | 2008–2019 | 2011, 2012, 2012-10, 2013, 2014, 2015, 2017, 2019 designs           |

## 1. Moves

### M1. Set the type at one size and build hierarchy from space, case and colour

What: one face at one size for everything, headings included; hierarchy comes from
white space, capitals, italics, colour, and position.

Where: *The Shape of Design* (2012): print, ebook and website are "typeset in one
typeface at one size". He did it because e-readers let readers scale text, which blew
headlines up to giant sizes; same-size type with negative space and capitals survives
any reader setting. [stated, "Borderlands"] The book site keeps this: Lyon Text 20/27px,
headings the same size as text, the chapter name set apart only by a burnt orange
(#b95b23) under a #333 "Chapter Three". [observed, CSS and seen live] The current
frankchimero.com does the same in Courier: `h2`, `h3` and body all 1rem/14px; the post
title is distinguished only by bold, centring and space around it; dates and subtitles
go grey (#828b87). [observed, `styles.css`, seen live]

Default it replaces: a type scale with a big H1 and stepped headings.

When it fits: text-led pages, documents meant for many reading environments, and any
page where restraint should carry the voice.

### M2. Split the screen: fixed index on one half, scrolling reading on the other

Current site [observed, CSS and seen live]: above 1000px the viewport splits 50/50. The
left half is a sticky dark green-grey panel (#3d4340) holding the name and the
navigation as a two-column grid of title + grey description pairs ("Studio Frank / My
design practice", "Dust / Collages · 2017–2020", "Post Archive / 2009–2025"). The right
half is a light grey (#eee) panel that scrolls on its own, with a centred 36rem column.
The home page has no right-hand content at all: the index is the home page.

The book site does the same split [observed, seen live]: at 1200px+ the chapter's
engraved illustration sits fixed in the left half on paper-grey, the chapter text
scrolls on the right, and the book title runs vertically up a thin left strip
in spaced monospace caps. Buy/Amazon are black circles at top right.

Default it replaces: a top nav bar over a full-width page.

When it fits: a small site where the whole table of contents fits on one screen and
reading is the main act.

### M3. The navigation item as a two-line label: name, then a quiet gloss

Every nav entry is a title in light text with a dimmer second line saying what it is
and when ("Book · 2012", "Profile & Contact"). The archive list sets titles left and
dates right on hairline-ruled rows; the About page uses the same ruled two-column
rows. [observed, seen live] Earlier versions did the same thing as a table: the 2019
home page lists "Writing Highlights" and "Work Highlights" as year | item rows, ending
with jokes ("1999 Very illegally scored a copy of Photoshop", "1992 Afternoons with
Mario Paint") and an "Otherwise" table ("Eating / Wellfleet oysters", "Endorsing /
Eight hours of sleep"). [observed (Wayback)]

Default it replaces: card grids and nav labels with no context.

### M4. Monospace as the whole voice

The current site sets everything (nav, essays, captions) in plain `Courier, mono`,
with old-style proportional figures turned on, antialiased, 14px, line-height 1.5.
[observed, CSS] Monospace also served as the "utility" face on the book site (PitchWeb
for header, nav, captions, next-chapter labels, with Lyon for reading). [observed, CSS
via sub-agent; seen live: the vertical title strip and Buy buttons] On the current
site the typewriter face reads like a manuscript or a letter. [observed (seen); the
reading is inference] It fits his stated case for plain, "vanilla" materials (M10).

Default it replaces: a geometric sans for UI and a serif or sans for body.

### M5. A long essay as a sequence of coloured bands, one band per beat (2013–2015)

What Screens Want (2013) and The Web's Grain (2015) were published as their own
art-directed pages [observed (Wayback); also stated in their forewords: "This site is
an interpretation of my talk"]. The page is a stack of full-width `section`s, each with
its own ground: charcoal title block (#333) with a big white serif title ending in a
grey em-dash and an italic grey subtitle; a pale mint or light grey foreword band with
centred smaller text; white text sections; dark sections (#333 / #000) where the essay
turns; a section with a woodgrain photo as background for the "grain" passage; black
video sections. [observed (Wayback), CSS `section.white/.black/.realblack/.wood/
.video`] Each band changes when the argument changes, so the reader feels the talk's
slides as colour changes while reading one 30em serif column (Tiempos 21px, text at 65%
black). [observed; the reading is inference]

The Web's Grain reused the same class names and look with Calibre for display, Minion
Pro/Times for text, a gold (rgb 185,154,84) for pull quotes and the end mark ◆.
[observed (Wayback), `custom.css`] So the essays formed a series with a shared kit.

Default it replaces: a blog post template with images inline.

When it fits: a talk turned into an essay; any long piece with distinct movements.

### M6. Gradient "breaks": one thin word per screen

Between movements, a tall section with a vertical peach → pink → lavender → mint
gradient image (`vertgrad.jpg`), in which single words in Lato 100 (2013) or Calibre
Thin (2015), white, 6em, letter-spaced, uppercase, sit far apart: scrolling reads
"THE … VOLUME OF … LIGHT" one word at a time. The last break is 120em tall.
[observed (Wayback), seen and CSS] Scroll becomes time, which matches his thesis that
screens are about change ("flux"). [observed; the link is inference from his text]

Default it replaces: a heading (H2) between sections.

### M7. Statements set as centred headings between short rules

Key sentences ("The padding isn't around the screens. It's *in* them."; "If something
can be anything, it usually becomes everything.") are set as centred 2.5em headings in
gold or grey, with a 3em-wide pale rule above and below; quotes in The Web's Grain are
gold sans at large size ("We begin in admiration and end by organizing our
disappointment."). [observed (Wayback)] A slide-like sequence (James Burke's
"plastic → software" passage) is a centred italic stack of image + caption steps,
opened and closed by giant 10%-opacity quotation marks. [observed (Wayback), CSS
`div.burkestep`]

### M8. Frame small images as objects; let motion carry the idea

In What Screens Want small pictures sit inside a thick translucent ring (`border-radius`
70em, 1em border at 5% opacity), like a porthole or a pill; the zoopraxiscope image
spins with a CSS animation; one band has an animated Muybridge horse GIF as a fixed,
full-cover background; the Muybridge strip is shown twice, offset left −20% and right
+20%. [observed (Wayback), CSS] He argues animation is "a functional method for
design", and half the job is "crafting the interstitials". [stated, What Screens Want]

### M9. Collage and layering, from joiners to Dust

The 2015 home page was a collage on charcoal with a grey dot grid: a Muybridge strip
tinted purple, an engraved eye in a cyan circle, a blue panel of white blobs, black and
white photos with white borders, a plaster bust, a pink-tinted beach photo, a teal
diagonal bar, a white silhouette figure, all overlapping at different sizes. Only the
header text ("Frank Chimero is a designer who writes.", nav: Writing, Books, Library,
About) sat above it. [observed (Wayback)] In The Web's Grain (same year) he holds up
Hockney's photo joiners as the model of web design: "an edgeless surface of unknown
proportions" assembled from small pieces. [stated] Dust (2017–2020, live) continues it:
collages of "old, forgotten images from public archives" on paper-grey, with a
hand-drawn red line, ink brush marks, a bird, a hand, cherries; he made them to balance
design's "newness and optimistic clarity" with "ambiguity and wistfulness". [observed
and stated, Dust page]

Default it replaces: a hero image or a tidy grid of thumbnails.

### M10. Plain, "vanilla" materials, refined by attention

He wants design "like vanilla ice cream: simple and sweet, plain without being austere";
"attentiveness turns the normal artful". Defaults (Helvetica, Times, link blue) carry
baggage, so designers must keep finding "new, plain materials", e.g. Klim's Untitled
Sans and Serif, which became studio staples. [stated, "Plainness and Sweetness"] His
sites act this out: 2014 home was a single text column with small letter-spaced caps
labels and em-dash lists [observed (Wayback)]; 2019 was black with small system-sans
text and red-underlined links in a year table [observed (Wayback)]; today it is Courier
on two greys. [observed]

Default it replaces: individuality signalled by decoration.

### M11. Go with the grain of the web: stack, flow, and avoid fighting proportion

He names the web's natural patterns: fluid width, vertical stacking, flat colour and
simple gradients (cheap, scale to unknown areas), horizontal bands, text as interface,
tinted background photos with big type over them, mosaics. These shared patterns are
"best practices" from a common medium, "not evidence of a visual monoculture".
[stated, The Web's Grain] The core conflict to manage: images keep their proportions
and get taller as they widen; text gets shorter. [stated] Against it are "bicycle bear
websites", e.g. scroll-jacked product pages. [stated] His own sites follow this: full-
width colour bands, single columns, flat colour. [observed]

### M12. Draw the content first, then put the box around it

"It's better to come up with an arrangement of elements and assign them to a size,
rather than the other way around" — sketch content lock-ups first, then the frame
(example: Kasper Laigaard's Hello Monday sketches). Design how pieces "build up", not
how they break down. [stated, The Web's Grain]

### M13. Change the design, not the toolchain

"Instead of changing my tools or workflow, I change my design" — like designing a house
easy to build rather than renting skyscraper cranes. His whole technical list: simple
responsive layout, web fonts and nicely set text, performant images. "No razzle-
dazzle": find "the one or two uniquely true things" about the client and express them
"with a light touch"; a great photo, illustration or sentence "does most of the work".
[stated, Everything Easy] Legible source matters so others can learn. [stated] The
current site's whole stylesheet is about 250 lines of plain CSS with nesting, no
framework, no JavaScript. [observed]

### M14. Design one system from the most limiting medium outward

For *The Shape of Design* he started from the most restrictive format (Kindle) and let
it set the rules for print, ebook, site and merchandise: Quadraat chosen for screen
legibility and webfont availability; a line-etching illustration style because it
looked best on e-ink; a starburst cover legible at thumbnail size, which became the
brand. [stated, "Borderlands"] The book site still shows the engraved,
orange-and-black line illustrations beside the text. [observed, seen live]

### M15. Use images as plates, in pairs

On the current site, images sit full column width with a 2px radius; on Beyond the
Machine a pair of black-and-white portraits (Coltrane and J Dilla) sits side by side
inside one black plate, with a small centred grey caption in Courier below.
[observed, seen live] Hairline `hr`s are short (10rem) and centred, not full width.
[observed, CSS]

## 2. Process and thinking

- **Design as articulation.** His ideal moved from decoration (editorial illustration
  for The Atlantic, Time, Newsweek) to construction (interfaces) to articulation:
  "clarity, fluency, and coherence"; describe the problem accurately, then chip at it.
  He asks "Can you write a design?" and started chasing verbs over nouns. [stated,
  "Borderlands"]
- **Problems have grain.** Like wood, a problem shows how it wants to be cut, but it
  takes time to unfold. [stated, "Borderlands"] The 2013 holding page on his own site
  (Wayback) asked exactly this, in scattered, slightly rotated light-sans phrases on
  pale pink: "Make it look like what it is.", "Play it as it lays", "I'm working on a
  new site — but don't know what a personal website looks like any more. So, 'What does
  it want to be?'" [observed (Wayback)]
- **Why before how.** Write the purpose; copying a finished piece's surface without its
  why is the mockingbird imitating a car alarm. Alternate close work with stepping back
  to judge the whole. [stated, book ch1]
- **Start with bad ideas inside fixed limits.** Write objectives, put them away, start
  with the worst ideas to get moving, then bring the objectives back. Set limits of
  content, structure and tone, then say "yes, and" inside them. Expect waste. [stated,
  book ch3] Cheap paper so bad ideas feel free. [stated, "Ten Principles"]
- **Message, tone, format as separate levers.** Tone is not style; style is a tool to
  set tone. New formats and materials make breakthroughs. [stated, book ch4]
- **Respond to the site.** Like Robert Irwin, study the context before deciding; many
  good answers exist (Shaker, Eames, Gehry chairs). [stated, book ch6]
- **Pace as story.** Find where time passes (scroll, sections, line height) and change
  the rhythm there; leave a void for the reader to fill (Hopper's *Nighthawks*).
  [stated, book ch7]
- **One thing per piece.** Choose the one thing a piece should do, then find the best
  way to do it; consistent voice matters more than consistent style; cut anything not
  spectacular. [stated, "Ten Principles"]
- **Designer as translator.** Move work across print and screen; designing across
  formats is easier as one system than as separate pieces (Hollis's *Ways of Seeing*
  set in bold Univers so text weighs as much as image; Fiore's *Medium is the
  Massage*). [stated, "Borderlands"]
- **Translate talks into pages.** His major essays are talks rebuilt as web pages, with
  audio, video and GIFs where the talk had them (modem sound player in The Web's Grain).
  [stated and observed]

## 3. Taste

- **Praises:** Hockney's joiners; Muybridge; James Burke; Calvino's *Six Memos*
  (lightness); Saul Bass, Alvin Lustig, Paul Rand, the Eameses as cross-discipline
  heroes; Quentin Fiore, Richard Hollis, Jerome Agel; Jasper Morrison's "Super Normal";
  Dot Dot Dot's normalised ads; Klim's Untitled faces; Vignelli, after a grudge
  ("fight for beauty"); Miles Davis's *Kind of Blue* (air over Bebop density); the
  Shakers. [stated]
- **Dislikes:** "bicycle bear" sites (Apple's Mac Pro scroll page); the flat vs
  skeuomorphic debate, since "screens are aesthetically neutral"; showmanship and
  over-composed coldness; toolchain complexity and illegible source; dark patterns and
  attention-greedy business models; "tips" over principles. [stated]
- **Recurring motifs:** horses and Muybridge, maps, grain and wood, gradients,
  collage from archive images, plain type, jazz and hip-hop as models of practice
  (Coltrane, J Dilla, "you *play* an instrument"). [observed across essays]
- **Self-image:** a generalist "chimera" in the borderlands between illustration, type,
  web and writing; "a designer who writes" (2014–2015 home pages). [stated; observed
  (Wayback)]
- **Colour habits:** greys and one warm accent (burnt orange #b95b23 on the book site,
  gold in the essays, crimson link hover on the 2015 site, red underlines in 2019,
  sage #5e786d hover today), against which he sets the occasional full saturated field
  (the 2012 coral home page, the 2013–2015 gradient breaks, the 2015 collage).
  [observed; 2012–2019 from Wayback]

### Site versions seen (for reference)

| Version   | What it looked like                                                                          |
|-----------|----------------------------------------------------------------------------------------------|
| 2011-04   | "BRB" temporary page: small sans, two narrow columns, arrow links, yellow highlight (Wayback) |
| 2012-01   | Full coral page, big serif one-line bio, linked prose in one left column (Wayback)           |
| 2012-10   | White, centred narrow column, light sans, coral lead paragraph (Wayback)                     |
| 2013-07   | Pale pink holding page of scattered, tilted phrases (Wayback)                                |
| 2014-11   | One serif column, letter-spaced small-caps labels, em-dash lists (Wayback)                   |
| 2015-06   | Charcoal with dot grid, full-page collage under a one-line header (Wayback)                  |
| 2017-08   | Navy temporary page, pink sans labels, serif text (Wayback)                                  |
| 2019-01   | Black, small sans, year tables, red underlines (Wayback)                                     |
| 2025–2026 | Split screen, all Courier, dark green-grey index and light grey reading panel (live)        |

## 4. Open questions

- Wayback use stopped mid-research by instruction. Not seen: the 2008–2010 designs
  (2008 capture had no CSS; 2009 rendered only a pale blue page), 2016, 2020–2024 home
  pages, the original art-directed Everything Easy is Hard Again (2018, had its own
  title SVG), The Good Room, Back to the Cave, and the 2016 New Yorker post. Their own
  designs are unknown; the live versions all use the one current template.
- Images in the archived What Screens Want were lazy-loaded and did not render, so the
  ring frames were judged from CSS and empty frames.
- Redesign posts or a colophon for the current site were not found on the live site.
- Typeface of the 2012 coral home page and 2017 serif not identified.
- "Only Openings" and "Beyond the Machine" were fetched but only skimmed.
- No YouTube or talk video was used; talk content here comes only from his written
  adaptations. Talks, client work (NPR, Wikipedia, Abstract) and others' accounts are
  in the sibling streams.
