# Rob Weychert

Design the way Rob Weychert works: an editorial designer who builds a page from its
text up. Content first, then a typographic scale, then a grid taken from that scale,
then black and white, then grayscale, and colour last. Each step below is a decision to
settle before the next. Numbers come from his current site (V7) unless marked; detail
and sources are in `synthesis.md` and `notes/`.

## 1. Take stock of the content

List every kind of text the page will hold, "pretty much every species of text":
headline, intro, body, labels, captions, metadata, navigation. Reduce them to a handful
of classes. Rank what matters most; the most important content's structure becomes the
page's structure.

## 2. Start from the convention, then find where it falls short

Flow the real text into the most conventional layout for this kind of page. Read it.
Ask how that convention fails this specific business, not this category of business,
and add or take away only to answer that. If the information has a meaning of its own
(something missing, two sides, a count, a sequence), let the form show it instead of
what that type of information is "supposed" to look like.

## 3. Build one typographic scale

- Use a 4:3 interval: `size = base × (4/3)^n`. Body at about 22 px (set it in rem;
  body text is the unit everything else is measured in). That gives roughly 16.5, 22,
  29.3, 39.1, 52.1, 69.5 px. Use as few steps as the text classes need: "the more sizes
  you use, the less they'll mean".
- Tie weight to the same scale: `weight = baseWeight ÷ (4/3)^n`, so text gets lighter as
  it gets bigger and heavier as it gets smaller. A 39 px intro sentence sits at a
  hairline weight (about 225); 16.5 px labels at about 533. Reset the base to 700 for
  the headline only, and give it a tight line-height (0.9). The aim is type that looks
  "drawn with one of two technical pens": few sizes, few stroke widths, a calm page.
- Body line-height about 1.45.
- Set the whole page in one type family: a variable sans with low stroke contrast, warm
  rather than geometric, that runs from hairline to bold. Headings, body, labels and
  navigation all come from it; hierarchy is size and weight. Self-host the font.
- Move a size off the scale by eye when it reads better. The system is the foundation;
  you have the final say.

## 4. Take the grid from the scale

- 12 columns. At 1440 px: 61.3 px columns, 44 px gutters, 110 px side margins, 1220 px
  of content. Running text spans columns 1–8 (about 800 px). Columns 9–12 hold a sidebar
  of related material, sticky, scrolling on its own when longer than the window. Header
  and footer sit on the same 12 columns.
- Keep text to a 45–75 character line, about 66 by preference; a line too short reads
  better than one too long.
- Let one structural element leave the text column: a figure or video floated right
  into the text (about a third of the column wide) with the text wrapping beside it; a
  row of images wider than the text measure; or a prev / next control fixed at the
  bottom left that rides over the text. Vary element sizes and offsets to modulate
  rhythm and contrast: a small image off-centre in white space tells a different story
  from a full-width one.
- Divide rows, sections and footer rows with rules: a hairline between every row of
  items and every footer row; a heavier rule (3–8 px) under a title or over a section
  where a stronger break is needed. Do not hold rows of items apart with filled or
  shadowed cards.
- Take every line's weight from the type, and any angle from the mark: set borders to
  the stroke width of the body face at regular weight at 16 px (1/16 rem for Degular).
  When the identity has a mark with a stroke and a slant, draw dividers and borders at
  that stroke and skew them to that slant, and draw any hatching at the same angle.

## 5. Black and white, then grayscale

Fix size, shape and position in pure black and white. Then add contrast in grayscale
and settle on about six named grey values, checked for WCAG contrast. These are the
slots the colours go into.

## 6. Colour last, and not fixed

- Map colour onto the grey values. Keep the ground and text nearly neutral: in oklch,
  chroma about 0.008, the greys tinted toward one hue.
- Choose one saturated accent, oklch(0.65 0.18 hue), and let it change: derive its hue
  from something the page carries, such as its date (`hue = 300 − month × 30 − day`, so
  each page has its own accent and an index takes today's), and tint the greys to the
  complementary hue (accent + 180) at 2% chroma. Tie the colour to the content the way a
  poster belongs to its show.
- Use the accent only for thin things: link underlines, every 1 px rule, field and chip
  outlines, small round controls, and at most one small filled block, such as the
  sidebar's header. It covers about 2% of the page.
- Lay a faint full-page pattern of fine moiré curves behind everything.

## 7. Set the text like a book

- Separate paragraphs with a first-line indent of 2 em and no space between them. Never
  indent the first paragraph, and never combine an indent with a blank line.
- Open the text with a run-in inside the first line, at body size: the first few words in
  letterspaced capitals (about 0.13 em), a small-capital dateline running into the first
  sentence ("PLACE, CITY—"), or a bold first phrase.
- Hang list bullets and numerals outside the text's left edge, in the accent colour, so
  the text keeps one edge.
- Left-align running text and leave the right edge ragged. Never centre a list or a run
  of items meant for scanning, so that each line begins in a different place.
- End an article with its metadata as small outlined chips (1 px accent border, icon and
  label), then a segmented prev / index / next control.
- Images at the full text width in their own proportions, uncropped, with a 4 px radius
  and a small caption below at the left. Where images sit in a row to be scanned, give
  them one uniform crop.

## 8. On a phone

- 6 columns, 18 px gutters, 16 px margins. Body 18 px / 26.1; headline about 43 px over
  two lines; the intro about 24 px.
- Floated figures go full width; a row of images wider than the text drops to fewer
  across; a closer crop may replace a wide one.
- The sidebar becomes a floating accent-coloured button at the bottom left that opens
  it. Drop small thumbnails that sat inside text rows; set short item groups two-up.
- Keep the paragraph indent and the hanging markers.
- A big display title may be redrawn for the tall screen rather than shrunk.

## 9. Motion

Links change colour over 0.2 s on hover; pages may use cross-page view transitions. Put
video, animation and scroll effects behind `prefers-reduced-motion: no-preference`. No
effects for their own sake.

## 10. Take away

Remove pieces until the page breaks, then put the last one back. Leave out detail the
reader does not need, frameworks and generic component patterns, and anything that asks
to be admired more than it serves the text.
