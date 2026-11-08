# Build the frame

## 1. Reuse the Astro starter

Use Astro. Inspect existing preview capabilities before creating files. In an Astro
project, install the frame in its normal source tree. Otherwise use an isolated Astro
workspace inside the repository, such as `study/<study-name>/preview/`, with the
project's package manager. Keep the production application's framework unchanged.

The frame's construction is prescribed below; do not ask the user to design its chrome.
Keep study questions for the option set, not for toolbar construction.

**New workspace:** copy this skill's `assets/astro/` tree into the study workspace,
preserving paths. Run `pnpm add astro` there and keep the generated lockfile. Create
`public/` for assets. Do not run the server.
This uses Astro's [manual installation](https://docs.astro.build/en/install-and-setup/#manual-setup).

**Existing Astro project:** copy only missing compatible source files from the tree.
Preserve existing package/config files; do not overwrite a frame already in use.

| Starter file                                                                                             | Purpose                         |
| -------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [package.json](../assets/astro/package.json)                                                             | New workspace manifest          |
| [src/study.js](../assets/astro/src/study.js)                                                             | Shared study title              |
| [src/layouts/Preview.astro](../assets/astro/src/layouts/Preview.astro)                                   | Full review frame               |
| [src/components/preview/Toolbar.astro](../assets/astro/src/components/preview/Toolbar.astro)             | Navigation and configuration    |
| [src/components/preview/Option.astro](../assets/astro/src/components/preview/Option.astro)               | Contained content wrapper       |
| [src/components/preview/discover.js](../assets/astro/src/components/preview/discover.js)                 | Route metadata discovery        |
| [src/scripts/preview.js](../assets/astro/src/scripts/preview.js)                                         | Selection, movement, and motion |
| [src/styles/preview.css](../assets/astro/src/styles/preview.css)                                         | Dark pane and option sizing     |
| [src/styles/toolbar.css](../assets/astro/src/styles/toolbar.css)                                         | Compact toolbar chrome          |
| [src/pages/index.astro](../assets/astro/src/pages/index.astro)                                           | Root redirect for an empty app  |
| [src/pages/preview/index.astro](../assets/astro/src/pages/preview/index.astro)                           | Thin start route                |
| [src/pages/preview/example.astro](../assets/astro/src/pages/preview/example.astro)                       | Working thin route to duplicate |
| [src/components/preview/example/options.js](../assets/astro/src/components/preview/example/options.js)   | Metadata and descriptor catalog |
| [src/components/preview/example/Mock.astro](../assets/astro/src/components/preview/example/Mock.astro)   | Replaceable option content      |
| [src/components/preview/example/Knobs.astro](../assets/astro/src/components/preview/example/Knobs.astro) | Working configuration controls  |

Use `/preview/<slug>/` routes and components under `src/components/preview/<slug>/`.
When an application stylesheet exists, import it into routes studying that application.
For a standalone diagram study, use artifact styles instead. Use plain JavaScript
frontmatter and the frame's `head` slot for existing font or head markup. Set
`--pv-page-background` to the real background token when previewing a page. Otherwise
let the artifact component supply its own background. Reproduce relevant production
parents inside the option component.

Set `studyTitle` in `src/study.js` to the study title recorded in the brief. Use the
user's explicit title; otherwise infer a concise title from the brief without asking.
The start page's browser title is the study title. Decision pages use
`<preview title> · <study title>`.

Evidence: installed frame paths, runtime dependency, study title, and content styles/assets.

## 2. Define metadata and options

Each decision route exports `meta`. Required fields: `group` and `title`. Other fields:
`note` for the current round, `building` while work remains, `settled` for the ruling
date, and `questions`/`notes` arrays of `{ id, text }`. Allocate stable IDs such as
`controls-Q2` and `controls-N3`; never derive them from array position or recycle them.

Read the example route, `options.js`, `Mock.astro`, and `Knobs.astro` linked above.
Duplicate the route and its component directory under the new slug; update imports,
metadata, `sidebarProps.slug`, radio IDs, and their matching CSS selectors together.
Replace the mock content, not the frame.

Use one descriptor array for the Options dropdown and rendered options. Each descriptor
has `id`, `name`, `component`, and its `props`. Add `note`, `width`, `sidebar`, and
`sidebarProps` when the option needs them. Pass the catalog to `<Preview {meta} {options} />`.

**Use the frame's components and styles.** `Preview.astro` owns the layout, dark pane,
option selection, and toolbar. `Option.astro` wraps each content component inside
`.pv-page`; builders never construct that wrapper themselves.

**Use the configuration contract.** Keep the descriptor fields `sidebar` and
`sidebarProps` for option controls; put intent in `note`. The toolbar starts at the
bottom-left with labeled Preview navigation, an Options dropdown, and
direct Settings, Questions, and Notes actions beside the drag grip. Support pointer
dragging and arrow-key movement. Each dropdown frame carries previous and next arrows that
step through its entries and wrap at the ends. Keep navigation and the Options dropdown
available with settings closed. Show Questions and Notes actions only with content; show question
counts without opening a panel. Badge Settings with the selected option's knob count: one per
distinct control `name`, so a radio group counts once. Clicking the active action closes it; another action
switches panels. Show one option's content, intent, and settings at a time. Preserve
control values by keeping inactive options and panels mounted but hidden. Initialize
selection from a valid option fragment or the first option. Use the shipped compact
chrome; do not add frame labels inside option content or replace its styles.

**Mark content motion.** Add `data-pv-piece` to the individual content elements that
should move vertically in a tight sequence. Without markers, the frame animates the
content root. Mark a stationary header with `data-pv-still`; keep the canvas steady.
The frame exits pieces over 92 ms with a 5 ms stagger and 32–48 px travel, then enters
pieces over 104 ms with a 6 ms stagger and 36–52 px travel. Cancel obsolete animations
and pending changes after rapid selections. Knob changes animate marked content after
input handlers and CSS state update. Respect reduced motion immediately. Configuration
height changes take 88 ms.

**Choose the option width.** Use the descriptor's `width`: `64rem` is the page default;
use a smaller width such as `28rem` for a component and one common width for diagram
comparisons. The wrapper clamps this to the pane, centers it, and supplies an inline-size
container. Use container queries inside options, not window widths or `100vw`.

**Keep content inside its wrapper.** The pane and gutters stay near-black. The wrapper
clips overflow, isolates stacking, and contains positioned children. Keep fixed controls,
wide media, and overlays inside the option. Size images/SVG to `max-width: 100%` with
proportional height; put oversized diagrams in a preview-owned scroll or zoom region.
Give entirely positioned scenes an explicit height. Do not override `pv-*` styles,
stretch a mock to the viewport, or portal content outside the wrapper.

Keep toolbar navigation, actions, panels, and knobs usable at desktop and phone widths.
Scripts drive frame and preview interactions; expose failures.

For a CSS knob, put labeled radios in the configuration component. Use IDs unique to
preview, option, and value. Match the checked default to the option's initial appearance:

```css
/* Radio controls-B-radius-2 sets B's preview-owned variable. */
:root:has(#controls-B-radius-2:checked) #B { --control-radius: 0.5rem; }
```

Evidence: two comparable options, stable metadata IDs, and a working configuration knob.

## 3. Verify discovery and access

The toolbar's preview index discovers route metadata by glob; no separate registry is
needed. Keep `/preview/` a thin route using `<Preview {meta} options={[]} />` with
`meta` containing `title: 'Start'`, `questions: []`, and `notes: []`. Its canvas says
“Use the toolbar” and points to the toolbar with an arrow.

Put verified previews awaiting feedback first, grouped in phase order with question
counts. List unfinished previews under “Building”, including work awaiting verification;
do not tag
them in the ready lists. List settled previews under “Settled” with their dates. Surface
metadata/import failures under “Broken right now”, outside the ready lists, and log the
error. Syntax or compiler failures can still block the server; keep every saved route
importable.

Give “Building” its own labeled group with muted neutral headings and entries.
Reserve the toolbar index's yellow review emphasis for ready groups.

Keep `noindex` on study routes and exclude them from an existing sitemap. When the
repository has no built application or site root, redirect `/` to `/preview/` using
the starter's `src/pages/index.astro`. Preserve an existing application or site root.

For remote review, configure host `0.0.0.0` and explicit allowed hostnames through
Astro's documented configuration. Obtain the assigned port from the project's control
agent before writing it; use the user's configured 8000–9000 range. Without a control
agent, ask the user for the assignment. Do not choose a port or start the server.

On the user's running server, check the start page and browser title, toolbar index,
an under-edit stub, open-question counts, a metadata-failure fixture, and two options
at desktop and phone widths. Check dragging, arrow-key movement, navigation with
configuration closed, selected-only settings, retained knob values, rapid changes,
piece motion, and reduced motion.
Restore the fixture through normal edits. Without the server, record the verification
blocker; do not mark the frame verified.

Evidence: discovery, failure isolation, responsive toolbar navigation, motion, and knob
results, with the running server URL and assigned port recorded in the ledger.
