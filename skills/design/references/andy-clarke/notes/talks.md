# Andy Clarke: talks, guest writing, interviews (stream `talks`)

Scope: Clarke's writing outside his own site and outside the Smashing "Inspired Design
Decisions" series (24 ways, A List Apart, other Smashing articles), his conference talks
(transcripts, slides), and interviews and podcasts where he explains how he works.

Claim markers used throughout:

- **[S]** stated by Clarke himself (his article, talk transcript, or interview answer).
- **[O]** observed by me in the work (slides, article figures, screenshots).
- **[R]** reported by someone else (event write-up, interviewer, podcast guest).

Raw text for every source is in `tmp/andy-clarke/raw/talks/` (URL on line 1). Slide and
figure contact sheets are in `tmp/andy-clarke/shots/talks/`. The six Unfinished Business
transcripts are summarised in `digests/talks-unfinished-business.md`, with page references.

## Sources covered

| Source                                                                                                              | Date        | What it is                                                                 |
|---------------------------------------------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------|
| https://conffab.com/presentation/art-directing-web-design/                                                          | Nov 2016    | Transcript of "Art Directing Web Design" keynote, Direction 16, Sydney     |
| https://speakerdeck.com/malarkey/art-directing-web-design                                                           | Aug 2016    | Slides for the same talk (image-only; sampled 18 slides)                   |
| https://speakerdeck.com/malarkey/designing-imaginative-grid-systems-port-80-newport                                 | 2016        | "Designing imaginative grid systems" slides + slide text (WWF, Smashing)   |
| https://conffab.com/presentation/counting-stars-creativity-over-predictability/                                     | 2015        | "Counting Stars: Creativity Over Predictability", Respond 2015 (abstract)  |
| https://www.smashingmagazine.com/2014/03/a-modern-designers-canvas/                                                 | Mar 2014    | Edited transcript, "A Modern Designer's Canvas" (AEA, SmashingConf)        |
| https://www.smashingmagazine.com/2012/09/better-client-participation-in-responsive-design-projects/                 | Sep 2012    | Notes for SmashingConf Freiburg talk: process, "atmosphere", client crits  |
| https://v9.bradfrost.com/blog/post/andy-clarke-at-smashing-conference                                               | Sep 2012    | Brad Frost's live notes on that same talk                                  |
| https://www.smashingmagazine.com/2018/04/art-directing-web-css-grid/                                                | Apr 2018    | "Art Directing For The Web With CSS Grid Template Areas" (Hardboiled)      |
| https://www.smashingmagazine.com/2019/04/art-direction-for-the-web-using-css-shapes/                                | Apr 2019    | "Art Direction For The Web Using CSS Shapes" (before/after layout pairs)   |
| https://www.smashingmagazine.com/2025/05/smashing-animations-part-1-classic-cartoons-inspire-css/                   | May 2025    | Hanna-Barbera limited animation as a model; Mike Worth site                |
| https://www.smashingmagazine.com/2025/09/ambient-animations-web-design-principles-implementation/                   | Sep 2025    | Ambient animation principles (Quick Draw McGraw comic cover)               |
| https://www.smashingmagazine.com/2025/10/ambient-animations-web-design-practical-applications-part2/                | Oct 2025    | Ambient animation in client work: Reuven Herman, Mike Worth, EPD           |
| https://www.smashingmagazine.com/author/andy-clarke/                                                                | 2026        | Author index (28 articles; used to find the above)                         |
| https://24ways.org/2007/underpants-over-my-trousers/                                                                | Dec 2007    | Comic-book panel size as timing; borderless panels; white space as drama   |
| https://24ways.org/2010/circles-of-confusion/                                                                       | Dec 2010    | Ranking which parts of a design must stay "sharp" across browsers          |
| https://24ways.org/2011/theres-no-formula-for-great-designs/                                                        | Dec 2011    | Custom grids (84px col / 24px gutter, odd column counts); "connectedness"  |
| https://24ways.org/2014/taglines-and-truisms/                                                                       | Dec 2014    | Finding a company's one "truism" and turning it into a tagline             |
| https://24ways.org/2016/designing-imaginative-style-guides/                                                         | Dec 2016    | Art-directed style guides; colour shown as hierarchy, not paint chips      |
| https://24ways.org/2018/designing-your-site-like-its-1998/                                                          | Dec 2018    | Planes, Trains and Automobiles page; shows a 3fr 1fr 2fr 2fr 1fr 3fr grid  |
| https://24ways.org/2019/zs-still-not-dead-baby-zs-still-not-dead/                                                   | Dec 2019    | Against flat sameness: depth via blend modes, overlap, z-index (Mini page) |
| https://24ways.org/authors/andyclarke/                                                                              | 2005-2019   | Index of all 15 of his 24 ways pieces (business ones skimmed only)         |
| https://alistapart.com/blog/post/a-different-letter-to-a-junior-designer/                                           | Apr 2014    | Ideas over iteration; practicalities later; sell with passion              |
| https://alistapart.com/author/andyclarke/                                                                           | -           | ALA index: this letter plus a 2004 technical piece (skipped)               |
| https://www.smashingmagazine.com/2019/11/smashing-podcast-episode-1/                                                | Nov 2019    | Smashing Podcast ep. 1, full transcript: "What is art direction?"          |
| https://thewebahead.net/75                                                                                          | Jun 2014    | The Web Ahead ep. 75 "Creative Direction", full transcript (Jen Simmons)   |
| https://thewebahead.net/45                                                                                          | 2013        | The Web Ahead ep. 45 (show notes only; no transcript read)                 |
| https://stuffandnonsense.co.uk/content/transcripts/UBPS3E2-mark-porter.pdf (and E3-E7)                              | 2018        | Unfinished Business art-direction season: 6 transcripts (see below)        |
| https://caffeineandconcrete.com/volume/28/                                                                          | Nov 2017    | Long interview: background, sales, art direction vs product utility        |
| https://www.agencymavericks.com/?p=18771                                                                            | c. 2015     | WP Elevation podcast show notes (no transcript; little design content)     |
| https://stuffandnonsense.co.uk/speaking-info/                                                                       | 2026        | Current talk abstracts: "The designer's scrapbook" (AI), "retro wrestling" |
| https://noti.st/malarkey                                                                                            | 2019        | Notist: "Art Direction for the Web" talk abstract (Contao, SydCSS)         |

## 1. Moves

Each move: what it is, where, the default it replaces, his stated reason, and fit.

### 1.1 Compound grid: lay two grids over each other

- **What.** Overlay two column grids with different counts (6 and 4 for Smashing
  Magazine; 6 and 4 again in Art Direction for the Web) so the layout has more column
  lines than either grid alone. Elements snap to whichever grid suits them.
- **Where.** Direction 16 keynote and Port 80 "imaginative grids" deck: Smashing
  Magazine's editorial content sat on a 6-column grid, but the ads it depends on were a
  bad fit (one column too narrow, two too wide), so a 4-column grid was overlaid; the
  4-column lines also set the size and position of conference promos that "subtly
  interrupt the reading experience" [S]. The deck labels it "6/4 compound grid"
  [O]. The 24 ways 1998 piece shows a modern implementation with columns
  `3fr 1fr 2fr 2fr 1fr 3fr` [O], which is what a 6+4 compound resolves to.
- **Default replaced.** One 12-column, equal-ratio grid (Bootstrap) used for alignment
  only.
- **Why (his words, paraphrased).** "Nowhere is it written that we have to use only one
  grid per page"; compound grids are "an established design technique that's rarely
  used on the web" [S, Direction 16].
- **Fits.** Any page that must hold fixed-size things (ads, product cards, forms) next to
  editorial content; it gives uneven but related column widths. **Does not fit** when
  there is too little content to reveal the second grid; it then reads as random.

### 1.2 Skinny column, often left empty

- **What.** Simplify 12 columns to 6, then split one column into a narrow "skinny"
  column and give the spare width to the opposite side (for a wide tool sidebar). Leave
  the skinny column empty most of the time so the page is asymmetric; occasionally pull
  one element into it for emphasis.
- **Where.** WWF UK fundraising site (Direction 16 talk and Port 80 deck) [S]. The
  skinny left column is empty on most pages, holds a map of where the 880 remaining
  mountain gorillas live, and marks new sections in a conservation timeline instead of
  "Bootstrap's full width fields" [S]. Slides show the hero with a big "880 in the wild"
  numeral in a red circle, condensed uppercase display type, a dark photographic hero
  and a dark fundraising panel on the right [O, sheet-grids-wwf.jpg].
- **Default replaced.** Symmetrical 12-col layout; full-width coloured bands to start
  sections.
- **Why.** Asymmetry "adds to the visual energy and interest"; the grid stays flexible
  and easily responsive [S].
- **Fits** almost any site; cheap to apply. The empty column only works if it is
  disciplined (kept empty except for genuinely special content).

### 1.3 Choose column widths by ratio, not by guesswork

- **What.** Derive column relationships from ratios: golden ratio (carving golden
  rectangles into squares), Fibonacci squares, root rectangles (√2, √3, √4), and a list
  of named ratios (Hecton 1.732, Hemiolon 1.5, Diagon 1.414, Penton 1.272...).
  Fibonacci squares laid out "at first a random arrangement" become a distinctive layout
  [S, Direction 16; O, Port 80 deck slides 19-32].
- **Default replaced.** "Should our main content be eight columns wide, twice the
  sidebar?" decided by guesswork [S].
- **Fits** landing pages and image-led sections where proportion is visible. He also
  built custom grids early on: 84 px columns, 24 px gutters, chosen to give an *odd*
  number of columns at common widths (7, 9, 13) and fit 300 px ad units [S, 24 ways
  2011].

### 1.4 Modular grid as the source of image sizes, type sizes and captions

- **What.** Add horizontal fields so the grid has modules; use modules to fix image
  formats, line lengths and white-space depth, and to make a set of page templates that
  differ enough to avoid repetition but stay connected [S, Direction 16].
- **Captions as a design element.** Put captions above images, beside them aligned to
  the image's bottom, as a long vertical caption filling a column of modules with
  borders, or over a cropped image. "Nowhere is it written that captions must always be
  shown below an image"; "a strong image needs an equally strong caption" [S]. Slides
  show a deep red ground, a 6x4 module grid, one dark module block for the image and the
  caption occupying neighbouring modules [O, sheet-grids-wwf.jpg].
- **Default replaced.** Caption in small grey text under the picture.
- **Fits** galleries, product pages, portfolios; any site with strong photos.

### 1.5 One fixed foundation, then design each piece on top ("the Brody model")

- **What.** Design the foundation once (grid, type hierarchy, recurring "furniture"),
  then art-direct individual pieces almost uniquely on top of it. He names Neville
  Brody's *The Face* as the model and hopes it becomes "the next step in web design"
  [S, UB E2 p20]. ProPublica stories share one typeface and grid but feel entirely
  different [S, Direction 16].
- **Small-business version he describes.** For a French football magazine he designed
  about six layout templates on the same CSS, then separated three independent layers a
  CMS can toggle: **layout**, **theme** (headline, blockquote, table header and button
  styles, each theme named after a French footballer, e.g. "Cantona"), and **colour
  scheme** (six) [S, Smashing Podcast 1]. Fixed pages (league tables, results) stay
  fixed.
- **His phrase for the base layer.** "Foundation styles": colour, type and interaction
  patterns that carry *this* client's personality. "It's okay to have a boring design
  system as long as it's your boring design system and not somebody else's" [S, UB E7
  p17]. Bootstrap tweaked with a few colours, or Material Design, carries someone else's
  personality [S].
- **Fits** exactly the AppBaoBao problem: a shared base with per-client layers. The
  risk he names is that the system becomes the end ("snowflakes" get folded back in) and
  nobody designs "outside of those edges" [S, UB E2, E3].

### 1.6 Change the composition from section to section to match the story beat

- **What.** Treat consecutive pages or sections as panels in a sequence, each with a
  different layout chosen for its moment.
- **Where.** Smashing 2018 Grid article, three Hardboiled pages [S + O,
  sheet-hardboiled-grid-areas.jpg]:
  - *Chapter three (tension):* villains' image as large as possible (citing McCloud:
    panel size controls dwell time), and the layout connects the villains' eye line to
    the woman waiting on the far right, which also leads the reader to where text
    starts.
  - *Chapter four (the fight):* the page's left edge, with no margin, stands for the open
    door; one large spatial zone for the action; content arrives from the top (white
    space drawing the eye down to a bold paragraph) and from the left (a huge stacked
    headline "Kiss Me, Deadly"). "When fists fly in all directions, our layout needs to
    do the same."
  - *Chapter five (order restored):* solid justified columns with lots of white space for
    calm, and a right-aligned caption that "feels edgy and uncomfortable" for the
    interrogation.
- **Default replaced.** Every section the same full-width band with the same internal
  layout.
- **Why.** "Symmetry and asymmetry, harmony and tension" guide people and help them
  understand; layout is as much a communication choice as typeface [S].
- **Fits** long single-page small-business sites well: each section can have a "beat"
  (problem, product, proof, calm close) with its own composition.

### 1.7 Panel size and borders control time (comics)

- **What.** Bigger panels slow the reader; small panels speed them up; a mostly white
  panel can be the most dramatic of all. Removing a border *increases* emphasis, and
  bleeding to the page edge increases it further [S, 24 ways 2007, using *Watchmen*'s
  3x3 grid broken only at dramatic moments and Paul Chadwick's *Concrete*]. He repeats
  this in later talks (Port 80 deck shows *Watchmen* pages [O]) and on UB E5 [S].
- **Default replaced.** Size panels by how much content they hold; use borders/boxes to
  emphasise.
- **Why.** Clients ask to "fill every pixel"; he cites Apple's "Say hello to iPhone"
  page as space telling the story [S].
- **Fits** the key benefit or signature product: give it the big, borderless,
  edge-bleeding treatment and keep secondary content in small, boxed panels.

### 1.8 Headline as a composed object, placed where the story needs it

From the Direction 16 transcript and slides [S + O, sheet-direction16-a/b.jpg]; one
piece of content (Jules Verne's *Voyage au Centre de la Terre*) redesigned many ways:

- Pick a typeface that evokes the subject's era (a modern serif for 1864) [S].
- Put the headline *after* the first paragraphs so those paragraphs become a prologue
  [S].
- Push a headline slightly off the viewport edge with transforms; tight leading and
  overlapping letters make it a visual element [S]. Slides show "Centre" deconstructed
  into stacked oversized letters with "Voyage au" and "de la Terre" tucked in [O].
- Small headline plus lots of white space can attract more than a big one [S].
- Text set as highlighted word blocks forming a ragged shape, like ransom-note strips
  [O].
- Uppercase condensed headline sitting in a modular grid next to an image and a dark
  pull-quote panel [O].

### 1.9 Standfirst, quotes and drop caps as layout tools

All [S, Direction 16] unless noted:

- **Standfirst:** a large gap between standfirst and article gives a pause; centre it as
  the only centred text; place it *above* the headline; align it right; or set it in
  spaced uppercase.
- **Pull quotes:** outdent into the margin with a symbol that points back into the text;
  indent into the right edge of the column (not the left, which makes the next line hard
  to find); vary type size inside the quote to stress words (Brody). Same size/weight as
  body says "equally important", so contrast it.
- **Drop and initial caps:** scale them up on large screens and hang them in the
  margin; frame them; replace them with a symbol or illustration and wrap text around
  it; use more than one per article to mark sections; put a decorative cap behind the
  text. Slides show a huge grey "I" behind the first paragraph and an illustrated
  ornament cap [O].
- **First line:** emphasise the whole first line (it reflows naturally across widths).
- **Taste note:** he does *not* want art direction reduced to this list: he doesn't want
  people to "confuse art direction with hanging [pull] quotes" [S, UB E4 p9-10].

### 1.10 Text shaped by the picture (CSS Shapes as composition)

From the 2019 Smashing article, each shown as a "presentable but predictable" version
next to the shaped one [S + O, sheet-shapes.jpg]:

- **V-shape:** body text runs in a funnel between two triangles, pointing at the car.
- **Z-pattern:** full-width image with a right-aligned headline at its end, a narrow
  column of text squeezed diagonally between two shapes, then a thick-bordered footer
  figure; "suggests speed and the fun" of driving a Mini.
- **Staggered margins:** headline, image and text each get a different left margin in
  `vw`, forming a diagonal from the back of the headline to the front of the car.
- **Diagonal:** text follows a sloped image edge. He notes he sees horizontal and
  vertical axes every day "but rarely anything based on a diagonal" [S].
- **Rotated whole composition:** images drawn rotated +10°, the whole layout rotated
  −10° so the cars look upright and the page tilts; split numerals "19 / 59" in red
  as a side element [O].
- **Numerals carved into columns:** huge "2" and "4" cut into two justified text
  columns, after Brodovitch [O].
- **Warnings he gives:** don't let wrapped lines get so narrow they hold one or two
  words; don't merely mimic old print work [S].
- **Fits** hero and feature sections with a cut-out product photo or illustration. Needs
  an image with a clean silhouette.

### 1.11 Overlap and depth instead of flat side-by-side

- **What.** Make the image and caption share the same grid cell, push the image across
  the full width, and stack the caption above it with z-index; add blend modes and
  transparency for richness [S, 24 ways 2019]. His figure caption: the conventional
  alignment "lacks energy"; overlapping "adds movement" [S].
- **Default replaced.** Flat design with image and text in separate cells: "a
  regrettable uniformity which makes it difficult to distinguish" brands [S].
- **Fits** product shots, hero images. Also: recolour one illustration set by swapping
  background colour plus blend modes instead of exporting new art [S].

### 1.12 One accent colour that ties words to picture

- **What.** A dark, inverse page with a single bright red that links the word "Deadly"
  in the title to the woman's red dress [S + O, Smashing 2018]. The WWF and Direction
  16 decks use the same restraint: one red accent with greys [O].
- **Fits** almost any small-business site: pick one accent that appears both in the
  imagery and in one key word of the headline.

### 1.13 Ownable illustration built from the brand mark (instead of stock)

- **What.** For EPD, a property investment firm, he rejected the sector's default
  ("full-width banners with faded stock photos of generic city skylines or ethnically
  diverse people shaking hands") and drew skylines of Dubai, London and Manchester made
  entirely of circles that echo the logo mark, in off-white on charcoal with teal
  accents [S + O, sheet-ambient-clients.jpg]. For composer Reuven Herman he borrowed
  Alex Steinweiss record-sleeve depth and texture: a floating piano keyboard over wavy
  stave lines [S + O]. For Mike Worth he invented a mascot (orangutan "Orango Jones")
  who appears on every page and takes the reader on an adventure [S].
- **Why.** "A distinctive visual style that the company could own" [S]. He mocks stock
  photography elsewhere: "ethnically diverse people enjoying a spreadsheet" [S, UB E5].
- **Fits** small businesses very well: a single drawn motif derived from the logo or
  product replaces stock imagery across hero, section dividers and 404.

### 1.14 Ambient motion: atmosphere, not action

- **What.** Slow, looping, barely noticed movement (smoke curling, feathers swaying,
  city lights flickering, a wheel turning) that adds mood, not calls to action [S,
  Smashing 2025 ambient 1 and 2].
- **Rules he gives [S]:** choose things that would move in real life ("Does this thing
  have weight? Is it flexible?"); reserve the most obvious motion for what needs most
  impact; keep it slow and smooth; loop seamlessly; layer several small motions with
  different rhythms "like building a sound mix"; if someone's eye is drawn to it, dial
  it back; respect reduced motion. "Restraint isn't just about doing less; it's about
  doing the right things less often."
- **Interaction easter eggs:** a hidden tap target on the mascot's magnifying glass
  lights up the cave; a red button turns off a desk lamp; a 404 where the hero sinks in
  quicksand [S, Smashing 2025 cartoons].
- **Source:** Hanna-Barbera limited animation: few frames, reused backgrounds, static
  bodies with only mouths and eyes animated; constraints "created a charm" [S].

### 1.15 Design the "atmosphere" separately from layout

- **What.** Split a design into layout (changes per screen) and "atmosphere": colour,
  texture, typography (stays the same everywhere). Present atmosphere to clients as
  components out of context, before arranging them [S, Smashing 2012; Modern Designer's
  Canvas 2014; Web Ahead 75]. Brad Frost's notes add texture examples: round or square
  boxes, gradients, a linen background [R].
- **Why.** Clients conflate layout with "the design" ("I don't like the design" really
  means "the sidebar should be on the left") [S]. Separating them focuses feedback.
- **Small screens.** This is his main answer to small screens: on the tiniest screen "we
  may not have layout ... but we still got mood. We still got feeling. We still got
  great typography" [S, UB E7 p12]. Complex grid layout is "almost like another layer of
  progressive enhancement" for big screens [S]. In the Hardboiled example he starts
  small and simply reassigns elements to different template areas per breakpoint; the
  small version stacks the headline above the image but keeps the inverse colours, the
  red accent and the sketch [S + O, sheet-hardboiled-grid-areas.jpg]. In the rotated
  Mini example the small-screen version drops the rotation and stacks [O]. In 2011 he
  recalculated column percentages per breakpoint to keep "connectedness" so elements
  stay in proportion to the viewport [S].
- **Gap.** Rob Weychert (guest) says phone layouts are still a "tall stacked thin
  layout" and nobody has solved memorable storytelling there; Clarke does not offer a
  method [R, UB E7].

### 1.16 Uneven colour hierarchy instead of equal swatches

- **What.** Show the palette as a hierarchy: different-size panels, colour blocks on a
  modular grid, shapes from the brand (not default circles), colour repeated across
  pages in context [S, 24 ways 2016]. He praises OpenTable for sizing chips by role and
  criticises equal "paint chart" chips and GOV.UK's unexplained circles [S].
- **Fits** the client-facing brand sheet AppBaoBao delivers, and on-site colour usage
  (one dominant, one supporting, one accent in clearly unequal amounts).

### 1.17 One truism, then one line (copy as part of art direction)

- **What.** List truths about the company, cut to the single most important one, and
  write a tagline from it that is "difficult to argue with" and uniquely theirs [S, 24
  ways 2014]. Stuff & Nonsense's became "Fabulously flexible". He points at agencies
  who all "craft delightful digital experiences" as the default to avoid [S].
- **Concept example.** For a developer shop with a template site: ignore "what do users
  expect" at first and ask "Why are we different? What are we saying?"; what is the
  picture (his made-up "banana") on the home page, why is it there, what wordplay does it
  set up, could it work in other media [S, Web Ahead 75]. His own site's apes header is
  tied to a new message and new copy [S].
- **Fits** every small-business site; it is the step before any layout.

## 2. Process and thinking

- **Definition.** "Art direction is the art of distilling an essential, precise meaning
  or purpose from a piece of content ... and then conveying that meaning or purpose
  better by using design" [S, Direction 16; repeated in Smashing 2018]. On the podcast
  he defines it by examples: the Boddingtons "Cream of Manchester" posters (the creamy
  head shaped into an ice cream or a quiff shows the product's key trait) and a magazine
  cover that put the barcode on Trump's top lip [S, Smashing Podcast 1].
- **It is about feeling.** "What is somebody feeling at this point? ... quirky and
  delightful or more serious and conservative" [S, Smashing Podcast 1]. Even a spinner's
  bounce is art direction if it says something about the brand [S, UB E3].
- **Every story has a deeper message.** A company, charity or app has a story beyond
  the facts: "what does that actually mean in people's lives?" [S, Direction 16].
- **Start with purpose, not features.** For Smashing Magazine he ran about a week of
  round-table workshops, three or four times, to find "the Smashing message"; the output
  was words ("bright and bold", "turned up to eleven", "quirky") handed to Dan Mall as a
  brief, plus rough early concepts [S, Smashing Podcast 1]. He would ask Notist what its
  bigger purpose is beyond hosting slides [S].
- **Principles workshop.** Single words, not sentences ("bold, clear, intentional,
  reassuring"); then for a week everyone pins up references meaning "this is bold to
  me" and the group finds common ground; "reassuring" turned out to mean warm neutrals,
  and also behaviour such as pulsing placeholders [S, UB E3, E6]. He strongly agrees
  with Stephen Hay's funnel: values, moods and metaphors, concept, visual language, then
  design [S, UB E6].
- **Instinct over research for direction.** "I don't need somebody to test something to
  tell me that I'm going in the right direction"; early user testing is "the ultimate
  delegation" [S, Web Ahead 75]. "You can't turn a poor idea into a brilliant one by
  iterating" [S, ALA 2014]. Don't kill an idea by asking about build and usability too
  early [S, ALA 2014].
- **Look outside the web, understand the principle, don't pastiche.** "To make inspired
  design decisions, we need to feel inspired"; study designers outside the web and the
  context they worked in so as to avoid "retro designs that are just pastiches" [S,
  Direction 16]. He keeps Dropbox folders of print inspiration [S, Smashing 2019]. In
  2026 he talks about using AI as a "designer's scrapbook" for references and early
  directions, "a reference rather than a replacement" [S, speaking-info].
- **Working with clients.**
  - No big reveal; keep clients involved throughout (shared folders, working on site
    alongside them) [S, Smashing 2012].
  - Never email a picture and ask for "thoughts"; run structured, face-to-face design
    crits with time and scope limits; only attendees get an opinion, including the CEO;
    leave feelings at the door [S, Smashing 2012].
  - Don't get sign-off on static full-page comps: they set wrong expectations (fixed,
    centred 960 px sites exist because clients signed off 960 px pictures) [S, Smashing
    2012 and 2014].
  - Ask for feedback in feeling words ("too quiet", "doesn't feel like us"); he calls
    "It doesn't feel like us" incredibly important feedback [S, UB E3]. He agrees with
    Mark Porter: judge a design after a week of living with it [S, UB E2].
  - Selling is a skill: learn to present so the client "must buy from you" [S, ALA
    2014]. He learned it selling cameras for years [S, Caffeine & Concrete].
  - "You are the designer ... never underestimate your role" [S, Smashing 2012].
- **Tools.** Graphics apps for atmosphere and polish, real browser for layout; CSS Grid
  used live with the client to "get the layout right" [S, Smashing 2012; UB E4]. Starts
  small and works up [S, Smashing 2018].
- **How much art direction.** Proportional to the job: he quotes Mark Porter that GOV.UK
  is great art direction because it leaves him reassured [S, Smashing Podcast 1];
  expressive work suits brands where feeling sells.

## 3. Taste

- **Dislikes (all [S]).** Sites "not a gajillion miles away from framework default"
  (Smashing Podcast 1); Bootstrap's 12-column sameness and "every effing Bootstrap
  website" (Direction 16); Squarespace-like tidy, "soulless" sites with none of the
  owner's personality (Web Ahead 75); flat design's uniformity (24 ways 2019); paint-chip
  style guides; stock photos of handshakes and skylines; agency taglines about
  "delightful digital experiences"; atomic design's periodic-table metaphor ("I can't
  imagine anything less creatively stimulating", Modern Designer's Canvas); product
  thinking that treats design as decoration added at the end; SlideShare ("dreadful").
- **Praises (all [S]).** Neville Brody's *The Face* ("still inspired by this every
  day"); Alexey Brodovitch's *Harper's Bazaar*, especially his pencil sketches;
  ProPublica (two-voice story with illustration vs photography; tiny drug-test kit image
  to show disproportionate consequences; "Lost Mothers" mostly-empty grid); Mark
  Porter's Guardian; Jason Santa Maria and Trent Walton's per-post art direction;
  GOV.UK for fitting its purpose (while joking it is "the website that design forgot");
  Hanna-Barbera backgrounds; Alex Steinweiss sleeves; advertising craft (Benson & Hedges,
  Marlboro, MasterCard "Priceless", Guinness).
- **Influences.** Comics (*Watchmen*, *Concrete*, Scott McCloud's *Understanding
  Comics*; his art-school dissertation was on Batman), hardboiled crime fiction and its
  covers, 1960s British pop culture (Mod, the original Mini), Planet of the Apes and
  King Kong, pop art and Hockney, vintage car and poster advertising, British retro
  wrestling posters (2026 talk), magazines browsed at Magma Books [S].
- **Personality in the work [O].** Recurring motifs: apes and gorillas, film noir pin-ups
  and gangsters, classic cars, cartoon mascots, big numerals in circles, dark inverse
  pages with one hot red accent, condensed uppercase display type, tilted elements. He
  likes "embellishment": "stuff is stimulating" [S, UB E6]. Humour is part of the
  delivery (puns, mock-hardboiled voice).
- **Values.** Commercial and creative are not opposed: "to do the commercial right, you
  have to have soul ... you're not going to sell" [S, Web Ahead 75]. Art direction
  amplifies content and utility rather than fighting it; don't break mental models (keep
  the CTA obvious) but be distinctive everywhere else [S, Caffeine & Concrete]. Designers
  should put themselves into the work; "you can see their fingerprints" [S, Direction
  16].

## 4. Open questions

- **"Designing for Changes"** and a talk literally titled **"Hardboiled"**: I found no
  public page, slides or transcript under those titles. The Hardboiled theme appears in
  the 2018 Grid article and several Speaker Deck workshop decks (not read in full).
- **The Web Ahead ep. 45** (2013) has no transcript I could find; only show notes read.
- **Unfinished Business transcripts** are machine-made and garbled in places; the
  digest marks uncertain readings. Audio was not used.
- **Video-only talks** (Counting Stars 2015, Direction 16 video, SmashingConf talks) sit
  behind Conffab or Vimeo; I used the Direction 16 transcript and abstracts only.
- **Net magazine / Creative Bloq**: no Clarke-authored article or interview surfaced in
  searches; the Port 80 deck cites Creative Bloq pieces by others (Elliot Jay Stocks,
  Noah Stokes) as the "soul" debate he joins.
- **Small screens:** across all sources he never gives a full method for keeping art
  direction on phones beyond "atmosphere survives" and reassigning grid areas. Worth
  checking his books or the IDD series (other stream), where he says he shows how to
  "maintain scale contrast on even the smallest screens" (Bea Feitler blurb).
- **Smashing Magazine compound grid** slides referenced a live demo at
  malarkeyhosting.com/smashing; not checked.
- **Mike Worth, Reuven Herman, EPD** live sites were not screenshotted here (the
  `clients` stream may cover them); I looked at the article figures only.
