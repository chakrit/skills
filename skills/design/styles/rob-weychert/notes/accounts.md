# Accounts: what other people say about Rob Weychert's design

Stream: `accounts`. Raw records are in `/tmp/designers/rob-weychert/raw/accounts/`, one
file per source with its URL on the first line (HTML working copies in `html/`). All
pages were fetched with curl and read as full text; the two podcast transcripts are
machine-made (they render Sleight as "Slate" and Harmonix as "Harmonic"), so quotes from
them are close but not exact. No visual judgement here rests on seeing the work: this
stream is entirely second-hand, and the browser was not used.

Public writing about Weychert by others is thin. Most of what exists comes from his
ProPublica design director, David Sleight, and from Andy Clarke's 2018 podcast. Most of
the Clarke episode is Weychert's own words, so it overlaps the `talks` stream; it is used
here for what Clarke and Sleight say, and for Weychert's statements as Clarke relays them.

Claim markers: **[reported]** someone else describes it; **[stated, via X]** his own
words as relayed or quoted by someone else; **[observed]** seen in the work.

## Sources

| Source                                                                                                                                                                                                                                                          | Date       | What it gives                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------------------------|
| [Andy Clarke, Unfinished Business S3E7, with Weychert](https://stuffandnonsense.co.uk/blog/unfinished-business-art-directing-for-the-web-with-rob-weychert/) ([transcript](https://stuffandnonsense.co.uk/content/transcripts/UBPS3E7-rob%20weychert.pdf))      | 2018-06-10 | Clarke's reading of the Lost Mothers grid; Weychert on process, systems, simplicity |
| [Andy Clarke, Unfinished Business S3E5, with David Sleight](https://stuffandnonsense.co.uk/blog/unfinished-business-art-directing-for-the-web-with-david-sleight/) ([transcript](https://stuffandnonsense.co.uk/content/transcripts/UBPS3E5-david-sleight.pdf)) | 2018       | His design director: designers code, sketch-to-code speed, two-voice story          |
| [Erin Kissane and David Sleight, Source (OpenNews)](https://source.opennews.org/articles/new-propublica-site/)                                                                                                                                                  | 2017-08-31 | 2017 ProPublica site launch; credits him with the grid tool and type scale          |
| [ProPublica, hire announcement](https://www.propublica.org/atpropublica/rob-weychert-to-join-propublica-as-editorial-experience-designer)                                                                                                                       | 2015-11-12 | Role defined; Sleight on his "nuance, intelligence and insight"                     |
| [ProPublica, Murrow Award release](https://www.propublica.org/atpropublica/propublica-wins-edward-r-murrow-award-for-excellence-in-innovation-1)                                                                                                                | 2018-06-21 | Lost Mothers gallery credited to him; award for innovation                          |
| [ProPublica, SND Best of Digital Design](https://www.propublica.org/atpropublica/propublica-wins-35-society-for-news-design-awards-of-excellence)                                                                                                               | 2018-02-13 | Award of Excellence for his individual portfolio; site redesign recognised          |
| [ProPublica, 2017 year in visual storytelling](https://features.propublica.org/2017-year-in-review/visual-storytelling-interactive-data-journalism/)                                                                                                            | 2017-12    | Lost Mothers "interactive gallery" credit                                           |
| [ProPublica, 2016 year in visual storytelling](https://www.propublica.org/article/2016-propublica-visual-interactive-storytelling)                                                                                                                              | 2016-12    | He animated a story on Amazon's pricing algorithm                                   |
| [Fonts In Use, "An Unbelievable Story of Rape"](https://fontsinuse.com/uses/11297/an-unbelievable-story-of-rape)                                                                                                                                                | 2015-12-17 | Stephen Coles's entry: faces, credits, two editions                                 |
| [Fonts In Use, "Devils, Deals and the DEA"](https://fontsinuse.com/uses/11299/devils-deals-and-the-dea)                                                                                                                                                         | 2015-12-17 | Faces of a ProPublica feature he is credited on                                     |
| [Zeldman, "Weychert lives"](https://zeldman.com/daily/0305f.shtml)                                                                                                                                                                                              | 2005-03-29 | Announces the 2005 site relaunch: columns and haiku                                 |
| [Zeldman, An Event Apart Philadelphia](https://zeldman.com/daily/1205b.shtml)                                                                                                                                                                                   | 2005-12    | Social only: thanks him for ground support                                          |
| [An Event Apart 2009 speaker bio](https://aea09.complexspiral.com/speakers/robweychert/)                                                                                                                                                                        | 2009       | Organiser's framing: meticulous detail, print training, humour, clients             |

## 1. Moves

### Let the empty space carry the finding

- **What.** A data display built so that what is missing is the story: a field of slots
  for every case, most of them left empty, with the few known cases filled in and
  clickable.
- **Where.** ProPublica's "Lost Mothers" gallery (2017), on maternal deaths in the US.
  An estimated 700 to 900 women died in 2016; reporters could identify about 130. He
  built a grid of roughly 800 slots so readers see "how few we were actually able to
  flush out", with about 15 deeper vignettes behind it [stated, via Clarke 2018]. "The
  vast majority of it is empty and that sort of the point" [stated, via Clarke]. Clarke
  read it as "telling a story within a story": scope and scarcity at a glance [reported,
  Clarke]. ProPublica credits the gallery to him; it won a Murrow Award for innovation
  [reported, ProPublica 2017 and 2018].
- **Default it replaces.** A gallery of portraits. The first brief was a page of faces;
  Sleight pushed back that nobody would want to look through a page full of unfamiliar
  faces [stated, via Clarke, relaying Sleight's objection]. The records were also uneven
  (some photos, some only an obituary), which a portrait grid would expose badly
  [stated, via Clarke].
- **Why.** Not to shock, but to show "how little is really known" [stated, via Clarke].
- **Source of the form.** The dot-grid floor of the elevator in ProPublica's building:
  "Oh! That could be an interface" [stated, via Clarke].
- **When it fits.** Incomplete datasets where the gap is itself the news.

### House type scale and a grid you define, not a framework you fill

- **What.** A shared typographic scale and a custom grid helper as the base of a news
  site, so new features inherit proportion instead of being sized ad hoc.
- **Where.** ProPublica's 2017 site. Sleight gives "all credit" for the site's
  readability to Weychert, who built "a grid helper tool in SASS and a typographic
  scale"; the scale means "you don't have to make lots of ad-hoc decisions" and gives
  "harmony between the pieces" [reported, Sleight in Source 2017]. The grid tool became
  Column Setter: he says it does not touch the HTML (no "six col" classes) and is not a
  fixed grid like 960 to "shoehorn your stuff into"; you set the grid's parameters to
  what the layout needs [stated, via Clarke]. The site redesign and his individual
  portfolio won Society for News Design Awards of Excellence in 2018 [reported,
  ProPublica].
- **Default it replaces.** Bootstrap-style class grids and generic design systems, which
  he calls outsourcing the work to someone who does not know the problem [stated, via
  Clarke].
- **When it fits.** Any multi-page site: fix the proportions once, keep layouts free.

### Long reading first: places to breathe, pause and resume

- **What.** For a newsroom whose pieces often run past 5,000 words, the article page is
  the product: producers move blocks inside the article to add editorial art, signposts,
  and "places where things can breathe, where you pause and resume" [reported, Sleight in
  Source 2017; the block system is credited to the team, the readability to Weychert].
- **Detail.** He wants line length and other typographic principles to survive fluid
  layouts, and checks how a piece reads in RSS or a read-later app [stated, via Clarke].

### Two voices, two image languages (a team move he worked on)

- **What.** One story told from two reporters' sides, each side art directed in its own
  visual language: the victim's side in figurative illustration, the police side in
  evidentiary photography.
- **Where.** "An Unbelievable Story of Rape" (2015), co-published by ProPublica and The
  Marshall Project, each site with a slightly different layout [reported, Fonts In Use].
  Sleight names "me and Rob on our side" and calls it his textbook case of art direction
  setting the editorial structure [reported, Sleight via Clarke]. The idea is Sleight's
  by his own account; Weychert's part is not described.
- **Type.** Fonts In Use lists Acumin, FF Tisa, Miller and Utopia across the two
  editions; another ProPublica feature credited to him, "Devils, Deals and the DEA", pairs
  JAF Bernina Sans with FF Tisa [reported, Fonts In Use 2015]. Which faces belong to which
  edition is not stated. These are his only two Fonts In Use credits.
- **Default it replaces.** Merging two drafts into one voice and one look.

### The thing itself, unadorned

- **What.** Distil to content: "Here's the stuff. Here's the imagery. Here are the colors
  and the shapes and the type", rather than interactivity that is "superficially forward
  thinking" [stated, via Clarke]. He worries this costs him chances, and wants a balance
  between experiments and a "base layer" of the thing unadorned [stated, via Clarke].
- **For an agent.** Add an interactive or decorative layer only when the story needs it.

### Humour as part of the work

- Organisers and peers foreground his humour: Virtual Stan (a "viral phenomenon"), the
  air-guitar alter ego Windhammer, and a 2005 site with dictionary-based daily haiku
  [reported, An Event Apart bio 2009; Zeldman 2005; Clarke 2018]. Zeldman greeted the 2005
  relaunch with "Let columns multipy" [sic] [reported]. No account says how humour shows
  in the visual design itself.

### Motion (thin)

- ProPublica's 2016 review says he "had a little fun animating" its reporting on
  Amazon's pricing algorithm [reported]. Nothing was found from others on his Beyond
  Tellerrand title sequences or other CSS animation.

## 2. Process and thinking

- **Convention first, then make it specific.** Start with the problem; apply the most
  conventional solution; ask where that convention falls short; add or subtract until the
  design answers "the very specific problem to be solved as opposed to the category of
  problem". For an article: flow the text into a standard layout, read it, then ask "How
  might I hear it better?" [stated, via Clarke].
- **Specificity over sameness.** His complaint is not that everything looks alike but
  that people do not work out what makes their project unique [stated, via Clarke].
- **Sketch, then code, fast.** Sleight told Clarke he moves very quickly from sketches
  into code [reported, via Clarke]; Sleight says the whole team goes from sketching to
  code pretty quickly, and Weychert, a "brilliant ... CSS web standards coder", implements
  his own layouts [reported, Sleight]. Weychert calls diving into code too early a bad
  habit he is working on; he rarely makes high-fidelity mockups and seeks a middle ground
  between wireframe and finished code [stated, via Clarke].
- **Reporters as clients.** For Lost Mothers: initial concepts, benefits and drawbacks
  talked through, a few wireframe-level options, then a prototype built up; the concept
  settled in about a week [stated, via Clarke].
- **Type tools.** Type is "so core to what I do" that Sketch's handling of type kept him
  in Illustrator and Photoshop [stated, via Clarke].
- **Visual thinking.** Associations most people would not make, drawn from outside the
  discipline: the city, the commute, nature, art [stated, via Clarke].
- **Editorial means more than one mind.** Editorial design is where several people's
  expertise shapes how a story is told; he likes designers' case studies best when an
  editor helped distil them [stated, via Clarke].
- **Team structure.** Sleight keeps each designer on two of three tracks (daily
  production and art commissioning, big features, the site itself) and rotates them
  [reported, Sleight via Clarke].
- **Small screens.** Designers still fetishise big-screen layouts; storytelling on a
  phone, still "tall stacked thin", is the unsolved problem [stated, via Clarke].
- **Art direction redefined.** As the web caught up with print, art direction must give
  up control and self-expression and accommodate readers who may not even see the design
  [stated, via Clarke].
- **Character.** Sleight, hiring him: "a level of nuance, intelligence and insight to
  editorial design that few can claim" [reported, ProPublica 2015]. The 2009 An Event
  Apart bio: "neurotically meticulous attention to detail", and print training adapted
  to standards-based web design [reported].

## 3. Taste

- **Editorial and print roots.** Print-trained; wanted to work for magazines after
  school; inspired early by David Carson [stated, via Clarke]. Organisers frame him as
  applying classic graphic design principles to the web [reported, AEA 2009].
- **Dislikes.** Committee design that serves stakeholders, not readers; the
  Bootstrap-mannered web; generic frameworks; "bells and whistles" [stated, via Clarke].
- **Values.** Simplicity, specificity, the open web, and reading on the reader's terms
  [stated, via Clarke]; ProPublica called him "an outspoken advocate for user-centered
  design and the open web" [reported, 2015].
- **Faces credited on his ProPublica work:** Acumin, FF Tisa, Miller, Utopia, JAF Bernina
  Sans [reported, Fonts In Use]; shared credits, so not proof of his own choice.

## 4. Open questions

- No account by others of the Beyond Tellerrand title sequences: the festival blog has
  posts on other years' titles (Berlin 2023, Berlin 2025, Düsseldorf 2024) but none for
  his Berlin 2022 or 2024 work.
- No review or write-up of plus=equals by anyone else turned up.
- No CSS-Tricks, Codrops or Smashing coverage of his work, and no Typewolf or SiteInspire
  entries, were found.
- Wayback could not be reached from this environment (curl got no connection; the fetch
  tool refuses web.archive.org). His 2005 Web Standards Award and the gallery listings
  his old About page claims (CSS Vault, Stylegala, Unmatched Style) are unverified.
- No Happy Cog colleague (Zeldman, Santa Maria, Hoy) writing about his Happy Cog projects
  was found; Zeldman's mentions are social. The AEA bio lists Comhaltas Ceoltóirí Éireann
  as his client, but no account says what he did on it.
- No Nieman Lab, Poynter or press coverage of The Markup work names him.
- Lost Mothers numbers differ between sources (about 130 identified per Weychert, 134 on
  the page per Clarke, more than 160 per ProPublica's later release); the page was being
  updated.
