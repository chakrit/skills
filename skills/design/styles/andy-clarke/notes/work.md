# Andy Clarke: work notes

Stream: `work`. Pages the designer designed, studied in a browser on 2026-11-24 at
1440 px (desktop) and 390 px (phone). Numbers come from the rendered pages
(`getComputedStyle` and element boxes) read after looking at full-page screenshots.
Every finding in this file is **observed in the work**; the URL in each heading or
citation is the page that shows it. Nothing here is stated by the designer or
reported by others, and nothing comes from memory.

Page numbers (P1 to P14) are used for citation below.

## Sources

| #   | URL                                                                     | Date seen  | What it is                                                         |
|-----|-------------------------------------------------------------------------|------------|--------------------------------------------------------------------|
| P1  | https://stuffandnonsense.co.uk/                                         | 2026-11-24 | His studio site, home page                                         |
| P2  | https://stuffandnonsense.co.uk/design/                                  | 2026-11-24 | His portfolio index, about 35 projects                             |
| P3  | https://stuffandnonsense.co.uk/portfolio-lockrose/                      | 2026-11-24 | Case study for the Lockrose site                                   |
| P4  | https://stuffandnonsense.co.uk/blog/project-companion-moonwalk-audio/   | 2026-11-24 | Blog article (dated 1 November 2026) on designing Moonwalk Audio   |
| P5  | https://stuffandnonsense.co.uk/shop/standout-designs-for-the-web/       | 2026-11-24 | Shop product page for his book                                     |
| P6  | https://stuffandnonsense.co.uk/about/                                   | 2026-11-24 | "Why clients choose Andy Clarke" page                              |
| P7  | https://lockrose.com/                                                   | 2026-11-24 | Client home page, energy-infrastructure consultancy                |
| P8  | https://moonwalkaudio.com/                                              | 2026-11-24 | Client home page, game-audio studio                                |
| P9  | https://mountain-duck.netlify.app/                                      | 2026-11-24 | Client home page (Netlify deployment linked from his portfolio)    |
| P10 | https://ryanknaggsmusic.com/                                            | 2026-11-24 | Client home page, film and game composer                           |
| P11 | https://begopereda.com/                                                 | 2026-11-24 | Client home page, composer and producer                            |
| P12 | https://lockrose.com/case-studies/london-power-tunnels-2/               | 2026-11-24 | Client inner page: a Lockrose case study (same site as P7)         |
| P13 | https://codeboxx.co.uk/                                                 | 2026-11-24 | Client home page, printer and ribbon supplier                      |
| P14 | https://sharedhomeland.com/                                             | 2026-11-24 | Client home page, research project on Palestine-Israel             |

Each client page (P7 to P14) carries a footer credit to Stuff & Nonsense ("Design by
Stuff & Nonsense" or "Website design by Stuff & Nonsense"; on P14 a "Design" link to
https://stuffandnonsense.co.uk). P7 to P11, P13 and P14 were found through the project
links on P2's portfolio pages; P12 through P7's navigation.

Set aside for step 8, screenshotted at both widths and not studied (screenshots outside
the repository, in `/tmp/design-research/andy-clarke/set-aside/`):

- https://mikebaugh.co.uk/ (client home page)

https://codeboxx.co.uk/ and then https://sharedhomeland.com/ were the second set-aside
page. Each step 8 review judged that page not to pass as the designer's against the
style folder, so each was moved to the studied pages (P13, then P14) and the notes were
corrected from it.

## Findings by page

### P1. Studio home page (https://stuffandnonsense.co.uk/)

- **Grid.** Content sits on an eight-track grid at x 40 to 1395 (40 px side margins,
  1355 px wide, 30 px gaps) with tracks of 229, 57.25, 171.75, 114.5, 114.5, 171.75,
  57.25 and 229 px, a ratio of 4:1:3:2:2:3:1:4. The header, the H1 band, main, the
  services intro and the footer use it. The four service cards sit on a separate
  12-column grid (85.4 px columns, 30 px gaps); portfolio cards use inner five-column
  grids (229.8 px, 40 px gaps, and 249.8 px, 15 px gaps); the blog list uses two equal
  columns of 662.5 px. Intro paragraphs run x 40, 807 px wide (tracks 1 to 5); the
  "Planning a new website?" call-to-action box sits at x 872, 500 px wide, centred text.
- **Type.** One family, Obviously (variable, `obviously-variable`, axes width and weight,
  200 to 900 loaded). H1 and H2 use width 90, weight 500; H3 width 100, weight 500; body
  width 100, weight 400. Sizes: body 14.4/23.04 px (line height 1.6); H1 72/86.4 px; H2
  43.9 px; H3 22.5 px; small 12.8 and 11 px; small uppercase labels at 12.8 px. H1 to
  body ratio 5.0. Intro paragraphs run about 80 to 85 characters per line, left aligned.
- **Colour.** Whole page on dark navy `oklch(0.284 0.057 269)`. Text pale blue-grey
  `oklch(0.873 0.007 269)`. Links blue `oklch(0.666 0.12 240)`, about a quarter of all
  text characters (1089 of 3886). Buttons filled with a deeper blue
  `oklch(0.559 0.115 241)`. White only in logos and a few labels.
- **Imagery.** A full-bleed SVG illustration, 1440 by 550 px, under the header: a flat
  cartoon desert with mesas, cacti and flowers and a line of seven cartoon outlaws in
  long coats and hats, burgundy, brown and black. Its lower edge is the irregular line
  of flowers and ground, not a straight cut. The four service cards each carry an image
  of lettering (305 by 217 px): a script line over heavy condensed capitals ("Design a
  new / WEBSITE OR PRODUCT"), white on navy; the lettering is an image, not live text.
  Client logos in a white monochrome row. Portfolio cards hold crops of each project's
  illustrations and site screenshots.
- **Composition.** The illustration is the first thing seen and fills the first screen;
  the H1 ("Pioneering web design / that starts with your story") sits left under it, two
  lines. The winged "SN" badge logo sits top left (229 by 89 px), the navigation top
  right with thin vertical dividers. A thin dark banner above everything announces the
  book.
- **Motion.** Nav fades down on load (1 s); clouds drift (240 s loop); spring flowers
  fade in (0.45 s); four small buttons bottom left of the illustration, the first
  labelled "Pause animations"; a hidden "outlaw game" has a close button. 11
  `prefers-reduced-motion` rules in the CSS.
- **Phone.** Side margins 18 px. Logo centred, nav as a three-column grid of six links.
  The hero becomes a separate `<picture>` image 390 by 546 px, a portrait crop with the
  characters larger. H1 48.5/58.2 px in four lines (H1 to body 3.4); body stays 14.4 px,
  about 38 characters per line. The four service cards become a horizontal scroll-snap
  row (cards 288 px, next card visible at the right edge, a progress bar under it).
  Portfolio images in two columns of 145.7 px.

### P2. Portfolio index (https://stuffandnonsense.co.uk/design/)

- **Grid.** Same 4:1:3:2:2:3:1:4 grid. Each project card is a bordered box; the title
  runs x 63, 769 px wide; a client quote sits right (x 872, 500 px, centred, about 54
  characters per line) under a quote glyph; below, a five-column image grid (249.8 px,
  15 px gaps) holds two or three illustration crops and, on the right, a tall crop of the
  site (505 by 1518 px).
- **Type.** Obviously only. H1 72 px **centred** ("Every website tells a different
  story") with a centred line under it; project titles 43.9 px links in blue.
- **Colour.** Same navy page. The project images carry each client's own palette, so
  colour on this page comes from the work: teal and orange (Lockrose), blue-grey and red
  (Moonwalk Audio), blue and yellow (Mountain Duck), teal halftone (Codeboxx), cream,
  teal and orange stripes (Begoña Pereda), red and white (Tristan Jakob-Hoff), rainbow
  gradient (Alessandro Mastroianni) and others.
- **Imagery.** Almost every project shows bespoke illustration in a style of its own:
  flat low-poly landscape (Lockrose), black-outlined toy world (Moonwalk), steampunk
  machine (Mountain Duck), retro tape reels (Begoña Pereda), mid-century geometric
  blocks (Portico), constructivist red poster (Tristan Jakob-Hoff), 1930s cartoon
  adventure (Mike Worth). Two projects are labelled "(spoof)" (Cheeky Condiment Company,
  Rebrand Britain). A few use photography (Ryan Knaggs, Black Mountain Honey). A wall of
  white client logos near the foot.
- **Interaction.** Category filter pills (All, Business, Creative, Entertainment and
  others), small uppercase.
- **Phone.** Doc 38,324 px. Filter pills become a horizontal scroll-snap row. H1 48.5 px
  centred; card content x 39, 306 px wide; quote stacks under the title; images in two
  columns, the tall site crop 296 by 892 px.

### P3. Case study, Lockrose (https://stuffandnonsense.co.uk/portfolio-lockrose/)

- **Grid.** Main column x 40, 807 px (tracks 1 to 5 of the 4:1:3:2:2:3:1:4 grid, ending
  near the page centre); the right sidebar ("Related projects" cards and the
  call-to-action box) in tracks 7 and 8, about 316 px; track 6 left empty.
- **Type.** The H1 contains the client's logo as an SVG (160 by 97 px, white), centred,
  with a centred standfirst under it at 22.5/36 px weight 500. Section H2s at 43.9 px:
  The challenge, My approach, The solution, Behind the design, The result, What this
  project demonstrates. Body 14.4/23.04 px, 78 to 84 characters per line. A pull quote
  at 22.5 px weight 500 in white.
- **Imagery.** A figure on a 2:1 grid (524.7 and 262.3 px): a square 525 by 525 px video
  of the animated illustration with a small caption to its right ("Mid-century
  modernist magazine covers were the inspiration behind my illustrations"). Under it a
  row of eight 122 px thumbnails (gallery navigation, 10 px gaps). A full-column image
  807 by 415 px shows the five-stage process illustration from the client site.
- **Other.** Client, Sector, Duration and "What I did" as a two-column list with small
  uppercase labels; a "Visit Lockrose's website" button; a bordered "Related reading"
  box; a bordered, centred "Looking for something similar?" box.
- **Phone.** One column, 18 px margins; logo and standfirst centred; the thumbnail row
  scrolls; the sidebar's related projects move below the article as a horizontal
  scroll-snap carousel with a progress bar.

### P4. Article (https://stuffandnonsense.co.uk/blog/project-companion-moonwalk-audio/)

- **Grid.** Main column x 40, 807 px (tracks 1 to 5); sidebar x 1079, 316 px (tracks 7
  and 8): a boxed book promotion with the book's lettering, a short bio, links, then a
  "Planning a new website?" box that stays in view while the page scrolls, then "You may
  also like" links. Track 6 empty.
- **Type.** H1 68.7/82.4 px, left, set in five short lines; headings use
  `text-wrap: balance`. H2s 43.9 px. Body 14.4/23.04 px, 73 to 85 characters per line.
- **Imagery.** Five images at the full main-column width (807 px, 395 to 452 px tall),
  without captions, in the order of making: a photograph of real objects (pencils, a tin
  robot, a plastic dragon, toy soldiers, a toy UFO); the same objects as black-and-white
  line drawings; the finished navy and grey illustration (castle, Godzilla, robot); the
  astronaut-with-a-microphone-head mascot in three poses; a final scene.
- **Other.** A bordered aside pointing to the portfolio page; a webmention box; at the
  foot a horizontal carousel of shop cards, each with hand-drawn or condensed product
  lettering (Standout Designs for the Web, Art Direction for the Web, Hardboiled Web
  Design, Contract Killer, Layout, Eleventy in a Box), with a progress bar.
- **Motion.** Nav fade-down (1 s); the "open" sign in the footer wobbles (2.5 s). 6
  reduced-motion rules.
- **Phone.** H1 48.5 px in eight lines; images 349 px wide; sidebar content follows the
  article; shop cards scroll horizontally with mandatory snap.

### P5. Shop product page (https://stuffandnonsense.co.uk/shop/standout-designs-for-the-web/)

- **Colour.** The page is re-themed away from the site's navy: page background
  `rgb(23, 20, 31)` (near-black violet), buttons burgundy `rgb(144, 36, 63)`, the author
  link and labels tan `rgb(205, 178, 150)`. Same typeface and grid.
- **Imagery.** Full-bleed painted comic illustration, 1440 by 654 px: a hard-boiled
  detective throwing a punch, a woman in a red hat, a red-haired man flung backwards,
  flying chairs, hanging lamps, purple shadow. The flung man's hand extends **below the
  hero's bottom edge** into the content band. The title is lettering inside the
  illustration at left: script "Andy Clarke's", heavy condensed white capitals
  "STANDOUT DESIGNS FOR THE WEB", script "Hardboiled Web Design Shot".
- **Grid.** Under the hero, on the 4:1:3:2:2:3:1:4 grid: book cover in track 1 (229 by
  324 px); a small uppercase label, a 22.5 px standfirst and body (x 386, 663 px, about 66
  characters per line) in tracks 3 to 6; price and "Buy now" in tracks 7 and 8. Four
  feature columns on the 12-column grid (H3 28 px). "Look inside": a four-by-two grid of
  page spreads (306 px, 30 px gaps) that open in a spread viewer. Chapters as a
  disclosure list (x 386, 663 px). Four reader quotes in four columns. Author photo.
- **Phone.** Hero becomes a 390 by 354 px crop with the lettering still readable;
  spreads in two columns; everything else stacked.

### P6. About page (https://stuffandnonsense.co.uk/about/)

- **Colour.** Re-themed again: body background `rgb(22, 29, 26)` (very dark green),
  buttons and links sage `rgb(142, 164, 155)`.
- **Imagery.** Full-bleed illustration: inside a sheriff's office, a large cartoon
  sheriff in the left foreground cut off by the bottom edge, the outlaw gang lined up at
  right, WANTED posters on the wall; desaturated green-grey with burgundy coats. Pause
  controls bottom left.
- **Grid and type.** H1 72 px left, one line. Main column tracks 1 to 5, call-to-action
  box in tracks 7 and 8. Testimonials in a two-by-two block inside the main column (a
  12-column subgrid of 39.75 px). "Life and work" is a centred H2 over a vertical
  timeline: a central line, year markers, entries alternating left and right, inside a
  fixed-height box that scrolls.
- **Phone.** The hero is a portrait crop showing the gang. The timeline becomes a
  horizontal scroll-snap list, one year per screen. H2s break into short lines.

### P7. Lockrose (https://lockrose.com/)

- **Grid.** The same 4:1:3:2:2:3:1:4 ratio (230, 57.5, 172.5, 115, 115, 172.5, 57.5, 230
  px; 30 px gaps; x 37 to 40, 1354 to 1360 px wide). The hero band uses the same ratio
  across the full 1440 px with no gaps (288, 72, 216, 144, 144, 216, 72, 288 px), so the
  illustration (864 by 749 px, starting x 573) runs to the right edge of the window.
  Stats and the sector cards use a 12-column grid.
- **Type.** One family, Commissioner (variable). Headings **uppercase at light weights**:
  H1 57.6/57.6 px (line height 1.0) weight 300; H2 39 px weight 200; H3 20 px weight 300.
  Body 16/24 px at weight 200. Bold uppercase lead-ins at 16 px weight 500. H1 to body
  3.6. H1 set in five short lines at left ("GUIDING COMPLEX / PROJECTS / THROUGH / THE
  REALITIES / OF DELIVERY").
- **Colour.** Page mint-white `rgb(243, 249, 246)`; hero and stats band dark teal
  `rgb(0, 58, 59)` (the largest coloured area); text teal `rgb(0, 73, 74)`; orange
  `rgb(255, 119, 0)` for the logo, primary buttons, the active tab underline and the
  borders of "Client story" boxes.
- **Imagery.** Flat, low-poly landscape: pylons, wind turbines, a dam, a nuclear plant
  with a glowing dome, solar panels; teal, grey, white and orange. A grey line-drawing
  panorama (1354 by 365 px) under five process tabs. Four sector illustrations in the
  same style, separated by thin vertical rules.
- **Motion.** Turbine blades rotate (10 s); the nuclear dome pulses (4.8 s). 7
  reduced-motion rules, 1 scroll-timeline rule. The process tabs change the panorama.
- **Phone.** The illustration moves **above** the H1 (390 by 338 px). H1 35.5/35.5 px;
  body 14.1/21.1 px, about 41 characters per line. Stats stack centred; tabs wrap.

### P8. Moonwalk Audio (https://moonwalkaudio.com/)

- **Grid.** The same 4:1:3:2:2:3:1:4 grid for content (x 40, 1354 px, 30 px gaps);
  12-column grid (76.2 px, 40 px gaps) for project cards. The navigation is a grid of
  590, 220 and 590 px: the logo in the middle and three pill links on each side,
  **staggered** in a zigzag rather than in a straight row.
- **Type.** One family, Alexandria: weight 300 for body and lead, weight 900 uppercase
  for headings. H1 72/72 px (line height 1.0); H2 35 px; H3 28 px; testimonial text
  22.5 px weight 300; body 18/27 px. H1 to body 4.0.
- **Colour.** Dark slate `oklch(0.258 0.030 259)`; text `oklch(0.88)`; red
  `oklch(0.51 0.198 18)` for the logo disc, buttons, rules and carousel arrows;
  slate-blue nav pills.
- **Imagery.** Full-bleed illustration, 1440 by 833 px, built from at least eight
  layered SVGs: a blue-grey world of oversized pencils and brushes, a tin robot, a
  castle, Godzilla, toy soldiers, a UFO, fan-shaped trees; the one white figure is an
  astronaut whose head is a microphone, the mascot. Heavy black outlines, flat tones.
  This is the illustration whose making P4 shows.
- **Motion and sound.** About 90 twinkling stars (7.7 to 13.9 s loops); pencils, pens and
  shavings sway (10 to 12 s). Objects play sound when pressed ("Press something to play
  audio"), with "Mute all banner audio" and "Sounds on" controls. Each of eight project
  cards has a play-audio button. 11 reduced-motion rules, 2 scroll-timeline rules.
- **Other.** Testimonials in a horizontal scroller, each quote framed by giant tan curly
  braces. A footer where the mascot peeks over a rule above "TELL US ABOUT THE WORLD
  YOU'RE BUILDING".
- **Phone.** The illustration shrinks to a boxed 348 by 201 px crop inside the margins
  (no longer full bleed); nav becomes a two-column grid of pills; H1 35.5 px; body
  14.1 px, about 44 characters per line; the braces turn horizontal above each quote;
  testimonials scroll-snap; the project cards stack over one another as the page
  scrolls, their top edges visible as a pile.

### P9. Mountain Duck (https://mountain-duck.netlify.app/)

- **Grid.** An eight-track grid with a **different** ratio, 2:1:1:2:2:1:1:2 (191.2,
  95.6, 95.6, 191.2, 191.2, 95.6, 95.6, 191.2 px; 30 px gaps) for header, hero and
  footer; 12 columns for features; a six-column horizontal scroller for testimonials.
- **Type.** One family, Zalando Sans SemiExpanded: weight 300 body, 500 lead and labels,
  900 headings in sentence case. H1 is the wordmark "MOUNTAIN / DUCK" 48.8/63.5 px
  weight 900, under the duck app icon. Lead 25/40 px weight 500; body 16/25.6 px. H1 to
  body 3.05.
- **Colour.** Near-black violet `oklch(0.19 0.027 277)`; text `oklch(0.92)`; yellow
  `oklch(0.834 0.169 91)` for nav links, buttons and inline links (the duck's colour);
  blue rounded frames around product screenshots; thin orange rules.
- **Imagery.** To the right of the hero text (x 499, 900 px wide): a steampunk
  file-processing machine with boilers, gauges, pipes topped with cloud-service icons, a
  conveyor of DOC, PDF and CSV file tiles, files floating up into a cloud; steel blue
  with brass-yellow accents.
- **Motion.** About 40 cogs turning, some counter-rotating (14 to 24 s); files run along
  the conveyor (7.8 to 8.2 s); pipes glow (9 s); bubbles rise (about 5 s). 7
  reduced-motion rules, 2 scroll-timeline rules.
- **Phone.** Margins 27 px; the illustration moves above the wordmark (333 by 280 px);
  H1 35.2 px; body 14.1 px, about 40 characters per line.

### P10. Ryan Knaggs Music (https://ryanknaggsmusic.com/)

- **Grid.** 12 columns only (85.3 px, 30 px gaps, x 40, 1354 px); no compound grid
  found. Hero: left four columns (x 40, 431 px) hold the logo lockup, nav, H1 and intro;
  right eight columns (x 501, 893 px) a full-height panel.
- **Type.** **Two** families: Delirium, a tall ultra-condensed display face, for the
  logo, nav, all headings and the pull quote (H1 72/72 px, H2 55 px, H3 44 px); Fira
  Sans Condensed Light for body (14.4/23.04 px) and lead (18/28.8 px). H1 to body 5.0.
- **Colour.** Near-black `rgb(2, 3, 7)`; text `rgb(228, 229, 231)`; electric blue
  `rgb(41, 91, 190)` for links, logo, rules and play buttons; the footer fades into a
  navy glow.
- **Imagery.** **Photography, not illustration**: a blue duotone photograph of the
  composer from behind at his desk facing a screen of a galaxy, vignetted into the black
  page, with a centred play button and the track title laid over its lower left. Under
  it a strip of eight numbered cue blocks stepping in colour from green to blue to navy
  to black (2 px gaps). Project cards use game art; demo reels use duotone portraits.
- **Motion.** 2 CSS animations, 4 scroll-timeline rules, 4 reduced-motion rules; an
  audio cue player.
- **Phone.** Margins 27 px; H1 35.5 px; the photograph becomes a 330 by 247 px vignetted
  crop; everything stacks.

### P11. Begoña Pereda (https://begopereda.com/)

- **Grid.** The 2:1:1:2:2:1:1:2 ratio again (204, 102, 102, 204, 204, 102, 102, 204 px,
  30 px gaps), across the full width with no outer margin. Left four units: a sidebar.
  Right (x 497, 935 px): illustration and content.
- **Type.** Fido, an irregular, hand-cut-looking display face, for the logo, nav,
  headings **and body copy** (18/27 px, centred, about 36 characters per line); Archivo
  only inside the audio player. H1 (logo) 55 px uppercase with jostled letters; H2 44
  px uppercase, centred, one or two words per line ("WHAT / DO I / DO?"); H3 28 px. H1 to
  body 3.05.
- **Colour.** **Light page** `oklch(0.963 0.009 232)`; deep petrol blue for type; a
  petrol-blue panel behind the service blocks; a five-colour set of vertical bars:
  green, sage, mustard, near-black and vermilion.
- **Imagery and composition.** The five bars stand above the nav, then continue below
  the intro down the full height of the left column; at the foot of the page they bend
  through a rounded 90-degree corner and run horizontally to the right edge under the
  footer, like racing stripes. To the right, a flat 1970s-style reel-to-reel tape
  machine, 935 by 880 px, its reels cut off by the top and right edges of the window.
- **Motion and sound.** Reels spin (9 s), tape transfers (60 s), knobs turn, the counter
  blinks; numbered buttons 1 to 6 under the machine play audio. 2 reduced-motion rules.
- **Phone.** The stripes shrink to a five-swatch block above the nav and above the
  footer logo; the machine sits under the intro (382 by 360 px, cut at the right);
  headings move to left alignment at 29.5 px.

### P12. Lockrose case study (https://lockrose.com/case-studies/london-power-tunnels-2/)

The browser window could not be widened past 1054 px in this pass, so the desktop numbers
were read inside a 1440 px wide frame laid over the page, and the desktop screenshot is
a scaled copy of that frame.

- **Grid.** The same 4:1:3:2:2:3:1:4 grid as P7 (229, 57, 172, 114, 114, 172, 57, 229 px;
  30 px gaps; x 40, 1354 px). The article runs in tracks 1 to 5 (x 40, 806 px wide); a
  sidebar sits in tracks 7 and 8 (from about x 1078): Categories, "The result", "What
  changed" as a list with small triangle bullets, and two links to the other client
  stories in orange capitals. Track 6 stays empty. This is the same column-and-sidebar
  split as his own case study and article (P3, P4).
- **Type.** Commissioner only, as on P7: H1 57.6/57.6 px weight 300 uppercase, in three
  lines; H2 31.2/37.5 px weight 200 uppercase; H3 20/24 px weight 300 uppercase; body
  16/24 px weight 200, 91 to 103 characters per line in the 806 px column. A small
  uppercase label above the H1 ("NATIONAL GRID ▲ 2026"). H1 to body 3.6.
- **Colour.** Mint-white page `rgb(243, 249, 246)`, teal text `rgb(0, 73, 74)`, orange
  `rgb(255, 119, 0)` for the label triangle, sidebar links and the footer button. No dark
  hero band: the dark teal of P7's hero does not appear.
- **Imagery.** **A photograph, not illustration**: one documentary photograph of the
  cable tunnel with workers and cable runs, 806 by 454 px, at the top of the article
  column above the H1, inside the margins. No illustration on the page; the footer
  carries only the logo.
- **Other.** A key-facts table under the intro (figures such as "£1BN INVESTMENT",
  "8-YEAR PROGRAMME", "30KM OF CABLE TUNNELS" in uppercase at left, a description at
  right, thin teal rules between rows). Sections: The challenge, Key considerations, Our
  approach, each with uppercase H3 sub-heads.
- **Motion.** No CSS animations; 6 reduced-motion rules and 1 scroll-timeline rule.
- **Phone.** Margins 18 px; the photograph 348 by 196 px, still above the H1; H1
  35.5/35.5 px in four lines; body 14.1/21.1 px, about 50 characters per line; the
  key-facts table keeps two columns with a narrow description column; the sidebar
  follows the article.

### P13. Codeboxx (https://codeboxx.co.uk/)

Studied without the browser: from full-size screenshots taken earlier at 1440 px (each
viewport as two overlapping 1054 px halves) and at 390 px, and from the page's HTML and
its stylesheet https://codeboxx.co.uk/css/critical.css, fetched with `curl`. Positions
come from the screenshots; sizes marked "from the CSS" are the stylesheet's `clamp()`
values worked out for the width named, not read from a rendered page.

- **Grid.** The stylesheet holds two templates: `--grid-4-5: 2fr 1fr 1fr 2fr 2fr 1fr 1fr
  2fr` (the 2:1:1:2:2:1:1:2 ratio, no named lines, the same name and value as P9) and
  `--grid-12-col: repeat(12, 1fr)`. `.layout` uses `--grid-4-5` inside
  `@media screen and (width>=64em)`; the `vilnius`, `vienna` and `valletta` layouts
  switch to 12 columns. Which sections use which:
  - Header (`warsaw` on the eight tracks): logo `grid-column: 1/3`, navigation
    `4/-1`.
  - Hero (`main`, `vilnius` on 12 columns): portrait `2/7`, text `8/12`. In the
    screenshot the portrait spans about x 155 to 700 and the text starts at about
    x 848, so the hero reads as two halves.
  - "Direct access to leading products": a flex row, heading and button left, four
    product boxes right.
  - Three feature columns (`vienna` on 12 columns, `span 4` each): equal thirds, with
    thin teal vertical rules between them.
  - FAQ (`brussels` on the eight tracks): `grid-column: 2/8`, a centred column from about
    x 260 to 1175.
  - Footer (`athens` on the eight tracks): links `1/7`, logo `8`.
  So the eight-track grid is in the CSS and sets the header, the FAQ column and the
  footer; the hero and the feature row sit on 12 columns.
- **Type.** One family, Space Grotesk (Google Fonts, weights 300 to 700). From the CSS:
  H1 `--font-size-3xl`, which is 61 px at 1440 px, line height 1.1 (line pitch about
  67 px in the screenshot), weight token 800; lede paragraph (`.alt-lede`) 20 px weight
  500; body paragraphs `--font-size-s`, 16 px; H2 `--font-size-2xl`; H3 `--font-size-l`.
  H1 to body about 3.8. Headings in sentence case, `text-wrap: balance`. H1 in four
  lines at right of the portrait.
- **Colour.** Ground `--color-background-default: oklch(13.07% .0033 325.76)`, a
  near-black. Text `oklch(92.17% .0029 264.54)`. Brand teal `#2db7b8` for the portrait,
  logo, links, buttons, rules and FAQ dividers; accent orange `#fe5d26` for the active
  numbered button, the small ring separators in the navigation, link hover and link
  underline. A secondary button in slate `oklch(45.74% .0442 212.89)`. The four product
  boxes carry their own fills (`#612e6c`, `#2d864b`, `#263974`, `#047296`).
- **Imagery.** The hero is one portrait at a time, about 545 by 610 px, built from
  small teal squares with QR-code finder squares in three corners. Five numbered
  buttons under it switch the portrait. Their labels in the HTML are "Show Van Gogh
  portrait", "Show The Scream", "Show Mona Lisa", "Show Marilyn" and "Show Girl with a
  Pearl Earring". The portrait sits inside the margins in the left half; it reaches no
  edge of the window, and it is not a scene with characters. The four product boxes,
  labelled Markem-Imaje, Domino, ICE and Videojet, are the same isometric box. In the
  HTML each SVG has the same path data and only the fill colour changes. Each carries
  the Codeboxx mark on its face.
- **Composition.** First screen: portrait left, H1, lede, paragraph and two buttons
  right. After it, the product row with a teal rule under its heading, the three
  feature columns, then ten FAQ items as `<details>` elements. `faqs.css` styles only
  their bottom border, padding and summary font, so the browser's default triangle
  marker shows. In the desktop screenshots the FAQ runs from about y 1470 to 2215 of a
  2461 px page, about 30 percent of its height. The footer has links and a teal rule
  left, logo right.
- **Motion.** Keyframes `logo-teal-shift`, `footer-logomark-bounce`, `product-fade-in`
  and `product-fade-out` (the portrait switch); product boxes lift 5 px on hover. No
  ambient loops in the hero. Six `prefers-reduced-motion` mentions in the CSS.
- **Phone.** Margins 18 px. Logo, then navigation as a two-by-two grid of links; the
  portrait at full content width, then the numbered buttons, then the H1 (about 40 px
  from the CSS), lede, paragraph and centred buttons. The portrait comes before the H1
  in the HTML, so this is the source order, not a reordering. The product boxes become a
  two-by-two grid; the feature columns, FAQ and footer stack. No horizontal scroller.

### P14. The Shared Homeland Paradigm (https://sharedhomeland.com/)

Studied without the browser, the same way as P13: from full-size screenshots taken
earlier at 1440 px (each viewport one whole 1440 by 835 px frame) and at 390 px, and from
the page's HTML and its one stylesheet https://sharedhomeland.com/css/critical.css,
fetched with `curl`. Positions come from the screenshots; sizes marked "from the CSS"
are the stylesheet's `clamp()` values worked out for the width named.

- **Grid.** No eight-track template in the stylesheet: the only named template is
  `--grid-12-col: repeat(12, 1fr)`, used by `.layout` and the footer. The hero
  (`data-layout="chugga-boom"`) is `grid-template-columns: 1fr 1.5fr 1fr`, three unequal
  but mirrored columns: navigation across all three in the first row (padded in by
  `padding-inline: 20vw`), then the logo, standfirst, paragraph and links in the middle
  column, and the two blocks of rectangles in the outer columns. In the screenshot the
  middle column runs from about x 431 to 1003. The hero is pulled out to the window
  edges with negative inline margins. Below it, two sections (`data-layout="flex"
  data-border="r"`) each hold three equal columns divided by 1 px vertical rules
  (`[data-border="r"] > *:not(:last-of-type) { border-inline-end: ... }`), from x 40 to
  about 1394. A "Highlights" block of posts is in the HTML but commented out.
- **Type.** One family in the stylesheet, Bankside Sans VF, set through custom
  properties that pair weight and width: headings `--font-bold-condensed`
  (`"wght" 600, "wdth" 80`), body `--font-regular-normal` (`"wght" 400, "wdth" 100`),
  the standfirst `.alt-lede` `--font-regular-condensed`, uppercase. The tall condensed
  title "THE / SHARED HOMELAND / PARADIGM" is not live text: it is an SVG logotype
  (about 280 px wide in the desktop and the phone screenshots); the real H1 is visually
  hidden. H2 `--font-size-xl`; body `--font-size-r`, which is
  `clamp(1rem, 1.1761rem + -0.2273vw, 1.125rem)`: a negative slope, so it is 16 px at
  1440 px and 18 px at 390 px. Smaller text uses `--font-size-s`, about 14.6 px at
  1440 px and about 10.3 px at 390 px.
- **Colour.** Light page `--color-background-default: color(display-p3 0.98 0.977
  0.984)`; text and the inverted section background dark teal `color(display-p3 0.21
  0.368 0.439)`; accent mid teal `color(display-p3 0.32 0.634 0.638)` for the box behind
  "SHARED HOMELAND" in the logo (`.logo-bg { fill: var(--color-accent) }`, overriding
  the SVG's own `#d6845c`), buttons and link hover; a cream `--color-base` and a grey
  border colour. The hero's rectangles add cyan and pale grey. No warm accent shows.
- **Imagery.** The hero background is a raster map texture (`img-index-1.webp`,
  `background-size: cover`) in dark teal. In the outer columns, two raster images
  (`img-index-2.webp`, `img-index-3.webp`) of overlapping flat rectangles in teal, cyan
  and pale grey, laid over the map with `mix-blend-mode: screen` and opacity .8. They sit
  in `data-visibility="large"` blocks, which `display: none` hides on small screens. No
  drawn scene, no characters. Partner logos in the footer.
- **Composition.** The hero is centred and mirrored: navigation as three columns of
  links with a rule above each, the logo, an uppercase standfirst and a paragraph in the
  middle, rectangles left and right. Then "Future Scenarios" (an underlined heading
  link, three columns) on the light page, and "From the Alternative Lexicon" in a dark
  teal block with three columns. The footer has a small logo, a long rule, links, a
  "Design" credit and a moon icon for a dark theme.
- **Motion.** `fadeInDown` on the logo (0.5 s delay), view-transition `zoom-in` and
  `zoom-out` keyframes; no ambient loops. Five `prefers-reduced-motion` mentions.
- **Phone.** Margins 18 px. The map stays as the hero background; the rectangles are
  gone. The navigation stays as three columns with wrapped labels. The logo is about the
  same width as on desktop, so it is relatively much larger. Everything stacks. The
  Future Scenarios text is smaller than on desktop and the Lexicon text larger, in line
  with the two size tokens above.

## Moves

A move recurs across the pages and is not what a typical designer or AI model would do
by default. Counts are out of the fourteen pages studied.

### 1. An eight-track compound grid with mirrored ratios

- **Built:** eight tracks whose widths mirror around the centre. The usual one is
  4:1:3:2:2:3:1:4 (for 1355 px of content: 229, 57.25, 171.75, 114.5, 114.5, 171.75,
  57.25, 229 px with 30 px gaps); the other is 2:1:1:2:2:1:1:2. On his own site the
  reading column takes tracks 1 to 5 (807 px, ending about the page centre), track 6
  stays empty, and a sidebar or call-to-action takes tracks 7 and 8 (316 px). On P7 the
  hero repeats the 4:1:3:2:2:3:1:4 ratio across the full window without gaps so the
  illustration meets the window edge. The same pages also use a plain 12-column grid
  for rows of equal cards. P12, a client inner page, uses the same tracks 1 to 5 for the
  article and 7 to 8 for a sidebar, with track 6 empty. How much of a page sits on the
  eight tracks varies: on P13 only the header, the centred FAQ column (tracks 2 to 7)
  and the footer do, while the hero (two halves) and the feature row (three equal
  columns) sit on 12 columns, so the first screen shows no eight-track rhythm.
- **Pages:** 4:1:3:2:2:3:1:4 on P1 to P8 and P12 (9 of 14); 2:1:1:2:2:1:1:2 on P9, P11
  and P13 (3; on P13 only for the header, FAQ column and footer).
- **Not on:** P10 (12 equal columns only); P14 (12 equal columns, and a hero of
  `1fr 1.5fr 1fr`; its stylesheet defines no eight-track template).
- **Default instead:** a 12-column grid of equal columns, or one centred column.
- **In the CSS (observed in the stylesheets, fetched 2026-11-24):**
  - His own site, https://stuffandnonsense.co.uk/css/critical.css (the one site
    stylesheet linked from P1, P3 and P4). The templates are custom properties on
    `:root`, values as written:
    - `--grid-4-5: [a1] 4fr [b2] 1fr [a2] 3fr [b3] 2fr [a3] 2fr [b4] 3fr [a4] 1fr [b5] 4fr [a5]`
      (the 4:1:3:2:2:3:1:4 grid measured on P1 to P6)
    - `--grid-4-6: [a1] 2fr [b2] 1fr [a2] 1fr [b3] 2fr [a3 b4] 2fr [b5] 1fr [a4] 1fr [b6] 2fr [a5]`
      (the 2:1:1:2:2:1:1:2 ratio)
    - `--grid-3-4: [a1] 3fr [a2] 1fr [b2] 2fr [a3] 2fr [b3] 1fr [a4] 3fr [a5]`
      (not seen on any studied page)
    - `--grid-12-col: repeat(12, 1fr)`

    Summing the `fr` values: in `--grid-4-5` the `a` lines fall at 0, 5, 10, 15 and 20
    of 20 (four equal columns) and the `b` lines at 4, 8, 12 and 16 (five equal
    columns). In `--grid-4-6` the `a` lines fall at 0, 3, 6, 9 and 12 of 12 (four
    columns) and the `b` lines at 2, 4, 6, 8 and 10 (six columns). Inside
    `@media screen and (width>=64em)`, `.layout` sets
    `--layout-grid-template: var(--grid-4-5)` and
    `grid-template-columns: var(--layout-grid-template)`; the attributes
    `[data-grid="3-4"]`, `[data-grid="4-5"]` and `[data-grid="4-6"]` swap the template.
    Children are placed by named lines through `data-layout` attributes named after
    cities. The stylesheet has 22 of them, for example `amsterdam` (`a1/a5`) and
    `athens` (first child `a1/b4`, second `a4/a5`). P1 uses `amsterdam`, `athens`,
    `valletta` and `vilnius`; P3 and P4 use `athens`. `a1/b4` ends at 12 of 20, after
    tracks 1 to 5, and `a4` starts at 15, so `athens` gives the 807 px column, the
    empty track 6 and the sidebar in tracks 7 and 8 measured on P3 and P4. Gaps:
    `--grid-column-gap: clamp(1.6875rem, 1.6223rem + .3261vi, 1.875rem)`,
    `--grid-row-gap: clamp(1rem, calc(.89rem + .54vw), 1.31rem)`.
  - Lockrose, https://lockrose.com/css/critical.css (linked from P7). The same
    `--grid-4-5`, `--grid-4-6`, `--grid-3-4` and `--grid-12-col` values as above,
    character for character. It has the same `.layout` rule inside
    `@media screen and (width>=64em)`, the same `[data-grid]` switches and the same
    named-line placements. P7 uses `amsterdam`, `madrid` (`a1/a3`, `b4/a5`), `paris`
    (`a1/b3`, `a3/a5`), `stockholm` (`a1/b4`, `a4/a5`), `tallinn` (`a1/a2`, `b3/a5`)
    and `vilnius`. `.introduction`, the hero band, also takes `grid-template:
    var(--grid-4-5)`.
  - Mountain Duck, https://mountain-duck.netlify.app/css/critical.css (linked from P9).
    The custom property is also called `--grid-4-5`, but its value is
    `2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr`, with the comment `/* 4+6 grid system */` and
    **no named lines**. `[role="banner"]`, `[role="contentinfo"]` and `.layout` (under
    the comment `/* Main layout system */`, inside the
    `@media screen and (min-width: 64em)` block) use
    `grid-template-columns: var(--grid-4-5)`. Children are placed by line numbers, for
    example `[data-layout="edinburgh"] > *:nth-child(1) { grid-column: 1 / 4; }` and
    `nth-child(2) { grid-column: 4 / -1; }`. So the 2:1:1:2:2:1:1:2 grid measured on
    P9 is held under the name the other two sites use for 4:1:3:2:2:3:1:4.
  - Codeboxx, https://codeboxx.co.uk/css/critical.css (P13): the same
    `--grid-4-5: 2fr 1fr 1fr 2fr 2fr 1fr 1fr 2fr` as Mountain Duck, no named lines,
    placed by line numbers (`warsaw` `1/3` and `4/-1`, `brussels` `2/8`, `athens` `1/7`
    and `8`); the hero and feature layouts (`vilnius`, `vienna`) use `--grid-12-col`.
  - Shared Homeland, https://sharedhomeland.com/css/critical.css (P14): only
    `--grid-12-col: repeat(12, 1fr)`; no `--grid-4-5` or other eight-track template.
  - Not fetched: P8, P11 and P12 stylesheets.

### 2. A commissioned illustrated scene as the hero

- **Built:** a full-width or edge-bleeding illustration made for the client, turning
  the business's subject into a scene with characters or a mascot: outlaws in a desert
  (P1), a sheriff's office (P6), a noir fist-fight (P5), a low-poly energy landscape
  (P7), a toy-box world with a microphone-headed astronaut (P8), a steampunk file
  machine (P9), a reel-to-reel tape machine (P11). It meets or crosses at least one edge
  of the window, or its own box: the bottom of P1's scene is a ragged line of ground; a
  hand breaks below P5's hero; P7's and P9's machines and landscapes run to the right
  side; P11's reels are cut by the top and right edges. Each project's illustration
  style differs (flat low-poly, black-outlined cartoon, painted comic, steampunk
  machine, 1970s flat), and its palette is the site's palette.
- **Pages:** P1, P5, P6, P7, P8, P9, P11 (7). P3 shows the same kind of illustration as
  a square video; P2 and P4 show illustrations as content.
- **Not on:** P10, which uses a duotone photograph in the same place; P12, an inner page
  of the same site as P7, which has a documentary photograph at the head of the article
  and no illustration; P13, whose hero image is a single switchable portrait built from
  QR-style squares, boxed inside the margins in the left half, with no characters in a
  scene and no edge of the window reached;
  P14, whose hero is a full-bleed raster map with raster images of flat rectangles in
  the side columns, blended over it; no drawn scene, and the rectangles are hidden on
  the phone.
- **Also on P13:** the other artwork on the page is not a drawn scene either; the four
  product boxes are one isometric box recoloured.
- **Default instead:** a stock photograph, a product screenshot, an abstract gradient or
  a generic vector.

### 3. Small ambient loops inside the illustration, with a way to stop them

- **Built:** separate SVG parts loop slowly and independently: clouds 240 s (P1),
  turbine blades 10 s and a pulsing dome 4.8 s (P7), stars 7.7 to 13.9 s and swaying
  pencils 10 to 12 s (P8), about 40 cogs at 14 to 24 s plus a conveyor at 8 s (P9),
  tape reels 9 s and a 60 s tape transfer (P11). P1 puts a "Pause animations" button
  on the illustration, and P6 shows small control icons in the same place (their
  function was not checked). Every page where the CSS was counted (P1, P4 to P14) has
  `prefers-reduced-motion` rules, 2 to 11 of them.
- **Pages:** P1, P7, P8, P9, P11 (5).
- **Not on:** P2 to P6, which show only a nav fade and a wobbling sign (P6's
  illustration may have loops behind its controls; not checked); P10; P12 (no
  animations); P13 (a logo colour shift, a footer-logo bounce, a fade when the portrait
  is switched, a hover lift on the product boxes; no ambient loops); P14 (a logo fade
  on load and view-transition zooms; no ambient loops).
- **Default instead:** a static hero, or a fade-in-on-scroll effect.

### 4. A characterful display family carries the whole site, body text included

- **Built:** one variable or multi-weight family with personality does every job,
  hierarchy made by weight, width and case: Obviously on P1 to P6 (width 90 and weight
  500 for headings, width 100 and weight 400 for text); Commissioner on P7 and P12
  (uppercase headings at weights 200 to 300, body at 200); Alexandria on P8 (300 and
  900); Zalando Sans SemiExpanded on P9 (300, 500, 900); Fido on P11, including centred
  body copy. P13 also uses one family, Space Grotesk, with sentence-case headings and
  hierarchy by size and weight only (no width axis, no uppercase display setting). P14
  uses one family, Bankside Sans VF, with a width axis: headings at width 80, body at
  width 100; its tall condensed title is an SVG logotype, not a second typeface.
- **Pages:** one family on P1 to P9 and P11 to P14 (13); the display-face settings
  described above (width axis, uppercase light or black weights, a hand-cut face) on P1
  to P9, P11, P12 and P14 (12).
- **Not on:** P10, which pairs Delirium for display with Fira Sans Condensed for text.
- **Default instead:** a neutral sans for everything, or a display face for headings
  paired with a neutral text face.

### 5. Big display type over small text

- **Built:** body 14.4 px on his own site and P10, 16 to 18 px on the others; H1 between
  48.8 and 72 px. H1 to body ratios: 5.0 (P1, P10), 4.8 (P4), 4.0 (P8), 3.8 (P13, from
  the CSS), 3.6 (P7, P12), 3.05 (P9, P11). Client H1s are often set solid (line height
  1.0: P7, P8, P10, P12; 1.1 on P13); his own H1s at 1.2. On phones client H1s drop to
  about 35 to 40 px and his own to 48.5 px; body stays at or near desktop size.
- **Pages:** P1 to P13 (13).
- **Not on:** P14, where the H1 is visually hidden and the visible title is an SVG
  logotype about 280 px wide at both widths (so it does not shrink on the phone), and
  body text sizes move in opposite directions on the phone: `--font-size-r` grows from
  16 to 18 px, `--font-size-s` shrinks from about 14.6 to about 10.3 px.
- **Default instead:** 16 to 18 px body with an H1 two to three times larger.

### 6. Horizontal scroll-snap rows on phones instead of stacking

- **Built:** a row of cards that are side by side on desktop becomes a horizontal,
  snapping scroller on a phone, with the next item visible at the edge and often a
  progress bar under it: service cards (P1), filter pills (P2), thumbnails and related
  projects (P3), shop cards (P4), the life-and-work timeline (P6), testimonials (P8, P9).
  P8 also has a desktop testimonial scroller with previous and next buttons.
- **Pages:** P1, P2, P3, P4, P6, P8, P9 (7). On these pages it is one or two groups
  per page; the other groups stack (for example P1's portfolio cards and blog list,
  P9's feature columns).
- **Not on:** P5, P7, P10, P11, P12, P13, P14 (every group stacks; P13's product boxes
  become a two-by-two grid).
- **Default instead:** stack every item vertically.

### 7. A different image for the phone, or the image moved

- **Built:** the phone gets its own crop through `<picture>` (P1 portrait 390 by 546 px,
  P5 390 by 354 px, P6 portrait crop of the gang), or the illustration moves above the
  headline (P7, P9), or it becomes a boxed crop inside the margins (P8). P11 keeps the
  machine but cuts it at the right edge; its full-height stripes collapse into a
  five-swatch block.
- **Pages:** P1, P5, P6, P7, P8, P9, P11 (7).
- **Not on:** P12, whose photograph is already above the H1 on desktop and is only
  scaled down on the phone; P13, whose portrait stacks above the H1 in source order
  and is scaled to the content width; P14, which keeps the map background and hides the
  rectangle images on the phone rather than recropping or moving them.
- **Default instead:** the same image scaled down, below or behind the headline.

### 8. Hand-made lettering as image, inside or beside the illustration

- **Built:** titles drawn as artwork, usually a script line over heavy condensed
  capitals: the four service cards (P1), the book title inside the hero (P5), product
  cards for books and templates (P4, P5). On client sites the logos are lettered marks
  (Begoña Pereda's jostled letters on P11, Ryan Knaggs's outlined condensed lockup on
  P10, and on P14 a tall condensed SVG logotype with a teal box behind its middle line,
  used in place of a visible H1).
- **Pages:** P1, P4, P5, P10, P11, P14 (6).
- **Not on:** P12 (the Lockrose logo is a plain wordmark; titles are live text); P13
  (titles are live text; the logo is a geometric wordmark with a hexagon mark).
- **Default instead:** live text in the site's heading font.

### 9. Pages of his own site re-themed to their subject

- **Built:** the shop page for a hard-boiled-themed book switches the navy for
  near-black violet with burgundy buttons and tan accents (P5); the about page switches
  to very dark green with sage (P6). Grid, type and header stay the same.
- **Pages:** P5, P6 (2 of his 6 pages); P1 to P4 keep the navy.
- **Default instead:** one colour theme across every page of a site.

## What changes from one project to the next

- **Illustration style and subject** change with the client's business: energy
  infrastructure gets a low-poly landscape of pylons and turbines (P7); a game-audio
  studio a toy-box world with a microphone mascot (P8); file-sync software a machine
  that processes files (P9); a composer a tape machine (P11); his own studio cartoon
  outlaws (P1, P6) and a noir comic for a book (P5). Not every client gets a scene: a
  printer-supplies company gets famous paintings redrawn as QR-style pixel portraits and
  one recoloured product box (P13); a research project on Palestine-Israel gets a map
  texture with abstract rectangles (P14).
- **Palette** comes from the client: teal and orange (P7, P12, P13), slate and red
  (P8), near-black and duck yellow (P9), black and electric blue (P10), pale blue with a
  five-colour 1970s stripe set (P11), teal on teal on a near-white page (P14). Dark
  grounds on 10 of 14 pages; light grounds on P7 (with a dark hero band), P11, P12 (no
  dark band) and P14 (with a dark teal hero and a dark teal section). The darkest grounds are
  near-black: `rgb(2, 3, 7)` on P10 and `oklch(13.07% .0033 325.76)` on P13; the others
  are tinted (navy on P1 to P4, violet-black on P5 and P9, green-black on P6, slate on
  P8).
- **Number of accent colours** (colours beyond ground and text, from the page findings):
  one on P1 to P4 (blue, with red only in the logo badge), P6 (sage), P7 and P12
  (orange); two on P5 (burgundy and tan) and P13 (teal and orange, plus the four
  product-box fills); P8 has red with slate-blue nav pills and tan braces; P9 yellow
  with blue frames and orange rules; P10 blue with a green-to-navy cue strip; P11 a set
  of five stripe colours; P14 one mid teal against dark teal text, with cyan only in the
  hero's rectangle images and no contrasting hue.
- **Typeface** changes every project (Obviously, Commissioner, Alexandria, Zalando Sans
  SemiExpanded, Delirium with Fira Sans Condensed, Fido, Space Grotesk, Bankside Sans
  VF), and so does heading case: uppercase on P7, P8, P10, P11 and P12, sentence case on
  P1 to P6, P9, P13 and P14 (P14's logotype and standfirst are uppercase). Within one
  client site the typeface, case and colours carry over from home page to inner page
  (P7 to P12).
- **Grid ratio**: 4:1:3:2:2:3:1:4 on most; 2:1:1:2:2:1:1:2 on P9, P11 and P13 (P13 only
  for header, FAQ and footer); plain 12 columns on P10 and P14, and for P13's hero and
  feature row. P14's hero is three mirrored columns of `1fr 1.5fr 1fr`.
- **Plain equal-column rows** appear on most pages: two rows of four on P1 (12-column
  `vilnius` with `data-divider="true"`, which draws a 1 px vertical rule between
  columns), four feature columns and four quotes on P5, a two-by-two of testimonials on
  P6, a two-by-two of values and four sector columns with thin vertical rules on P7,
  four-by-two project cards on P8, three feature columns and a two-by-two of
  screenshots on P9, three project cards on P10, a two-by-two of services on P11, three
  feature columns with vertical rules on P13, two rows of three with vertical rules on
  P14 (every section below its hero). Vertical rules between equal columns: P1, P7,
  P13, P14.
- **Disclosure (accordion) lists** appear on two pages, checked in the HTML of all
  fourteen: P5's five chapters and P13's ten FAQs, both `<details class="item-faq">`.
  On P5 his stylesheet hides the browser marker (`.item-faq summary::marker
  {content:""}`) and the summary has its own 8 px marker column; on P13 `faqs.css`
  leaves the browser's default triangle. P13's FAQ fills about 30 percent of the
  desktop page.
- **Sound** appears only on the music and audio clients (P8, P10, P11): pressable
  objects, numbered cue buttons, audio players.
- **Photography instead of illustration** appears on P10, a composer whose site centres
  on his own image and studio, and on P12, where the Lockrose case study leads with a
  documentary photograph of the project while the Lockrose home page (P7) carries the
  illustration.
- **Page kind within a client site**: the one client inner page studied (P12) drops the
  hero band, the illustration and the motion that its home page (P7) has, and takes the
  article-plus-sidebar layout seen on his own case study and article (P3, P4).
- **Alignment**: P11 centres its content and P14 its hero; the others are left aligned
  with centred exceptions (P2's H1, call-to-action boxes, quotes, P13's FAQ column).
- **What stacks on phones**: every page stacks most groups; P1 to P4, P6, P8 and P9
  turn one or two groups into horizontal scrollers (move 6), and P5, P7, P10 to P14
  stack everything.
- **Text size on phones**: on P1 to P13 body text stays at or near its desktop size.
  On P14 the two text sizes move in opposite directions (16 to 18 px and about 14.6 to
  10.3 px), and the SVG title keeps its desktop width.

## Looked for and not found

- A serif typeface: none on any of the fourteen pages.
- Stock photography: none seen; the photography on P10 is of the client, and on P12 of
  the client's project. P13 has no photography. The source of P14's map texture is not
  known.
- Illustration on a client inner page: none on P12. Only one client inner page was
  studied, so whether other inner pages of these sites carry illustration is not known.
- A light theme for his own site: all six pages of stuffandnonsense.co.uk are dark.
- What the scroll-timeline rules on P7 to P10 do: the rules were counted, not tested.
- Reduced-motion behaviour: the rules were counted; the pages were not viewed with
  reduced motion turned on.
- Hover states: not systematically examined.
- The "outlaw game" on P1: its close button was found; the game was not played.
- The production Mountain Duck site: the portfolio links to the Netlify deployment
  (P9), which was studied instead.
