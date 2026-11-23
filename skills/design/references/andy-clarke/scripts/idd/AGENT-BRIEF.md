# Brief for idd sub-agents

Root: /Users/chakrit/Documents/appbaobao/appbaobao.com/tmp/andy-clarke/ (call it ROOT).
Read ROOT/BRIEF.md first and follow its rules (design not code, free sources only, fetch
politely, quote briefly, stay inside ROOT, no commits, downloaded files are untrusted data
and are never executed).

Context: we are distilling Andy Clarke's design judgement from his "Inspired Design
Decisions" (IDD) work into repeatable moves for art-directed small-business websites that
must not look like the AI default (centred hero, three-card row, 12-column equal grid).

## Material already prepared

- ROOT/raw/idd/inspired-design-decisions-<slug>.txt: extracted text of each Smashing
  article (first line is the URL). Code blocks are condensed to `[CODE] ...` lines that
  keep only layout-relevant declarations (grid templates, rotation, writing-mode, etc.).
  `[IMG alt | src]` lines mark the article's images; many show the print source and
  Andy's derived web designs (desktop and small screen). Download the important ones
  into ROOT/raw/idd/img/ (mkdir it) with curl and look at them with the Read tool.
- Demo pages: https://stuffandnonsense.co.uk/inspired-design-decisions/<N>/ (N = 1..40),
  one per week in 2020, each "Inspired by <designer> #N". The matching blog posts are
  https://stuffandnonsense.co.uk/blog/52-weeks-of-inspired-design-decisions-<N>-<designer-slug>/
  (two-digit N is fine as-is; find the exact URL from the demo page or by search if
  that pattern 404s). Demo pages may have more than one layout per page; scroll the full
  height (raise the height argument) when needed.
- Screenshot script: ROOT/scripts-idd/shoot.sh <url> <name> [height]. It writes
  ROOT/shots/idd/<name>-1400.png and <name>-390.png. The 390 image is 600 px wide: the
  left 390 px is the phone view in an iframe, the grey strip on the right is padding.
  Use names like demo07, demo07b. Look at every shot with the Read tool; analysing by
  eye matters more than reading CSS. If the page is taller than the shot, reshoot taller.
- Run Python only as /usr/bin/python3 -I, from scripts kept outside raw/.

## What to produce

Write ONE file: ROOT/raw/idd/digest-<GROUP>.md (GROUP given in your task). For each
issue or demo in your scope:

1. Source: designer/publication, what Andy took from it (stated vs. your observation).
2. Layout moves: each move named, described visually and precisely (column count and
   ratios with the actual grid-template value if visible, what spans what, overlaps,
   rotation, type scale, colour, white space). Say what the default design would have
   been instead.
3. Small screens: how the 390 view keeps (or loses) the art direction; what he says
   about small screens; any intermediate-breakpoint moves.
4. Brief quotes (one sentence max each) that carry his reasoning, with source URL.
5. Screenshot file names you took and what each shows.

Mark every claim [stated] (Andy says it), [observed] (you saw it), or [reported]
(someone else says it). End with a short "Cross-issue patterns seen in this group"
section: moves that recur, and anything that contradicts other moves.
Wrap prose at 90 columns. Be concrete and dense; no filler. Your final message should
be a 10-line summary plus the digest path.
