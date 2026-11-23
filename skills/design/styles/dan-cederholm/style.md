# Dan Cederholm: handcrafted bits

Build a plain, sturdy page, then make it warm with small handmade bits: a display face
that came from an old label, one orange, a badge, a joke. Distilled from Dan Cederholm's
(SimpleBits, co-founder of Dribbble) own sites and goods, his talks and articles, and
other people's accounts. Written in our own words.

- **Feels like:** a small shop with a hand-painted sign. Cream paper, one warm orange,
  chunky caps with inky edges, a calm column of comfortable text, a badge or a lightning
  bolt in the corner, copy that makes you smile a little.
- **Fits:** makers and small shops, cafés and roasters, hardware and trade businesses,
  type and print studios, clubs, side projects, personal sites, and galleries or
  marketplaces of other people's work (in frame mode, below).
- **Fits poorly:** businesses that must look neutral and institutional, and dense
  application interfaces.

The page is built the way he describes building CSS: a sound base first, then layers of
enrichment, each one optional for the layer below. Work through the layers in order and
keep a drawer of small named patterns as you go.

## Choose the mode first

Ask whose work the page shows.

- **Your voice.** The business is the subject (a shop, a studio, a maker). The signature
  runs at full strength everywhere except the reading column.
- **Frame mode.** The page shows other people's work (a gallery, a member directory, a
  marketplace, a portfolio of many hands). Keep the interface nearly monochrome, in one
  plain sans, with simple glyphs. Take one accent from the logo and use it for actions
  and the current item only. Put the personality in the mark, the names of things and
  the copy: invent a small vocabulary from the community's world, the way Dribbble's
  came from basketball. Holding back is the hard part; hold back.

Write the mode in the brief.

## Find the object

Before any layout, find one real object from the business's ordinary world whose
lettering or shape the brand can grow from: a luggage label, a cigar box, a manhole
cover, a seed packet, a feed-store sign, a ticket stub, a hardware tag, a ballpark
scorecard, a delivery van's door.

- Name it in the brief, with the two or three quirks you will keep (an odd crossbar, a
  rounded-but-rough edge, a slanted stroke, a lightning bolt).
- Take the display type, the badge and the palette from it. Keep its quirks; do not tidy
  them away.
- Ask whether the idea makes you laugh a little. If it does not amuse anyone, find a
  better object.

## Layer 1: the X-ray

Write the content and set it with no styling at all. Read it as a plain document.

- Question each element. Cut what does not earn its place before anything is styled.
- Put the content in a sensible reading order. Every later layer must leave it usable if
  that layer fails to load.
- Write the copy from the subject's own world: its trade terms, its prices, its dates, the
  names of its things. No placeholder text, ever.
- Let the voice be dry and a bit self-deprecating, the way a shopkeeper talks about the
  shop. Name things with care; a slightly misspelled or punning name is fine when it
  makes the thing its own. Keep jokes in plain type; the words carry them.

## Layer 2: a quiet structure

Lay the page out plainly so the warm bits have somewhere calm to sit.

- One centred column, or one main column and a narrow side column. A single reading
  column of about 30 to 36em is his recent habit.
- Repeat the same few patterns down the page instead of inventing a new layout per
  section.
- Keep the reading field clean. Decoration goes to the edges: a patterned or textured
  border along the top, the sides or the foot of the page, never behind the text.
- Set navigation as short items with a plain second line saying what is behind each:
  "WORK / things we made".
- Keep the layout flexible. It must survive larger text, longer words and a missing
  image without breaking.

## Layer 3: the warm bits

This is where the page becomes his. Every bit is small; together they are the signature.

### Type

- **Two faces, two jobs.** A plain, sturdy text face (a humanist or grotesque sans such
  as he uses, or a sturdy serif) and one characterful display face in caps.
- **The display face has a source in the world.** Chunky caps from vintage commercial
  lettering, condensed poster caps, or a rounded slab; a rough (worn, inky) or soft
  (rounded) finish is welcome. Pick it from the object you found. In frame mode the
  only display type may be the mark, and it may be a script, as Dribbble's was.
- **Text is comfortable**: about 18 to 20px, line-height about 1.5, dark warm grey or
  brown on cream.
- **Small letterspaced caps for navigation and metadata**: very small, tracked about 0.1
  to 0.2em, in the signature colour or a muted ink, with inactive items faded. A
  section's heading may itself be set this way with an arrow after it, "LATEST
  ROASTS →", when the section is an index. Never stack such a label above another
  heading.
- **The ampersand is an ornament.** Set a big italic or display ampersand as an object
  on its own (a mark, a print, a divider), or in small utility text. Keep it out of
  headlines.

### Colour

- **One warm signature colour**, an orange or red-orange, used for links, arrows, the
  badge, a drop cap, an end mark, the current nav item. It is the brand's thread; once
  chosen, it stays through every redesign.
- **A warm ground**: cream, beige or warm off-white rather than white.
- **Around them, a few flat colours** from the object: mustard, navy, teal, forest green,
  brick. Three to five in all, flat, no gradients, as if printed in a few inks.

### Ornament

- **Small icons and glyphs** beside dates, links and practical facts: a lightning bolt, a
  pointing hand, a star, a cube. One line weight, flat, drawn in the palette.
- **Braces or brackets** round the current item or a date may stand in for an icon:
  `{ NOW OPEN }`.
- **A badge** for the business: a round or shield-shaped mark with the name and a line
  running round the rim ("NEVER PERFECT SINCE 1987"), or a pastiche of a mark everyone
  in its world knows, rebuilt with the business's own name and a pun.
- **Texture** on the display type or at the page's edges: grain, ink spread, a pattern
  border. Not under text.

### Imagery

- **Show the real things.** A still life of the business's own objects, laid out on the
  ground colour as if on a table: its products, tools, labels, tickets. In a preview
  with no photographs, draw them as flat SVG objects in the palette.
- **The specimen block** shows the voice: a field packed edge to edge with words from
  the trade (names, prices, dates, terms), the outer ones cropped by the frame, each
  line set whole in its own size, weight and colour, small icons between. Use it as a
  hero, a band or a poster; never change treatment inside one line.

## Layer 4: enrichment

Add the finish last, as a reward for capable browsers and big screens. Nothing here may
carry content or structure.

- Softened corners on controls and single objects, a gentle shadow under a lifted thing,
  translucent colour where layers meet.
- Hover and focus share one treatment: a colour shift or a small lift or tilt, about
  0.2 to 0.3s. Snappy actions stay snappy.
- Move only what invites a hand: a link, a button, a badge, a sticker. Do not animate the
  page. Respect reduced motion.

## The pattern drawer

Design one strong version of each pattern the page needs, name it, and repeat it. These
are his usual ones.

| Pattern        | What it is                                                                          |
|----------------|-------------------------------------------------------------------------------------|
| Slat           | Glyph, title, one line, date or tag, linking through; a ruled row, never a box      |
| Label          | Tiny tracked caps for nav and meta, with an optional lowercase second line          |
| Index heading  | A section heading set as small tracked caps with an orange arrow, for index lists   |
| Badge          | Round or shield mark, name in the display face, a line round the rim                |
| Specimen       | Edge-to-edge words from the trade, each line its own treatment, cropped at edges    |
| Still life     | The business's objects laid out flat on the ground colour                           |
| Edge border    | A pattern or texture strip along the page edge, framing the clean column            |
| End mark       | A small glyph in the signature colour closing a piece of text                       |
| Fact line      | Hours, address, price or date with a small glyph before it                          |

## Phones: baby steps

Adapt the same page; do not design a second site.

- Stack the items that sat side by side. Set short vertical lists (hours, links, sizes)
  in two columns where they fit.
- Hide as little as possible. Content on the desktop is content on the phone.
- Set breakpoints where the content breaks, often only one.
- Keep the warm bits: the badge, the signature colour, the display face, the edge border.
  The specimen block may lose its outer words to the crop.

## Ship it, then refine

Never perfect. Ship the sound version, then improve it in small steps.

- When redesigning an existing brand, keep a trace of every earlier version: the
  colour, a shape from the old mark, a phrase. Refine the mark; do not restart it.
- Before calling it done, answer each in one line:
  - Which mode is it, and does the frame stay out of the content's way?
  - What is the object, and which of its quirks survive in the type and badge?
  - Does the page still read as a plain document with the styles gone?
  - Where is the one signature colour, and is it the only loud colour?
  - Where is the decoration, and is the reading field clean?
  - Which patterns repeat, and is any of them a box round each item?
  - Does it make you laugh a little, without a joke built as a setup and payoff?
  - Could this belong to another shop in the same trade? If yes, what is generic?

## Deeper reference

- `synthesis.md`: the full design model, each point citing its note, with the ban
  conflicts and the gaps in the research.
- `notes/own.md`: simplebits.com from 2005 to 2026, his fonts and newsletter.
- `notes/work.md`: products and goods, the specimen posters and badges.
- `notes/talks.md`: talks, articles and interviews: process, enrichment, motion.
- `notes/accounts.md`: what peers and reviewers say about his style and method.
