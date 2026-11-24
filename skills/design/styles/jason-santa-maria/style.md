# Jason Santa Maria

Typography is the design's voice: choose the type first and let the page be set the way
a good magazine or book is set. Build a system with fixed parts, a grid, a few faces,
the masthead and footer, then art-direct the piece inside it so the design is a partner
to the content rather than a template it was poured into.

Numbers below come from his own sites (2004 to 2026) and his practice's site, as
recorded in `synthesis.md`. Read `synthesis.md` for the reasons and the pages behind
each instruction, and `notes/` for the raw observations.

## Before any layout

1. **Find the message.** Write down what the business wants to say and what its
   customers expect of it. Then write down the clichés of its category (for Irish music,
   leprechauns and shamrocks) and keep every one of them off the page.
2. **Gather references from the subject's world.** Old printed matter, packaging,
   objects, signage, photographs that belong to the business's world. Name the ones
   the page will draw on.
3. **Write mood words, then choose type from them.** For his studio Mighty the words
   were "stable, powerful, industrial, boxy, angular, geometric, machined, blue collar",
   and they led to a bold condensed sans set large in capitals. Choose the text face
   first: a serif with "a touch of personality (and I mean ever so little)", since
   readers spend most of their time in it. Then a condensed or narrow sans for labels,
   nav and the title, set in capitals, distinct from the serif in build. Then a
   monospace for dates, captions and prev/next. Allow one display face at most. Never
   Helvetica or Arial as the safe choice.
4. **Lay it out in grey first.** Settle hierarchy and layout with no colour. Add colour
   after.
5. **Hold colour to three or four values.** A ground, a text colour, a brighter colour
   for the largest type, and at most one accent. Do not set running text at full
   contrast: dark grey (#333 to #444) on a light ground, or light grey rgb(206,210,216)
   on a near-black ground rgb(23,25,29) with white for the intro and labels. Take the
   accent from the piece's main photograph or from the subject itself (yellow from a
   yellow book cover, red from a red table). Let the photographs carry every other
   colour on the page: no tints, gradients or extra brand colours in the type.

## The system

### Grid

- Four equal columns in a 1240 px box, 43 px gutters (277.6 px columns), on a ground
  that runs to the window edge. For a page of a few statements, six columns of 183 px
  with 20 px gutters in 1200 px, body in columns 3 to 6.
- Start every section's body in column 2 and run it across columns 2 to 4 (919 px).
  Column 1 holds only the section's name, a date, or a portrait exactly one column wide
  (a circle, 278 px). Leave the rest of column 1 empty for the full length of the
  section.
- Put a picture that sits beside text in column 4 with the text in columns 2 to 3; put
  a picture that leads a section across columns 2 to 4 at full width, square corners,
  no border, with a mono caption under it.
- Keep the same grid in every section.

### Type

- Body: the serif at 24/36 px, about 76 to 79 characters a line across columns 2 to 4.
  An opening paragraph at about 50/60 px in the serif.
- Section names in column 1: the condensed sans, bold, capitals, 40/52 px.
- Set the title far larger than the text: about 3.5 times the body (an 84/84 px
  condensed bold title over 24 px body). Treat it as a picture of type
  that anchors the layout, like a book cover or poster, and set its line breaks by hand
  for each width.
- Dates, captions, prev/next: the mono at about 19 px in a mid grey (rgb(106,118,135)
  on the dark ground). Set an article's date in column 1, right-aligned against the
  gutter, level with the top of the lead picture.
- Set long text like a book: first paragraph flush, every later paragraph indented 1 em
  with no space between; `hyphens: auto`; curly quotes and apostrophes everywhere; hang
  opening quotation marks of pull quotes and set-off quotes outside the text edge.
  Open an article with a drop cap about three lines tall.
- Judge sizes and spacing by eye after a first pass from the numbers; do not lock text
  to a baseline grid.

### Rules

- Divide sections with full-width bars 18 px thick (dark grey-teal on the near-black
  ground), not with space alone and never with cards or boxes.
- Put a double rule under an article's title, and set its meta (date, tags, prev/next)
  in a row of cells divided by thin vertical rules, with small letter-spaced capital
  labels.

### Fixed parts

- Nav starts in column 2, in the condensed sans. A monogram or mark at the right end of
  column 4. Footer in the condensed sans, its items on the grid.

## Art-direct the piece

For an article, a feature, or the lead story of a page, change the system's open parts
to suit that one piece, as a magazine art director would:

- Give it its own ground (near-black, white, light grey or a warm paper tone) and its
  own accent, both taken from its subject.
- Build it around one photograph of the thing it is about, or, when there is no
  picture, around a display face chosen for the subject (a writer's quote in a
  typewriter face).
- Let one object break the structure: the photograph hangs over the title and through
  the rule below it, or fades behind the text and past the layout's edge; a drop cap
  hangs out of its column.
- End an article with a line naming its typeface and colours (for example "Design
  tags: Photo, Titling Gothic, White, Yellow").
- Keep the masthead, nav and footer exactly as the system sets them.

## Phone

- Keep the four columns: 342 px box, 24 px margins, 16 px gaps. Stack each section's
  name above its text, and keep a portrait one column wide.
- Body 16/24, opening paragraph 28/34. Keep section names at their desktop size, 40 px,
  so they become larger than the opening paragraph.
- Keep the display element at the same ratio to the body as on desktop: 84 px over 24
  becomes 56 px over 16.
- Bars between sections become 12 px. Dates move above the lead picture; captions drop
  to about 13 px mono; prev and next stack.

## Build

- Plain HTML and CSS with CSS grid; no grid framework.
- Relative units for type and columns. Load web fonts over fallbacks matched closely
  enough that nothing jumps when they arrive.
- Do not arrange the page around the fold.
