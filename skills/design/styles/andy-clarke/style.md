# Andy Clarke

Design the way Andy Clarke (Stuff & Nonsense) works: find the business's story, pick one
thing that is particular to it, draw that thing into a world, and build every layer of
the page so it tells the same story. His refusal sits under all of it: a site whose
logo, colours and photographs could be swapped to make it another company's site is the
failure to avoid.

The reasons and sources for everything below are in `synthesis.md`; the evidence is in
`notes/`.

## 1. Find the story before any visual decision

Before you think about illustration, layout or type, work out the story the site has to
tell: the business's experience, expertise and values, and the reasons people choose it.
Uncover it from what the business is; do not invent one. Then say what the brief is
really about in your own words, the way Clarke found that a printer-supplies company's
real problem was trust, or that a property investor "didn't need pictures of property,
it needed a strong visual language".

Plan the path through the content as a storyboard, not a diagram of boxes: what someone
should discover, and in what order. Keep conventions that work (Mountain Duck kept its
feature, edition and download journey); change only what turns into imitation.

## 2. Pick one idea particular to this business

Build the identity on one thing the business loves or is: a composer's love of tape
machines became a reel-to-reel machine; other projects were built on a client's interest
in 1950s and 1960s science-fiction paperbacks, a game-audio studio's box of toys, and an
energy consultancy's pylons, turbines and dams. Do not look at other sites in the same
sector for it. Look to magazines and their art directors, posters, comics and cartoons,
album and paperback covers, and the business's own objects, and take their thinking
rather than copying them: no pastiche.

## 3. Draw that idea as the hero scene

Make the first screen a commissioned illustrated scene, not a stock photograph, a product
screenshot, a gradient or a generic vector. Turn the business's subject into a world with
characters, and give it a mascot that recurs in other poses further down the page. Every
illustration has a job to do: it carries the site's central idea (Lockrose's sequence of
drawings shows that projects develop through stages) and is never filler.

- Give the illustration a style of its own for this business, from a named reference:
  Lockrose's came from vintage Graphis covers ("Flat colours. Strong shapes. Clear
  compositions"), its shapes built on triangles echoing the company's identity. Other
  projects used flat low-poly, heavy black outlines with flat tones, painted comic,
  steampunk machinery and 1970s flat graphics.
- To make unrelated objects belong to one world, use black outlines, geometric shading
  and a limited palette, and keep it a little imprecise so it stays playful.
- The illustration's palette is the site's palette.
- Run it off the window: 1440 by 550 px under the header with a ragged lower edge of
  ground instead of a straight cut; a scene beside the headline running to the right
  edge of the window; a machine whose reels are cut by the top and right edges; a hand
  reaching below the hero into the content.
- Build it as layered inline SVG so parts can move (section 7).
- Put the headline under the scene or beside it.

Personality never costs clarity: every illustration, animation and interaction supports
the visitor's path through the site.

## 4. Choose one typeface with character, and let it do everything

Start type early; Clarke says type "sets the tone for everything else". Shortlist a few
faces, set them on the business's name and real copy (never lorem ipsum), and judge
their tone of voice, numerals and special characters. Choose a face with more
personality than the generic one the business would otherwise get; a technical or
financial business does not need conservative type to be credible.

- Use one family for logo, headings and body. Choose a family with plenty of styles and
  weights, and draw its character out with width, weight and case: headings at width 90
  and weight 500 over body at width 100 and weight 400 (Obviously); headings at
  `"wght" 600, "wdth" 80` over body at `"wght" 400, "wdth" 100`, with an uppercase
  condensed standfirst (Bankside Sans VF); uppercase headings at weights 200 to 300 over
  body at weight 200 (Commissioner); weight 900 uppercase headings over weight 300 body
  (Alexandria); an irregular hand-cut face for everything, body included (Fido).
- Make the hierarchy steep: an H1 of 48 to 72 px over body text of 14.4 to 18 px, an H1
  to body ratio between about 3 and 5. "A steep typographic hierarchy, weighted towards
  large type, is unapologetic."
- Set display headlines solid (line height 1.0) or close to it (1.1 to 1.2), broken into
  short lines (four or five lines for a short headline), with `text-wrap: balance`.
  Black and light weights, negative tracking and tight leading make a headline block
  that "demands attention" without a fancy font.
- Draw title lettering and the logotype as artwork: a script line over heavy condensed
  capitals, jostled hand-cut letters, an outlined condensed lockup, or a tall condensed
  logotype with a coloured box behind its middle line. When a display face appears once
  on a page, outline it as SVG and keep the text available to assistive technology.

## 5. Build a limited palette around one accent

Pick a base colour, derive the others from the colour wheel (split complementary,
double split or triadic), then adjust by eye. Keep it near monochrome with one bright
accent as a counterpoint: dark navy with blue links; dark teal on mint-white with
orange `rgb(255, 119, 0)`; dark slate with red; near-black violet with yellow. Put the
accent on links, buttons, the logo and rules. Use darker shades for borders and lighter
tints for highlights; make tints and shades with multiply and screen blends. Avoid pure
complementary pairs unless you want a very high impact. Check contrast while you design.

On a dark ground use a tinted off-black (navy, violet-black, green-black, slate) and
off-white, not pure black and white: lighten and saturate the colours, use a lighter
weight, raise small text to 14.5 to 16 px, and add a little tracking and word spacing.

Give a page of the site whose subject asks for it its own colours while the grid, type
and header stay: Clarke's navy site turns near-black violet with burgundy and tan for a
hard-boiled detective book, and very dark green with sage for his about page.

## 6. Lay the page on an eight-track mirrored grid

Do not start from twelve equal columns; its rhythm is monotonous. Overlay two grids of
equal columns and use the eight tracks they make, which mirror around the centre, with
40 px side margins at desktop width:

- 4+5, four columns over five: 4:1:3:2:2:3:1:4 (at 1355 px of content: 229, 57.25,
  171.75, 114.5, 114.5, 171.75, 57.25, 229 px), or
- 4+6, four columns over six: 2:1:1:2:2:1:1:2.

Build them as Clarke does, as custom properties with named lines, `a` for the four
columns and `b` for the other grid:

```css
--grid-4-5: [a1] 4fr [b2] 1fr [a2] 3fr [b3] 2fr [a3] 2fr [b4] 3fr [a4] 1fr [b5] 4fr [a5];
--grid-4-6: [a1] 2fr [b2] 1fr [a2] 1fr [b3] 2fr [a3 b4] 2fr [b5] 1fr [a4] 1fr [b6] 2fr [a5];
--grid-12-col: repeat(12, 1fr);
--grid-column-gap: clamp(1.6875rem, 1.6223rem + .3261vi, 1.875rem);
--grid-row-gap: clamp(1rem, calc(.89rem + .54vw), 1.31rem);
```

Apply the template from `width>=64em` up, and place each section's children on named
lines with a named layout per section (he names them after cities), for example
`a1/b4` with `a4/a5`, `a1/a3` with `b4/a5`, `a1/b3` with `a3/a5`, or `a1/a5` across.

Higher ratios between column widths add drama for designs with a strong purpose; lower
ones suit academic or editorial content.

- On articles, case studies and inner pages, run the text from `a1` to `b4` (tracks 1
  to 5, about 807 px, ending near the page centre), leave track 6 empty, and put a
  sidebar or a call-to-action box of about 316 px from `a4` to `a5` (tracks 7 and 8).
- Use the narrow tracks to offset a headline, widen an image by one narrow width, indent
  images and pull quotes, and as exact gaps between main and supplementary content.
- Align a pull quote's edge to grid lines so it belongs to the story.
- Repeat the same ratio across the whole window in the hero, with no gaps, so the
  illustration reaches the window edge.
- Set rows of equal items on the 12-column grid within the same page, with a thin 1 px
  vertical rule between the columns.
- Set a list of chapters or questions as a `<details>` list; hide the browser marker and
  give the summary its own 8 px marker column.
- Let unequal modules set the pace: larger areas hold the eye longer, repeated small
  ones speed it up.

Set the measure first and let layout follow it: start at `--measure: 60ch` and adjust by
eye, `55ch` for captions and short blocks, `80ch` for introductions, headings and hero
sections, e.g. `grid-template-columns: minmax(0, var(--measure)) 1fr`. Take breakpoints
from the measure with container queries: when a column gets narrower than a readable
line, the layout changes. Clarke's own pages run body text at 73 to 85 characters
per line in the 807 px column.

## 7. Let small parts of the scene move, slowly

Animate separate SVG parts of the scene on long, independent, seamless loops: clouds
drifting over 240 s, turbine blades turning in 10 s, a dome pulsing every 4.8 s, stars
twinkling at 7.7 to 13.9 s, cogs turning at 14 to 24 s with some counter-rotating, reels
spinning in 9 s. Pick what moves by asking whether it has weight, whether it is
flexible, and whether it would move in real life; a feather swings three degrees. Use
long durations, ease-in-out or relaxed cubic Béziers, and layer several subtle movements
like a sound mix. If the eye is drawn to a movement, dial it back; keep the most obvious
motion for the one element that needs the biggest impact. Put a pause control on the
illustration and wrap all motion in `prefers-reduced-motion`.

For a business that makes sound, make the scene's objects pressable and let them play
sound, with a mute control, so people explore rather than scroll.

## 8. Recompose for phones

Treat each section as its own composition on a small screen.

- Give the hero scene a phone crop through `<picture>` (a 390 by 546 px portrait crop
  with the characters larger), or move the illustration above the headline, or box it
  inside the margins. Crop; do not shrink.
- Drop the H1 to about 35 to 48 px and keep body text at its desktop size; set type
  readable on every screen and rarely enlarge it as screens grow.
- Use 18 to 27 px side margins.
- Turn one or two groups that sat side by side on desktop (images, quotes, a timeline,
  related links) into a horizontal scroll-snap row, and stack the rest: below a
  container width of `48rem`, each item `85%` wide so the next one shows at the edge,
  often with a progress bar under the row.
