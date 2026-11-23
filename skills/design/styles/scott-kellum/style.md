# Scott Kellum: draw the masters, design the space between

Design a site the way a type designer draws a variable family: decide the ends, then the
curve between them, so every size in between is designed rather than left to chance.
Distilled from Scott Kellum's freely published writing, talks, his own and client sites,
and other people's accounts. Written in our own words.

A page made this way reads as type first: a characterful serif speaking at large sizes, a
condensed or width-shifting display voice, warm dark grounds or single flooding colours,
the grid drawn as fine construction lines, and type that keeps its proportions as the
window narrows. It suits studios, publishers, guides, type and tool makers, and
businesses whose product is something people read or a voice they carry. It suits
poorly a business that has little to say and needs its photographs to sell.

## The model

A typeface designer draws a few masters (thinnest and heaviest, smallest and largest
optical size) and the font interpolates every instance between them. Treat the site the
same way:

- The site has **dimensions**: container width first, then the reader's font size,
  light and dark, scroll depth. A phone screen and a desktop screen are two slices of one
  object.
- Each **role** (body text, lede, page head, item title, price, caption, button) is
  designed at its two **masters**: its narrowest container and its widest.
- Everything between is **interpolated along a curve** you choose, per property.
- Judge the result as a family: a beautiful group of components, not a group of
  beautiful components. One part that looks right in one slot and wrong in another is a
  bad part.

There is no separate phone pass. The phone is the narrow master and gets as much design
as the wide one.

## 1. Talk before drawing

Branding is a conversation about what the business is now and what it should become.
Write the answers in the brief before any type is set:

1. **What it is now and what it should become**, in two plain sentences.
2. **Content before brand.** List what the site must hold and how people move through it.
   Design the home for the content first; the brand comes second.
3. **The category's defaults.** List the colours and faces the business's competitors use.
   Take the other side: if the trade is blue sans, go bright and serif; if it is beige
   and script, go dark and engineered.
4. **One specific source** the business can own: a period (deco, a 1970s timetable), a
   book (a children's star atlas), an object in the shop, the trade's own diagrams. Use
   one source, named in the brief.
5. **Split the jobs.** Give each element one quality to carry and write it down:
   - the mark carries expression;
   - the grid carries competence;
   - colour carries the feeling (optimism, warmth, calm).
   An element asked to carry everything carries nothing.

## 2. Choose faces like a type designer

Choose by utility first, then by character.

1. **Utility.** For each candidate, check: optical-size range, width range, weight range,
   spacing, the languages the site needs, which axes are variable, quality, licence. A
   face with real width and weight axes earns a place because the space between masters
   can use them.
2. **Character.** Then choose among the survivors by voice: professional or casual,
   classic or of its moment, widely used or rare. More character in letterforms often
   reads better, not worse; refuse the most neutral face as the safe one.
3. **Three voices**, each with one job:
   - a **text serif** with personality at large sizes (it will also set the lede);
   - a **display face** with a width or weight range, often condensed and heavy, for
     titles, the name and navigation;
   - a **utility voice** (a mono, or the display face small) for prices, times, captions
     and labels.
   Two can be enough; never four.
4. Prefer **independent foundries' variable families** and serifs for the brand's voice.
   Pick a text serif that could outlast the next three redesigns.
5. Where the client's values call for it (an open-source project, a cooperative), use an
   openly licensed face.

## 3. Draw the masters for each role

For each role, write its two masters in the brief as a small table: container width,
size, line height, weight, width axis, letter-spacing, and any other axis.

- **Body text** is as big as possible as soon as possible: reach full reading size early
  and hold it; shrink only at the very narrow end. Never below 16px. Measure about 60
  characters.
- **Headlines** stay modest through mid widths and grow fast at the wide end.
- **Hierarchy contrast scales with the space.** At the wide master, big heavy heads over
  small text; at the narrow master, move the ratio toward 1:1. Do not shrink the wide
  scale proportionally onto the phone.
- **Line height follows line length.** Longer lines get more leading. Heads tight
  (1 to 1.1), text loose (1.4 to 1.6), and both move with the measure. If the type looks
  off, fix the line height first.
- **Axes follow size.** Interpolate weight, width and optical size with the size: a head
  may be condensed and heavy in a narrow slot and wide and lighter in a wide one; a face
  may gain serif or contrast as it grows.
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

  ```css
  .slot { container-type: inline-size; }
  .slot h2 {
    animation: item-title 1s cubic-bezier(.6, 0, .9, .4) paused both;
    /* 100cqi divided by 1px: unit division, so the width becomes a number */
    animation-delay: calc(tan(atan2(100cqi, 1px)) / 1200 * -1s);
  }
  @keyframes item-title {
    from { font-size: 1.5rem;  line-height: 1.1;  font-variation-settings: "wdth" 70; }
    to   { font-size: 4.5rem;  line-height: 0.95; font-variation-settings: "wdth" 110; }
  }
  ```

  Here 1200 is the container width in px at which the wide master is reached. Make the
  `from` keyframe a complete, readable setting, so a browser that ignores the trick still
  shows the narrow master.
- The same width number may drive anything animatable: a hue, a column ratio, the angle
  of a colour split. Use that only where it says something about the business.

## 5. Let the type say what a thing is

Give each kind of content its own typographic thread (face, weight, width, case, colour)
and keep it at every size, so a reader knows an event from an article from a product
without being told.

- No category tags, badges or labels stamped above headings to sort content; the type
  does the sorting.
- Keep the range of styles the content needs. Do not flatten every kind into one card
  title to avoid the work.

## 6. Compose the page

Pick the moves the content calls for; none is required.

- **The lede is the opening.** For a studio, a publisher or anyone whose voice is the
  product, open on a paragraph of the text serif at lede size (about 2 to 2.5 times body
  at the wide master) filling the first screen. No hero image, no slogan headline, no
  button. Nothing stamped above it; the name lives in the navigation.
- **Draw the grid.** Mark column edges with hairlines one step off the ground colour,
  running past the content to the viewport edges and crossing at section joins like
  construction lines. Dashed inner guides may mark columns inside a figure. Keep them
  quiet enough to read as texture.
- **Unequal columns, set as ratios** (2:4:3, a 2:8:2 triptych), with a central measure
  such as `1fr min(50rem, 90%) 1fr`.
- **A map of where you are.** For guides, documentation, menus, timetables and anything
  long, keep a rail listing every section, grouped under small coloured group names,
  visible while reading. On a narrow container it becomes a strip that stays in reach.
- **Loud brand, quiet reading.** Flood the home and index with the brand colour; set
  reading pages plain, dark on light or light on dark, in the text face.
- **One item per row** for short lists (work, posts, products): an image on one side,
  its title beside it in the heavy display face sitting on a hairline, a sentence of
  serif summary under it. The text sits on the ground, never in a box.
- **Leaf corners.** Square images with two opposite corners rounded large and two left
  square (`border-radius: 0.1px 4rem`).
- **A diagonal colour split** across the ground between two colours, shifting with
  scroll or width, for movement on a page with almost no imagery.
- **A small floating navigation pill**: the mark, two or three links, over a blurred
  shape. A vertical line of plain fact (hours, an address, a running count) may run up
  one margin.
- **Specimen moves** where type is the subject: one long word at display size running
  off the edge, with a small spaced-capital caption beside it naming what it is.

## 7. Colour

- Use **strong single colours as fields**: a whole page or section in gold, butter yellow,
  teal, deep green, brown or magenta, not a tint used evenly everywhere.
- His own taste is **warm dark**: brown or deep green near black, pale pink or cream type,
  one hot accent (orange, signal red). Use it when the brand's job allows; take the exact
  colours from the source in §1.
- Draw rules and grid lines in a colour one step off the ground (on #371506, #522200).
- When a mark lives inside other apps, let the **shape** carry identity and let light and
  dark modes take opposite palettes (warm in light, cool in dark).
- In print, collapse to black on white, drop sticky navigation, fix heading sizes.

## 8. Images and objects

- No stock photography. Use the business's own material, or make images: saturated
  **collage and overprint** (magenta, cyan, yellow, mesh distortion, pattern), or a
  **period illustration** from the source in §1 (a star chart, a deco frame, an
  engraving). In SVG, overprint is flat shapes in `mix-blend-mode: multiply` or `screen`.
- **Type as material.** Make artifacts with the business's type: a label, a stamp, tape,
  a badge that completes a word. Show them as objects.
- A specimen or a diagram may become something the reader moves through (a slider along
  an axis, a scene that zooms with the window).

## 9. Motion

- **Ambient motion from primes.** Several slow loops with prime-number durations (7s,
  11s, 13s) so they rarely line up and read as organic.
- **Honest parallax**: real 3D perspective, near layers passing faster than far ones. No
  scroll hijacking.
- Width is a motion axis too: a resized window may zoom a drawn scene or inflate a font
  along its weight axis.
- Respect `prefers-reduced-motion` for every loop.

## 10. Ship small

- Set a weight budget and keep to it; his own site once fit 14kb. Few files, system
  defaults where they serve, no resets for their own sake.
- Write a print stylesheet.
- Spend design effort on the two or three places that carry the business (the home, the
  signature format) and reuse plain parts elsewhere.

## Refuse

- Type that snaps between two or three fixed sizes at breakpoints; per-slot headline
  overrides; a phone layout that is the desktop scale shrunk evenly.
- Linear `vw` or `clamp()` ramps as the whole fluid system.
- A modular scale used as a menu of sizes; an 8pt or baseline grid forced on everything.
- The most neutral face chosen as the safe one; one sans in two weights for everything.
- Category tags and badges doing the type's job; any label stamped above a heading or
  above the lede.
- Word-level emphasis inside a heading: no word in another colour, weight, width or face.
  Interpolated axes apply to the whole line.
- Hero image, slogan and button as the opening; stock photography; uniform rounded cards
  in a three-column grid.
- Scroll jacking; parallax faked with background offsets.

## Judge it

Drag the window from narrow to wide, or read the masters and curves in the source, and
answer each in one line:

- What are the two masters of the page head, the body and the item title, and does each
  read well at both ends and in the middle?
- Does the heading-to-body ratio close toward 1:1 on the narrow master?
- Does line height grow with line length?
- Does any type size come from a breakpoint jump or a per-slot override?
- Can a reader tell each kind of content by its type alone, with no label?
- What jobs did the mark, the grid and the colour each get, and does each carry only its
  own?
- What is the category default, and which side did this design take?
- Is the grid visible, and does it read as construction rather than borders?
- Could this belong to another business in the same trade? If yes, what is generic?

## Deeper reference

- `synthesis.md`: the full model, each point citing its note, with cautions and the
  moves this file adjusts for the bans.
- `notes/own.md`: his sites from 2010 to now, their CSS, his essays and teaching.
- `notes/work.md`: client and product work, per-project table.
- `notes/talks.md`: talks and interviews on fluid type, the typographic map, curves.
- `notes/accounts.md`: what other people report and the critiques on record.
