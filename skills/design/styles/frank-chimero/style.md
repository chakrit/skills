# Frank Chimero

Work the way he does: settle why the page exists, then its limits, then the phone stack,
and only then the wide screen. The page is plain material handled closely: one text
size, a typewriter voice, a still half and a scrolling half, a lot of empty field, one
hand-made image at a time, one hue and one accent. Detail, sources and the pages each
number comes from are in `synthesis.md` and `notes/`.

## 1. Before any layout

1. Write down the objectives by asking Why: what is this page for, what are we building
   it for. Then put them aside while you sketch, so they do not kill the early ideas;
   bring them back to steer.
2. Name the one or two things that are uniquely true about this business, and the one
   thing this page must do. Spend the time here.
3. Find the one piece of content that will carry the page: "a great photo, memorable
   illustration, or pitch-perfect sentence does most of the work." Put your effort into
   the content before the looks.
4. Set your limits now, in three groups: content, structure, tone. Saying no before you
   start lets you say yes while working.
5. Decide what medium the content belongs to and take that medium's conventions whole.
   A book takes book setting: a serif reading face, paragraphs indented 1.5em after the
   first with no space between them, hyphenation, chapter openers, a paper texture.
   Personal writing takes the typewriter: a monospace for every word. Choose a typeface
   this project has not been given before; he does not repeat faces across projects.

## 2. Phone first

Start at phone width. The page is one stack, and the order of that stack is the
hierarchy: decide it here, and let the wider layout inherit it. Sketch arrangements of
elements first, then draw the frame around them. Decide what the page looks like empty
and what it looks like full.

On the phone:

- Keep every text size the same as on desktop.
- Keep the navigation on the page as a stacked list. No menu button.
- The held-still half (section 3) becomes a band at the top holding the name and the
  full navigation, or, when it holds an image, a screen of its own before the text.
- Images take the text column's width.

## 3. The wide screen

**Cut the screen in two at the centre and hold one half still.** At 1440 px each half is
720 px. The left half carries the name and navigation, or one small image on an
otherwise empty field, and stays fixed at full viewport height (sticky or fixed). The
right half holds the content and scrolls in its own box (`overflow-y: scroll`, height
100dvh), padded calc(3vw + 1rem), with a text column of at most 36rem (504 px) centred
in it. On a page that has nothing to read, such as a home page, leave the right half
empty. He built a side column for navigation because his site had many pages and he
did not want navigation hidden, knowing it looks "very, very reminiscent of 90's
frames".

**Leave a large field empty, and measure it.** Half the screen (720×891 on a home page);
or 40–45% of the first screen between the header and the first item; or the top
two-thirds of the screen with the one sentence placed low and left of centre; or a
650×891 panel holding a drawing of about 140×190. Above and below a centred title, leave
about 84 px.

**Put navigation on a column line as a short vertical list.** Two to six links, one per
line, starting at a column edge of the grid (in a `1fr 1fr` header, the second column at
x=360; on a 12-column grid with 14 px gaps and 28 px outer padding, column 7; or the
page's centre line). Never right-aligned in a bar. "Let's just put seven words up on
the screen for you to tap on."

## 4. Type

**Set every word at one size.** Make hierarchy with weight and colour only: a title is
the body size, set bold or in the accent; a secondary line is the body size in a dimmer
tint of the text colour. For the book he gave the reason: with all the type the same
size, the text "retains its hierarchy, regardless of the user's settings."

- Typewriter setting: monospace (Courier) 13 px / 19.5 px for navigation and short text,
  14 px / 21 px for reading; reading column 504 px, about 57–60 characters a line, left
  aligned, ragged right. The title of a piece: 14 px bold, centred, its date under it in
  the dim tint, with about 84 px of space above and below the pair.
- Book setting: a serif at 20 px / 27 px, measure 30em (about 64 characters), the chapter
  title the same 20 px in the accent colour; a monospace at 14 px / 24 px for labels,
  quotes, the next-chapter link and the footer.

**Use a monospace as the working voice.** Navigation, labels, dates, numbers and the
footer are set in it; on a page of personal writing, everything is.

**Write labels as two lines at one size:** the name, and under it, on its own line, a
descriptor or date in the dim tint ("Studio Frank" over "My design practice"; "Chapter
One" over "How and Why"). No icons, no size change.

**Turn on oldstyle proportional numerals** (`font-variant-numeric: oldstyle-nums
proportional-nums`), tabular for a column of years, and kerning.

## 5. Colour

Build the palette from one hue family for both the field and the text, plus a single
accent used only for links, hover or one element. Pick a new ground for each project.
His palettes have this shape:

| Field                        | Text          | Dim tint           | Accent                 |
|------------------------------|---------------|--------------------|------------------------|
| dark grey-green #3d4340      | #eeeeee       | #717d78            | green #5e786d on hover |
| light #eeeeee (reading half) | #2f3432       | #828b87            | green #5e786d on hover |
| cream #F9F7EA                | olive #515F44 | pale green #A5AF9B | none                   |
| grey #dfdfdf, paper texture  | #333333       | none recorded      | rust #b95b23           |
| black #000000                | white         | 40% white          | none                   |

On the split screen the two halves take two values of the same family: the still half
dark, the reading half light. Underline links in the dim tint.

## 6. Images

Use hand-made or found images, one at a time: a single-weight line drawing in the text
colour; a hand-lettered logotype; old black-and-white or sepia photographs from public
archives, collaged with torn paper edges, flat geometric shapes (semicircles, arches,
rings), thin hand-drawn lines and one ochre or rust accent on a warm grey paper ground;
a small black engraving-style drawing alone in a large empty panel; a product (such as
a book cover) shot as an object with soft stacked shadows. Flat vector alone "Looks
computerish… We need to get some hands in to this."

Place one image per row at the text column's width (504 px; square for collages), 56 px
above and below, corners 2 px, with no caption or a centred 13 px caption (against
14 px text) in the dim tint. Never a grid of thumbnails, never stock photographs or
screenshots in cards.

## 7. Motion

Links and buttons change colour or opacity in 0.2–0.3 s on hover (a title fading to the
dim tint, a link turning to the accent); a whole-page change fades out in 500 ms and in
in 300 ms; a "next" arrow may slide 1rem right on hover in 0.2 s. Nothing reveals,
slides in or moves on scroll; no parallax, no custom cursor. He
wants "no razzle-dazzle" and dislikes fancy animations and transitions on the web.

## 8. Edit

Show the work early and unfinished, stay open to new ideas until about two-thirds of the
way through, then edit hard: "If it isn't spectacular, it gets cut." Do not make a thing
look special; "Special things demand attention for the wrong reasons." Do not reach for
minimalism without cause, and do not pick Helvetica or Times as the plain choice.
