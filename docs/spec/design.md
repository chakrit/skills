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
  preview the styles there.
- Start each preview with one agent running the skill once. Brief it the way a user
  would ask: the style, the language, a fictional business, the file path, plus the
  environment's limits. Add nothing else: no fonts, copy rules, review rules or
  checklists. A preview exists to show what the skill and the style produce on their
  own. The agent treats every line of its brief as a requirement and puts its effort
  there, so an added rule shows up in the page in place of the style: a copy rule turns
  the page into a writing job and its critique into proofreading.
- Previews are self-contained HTML files in `styles/<style>/previews/`: inline CSS and
  SVG, no raster images, Google Fonts links allowed, inline JavaScript allowed. They follow the style and every
  ban, and their businesses are fictional.

## Adding a designer

chakrit names a designer. Work through these steps in this repository.

1. **Brief.** Write a research brief for the agents gathering the material. It states:
   - the point: the designer's design thinking and taste (layout, composition, type,
     colour, imagery, motion, where ideas come from, how they work with a client, how
     they handle phones), not their code;
   - where the designer departs from what a typical designer or an AI model would do by
     default: that is the signal to collect;
   - the streams, one agent each, chosen for this designer: typically their own writing
     and site, their talks and interviews, their client or portfolio work, and other
     people's accounts of working with them, plus any large public series of theirs.
2. **Sources.** The skill is published, so use only material that is freely and legally
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
3. **Look at the work.** Screenshot pages at desktop and phone widths and look at them;
   looking matters more than reading CSS. Keep screenshots and raw page text in a
   temporary directory outside the repository; they are not committed.
4. **Notes.** Each stream writes `notes/<stream>.md`: its sources (URL, date, one line
   each), then the designer's repeatable moves (what, where, the default it replaces,
   their reason if they give one, when it fits), their process, their taste, and open
   questions. Mark every claim as stated by the designer, observed in the work, or
   reported by someone else.
5. **Synthesis.** Write `synthesis.md`: the design model drawn from all streams, citing
   the notes.
6. **Style.** Write `style.md` as the designer's own set of instructions, in the shape
   their way of working suggests. Point to the synthesis and notes for detail.
7. **Previews.** Build two or three previews by running the skill's own process with
   this style, each for a different fictional business that suits it.
8. **Register.** Add the style's row to `styles/README.md` and its section to
   `styles/index.html`.

All of it goes in `skills/design/styles/<designer>/`.
