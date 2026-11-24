# Scott Kellum: draw the masters, design the space between

Design a site the way a type designer draws a variable family: decide the ends, then the
curve between them, so every size in between is designed rather than left to chance.
Distilled from Scott Kellum's freely published writing, talks, his own and client sites,
and other people's accounts. Written in our own words.

A page made this way reads as type first: a characterful serif speaking at large sizes, a
condensed or width-shifting display voice, warm dark grounds or single flooding colours,
the grid drawn as fine construction lines, and type that keeps its proportions as the
window narrows. It suits studios, publishers, guides, type and tool makers, and
businesses whose product is something people read or a voice they carry.

## The model

A typeface designer draws a few masters (thinnest and heaviest, smallest and largest
optical size) and the font interpolates every instance between them. Treat the site the
same way:

- The site has **dimensions**: container width, the reader's font size, light and dark,
  scroll depth. A phone screen and a desktop screen are two slices of one object.
- Each **role** (body text, lede, page head, item title, price, button) is designed at its
  two **masters**: its narrowest container and its widest.
- Everything between is **interpolated along a curve** you choose, per property.
- Judge the result as a family: a beautiful group of components, not a group of
  beautiful components.

There is no separate phone pass. The phone is the narrow master and gets as much design
as the wide one.

## 1. Talk before drawing

Branding is a conversation about what the business is now and what it should become.
Write the answers in the brief:

1. **What it is now and what it should become.**
2. **Content before brand.** Design the home for the content first; the brand comes
   second.
3. **The category's defaults.** List the colours and faces the business's competitors use.
   Take the other side: if the trade is blue sans, go bright and serif.
4. **One specific source**: a period (deco), a book (a children's star atlas). Use one
   source, named in the brief.
5. **Split the jobs.** Give each element one quality to carry and write it down:
   - the mark carries expression;
   - the grid carries competence;
   - colour carries the feeling (optimism).

## 2. Choose faces like a type designer

Choose by utility first, then by character.

1. **Utility.** For each candidate, check: optical-size range, width range, weight range,
   spacing, the languages the site needs, which axes are variable, quality.
2. **Character.** Then choose among the survivors by voice: professional or casual,
   classic or of its moment, widely used or rare. More character in letterforms often
   reads better, not worse; refuse the most neutral face as the safe one.
3. **Three voices**, each with one job:
   - a **text serif** with personality at large sizes (it will also set the lede);
   - a **display face** with a width or weight range, often condensed and heavy, for
     titles and navigation;
   - a **utility voice** (a mono).
4. Prefer **independent foundries' variable families** and serifs for the brand's voice.
   Pick a text serif that could outlast redesigns.
5. Where the client's values call for it (an open-source project), use an openly licensed
   face.

## 3. Draw the masters for each role

For each role, write its two masters in the brief: container width, size, line height,
weight, width axis, and any other axis.

- **Body text** is as big as possible as soon as possible: reach full reading size early
  and hold it; shrink only at the very narrow end. Never below 16px. Measure about 60
  characters.
- **Headlines** stay modest through mid widths and grow fast at the wide end.
- **Hierarchy contrast scales with the space.** At the wide master, big heavy heads over
  small text; at the narrow master, move the ratio toward 1:1. Do not shrink the wide
  scale proportionally onto the phone.
- **Line height follows line length.** Longer lines get more leading. Heads tight, text
  loose, and both move with the measure. If the type looks off, fix the line height
  first.
- **Axes follow size.** Interpolate weight, width and optical size with the size: a head
  may be condensed and heavy in a narrow slot and wide and lighter in a wide one; a face
  may gain serif as it grows.
- **Balance** heads and ledes (`text-wrap: balance`).
- Use proportions, not a fixed unit grid. No 8pt grid, no baseline grid; keep a shared
  baseline only where text columns sit side by side. Size in `em` and `rem` so the whole
  page rescales from the root and from the reader's own font setting.

## 4. Set the curve between

Every size between the masters comes from one rule per role, driven by the width of the
**container the element sits in**, not the viewport. The same item title in a sidebar and
in a full-width list comes from the same rule.

- Use an eased curve, not a straight line. A linear `clamp()` or `vw` ramp is the default
  to beat: it shrinks body text too soon and grows heads too early.
- Write no per-slot overrides and no breakpoint jumps for type.
- Plain CSS can do it: make the slot a size container, compute the container's width as
  a number, and scrub a paused animation with it. The animation's timing function is the
  curve.
- The same width number may drive anything animatable: a hue, a column ratio.

## 5. Let the type say what a thing is

Give each kind of content its own typographic thread (face, weight, width, case) and keep
it at every size, so a reader knows without being told.

- No category tags, badges or labels stamped above headings to sort content; the type
  does the sorting.
- Keep the range of styles the content needs. Do not flatten every kind into one card
  title to avoid the work.

## 6. Compose the page

Pick the moves the content calls for; none is required.

- **The lede is the opening.** For a studio or anyone whose voice is the product, open on
  a paragraph of the text serif at lede size filling the first screen. No hero image, no
  slogan headline, no button. Nothing stamped above it; the name lives in the
  navigation.
- **Draw the grid.** Mark column edges with hairlines one step off the ground colour,
  running past the content to the viewport edges and crossing at section joins like
  construction lines. Dashed inner guides may mark columns. Keep them quiet enough to
  read as texture.
- **Unequal columns, set as ratios** (2:4:3, a 2:8:2 triptych), with a central measure
  such as `1fr min(50rem, 90%) 1fr`.
- **A map of where you are.** For guides, documentation and anything long, keep a rail
  listing every section, grouped under small coloured group names, visible while
  reading.
- **Loud brand, quiet reading.** Flood the home and index with the brand colour; set
  reading pages plain, dark on light or light on dark, in the text face.
- **One item per row** for short lists (work, posts): an image on one side, its title
  beside it in the heavy display face sitting on a hairline, a sentence of serif summary
  under it. The text sits on the ground, never in a box.
- **Leaf corners.** Square images with two opposite corners rounded large and two left
  square (`border-radius: 0.1px 4rem`).
- **A diagonal colour split** across the ground between two colours, shifting with
  scroll, for movement on a page with almost no imagery.
- **A small floating navigation pill**: the mark, two links, over a blurred shape. A
  vertical line of plain fact may run up one margin.
- **Specimen moves** where type is the subject: one long word at display size running
  off the edge, with a small spaced-capital caption beside it naming what it is.

## 7. Colour

- Use **strong single colours as fields**: a whole page or section in gold, butter yellow,
  teal, deep green, brown or magenta, not a tint used evenly everywhere.
- His own taste is **warm dark**: brown or deep green near black, pale pink type, one hot
  accent (orange).
- Draw rules and grid lines in a colour one step off the ground (on #371506, #522200).
- When a mark lives inside other apps, let the **shape** carry identity and let light and
  dark modes take opposite palettes (warm in light, cool in dark).
- In print, collapse to black on white, drop sticky navigation, fix heading sizes.

## 8. Images and objects

- No stock photography. Use the business's own material, or make images: saturated
  **collage and overprint** (magenta, cyan, yellow, mesh distortion, pattern), or a
  **period illustration** from the source in §1 (a star chart, a deco frame, an
  engraving).
- **Type as material.** Make artifacts with the business's type: tape, a badge that
  completes a word. Show them as objects.
- A specimen or a diagram may become something the reader moves through (a slider along
  an axis, a scene that zooms with the window).

## 9. Motion

- **Ambient motion from primes.** Several loops with prime-number durations so they
  rarely line up and read as organic.
- **Honest parallax**: real 3D perspective, near layers passing faster than far ones. No
  scroll hijacking.
- Width is a motion axis too: a resized window may zoom a drawn scene or inflate a font
  along its weight axis.

## 10. Ship small

- Set a weight budget and keep to it; his own site once fit 14kb. System defaults where
  they serve, no resets.
- Write a print stylesheet.
- Spend design effort on the places that carry the business (the home, the signature
  format) and reuse plain parts elsewhere.

## Refuse

- Type that snaps between two or three fixed sizes at breakpoints; per-slot headline
  overrides; a phone layout that is the desktop scale shrunk evenly.
- Linear `vw` or `clamp()` ramps as the whole fluid system.
- A modular scale used as a menu of sizes; an 8pt or baseline grid forced on everything.
- The most neutral face chosen as the safe one; one sans in two weights for everything.
- Category tags and badges doing the type's job; any label stamped above a heading or
  above the lede.
- Hero image, slogan and button as the opening; stock photography; uniform rounded cards
  in a three-column grid.
- Scroll jacking.

## Deeper reference

- `synthesis.md`: the full model, each point citing its note, with cautions and the
  moves this file adjusts for the bans.
- `notes/own.md`: his sites from 2010 to now, their CSS, his essays and teaching.
- `notes/work.md`: client and product work, per-project table.
- `notes/talks.md`: talks and interviews on fluid type, the typographic map, curves.
- `notes/accounts.md`: what other people report and the critiques on record.
