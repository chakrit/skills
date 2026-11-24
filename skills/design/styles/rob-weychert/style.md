# Rob Weychert: the system, then the deviation

Design a page by stating a small system (one interval, one grid, one hue), letting it
produce the plain conventional version, then bending a single convention so the page fits
this content and no other. Distilled from Rob Weychert's freely published writing, his
seven site versions, his project write-ups, one talk text, one podcast transcript and
other people's accounts. Written in our own words.

- **Feels like:** an editorial page or a printed listing made by someone who did the
  maths and then trusted his eye. Even, calm type where large lines are light and small
  ones are heavy; a grid with visible proportion; a strong limited palette from one hue;
  one surprising structural idea, such as an empty grid showing what is missing.
- **Suits:** newsrooms and long reads, archives, diaries, listings, anything with data,
  counts or permutations to show, small cultural venues, zines.

## The way of working

Work in this order.

1. **Inventory.** List every kind of content the page holds and how often each appears
   (body, dates, names, prices, captions, labels, headings). For a listing, list what a
   reader scans for.
2. **The conventional version.** Lay the content out the most ordinary way that works:
   one reading column, a plain list, a plain table. Do it in black and white.
3. **Read it as a reader.** Ask how that convention fails this content.
4. **State the system.** Fill in the parameter sheet below. Everything visual comes from
   it.
5. **Make one deviation.** Change the one convention step 3 names, and only that. See
   "Deviations" for the moves he uses.
6. **Grey, then hue.** Settle hierarchy in black and white, add greys as a second layer of
   contrast, then map one hue and its rotations onto the grey roles.
7. **Subtract until it breaks.** Remove pieces one at a time until the page stops working,
   then put the last one back.
8. **Eyeball the system.** Where a derived value looks wrong, override it. The system is
   the foundation; it does not have the final say.

Draw the deviation on paper first when it is a grid or a partition. Patterns like these
cannot be found in code.

## The parameter sheet

State every value. One number should drive most of the others.

| Variable          | What it sets                                         | His habit                                           |
|-------------------|------------------------------------------------------|-----------------------------------------------------|
| Interval          | Ratio between size steps, weight steps, grid units   | 1.5 (V6), 4:3 (V7); choose one with a reason        |
| Base size         | `--scale0`, body text                                | rem from a percentage root                          |
| Base weight       | Weight at `--scale0`                                 | about 400 on a variable weight axis                 |
| Pens              | The thin and the thick stroke                        | a thin pen for most type, a thick one for the name  |
| Grid ratios       | margin : column : gutter : padding                   | small integers, e.g. 4 : 4 : 2 : 1                  |
| Column counts     | Columns per breakpoint                               | e.g. 4 / 8 / 12, or 14 with text in the centre 8    |
| Rule width        | Every border, rule and icon stroke                   | the face's stem, about 1/16 of the type size        |
| Base hue          | The one hue all colour derives from                  | from a date, a source image, or the RYB wheel       |
| Rotations         | Accent and neutral hues                              | triad ±120°, complement +180° for neutrals          |
| Hue source        | What sets the base hue per page                      | the page's own date when it has one                 |
| The deviation     | The one convention bent for this content             | from step 3                                         |

### Deriving from the interval

- **Sizes:** `size(step) = base × interval^step`. Name steps from body text: `--scale-1`,
  `--scale0`, `--scale1`, `--scale2`. Use few steps.
- **Weights run the other way:** `weight(step) = base weight ÷ interval^step`. Large type
  is light and small type is heavy, so every stroke on the page looks drawn with the same
  thin pen. Keep one heavy setting as the thick pen, for the name. This needs a variable font with a continuous weight axis; choose a low-contrast face
  with a little character in its joins, not a sterile geometric.
- **Grid:** take the four grid ratios from the interval or from small integers, and
  derive widths from them. The type and the layout should speak the same language.
- **Rules and icons:** draw them at the stem width. Icons are stroke-only, on a small
  square grid, with no fills.
- **Colour:** one base hue, the others by fixed rotation. Changing the base hue must
  recolour the whole page correctly.

## Type

- **Two voices by job.** Structural text (navigation, dates, labels, headings) in one
  sans; prose in which the business speaks to the reader may take a text serif, reserved
  for that voice alone. One family alone is also his way (V7).
- **Print craft, translated.** A measure near 66 characters; paragraph indents on short
  texts and space between paragraphs on long ones; true small caps never beside faux
  ones; letterspaced capitals for a date line.
- **Fit type to its cell.** When a name must fill a cell of fixed width, use a variable
  width axis and set the width per cell, tested against the longest name.
- Use rem throughout so a reader's larger default font scales the whole design.

## Grid and layout

- Define the grid; do not adopt one. No grid classes in the markup; widths come from the
  ratios.
- Describe every figure or block by a few parameters: size in columns (or full bleed),
  position (left, right, centre, pushed in or pulled out by up to three columns), wrap,
  and a phone override. Size and position say as much as the content does: a small image
  off-centre in white space reads differently from a full-width establishing image.
- Never centre lists or running text: each line should start in the same place.
- Long pages need places to pause and resume: a full-bleed figure.
- A homepage for an organisation may open with one sentence of purpose, its sections
  linked inline, then a section per part with the section name in a left column and its
  few items to the right.

## Deviations

Each starts from a convention, names how it fails, and changes one thing. Use the one
the content calls for.

- **A gallery of the known items**, when the data is partial and the gap is the news:
  draw the whole population at full count and fill only what is known, so the empty
  slots carry the finding. Keep it a plain list in the markup.
- **A table of figures**, when order or proportion is the point: restyle the same table
  as a bar chart. The markup stays a table.
- **One reading column**, when the story has two places, threads or voices: shift the
  column one way for one thread and the other way for the other, and let them meet at
  the end.
- **A list of events or products**, when readers scan for several fields at once: give
  each field a fixed place and style (a date block in its own column, names large, venue
  in small caps, price as a button). Accept that there is no single focal point.
- **A uniform list or grid**, when there are many items and the page is a wall to browse:
  partition the rows by item count, from a long repeating pattern, and size type to each
  cell. No boxes; rules run the whole grid.
- **One accent colour site-wide**, when each item or page has a date: key the hue to the
  date, months placed round the wheel and days between; hold luminance constant across
  hues; fade older items toward grey.
- **A few showcase examples**, when the product is a system of parts: enumerate every
  combination and show all of them, each numbered with a code, under the rule that made
  them.

The deviation serves the information. Information can take whatever shape the reader
needs; what it is "supposed" to look like is only the convention.

## Colour

- Map colour onto roles, not swatches: text, inverse, background, background alt, accent
  one (metadata), accent two (links and actions, used sparingly).
- Strong and limited: black and white with one vivid hue; or white line on black; or a
  hue family from one base with its triad. He calls colour his weakest skill.
- When hues change from page to page or item to item, solve each one's lightness so
  contrast stays the same, and give the neutrals a slight tint of the complementary hue.
- Take a palette from one collected image (a painting) or the RYB wheel.

## Surface and motion

- **Overprint:** a duotone, a scribble masking a picture.
- **Generative texture behind a strict page:** a field of thin parallel lines or a moiré,
  low in contrast, behind type that stays on the grid. The texture may vary; the page may
  not.
- **Genre costume** for a piece that is itself an event (a marathon): borrow one period of
  one genre's printed matter (a VHS sleeve) and build it in CSS and SVG, fitted to any
  aspect ratio. Accept the genre's clichés when the piece belongs to that tradition.
- **Motion** as an animator would: count in frames, build transitions from one rule, keep
  it behind `prefers-reduced-motion: no-preference`. The base page is the thing unadorned;
  motion is an occasional experiment.
- Humour is welcome in copy (a bio), in a self-deprecating voice.

## Phones

- Set column counts per breakpoint (for example 4, 8, 12) from the same four ratios, so a
  phone layout is the same system with fewer columns.
- Give each figure a phone override: full width, or a different crop.

## Out of bounds

- Framework grids and template sections chosen because they are familiar.
- Centred blocks of text and centred lists.
- Content in boxes: no fill, border, radius or shadow around each item. A partition grid
  is type in cells separated by rules that run the full grid, never a mosaic of tiles. A
  contact sheet of images is fine; a grid of image, title and blurb in boxes is not.
- Per-letter costume titles only when every letter gets its own treatment evenly; never a
  word set apart inside a headline (see `../../references/bans.md`).
- Small-cap or letterspaced labels inside a listing row or a date line, never as a stamp
  above a section heading. A section name in a left column beside its items is the
  heading itself.
- Decoration that overwhelms the substance; interactivity added to look forward-thinking.

## Deeper reference

- `synthesis.md`: the full design model, each point citing its note, with the moves that
  meet the bans and how this file bounds them.
- `notes/own.md`: his seven site versions and design posts: the technical-pen scale, the
  interval, date-keyed colour, partition grids, print typography.
- `notes/work.md`: client and personal work with a per-project table: ProPublica, Lost
  Mothers, The Markup, Plus Equals, Robtober, title sequences.
- `notes/talks.md`: the SND 2018 talk, the 2018 podcast, his process step by step.
- `notes/accounts.md`: what his design director and others report.
