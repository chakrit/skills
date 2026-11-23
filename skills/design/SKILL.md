---
name: design
description: >-
  Art-direct a web page, site or visual UI in a chosen designer's style, seeded by real
  randomness so designs don't come out the same, and free of AI-slop patterns. TRIGGER
  when the user asks to design, redesign or art-direct a website, landing page, page
  layout or visual identity for the web; to "make it look designed" or "not generic";
  to pick or preview a design style; or invokes /design. DO NOT TRIGGER for auditing or
  stripping AI tells from existing work without a redesign (use de-slop), for backend
  or purely functional UI fixes, or for charts and data visualisation.
---

# design

| Operation       | Use when                                                      |
|-----------------|---------------------------------------------------------------|
| Design          | the user wants something designed or redesigned: steps 1–5    |
| Show the styles | the user asks which styles exist or wants to see the previews |

Paths below are relative to this skill's directory. Give the user absolute paths.

## Files

- `styles/README.md`: the style registry, one row per style.
- `styles/index.html`: one page showing every style's previews side by side, for the
  user to browse and pick from.
- `styles/<style>/style.md`: that style's instructions. Each style is written in its
  own shape; read it whole and follow it as written.
- `styles/<style>/previews/*.html`: self-contained pages showing the style.
- `references/bans.md`: patterns no design may use, in any style.

## Design

Run every step in order, before and around any design work. Skip none, including for a
small change.

1. **Seed.** Run `openssl rand -hex 24` in a shell and keep the output string. Never
   write a string yourself: a made-up string is not random. If no shell can run it, ask
   the user to run the command and paste the output, and wait.
2. **Pick a style.**
   - The user named a style in the registry: use it.
   - Otherwise list the registry's styles with one line each, give the absolute path of
     `styles/index.html`, and ask the user to open it in a browser, look at the previews
     and pick a style. When you run on the user's own machine, you may open it for them
     (`open <path>` on macOS, `xdg-open <path>` on Linux). Wait for the answer.
   - The user says "you pick", or the work runs unattended: read the seed string and
     let it choose among the registered styles.
3. **Write the brief.** Read the chosen `style.md` and `references/bans.md` in full.
   Write `design-brief.md` where the project keeps work files (its own convention
   first; otherwise a temporary directory) and give the user its path. It holds:
   - the seed string, and what you read in it: look for patterns, repeats, special
     numbers, letters, anything that suggests a palette, a layout, a type choice or a
     rhythm. Read it freely; there is no fixed mapping;
   - a few facts about the style that will govern this design, in your own words,
     taken from `style.md`;
   - the decisions the style asks for before any layout (for example a concept, a
     reference, a palette, type);
   - the bans most at risk for this design.
   Never show the seed string in the design itself.
4. **Design.** Follow the style's own order of work and the brief. Let the seed's
   reading decide what the style leaves open. Check each choice against
   `references/bans.md` as you make it.
5. **Critique.** Render the design at desktop and phone widths and take screenshots.
   Give a reviewer in fresh context the screenshots, `design-brief.md`, the style's
   folder (`style.md`, `synthesis.md`, `notes/`) and `references/bans.md`, and nothing
   else from this session. The reviewer is a subagent when the harness has one,
   otherwise yourself after re-reading only those files. The reviewer answers one
   question: would this design pass as designed by the style's designer? It first
   names what gives the design away as not theirs, if anything (a banned pattern is a
   giveaway), comparing it with the designer's real work as the notes describe it.
   Then it gives its verdict, yes or no.
   - **No:** rework the design as a whole toward what the reviewer named, then
     critique again with a new reviewer.
   - **Yes:** the critique is done.
   When no screenshot can be taken, the reviewer judges the source, and tell the user
   the design was not checked visually.

## Show the styles

Read `styles/README.md`. List each style with its one-line description, give the absolute
path of `styles/index.html`, and ask the user to open it in a browser to preview them.

## Done

A design is done when:

- `design-brief.md` exists with the seed string and its reading, the style facts and
  the style's decisions;
- the last critique's verdict was yes;
- the user has the brief's path and the design's location, and knows whether the
  critique was visual or source-only.
