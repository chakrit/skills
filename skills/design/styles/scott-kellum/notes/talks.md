# Scott Kellum: talks, interviews, podcasts

Stream: `talks`. Raw text of every source is in `/tmp/designers/scott-kellum/raw/talks/`,
one file per source, URL on the first line.

Claim tags: **[S]** stated by him in his own words (a transcript, a written interview, his
slides); **[R]** reported by someone else (a summary, a host's paraphrase, an event bio
he likely supplied); **[O]** observed by me, from text or code on slides only. No browser
was used for this stream, so nothing here was seen rendered.

Most of his public speaking is about one idea, fluid typesetting, so the talks repeat
each other; the beyond tellerrand transcript is the fullest single record.

## Sources covered

| Source                                                                                                               | Date       | What it is                                                                                    |
|----------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------|
| https://beyondtellerrand.com/events/dusseldorf-2023/speakers/scott-kellum                                            | 2023-04    | "Mapping Typography", beyond tellerrand Düsseldorf: full transcript on the page               |
| https://conffab.com/presentation/mapping-typography/                                                                 | 2023       | Same talk at Web Directions Summit '23; read only as a summary plus short quotes (see note)   |
| https://www.meetup.com/css-cafe/events/293341869/                                                                    | 2023-06-22 | Same talk at CSS Café (online); abstract and bio only                                         |
| https://shoptalkshow.com/353/                                                                                        | 2019-03-25 | ShopTalk Show 353 "Typetura with Scott Kellum", full transcript                               |
| https://wordpress.tv/2020/10/22/scott-kellum-practical-responsive-typography/                                        | 2019 talk  | "Practical Responsive Typography", WordCamp Boston 2019; abstract only, video not watched     |
| https://practical-responsive-type.netlify.app/                                                                       | 2019       | His HTML slides for that talk: slide text and CSS read, not seen rendered                     |
| https://web.archive.org/web/2020/https://medium.com/type-thursday/from-modular-scales-to-variable-fonts-8312841d9e0d | 2017-08-28 | Type Thursday interview by Ulrik Hogrebe: background, dyslexia, modular scale, variable fonts |
| https://tdc.org/profiles/scott-kellum/                                                                               | 2020-02    | Type Directors Club member-of-the-month Q&A: type design, Vox headlines, Typetura aims        |
| https://typenetwork.com/news/article/using-all-the-axes-typetura-scott-kellum                                        | n.d.       | Type Network interview "Using all the axes": SB Nation origin of Typetura, variable axes      |
| https://sessionize.com/scottkellum                                                                                   | n.d.       | Speaker bio: Roger Black, Darden Studio, Vox launch team, focal-point crops, dyslexia         |

Note on Conffab: the page blocked curl, so the raw file holds a WebFetch summary and short
quotes from its transcript, not the page itself. Treat its quotes as reliable in wording
but thin in context.

## 1. Moves

### 1.1 Typographic map: one rule set per role, from plotting the sizes you want

- **What.** Take every instance of one role (all headlines on a page, all product names),
  plot font size against the width of its container, fit a line or curve, and express
  that curve as a single CSS rule that runs off container width. Every headline, in
  every slot, at every viewport, then comes from that one rule. [S: btconf 2023]
- **Origin of the idea.** He plotted the headlines of an old printed newspaper front page
  ("The Times" per Conffab) and found that "as the headline width gets wider, the font
  size tends to increase", strongly correlated; the map turns that print habit into a
  function. [S: btconf 2023; R: Conffab]
- **Where.** A product page (Nike, per Conffab) where "every single one of these product
  names, as well as the headline at the top, use one single CSS rule set"; a study (not
  live) of The Atlantic's home page, all headlines from one curved map. [S: btconf 2023;
  R: Conffab] A rich editorial page built in a Twitch stream with Alex Trost from two
  rule sets, root and headline. [S: btconf 2023]
- **Replaces.** Typesetting each context separately. At Vox he counted four article types
  x six placements x three breakpoints = 72 headline styles: "We were typesetting for
  each individual context." Most sites react by oversimplifying their type. [S: TDC 2020]
  His aim is to "typeset in a way that adapts to those contexts", removing breakpoints
  and placement styles. [S: TDC 2020] (The Type Network interview gives five entry
  types x six placements = thirty per breakpoint; same point. [S])
- **Also replaces.** The type scale as a menu: "Type scales are a laundry list of
  options. But they don't often help guide people to which specific size". He includes
  his own Modular Scale in that critique. [S: btconf 2023]
- **When it fits.** Any page where one role (headline, card title, product name) appears
  at many sizes. For an agent: decide sizes for the narrowest and widest slot, size in
  between by container width, and do not write per-slot overrides. "As an added bonus,
  responsive just works because the containers themselves are moving." [S: btconf 2023]

### 1.2 Let type, not labels, tell the reader what a thing is

- **What.** Each typographic role carries a "thread" that marks it as a headline, a call
  to action, a price, a byline, "regardless of where they are displayed and at what
  screen size". [S: btconf 2023]
- **Where.** SB Nation redesign (2012): a type system so readers "could know what kind of
  media they were clicking on: Is it an article? Is it a fan post? Is it a feature? We
  wanted users to know from the type, without a hundred labels." He calls knowing where
  a link goes "one of the biggest problems on the web". [S: Type Network]
- **Stance.** Faced with 72 styles, "most might want to narrow the typographic diversity,
  but I wanted to capture that entire array of styles and make it possible." [S: Type
  Network]
- **Replaces.** Uniform card titles plus category tags or badges.
- **When it fits.** Mixed-content indexes and home pages: give each content type its own
  face, weight, width or case, and let that difference survive every placement.

### 1.3 Curve the interpolation; do not scale linearly

- **What.** Fluid sizes should follow a curve, not the straight line that `clamp()` and
  viewport-unit formulas give. "Maybe we want the headlines to remain smaller and then
  get bigger really quickly as the width of its container starts to grow." [S: btconf
  2023]
- **Body text curve.** For root size: "We want our text to be as big as possible as soon
  as possible", but able to scale down to watch-size without overflowing. Linear "gets
  really small really quickly". [S: btconf 2023]
- **Why.** With clamp and CSS locks the function is "very much by feel, and always scales
  linearly"; more media queries only chain linear segments. Typetura offers Bézier
  curves per property. [S: Type Network] "Control over how styles interpolate is
  powerful" (slide). [R: Conffab]
- **Related.** On GitHub's sign-up page: "an opportunity to keep this call to action as
  big as possible for as long as possible." [S via Conffab quote]
- **When it fits.** Display type and the root size of any fluid page. For an agent: hold
  headlines modest through mid widths and let them jump late; hold body large and shrink
  it only at the very small end.

### 1.4 Hierarchy contrast scales with the screen

- **What.** On a big screen, "big, chunky headlines with small text" for a dynamic page;
  on a phone the ratio should move toward 1:1, because a large ratio there gives "one
  character per line". The ratio itself is what should interpolate. [S: ShopTalk 353]
- **Image he uses.** Towers into the sunset, or Christo and Jeanne-Claude's *The Gates*:
  seen from the ground the near one is much bigger; seen from above they look alike. The
  relationship keeps meaning while the ratio changes. [S: Type Thursday 2017]
- **Replaces.** One fixed modular-scale ratio for all sizes, or a smaller copy of the
  desktop scale on mobile.
- **When it fits.** Always on fluid pages. Do not shrink the whole scale proportionally;
  compress the gap between heading and body on small screens and widen it on large.

### 1.5 Line height follows line length; headlines tight, text loose

- **What.** "Increase your line height with more characters per line. Decrease your line
  height with fewer characters per line." [S: btconf 2023] "As line length grows, so
  should line height" (slide). [O: 2019 slides]
- **Diagnostic.** "If your typography looks off, it's probably your line height." He
  shows a headline set too loose and body too tight, then swaps them: "much, much
  better". "Don't sleep on line height. Always, always dial that in." [S: btconf 2023]
- **Measure.** Quotes Bringhurst's 45-75 characters and sets `max-width: 60ch`; root
  `line-height: 1.4` at `font-size: 120%` in his slides. [O: 2019 slides]
- **When it fits.** Everywhere; interpolate line height together with size, not as a
  fixed number.

### 1.6 Interpolate the font's axes, not just its size

- **What.** Drive weight, width, optical size and grade with the same map as size, so a
  headline changes weight and width as its container grows. His demos use Obviously (OH
  no Type Co) for its width and weight range. [S: btconf 2023; S: Type Network]
- He notes that weight cannot be interpolated by viewport-unit formulas, which is one
  reason he built on CSS animations. [S: btconf 2023]
- **Expressive use.** "Imagine something like a website about balloons, being able to
  inflating a bubble font headline from thin to black." [S: Type Thursday 2017]
- **When it fits.** With a variable family that has real width and weight ranges:
  condensed and heavier in narrow slots, wider and lighter (or heavier) in wide ones.

### 1.7 Skip the baseline grid unless columns sit side by side

- **What.** He does not hold to vertical rhythm on a 4px baseline: on the web it is
  "extremely difficult to maintain", half-leading pushes baselines off, and it "creates
  such a fragile mess". He keeps it for one case: "columns of text next to each other".
  [S: ShopTalk 353]
- **Replaces.** Forcing every size and line height to a multiple of a base unit.

### 1.8 Motion that looks organic, depth that is real

- **Cicada principle.** Stack several animations with prime-number durations so they
  "diverge and they almost never converge"; with few moving parts it reads as "organic"
  and random. "My favorite thing and I really want to bring it back." [S: ShopTalk 353]
- **Honest parallax.** His pure-CSS parallax uses 3D perspective so near things really
  pass faster than far ones, "very honest to the original representation of parallax";
  he regrets that parallax is "conflated with just scroll jacking" and with slow sites.
  He no longer recommends that exact technique for production. [S: ShopTalk 353]
- **Responsive as zoom.** He singles out Lynn Fisher's site, which uses Typetura to zoom
  a whole illustrated scene, "doors opening and everything", as the browser resizes. [S:
  Type Network]
- **When it fits.** Ambient decorative motion (prime durations) and layered hero art
  (true perspective), never scroll hijacking.

### 1.9 Character in letterforms as a legibility tool

- **What.** From Joshua Darden: "adding more character to forms can enhance, not
  diminish, legibility." [S: TDC 2020] He admires Omnes's partially rounded terminals
  and Turnip's (David Jonathan Ross) top-weighted forms, which give paragraphs a colour
  "easy to read on top of it's nice aesthetic". [S: Type Thursday 2017]
- **Replaces.** The assumption that the most neutral face is the most readable.

## 2. Process and thinking

- **Websites are multidimensional objects.** A viewport is one slice; "extrude" the site
  to see all its widths, plus height, light and dark mode, preferred font size, scroll
  depth. Components add more dimensions by sitting in many slots. [S: btconf 2023]
  Scalability is "just another dimension on which to design"; "It behaves more like time
  than space." [S: TDC 2020]
- **Typeface design as the model.** A typeface is a design system: start from H O D and
  n o p, test words ("Handglvoes"), then masters across weight and optical size; the
  Noordzij cube and Superpolator show a design space where masters are "a lot like
  breakpoints" and instances are interpolated between them. Web type should work the same
  way. [S: btconf 2023]
- **"A beautiful group of things."** He extends Matthew Carter's "Type is a beautiful
  group of letters, not a group of beautiful letters" to components: "a beautiful group
  of components, not a group of beautiful components." [S: btconf 2023; S: TDC 2020]
  The goal is "greater than the sum of each part". [S: TDC 2020]
- **Voice and utility.** "Typography is the voice we give to written words"; look for "a
  voice that is appropriate for its context"; "the utility of typography is legibility."
  [O: 2019 slides] He separates legibility ("Can I read this?") from readability ("Do I
  want to read this?"): Wikipedia and Twitter's I/l disambiguation favour legibility over
  readability, which is right for their job. [R/S: Conffab]
- **Dyslexia.** He confused b, d, p, q as a child and learned to read shapes as "designed
  objects"; it made him sensitive to how stress and serifs separate glyphs. [S: Type
  Thursday 2017; S: TDC 2020] "So reading is coding." [R: Conffab]
- **Know the press.** "Just as a print designer needs to understand the process of how
  paper and ink moves through a press I wanted to gain a good understanding of how my
  pixels were drawn onto a screen." CSS became "just another fun way to craft my
  designs." [S: Type Thursday 2017] He enjoys "CSS's sort of poetry as opposed to writing
  instruction manuals". [S: ShopTalk 353]
- **Proportion as guideline.** A modular scale is "just a ruler" whose steps grow; the
  golden ratio "won't necessarily make your type more beautiful". "I always try to steer
  people away from the rules to maybe think of these more as guidelines." [S: Type
  Thursday 2017]
- **Design where you can see it move.** "Designers can't see what they're doing": fixed
  artboards in Figma for a fluid medium. Mock-ups arrive as "tablet" and "desktop" with
  "no indication of how things change in between"; he sets the two ends and lets the
  tool find the middle, "Goldilocks". [S: Type Network; S: ShopTalk 353] "We have the
  tech and we need the tools." [R: Conffab]
- **Tools that teach.** Caren Litherland's advice while he built modularscale.com. [S:
  TDC 2020]
- **Print is fixed, web is not.** "With print, the designer chooses the paper size,
  color, and weight, but with digital we have no idea" what the reader sees; the
  conflict, after Frank Chimero's *The Web's Grain*, is that images flex but "the text is
  incompressible". [S: TDC 2020; S: Type Network]

## 3. Taste

- **Praises.** Heath Ceramics ("I think it is gorgeous", though its proportions drift
  against body text); Stripe (text grows as screenshots pop in and out); The Atlantic
  ("beautiful, rich typography"). [S via Conffab quotes]
- **Faces and designers.** Joshua Darden and Omnes; David Jonathan Ross's Turnip and
  Roslindale; Arrow Type's Recursive; Obviously by OH no Type Co. [S: Type Thursday;
  btconf 2023; 2019 slides]
- **Influences named.** Matthew Carter, Bringhurst, Frank Chimero, Tim Brown (modular
  scale co-author), Trent Walton (fluid type, 2012), Mike Riethmuller (CSS locks),
  Utopia, Roger Black, Sam Barclay's book on dyslexia. [S: across sources]
- **Dislikes.** Snapping headline sizes at a few breakpoints, "how most editorial sites
  manage their typography" (LA Times); linear `vw` scaling; type scales that list sizes
  without guiding; oversimplified type to dodge complexity; golden-ratio mysticism;
  baseline-grid perfectionism; scroll jacking. [S: btconf; ShopTalk; Type Thursday; TDC;
  Conffab]
- **Recurring motifs.** Interpolation everywhere (colour mixed via paused animations,
  axes, size); recursion and nesting in CSS as play; print newspaper as reference for
  hierarchy. [S: ShopTalk 353; btconf 2023]

## 4. Open questions

- The WordCamp Boston 2019 video and the beyond tellerrand YouTube video
  (https://www.youtube.com/watch?v=5kixsu_yeHs) were not watched; the btconf transcript
  stands in, the WordCamp talk is known only from slide text.
- The btconf slides are a Figma prototype; not viewable without a browser. The Atlantic
  and Nike studies, and the newspaper plot, were not seen.
- Web Directions / Conffab blocked direct fetch; its content is a model summary with
  short quotes. Its date and any differences from the btconf version are unverified.
- The Type Network interview is undated (mentions the WordPress plugin and a later Alex
  Trost conversation, so likely 2022 or later).
- SB Nation numbers differ by source: 4 x 6 x 3 = 72 (TDC), 5 x 6 = 30 per breakpoint
  "more than 72" (Type Network), "300+ sites, ~72 components" (Conffab summary).
- No Vox Product blog interview, CodePen Radio, Responsive Web Design Podcast, CSS Day,
  An Event Apart or Smashing appearance was found. The Alex Trost stream he mentions was
  not located.
- Nothing in these sources speaks to colour, imagery, grid or layout beyond type; those
  must come from the `work` and `own` streams.
