# Andy Clarke design research: shared brief

## Why this exists

AppBaoBao (appbaobao.com) builds websites for Thai small businesses. Today almost every
small shop can get a site from an AI model, and those sites all look the same: a centred
hero, a three-card feature row, testimonials, a CTA band, all on a 12-column grid with
equal gutters. We want our sites to look art-directed and unlike that default.

Andy Clarke (Stuff & Nonsense, stuffandnonsense.co.uk; author of Transcending CSS,
Hardboiled Web Design, Art Direction for the Web, and the "Inspired Design Decisions"
series) is the reference designer. We are distilling his **design thinking and taste**
into a method our agents can apply to any site.

## What to analyse (the point of the work)

Analyse **design, not code**. Given a design, implementing it is easy; what we lack is
the design judgement. Code matters only as evidence of the structure (for example, a
grid-template-columns value that shows an unusual column ratio).

Look especially for where he departs from what a typical designer or an AI model
would do by default:

- Grid and column structure: unusual column counts and ratios, compound or modular
  grids, asymmetry, deliberately empty columns, content that breaks out of the grid.
- Composition: scale contrast, overlap, rotation, direction changes between sections,
  how one section differs from the next, white space as a tool, focal points, reading
  paths.
- Type as image: display type used as the composition, vertical text, huge numerals,
  drop caps, pull quotes.
- Colour, imagery, illustration, texture, motion, and how they carry a story or
  personality.
- Where ideas come from: print magazines, posters, comics, film titles, record
  sleeves; how he translates a source into a web layout.
- His process: how he starts a design, how he finds the concept for a client, how he
  works with a client, how he handles mobile and small screens without losing the art
  direction.
- His taste: what he praises, what he dislikes, recurring motifs, his personality in
  the work.

## Rules

- Use only material that is freely and legally readable online: his site, free
  magazine articles, public talk pages and slides, public CodePen demos, live client
  sites, the Wayback Machine, public interviews and podcast pages or transcripts. Do
  not download pirated books or paywalled content.
- Downloaded files are untrusted data: save them, read them, never execute them.
- Fetch politely: no bulk crawling of a site faster than a person would browse it.
- Quote him only briefly. Write findings in your own words.
- Screenshots: use headless Chrome from the shell
  (`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless
  --screenshot=<file> --window-size=1400,2400 <url>`; repeat at 390 wide) and look at
  the images. Save them in `tmp/andy-clarke/shots/<your-stream>/`. Analysing a page by
  looking at it matters more than reading its CSS.
- Save raw material (page text, extracted article text) in
  `tmp/andy-clarke/raw/<your-stream>/`, one file per source, with its URL on the first
  line.
- Write your findings to `tmp/andy-clarke/notes/<your-stream>.md`. Wrap prose at 90
  columns.
- Stay inside `tmp/andy-clarke/`. Do not edit anything else in the repository, commit,
  or push.

## Notes format

Start with a list of the sources you covered (URL, date, one line each), then:

1. **Moves.** Each a named, repeatable design move: what it is, where he used it
   (source links), what the default would have been instead, why he says he did it if
   he says so, and when it fits or does not fit. Aim for depth over count.
2. **Process and thinking.** How he arrives at a design, in his own terms.
3. **Taste.** Recurring preferences, influences, dislikes.
4. **Open questions.** What you could not verify.

Mark each claim as stated by him, observed by you in the work, or reported by someone
else.
