# Accounts: what other people say about Scott Kellum's design

Stream: `accounts`. Raw records are in `/tmp/designers/scott-kellum/raw/accounts/`, one
file per source. Pages were read as stripped text with curl where the site allowed it, and
through a fetch tool's summary otherwise (the raw file says which). No visual judgement
here rests on seeing the work; this stream is entirely second-hand, and the browser was
not used.

Outside writing about Kellum is thin. Most public pages about him are his own essays,
interviews and talk listings (the `own` and `talks` streams). The accounts below are
mostly short: a CSS-Tricks link post, reader arguments under his own CSS-Tricks essay, a
design-agency talk write-up, Fonts In Use entries, and library write-ups by other
developers. No Vox Media colleague's account of his work was found.

Claim markers: **[reported]** someone else describes it; **[stated, via X]** his own
words as relayed or quoted by someone else; **[observed]** seen in the work.

## Sources

| Source                                                                                                                                                               | Date       | What it gives                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------|
| [Mulligan, "Well, Typetura seems fun", CSS-Tricks](https://css-tricks.com/well-typetura-seems-fun/)                                                                  | 2019-02-01 | Outside framing of Typetura: fluid canvas, plain-CSS syntax, any input         |
| [Reader comments on "Intrinsic Typography"](https://css-tricks.com/intrinsic-typography-is-the-future-of-styling-text-on-the-web/)                                   | 2021-04-20 | The only real critique found: clutter, naming, complexity; his replies         |
| [TDC Member of the Month (ECS)](https://tdc.org/profiles/scott-kellum/)                                                                                              | 2020-02    | TDC's framing; his account of 72 Vox headline styles, Darden, Carter, dyslexia |
| [Type Network, "Using all the axes"](https://typenetwork.com/news/article/using-all-the-axes-typetura-scott-kellum)                                                  | n.d.       | Interviewer framing: patents, Vox/Darden/Roger Black; Bézier curves, axes      |
| [denkwerk, "Fluid Typography" talk write-up](https://www.denkwerk.com/en/blog/fluid-typography-how-we-optimize-fonts-for-all-screen-sizes)                           | 2026-11-11 | Agency developers adopting his curve-based interpolation; newspaper demo       |
| [Changelog news item](https://changelog.com/news/9N0y)                                                                                                               | 2018-11-28 | "keyframes, not breakpoints"; concept hard to grasp without trying it          |
| [Fonts In Use 6384, his site](https://fontsinuse.com/uses/6384/scott-kellum-s-website)                                                                               | 2014-04-06 | 2013 personal site: Acta Display headlines, Turnip RE body; Vox Media          |
| [Fonts In Use 45138, his site](https://fontsinuse.com/uses/45138/scott-kellum-website)                                                                               | 2022-09-15 | 2022 redesign: "full monospaced", Nostra + Arnold, black/white/red             |
| [Fonts In Use 6828, Vox.com](https://fontsinuse.com/uses/6828/vox-website)                                                                                           | 2014-05-19 | Vox.com launch type praised; does not credit a designer                        |
| [Fonts In Use 25523, Typetura articles](https://fontsinuse.com/uses/25523/typetura-introduction-articles)                                                            | 2019-03-13 | Self-submitted; variable Foreday gaining serifs as it grows                    |
| [Zell Liew, "Modular Scale"](https://zellwk.com/blog/modular-scale/)                                                                                                 | 2016-05-25 | Developer's view of the Sass modular-scale library he co-wrote                 |
| [Ian Carrico, Four Kitchens, Singularity](https://www.fourkitchens.com/blog/article/singularity-grids-without-limits/)                                               | 2013-10-14 | Asymmetric, ratio-based, per-breakpoint grids (Kellum and Sam Richard)         |
| [Singularity wiki, "Creating Grids"](https://github.com/Team-Sass/Singularity/wiki/Creating-Grids)                                                                   | n.d.       | Project docs (co-authored): triptych example, columns as ratios                |
| [Conffab, "Mapping Typography"](https://conffab.com/presentation/mapping-typography/)                                                                                | 2023       | Editor's blurb and chapter notes for his Summit '23 talk                       |
| [The Web Ahead 36, guest page](https://thewebahead.net/guest/scott-kellum) and [transcript gist](https://gist.github.com/nplayfair/1a4dbfbd3390227720f0fb6a89556071) | n.d.       | Jen Simmons's intro: designer "who also knows how to do great development"     |
| [Product Hunt, Typetura](https://www.producthunt.com/posts/typetura)                                                                                                 | 2019       | "Typeset it and forget it"; no outside reviews                                 |

## 1. Moves

### Typeset once for every context, not once per context

- **What.** Instead of writing a separate headline style for each article type, placement
  and breakpoint, define how one style changes as the space it sits in changes, so the
  same text component adapts wherever it lands.
- **Where.** His own account to TDC of typesetting the Vox home page: four article types,
  six placements and three breakpoints made "72 headline styles", which the team cut down
  but which convinced him they were "typesetting for each individual context" [stated,
  via TDC 2020]. Type Network names the same Vox and SB Nation experience as Typetura's
  origin [reported, Type Network]. Under his CSS-Tricks essay he says headlines and pull
  quotes are styled by their own size while other elements follow the parent or the
  viewport, and estimates a 75 to 90 percent cut in typographic CSS [stated, in reply to
  reader comments, CSS-Tricks 2021].
- **Default it replaces.** A fixed type scale that snaps at a few breakpoints, with
  per-placement overrides; or, as he puts it to TDC, sites that "oversimplify their
  typography" to avoid that complexity [stated, via TDC].
- **When it fits.** Pages where the same headline or card appears at many sizes: home
  pages, card grids, editorial front pages.
- **Critique.** A reader (Rob) said he saw "very little improvement on existing
  practice" and feared many sizes and weights on one page would look cluttered and
  inconsistent; he came round after Kellum's reply [reported, CSS-Tricks comments]. A
  second (James Reilly) called the approach "gobbledygook" and asked for "less, not more
  complexity" [reported]. A third (Ron) objected that responding to available space is
  extrinsic, not intrinsic, in CSS terms [reported].

### Size changes along a curve, not a straight line

- **What.** Type size (and other properties) interpolates between keyframes set at widths,
  along an eased curve: slow change at the smallest and largest sizes, fast change in the
  middle.
- **Where.** denkwerk's developers present this as "following the work of Kellum" and
  recommend it over linear scaling [reported, denkwerk 2026]. Type Network relays his view
  that `clamp()` and CSS locks scale linearly and are hard to tune, while Typetura sets a
  Bézier curve per property and per variable-font axis [stated, via Type Network].
  Changelog summarised Typetura as CSS that "scales with animation keyframes, not
  breakpoints" [reported, quoting the project, Changelog 2018].
- **Default it replaces.** A breakpoint jump, or a linear `clamp()` ramp between two
  sizes.
- **When it fits.** Display type and headlines that span phone to wide desktop; less so
  for body text (below).

### Scale headlines; keep body steady and loosen its leading

- **What.** Large scaling belongs to headlines and extreme viewports; paragraph text stays
  near a fixed comfortable size (he cites a 16px minimum) and instead gets line-height
  that grows with line length ("molten leading").
- **Where.** His reply to reader Lori O under the CSS-Tricks essay [stated, in comments].
  Conffab's chapter notes for "Mapping Typography" record the same rule, line height
  rising with line length [reported, Conffab]. In the same talk notes he praises Stripe's
  headline growing as its screenshots move, and wants GitHub's sign-up call to action to
  stay large for longer [reported, Conffab].

### Every axis of a variable font follows the space

- **What.** Not only size: weight, width, grade and optical size shift with the
  container, so a face can gain serifs or weight as it grows.
- **Where.** The Typetura introduction articles used DSType's variable Foreday, which
  "gradually" gains serifs and weight as its size increases [stated, his own Fonts In Use
  submission, so not independent]. Type Network relays his point that these axes are
  linked in parametric fonts and need separate curves [stated, via Type Network].
- **Default it replaces.** One static weight per heading level.

### Proportion over fixed measurements

- **What.** Consistency comes from keeping proportions constant, not from repeating exact
  values; he avoids systems like the 8pt grid as more useful to the designer than to the
  reader.
- **Where.** His reply to Rob under the CSS-Tricks essay [stated, in comments]. Related
  tools others credit him with: the Sass modular-scale library (with Adam Stacoviak and
  Mason Wendell), whose double-ratio scales Zell Liew calls "superb" because ordering
  those steps by hand is hard [reported, Liew 2016]; modularscale.com, rebuilt with Tim
  Brown [stated, via TDC]; and Singularity, a Sass grid system with Sam Richard that
  allows unequal columns set as ratios (2:4:3, a 2:8:2 triptych, golden-ratio grids) and a
  different grid per breakpoint [reported, Carrico 2013; Singularity wiki].
- **Default it replaces.** Equal 12-column grids and arbitrary pixel scales.

### Width as a general input, not only for type

- **What.** The same width-to-keyframe mapping can drive any animatable property, and
  scroll or cursor position can stand in for width.
- **Where.** CSS-Tricks quoted the project: "a fluid design solution, for any property,
  based on any input" [reported, Mulligan 2019]. Conffab notes and Type Network both cite
  Lynn Fisher's site, which maps width to SVG motion and zoom [reported].

## 2. Process and thinking

- **Fluid canvas instead of artboards.** Others repeat his framing that design software is
  built around fixed artboards and designers need a way to show how a design changes
  between sizes; Mulligan quotes "Typetura is a tool that enables designers to work with
  a fluid canvas" [reported, CSS-Tricks 2019]. Asked how a Figma designer would work this
  way, he said he does not worry about implementation while designing, mocks up static
  instances as usual, and treats the intrinsic rules as "a map" of the proportions those
  mockups already follow [stated, in comments].
- **Scale as a third dimension.** To TDC he described scalability as a dimension beside
  width and height that "behaves more like time than space" [stated, via TDC].
- **Tools that teach.** Caren Litherland's advice while he worked on modularscale.com,
  "create tools that teach", shaped Typetura's first app [stated, via TDC].
- **The type designer's eye.** TDC frames him as someone who started in type design and
  kept "type at the heart of everything he makes" [reported, TDC]. He credits drafting at
  Darden Studio and Joshua Darden for showing that more character in letterforms can
  improve legibility, and quotes Matthew Carter: a typeface is "a beautiful group of
  letters, not a group of beautiful letters" [stated, via TDC]. He links his attention to
  letterforms to childhood dyslexia [stated, via TDC].
- **Design in the browser.** Jen Simmons introduced him as a web designer "who also knows
  how to do great development" [reported, The Web Ahead]. In that episode he argued for
  designing in the browser because responsive sites scale and Photoshop misrepresents
  them [stated, via transcript].

## 3. Taste

- **Personal sites as type showcases.** His 2013 site paired Acta Display headlines with
  Turnip RE body text, an entry contributed by Webtype [reported, Fonts In Use 2014].
  The 2022 redesign is "full monospaced", Nostra (Sett and Stream) with Arnold, and its
  photography page uses large type and a black, white and red palette [reported, Fonts
  In Use 2022]. Both are worth checking by eye in the `own` stream.
- **Praise he gives** (via talk notes): Stripe's fluid headline; Heath Ceramics as a
  favourite shop that uses viewport units, though its type proportions drift against body
  text [reported, Conffab].
- **Dislikes:** breakpoint snapping (the LA Times headlines jumping at about three sizes),
  linear `clamp()` ramps, and fixed-grid systems like 8pt [reported, Conffab; stated, via
  Type Network and comments].
- **Peers' reception.** Positive but light: "what a delight" (Mulligan), "super flexible"
  (denkwerk), a concept "hard to grasp" until tried (Changelog) [reported]. denkwerk adds
  a caution that fluid sizing with `clamp()` can conflict with screen magnifiers and must
  be tested for accessibility; under his essay he answered a reader's zoom question by
  pointing to `%` and `em`/`rem` units and WCAG 1.4.4 [reported; stated, in comments].

## 4. Open questions

- **Vox Media colleagues.** No post by a Vox Media designer or engineer describing his
  work turned up; the Vox Product tumblr (which a search snippet says lists him as a
  designer) returned 403 and has no Wayback capture of the relevant page. His Vox credits
  (Concert ads, the Athena ad unit, image cropping, the launch team, headline typesetting)
  come only from his own résumé, speaker bios and the TDC interview.
- **Vox.com launch type.** The Fonts In Use entry praises the hierarchy but does not say
  who set it; his role in the vox.com headline system rests on his TDC account alone.
- **Treesaver / Roger Black.** Outside coverage of Treesaver (Print, 2010) does not
  mention him; his design-director role comes from his own A List Apart bio.
- **No award or gallery write-up** (Awwwards, CSS Design Awards, siteInspire, TDC
  competition) was found for his sites or for Typetura clients such as Gold's Guide.
- **No sustained critique** beyond the CSS-Tricks comment thread; no review compares
  Typetura with Utopia or plain `clamp()` on design grounds.
- The Type Thursday interview (Medium) and a Turkish Medium roundup returned 403; the
  Type Network piece is undated.
