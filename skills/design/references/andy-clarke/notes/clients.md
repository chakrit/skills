# Andy Clarke: client sites (stream `clients`)

Scope: sites Andy Clarke / Stuff & Nonsense designed for clients, how he found each
client's concept, and the layout and art-direction moves visible in the live sites.

Claim markers used throughout:

- **[S]** stated by him (his case studies, blog, studio diary)
- **[O]** observed by me in screenshots of the live or archived site
- **[R]** reported by someone else (client testimonial, third party)
- **[I]** my inference, not verified

Screenshots are in `tmp/andy-clarke/shots/clients/` (`<client>-1400.png`,
`<client>-390.png`). The 390 shots are a 390 px iframe inside a 600 px window; the grey
strip on the right is the window, not the site. Headless Chrome at `--window-size=390`
lays out wider and crops, so do not trust 390 captures made that way. Raw text is in
`tmp/andy-clarke/raw/clients/` (`portfolio-*.txt`, `blog-*.txt`, and `body-blog-*.txt`
with the site chrome stripped).

## Sources

Fetched 9 November 2026. Dates are publication dates on the page; many portfolio
companions carry his 2026 rewrite date rather than the project date.

His site (stuffandnonsense.co.uk):

- `/design` and `/sitemap.xml` — current portfolio index; 31 `/portfolio-*` pages.
- `/portfolio-<client>/` for all 31 clients — challenge, approach, solution, captions.
  Small-business pages (Abergele Dental, Black Mountain Honey, NWPS, Dementia Care
  Solutions, Llanasa Council, Emma Bodger, etc.) carry only a title line and gallery.
- `/blog/project-companion-<client>/` (Nov 2025–Nov 2026) — process essays for Mike
  Worth, Michael Baugh, Begoña Pereda, Tristan Jakob-Hoff, Ryan Knaggs, Codeboxx,
  Lockrose, Verkehrsteiner, Portico, Scoring Arts, Moonwalk Audio, Mountain Duck,
  Changemakers, Shared Homeland, Count Binface.
- `/blog/how-i-designed-an-animated-svg-driven-website-for-composer-begona-pereda/`
  (27 Mar 2026) — type selection and SVG player process in detail.
- `/blog/designing-banners-for-the-academy-of-scoring-arts/` (17 Dec 2025) — rejected
  concepts, one after another.
- `/blog/designing-for-the-cheeky-condiment-company/` (31 Mar 2023) — spoof shop.
- `/blog/election-2024-imagining-what-id-make-if-count-binface-came-calling/` (4 Jun
  2024) and `/blog/designing-for-count-binface/` (16 Jun 2024) — spec pitch, then job.
- `/blog/last-week-in-the-studio-cw15-26/` to `cw45-26` (Apr–Nov 2026) — weekly studio
  diary covering Mountain Duck, Ryan Knaggs, Codeboxx, Aurus, Black Mountain Honey,
  Lockrose, Portico, Jas Dosanjh, Moonwalk Audio.
- Older client write-ups (Woodland Trust, Karova, DIG, ISO, Hillsborough, Equfund, New
  Internationalist, Cannybill) and process posts on sign-off and feedback: see the
  section on older work below.

Wayback captures of earlier portfolio pages (2023–2025, fetched over plain HTTP; HTTPS
was refused), saved as `raw/clients/sb-wb-*.txt`: Abergele Dental, Dementia Care
Solutions (`/portfolio-dementiacare`), NWPS, Emma Bodger, Alessandro Mastroianni
(`/portfolio-alessandro`), Neurodiverse, Brexitstan / Rebrand Britain, Reuven Herman.
Six 2023 posts on the Emma Bodger build (`sb-blog-*emma*.txt`). Old Stuff & Nonsense
client lists on Wayback: malarkey.co.uk/Corporate_clients.aspx (Oct 2005),
stuffandnonsense.co.uk/work/ (2008), /clients (2012); the helper saved these to
`/tmp/ac-clients/`, outside our folder. Gallery images from res.cloudinary.com/malarkey
in `shots/clients/gallery/`; design images from his older posts in
`shots/clients/blogimg/`.

Live client sites screenshotted at 1400 and 390 (Nov 2026): mikeworthmusic.com,
mikebaugh.co.uk, begopereda.com, tristanjakobhoff.com, ryanknaggsmusic.com,
codeboxx.co.uk, lockrose.com, verkehrsteiner.ch, porticoinvestment.netlify.app,
moonwalkaudio.com, mountain-duck.netlify.app, scoringarts.com, changemakers.wales,
sharedhomeland.com, cheeky-condiment.netlify.app; Wayback countbinface.com (2 Jul 2024,
1400 only).

## 0. The per-client concept, client by client

This is the part most relevant to AppBaoBao: for each client, where the concept came
from. Grouped by the source he mined. Detail on each move follows in section 1.

| Client (trade)                         | Source of the concept                        | Concept → what it became on the page                                                                        |
|----------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Codeboxx (thermal printheads, ribbons) | Product mechanics + a phrase the client said | Printers print QR codes; client said keeping lines moving "is an art" → famous paintings made of QR texture |
| Lockrose (energy project consultants)  | Their own logo shape + a vintage magazine    | Logo triangle → every illustration built from intersecting triangles, Graphis-cover style                   |
| Portico Investment (property)          | The emotional job (trust), not the product   | No buildings; Cubist/De Stijl faceted rectangles = balance, structure                                       |
| Verkehrsteiner (transport planning)    | Reframing the trade one level up             | "Transport planning" → "movement" → animated grid of signal-like circles                                    |
| Moonwalk Audio (game audio)            | Their tagline + a box of the team's own toys | "Imagine the sound of your world" → explorable toy world; objects play sounds                               |
| Mountain Duck (cloud-drive software)   | The product's name                           | A duck → duck-headed machines that move files                                                               |
| Mike Worth (composer)                  | Client's stated passion (DuckTales)          | Original character Orango Jones + a quest story across every page                                           |
| Michael Baugh (composer)               | Client's reading (Asimov) + his studio kit   | 1950s SF paperback look; robots built from amps and jack plugs                                              |
| Begoña Pereda (composer)               | Client's hobby (analogue tape gear)          | Reel-to-reel and cassettes as the actual audio players                                                      |
| Tristan Jakob-Hoff (composer)          | Client's taste (Saul Bass) + his instrument  | Bass-style poster pages; piano keys as the graphic motif                                                    |
| Ryan Knaggs (composer)                 | Client's genre love (horror) + his music     | Dark cinematic palette, condensed type, duotone photography                                                 |
| Jas Dosanjh (memoir author)            | Her existing book-cover artwork              | Cover cages become swinging, clickable banner; palette sampled from covers                                  |
| Academy of Scoring Arts (community)    | Reframing: community, not content            | People photos inside lens shapes woven from music staves                                                    |
| Changemakers (youth politics, Wales)   | Other fields that mobilised young people     | Fanzine and protest-poster language (Rock Against Racism, Red Wedge)                                        |
| Shared Homeland (Palestine-Israel)     | Place and shared geography                   | Topographic and historical maps under translucent blocks                                                    |
| Count Binface (novelty candidate)      | The character's personality and silhouette   | Comic-book type; the bin helmet replaces a letter in his name                                               |
| Cheeky Condiment (spoof jewellery)     | The product itself and British food habits   | Sauce bottles as charms on a bracelet that frames the headline                                              |
| Abergele Dental (family dentist)       | The owner's family-first story               | Cartoon of the dentist's own family; toothpaste tube squeezes out his name as the logo                      |
| Black Mountain Honey (bees, queens)    | Place + product                              | One line drawing: a mountain range whose base is a bee's wing                                               |
| NWPS Construction (builder)            | A verb from the trade                        | "Building confidence / trust / communities" in every heading; orange line drawings                          |
| Dementia Care Solutions (home care)    | Founder's reason for starting                | Tree with heart-shaped leaves: stability plus care                                                          |
| Llanasa Council (13 Welsh villages)    | The place names themselves                   | Width-justified tower of the 13 village names under a wreath of local foliage                               |
| Emma Bodger (film/TV director)         | Her work is "multi-dimensional" + a remark   | Red/cyan anaglyph duotones; hidden Hitchcock theme from something she said                                  |
| Alessandro Mastroianni (sound design)  | Italian heritage + obsessive detail          | Giovanni Pintori palette; fine contour-line illustrations with built-in players                             |
| Dig Business (2005)                    | The client's business card                   | Orange card sliding from a cream sleeve → orange column with the card's thumb-cut                           |
| Woodland Trust shop (2005)             | Their print catalogue + a native bird        | Catalogue-style picture navigation; a robin breaking out of the masthead                                    |
| Ceredigion info service (2008)         | The local town                               | Painted buildings of Aberaeron as hand-drawn line backgrounds, day and night                                |

## 1. Moves

### 1.1 Mine the conversation for one non-design detail; build everything on it

- **What.** In the first conversations he listens for a personal interest, a phrase, an
  object, or a fact about the trade that has nothing to do with web design, and makes it
  the single generating idea for palette, type, illustration and interaction.
- **Where.** Begoña Pereda's love of cassette decks and reel-to-reel machines
  ([project companion](https://stuffandnonsense.co.uk/blog/project-companion-begona-pereda/));
  Michael Baugh's Asimov and vintage SF paperbacks
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-michael-baugh/));
  Tristan Jakob-Hoff's Saul Bass habit
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-tristan-jakob-hoff/));
  Ryan Knaggs's love of horror films
  ([portfolio](https://stuffandnonsense.co.uk/portfolio-ryan-knaggs/)); Codeboxx staff
  saying that knowing what customers need and when "is an art"
  ([CW17-26 diary](https://stuffandnonsense.co.uk/blog/last-week-in-the-studio-cw17-26/)).
- **Default instead.** Look at competitors in the same sector and pick the sector look
  (composers: cinematic photo backgrounds; B2B: product shots; property: skylines).
- **Why, in his words [S].** He says he spends little time on other composers' sites
  and is more interested in what makes the client different; originality comes from
  paying closer attention to what people tell you; templates begin with
  generalisations, he begins with individuals (Begoña companion). For Michael Baugh,
  personality is "the foundation for every design decision", not something sprinkled on
  top.
- **How the conversation goes [S].** Talk moves "far beyond composing" to the people
  who influenced the client, books, films (Baugh). With Tristan they "kept returning" to
  Saul Bass. With Begoña "one detail kept resurfacing". The concept is whatever the
  client keeps coming back to, not what the designer likes.
- **Fit.** Strong for owner-led small businesses, where the owner's own interests or
  the shop's story are available and believable. Weak where the client is an
  institution with no single personality (there he switches to 1.3 or 1.4).

### 1.2 Turn a phrase from the client or their tagline into a literal visual pun

- **What.** Take the client's own words literally and build the hero from them.
- **Where.** Codeboxx: printers that print QR codes + "keeping production lines moving
  is an art" → the Mona Lisa, The Scream and Van Gogh rebuilt from QR-code textures of
  varying density; four became postcards packed in deliveries
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-codeboxx/),
  [CW18-26](https://stuffandnonsense.co.uk/blog/last-week-in-the-studio-cw18-26/)).
  Moonwalk Audio: tagline "Imagine the Sound of Your World" → a world to explore whose
  objects play sound when pressed
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-moonwalk-audio/)).
  Mountain Duck: the product name → "duck machines" that pipe files between cloud and
  desktop ([CW15-26](https://stuffandnonsense.co.uk/blog/last-week-in-the-studio-cw15-26/)).
- **Observed [O].** `codeboxx-1400.png`: the QR Van Gogh in cyan on black fills the left
  half; the headline "The art of keeping production lines moving" sits right. The rest
  of the page is a plain three-column feature row and an FAQ: the concept lives almost
  entirely in the artwork, not the layout.
- **Default instead.** Stock or manufacturer product photos, which he calls dreadful for
  this industry [S]; he replaced them with animated graphics per product category.
- **Fit.** Works for unglamorous trades where the product photo is dull; the pun must
  come from the trade's own mechanics so it reads as insight, not decoration.

### 1.3 Reframe what the business really sells, one level above the product

- **What.** Ask what the customer is actually buying, and design that instead of the
  product.
- **Where [S].** Portico Investment: people "invest in confidence before they invest in
  property", so no photos of buildings at all
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-portico-investment/)).
  Codeboxx: the problem turned out to be trust, not organisation. Verkehrsteiner:
  transport planning is "really about movement"
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-verkehrsteiner/)).
  Academy of Scoring Arts: designing for a community, not a video library; "membership
  organisations rarely sell content. They sell belonging"
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-scoringarts/)).
  Lockrose: their strength is delivering complicated projects, energy is only where
  they built the reputation
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-lockrose/)).
- **His test [S].** For Portico every decision had to pass "Does this make Portico feel
  more trustworthy?"; the question changed from "how do I make this look like a
  property investment site" to "how do we help people feel they're in safe hands".
- **Default instead.** Sector imagery: faded skylines, handshakes over laptops (his own
  description of property sites, [CW29-26](https://stuffandnonsense.co.uk/blog/last-week-in-the-studio-cw29-26/)).
- **Fit.** Any service business. For a Thai clinic, tutor or repair shop the reframe
  (reassurance, progress, "it works again") can pick the imagery when the product
  itself is invisible.

### 1.4 Borrow the visual language of a field that already solved the emotional problem

- **What.** Research outside the client's sector, in a field that achieved the feeling
  the client needs, and translate its qualities (not its surface).
- **Where [S].** Changemakers (Open University, youth politics in Wales): CND, Red Wedge,
  Rock Against Racism, Anti-Nazi League posters, fanzines, gig posters, because they got
  young people to stop and look
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-changemakers/)).
  Lockrose: covers of Graphis nos. 46 and 48 from his shelf
  ([CW27-26](https://stuffandnonsense.co.uk/blog/last-week-in-the-studio-cw27-26/)).
  Portico: Picasso's Cubist faceting, Mondrian, Klee's building shapes (CW29-26).
  Scoring Arts: Erik Nitsche album covers, then Juan Gris, Kandinsky, Miró
  ([banners post](https://stuffandnonsense.co.uk/blog/designing-banners-for-the-academy-of-scoring-arts/)).
  Count Binface: 1930s Flash Gordon serials for video frames, Comicraft comic fonts
  ([imagining post](https://stuffandnonsense.co.uk/blog/election-2024-imagining-what-id-make-if-count-binface-came-calling/)).
- **He says [S].** "I rarely begin by researching websites in the same sector." Saul
  Bass is memorable not for a colour or shape but for confidence, simplicity and economy;
  those qualities, not the look, are what he carried to Tristan's site. Taking
  inspiration from DuckTales "didn't mean copying its artwork" but studying why Mike
  responded to it.
- **Observed [O].** `changemakers-1400.png`: ransom-note logo of mixed cut letters;
  cut-out photos of three young people with thick white sticker outlines on a
  blue-to-magenta textured ground; the headline sits in a black torn-tape banner; the
  issue list is a pile of slightly rotated black label stickers; below, a 3x4 grid of
  issues held together by hand-drawn dashed arrows that loop between cells, with
  magenta brush-script headings. `portico-1400.png`: a faceted De Stijl/Cubist panel of
  ochre, olive, rust and cream fills the right half and bleeds off the top and right
  edges; the same blocks shrink into a horizontal divider bar lower down and into the
  coloured squares that mark steps 1-2-3.
- **Fit.** Very portable: for a Thai noodle shop the field might be Thai cinema posters
  or market signage; for a garage, enamel oil-company signs. The source must carry the
  emotion the client needs, which he states before choosing it.

### 1.5 Build illustration from the client's own logo or existing assets

- **What.** Extend the one asset the client already has into a whole visual system.
- **Where.** Lockrose's triangle → all illustrations constructed from triangles whose
  points intersect on an underlying grid [S] (CW27-26). Moonwalk Audio's tiny
  microphone-headed logo mascot → a full character in several poses at the centre of the
  world [S] (CW42-26). Jas Dosanjh's commissioned book covers → palette sampled from the
  artwork (six colours plus a dark blue base), leaves and embroidery motifs redrawn as
  SVG dividers, the covers' cages turned into a swinging banner where each cage links to
  its book [S] ([portfolio](https://stuffandnonsense.co.uk/portfolio-jas-dosanjh/)).
- **Observed [O].** `lockrose-1400.png`: a single faceted island landscape holding
  pylons, a dam, solar, wind and a nuclear plant in teal, grey and orange; the small
  icons beside "Deliberately lean / Curated capability" reuse the triangle. Layout is
  otherwise conventional (left headline, right illustration, stat row of ">£1bn /
  ≤400kV / End-end" in big numerals).
- **He also rebuilds weak brand kits [S].** Portico's PDF guidelines had black plus three
  green tints and no accent; he darkened and desaturated the darkest green for text,
  lightened the light green into the page background, and added accents for links and
  states; he says pure black and white do not belong in a palette. Lockrose's oranges
  made dirty tints, so he adjusted them. Display serifs too contrasty for body text
  (The Seasons, Orpheus Pro) were swapped for a lower-contrast relative (Calibra,
  Cormorant) so the brand voice holds at small sizes (CW25, CW28-26; Jas portfolio).
- **Fit.** Directly relevant: most small shops have a logo and nothing else.

### 1.6 Make the content a story with a cast, so every page is a scene

- **What.** Write a narrative and a character that runs through the site, so
  illustrations, animation and even interface controls have a reason to exist.
- **Where [S].** Mike Worth: an orangutan archaeologist, Orango Jones, on a quest in
  Borneo for an emerald flute; the home page invites visitors to join, and work, bio,
  news, FAQ and contact are "destinations along the way"
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-mike-worth/)).
  Mountain Duck: the duck as a guide that introduces sections. Moonwalk: the mascot
  stands in the middle of the world.
- **His reasoning [S].** Decorating a conventional portfolio with cartoon graphics would
  feel superficial; the story connected pages that would otherwise feel separate and
  "gave me a reason for every illustration, animation, and interaction". The story must
  never be more important than why people visit: music, credits and contact stay clear.
- **Observed [O].** `mike-worth-1400.png`: Orango bursts toward the viewer out of a
  radial sunburst; comic speech balloons carry the intro copy; the menu button is a
  torn parchment tag; section titles ("REEL", "NEWS", "PROJECTS") are skewed comic
  lettering with a hard drop shadow; news sits on an unrolled scroll; projects are round
  gold-rimmed medallions. Only the audio player is untouched default UI.
- **Fit.** Suits personality-led businesses (a café, a toy shop, a tour guide). Costly:
  it needs real illustration; budget it or skip it.

### 1.7 Skin the interface in the story's materials

- **What.** Ordinary controls become objects from the concept world while keeping their
  usual behaviour.
- **Where [S].** Mike Worth: drop-down navigation as a stone tablet, buttons and social
  icons carved in stone, news on animated scrolls, portfolio images with thick outlines
  and gloss. Begoña: SVG reel-to-reel and cassettes are the audio players; reels turn
  only while her music plays (JavaScript sets a playing state, CSS does the motion)
  ([how-I-designed post](https://stuffandnonsense.co.uk/blog/how-i-designed-an-animated-svg-driven-website-for-composer-begona-pereda/)).
  Cheeky Condiment: the "notify me" dialog is a ketchup-bottle shape that turns from red
  to green when the email is valid
  ([post](https://stuffandnonsense.co.uk/blog/designing-for-the-cheeky-condiment-company/)).
  Moonwalk: objects are monochrome blue until hovered, then full colour, and pressing
  plays a sound — the illustration is the player [S]. Michael Baugh: four orange PLAY
  discs sit on the robot's shoulders and arms [O] (`michael-baugh-1400.png`).
- **His caveat [S].** "Buttons still needed to look clickable"; a generic rounded button
  "would have felt imported from another website", but the established pattern stays.
- **Observed numbered selectors [O].** Begoña's six track buttons are tape-deck keys
  under the reels; Ryan Knaggs's eight track tabs form a bar whose colours step from
  green through blues to black (`ryan-knaggs-1400.png`). A recurring device: the track
  list rendered as hardware.
- **Fit.** Cheap wins for small sites: one or two signature controls (the order button,
  the menu) dressed in the concept are enough.

### 1.8 Type as the hero: stacked, width-fitted names and word lists

- **What.** Display type sized so each line fills the same measure, stacked into a block
  that works as the logo or the main image.
- **Observed [O].** Cheeky Condiment (`cheeky-condiment-1400.png`): a left column of
  "KETCHUP / BROWN / MUSTARD / TABASCO / BBQ / SOY / MAYO", each word scaled to the same
  width, so short words (BBQ, SOY) become huge; the column is the left third, the
  bracelet hero the right two thirds. Tristan Jakob-Hoff (`tristan-jakob-hoff-1400.png`):
  name, "MUSIC FOR TV + FILM / STAGE / VIDEO GAMES" and the nav "LISTEN / ABOUT /
  INTERVIEW / NOTES / CONTACT" all set to one narrow width in a condensed family,
  alternating heavy, light and hairline weights, like Bass title credits. Count Binface
  (`count-binface-2024-1400.png`, Wayback 2 July 2024): "COUNT / BINFACE / FACE"
  stacked in red over a comic smoke cloud, with the bin-helmet silhouette replacing the
  I. Michael Baugh: a client quote set as a wall of condensed caps ("EXCEPTIONAL
  PROFESSIONALISM HIGH ENERGY AND MASTERFUL INTUITIVENESS") filling the right two thirds
  and running past the right edge, with an illustrated hand of jack plugs in the empty
  left third.
  The strongest small-business case is Llanasa Community Council
  (`sb-llanasa-council-live-1400.png`): the 13 village names stacked, each set to the
  column width in gold and orange serif caps under a wreath logo, filling the left half;
  a thin orange vertical rule splits it from the headline and text; at 390 the tower is
  re-set as two justified columns rather than dropped (section 3a).
- **Default instead.** One centred H1 and a subtitle.
- **Fit.** Works in any language with a good display face; for Thai, needs a Thai
  display face with enough weights (an open question for us).

### 1.9 Poster pages: one huge flat field, deliberate emptiness, cut-out portrait

- **Observed [O].** Tristan Jakob-Hoff's home page is a single red sheet inset with a
  cream margin like a printed poster on paper; the stacked type block sits top left in a
  narrow column; most of the sheet is empty red; a black-and-white cut-out portrait
  with a thick torn white outline sits bottom right, with two constructivist bars (one
  white, one black) shooting in from the left. Changemakers and Tristan both use the
  sticker-outlined cut-out photo.
- **Why [S].** Inspired by Saul Bass and modernist layout; he says he built a compound
  layout grid for Tristan's site for "its unique visual rhythm"
  ([portfolio](https://stuffandnonsense.co.uk/portfolio-tristan-jakob-hoff/)). He also
  says he used a compound grid instead of a 12-column grid for Michael Baugh [S].
- **Default instead.** Portrait in a circle next to a bio paragraph.
- **Fit.** Personal brands (a stylist, a chef, a tutor). Needs a portrait with a clean
  silhouette.

### 1.10 The hero illustration is a world that fills the first screen

- **Observed [O].** Moonwalk Audio (`moonwalk-audio-1400.png`): a full-width scene of a
  cardboard castle, a giant Godzilla, a tin robot, pencils and paintbrushes as trees,
  toy soldiers, all drawn in monochrome slate blue with black outlines, and a white
  microphone-headed astronaut in the middle; the logo sits top centre with pill buttons
  for nav fanned symmetrically around it. Begoña (`begona-pereda-1400.png`): a giant
  reel-to-reel deck cropped by the right and top edges, so it reads bigger than the
  screen; five full-height vertical stripes in her palette (green, sage, mustard, near
  black, orange-red) run down the left column like tape or VU colour bars. Lockrose,
  Portico, Mountain Duck: the same right-half illustration hero.
- **Pattern [O].** Below the hero most of these sites settle into ordinary stacked
  sections (three-column text rows, logo walls, card rows, FAQs). The art direction is
  concentrated in the first screen, the signature controls and section headings, not
  spread evenly. That is worth copying: one strong moment plus consistent details, not
  every section reinvented.

### 1.11 Bespoke imagery, never stock; let the concept choose what *not* to show

- **Stated [S].** Portico: no property photos. Lockrose: the team refused photos of
  people, so he went illustration-only. Scoring Arts: replaced the stock "faded image,
  intro text, big ol' button" banner which "20,110,000* others" have. Codeboxx: no
  product shots. Count Binface: original illustrations rather than press photography.
- **Fit.** For small Thai businesses the cheaper equivalent is the owner's own photos
  (Ryan Knaggs's commissioned studio portraits, duotoned blue) or simple flat vector art
  built from a logo shape.

### 1.12 Show early graphics as conversation pieces, expect to lose favourites

- **What.** Make rough concept graphics early, present them as talking points, and use
  the client's reactions to steer.
- **Where [S].** Scoring Arts banners: Nitsche-style piano keys (rejected: too jazz, no
  sense of community) → Gris still life (energy liked, too literal) → Kandinsky → Miró
  (his favourites; client not convinced) → member photos inside shapes joined by lines
  (chosen). Lockrose: photo plus graphics rejected; Graphis-style triangles accepted;
  then the client asked for their London office drawn the same way, which he reads as a
  sign of commitment. Shared Homeland: first concept birds of the region crossing
  borders, replaced by topographic and historical maps
  ([companion](https://stuffandnonsense.co.uk/blog/project-companion-shared-homeland/)).
  Mountain Duck: rejected illustrations and a rejected home page concept are published
  in the case study.
- **He says [S].** Graphics take a long time, so he demonstrates them early to see
  reactions; "every attempt becomes a conversation", which is how he moves past his own
  preferences.
- **Observed result [O].** `scoring-arts-1400.png`: two five-line staves cross and
  re-cross like a waveform, forming three lens shapes holding black-and-white photos of
  composers and sessions, with green notes and dynamics marks running along the lines.

### 1.13 Spec redesign as a pitch

- **Where [S].** During the 2024 UK election he published an unsolicited redesign of
  Count Binface's Squarespace site (new illustration, primary palette, Wildwords comic
  font, Flash Gordon video frames, cleaned-up nav). Days later the candidate hired him;
  he built it in under a week by injecting SVG and CSS into Squarespace
  ([imagining](https://stuffandnonsense.co.uk/blog/election-2024-imagining-what-id-make-if-count-binface-came-calling/),
  [designing](https://stuffandnonsense.co.uk/blog/designing-for-count-binface/)).
- **Detail [S].** He noted the old site used Proxima Nova, the same face as the
  Conservatives, the Count's arch-nemesis: a type choice criticised for its story, not
  its looks.
- **Fit.** Directly relevant to AppBaoBao's sales: a free one-page concept for a named
  shop, made from their own story, is his proven door-opener.

### 1.14 Ambient motion and Easter eggs, kept light

- **Stated [S].** Lamps flicker, scrolls unroll, turbines turn, the nuclear plant glows;
  ambient animations "add atmosphere without demanding attention". He nearly always
  hides an Easter egg (Mountain Duck, Lockrose). Michael Baugh's colours shift lighter
  in the morning and darker in the evening. All SVG with static and moving layers
  separated; his cassette and reel-to-reel graphics are under 12 KB each.
- **Fit.** One ambient loop in the hero is enough for a small-business site; keep it
  small for Thai mobile networks.

### 1.15 Mobile: keep the motif, shrink or reorder it, drop the ornaments

Observed in the 390 shots [O]:

- Begoña (`begona-pereda-390.png`): the full-height palette stripes become a short colour
  bar above the nav; the name block stays large; the reel-to-reel still bleeds off the
  right edge, so the scale gesture survives.
- Tristan (`tristan-jakob-hoff-390.png`): order flips: the cut-out portrait comes first,
  then the name stacked full width, then a giant "LISTEN"; the empty red field is gone;
  the vertical-stripe (piano key) motif closes the page.
- Cheeky Condiment (`cheeky-condiment-390.png`): the width-fitted condiment word column
  is dropped; the bracelet hero stays; product rows of bottles shrink but keep the
  "shelf of products" idea.
- Changemakers (`changemakers-390.png`): photo strip and torn banner first, sticker tags
  centred in a loose pile; the looping dashed arrows are dropped.
- Michael Baugh (`michael-baugh-390.png`): the robot is cropped tighter and the PLAY
  discs on its body disappear (a normal player remains); the condensed quote wall stays
  as the dominant type moment.
- Mike Worth (`mike-worth-390.png`): skewed comic name, sunburst character and parchment
  button all survive; speech balloon becomes a full-width box.

Rule of thumb from these: the concept's one signature element (reel, bracelet, character,
stacked type) always survives at 390; secondary ornaments (arrows, word columns, extra
interactions) are cut.

## 2. Process and thinking (recent work, 2024–2026)

From his project companions and the weekly "Last week in the studio" diary
(CW15–CW45 2026), all [S] unless marked:

1. **Kick-off conversation about the business and the person.** He asks what they want
   the site to achieve, then lets the talk wander into interests and influences. He has
   written a 35-page "Hardboiled Client Interview Guide" (bundled with *Standout Designs
   for the Web*, Nov 2026); I have not read it.
2. **Content before visuals.** Content audit, reorganise and rewrite copy, then
   low-fidelity wireframes he calls storyboards: what someone should discover, in what
   order (Mike Worth, Codeboxx, Lockrose). For Lockrose he wrote initial copy so the team
   could hear the proposed voice.
3. **Type early.** "I always start with type." He shortlists faces and asks the client
   how each one *feels* (formal or informal, approachable but professional), not which
   they prefer; choosing is his job. Type sheets use real or self-written copy, never
   lorem ipsum; he checks the client's name in each face, numerals, both cases, and
   accented characters for the client's language (Begoña, Spanish). For Moonwalk he
   looked for round, moon-shaped Os.
4. **Palette as a system with roles**, often rebuilt from a weak brand kit (1.5). He
   builds an HTML/CSS style guide early instead of relying on PDF guidelines, which he
   calls relics written for print.
5. **Sketch on paper, then vector, then animate.** Pencil sketches → flat colour blocks
   with few points → details → SVG export with moving parts separated.
6. **Show graphics early as talking points** (1.12).
7. **Design in the browser.** He codes before the design is final because code sparks
   ideas; he spends days testing interactions: "If it doesn't feel right in the
   browser, it isn't right". He hands developers a working Eleventy prototype instead of
   Figma or PDFs, even when the final build is WordPress (Portico, Verkehrsteiner,
   Aurus). His own starter kit lets him finish build work fast and spend the budget on
   content and illustration.
8. **Extend to print and merch** when the system is strong: Codeboxx postcards in
   deliveries, Mike Worth pins, caps, mugs and T-shirts, a square business card for Ryan
   Knaggs.
9. **Use of AI [S].** He uses generative tools as a scrapbook and corrector (perspective,
   poses, badge bevels) while he directs; not for writing or for inventing the idea.

## 3. Taste

- Mid-century modernism and print: Saul Bass, Erik Nitsche, Graphis covers, Richard
  Hollis (via Block Berthold), Cubism, De Stijl, Klee, Kandinsky, Miró [S].
- Cartoons and comics: '90s Disney TV (DuckTales), 1930s SF serials, Comicraft fonts,
  his own Toon Titles side project; Godzilla figures, which he slipped into Moonwalk
  [S].
- Flat colour, strong outlines, little or no shading, limited palettes; desaturated
  accents; no pure black or white [S][O].
- Condensed and characterful display faces paired with a plain readable text face (Fido
  + Archivo Condensed; Cormorant + P22 Underground; Wildwords; Block Berthold) [S].
- Dislikes [S]: sites that "could belong to almost anyone"; framework sameness (hero,
  feature grid, floating cards, gradients, anonymous illustration); stock banners;
  "horribly generic" Lato and ubiquitous Poppins; brand PDFs without systems; animation
  for its own sake.
- Likes clients who bring their own ideas once a direction lands [S]; enjoys
  unglamorous briefs: "there are stories to tell about every business; you just have to
  find and tell them" (CW17-26).

## 3a. Small and local business clients (2022–2026)

These portfolio pages now carry only a title and gallery; the write-ups below come from
Wayback captures (2023–2025) of the earlier versions, read by a helper agent, plus its
screenshots `sb-<client>-live-{1400,390}.png` and gallery images in
`shots/clients/gallery/`. Raw text: `raw/clients/sb-wb-*.txt`, `sb-blog-*emma*.txt`.
I re-checked the Llanasa and Abergele screenshots myself and agree; the other markers
are the helper's.

- **Abergele Dental** (family practice, North Wales, 2 weeks). Brief [S]: the dentist
  found competitors' sites "generic and template-based" and wanted his family-first
  approach shown. Clarke interviewed him, rewrote the copy in a friendly voice, drew the
  family. [O]: hero cartoon of the dentist's family and their striped cat before a gold
  heart; logo is a toothpaste tube labelled with the surname squeezing out his name in
  brush script; "Love your smile" set rotated about −15° over the drawing; palette only
  charcoal, slate, gold; a narrow right rail holds what patients need (hours, the phone
  number set as display type, a quote, treatments); a signature by the contact line; a
  palette switcher in the footer. At 390 the illustration and rotated type stay, the
  rail drops below. Client testimonial calls him "a researcher, an artist, and a
  storyteller" [R].
- **Black Mountain Honey** (bees, queens, honey; with Paul Boag on strategy). [O]: the
  mark is one line drawing where a mountain range's base becomes a bee's wing with a
  striped abdomen, so place and product fuse, and it still reads as a favicon. Honey
  orange on near-black brown, heavy wide capitals, the owner-beekeeper cut out over
  orange-toned bee macros, hero bands ending in a soft scooped edge. New page design
  routes by intent ("What brings you here?": start an apiary / need a queen / just want
  honey), a seasonal "Queen season starts in April" block, pun copy ("The Buzz Blog").
  The grid is conventional; the character is in the identity, the owner's face and the
  copy. Live site is Wix with his identity applied; he keeps a standalone style guide
  site to carry the identity to WordPress [S].
- **NWPS Construction** (builder bidding for council and housing-association work).
  Concept [S]: "Building Confidence"; the verb repeats in every heading (building
  trust, partnerships, communities); lead with how they work, not a service list. Slab
  serif, compound grid, orange continuous-line illustrations "to avoid cliches",
  photographs only for finished work [S]. [O]: an orange bracket over "NWPS" like a
  lintel; two text columns split by orange rules with a drop cap; a giant "25 yrs"
  numeral in a rail; a full-height orange strip at the right edge with phone and email
  set vertically (lost at 390).
- **Dementia Care Solutions** (home-care start-up). [S]: founder began it after his
  mother-in-law lived with dementia; sector identities generic; after dozens of sketches,
  a tree (stability) with heart-shaped leaves (care), soft colours, compound grid. [O]:
  serif headline "The next best thing to family" with a handwritten subline; tree bleeds
  off the right edge; a cut-out photo of carer and resident breaks into the next band.
- **Llanasa Community Council** (13 villages, 2 weeks, no write-up). [O]: the place names
  are the identity: a justified tower of the 13 village names, each set to full column
  width (short SARN huge, long FFYNNONGROYW small), gold and orange on black, crowned by
  a wreath of local foliage that is the logo; footer roundel packs the names into a
  circle; "Next meeting 19:15 Tuesday" set like a poster; English/Cymraeg switch. At 390
  the tower is re-set as two justified columns of names, still a type block: the best
  mobile re-composition found in this stream.
- **Emma Bodger** (film/TV director). [S]: her work is "multi-dimensional", so red/cyan
  anaglyph: SVG filters turn every still into a matching duotone with an optional 3D
  offset and a 3D-glasses toggle. Unused concepts he published: a word-search of her
  credits; colons around "EMMA:" as film sprocket holes (the colon survived in the
  logo). Her aside "I'm not comparing myself to Hitchcock…" became a hidden Vertigo/
  Psycho theme triggered from a faint silhouette in the footer.
- **Alessandro Mastroianni** (game sound designer). [S]: "obsessive level of detail",
  Italian heritage → Giovanni Pintori palette and an Italian display face. [O]: one
  symmetrical rainbow contour-line illustration per category; play buttons on stems like
  microphones; the face swaps every S for a slash.
- **Sabina Baugh** (piano tutor) and **Reuven Herman** (LA composer): restrained, no
  write-up; Reuven's bio lines run along the curve of a grand-piano lid [O].
- **Neurodiverse Training**: his collage of watercolour portraits has since been
  replaced on Odoo by the textbook AI default (centred hero, one gradient word, logo
  strip, equal cards) [O]. The clearest before-and-after: without the bespoke concept
  assets, the site falls straight back to the default.

Patterns the helper drew across these [I, agreed by me]: the name or trade object becomes
the mark (tube, mountain-bee, lintel, sprocket colons, village wreath); illustration
replaces stock in a style fitted to each client; two or three colours, often on a dark
ground, with photos duotoned into it; type as image (rotated slogans, name towers, phone
numbers as display type, giant numerals); an asymmetric main column plus a narrow
utility rail (hours, phone, services) instead of equal three-card rows; small visitor
toys (palette switchers, hidden themes, language switch); jobs of two weeks to a month.

## 3b. Older client work (2004–2018)

From his blog write-ups (raw text in `raw/clients/blog-*.txt`) and design images he
published, saved in `shots/clients/blogimg/`, read by a helper agent. Wayback
screenshots of these sites mostly failed (missing 2005 CSS, refused connections); see
open questions. [S] = stated by him.

- **Dig Business** (NY consultancy, 2005). The client's business card, an orange card
  sliding from a cream sleeve, was the "irresistible early inspiration" [S]; it set the
  palette and became a full-height orange column with the card's curved thumb-cut
  (`blogimg/dig-3.jpg`). The client chose a cleaner, more open version; card ideas
  "crept back in" later [S]. He published all seven comps.
- **Woodland Trust Christmas shop** (2005). Made to work with the print catalogue so
  visitors "feel at home" [S]; catalogue picture-navigation became a 3x2 tile grid; a
  robin cut from a photo breaks out of the masthead and looks toward the logo [O]
  (whether the gaze was intended is unconfirmed).
- **Karova** (e-commerce framework, 2005). Logo dots → colour codes for each column; a
  hand-annotated iteration sheet (`blogimg/karovasite-02.jpg`) shows content "fingers"
  overlapping the header and an abandoned 15°-rotated layout that he reused as the
  sign-up form [S]. Dropped the old stock-photo model.
- **New Internationalist** (2009). Studied every masthead since 1973; revived the
  magazine's old habit of changing wordmark colour per issue as a per-section colour
  [S]; halftone texture for print heritage; story summaries sized by importance, as in
  newspapers and comic panels [S]; current articles in a narrow single column, older ones
  in a conventional two-column template with context [S]; designed in public with
  working HTML prototypes; content pages first, home page last; order of work
  structure → type → colour → sparing graphics [S].
- **CannyBill** (invoicing software, 2009–10). Public redesign; background texture made
  of over a thousand copies of the logo symbol [S]; palette from two old brand colours;
  competitor research only to find conventions and clichés to avoid [S]; day-one black
  and white on a visible grid; copywriter found the voice from the product name [R].
- **ISO** (2011–12): grid from the proportions of the ISO logo [S]; four week-long
  browser sprints with templates tested on real content weekly [S].
- **Hillsborough Independent Panel** (2012): weeks of research including families'
  interviews; deliberate restraint driven by empathy; expressiveness scales with the
  subject [S][O].
- **Equfund** (2018): 6+4 overlapping compound grid after Karl Gerstner's *Capital*
  grid, six layout variants; commissioned illustrations of figures stepping out of
  panels; giant "1 IN 20" numeral; slightly rotated photos; layouts named after
  Liverpool FC players as a joke [S][O].
- **Old portfolio lists** (Wayback 2005, 2008, 2012): British Heart Foundation, Disney
  Store, WWF UK, Empire Hotel, Osborne House, Status Mortgages; Solihull Council, whose
  brief said "We do not want it to look like a council site", answered with an
  asymmetric two-wide-column grid instead of the council three-column norm [S];
  Ceredigion information service with illustrator Holly Lloyd, using photos of
  Aberaeron's painted houses turned into line backgrounds coloured as day or night [S];
  a 2008 positioning line "Small business, not small ideas" [S]; ~130 names in 2012
  including many North Wales small businesses (hotels, caravan parks, a timber merchant,
  a fireplace maker).
- **Process then** [S]: a 2004 four-stage sign-off sheet (concepts, templates,
  functionality, launch; each stage approved or a definitive change list); from 2008 he
  stopped showing static visuals and had clients approve working pages; when a client
  wants an alternative he builds it, says which he prefers and why, and leaves the call
  to them.

Continuity across 20 years [I]: the concept still comes from something the client
already owns (card, catalogue, logo, masthead history, town), competitors are studied to
avoid them, rejected ideas get reused, and approval happens on working pages.

## 4. Open questions

- Jas Dosanjh's site: `jasdosanjh.com` currently shows a hosting placeholder, so I
  could not screenshot it; the analysis rests on his portfolio text only.
- Portico: the URL in his portfolio (`portico-investment.netlify.app`) is dead; the
  prototype lives at `porticoinvestment.netlify.app` (from his CW30-26 diary). The live
  WordPress build by another team may differ.
- Verkehrsteiner's hero rendered as an empty dark field above the circle grid in
  headless Chrome; it is probably an animation that had not started. Not verified.
- Most "project companion" posts carry the date of his 2026 portfolio rewrite, not the
  project date, so project years are approximate.
- Several companion posts reuse an opening paragraph from another post (Scoring Arts and
  Shared Homeland start with Codeboxx's "People don't buy products from companies they
  don't trust"), so treat those openings as template text, not project-specific.
- Count Binface 390 view: Wayback refuses framing, so no small-screen capture.
- Older sites (New Internationalist, CannyBill, ISO, Woodland Trust, Dig, Karova) could
  not be seen styled as launched; Wayback lacks 2005 CSS or refused connections. The
  analysis rests on the design images in his own posts (`shots/clients/blogimg/`).
- Ceredigion: his 2008 pages disagree on the source (60s music and fashion vs Pink
  Panther cartoons).
- Black Mountain Honey and Llanasa have no write-up anywhere; their concepts are read
  from the work, not stated by him. Sabina Baugh and Reuven Herman have no 390 capture
  (they refuse framing).
- Not read: his paid book *Standout Designs for the Web* and the Client Interview Guide
  bundled with it, which likely state his concept-finding method directly.
