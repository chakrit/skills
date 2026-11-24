# Frank Chimero: work stream notes

Stream: `work` (step 3 of "Adding a designer" in `docs/spec/design.md`). Every page was
opened in a browser on 2026-11-24, in a same-origin frame 1440 px wide (desktop) and
390 px wide (phone), and screenshotted viewport by viewport from top to bottom. Numbers
come from the rendered page (computed styles and element boxes read in the browser);
stylesheets were read only to name a number already seen. Screenshots and raw page text
are kept outside the repository and are not committed.

Claim marks: **[observed]** = seen on the page named; **[stated]** = Chimero says it, on
the URL given; **[reported]** = another person or site says it, on the URL given.

## Sources

Pages studied, with their kind and the source for authorship:

1. https://frankchimero.com/ (personal home page). His own site.
2. https://frankchimero.com/blog/2020/hands-tv/ (essay, August 3, 2020). His own site.
3. https://frankchimero.com/projects/dust/ (collage gallery). His own site; collages
   dated 2017–2020 on the page.
4. https://design.frankchimero.com/ (portfolio index). His own site; footer "© 2021",
   header "Design stuff 2007–2021".
5. https://studiofrank.co/ (studio splash page). His studio; page description "a brand
   studio and design consultancy by Frank Chimero".
6. https://studiofrank.co/info (studio about page, 2020 site).
   https://studiofrank.co/colophon: "Its site was produced in 2020. Design and
   development by Frank Chimero." [stated]
7. https://shapeofdesignbook.com/ (book landing page).
   https://fontsinuse.com/designers/58/frank-chimero credits him with "The Shape of
   Design website and online edition". [reported]
8. https://shapeofdesignbook.com/chapters/00-introduction/ (online book chapter). Same
   source as 7.
9. https://www.moderntreasury.com/ (client marketing home page).
   https://v8.helenvholmes.com/work/modern-treasury-dot-com lists "Designers: Frank
   Chimero, Ryan Essmaker", year 2023 [reported]; https://frankchimero.com/about/ lists
   him as Modern Treasury "Creative Director and Head of Brand", 2022–2025 [stated].

Caveat on page 9: the live page mentions stablecoins and a "Dec 3rd" webinar, so its
content has changed since the 2023 redesign the credit names, and Chimero left in 2025
(about page). Which parts of today's page are his is not stated anywhere I found. Its
findings below are kept separate from the moves of his own sites for that reason.

Other sources used:

- https://frankchimero.com/about/ (live 2026): roles and clients; "I helped design a few
  things you've probably used, like NPR's online audio player and Wikipedia's article
  pages."
- https://design.frankchimero.com/ (page 4) is also a list of his projects with year and
  kind; source for set-aside page A ("2017 Dropmark — Brand and web design — Site design
  and corraling loose design elements into a cohesive brand").
- https://yayitsye.com/dropmark/ (live): developer Ye Shin credits "the designs being
  done by Frank Chimero", "Design Lead"; new marketing pages (home, about, pricing) went up
  October 2019. Source for set-aside page A.
- Stylesheets and scripts read for numbers: https://frankchimero.com/styles.css,
  https://design.frankchimero.com/css/screen.css, https://design.frankchimero.com/main.js,
  https://studiofrank.co/splash/styles.css, https://studiofrank.co/splash/script.js,
  https://studiofrank.co/css/screen.css, https://shapeofdesignbook.com/css/styles.css,
  https://www.dropmark.com/assets/css/all.css?20230508,
  https://www.dropmark.com/assets/css/layouts/index.css?20230508,
  https://www.dropmark.com/assets/js/illustrate-animate.js?20230508.

Pages added after step 8 (they were the two set-aside pages; studied from the full-size
screenshots taken on 2026-11-24 and their HTML and stylesheets fetched with curl):

10. https://www.dropmark.com/ (client marketing home page). His index (page 4) lists
    "2017 Dropmark — Brand and web design — Site design and corraling loose design
    elements into a cohesive brand for the visual bookmarking tool" [stated];
    https://yayitsye.com/dropmark/ credits "the designs being done by Frank Chimero",
    "Design Lead", for new marketing pages (home, about, pricing) that "went up October
    2019" [reported].
11. https://design.frankchimero.com/info (portfolio about page). Same site as page 4,
    footer "© 2021".

Set aside for step 8: none (step 8 has been run; both former set-aside pages are now
pages 10 and 11).

## Findings per page

### 1. frankchimero.com home

- Grid [observed]: at 1440 the page is two halves. The left half (720 px) is a header
  set as a two-column grid (`1fr 1fr`, padding 1.5rem = 21 px): name block at x=21, nav
  list at x=360. The right half is empty. Page height equals the viewport (891); nothing
  scrolls.
- Type [observed]: one face, `Courier, mono`, one size, 13 px / 19.5 px, for every word.
  Each nav item is two lines: title in #eeeeee, a descriptor under it ("My design
  practice", "Book · 2012") in dim #717d78. Largest size : body size = 1 : 1. Oldstyle
  proportional numerals (`font-variant-numeric: oldstyle-nums proportional-nums`).
- Colour [observed]: whole page dark grey-green #3d4340; text #eee and #717d78. No
  accent colour on this page.
- Imagery [observed]: none, except a 12 px arrow (↗) after external links.
- Composition [observed]: the name, top left, is met first; half the page (right side,
  720×891) is empty dark field.
- Motion [observed]: on hover the title line of a nav item fades to the dim colour
  (0.2 s).
- Phone [observed]: one column at x=21, the same 13 px; the full nav list stays visible
  as a stacked list (no menu button). Between 500 and 999 px the nav becomes a two-column
  grid (stylesheet).

### 2. Essay "Hands TV" (frankchimero.com, 2020)

- Grid [observed]: same two halves. Left half = the home page header, sticky, full
  viewport height. Right half (x=720–1440) is the article, light #eeeeee, scrolling on
  its own (`overflow-y: scroll`, height 100dvh), padding calc(3vw + 1rem) ≈ 57 px. Text
  column max 36rem = 504 px, centred in the right half (x=828–1332). Images are the
  column width (504), radius 2 px, 4rem (56 px) above and below.
- Type [observed]: Courier 14 px / 21 px body, #2f3432; title "Hands TV" 14 px bold,
  centred, date under it in dim #828b87; header has 6rem (84 px) padding above and below.
  Captions and footer 13 px centred dim. Largest : body = 14 : 14 = 1.0. Line length
  about 57–60 characters (counted on the screenshot; 504 px of 14 px Courier).
- Colour [observed]: left half #3d4340 (50% of the screen), right half #eeeeee; links
  underlined in dim grey, hover to green #5e786d (0.2 s).
- Imagery [observed]: five video stills (504×284, 16:9), uncropped, each with a centred
  13 px linked caption; they sit on the text column, never wider.
- Composition [observed]: title block centred with ~84 px of empty space above and
  below; text left-aligned, ragged right; footer sign-off "Thanks for looking." centred.
- Phone [observed]: header stacks on top (dark band, ~315 px tall, full nav visible),
  article below at x=26, column 339 px, same 14 px type (~37 characters per line).

### 3. Dust (frankchimero.com, collages 2017–2020)

- Same template as 2 [observed]. Intro: "Dust" 14 px bold centred, description in dim
  14 px centred, date range under it.
- Imagery [observed]: 21 square collages, each 504×504 (phone 339×339), one per row,
  56 px apart, no captions. Collage content: old black-and-white and sepia photographs
  (birds, faces, clouds, statues, flowers), torn paper edges, flat geometric shapes
  (semicircles, arches, rings), thin hand-drawn lines, one ochre/rust accent, on a warm
  grey paper ground. The page says they "gather old, forgotten images from public
  archives" [stated, https://frankchimero.com/projects/dust/].
- Phone [observed]: as page 2; images 339 px square.

### 4. design.frankchimero.com index ("Design stuff 2007–2021")

- Grid [observed]: 12 columns, gap 1rem (14 px), outer padding 2rem (28 px). Header:
  cols 1–6 name block, cols 7–12 nav ("Index / Info", stacked, x=707). Each project row:
  year col 1 (x=28), name cols 2–6 (x=145), kind cols 7–8 (x=707), description cols 9–12
  (x=933). The grid does not change down the page.
- Type [observed]: Newsreader (serif) light 300 at 4vw = 57.6 px, line-height 1, for
  project names only; header Newsreader 36 px (clamp 24–36 px). Everything else system
  UI sans 14 px weight 600, letter-spacing −0.01em, at 40% white. Largest : body =
  57.6 : 14 ≈ 4.1. Oldstyle numerals (`onum`), tabular for years. About 105 rows.
- Colour [observed]: black #000 field; white names; 40% white metadata; row rules 1 px at
  12% white. No accent.
- Imagery [observed]: none on the page; the list is all type.
- Composition [observed]: ~390 px of black (header margin 140 px + first row 25vh)
  between header and the first row; names are what the eye meets; the 2007 entry has no
  client name, only "———".
- Motion [observed in main.js]: page changes fade out 500 ms / in 300 ms (Barba.js,
  easeInOutCirc); header links 40% → white on hover (0.2 s). No hover state on rows.
- Phone [observed]: rows stack year / name (24 px, weight 325) / description; the kind
  column is hidden below 800 px. Header keeps two columns.

### 5. studiofrank.co (studio splash, 2025)

- Grid [observed]: content block is pushed to the bottom of a 100dvh header. Left inset
  10rem (160 px), then columns `1fr 3fr` with a 40 px gap: logo mark at x=180, headline
  at x=530. Two fixed 1 px vertical hairlines (white 25%) run the full height at x=160
  and x=500, drawn over the photo at the column edges.
- Type [observed]: headline Signifier Light (serif) 36 px / 45 px, yellow #ffee00,
  `text-wrap: balance`, max 26em, three lines; small text Söhne 14 px. Largest : body =
  36 : 14 ≈ 2.6.
- Colour [observed]: a full-bleed fixed photograph of blue sky and white cloud covers
  the whole viewport; yellow for headline, button and logo; white 14 px status line.
- Imagery [observed]: the cloud photo, uncropped to the viewport edges (object-fit
  cover); a 23 px yellow dot-grid logo mark.
- Composition [observed]: top two-thirds of the screen is only sky; the sentence sits
  low, left of centre.
- Motion [observed]: button hover yellow → black with white text (0.3 s); click copies
  the email and the label reads "Email copied" for 2 s (script.js).
- Phone [observed]: hairlines removed; logo and headline separated by horizontal 1 px
  white 20% rules; 20 px side padding; headline 28 px / 35 px; still bottom-anchored.

### 6. studiofrank.co/info (studio site, 2020)

- Grid [observed]: body margin 25.5 px; main is two equal columns (`1fr 1fr`, gap
  25.5 px). Left: line illustration centred (~476×425). Right: text starting at x=733,
  the page's centre line; nav "Work / Info" stacked, also at x=733. Lower section on a
  four-column grid (Capabilities at x=366, client list in two columns at 733 and 1047).
  All vertical spacing is multiples of the line height (1.5em): 2×, 4×, 5×.
- Type [observed]: system UI sans stack (-apple-system, Segoe UI…) 17 px / 25.5 px;
  "About Frank" 23.8 px regular; section labels ("Frank the Office") the same 17 px as
  the text but pale green. Largest : body = 23.8 : 17 = 1.4. Text measure up to 35em;
  a line holds about 72 characters (counted).
- Colour [observed]: cream #F9F7EA field; olive #515F44 text and drawing line; pale
  green #A5AF9B labels and link underlines. Nothing else.
- Imagery [observed]: a hand-drawn single-weight line portrait (a bald, bearded man
  leaning on his hand at a desk with a laptop and phone) in the text colour; a
  hand-lettered "frank" logotype top left.
- Motion [observed]: link opacity 0.3 s; background-colour transition 0.6 s.
- Phone [observed]: drawing first, centred (274 px); text one column at x=24, 16 px /
  24 px; lists in two columns.

### 7. shapeofdesignbook.com (book landing)

- Grid [observed]: a fixed white bar 7rem (98 px) on the left edge with a 1 px #eee
  border, holding a menu button and the title "THE SHAPE OF DESIGN · Frank Chimero"
  rotated 90° and running down the bar. The rest is a flex row, max 70rem, height
  100vh − 9rem: quote | cover | quote.
- Type [observed]: Pitch (monospace) 14 px / 24 px for quotes, labels, footer; source
  names uppercase, underlined. Lyon Text (serif) 17.5 px for chapter titles in the menu.
  Oldstyle numerals and kerning on (`onum`, `kern`).
- Colour [observed]: light grey #dfdfdf with a 100 px tiled paper texture multiplied over
  it; book cover white; black circles; rust #b95b23 on link and button hover.
- Imagery [observed]: the book cover (404×642) presented as an object, with four stacked
  soft shadows offset to the lower left.
- Motion [observed]: menu panel slides in from the left (300 px, 0.3 s), menu icon turns
  into ×; "Buy" and "Amazon" are 70 px black circles fixed top right that turn rust and
  rotate continuously on hover; link underlines are drawn with a 2 px background
  gradient.
- Phone [observed]: left bar becomes a top bar with the title in uppercase mono; cover
  210 px wide centred on the texture; quotes stacked; the table of contents follows on
  the page; the two black circles stay fixed bottom right, over the text.

### 8. The Shape of Design online edition, Introduction

- Grid [observed]: at ≥1200 px the page is split: the fixed 98 px bar, then a fixed
  left panel (x=70–720, 50vw − 5rem) on the paper texture, then the text on the right
  from x=769, 587 px wide (max 30em).
- Type [observed]: Lyon Text 20 px / 27 px, #333, hyphenation on; paragraphs are not
  spaced but indented 1.5em after the first (book setting). The chapter title is the same
  20 px, in rust #b95b23. Largest : body = 1.0. About 64 characters per line (counted).
  Pitch 14 px for the next-chapter label and footer.
- Imagery [observed]: one small black engraving-style drawing (a candle lit by another
  candle, ~140×190) centred in the 650×891 left panel; the panel is otherwise empty
  texture.
- Composition [observed]: the drawing stays fixed while the text scrolls; the end of the
  chapter has a rule, an arrow, "Chapter One / How and Why" centred (arrow moves 1rem
  right on hover, 0.2 s).
- Phone [observed]: the drawing gets its own near-full screen (390×772) before the
  text; text 334 px at x=28, same 20 px (~35 characters per line); the table of contents
  follows the chapter.

### 9. moderntreasury.com home (client; see caveat under Sources)

- Grid [observed]: sticky top nav 63 px; content max ~1166 px (x=117–1283), centred.
  Sections: centred hero; logo strip; 2×2 rounded panels; three-column stats with
  hairlines; four-step stepper; code panel; three cards; testimonial; form; six-column
  dark footer.
- Type [observed]: three custom families: a display grotesk (`mt-neue-display`, 47 px,
  weight 450) for headlines, `mt-sans` 16 px / 24 px weight 360 for text, `mt-mono`
  13 px for labels, step numbers and code. Largest : body ≈ 2.9.
- Colour [observed]: mostly white; black text; pale beige, mauve-white and aqua panel
  fills; deep green #0C221D footer and green logo; mint highlights in code and labels.
- Imagery [observed]: faint square grid behind the hero; a line diagram of payment rails
  (black square node, thin grey connectors, mono-caps labels in pale green tags that
  highlight in turn); UI mock cards inside panels.
- Phone [observed]: hamburger menu; hero 3 lines; panels and stats stack; stepper shows
  one step with arrow buttons; footer two columns.


### 10. dropmark.com home (client; studied after step 8)

Authorship and date: his index (page 4) dates the project 2017 [stated]; Ye Shin dates
the marketing pages he designed to October 2019 [reported, https://yayitsye.com/dropmark/].
Whether the live page is that page cannot be shown: its stylesheets and scripts carry the
version `?20230508` (May 2023), the footer reads "Made by Oak Studios" and "© 2011-2026",
and the copy says "Trusted for 15+ years" and offers "Dropmark for Figma". So the page has
been edited since 2019 at least in copy and assets; no source says which parts of the
layout are his. Findings below are kept apart from the moves of his own sites, as for 9.

Reviewer's points checked against the page:

1. Navigation [observed; held]: a horizontal bar, items right-aligned
   (`.nav__items{display:flex;justify-content:flex-end}`), 20 px text, a filled dark
   #404040 "Sign up" button at the right end; logo and wordmark at the left. On phone the
   bar becomes the logo plus a text button "Menu" (a word, not an icon).
2. Sizes [observed; held with corrections]: centred h1 "Visual organization for people
   with things to do", 60 px / 72 px, `DropmarkRealHead` weight 500 (not ~48 px); intro
   20 px / 30 px (not ~18; the stylesheet's base is 18 px); section heading "Teams around
   the world use Dropmark everyday" 40 px weight 600; "Trusted for 15+ years" 40 px; stat
   numbers 24 px cyan with 14 px white captions; card titles 17 px semibold, card text
   15 px grey #7f7f7f. Largest : body = 60 : 20 = 3.0.
3. Type [observed; held]: two custom-named sans families, `DropmarkRealHead` (500) and
   `DropmarkRealText` (400/600), plus an icon font "Dropmark". No monospace in the
   stylesheets. No oldstyle-numeral setting.
4. Colour [observed; held]: white field, warm off-white #f7f7f1 bands, text #404040;
   cyan #00affa for the primary button, links and stat numbers; illustration and panel
   colours coral #ff5d43, pink #f8b3b8, navy #2c2a6c / #1e2554, teal #38dede, purple
   #9163f9. Six saturated hues.
5. Imagery [observed; held]: a flat vector illustration of folded paper blocks seen at an
   angle (axonometric) with figures at work on their faces, full width below the hero
   (svg 1440×894), in the six hues; pieces animate in on load with staggered delays of
   0–1.2 s, 0.5 s each (`illustrate-animate.js`, `index.css`). A carousel of cards (image
   left, title, two lines, a cyan link) that wraps around and advances every 3 s
   (Flickity, `autoPlay: 3000`). A strip of client logos that scrolls continuously
   (`scrollCompanies`, 60 s, linear, infinite).
6. Order [observed; held]: nav; centred headline, intro, two buttons ("Sign up for free"
   filled cyan, "Show me more" outlined); illustration; card carousel; logo panel beside a
   navy stats panel with geometric shapes; footer with credit line and four link columns.
   Phone: everything stacks; headline 3 lines left-aligned; the illustration area is
   blank in the phone screenshot (it did not draw in the frame).

### 11. design.frankchimero.com/info (studied after step 8)

Same site, stylesheet and script as page 4.

Reviewer's points checked against the page:

1. Ground [observed; held in part]: the background is never fixed; `body.info` animates
   through hsl(160 → 190 → 220 → 250 → 270 → 300 → 330 → 0 → 30 → 60, 70%, 90%) over
   130 s, infinitely, after a 2 s delay, with `mix-blend-mode: multiply`. The screenshots
   caught aqua, periwinkle and lavender; the cycle also passes mint, pink, peach and pale
   yellow. "Lavender to periwinkle" is only the part the screenshots caught.
2. Type [observed; held with corrections]: biography in Newsreader regular at
   clamp(24 px, 2.5vw, 36 px) = 36 px at 1440 (not ~30), line-height 1.33 (≈48 px);
   labels, lists and footer in the system UI sans at 14 px weight 600 (not 13); header
   Newsreader 36 px as on page 4. No monospace. On phone the biography is 24 px.
   Largest : smallest = 36 : 14 ≈ 2.6, and the largest size is the running text.
3. Grid [observed; held]: at ≥1400 px a 12-column grid (padding 28 px, gap 14 px):
   portrait cols 3–4, links/capabilities/clients cols 5–6 (x≈497), biography cols 7–12
   starting at the centre line (x≈731), about 660 px wide less 28 px right padding.
   No element is fixed or sticky; both halves scroll. About 43–45 characters a line
   (counted on the screenshot).
4. Imagery [observed; held]: one black-and-white portrait photograph (`/fc.jpg`, alt
   "Portrait of Frank Chimero"), cropped to a circle (`border-radius: 100%`), max 18rem,
   80% of its two columns; it multiplies into the moving ground.

Also [observed]: ~200 px of empty ground between header and content (y≈140–340 of an
835 px screen); cols 1–2 stay empty beside the portrait. Header and nav as on page 4
("Frank Chimero / Design stuff / 2007–2021" with the last two lines at 40%; "Index /
Info" stacked at the centre line, current item dark). Phone: header keeps two columns;
portrait and links side by side; biography one column at 24 px; capabilities and
clients in two columns; footer two columns.

## Comparison across the pages

Pages are referred to by number. "Own sites" = 1–8 and 11; pages 9 and 10 are client
work whose live versions have changed since the dates the credits give (see 9 and 10).

### Moves

1. **The screen split into two halves, one of which holds still.**
   How: the viewport is cut at or near the vertical centre; one half carries navigation
   or a single image and stays fixed (sticky/fixed, full viewport height) while the other
   half scrolls the content.
   Shown by: 1, 2, 3 (left header sticky, right article scrolls inside its own box);
   8 (fixed image panel left, text right).
   Not shown by: 4, 5, 7, 9, 10. Pages 6 and 11 split at the centre line (text starts at
   x≈731–733) but nothing holds still; both halves scroll.
   Default in its place: one centred column under a horizontal top bar.
   Phone: the halves stack; the fixed half becomes a band (1–3) or a full screen of its
   own (8) above the content.

2. **One text size; hierarchy made with colour and weight, not size.**
   How: titles are the body size (bold, or in an accent colour); secondary lines are the
   same size in a dimmer tint.
   Shown by: 1, 2, 3 (13/14 px only, ratio 1.0–1.08); 8 (title and body both 20 px,
   title in rust); 6 (labels same 17 px as text, pale green; one heading at 1.4×).
   Not shown by: 4 (names 4.1× body), 5 (2.6×), 9 (2.9×), 10 (3.0×), 11 (36 px serif
   running text against 14 px sans labels, 2.6×). Page 7 has no running text.
   Default in its place: an H1 2.5–4× body with a size step for each level.

3. **Stacked two-line labels: a name, and under it a dimmer line at the same size.**
   How: item title, then a descriptor or number on its own line in the dim colour; no
   size change, no icons.
   Shown by: 1–3 nav ("Studio Frank / My design practice"); 4 and 11 header ("Frank
   Chimero / Design stuff / 2007–2021"); 6 ("Frank the Office" over its paragraph); 7 and
   8 table of contents ("Chapter One" dim mono over "How and Why").
   Not shown by: 5, 9, 10.
   Default in its place: one-line links in a horizontal bar; headings set larger.

4. **Navigation as a short vertical list placed on a grid column, kept visible on phone.**
   How: two to six links stacked one per line, sitting at a column line (x=360 on 1;
   x=707 on 4; x≈731–733, the centre, on 6 and 11) rather than right-aligned in a bar; on
   phone the same list stays on the page with no menu button.
   Shown by: 1, 2, 3, 4, 6, 11.
   Not shown by: 7, 8 (hidden behind a menu button in a left bar), 9 (horizontal bar,
   dropdowns, hamburger on phone), 10 (horizontal right-aligned bar with a filled sign-up
   button, "Menu" button on phone). Page 5 has no navigation.
   Default in its place: horizontal nav bar right-aligned, hamburger on phone.

5. **A large deliberate empty field, often half the screen.**
   How (measured): 1, right half empty (720×891, 50% of the screen); 4, ~390 px of black
   between header and list (44% of the first screen); 5, the top ~600 of 891 px is only
   sky; 8, a 650×891 panel holding a ~140×190 drawing (about 5% filled); 11, ~200 px of
   empty ground under the header (~24% of the first screen) and two empty columns
   beside the portrait.
   Shown by: 1, 4, 5, 8, 11; 2 and 3 have ~84 px empty above and below a small centred
   title.
   Not shown by: 6 (normal spacing), 9 and 10 (sections packed in sequence).
   Default in its place: content filling the width, hero with image beside the text.

6. **Typewriter/monospace face as a working voice.**
   How: a monospace face carries UI, labels and metadata, and on 1–3 all text including
   long essays (Courier 14 px).
   Shown by: 1, 2, 3 (Courier for everything); 7, 8 (Pitch for UI, quotes, labels; serif
   for reading); 9 (mono for labels, numbers and code).
   Not shown by: 4 and 11 (system sans for metadata), 5 (Söhne), 6 (system sans), 10
   (two sans families, no mono).
   Default in its place: one sans family for UI and text.

7. **Oldstyle numerals turned on.**
   Shown by: 1–3 (`oldstyle-nums`), 4 and 11 (`onum`; tabular for the year column on 4),
   7–8 (`onum`).
   Not shown by: 5, 10 (no numeral setting in their stylesheets). Not checked: 6, 9.
   Default in its place: lining figures.

8. **Hand-made or found imagery, one piece at a time, set small or square in empty
   space.**
   How: archival photographs collaged (3), a found engraving (8), a hand-drawn line
   portrait and hand-lettered logotype (6), the book cover shot as an object (7); one
   image per row or per panel, never a grid of thumbnails.
   Shown by: 3, 6, 7, 8.
   Not shown by: 1, 4 (no images at all); 2 (borrowed video stills); 5 (stock-like sky
   photograph); 9 (UI mocks and diagrams); 10 (flat vector illustration, card carousel,
   logo strip); 11 (a circular-cropped portrait photograph; one image, set small beside
   empty columns, but a photograph, not made or found).
   Default in its place: product screenshots or stock photos in a card grid.

9. **Muted single-hue palettes with at most one accent.**
   How: one family of tints for field and text, plus one accent used only for links,
   hover or one element: 1–3 grey-green #3d4340 / #eeeeee, accent #5e786d on hover; 6
   olive on cream, nothing else; 7–8 grey paper and #333, rust #b95b23 accent; 4 black and
   white only.
   Not shown by: 5 (saturated sky blue with pure yellow #fe0), 9 (several pale tints plus
   green brand), 10 (six saturated hues), 11 (black text on a pale ground that moves
   through every hue at 70% saturation, 90% lightness; one ground colour at a time, but
   not one hue).
   Default in its place: white background, one bright brand blue for buttons.

10. **Motion limited to hover colour changes and page fades.**
    How: 0.2–0.3 s colour or opacity transitions on links and buttons; whole-page fades
    (4, 11); a menu slide (7, 0.3 s).
    Shown by: 1, 2, 4, 5, 6, 7, 8, 11.
    Exceptions: 7 spins the buy buttons on hover; 9 animates its rail diagram; 11 moves
    its whole background through the hue circle over 130 s by itself; 10 animates its
    illustration in on load, auto-advances its carousel every 3 s and scrolls its logo
    strip without end. No page has scroll-triggered reveals (none found in the
    stylesheets or scripts read).
    Default in its place: fade/slide-in on scroll.

### What changes from project to project

- **Medium sets the conventions.** The book site (7–8) takes print book setting: serif
  reading face, indented unspaced paragraphs, hyphenation, chapter openers, a paper
  texture, the cover shown as an object. The personal site (1–3) takes the typewriter:
  Courier for everything, one size. [observed]
- **Typefaces change every project.** Courier (1–3); Newsreader + system sans (4, 11);
  Signifier + Söhne (5); system sans only (6); Lyon + Pitch (7–8); custom grotesk/sans/
  mono (9); two custom-named sans families (10). No face repeats across projects; within
  a project the pairing holds (4 and 11). [observed]
- **Within one site the roles of the faces can swap.** On 4 the serif is for short
  names at 4vw and the sans for running descriptions; on 11 the serif is the running
  biography at 36 px and the sans is for lists and labels. [observed]
- **Ground changes:** dark grey-green (1–3), black (4), photograph (5), cream (6),
  textured paper (7–8), white (9), white and warm off-white (10), a pale ground cycling
  through hues (11). Within one site it can change by page (4 black, 11 moving pastel).
  [observed]
- **Studio pitch vs. own writing.** The 2025 studio splash (5) is the only own page with
  a large headline, saturated colour and a full-bleed photograph; the pages for his own
  writing and archive (1–4, 8) keep sizes flat and colour muted. The 2021 about page
  (11) sets its biography large (36 px) but keeps colour to one pale ground and black.
  What decides this is not stated on the pages.
- **Client marketing pages (9, 10)** both follow the conventional software marketing
  order (hero with two buttons, illustration or diagram, feature cards, logo strip,
  stats, form or footer sitemap), with cards or rounded panels and saturated or
  multiple tints; none of the own sites do. Both live pages have changed since the
  dates their credits give, so whether this is Chimero's choice or later edits is not
  known.

## Looked for and not found

- A case-study page by Chimero: his portfolio index (4) has no project pages (rows link
  to "#"); the 2020 studio site's "Work" link now goes to the 2025 splash. No live case
  study found.
- A source showing that the live dropmark.com home (10) is the October 2019 page: none
  found. Its assets are versioned May 2023 and its copy dates from later; Dropmark's own
  blog post on the redesign (https://www.dropmark.com/blog/using-dropmark-to-design-dropmark/)
  returned 403.
- An essay or talk by Chimero still live as its own designed page: What Screens Want,
  The Web's Grain, Everything Easy is Hard Again, The Good Room and Beyond the Machine
  are all in the frankchimero.com template now; the standalone address Fonts in Use
  records for What Screens Want (http://frankchimero.com/what-screens-want/) returns 404.
- NPR article page and audio player (2015, listed on 4 and the about page): not studied;
  I found no source saying the current NPR pages are still his design.
- abstract.com returned 403; not studied.
- shiflett.org and faculty.com are listed on 4 (2017); a 2019 post
  (https://stellify.net/stellify-realigned/) says they were "designed by Frank Chimero",
  but nothing says the live versions are still that design; not studied.
- Scroll-driven animation, parallax, custom cursors: none found on any page.
- Dropmark at phone width: the illustration did not draw in my frame, so its phone
  treatment is not recorded.
