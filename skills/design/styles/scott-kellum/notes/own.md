# Scott Kellum: his own sites and writing

Stream `own`. Raw copies are in `/tmp/designers/scott-kellum/raw/own/`, one file per
source, URL on the first line. Claim tags: **[stated]** he said it, **[observed]** seen
in the browser on 2026-11-23, **[code]** read from CSS or markup only, **[reported]**
someone else said it. Talks and interviews are in `talks.md`; outside views are in
`accounts.md`.

Wayback note: curl access to the Wayback Machine was blocked as bot traffic, and later
captures stopped loading in the browser as well. Only the home pages of 2010, 2012, 2016
and 2018 were seen; the 2013 to 2015 blog posts were read only as the excerpts on the
2016 home page.

## Sources

| Source                                                              | Date        | What it gave                                                       |
|---------------------------------------------------------------------|-------------|--------------------------------------------------------------------|
| scottkellum.com (home, seen and CSS read)                           | live, 2025  | Brown/black diagonal ground, Sentient + Gamay, visible grid lines  |
| scottkellum.com/_astro/_slug_.CtW6py_J.css                          | live        | Typetura layer, keyframed sizes, palette, print sheet              |
| scottkellum.com/resume                                              | live        | Career, patents, talks list, Sass tools, CSS parallax              |
| scottkellum.com/writing/                                            | live        | Three posts only; essays filed under /portfolio/                   |
| scottkellum.com/portfolio/discussing-our-design-practice/           | 2024-12-16  | "Branding is talk therapy for a business"                          |
| scottkellum.com/portfolio/unit-division-with-css-and-fallbacks/     | 2024-09-13  | Width as a number to drive colour, animation, axes                 |
| scottkellum.com/portfolio/making-a-smartphone-dumbphone/            | 2025        | Personal; little design content                                    |
| github.com/scottkellum/scottkellum.com (drafts/editorial-design.md) | stub        | Unwritten case study "storytelling experiences for Vox Media"      |
| github.com/scottkellum/web-typography-class (index, weeks 1-10)     | 2022-2025   | Cooper Union syllabus: font selection, fluid sizing, text effects  |
| github.com/scottkellum (repo list)                                  | live        | modular-scale, singularity, typographic, color-schemer, momentum   |
| css-tricks.com/intrinsic-typography-is-the-future-of-styling-text…  | 2021-04-20  | Intrinsic typography; his replies on proportion and the 8pt grid   |
| alistapart.com/article/a-pixel-identity-crisis/                     | 2012-01     | Reference pixel vs hardware pixel; size everything in ems          |
| Wayback scottkellum.com 2010-07-30                                  | 2010        | Unstyled list: "Website, Publication, Typeface Design"             |
| Wayback scottkellum.com 2012-01-27                                  | 2012        | Full-bleed screenprint texture, keycap avatar, paged slider        |
| Wayback scottkellum.com 2016-01-09                                  | 2016        | Georgia italic name, Georgia teal titles, Verdana text; 14kb site  |
| Wayback scottkellum.com 2018-06-03                                  | 2018        | Flat teal page, white Georgia list of post titles                  |

## 1. Moves

### 1.1 The whole page breathes with its container

- **What.** Every text size on the page sits on a keyframe that is scrubbed by the width
  of its container, not stepped at breakpoints. On his site the root font size runs from
  0 to 125% across 0 to 50em, page heads from 2rem to 6rem, headings 1.5rem to 3rem, the
  lede from 1.1rem to 1.5rem. Headings and the lede get `text-wrap: balance`. [code]
- **Where.** scottkellum.com and typetura.com both run the Typetura CSS layer (paused
  animations whose delay is computed from container width, with a `tan(atan2())`
  fallback for unit division). [code] Narrowing the window rescales type smoothly.
  [observed]
- **Default it replaces.** A fixed scale with two or three media-query jumps.
- **Why.** He wants one style that knows every size, so a headline style does not
  multiply per placement; see `talks.md` 1.1. [stated, CSS-Tricks 2021]
- **When it fits.** Any page; especially when the same component sits in wide and narrow
  slots.

### 1.2 Big-text lede instead of a hero

- **What.** The home page opens with no image and no headline: a paragraph of serif text
  at about 30px/45px (Sentient, light weight) fills the first screen, preceded only by a
  tiny italic kicker ("Scott Kellum — Human-centered and technology-driven design").
  The second screen keeps the same scale for two plain sentences about work. [observed]
- **Where.** scottkellum.com; typetura.com does the same with Roslindale at about 37px.
  [observed]
- **Default it replaces.** Centred hero headline, subhead and button over an image.
- **When it fits.** Personal and studio sites where the voice is the product; needs a
  text face with personality at large sizes.

### 1.3 Show the grid as drawing

- **What.** Hairline rules in a dark accent colour (#522200 on #371506) mark the column
  edges and run past the content to the viewport edges, crossing at section joins like
  construction lines. Boxes on typetura.com carry dashed inner column guides. [observed]
- **Where.** scottkellum.com, typetura.com. Body grid `1fr min(50rem, 90%) 1fr` with
  subgrid wrappers. [code]
- **Default it replaces.** An invisible grid and card shadows.
- **When it fits.** Dark, typographic pages; keep the lines one step off the background
  so they read as texture, not borders.

### 1.4 A diagonal colour field that moves on scroll

- **What.** The ground is split by a single steep diagonal between brown and black; the
  split shifts as you scroll, so the page has motion without any animated object.
  [observed]
- **Default it replaces.** A flat background or a gradient hero.
- **When it fits.** Pages with almost no imagery that still need movement.

### 1.5 Leaf-cornered image tiles with a heavy condensed title beside them

- **What.** Featured-post images are squares with two opposite corners rounded at 4rem
  and two left square (`border-radius: 0.1px 4rem`). The title sits to the right in a
  heavy condensed face (Gamay, pale pink #ffd5ce), set bottom-aligned on a hairline rule
  with a short serif summary under it. [observed, code]
- **Image style.** Saturated collage art: glitched textures, mesh distortions, magenta,
  cyan and yellow, overprinted pattern. Each post has its own montage. [observed]
- **Default it replaces.** Uniform rounded cards in a three-column grid.
- **When it fits.** Short lists of work or posts (he shows four on the home page, one
  per row).

### 1.6 Blurred pill behind sticky navigation

- **What.** The logo, two text links and three icons sit in a sticky pill whose
  background is a blurred, lightened shape (`filter: blur`, `mix-blend-mode: lighten`)
  that grows in on scroll. The vertical phrase "Keep Scrolling, there's so much more!"
  runs up the right margin. [observed, code]
- **Default it replaces.** A full-width header bar.

### 1.7 Three-face system: text serif, condensed display, mono

- **What.** Sentient (variable serif, 200-700) for text, Gamay (Darden Studio's
  variable-width sans, a foundry he works for) for display and navigation, Arnold for
  mono. On typetura.com he swaps the text and display face to Roslindale. [code]
- **Testimonials** are centred italic serif with the credit in small, wide-tracked
  caps. [observed]
- **Default it replaces.** One sans in two weights.

### 1.8 Each redesign changes medium, not just look

- **What.** His site versions are each a different idea: a 2012 full-bleed screenprint
  texture with a keycap avatar and sideways paging; a 2015-16 site built to fit in 14kb
  using only Georgia (huge italic name) and Verdana; a 2018 flat teal sheet with a list
  of white Georgia titles; today's dark Astro site with variable fonts and Typetura.
  [observed, Wayback]
- **Why.** "Stop redesigning, keep designing" (2013) argues against the cycle of
  perfecting a personal site and abandoning it. [stated, excerpt only]

### 1.9 A print stylesheet that respects the reader

- **What.** In print the palette collapses to black on white, the sticky nav is
  dropped and heading sizes are reset to fixed points. [code]

## 2. Process and thinking

- **Branding as conversation.** "Branding is talk therapy for a business": working out
  what the business is now and what it should become. He declines to judge a logo or
  type choice without knowing the stakeholders' reasons. [stated, 2024]
- **Know the medium.** His 2013 post "Designers, know your medium" ties design to its
  production technology, from movable type to CSS. [stated, excerpt only]
- **Design abstractions.** He sees reusable components as a design practice, not only a
  coding one (2013 post). [stated, excerpt only]
- **Width as raw material.** Unit division lets one value (container width) drive
  colour, proportions or variable-font axes; his demo turns viewport width into a hue.
  [stated, 2024]
- **Proportion over measurement.** He avoids the 8pt grid because it serves the designer
  more than the reader, and controls consistency of proportion instead. [stated, 2021]
- **Teaching order.** His Cooper Union class goes: balance line length, size and
  leading; units and hierarchy; fluid sizing (modular scales, clamp, Typetura); font
  selection; variable fonts; text effects (gradient, outline, long shadow, SVG
  displacement, COLRv1 colour fonts); UI type. [stated, syllabus]
- **Choosing fonts.** Narrow by utility first (optical size range, width range, weight
  range, spacing, languages, axes, quality, budget), then by aesthetic (professional or
  casual, character, trendy or classic, mass or niche). "Organize fonts like music";
  build relationships with foundries. [stated, syllabus]
- **Pixels are not stable.** Size everything in ems so a whole page can be rescaled from
  the root (2012). [stated]

## 3. Taste

- Variable fonts from independent foundries he works with: Darden Studio (Gamay, Kit),
  DJR (Roslindale, Fern, Zenith), MCKL (Redaction). [observed]
- Warm dark grounds (brown, deep green) with pale pink type and a hot orange accent,
  rather than pure black and white. [observed]
- Glitched, overprinted, high-chroma collage art for thumbnails. [observed]
- Small, fast pages: the 14kb budget site; "no resets, sensible defaults". [stated,
  excerpt only]
- Reference reading he assigns: Frank Chimero's "The Web's Grain", Ze Frank on taste,
  John Berger's *Ways of Seeing*; sites he shows students include Ling's Cars, Dinamo
  and Plain Form. [stated, syllabus]

## 4. Open questions

- The full text of the 2013-2015 posts ("Designers, know your medium", "Design
  abstractions", "Stop redesigning, keep designing", "Websites on a 14kb budget"): only
  excerpts were read, because the Wayback Machine blocked access.
- The 2013 and 2014 site versions (Acta Display era, per `accounts.md`) were not seen.
- The Vox storytelling case study exists only as an empty draft in his repository.
- ".NET Magazine: Colour Theory for the Web" (2014) is print-only and was not read.
