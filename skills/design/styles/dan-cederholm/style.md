# Dan Cederholm: handcrafted bits

Build a plain, sturdy page, then make it warm with small handmade bits: a display face
that came from an old label, one orange, a badge, a joke. Distilled from Dan Cederholm's
(SimpleBits, co-founder of Dribbble) own sites and goods, his talks and articles, and
other people's accounts. Written in our own words.

- **Feels like:** cream paper, one warm orange, chunky caps with inky edges, a calm
  column of comfortable text, a badge or a lightning bolt, copy that makes you smile a
  little.
- **Fits:** makers and small shops, studios, side projects, personal sites, and
  galleries or marketplaces of other people's work (in frame mode, below).

The page is built the way he describes building CSS: a sound base first, then layers of
enrichment, each one optional for the layer below. Work through the layers in order and
keep a drawer of small named patterns as you go.

## Choose the mode first

Ask whose work the page shows.

- **Your voice.** The business is the subject (a shop, a studio, a maker). The signature
  runs at full strength everywhere except the reading column.
- **Frame mode.** The page shows other people's work (a gallery, a marketplace, a
  portfolio of many hands). Keep the interface nearly monochrome, in one plain sans, with
  simple glyphs. Take one accent from the logo. Put the personality in the mark, the
  names of things and the copy. Holding back is the hard part; hold back.

Write the mode in the brief.

## Find the object

Before any layout, find one real object from the business's ordinary world whose
lettering or shape the brand can grow from: a luggage label, a cigar box, a manhole
cover.

- Name it in the brief, with the quirks you will keep (an odd crossbar, a
  rounded-but-rough edge).
- Take the display type, the badge and the palette from it. Keep its quirks; do not tidy
  them away.
- Ask whether the idea makes you laugh a little.

## Layer 1: the X-ray

Write the content and set it with no styling at all. Read it as a plain document.

- Question each element. Cut what does not earn its place before anything is styled.
- Every later layer must leave the content usable if that layer fails to load.
- Write the copy from the subject's own world: its trade terms, its prices, its dates, the
  names of its things.
- Let the voice be dry and a bit self-deprecating. Name things with care; a slightly
  misspelled or punning name is fine when it makes the thing its own. Keep jokes in plain
  type; the words carry them.

## Layer 2: a quiet structure

Lay the page out plainly so the warm bits have somewhere calm to sit.

- One centred column, or one main column and a narrow side column.
- Repeat the same few patterns down the page instead of inventing a new layout per
  section.
- Keep the reading field clean. Decoration goes to the edges: a patterned or textured
  border along the top, the sides or the foot of the page, never behind the text.
- Set navigation as short items with a plain second line saying what is behind each:
  "WORK / things we made".
- Keep the layout flexible. It must survive larger text and a missing image without
  breaking.

## Layer 3: the warm bits

This is where the page becomes his. Every bit is small; together they are the signature.

### Type

- **Two faces, two jobs.** A plain, sturdy text face (a humanist or grotesque sans such
  as he uses) and one characterful display face in caps.
- **The display face has a source in the world.** Chunky caps from vintage commercial
  lettering, or condensed caps; a rough (worn, inky) or soft (rounded) finish is
  welcome. Pick it from the object you found. In frame mode the only display type may be
  the mark, and it may be a script, as Dribbble's was.
- **Text is comfortable**: about 20px, line-height about 1.5.
- **Small letterspaced caps for navigation and metadata**: very small, tracked about 0.1
  to 0.2em, in the signature colour or a muted ink, with inactive items faded. A
  section's heading may itself be set this way with an arrow after it, "LATEST
  ROASTS →", when the section is an index. Never stack such a label above another
  heading.
- **The ampersand is an ornament.** Set a big italic or display ampersand as an object
  on its own (a print), or in small utility text. Keep it out of headlines.

### Colour

- **One warm signature colour**, an orange or red-orange, used for links, arrows, the
  badge, a drop cap, an end mark. It is the brand's thread; once chosen, it stays
  through every redesign.
- **A warm ground**: cream, beige or warm off-white rather than white.
- **Around them, a few flat colours** from the object: mustard, navy, teal, forest green.
  Three to five in all, flat, no gradients, as if printed in a few inks.

### Ornament

- **Small icons and glyphs** beside dates and links: a lightning bolt, a pointing hand, a
  cube. Flat, drawn in the palette.
- **Braces** round the current item or a date.
- **A badge** for the business: a round mark with the name and a line running round the
  rim, or a pastiche of a mark everyone in its world knows, rebuilt with the business's
  own name and a pun.
- **Texture** on the display type or at the page's edges: grain, ink spread, a pattern
  border. Not under text.

### Imagery

- **Show the real things.** A still life of the business's own objects, laid out on the
  ground colour as if on a table: its products, tools, labels.
- **The specimen block** shows the voice: a field packed edge to edge with words from
  the trade (names, prices, dates, terms), the outer ones cropped by the frame, each
  line set whole in its own size, weight and colour, small icons between. Use it as a
  hero or a poster; never change treatment inside one line.

## Layer 4: enrichment

Add the finish last, as a reward for capable browsers and big screens. Nothing here may
carry content or structure.

- Softened corners on controls and single objects, a gentle shadow under a lifted thing,
  translucent colour where layers meet.
- Hover and focus share one treatment: a colour shift or a small lift or tilt, about
  0.3s. Snappy actions stay snappy.
- Move only what invites a hand: a link, a button. Do not animate the page.

## The pattern drawer

Design one strong version of each pattern the page needs, name it, and repeat it. These
are his usual ones.

| Pattern       | What it is                                                                        |
|---------------|-----------------------------------------------------------------------------------|
| Slat          | Title, one line, date or tag, linking through; a ruled row, never a box           |
| Label         | Tiny tracked caps for nav and meta, with an optional lowercase second line        |
| Index heading | A section heading set as small tracked caps with an orange arrow, for index lists |
| Badge         | Round mark, name in the display face, a line round the rim                        |
| Specimen      | Edge-to-edge words from the trade, each line its own treatment, cropped at edges  |
| Still life    | The business's objects laid out flat on the ground colour                         |
| Edge border   | A pattern or texture strip along the page edge, framing the clean column          |
| End mark      | A small glyph in the signature colour closing a piece of text                     |

## Phones: baby steps

Adapt the same page; do not design a second site.

- Stack the items that sat side by side. Set short vertical lists in columns where they
  fit.
- Hide as little as possible. Content on the desktop is content on the phone.
- Set breakpoints where the content breaks, often only one.

## Ship it, then refine

Never perfect. Ship the sound version, then improve it in small steps.

- When redesigning an existing brand, keep a trace of every earlier version: the
  colour, a shape from the old mark. Refine the mark; do not restart it.

## Deeper reference

- `synthesis.md`: the full design model, each point citing its note, with the ban
  conflicts and the gaps in the research.
- `notes/own.md`: simplebits.com from 2005 to 2026, his fonts and newsletter.
- `notes/work.md`: products and goods, the specimen posters and badges.
- `notes/talks.md`: talks, articles and interviews: process, enrichment, motion.
- `notes/accounts.md`: what peers and reviewers say about his style and method.
