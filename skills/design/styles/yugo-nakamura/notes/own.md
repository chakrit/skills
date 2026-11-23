# Yugo Nakamura: own sites

Stream `own`. Raw copies are in `/tmp/designers/yugo-nakamura/raw/own/`, one file per
source, URL on the first line. Claim tags: **[stated]** Nakamura or tha said it,
**[observed: seen]** looked at in Chrome, **[observed: code]** read from markup, CSS or
JS only, **[reported]** someone else said it.

Scope note, 2026-11-23: midway through, chakrit ruled out the Wayback Machine, YouTube and
other workarounds. The three Wayback views below were made before that ruling; nothing
further was pulled from the archive. Nakamura keeps no blog or essays on his own sites
that I could find; his own words live in interviews (see `talks.md`).

## Sources

| Source                                                    | Date        | What it gave                                                         |
|-----------------------------------------------------------|-------------|----------------------------------------------------------------------|
| tha.jp (home)                                             | live 2026   | Black page, plain title list, video on hover, scrambling tagline     |
| tha.jp/works                                              | live 2026   | Full works index 2003–2025 with tags; 3-column thumbnail grid        |
| tha.jp/about                                              | live 2026   | Self-description, members, awards                                    |
| tha.jp theme `main.css` and `bundle.js`                   | live 2026   | Helvetica Neue Thin/Roman + Noto Sans JP; text-shuffle routine       |
| yugop.com                                                 | live 2026   | "Under maintenance" placeholder pointing to tha.jp                   |
| web.archive.org yugop.com 2005-01 (Flash via Ruffle)      | 2004–2005   | yugop.com shell: pixel-font bar of numbered experiments              |
| web.archive.org yugop.com 1999-11, 2001-01 (HTML only)    | 1999–2001   | Titles "Gateway / MONO*crafts", "MONO*CRAFTS 3.0"; 550×200 Flash     |
| web.archive.org yugop.com CDX listing                     | 1999–2026   | File names of the experiment series (finger, distance, tree, etc.)   |
| web.archive.org tha.jp 2009-01 and 2014-01                | 2009, 2014  | tha's own site as a near-unstyled serif blog                         |

## 1. Moves

### Move: the list is the interface, the work plays behind it

- **What.** tha.jp's home is a black field with a left-aligned stack of project titles in
  small grey caps (mixed with Japanese). Hovering a title brightens it and plays that
  project's footage full-bleed behind the list; the list stays put. No hero, no cards, no
  intro copy. **[observed: seen]**
- **Default it replaces.** The portfolio hero plus thumbnail grid. The grid exists one
  click away on /works (a plain 3-column grid of 16:9 stills with title and date under
  each, all caps, tiny), but the home page refuses it. **[observed: seen]**
- **When it fits.** A body of work that is mostly motion: let the pointer choose what
  moves, and keep the typographic layer quiet so the footage carries the page.

### Move: text that decodes itself

- **What.** The tha.jp header tagline "THA LTD. IS DEVELOPING IDEAS FOR COMPOSITION OF
  LOGICS." first appears as random ASCII and settles letter by letter into the sentence.
  **[observed: seen]** The theme script offsets each character code by a random amount
  (clamped to printable ASCII 33–126) and steps it back one code per frame until it lands.
  **[observed: code]**
- **Earlier use.** The 2005 yugop.com shell did the same to its one-line captions: click an
  experiment and its description rattles through junk characters before reading
  "SIMPLE SKETCH OF HORIZONTAL COMPOSITION. MOVE YOUR MOUSE ON THE SURFACES". **[observed:
  seen, Wayback, before the ruling]**
- **Why it matters.** Type behaves as a process, not a static label: the reader sees the
  program arrive at the text. It is cheap, monospaced-feeling and very recognisable.
- **When it fits.** Short labels and taglines in all caps; never body copy.

### Move: the site as a numbered lab notebook

- **What.** yugop.com (personal site, 1999–c.2013; Ars Electronica Distinction 2005, per
  tha.jp/about **[stated]**) was organised as a run of numbered experiments ("stuff"
  01, 02 … and "FEED 01–06"), each a small interactive Flash sketch with a one-line caption
  of what physics or logic it tests ("MOTION LOGIC WITH RIGID BODY DYNAMICS. DRAG EACH CELL
  TO INTERACT"), plus ARCHIVE and PRODUCT tabs and a last-update date. **[observed: seen,
  2005 capture]** File names in the archive index show the series: finger1–5, distance,
  tree, gas, drag_and_throw, modulator, fingertension, clockblock. **[observed: code]**
- **Look.** White field, the sketch centred, a black strip along the bottom holding square
  numbered cells in a tiny pixel font, the active cell widening to show its title.
  **[observed: seen]**
- **When it fits.** A studio or personal site whose content is many small behaviours;
  number them, caption each with the rule being tested, date them.

### Move: the studio's own site stays plain

- **What.** Between at least 2009 and 2014 tha.jp was a near-default blog: lowercase
  "tha ltd." in a large serif, post titles as blue serif links, a narrow right column of
  plain link lists ("our product", "our services", "our label", "client works").
  **[observed: seen, Wayback, before the ruling]** The 2017 theme still in use is black or
  white, Helvetica Neue Thin and Roman at 13.5–15 px with a few 25–42 px sizes,
  Noto Sans Japanese for kana and kanji. **[observed: code]**
- **Reading.** The famous interactive studio does not perform on its own index; the
  pieces perform. Treat as an inference, not his statement.

## 2. Process and thinking

- The studio describes itself as a group of designers and programmers trying to make their
  own media design from both the expression side and the technical side, across web,
  apps, film, TV, installations and games. **[stated, tha.jp/about, own translation]**
- The English tagline frames the work as "composition of logics": design as arranging
  rules and behaviours rather than pictures. **[stated, tha.jp header]**
- Captions on yugop.com name the logic first ("motion logic with rigid body dynamics",
  "simple sketch of horizontal composition"), then the instruction to the user.
  **[observed: seen]**

## 3. Taste

- Monochrome grounds (black or white), small all-caps neo-grotesque labels, Thin weights,
  colour coming only from the work. **[observed: seen, code]**
- Bitmap pixel type on the Flash-era site. **[observed: seen]**
- Clocks recur across his own label and client work (DropClock, Kaze to Desktop as a
  wind-driven screensaver, Industrious Clock, Toranomon Hills Clock, GRANSTA Clock).
  **[observed: tha.jp/works index]**

## 4. Open questions

- What the individual yugop.com sketches looked like in motion: the content SWFs did not
  load in the archive shell, and the ruling ended further attempts.
- Whether Nakamura wrote any essays or notes on his own site; none found.
- The exact years of each yugop.com version (MONO*crafts 1–3, ver2, ver3, ver4).
