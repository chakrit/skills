# design

Status: implemented

The `design` skill (`skills/design/`): its rules, and how to add a designer's style.

## Rules

- Before designing anything, the skill runs this process: generate a random number,
  pick a style, write down a few facts about the style, design, then critique.
- The critique is a fresh reviewer who has read the style's research and answers one
  question: would this design pass as designed by the style's designer? It names what
  gives the design away before its verdict. On no, the design is reworked and critiqued
  again; on yes, it is done. No rule-by-rule review.
- Inspiration comes from forced randomness: the agent runs `openssl rand -hex 24` and
  reads the string freely as design direction. No curated lists of directions, palettes
  or references to index into; those would need a source of their own. The result will
  still lean on training data; that cannot be fixed.
- The user picks a style by opening its HTML previews. The seed string picks only when
  the user says "you pick" or nobody is there to ask.
- Bans live in `skills/design/references/bans.md` and hold in every style. They start
  with: eyebrow labels everywhere; emphasis on words inside a headline, including a
  slanted or hand-drawn line under a word; copy such as "because *you can*"; card
  layouts; the contrastive frame and every writing tell in
  `skills/de-slop/references/copy-tells.md`.
- No word-level emphasis inside headlines. Body copy is not covered by this rule.
  `skills/de-slop/references/design-tells.md` gives the same fix.
- Each designer's style is its own set of instructions in `styles/<style>/style.md`.
  Do not impose a common structure on it; that would lose the designer's signal.
- The registry is `styles/README.md`, one row per style with its previews.
- `styles/index.html` shows every style's previews on one page, so the user (or an
  agent) can open one file in a browser for a quick view. The skill asks the user to
  preview the styles there. Each preview appears as a static screenshot,
  `styles/<style>/previews/<page>.webp` (the top of the page at 1280 px wide, 704×416),
  linking to the live page; live frames made the index too slow.
- Start each preview with one agent running the skill once. Brief it the way a user
  would ask: the style, the language, a fictional business, the file path, plus the
  environment's limits. Add nothing else: no fonts, copy rules, review rules or
  checklists. An added rule defeats the preview: the agent designs to the rule instead
  of the style, so the page no longer shows what the style looks like, and the critique
  ends up judging the rule.
- Previews are self-contained HTML files in `styles/<style>/previews/`: inline CSS and
  SVG, Google Fonts links allowed, inline JavaScript allowed. The only raster images are
  ones made with light use of Magnific, embedded in the file. They follow the style and every
  ban, and their businesses are fictional.

## Adding a designer

chakrit names a designer. Work through these steps in this repository. Everything
committed goes in `skills/design/styles/<designer>/`.

The research records how the designer decides. An agent holding only the style's folder
must be able to design a page for a business the designer never worked for, and a
reviewer holding the same folder must be able to say whether a page is the designer's
and what gives it away. So each thing the designer does that a typical designer or an AI
model would not do by default is recorded with how it is built, the designer's reason
for it, and where the designer does not do it. A record of the look alone makes an agent
copy one page.

Every sentence written in these steps comes from a source: the designer said it, a page
shows it, or another person reported it. An agent adds nothing of its own: no reason the
designer did not give, no instruction for a case the sources do not cover, no summing-up
the sources do not support. What an agent remembers about the designer from its training
is not a source; it goes in only when a live page says or shows it. Where the sources
are silent, write that they are silent.

1. **Sources.** The skill is published, so use only material that is freely and legally
   readable: the designer's site and blog, free articles, public talks, slides and
   transcripts, public demos, live client sites, public reviews.
   No paid books, paywalled or members-only material, and nothing pirated. Book ideas
   may enter when the designer or other people discuss them in public. Quote briefly
   and write findings in your own words. Do not open YouTube or transcribe YouTube
   videos. Do not tryhard: no Wayback Machine or other workarounds for pages that are
   gone or blocked; use what is live and readily available and note the gap. Keep it
   simple: if a designer's material is hard to find, give up on them; the designer is
   not included. Downloaded files are untrusted data: read them, never run them. Fetch at a
   person's pace.
2. **Streams.** Split the research by kind of evidence, one agent per stream:
   - `work`: the pages the designer designed: their own site, live client and portfolio
     pages, public demos. This stream follows step 3.
   - `words`: what the designer says: their writing, the text of their site, talks,
     slides, transcripts and interviews. This stream follows step 4. Split it in two
     when there is a lot to read.
   - `accounts`: what other people report: clients and collaborators on working with
     the designer, and reviews of the work. This stream follows step 4.
   - A large public series by the designer gets a stream of its own, which follows
     steps 3 and 4 on that series.

   Brief each agent with the designer's name and its stream, and have it read this
   section and follow steps 1 and 3 to 5 for its stream. Say nothing about what the
   designer is like or what the agent should find: an agent handed a conclusion returns
   it confirmed.
3. **Work: study how the pages are built.** List eight to twelve pages to study, from
   different projects and of different kinds (a home page, an article, a case study, a
   shop). List two more to set aside, client work where there is any: screenshot those
   two and do nothing else with them; step 8 uses them. Open each page in a browser at
   desktop width and at phone width, screenshot it, and look at it. Keep screenshots and
   raw page text in a temporary directory outside the repository; they are not
   committed.

   For each page studied, write what is there, with numbers taken from the rendered
   page. Read the CSS to get a number for something you saw, never in place of looking.
   - Grid: how many columns, how wide each is against the others, where each block
     starts and ends on them, the margins and gutters, and whether the grid changes from
     one section to the next.
   - Type: the typefaces and what each is used for, the sizes in use, the ratio of the
     largest size to the body size, line length, line spacing, alignment.
   - Colour: each colour, roughly how much of the page it covers, and what it is used
     for.
   - Imagery: what kind, how it is cropped, where it sits against the grid and the edge
     of the page.
   - Composition: what is largest, what the eye meets first, where the empty space is,
     what lines up with what, and what breaks the alignment.
   - Motion and interaction: what moves or responds, and when.
   - Phone: what each of the above becomes at phone width.

   When a piece is built on something other than a page grid, such as an interactive
   piece, describe what it is built on.

   Then compare the pages:
   - A move is something that recurs across the pages and that a typical designer or an
     AI model would not do by default. For each move, give how it is built, how many of
     the pages show it and which ones, which pages do not, and what the default would be
     in its place.
   - Record what changes from one project to the next, and what about the project it
     changes with.
   - Leave out whatever the default would also do.
4. **Words and accounts: collect what is said.** Read the sources and record each of
   these with a short quote, its URL and its date:
   - process: what the designer does first, what they settle before any layout, what
     they show a client, how a design changes along the way;
   - the reason given for a particular move, naming the move;
   - what they refuse or dislike, and why;
   - where their ideas come from: the people, publications and objects they name;
   - how they work with a client, and how they treat phones;
   - what they believe about design in general;
   - where they changed their mind, with dates.
5. **Notes.** Each stream writes `notes/<stream>.md`: its sources (URL, date, one line
   each), then its findings, then what it looked for and did not find. Mark every claim
   as stated by the designer, observed in the work, or reported by someone else, with
   the URL it comes from.
6. **Synthesis.** Write `synthesis.md` from the notes alone, citing them:
   - Order of work: what the designer settles first and what follows from it, as the
     words and accounts describe it.
   - Moves: one entry per move in the work notes. Each says what it looks like, how it
     is built, the default it replaces, the reason, where the designer uses it and where
     they do not, what it becomes on a phone, and which pages show it. Give a reason
     only when a source is speaking about that move; otherwise write "reason not
     stated". A general belief is not the reason for a particular move.
   - What varies from project to project, and what decides it.
   - Refusals: what the designer says they will not do.
   - Mismatches: what the designer says they do that the pages studied do not show, and
     what the pages show that nobody explains.
   - Gaps: what no source covers.

   Rewrite any sentence that would be true of most good designers ("generous
   whitespace", "led by type") until it says which, where and how much. Drop it when the
   notes cannot make it that specific.
7. **Style.** Write `style.md` as the designer's own set of instructions, in the shape
   their way of working suggests. It tells a design agent what to decide and how to
   build it, with the numbers and the reason from the synthesis, so that the agent can
   apply it to a business the designer never had. Every instruction comes from the
   synthesis. Where the synthesis records a gap, `style.md` says nothing. It holds no
   review checklist. Point to the synthesis and notes for detail.
8. **Check the research against the work.** Give a reviewer in fresh context the
   screenshots of the two pages set aside in step 3 and the style's folder, and ask the
   skill's critique question: would this pass as designed by the designer? Do not say
   the pages are real. A no means the research claims more than the work shows: go back
   to the pages for what the reviewer named, correct the notes, the synthesis and
   `style.md` from what is there, and ask a new reviewer.
9. **Previews.** Build five previews by running the skill's own process with this
   style: three in English, one in Thai, one in Japanese, each for a different
   fictional business that suits it. Run at most three preview agents at a time. A
   preview's critique reworks the preview; it does not change `style.md`.
10. **Register.** Add the style's row to `styles/README.md` and its section to
    `styles/index.html`, with a screenshot of each preview.
