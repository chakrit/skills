# Rob Weychert: work notes

Stream: `work`. Pages studied in Chrome on 2026-11-24, each laid in a same-origin frame at
1440 px (desktop) and 390 px (phone) and screenshotted top to bottom. Numbers come from the
rendered page (computed styles and element boxes); CSS was read only to explain something
seen. Every claim is marked:

- **[observed]**: seen on the page named.
- **[stated]**: the designer says it, with the URL.
- **[reported]**: someone else says it, with the URL.

Caveat that applies to all v7 pages: the browser was in dark mode, so v7 pages rendered
their `prefers-color-scheme: dark` palette. The v7 CSS makes light mode the default
(`--colorBG: var(--shadeLighter)`, 96% lightness), which was not seen.

## Sources

Pages studied (all fetched 2026-11-24):

| #  | URL                                                                      | Project and kind                                      |
|----|--------------------------------------------------------------------------|-------------------------------------------------------|
| P1 | https://v7.robweychert.com/ (robweychert.com redirects here)             | Personal site v7 (2025–), home page                   |
| P2 | https://v7.robweychert.com/blog/2026/10/krasner-pollock-past-continuous/ | Personal site v7, blog article with images            |
| P3 | https://v7.robweychert.com/projects/propublica/                          | Personal site v7, portfolio case study                |
| P4 | https://v6.robweychert.com/blog/2024/10/robtober/                        | Robtober 2024, one-off art-directed post              |
| P5 | https://v6.robweychert.com/blog/2024/03/philadelphia-organ-festival/     | Personal site v6 (2017–2025), blog article            |
| P6 | https://v5.robweychert.com/writing/best-films-2012/                      | Personal site v5 (2011–2014), list article            |
| P7 | https://plusequals.art/                                                  | Plus Equals zine, home page / issue index             |
| P8 | https://cubes-revisited.art/                                             | Incomplete Open Cubes Revisited, generative art piece |
| P9 | https://v4.robweychert.com/                                              | Personal site v4 (2005–2008), home page               |
| P10| https://www.philamoca.org/about/                                         | PhilaMOCA (client), website inner page                |
| P11| https://themarkup.org/                                                   | The Markup (client), homepage inside the host's site  |

P10 and P11 were first set aside for step 8, then studied after it from the full-size
screenshots taken on 2026-11-24 (no browser measurements) and their HTML and stylesheets
fetched with `curl` the same day (`philamoca2022/style.css`, The Markup's
`static/dist/main.76f9f65b.css`). Their pixel values are computed from that CSS at 1440 px
and 390 px and checked against the screenshots.

Pages that say he made these:

- https://robweychert.com/about/ (2026-11-24): versions V1–V6 of the site are kept online;
  "this, the seventh version" launched September 2025. **[stated]**
- https://robweychert.com/projects/ and its project pages (2026-11-24): ProPublica article
  layout framework, The Markup homepage, PhilaMOCA branding and website, Plus Equals,
  Incomplete Open Cubes Revisited, Robtober. **[stated]**
- https://v7.robweychert.com/blog/2022/02/propublica-article-layout-framework/ (post dated
  2022-02-04, also on propublica.org): how the ProPublica layout framework works. **[stated]**

- https://robweychert.com/projects/philamoca/ (2026-11-24): he did PhilaMOCA's "Branding,
  website, and merch"; the identity is "high-contrast black and white", drawing on "the
  austere aesthetics of some corners of the late '70s post-punk movement". The P10 footer
  reads "Site design and development by Rob Weychert", and the theme stylesheet header
  names him as author. **[stated]**
- https://robweychert.com/projects/the-markup/ (2026-11-24): "the homepage design I
  created"; he delivered "documentation, Figma mockups, and HTML/CSS template", which The
  Markup implemented. The caption of his template image says it excludes "their
  pre-existing header and footer" and has "placeholders for copy and icons that folks at
  The Markup would later develop internally". **[stated]**

Set aside for step 8: none. The two set-aside pages (PhilaMOCA About, The Markup home)
were used in step 8 and are now studied as P10 and P11.

Screenshots: `/tmp/design-research/rob-weychert/work/shots/` (P1–P9,
`NN-<page>-d-NN.png` desktop, `-p-NN.png` phone) and
`/tmp/design-research/rob-weychert/work/set-aside/` (P10 as `A-…`, P11 as `B-…`). Not
committed.

## Findings per page

### P1 v7 home

- Grid: 12 columns of 61.3 px with 44 px gutters (gutter ≈ 0.72 column), 110 px side
  margins, 1220 px wide. The main content spans columns 1–8 (798 px); a "Recent blog
  posts" sidebar spans 9–12 (x958–1338). The header uses the same 12 columns. Featured
  items sit two-up on a subgrid, 377 + 44 + 377. The footer runs the full 12 columns.
  **[observed]**
- Type: one family, Degular (self-hosted variable font), for everything. H1 69.5 px,
  weight 700, line-height 0.9 (62.6 px). The intro sentence under it is 39.1 px at weight
  225, a hairline weight. Body base 22 px / 31.9 (1.45). Labels and sidebar text 16.5 px at
  weight 533. Card titles 22 px weight 700. H1 to body 3.16:1. Left-aligned, ragged.
  **[observed]**
- The v7 CSS builds this from a 4:3 scale: `font-size = base × (4/3)^n` and
  `font-weight = baseWght ÷ (4/3)^n`, so text gets lighter as it gets bigger unless a
  heading resets the base weight to 700. That is why the 39 px intro is weight 225 and the
  16.5 px labels are 533. **[observed in CSS, v7.robweychert.com/assets/css/main.css]**
- Colour (dark mode): near-black green-grey background oklch(0.28 0.008 156), warm
  off-white text oklch(0.9 0.008 75), one saturated accent, magenta oklch(0.65 0.18 336).
  The accent covers perhaps 2% of the page: every link underline, every 1 px rule, the
  search field outline, the filled sidebar header, the round play buttons. A full-page SVG
  of fine moiré curves sits faintly behind everything. **[observed]**
- Imagery: 16:9 card images, 4 px radius, the full card width; small book and film
  posters (75 px) set right inside text rows. **[observed]**
- Composition: the H1 and the light 39 px sentence are largest; the magenta sidebar
  header is the only filled colour block above the fold. Magenta hairlines separate every
  row of cards and every footer row. Empty space sits to the right of the intro within
  the 8 columns. **[observed]**
- Motion: the sidebar is sticky and scrolls on its own (its content runs to y≈4000 on a
  2307 px page). Links change colour over 0.2 s on hover; the CSS opts into cross-page
  view transitions. **[observed; transitions from CSS]**
- The last sentence of the intro changes on each load: "Enjoy your stay.", "No big
  whoop.", "Please remove your shoes before entering." **[observed across loads of P1–P3]**
- Phone: 6 columns of 44.8 px, 18 px gutters, 16 px margins. H1 43 px / 38.7 (two lines),
  intro 24 px. The sidebar becomes a floating magenta "Recent blog posts" button fixed at
  the bottom left. Poster thumbnails are dropped and the four "Watching / Reading /
  Listening / Attending" items go two-up. **[observed]**

### P2 v7 article (Krasner and Pollock)

- Same 12-column frame: text in columns 1–8 (798 px), sidebar "More art posts" in 9–12.
  Body 22 / 31.9, measured 84–86 characters per line. H1 69.5 px, two lines. **[observed]**
- Colour: here the accent is coral, oklch(0.65 0.18 17), and the grey background is tinted
  toward hue 197. The v7 script sets the accent hue from the page's own date:
  `300 − month × 30 − day` (main.js line ~1048), and the CSS sets the base hue to the
  accent + 180 (its complement) at 2% chroma. The CSS comment reads "Jan = 300, each month
  after subtract ~30". So every post has its own accent, and the home page takes today's.
  **[observed; formula from v7 main.js and main.css]**
- Images: two paintings at the full 8-column width, natural aspect (798×673, 798×479), not
  cropped, 4 px radius, caption 16.5 px below at the left. **[observed]**
- End of article: metadata as outlined chips (1 px accent border, icon plus label: month,
  tags, people, places), then a segmented prev / "Blog" / next control. Footer: the
  "Hi, I'm Rob Weychert." sentence large on the left (bold name, light remainder), nav on
  the right, then four "Featured" items in four 3-column slots. **[observed]**
- Phone: H1 43 / 38.7, body 18 / 26.1 at about 46 characters per line, images full width
  (359 px), chips wrap. No sidebar and no floating button. **[observed]**

### P3 v7 case study (ProPublica project page)

- Accent blue, hue 266. H1 "ProPublica" 69.5 px / 700, then a 39 px light subtitle over two
  lines, then an italic 22 px line of disciplines ("Graphic design, UI/UX design, web
  design, code"). **[observed]**
- A square screen-recording video spans the 8 columns (798×798). A second video is floated
  right, 272 px wide, and the body text wraps beside it at 43–45 characters per line. The
  page says the ProPublica layout framework is "in use (albeit modestly) on this very
  page!" **[observed; stated on the page]**
- Paragraphs: the second paragraph starts with a 2 em first-line indent and no space above
  it. The v7 CSS indents every `p + p` in posts by `--textIndent: 2em`. **[observed; CSS]**
- The prev / "Projects" / next segmented control is sticky at the bottom left and rides
  over the body text while scrolling. **[observed]**
- Phone: the floated video becomes full width (359×558); body 18 / 26.1. **[observed]**
- The video shows a ProPublica article (serif text, centred column); that article design
  is ProPublica's system, built with David Sleight and Allen Tan. **[stated,
  robweychert.com/projects/propublica/]**

### P4 Robtober 2024 (v6)

- Opening: one full viewport (1440×835) holds a lettered title: "ROBTOBER" in a heavy
  display face with the T drawn as an inverted cross, "MMXXIV" in small serif capitals,
  the letterforms filled with a looping flame video
  (`/assets/videos/2024-10-06-robtober-flames1.mp4`), a red glow behind. A fixed photo of
  glowing embers, toned navy and red, sits behind the whole page. **[observed]**
- On the phone the same title is stretched into tall, very condensed letters that fill the
  390×835 viewport. The project page calls this "a flaming title screen with dramatically
  responsive typography". **[observed; stated, robweychert.com/projects/robtober/]**
- Text: HEX Franklin (variable) 23.6 / 35.4 (1.5) in pinkish rgb(221,194,187) on navy
  rgb(6,19,45); accent orange-red rgb(255,100,61) for rules, the section heading, link
  underlines and the grid/list toggle. One centred measure, 805 px wide (x318), 48–57
  characters per line. The first paragraph opens with a bold run-in, "Every October,";
  later paragraphs indent 47.2 px (2 em) with no space between. **[observed]**
- Sizes: body, section heading and day headings are all 23.6 px; the only other text size
  is 18.9 px uppercase, tracked, in the footer. The heading is set apart by weight and
  colour, not size. **[observed]**
- The film schedule breaks out of the text measure: 6 columns of 192 px posters
  (2:3, uncropped), 11.8 px (0.5 em) gaps, 1213 px wide against the 805 px text column.
  A grid/list toggle sits at the right end of the heading row. **[observed]**
- Footer: avatar circle and bio in a 74 px | 707 px grid; copyright in tracked capitals.
  **[observed]**
- Phone: body 16.6 / 24.9, indent 33.2 px, posters 4 across at 83 px with 8.3 px gaps; the
  footer avatar floats and the bio wraps under it. **[observed]**

### P5 v6 article (Philadelphia Organ Festival)

- Colour: the page loads one of five colour schemes at random on each load (inline script
  commented "Load a random color scheme", choosing colors1, 2, 4, 5 or 6.css). Each scheme
  pairs a muted dark text colour (#614e65 plum, #6b4d47 brown, #74586a mauve, #665d79
  violet-grey, #495969 slate) with a pale tinted background, a hot accent (#ff668c pink,
  #ffa3a3, #ed6e87, #fa7538 orange, #ff974d) and a muted mid tone (olive, teal, tan, sage,
  terracotta). The desktop load got slate on #f3eeed inside a tan frame; the phone load got
  brown on #eaeff1 with a brown footer. **[observed]**
- Desktop frame: a 48 px tan border on both sides, a white navigation column (x48–271:
  circular "RW" logo, HOME / BLOG / SHOP in spaced capitals between hairlines), then the
  tinted content panel. The 666 px text column sits at x498, nearer the left of the panel
  (227 px left, 237 px right of it). **[observed]**
- Type: two families. Headline Ciutadella 45 / 45 at weight 400 (a regular sans, not
  bold); meta line 15 px tracked capitals in the scheme's mid tone with a link icon. Body
  Freight Text Pro 20 / 30 (1.5), 66–78 characters per line. H1 to body 2.25:1.
  **[observed]**
- The article opens with a newspaper dateline in small capitals: "FIRST PRESBYTERIAN
  CHURCH (GERMANTOWN), PHILADELPHIA, PA—" running into the first sentence. Later
  paragraphs indent 40 px (2 em), no space between. **[observed]**
- Lists: bullets and numerals hang outside the text edge, in the accent colour. A short
  rule (about half the column) separates the body from the credits list. **[observed]**
- Related posts: a 3 px dark rule, 15 px capital label, two columns divided by tan
  hairlines. Footer: full-width dark band, square black-and-white portrait, serif bio,
  capital copyright line. **[observed]**
- A banner at the top reads "This version of my site is no longer updated. Go to the
  latest version." **[observed]**
- Phone: the navigation becomes a top bar (logo left, HOME BLOG SHOP right in large spaced
  capitals) under the banner and a 6 px accent stripe. H1 40.5 px, barely smaller than the
  45 px desktop one. Body 18 / 27, 42 characters per line, indent 27 px; list markers
  still hang. **[observed]**

### P6 v5 list article (Best Films of 2012)

- The page's Typekit fonts (museo-slab, minion-pro in the CSS) did not load;
  `document.fonts` was empty, so it rendered in Georgia and Times. Faces below are what the
  CSS names, not what was seen. **[observed]**
- Desktop: dark slate background with a diagonal stripe pattern; a white panel with
  rounded corners (x236–1213); logo above the panel at the left; nav "About • Writing •
  Subscribe" with the current item in italic. The text column (540 px at x594) sits in the
  right part of the panel, leaving about 360 px of the panel empty on the left.
  **[observed]**
- H1 48 / 48 weight 900 slab, followed by a heavy 8 px rule across the column. Body 18 / 24
  (1.33), 52–72 characters per line. The opening words are set in spaced capitals ("I ONLY
  SAW 32 new movies"). The second paragraph indents 36 px (2 em), no space between.
  **[observed]**
- The ranking counts down 7 to 1; the numerals hang outside the column edge beside 24 px
  bold titles. Italic note, a 2 px rule, italic date and "Read more about film." One text
  colour, no accent. **[observed]**
- Phone: column 303 px at x43, H1 36 px centred (left-aligned on desktop), rule kept,
  indent kept, numerals still hang, footer meta centred and italic. **[observed]**

### P7 Plus Equals home

- Pure black background, light grey text rgb(217,217,217), one darker grey rgb(140,140,140)
  for the form field and "Powered by". No accent colour. **[observed]**
- One family, GimletTextNarrow (a narrow serif), for everything. The intro is an H1 written
  as a sentence, 28 / 42 at weight 400, with the zine title in italic and his name as an
  underlined link. Body 18 / 28, with a bold run-in "Now available in print!". H1 to body
  1.56:1. **[observed]**
- Grid: four fixed 273 px columns with 56 px gaps (equal to the 56 px left margin),
  anchored left, which leaves 124 px on the right at 1440. Each issue: "Plus Equals #7"
  above at the left, the square cover inside a heavy light-grey frame (about 7 px), the
  date below aligned right. Newest first; the last row holds three of four. **[observed]**
- Imagery: each cover renders "+ = n" for its issue number in that issue's visual system,
  white line or halftone work on black. **[observed]**
- Phone: one column, covers full width (365 px, 12 px margins), H1 24.9 / 37.3, same
  label-above, date-below-right arrangement. **[observed]**

### P8 Incomplete Open Cubes Revisited home

- Black background, white and grey rgb(179,179,179) text, a footer band rgb(38,38,38).
  Type is `system-ui` only: H1 72 / 79 at weight 400, subtitle 25.2 px grey, body 18 / 27.
  H1 to body 4:1. **[observed]**
- Built on the combinatorics, not a page grid: an intro split 1:2 (441.6 | 883.2 px) with an
  isometric open cube in shaded grey bars on the left, which cycles through variations by
  CSS animation (intro01 … intro12; no canvas), and the title on the right. A small grey
  "See the 4,094 variations" with a chevron closes the first viewport. Below, an index of
  the 11 part-counts in a 4-column grid of 267.75 px boxes with 3 px gaps, each box a 1 px
  dark outline holding a line drawing and "n-part: count", the counts padded to line up.
  Each box links to a page listing every variation with that many parts (/01/ … /11/).
  **[observed]**
- Phone: everything stacks and centres: animated cube above, H1 46.8 / 51.5 centred,
  the index one box per row. **[observed]**

### P9 v4 home (2005–2008)

- Fixed 725 px page centred on white; no web fonts (Georgia and a Verdana-like sans), as
  the era's sites were built. **[observed]**
- Header: a blackletter wordmark "Rob Weychert" in navy over a peach band of rococo scroll
  ornament; nav in small bold orange capitals, the current item on a pale-blue tab with a
  pointer. **[observed]**
- Three columns: main about 386 px, then two sidebar columns of about 150 px, separated by
  1 px vertical rules. Each entry: Georgia title about 22 px in navy over a 2 px rule; a
  date block at the left in bold brick red (rgb(153,51,51), "18 November 2008 / Tuesday,
  1:30 PM" with small-capital PM) beside a 1 px vertical rule; the entry opens with a
  spaced small-capital run-in ("WHAT A YEAR THIS TURNED OUT TO be."); the next paragraph
  is indented; text wraps under the date block. A dashed rule, then a centred capital
  link line "READ THE FULL EDITORIAL | COMMENTS CLOSED (51)" in orange with a dotted
  underline. **[observed]**
- Sidebar: an illustrated "Ask The Monkey" panel (blackletter title, monkey portrait,
  ornamental frame, lavender ground); section labels as maroon banner tabs with white
  capitals and a flourish ("RECENT WORK", "DAILY HAIKU", "CONSUMPTION"); sub-heads in small
  bold navy capitals over 2 px rules; fleuron and pointing-hand bullets. **[observed]**
- Phone: no viewport meta tag; the layout stays 725 px, so at 390 px the sidebar sits
  off-canvas. **[observed]**

### P10 PhilaMOCA About (client site, WordPress theme "PhilaMOCA 2022")

Everything on this page is his: the theme stylesheet names "Design and development by Rob
Weychert", and the logo is part of the branding his project page credits to him.
**[stated, philamoca2022/style.css header; robweychert.com/projects/philamoca/]**

- Grid (≥70em): two columns, `max-content` for a sticky left header column (logo, nav,
  social icons, address, email) and `minmax(auto, 90ch)` for the content; outer padding
  48 px (`--spacing3` = 2 × base). In the screenshot the content panel runs x343–1401 and
  the text x457–1287. The article is capped at 60ch and centred in the panel. Below 70em
  the page becomes one column, 40em wide from 52em up. **[observed in screenshot; CSS]**
- Type: one family, Archivo (Omnibus-Type, self-hosted, weights 400–700). A fluid scale
  "loosely based on Utopia" (CSS comment): base 16 px at 300 px wide rising to 24 px at
  1400 px; three sizes only, base × 13/16 for metadata, base, and base × 30/16 for titles.
  At 1440 px: body 24 / 33.6 (1.4), title "About PhilaMOCA" 45 px at weight 400 (not bold)
  and line-height 1, sub-heads ("Accessibility", "Rentals", "History (as we know it)") at
  body size, weight 700. Title to body 1.875:1. Nav in uppercase. About 70 characters per
  line. **[observed; CSS]**
- Paragraphs: separated by a margin of 0.75 × base (18 px at desktop), no first-line
  indent. The text opens plainly. **[observed; CSS `.page__article > * + *`]**
- Colour: greyscale only. Ground black hsl(0,0%,0%); in dark mode (as captured) the panel is
  hsl(0,0%,18%) with text hsl(0,0%,88%); in light mode the panel is the 88% grey with black
  text. White is used only for hover and focus. No accent colour. **[observed; CSS]**
- Panel: radius `--spacing-4` = base × 0.125, 3 px at desktop. Below 52em its left
  corners are square so it runs into the left edge. **[observed; CSS]**
- Imagery: the facade photo is floated right at 50% of the article width (415 px) with a
  1em gap, square corners; below 52em it is full width above the text. **[observed; CSS]**
- Rules: none on this page. The same stylesheet draws slanted dividers between event
  details and around ticket buttons on the events pages, `skewX(-11.69deg)`, the slant of
  the logo's line, with a border width `--logo-line` = 4.86/300 of the logo width, the
  logo's stroke. **[observed on P10; CSS for the events pages, not seen]**
- Header: the logo (a coffin with a heartbeat line and a slanted stroke dividing PHILA /
  MOCA) and a fade under the sticky header drawn as an SVG pattern of slanted hairlines,
  close to the logo's slant, so text scrolling under it breaks into hatching. Social links
  are a row of circular icons. Links underline in the text colour (0.05em, thickening to
  0.1em on hover). **[observed; HTML, CSS]**
- Phone: sticky header with logo and a three-line menu button (shown below 70em); base
  16.65 px; panel flush left, image full width. **[observed]**

### P11 The Markup homepage (client page inside the host's site)

What is his and what is the host's:

- The Markup's: the header (wordmark, "Menu", "About Us", stacked "Donate" button, the
  "2¢ for our 2¢?" tag with its curved arrow) and the footer, by his own caption; the
  icons in the story lines and the final copy, which his caption says The Markup developed
  later; the site-wide stylesheet in which the homepage rules sit. **[stated,
  robweychert.com/projects/the-markup/]**
- His: the homepage between header and footer, delivered as documentation, Figma mockups
  and an HTML/CSS template that The Markup implemented. His template image on the project
  page (v7.robweychert.com/assets/img/SJIS8NukZj-1200.webp) already holds the centred
  statement over a pill pattern, the dotted halftone band before each section, the dotted
  L-shaped connector with an arrowhead from each section label, pink section labels on the
  left of the articles, the two outlined call-to-action boxes with stacked buttons, serif
  headlines over sans text, and a "Category: link" line under stories with a placeholder
  circle where the icon now is. **[stated; observed in his template image]**
- Not settled by any source: whether the typefaces (Ivar Display / Ivar Text serif,
  Messina sans), the navy #242a49 / pink #ff335f / warm grey #f3f2f1 palette and the
  stacked-outline button came with The Markup's existing brand. His project page does not
  say. The pink and navy and the stacked button also appear in the parts he says were
  pre-existing: the header's "Donate" link uses the site-wide `.button` class, drawn with
  two offset `:before`/`:after` outline layers. The fonts and colours are declared in the
  site-wide stylesheet, not in homepage-only rules; the homepage re-implements the stacked
  button for its calls to action. **[observed in HTML/CSS]**
- The live page differs from his template: section labels are now single words
  ("Investigations", "Impact", "Blueprints", "Tools") where the template had sentences
  ("We investigate harmful technology."), the hero copy is different, the top story
  layout is different, and the icons are filled in. **[observed: live screenshots against
  his template image]**

Findings:

- Grid (≥65em): content max 71.25rem (1140 px) centred (x150–1290 at 1440); each section
  is a 16-column grid with the label in columns 1–4 and the stories in 5–16 as 1, 2, 3 or
  4 articles (`section--1up` … `--4up`, matching "one to four articles per section" on his
  project page). 42–65em uses 12 columns with the label above. **[observed; CSS]**
- Type: two families. Hero sentence Ivar Display 36 px weight 700, line-height 1.1, centred,
  two lines, max 35ch; under it two lines of Messina 21 px. Story headlines Ivar Display
  18 px bold (30 px for the top story); body and deks Messina 16 / 24 (1.5), deks grey
  #66615b; section labels Messina 21 px bold pink. The scale is 12, 14, 16, 18, 21, 24,
  30, 36 px. Hero to body 2.25:1. **[observed; CSS]**
- Colour: warm grey ground #f3f2f1, navy text #242a49, pink #ff335f for section labels,
  "This Just In", the CTA box outlines, filled CTA buttons, the "Related:" and "Original
  Investigation:" labels and their icons, and the dotted underlines in the hero. Tan
  #cac7c3 for hairlines. White under the CTA boxes and button layers. **[observed; CSS]**
- Texture and connectors: every section opens with a 12 px band of a 3 px dot pattern in
  navy (the "halftone band"); each section label is joined to its stories by a dotted
  navy line drawn as an L (top and left edges of a pseudo-element) ending in a right-
  pointing arrowhead SVG; the hero sits on `data-pills.svg`, a faint grid of capsules;
  hero links are underlined with a row of pink dots. **[observed; CSS]**
- Calls to action: two white boxes with a 1 px pink outline, each opening with a bold pink
  run-in ("Don't miss a thing.", "Help us help you change the world."); buttons filled
  pink with a navy outline and two white outlined layers offset 3 px and 6 px behind; the
  email field has a dotted tan shadow block. **[observed; CSS]**
- Story lines: under a story, a 20 px pink icon, a bold pink label and an underlined link
  ("Related:", "Original Investigation:", "Resource:"). **[observed]**
- Images: 16:9 photographs and illustrations, square corners, full article width; the
  "Inside The Markup" list uses small thumbnails at 2 of 12 columns. **[observed]**
- Phone (<42em): one column; the dotted connector runs along the right of the section
  text down to a downward arrowhead; after the first story, thumbnails float right at a
  third of the width, with tan hairlines between stories; hero 30 px. **[observed; CSS]**

## Moves across the pages

Each move: how it is built, the pages that show it, the pages that do not, and the default
it replaces.

1. **Paragraphs separated by a first-line indent, not by space.** Every paragraph after
   the first indents about 2 em and sits directly under the one before. Shown: P3, P4, P5,
   P6, P9 (5 of 11). P2's CSS applies the same rule to posts, but its paragraphs on screen
   are separated by images, so it was not seen there. Not shown: P10 (paragraphs spaced
   0.75 × base apart, no indent), P1, P7, P8, P11 (no running text of more than one
   paragraph). Default: block paragraphs with a blank line between. **[observed]**
2. **An opening run-in.** The first words of a text are set apart in the line: spaced
   small capitals (P6, P9), a small-capital newspaper dateline (P5), or bold (P4, and the
   "Now available in print!" line on P7), or bold in the accent colour (the call-to-action
   boxes on P11: "Don't miss a thing."). Shown: P4, P5, P6, P7, P9, P11 (6 of 11). Not
   shown: P1, P2, P3 (v7 posts begin plain), P8, P10 (the About text opens plainly).
   Default: a plain first paragraph, or a large drop cap or "lede" paragraph in a bigger
   size. **[observed]**
3. **Colour that is not fixed per site.** v7 derives each page's accent from its date and
   tints its greys to the complementary hue (P1, P2, P3: magenta, coral, blue). v6 picks
   one of five schemes at random on each load (P5). Robtober 2024 has its own palette for
   its theme (P4). Not shown: P6, P9, P11 (one fixed palette), P7, P8, P10 (black, white
   and grey only; P10 swaps panel and text greys with the system's light or dark mode).
   Default: one fixed brand palette. **[observed]**
4. **One saturated accent used only for thin things.** Where a page has an accent, it is
   used for link underlines, 1–2 px rules, outlines and one or two small filled blocks,
   not for large areas. Shown: P1, P2, P3 (accent on underlines, rules, chip outlines,
   sidebar header), P4 (rules, heading, underlines, toggle), P5 (meta, underlines, list
   markers, a 6 px stripe on phone). Not shown: P6, P7, P8, P10 (no accent), P9 (several
   colours: navy, brick, orange, peach, lavender, maroon tabs), P11 (pink fills the
   call-to-action buttons and sets the 21 px bold section labels). Default: an accent used
   for buttons and large fills. **[observed]**
5. **Rules carry the structure.** Hairline or heavy rules divide rows, sections and
   footers instead of boxes or shadows. Shown: P1, P2, P3 (1 px accent rules between every
   card row and footer row), P5 (3 px and hairline rules), P6 (8 px rule under the H1, 2 px
   before the meta), P9 (2 px under titles, dashed and vertical rules), P4 (orange rules
   between sections), P11 (a 12 px dotted halftone band opens each section, tan hairlines
   between stories, dotted connector lines). Not shown: P7 (thick frames around covers),
   P8 (1 px boxes), P10 (no rule; a filled grey panel, with space and bold sub-heads
   between sections). Default: cards with fills, radii and shadows. **[observed]**
6. **Hanging list markers.** Bullets and numerals sit outside the text edge so the text
   stays aligned. Shown: P5, P6 (2 pages; the only pages with lists). Not seen elsewhere
   because no other page, P10 and P11 included, had a list. Default: markers indented inside the text column.
   **[observed]**
7. **Big text that is not heavy.** Large type is set at regular or lighter weights. Shown:
   P1, P3 (39 px intro and subtitles at weight 225, by the v7 rule that weight falls as
   size rises), P5 (45 px headline at 400), P7 (28 px intro at 400), P8 (72 px title at
   400), P10 (45 px title at 400). Not shown: P1–P3 H1s (700), P6 (48 px at 900), P11
   (36 px hero sentence at 700). Default: big headlines in bold. **[observed]**
8. **One type family per site.** Shown: P1–P3 (Degular only), P4 (HEX Franklin, plus the
   lettered title), P7 (Gimlet only), P8 (system-ui only), P10 (Archivo only). Not shown:
   P5 (Freight Text and Ciutadella), P6 (a slab and Minion in its CSS), P9 (Georgia, a sans
   and blackletter lettering), P11 (Ivar serif and Messina sans; no source says whether he
   or The Markup chose them). Default: a display face paired with a text face.
   **[observed]**
9. **A structural element that leaves the column or the grid.** The Robtober posters run
   wider than the text measure (P4: 1213 px against 805 px); a video floats into the text
   column with text wrapping beside it (P3); the sticky prev/next control rides over the
   text (P3). Shown: P3, P4. Not shown: the other 9 (P10's photo floats inside the text
   column). Default: everything inside one container width. **[observed]**
10. **Line weights and angles taken from a letterform or the logo.** v7 sets every border
    to the stroke width of 16 px Degular at weight 400 (`--borderWidth`, CSS comment). The
    PhilaMOCA theme sets its divider and ticket-button borders to the logo's stroke
    (`--logo-line`) and skews them to the logo's slant (`--logo-slant: -11.69deg`); the
    header's hatched fade on P10 is drawn at about the same slant. Shown: P1, P2, P3, P10
    (in the CSS; on P10 only the hatching is visible, the slanted dividers are on the
    events pages). Not shown or not determinable: the other 7. Default: 1 px borders and
    unrelated angles. **[observed in CSS and P10 header]**

## What changes from project to project

- Typeface and palette change with every version of the personal site: blackletter
  wordmark, Georgia and ornament in v4 (P9); slab and serif on a striped ground in v5 (P6);
  Ciutadella and Freight with random schemes in v6 (P5); Degular with a date-derived
  accent in v7 (P1–P3). **[observed]**
- The art projects drop colour and decoration: Plus Equals and Cubes Revisited are black,
  white and grey, one plain family, and let the generated artwork be the only imagery
  (P7, P8). **[observed]**
- Robtober takes its look from the year's theme; the project page lists a VHS homage
  (2021), a ransom-note title (2022), a title that smashes into glass (2023) and a flaming
  title with responsive lettering (2024). P4 shows the 2024 one: full-viewport lettered
  title, horror-poster palette, poster grid. **[observed P4; stated for the other years,
  robweychert.com/projects/robtober/]**
- Grid depth changes with the amount of content: a 12-column grid with sidebar on v7
  (P1–P3), a single centred measure on Robtober (P4), a single offset column on v5 and v6
  (P5, P6), a fixed four-across cover grid on Plus Equals (P7), three fixed columns on v4
  (P9). **[observed]**
- Phone handling grew over time: none on v4 (P9, fixed 725 px); centred stacking on v5 (P6)
  and Cubes (P8); a top-bar navigation and nearly unchanged H1 size on v6 (P5); a 6-column
  grid, smaller scale and a floating sidebar button on v7 (P1–P3); a re-drawn title shape
  on Robtober 2024 (P4). **[observed]**
- What the two client pages keep from his own sites, and what they do not:
  - PhilaMOCA (P10), where he did the branding too, keeps: one family; a large title at a
    regular weight (45 px at 400); a fluid type scale with few sizes (v7 also scales its
    base with the viewport, 18–22 px; P10 16–24 px); line weights and angles taken from
    the mark; colour that follows the system's light or dark mode, as v7 does. It drops:
    the indented paragraphs (spaced instead), the run-in, any accent (greyscale, after the
    venue's "high-contrast black and white" identity), and rules on the page. **[observed;
    stated for the identity, robweychert.com/projects/philamoca/]**
  - The Markup (P11), inside the host's existing site, keeps: rules and dotted bands as
    section structure, a label column beside the stories, a bold run-in in the calls to
    action, a fixed accent. It drops: one family (Ivar and Messina), large text at light
    weights (hero 36 px at 700), the accent kept to thin things (pink fills buttons and sets
    large labels), and indented paragraphs. Whether the typefaces, colours and stacked
    button were The Markup's before him is not stated. **[observed]**

## Line length and scale, for reference

| Page | Body size / leading | Characters per line (desktop) | Largest text : body      |
|------|---------------------|-------------------------------|--------------------------|
| P1   | 22 / 31.9           | (no running text)             | 3.16                     |
| P2   | 22 / 31.9           | 84–86                         | 3.16                     |
| P3   | 22 / 31.9           | 68; 43–45 beside the float    | 3.16                     |
| P4   | 23.6 / 35.4         | 48–57                         | 1 (lettered title aside) |
| P5   | 20 / 30             | 66–78                         | 2.25                     |
| P6   | 18 / 24             | 52–72                         | 2.67                     |
| P7   | 18 / 28             | (short lines)                 | 1.56                     |
| P8   | 18 / 27             | (short lines)                 | 4                        |
| P9   | about 15 / 21       | about 60–65 (from screenshot) | about 1.5                |
| P10  | 24 / 33.6           | about 70 (60ch cap)           | 1.875                    |
| P11  | 16 / 24             | (short story texts)           | 2.25                     |

## Looked for and not found

- A résumé: the "Here's my résumé →" link on https://robweychert.com/about/ returned the
  site's 404 page on 2026-11-24.
- Plus Equals issue pages (/01/, /04/, /07/) are 10,500–15,700 px tall at desktop; not
  studied, so the zine's article layout is not in these notes.
- The ProPublica article "Inside ProPublica's Article Layout Framework" on propublica.org
  is about 15,100 px tall at desktop; not studied. The one studied page inside a host's
  site is P11.
- shop.robweychert.com is a Shopify store whose responses send `X-Frame-Options: DENY`,
  so it could not be laid at exact widths; not studied.
- Robtober 2021 and 2022 report a 835 px document height (their content scrolls inside an
  element); not studied.
- Solid Product Design (branding) and the conference title sequences have no live page
  showing the work beyond his project pages; not studied.
- v7 light mode, which the CSS makes the default, was not seen (browser in dark mode).
- P6's intended typefaces (Typekit) did not load.
- P10 and P11 were measured from screenshots and CSS fetched with `curl`, not from the
  rendered page; sizes are computed from the CSS at 1440 and 390 px.
- PhilaMOCA's light mode and its events home page (about 18,000 px tall at desktop) were
  not seen; the events styles (slanted dividers, ticket buttons) are known only from CSS.
- No source says whether The Markup's typefaces, colours and stacked buttons predate his
  homepage; his project page says only that the header, footer, icons and final copy were
  theirs.
- Hover and other interaction states were read from CSS (0.2 s colour transitions, a
  pulse highlight on a targeted sidebar, view transitions) rather than exercised.
