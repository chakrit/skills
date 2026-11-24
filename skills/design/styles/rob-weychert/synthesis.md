# Rob Weychert: synthesis

Written from the three notes files in `notes/` and nothing else. Citations name the notes
file and the source key it uses: `work` P1–P11 for pages studied (P10 and P11 are his
two client pages, PhilaMOCA About and The Markup's homepage), `words` short names (for
example `words` v7-type), `accounts` S1–S13. Each of those keys leads to a URL and a date
in the notes.

## Order of work

What he settles first and what follows, as his words and the accounts describe it.

1. **Research and content first.** He starts with research, from a day to two weeks: the
   information architecture and the client's brand (`words` 2007-interview). For his own
   sites he inventories the content before any visual design: "pretty much every species
   of text" reduced to seven classes on V6 (`words` v6-type), a content inventory by data
   category and source on V7, and a ranking of which content matters most, "their
   structure is the site's structure" (`words` v7-content, v7-inventory). For a client he
   worked from reader-survey data and the client's ambitions to three agreed jobs for the
   page (`words` p-markup).
2. **Apply the convention, then ask where it falls short.** "What is the most
   conventional way of solving that problem?", then how that convention is insufficient
   for "the very specific problem to be solved as opposed to the category of problem".
   For an article: flow the text into a standard layout, read it, ask "How might I hear
   it better?", then add or subtract (`words` ub-podcast; `accounts` S4).
3. **A typographic scale, from what the type needs to do.** "Most of what I design that
   incorporates type has a typographic scale as its foundation, which informs the
   typeface choices and layout proportions." The text classes from the inventory decide
   how many sizes; typefaces are then judged against the scale; column proportions take
   the scale's numbers (`words` v6-type). Sizes in rem, body text as "the core unit of
   measure" (`words` v7-type, modern-scale).
4. **Sketch, then a grid by arithmetic.** Ten to a hundred paper thumbnails, sketching on
   after he thinks he has the answer; then "some math to figure out a rational grid
   structure" for the chosen sketch (`words` 2007-interview).
5. **Black and white, then grayscale, then colour last.** Size, shape and position are
   fixed in binary black and white; contrast is added in grayscale; a set of named
   grayscale values (six on V6 and on Tinnitus Tracker, tested for WCAG contrast) becomes
   the slots colours are mapped onto. "Color is usually the final detail" (`words`
   2007-interview, v6-color, date-color).
6. **Rough mockups and a prototype in code.** Concepts go to the client as "very basic
   wire framey mockups", weighed openly, then a functional prototype; he rarely makes
   high-fidelity mockups (`words` ub-podcast; `accounts` S4). Some systems, such as his
   show-list grid partitions, must be "carefully planned out before it's coded" (`words`
   partitioning).
7. **The system does not have the last word.** He moved V6's smallest size off the scale
   by eye: "The system is the foundation, but it doesn't have the final say—I do"
   (`words` v6-type).
8. **Take away until it breaks.** "I tend to keep taking pieces away until the thing
   breaks, and then put the last one back in" (`words` about).

Other starting points, for pieces that are not page layouts: a title sequence that
"started with the music" and led to Reid Miles and Saul Bass (`words` p-bt2022); a
mantra, "show your work", that exposes the grid in the first frames (`words` p-adh2023);
for a lettered title, a set of reference logos with a note on what he liked in each
(`words` mussari).

## Grid and type system on the current site

The numbers the moves below sit in, from V7 (`work` P1–P3) unless marked.

- 12 columns of 61.3 px with 44 px gutters and 110 px side margins at 1440 px (1220 px
  wide). Running text spans columns 1–8 (798 px); a sidebar spans 9–12. The header and
  footer use the same 12 columns (`work` P1, P2). On V6 he kept text to eight columns "to
  keep the line length in check", with the outer columns for figures and asides, and
  took column, gutter and margin widths from the scale (`words` v6-type). The ProPublica
  framework sets text in the middle eight of 14 columns (`words` pp-framework).
- One scale at 4:3: `size = base × (4/3)^n` and `weight = baseWeight ÷ (4/3)^n`. Body
  22 px / 31.9 (1.45); a 39.1 px intro at weight 225; labels 16.5 px at 533; H1 69.5 px at
  700 with line-height 0.9; H1 to body 3.16:1 (`work` P1). The base scales with the
  viewport, 18–22 px (`work`, "What changes"). He states base 24 and interval 1 1/3
  (`words` v7-type); see Mismatches. PhilaMOCA uses a fluid scale too, base 16 px at
  300 px wide to 24 px at 1400 px, with three sizes only (`work` P10).
- Borders at 1/16 rem, the stroke width of 16 px Degular at weight 400 (move 10); icons
  drawn on a 16×16 grid (`words` v7-type; `work` move 10).
- Line length: he states a 45–75 character range with about 66 as the ideal, and prefers
  a too-short line to a too-long one (`words` 2007-chapter). Pages measure 48–86
  characters (`work` table).
- Running text is left-aligned and ragged on every V7 page (`work` P1). Short display
  text is centred on some pages: The Markup's two-line hero sentence, centred at a 35ch
  maximum, is in his template (P11); V5's and Cubes Revisited's titles centre on phones
  (P6, P8); V4 centres a one-line link row (P9). His show-list grids centre the text in
  each cell (`words` partitioning).
- Images: 16:9 card images at full card width with a 4 px radius; paintings at the full
  8-column width in their own proportions, uncropped, 4 px radius, a 16.5 px caption below
  at the left (`work` P1, P2). Robtober's posters are uncropped at 2:3 (P4). For concert
  listings he gave images "a uniform square crop" because unpredictable sizes disrupt
  scanning (`words` listings).
- End of an article: metadata as outlined chips (1 px accent border, icon and label for
  month, tags, people, places), then a segmented prev / index / next control (`work` P2,
  P3).
- Motion: the sidebar is sticky and scrolls on its own; links change colour over 0.2 s;
  the CSS opts into cross-page view transitions (`work` P1, read from CSS).
- Phone: 6 columns of 44.8 px, 18 px gutters, 16 px margins; H1 43 px over two lines,
  intro 24 px, body 18 / 26.1 (about 46 characters). The sidebar becomes a floating
  magenta "Recent blog posts" button fixed at the bottom left; poster thumbnails inside
  text rows are dropped and the four "Watching / Reading / Listening / Attending" items go
  two-up (`work` P1, P2). On Robtober 2024 the display title is redrawn into tall,
  very condensed letters that fill the phone viewport, "dramatically responsive
  typography" (`work` P4); for Robtober 2022 he rearranged the title letters into a
  vertical version for tall viewports (`words` robtober-2022). He says the phone layout
  is "still very much this just tall stacked thin layout" and expects more can be done
  there (`words` ub-podcast; `accounts` S4).

## Moves

One entry per move in `work` "Moves across the pages".

### 1. Paragraphs marked by a first-line indent, not by space

- **Looks like:** every paragraph after the first starts about 2 em in and sits directly
  under the one before, with no space between. The first paragraph is not indented.
- **Built:** `p + p { text-indent: 2em }` in V7 posts (`--textIndent: 2em`, `work` P3);
  47.2 px at 23.6 px body (P4), 40 px at 20 px (P5), 36 px at 18 px (P6), and the same on
  V4 (P9).
- **Replaces:** block paragraphs with a blank line between.
- **Reason:** an indent marks a new passage "while maintaining the text's cohesion"; a
  square indent (2.1em in Georgia); indenting the first paragraph, or combining indents
  with blank lines, is redundant (`words` 2007-chapter).
- **Where he does not:** PhilaMOCA's About page spaces its paragraphs 0.75 × base apart
  (18 px at desktop) with no indent (P10); pages with no running text of more than one
  paragraph (P1, P7, P8, P11). In 2007 he wrote that on the web indents suit short
  texts, because long web text needs the relief of a blank line (`words` 2007-chapter);
  see Mismatches.
- **Phone:** kept and scaled with the body: 33.2 px (P4), 27 px (P5), kept on P6.
- **Pages:** P3, P4, P5, P6, P9; in P2's CSS but not visible there.

### 2. An opening run-in

- **Looks like:** the first words of a text are set apart inside the first line: spaced
  small capitals ("I ONLY SAW 32 new movies", P6; "WHAT A YEAR THIS TURNED OUT TO be.",
  P9), a small-capital newspaper dateline running into the first sentence ("FIRST
  PRESBYTERIAN CHURCH (GERMANTOWN), PHILADELPHIA, PA—", P5), bold ("Every October,",
  P4; "Now available in print!", P7), or bold in the accent colour (the call-to-action
  boxes on The Markup's homepage: "Don't miss a thing.", "Help us help you change the
  world.", P11).
- **Built:** the run-in is the same size as the body, at the start of the paragraph, not
  a separate lede.
- **Replaces:** a plain first paragraph, or a large drop cap or a bigger lede paragraph.
- **Reason:** for the letterspaced capitals, a short run of all caps (0.13em tracking)
  bridges a drop cap and the small body text, and introduces the text "with dignified
  fanfare" (`words` 2007-chapter, which describes it together with a drop cap). For the
  dateline and the bold run-ins, reason not stated.
- **Where he does not:** V7 posts begin plain (P1, P2, P3); P8; PhilaMOCA's About text
  opens plainly (P10).
- **Phone:** not recorded separately.
- **Pages:** P4, P5, P6, P7, P9, P11.

### 3. Colour that is not fixed per site

- **Looks like:** the accent and the tint of the greys change from page to page or from
  load to load.
- **Built:** V7 sets each page's accent hue from its date, `300 − month × 30 − day`
  (January = 300), as oklch(0.65 0.18 hue); the background and greys take the
  complementary hue (accent + 180) at 2% chroma. So a post has its own accent and the
  home page takes today's: magenta 336 (P1), coral 17 with greys at 197 (P2), blue 266
  (P3). V6 loads one of five schemes at random; each pairs a muted dark text colour
  (plum, brown, mauve, violet-grey, slate), a pale tinted background, a hot accent
  (pinks, orange) and a muted mid tone (P5). Robtober takes a palette from its theme (P4).
- **Replaces:** one fixed brand palette.
- **Reason:** for the date-tied colour on Tinnitus Tracker, a different site of his: hues
  follow the seasons round the colour wheel and pages fade to grayscale with age, so
  each entry is "kind of like a poster for the show it documented"; saturation is tuned
  by hand per month and lightness adjusted by computed luminance for even contrast
  (`words` date-color). For V7's date colour and V6's random schemes, reason not stated.
- **Where he does not:** V4 and V5 (one fixed palette, P9, P6); The Markup's homepage
  (one fixed palette, P11); the art projects, which are black, white and grey (P7, P8);
  PhilaMOCA, greyscale after the venue's black-and-white identity, its panel and text
  greys swapping with the system's light or dark mode (P10).
- **Phone:** the same scheme; on V6 a 6 px accent stripe appears at the top (P5).
- **Pages:** P1, P2, P3, P4, P5.

### 4. One saturated accent, used only for thin things

- **Looks like:** the accent appears as lines and outlines, not areas: on V7 about 2% of
  the page (every link underline, every 1 px rule, the search outline, chip outlines,
  round play buttons, and one filled sidebar header).
- **Built:** one high-chroma accent (oklch chroma 0.18 on V7) against a near-neutral
  ground (2% chroma); link underlines, 1–2 px rules, outlines and at most one or two
  small filled blocks in it (P1–P3). Robtober: orange-red on rules, the section heading,
  link underlines and the toggle (P4). V6: meta line, underlines, list markers (P5).
- **Replaces:** an accent used for buttons and large fills.
- **Reason:** not stated.
- **Where he does not:** V5, the art projects and PhilaMOCA have no accent (P6, P7, P8,
  P10); V4 uses several colours at once, navy, brick, orange, peach, lavender and maroon
  (P9). On The Markup's homepage pink #ff335f fills the call-to-action buttons and sets
  the 21 px bold section labels (P11); no source says whether that palette and the
  stacked button were The Markup's before him, and the same pink, navy and button appear
  in the header he says was theirs (`work` P11).
- **Phone:** V7's floating "Recent blog posts" button is a filled magenta block (P1);
  V6 adds the 6 px stripe (P5).
- **Pages:** P1, P2, P3, P4, P5.

### 5. Rules carry the structure

- **Looks like:** rows, sections and footers are divided by lines, not by boxes, fills
  or shadows.
- **Built:** 1 px accent rules between every card row and every footer row (P1–P3); a
  3 px dark rule over related posts and hairlines between its two columns, a short rule
  of about half the column before the credits (P5); an 8 px rule under the H1 and a 2 px
  rule before the meta (P6); 2 px rules under titles, dashed and vertical rules (P9);
  orange rules between sections (P4); on The Markup's homepage a 12 px band of a 3 px
  navy dot pattern opens every section, tan #cac7c3 hairlines run between stories, and
  a dotted navy L-shaped line with an arrowhead joins each section label to its stories
  (P11, in his template). V7 sets borders at 1/16 rem (`words` v7-type); their width is
  the subject of move 10.
- **Replaces:** cards with fills, radii and shadows.
- **Reason:** not stated for the rules. He wants all type on V7 to look "drawn with one
  of two technical pens" (`words` v7-type), which speaks of strokes in type, not rules.
- **Where he does not:** Plus Equals frames each cover in a heavy, about 7 px light-grey
  frame (P7); Cubes Revisited uses 1 px outlined boxes (P8); PhilaMOCA's About page has
  no rule, and holds its content in a filled grey panel with a 3 px radius, with space
  and bold sub-heads between sections (P10).
- **Filled grounds he does use:** a content panel as the page's ground, not as a divider
  between items: V5's white panel with rounded corners on a striped ground (P6), V6's
  tinted content panel inside a tan frame (P5), PhilaMOCA's grey panel (P10). The Markup
  homepage's two calls to action sit in white boxes with a 1 px pink outline (P11). No
  studied page divides rows of items with filled or shadowed cards.
- **Phone:** on P11 tan hairlines separate stories and the dotted connector runs down
  the right of the section text to a downward arrowhead.
- **Pages:** P1, P2, P3, P4, P5, P6, P9, P11.

### 6. Hanging list markers

- **Looks like:** bullets and numerals sit outside the text's left edge, so the text
  lines up with the paragraphs around it.
- **Built:** V6 bullets and numerals in the accent colour, outside the column (P5); V5's
  countdown numerals 7 to 1 hang beside 24 px bold titles (P6).
- **Replaces:** markers indented inside the text column.
- **Reason:** not stated. He names browser default list markers among things he restyles
  (`words` v7-inventory, and a 2026 post title, "Customizing ordered list styles").
- **Where he does not:** no studied page with a list lacks it; only P5 and P6 had lists
  (P10 and P11 had none).
- **Phone:** markers still hang (P5, P6).
- **Pages:** P5, P6.

### 7. Big text that is not heavy

- **Looks like:** large text at regular or light weight: a 39 px intro at weight 225
  (P1, P3), a 45 px headline at 400 (P5), a 28 px intro at 400 (P7), a 72 px title at 400
  (P8), a 45 px page title at 400 on PhilaMOCA (P10).
- **Built:** on V7, weight is divided by 4/3 at each step up the scale, so text gets
  lighter as it gets bigger; a heading resets the base weight to 700 (P1, CSS).
- **Replaces:** big headlines in bold.
- **Reason:** for V7: "I want all the type on my site to look like it was drawn with one
  of two technical pens"; a limited set of stroke widths extends a limited set of sizes;
  the result is "essentially invisible to most viewers" but brings "a certain calm"
  (`words` v7-type). For P5, P7, P8 and P10, reason not stated.
- **Where he does not:** V7's H1s at 700 (P1–P3); V5's H1 at 900 (P6); The Markup's
  36 px hero sentence at 700 (P11).
- **Phone:** V7's intro drops to 24 px (P1).
- **Pages:** P1, P3, P5, P7, P8, P10.

### 8. One type family for the whole site

- **Looks like:** one family for headings, body, labels and navigation, with hierarchy
  carried by size and weight.
- **Built:** Degular, a variable font, self-hosted (P1–P3); HEX Franklin, with the
  lettered title as the only other letterforms (P4); GimletTextNarrow, a narrow serif
  (P7); `system-ui` (P8); Archivo, self-hosted, weights 400–700, three sizes only (P10).
  On Robtober the heading, the day headings and the body are all
  23.6 px and differ only by weight and colour (P4).
- **Replaces:** a display face paired with a text face.
- **Reason:** for V7: few sizes and few stroke widths for a big site with much text;
  high-contrast faces are out; geometric sans is too "sterile" for his own prose, and
  Degular "splits the difference" (`words` v7-type). Jason Santa Maria suggested Degular
  (`words` v7-type). For P4, P7, P8, P10, reason not stated.
- **Where he does not:** V6 split a serif for "speaking directly to the reader" from a
  condensed sans for metadata, labels and headings (P5; `words` v6-type); V5 and V4 mix
  families (P6, P9); The Markup's homepage pairs Ivar serif headlines with Messina sans
  text (P11), and no source says whether he or The Markup chose them. He changed his
  mind between V6 (2017) and V7 (2026) (`words`).
- **Phone:** the same family.
- **Pages:** P1, P2, P3, P4, P7, P8, P10.

### 9. An element that leaves the column or the grid

- **Looks like:** one structural element is wider than the text or sits across it: the
  Robtober poster grid runs 1213 px against an 805 px text measure (P4); a 272 px video
  floats right inside the 8-column text, which wraps beside it at 43–45 characters
  (P3); the prev / "Projects" / next control is sticky at the bottom left and rides over
  the body text as it scrolls (P3).
- **Built:** P3 uses the ProPublica layout framework ("in use (albeit modestly) on this
  very page!"): elements take one of 15 sizes, align centre, left or right, can be pushed
  in or pulled out up to three columns, and can wrap or interrupt text (`words`
  pp-framework).
- **Replaces:** everything inside one container width.
- **Reason:** the framework "works its magic by modulating visual rhythm and contrast";
  an image "small, off-center and surrounded by generous white space offers a different
  kind of contrast and tells a different story" (`words` pp-framework). For the Robtober
  posters and the sticky control, reason not stated.
- **Where he does not:** the other nine pages. PhilaMOCA's facade photo floats right at
  50% of the article width, but inside the text column (P10).
- **Phone:** the floated video becomes full width, 359×558 (P3); the posters go four
  across at 83 px (P4). In the ProPublica framework the grid drops to four columns,
  indents scale away, wrapping is dropped when there is no room, small images can go
  full width and a closer crop can be served (`words` pp-framework).
- **Pages:** P3, P4.

### 10. Line weights and angles taken from a letterform or the logo

- **Looks like:** every line on the page has the weight of a stroke in the type or the
  mark, and slanted lines take the mark's slant.
- **Built:** V7 sets every border to the stroke width of 16 px Degular at weight 400
  (`--borderWidth`, per its CSS comment; P1–P3). PhilaMOCA's theme sets divider and
  ticket-button borders to the logo's stroke (`--logo-line`, 4.86/300 of the logo's
  width) and skews them to the logo's slant (`--logo-slant: -11.69deg`); the fade under
  its sticky header is an SVG pattern of slanted hairlines at about that slant, so text
  scrolling under it breaks into hatching (P10).
- **Replaces:** 1 px borders and angles unrelated to anything else on the page.
- **Reason:** for V7, the post that gives the technical-pen reason ("I want all the type
  on my site to look like it was drawn with one of two technical pens") sets borders at
  1/16 rem as part of the same system (`words` v7-type). For PhilaMOCA's stroke and
  slant, reason not stated.
- **Where he does not:** not shown or not determinable on the other seven pages.
- **Phone:** not recorded.
- **Pages:** P1, P2, P3 (in the CSS); P10 (the hatching is visible; the slanted
  dividers are on the events pages, known only from CSS).

## What varies from project to project, and what decides it

- **Each version of his own site gets new type and colour:** blackletter wordmark,
  Georgia and rococo ornament on V4 (P9); a slab and a serif on a striped ground on V5
  (P6); Ciutadella and Freight with random schemes on V6 (P5); Degular with a date-derived
  accent on V7 (P1–P3) (`work`). What decides it on V6 and V7: the inventory of text
  classes, the scale, and how the text speaks (`words` v6-type, v7-type).
- **Art projects drop colour and decoration:** black, white and grey, one plain family,
  the generated artwork as the only imagery (P7, P8). Cubes Revisited is built on its
  combinatorics, not a page grid: a 1:2 intro split, then an index of the 11 part-counts
  in a 4-column grid of outlined boxes, each linking to its variations (P8). What decides
  it: not stated beyond the art itself.
- **Themed posts take their look from the theme:** Robtober's VHS homage (2021),
  ransom-note title (2022), title smashing into glass (2023), flaming title with
  responsive lettering (2024) (`work` P4; `words` p-robtober). References come from the
  theme's own material: 1980s horror logos, VHS boxes (`words` mussari, robtober-2021).
- **Client identities take a concept from the client's world:** PhilaMOCA's
  "high-contrast black and white" from "the austere aesthetics of some corners of the
  late '70s post-punk movement"; Solid Product Design's O as "something solidifying"
  (`words` p-philamoca, p-solid).
- **Grid depth follows the amount and kind of content:** 12 columns with a sidebar on V7;
  a single centred measure on Robtober; a single offset column on V5 and V6; four fixed
  cover columns on Plus Equals; three fixed columns on V4; on PhilaMOCA a sticky header
  column beside a content panel of up to 90ch, its article capped at 60ch and centred in
  the panel; on The Markup's homepage a 1140 px frame where each section is a 16-column
  grid with its label in columns 1–4 and one to four stories in 5–16 (`work`).
- **Client pages keep some of his own sites' moves and drop others** (`work`, "What
  changes"):
  - PhilaMOCA (P10), where he also did the branding, keeps one family, a large title at
    a regular weight, a fluid scale with few sizes, line weights and angles taken from
    the mark, and colour that follows the system's light or dark mode as V7 does. It
    drops the indented paragraphs (spaced instead), the run-in, any accent (greyscale,
    after the venue's black-and-white identity) and rules on the page.
  - The Markup (P11), inside the host's existing site, keeps rules and dotted bands as
    section structure, a label column beside the stories, a bold run-in in the calls to
    action, and a fixed accent. It drops one family, large text at light weights, the
    accent kept to thin things, and indented paragraphs. Whether its typefaces, colours
    and stacked button were The Markup's before him is not stated. His template (by his
    own caption) excludes the host's header and footer and left copy and icons as
    placeholders; the live page has since changed its section labels, hero copy and top
    story layout.
- **The form follows what the information means, not its type:** the Lost Mothers
  gallery became a grid of some 800 mostly empty slots because the missing data "was
  itself a big part of the story", and underneath "it's just a regular old bullet list"
  (`words` snd-talk; `accounts` S4). A story reported from two places got a headline
  jutting left and right from a central axis and a text column that shifts between the
  two, converging at the end (`words` snd-talk). Concert listings got one style and
  place per scanning category, no focal point, and uniform square crops (`words`
  listings). Show lists took the dense photocopied handbills of the Trocadero as their
  model, with partitions planned for even whitespace per cell and no orphans (`words`
  partitioning).

## Refusals

- Frameworks such as React and Bootstrap, because users share their complexity cost;
  remote CDNs and hosted font services such as Typekit (`words` v7-dependency).
- Generic design systems and pattern libraries, as "outsourcing the work" and skipping
  "what makes the thing ... unique"; Bootstrap layouts made the web "mannered" (`words`
  ub-podcast; `accounts` S4).
- Committee design, where stakeholders' needs are met and users' are not (`words`
  ub-podcast; `accounts` S4).
- "Superficially forward thinking" effects; "I'm a big believer in simplicity" (`words`
  ub-podcast; `accounts` S4).
- "KPI-obsessed, cookie-cutter, vibe-coded, careless slop" (`words` lowriders).
- Craft that wants "its hard work to be appreciated as much as (or more than) the
  product" (`words` 2011-artifice).
- Centred blocks of text where "each line begins in a different place"; an emphasis
  colour with lower luminance than the body text; unneeded detail such as "Presented by"
  (`words` listings).
- Redundant paragraph marking: indenting the first paragraph, or indent plus blank line
  (`words` 2007-chapter).
- Browser default list markers and table styles (`words` v7-inventory).
- px units, "very rarely" used (`words` v7-type).
- Liquid layouts that let lines run too long, and fixed layouts that scroll sideways
  (`words` 2007-chapter).
- Motion that is not optional: video, animation and scroll effects sit behind
  `prefers-reduced-motion: no-preference` (`words` robtober-2021).

## Mismatches

What he says that the pages studied do not show:

- **Line length.** He reveres a 66-character line (`words` 2007-chapter) and started V7
  at a 75ch maximum (`words` v7-content); V7's article measures 84–86 characters per line
  at 1440 px (`work` P2).
- **Indents on long texts.** In 2007 he wrote that indents suit short web texts and long
  ones need blank lines (`words` 2007-chapter); the indent appears on long articles on
  his own sites (`work` P3, P4, P5). PhilaMOCA's About text is spaced, not indented
  (P10), which agrees with the 2007 statement.
- **Drop caps.** His 2007 chapter pairs the letterspaced capital run-in with a drop cap
  (`words` 2007-chapter); no studied page is recorded with a drop cap (`work`).
- **Scale base.** He states base 24 (`words` v7-type); V7's base scales with the
  viewport from 18 to 22 px, rendering 22 px at 1440, and 22 × (4/3)^4 gives the 69.5 px
  H1 seen (`work` P1, "What changes").
- **Centred text.** He refuses centred listings where "each line begins in a different
  place" (`words` listings). The Markup's hero, a two-line centred sentence in his
  template (P11), is display text, not a listing, so it does not contradict those words;
  but no studied page shows centred running text or a centred list.
- **One family, light large type, thin accent on The Markup.** P11 has two families, a
  700-weight hero and pink filled buttons and labels; no source says which of these were
  The Markup's before his work (`work` P11).
- **Sketching first.** He describes many paper thumbnails before anything (2007) and
  calls diving into code early a bad habit (2018); David Sleight reports that he moves
  "very quickly from sketches into code" (`words` 2007-interview, ub-podcast; `accounts`
  S2, S4). The pages cannot show which.

What the pages show that nobody explains:

- V7's date-derived accent and complementary-tinted greys, and V6's random schemes (P1,
  P2, P3, P5); his only reason for date colour concerns Tinnitus Tracker.
- The accent kept to thin things; rules instead of boxes; hanging list markers.
- The last sentence of V7's home-page intro changes on each load: "Enjoy your stay.",
  "No big whoop.", "Please remove your shoes before entering." (`work` P1).
- A full-page SVG of fine moiré curves faintly behind V7 (`work` P1). He names
  "Overprint" as "the basis of the aesthetic I want to explore" for V7 without
  explaining it (`words` v7-intro).
- V7's sticky sidebar that scrolls on its own and becomes a floating button on phones
  (`work` P1).
- Robtober's same-size type, with headings set apart by weight and colour only (`work`
  P4).
- V7's and PhilaMOCA's colour following the system's light or dark mode (`work` P1,
  P10).
- PhilaMOCA's stroke and slant taken from the logo, and the hatched fade under its
  sticky header (`work` P10).
- On The Markup's homepage: the dotted halftone band opening each section, the dotted
  L-shaped connector with an arrowhead from each label, the faint capsule pattern behind
  the hero, and the pink dotted underlines in the hero (`work` P11). The notes give no
  reason for the client sites' layouts (`words`).

## Gaps

- How V7's layout, colour and phone treatment were decided: posts on these are not
  written yet (`words` v7-launch).
- Dark mode: listed as a consideration, not discussed (`words` v7-type). V7 and
  PhilaMOCA follow the system setting, but only their dark modes were seen; V7's default
  light mode and PhilaMOCA's light mode were not (`work`).
- Whether The Markup's typefaces, colours and stacked buttons predate his homepage
  (`work` P11).
- PhilaMOCA's events pages, where the slanted dividers and ticket buttons are, known
  only from CSS (`work`). P10 and P11 were measured from screenshots and CSS, not the
  rendered page (`work`).
- How many concepts he shows a client, in what format, and how he presents them
  (`words`).
- Reasons for the grid, type and colour of his client sites, beyond PhilaMOCA's identity
  concept (`words`; `accounts`).
- Plus Equals article layouts, the shop, Robtober 2021–2022 pages (`work`).
- Hover and interaction states beyond 0.2 s colour transitions and view transitions
  read from CSS (`work`).
- His reasons for image crops and placement, beyond the square crop for scanning in
  listings (`words` listings) and V6's white "isolating their colors from mine" (`words`
  v6-color).
- Accounts of his visual choices by other people: none (`accounts`).
