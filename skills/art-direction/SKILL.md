---
name: art-direction
description: >-
  Art-direct a website or page so it carries one concept specific to its business
  instead of the templated default (centred hero, three cards, CTA band), using a method
  distilled from Andy Clarke's public work. TRIGGER on "art-direct this site/page",
  "make it look designed, not templated", "give this homepage a concept", "editorial or
  magazine-style layout", "Andy Clarke style", or reviewing whether a design could belong
  to any business. DO NOT TRIGGER for stripping AI tells from finished work (de-slop),
  comparing rendered options (study), CSS bugs, or charts.
---

# Art direction

A templated site is assembled from known parts: a centred photo hero with a headline and
a button, three equal feature cards, a stats strip, testimonials, a CTA band, one evenly
divided grid with the same rhythm in every section, and stock or generated imagery. Each
part is reasonable; together they carry no idea, so the site says nothing about the
business. Art direction finds what this business means and makes the design carry it.

Familiar patterns are allowed. A twelve-column grid, a hero or a row of cards is fine
when chosen on purpose for this business. A pattern chosen only because it is familiar
is the failure. An unusual move with no idea behind it reads as random and becomes a new
cliché.

## Menu

| Operation         | Steps | Use when                                                   |
|-------------------|-------|------------------------------------------------------------|
| Art-direct a site | A1–A7 | designing a new site or page, or redesigning a generic one |
| Review a design   | V1–V2 | judging a design, mockup or built page before acceptance   |

Both operations end with the completion contract. The move catalogue is in
[references/moves.md](references/moves.md); read it at A6. The research behind the method
is indexed in [references/README.md](references/README.md); read
[references/synthesis.md](references/synthesis.md) when a step needs the reasoning or a
worked example.

## Art-direct a site

Work in this order. Each step feeds the next, and code comes only after A6.

- **A1. Gather the business and its content.** Hold one intake conversation with the
  owner, or ask the user for what the owner would say. Gather the content and rewrite it
  before designing; never design against placeholder text. Storyboard what a visitor
  discovers, in what order. A brief states goals, problems and hopes, never solutions;
  treat a "sites we like" list as context, not a target. Never invent facts about the
  business. **Wait** for the owner's or user's answers when the content or the A2 sources
  are missing.

- **A2. Find the concept.** A concept is one idea, specific to this business, that the
  design carries in its imagery, type, colour, composition and a few interface details.
  Look in these five places:

  | Source                                   | Ask                                                           | Example                                                        |
  |------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
  | What the business already owns           | Which logo, sign, card, packaging, place names do you have?   | A council's thirteen village names, stacked, become the hero   |
  | What the owner keeps returning to        | What do you love, collect, read, keep mentioning?             | A composer's tape machines become the site's audio players     |
  | What customers really buy                | What do people buy from you, one level above the product?     | An investment firm sells confidence, so no buildings are shown |
  | The trade's mechanics, taken literally   | What does your product physically do? Say your line literally | Printhead supplier: famous paintings rebuilt from QR codes     |
  | A field that already made people feel it | Who else made people feel what you need them to feel?         | Youth politics borrows protest and gig-poster language         |

  - Take the concept from what the owner keeps coming back to, not from what you like.
  - Study competitors only to list their clichés, then avoid them.
  - Treat a mundane trade as a good brief: every business has a story worth telling.

- **A3. Pin the concept down.** Write each of these in the design record:
  1. **One line.** List true things about the business, keep the one that is theirs
     alone and hard to argue with, and state it in one line. It is a design tool first;
     production copy still follows the project's copy rules.
  2. **Three or four feeling words** (for example bold, warm, precise, cheeky). Turn each
     into concrete choices: a colour temperature, a type weight, a motion speed.
  3. **One test question** every later decision must pass, taken from what customers
     really buy: "Does this make them feel they are in safe hands?"
  4. **What not to show.** No building photos for a firm that sells trust; no stock
     smiles for a clinic that sells family care.
  5. **Reassuring or energetic.** Symmetry, even columns and a shallow type hierarchy read
     as stable and calm. Asymmetry, odd column counts and a steep hierarchy read as
     energetic and opinionated. Choose for this business; a site may move between the two
     section by section as its story does.

- **A4. Borrow one reference.** Pick one outside reference per design (a poster, a
  magazine page, a record sleeve, a comic, a film title card, a shop sign, a printed
  menu) whose main device suits the concept. Do not blend several in one design.
  - Name its two to four distinctive threads (a structure, a type treatment, a palette,
    an image habit) and translate each into one web move.
  - Translate qualities, not surfaces: take a source's confidence, economy or noise, not
    its exact shapes. Never reproduce a source's artwork.
  - Look first at printed things the customers already know: local film and concert
    posters, market and shop signage, packaging, comics, the shop's own menu.
  - The page may become an object from the customer's world: a menu card, a ticket, a
    magazine cover, a shop sign, a label.

- **A5. Choose type, then palette.**
  - **Type first.** Shortlist faces for how they feel, test them with the business's
    name, its numerals and every script the site uses, then choose. Avoid faces chosen
    only because they are everywhere.
  - **Palette with roles:** one dominant, one supporting, one accent, plus a dark that is
    not pure black and a light that is not pure white. Use them in clearly unequal
    amounts. Sample colours from the business's own things: sign, product, packaging,
    place.

- **A6. Compose in greys before code.** Read [references/moves.md](references/moves.md).
  Sketch or describe the phone and desktop layouts side by side, in greys, before any
  colour, decoration or code; designing directly in code drifts to boxes. Place the art
  direction by **Concentration** below, keep the phone version by **Phones**, and pick
  each move for the concept. Record which default each move replaces.

- **A7. Make the concept assets, then build.** Make the assets listed under **Concept
  assets**, shown early and rough so the owner can react. Build the page. Judge the
  result fresh, in a later session, and by feeling: "does this feel like us?" **Wait**
  for the owner's or user's reaction before treating the concept as settled.

### Concentration

Concentrate the art direction; do not spread it evenly.

- **The first screen** carries the concept at full strength.
- **One or two signature controls** wear the concept's materials (the menu, the order
  button, the audio player, the form) while still looking clickable.
- **Section headings, numerals and practical facts** carry the type treatment.
- **Other sections** stay calm and consistent. On a long page, vary composition by each
  section's job: a large, slow composition for the main promise; small, quick modules for
  lists; calm even columns for reassurance and the close.
- **One thread** (palette, type family, grid, illustration style, character) ties every
  page together. Pages may each look different; they must feel connected.
- When everything is loud, nothing is heard. Some pages need only good typography.

### Concept assets

The concept lives in bespoke assets, not in the grid; a site stripped of them falls back
to the default. Make and save these as reusable files:

- the mark, or a mark extension (a motif built from the logo's own geometry);
- an illustration set or image treatment in one style (drawn motif, duotone photos,
  cut-outs with a consistent outline);
- display lockups (the name, the line, key numbers);
- the palette with roles;
- the dressed signature controls.

Prefer imagery drawn from the business's own logo, products, place or people over stock
or generic illustration. The owner's photos treated in the palette (duotone, cut-out)
are a cheap alternative to illustration.

### Phones

Design the phone version; do not derive it from the desktop.

- Decide which signature element must survive on a phone and build it in a phone-native
  form. Letting it disappear at a breakpoint is the failure.
- Keep it by one of these: a horizontal scrolling strip instead of a shrunken row; a
  different crop or drawing for the phone, never a scaled copy; the ratio of scale
  contrast rather than the sizes (size against the viewport); a small token of a device
  that cannot fit (a band of the palette, one shape behind each block); a recomposed type
  object (a tower of names becomes two columns).
- Let scale contrast grow on the phone: a side column of display type can become a
  full-width display block.
- A phone layout may keep columns, indents and empty space; it need not be one column.
- Set breakpoints where the content breaks, not at device widths. Secondary ornaments
  may go; the concept may not.

### Familiar mechanics

Pricing tables, buttons, forms, navigation behaviour and calls to action keep their
expected behaviour and look clickable. Reinvent what faces the brand; leave the mechanics
people rely on.

### Brand rules and scripts

- When the project has brand rules (palette, typeface, shapes, container), they win
  where they conflict with a move. The concept, the one thread, concentration, practical
  facts as display type, scale contrast, empty space and the phone rules still apply.
- Thai has no capitals and few condensed widths: get display contrast from weight, scale,
  tight leading, colour splits and width-fitting. Do not set Thai vertically; keep
  vertical type to Latin numerals, dates and short Latin words. Thai has no spaces
  between words, so set text wrapped around shapes ragged, never justified. Choose
  display faces with enough weights in every script the type moves need.
- Giant numerals (prices, years, counts) work in any script.

## Review a design

- **V1. Read the design and its record.** Read the design record from A1–A7 when one
  exists. Look at the design at phone and desktop widths; read rendered pages or
  screenshots, not only the code.
- **V2. Answer each question in one line.** A missing or weak answer is a finding; name
  the step (A2–A7) that fixes it.
  - What is the concept, and where on the page is it at full strength?
  - Could this site belong to a different business in the same trade? If yes, what is
    generic?
  - Which default does each unusual move replace, and why does this business need it?
  - Which signature element survives on a phone, and in what form?
  - Which assets are bespoke, and are they saved for reuse?
  - Does every familiar mechanic still behave as people expect?

## Completion contract

- **Art-direct a site** is complete when the design record holds the concept and its
  source (A2), the line, feeling words, test question, what not to show and the
  reassuring-or-energetic choice (A3), the reference and its threads (A4), the type
  choice and palette roles (A5), the grey phone and desktop compositions with the
  default each move replaces (A6), and the saved asset files (A7); and the V2 questions
  each have an answer. Leave a step open and name it when it waits on the owner or user.
- **Review a design** is complete when every V2 question has a one-line answer and each
  finding names the step that fixes it.
