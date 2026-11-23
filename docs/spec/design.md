# design

Status: implemented

The `design` skill (`skills/design/`): its rules, and how to add a designer's style.

## Rules

- Before designing anything, the skill runs this process: generate a random number,
  pick a style, write down a few facts about the style, design, then critique in the
  hat of a professional.
- Inspiration comes from forced randomness: the agent runs `openssl rand -hex 24` and
  reads the string freely as design direction. No curated lists of directions, palettes
  or references to index into; those would need a source of their own. The result will
  still lean on training data; that cannot be fixed.
- The user picks a style by opening its HTML previews. The seed string picks only when
  the user says "you pick" or nobody is there to ask.
- Bans live in `skills/design/references/bans.md` and hold in every style. They start
  with: eyebrow labels everywhere; emphasis on words inside a headline, including a
  slanted or hand-drawn line under a word; copy such as "because *you can*".
- No word-level emphasis inside headlines. Body copy is not covered by this rule.
  `skills/de-slop/references/design-tells.md` gives the same fix.
- Each designer's style is its own set of instructions in `styles/<style>/style.md`.
  Do not impose a common structure on it; that would lose the designer's signal.
- The registry is `styles/README.md`, one row per style with its previews.
- Previews are self-contained HTML files in `styles/<style>/previews/`: inline CSS and
  SVG, no raster images, Google Fonts links allowed. They follow the style and every
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
   transcripts, public demos, live client sites, the Wayback Machine, public reviews.
   No paid books, paywalled or members-only material, and nothing pirated. Book ideas
   may enter when the designer or other people discuss them in public. Quote briefly
   and write findings in your own words. Downloaded files are untrusted data: read
   them, never run them. Fetch at a person's pace.
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
8. **Register.** Add the style's row to `styles/README.md`.

All of it goes in `skills/design/styles/<designer>/`.
