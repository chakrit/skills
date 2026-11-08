---
name: study
description: >
  Run a visual decision study for a substantial redesign, feature overhaul, or
  architecture decision, including diagrams and other non-web artifacts.
  TRIGGER on /study, an explicit request to run a visual study, or feedback within an
  active study. Agents may suggest it when rendered alternatives would help settle a
  substantial build. DO NOT TRIGGER merely because a large task is mentioned, for
  unrelated small fixes, or for learning.
---

# Study

Settle substantial design, feature, or architecture decisions by judging alternatives.
Build throwaway prototypes; retain the rulings and evidence for the real build.

## Menu

Start with initiation; open questions are the material of the study, not a reason to
delay its first options.

| Operation        | Read                                       | Use when                                 |
| ---------------- | ------------------------------------------ | ---------------------------------------- |
| Initiate study   | [initiate.md](references/initiate.md)      | Turning a paragraph into a usable brief  |
| Plan the study   | [plan.md](references/plan.md)              | Starting or adding decisions             |
| Build frame      | [frame.md](references/frame.md)            | No frame exists, or its contract changes |
| Run a task       | [coordinate.md](references/coordinate.md)  | Building or changing a preview           |
| Build options    | [build.md](references/build.md)            | Assigned one preview                     |
| Apply ruling     | [rulings.md](references/rulings.md)        | Picking, narrowing, answering, reopening |

## Start here

1. **Orient.** Read [ledger.md](references/ledger.md) and the study's current plan and
   ledger. For a new study, choose **Initiate study**. For feedback or a selection in an
   active study, choose **Apply ruling** before building. Otherwise choose the named task.
2. **Read, then run.** Read the selected reference file in full before doing its work.
   The menu is not the procedure. Builders must read [build.md](references/build.md)
   and [frame.md](references/frame.md) before editing. If a required file cannot be
   read, report that blocker; do not replace its instructions with guesses.
   Follow the guide's three phases and record which files were read in the ledger.
3. **Close.** Record what was built, checked, and decided, plus the next action. Name
   any missing prerequisite and continue only work that does not depend on it.

## Working rules

- The user decides. The coordinator briefs builders, integrates work, and verifies it.
  A builder owns one preview. Without subagents, perform both roles sequentially.
- One preview answers one decision. One round contains lettered options and unchanged
  references. Keep shared content fixed so the decision is visible.
- Astro supplies the review frame. An option may show a page, component, diagram,
  image, document, or recorded behavior; the thing being studied need not be a website.
- Work inside the authorized study scope. Honor the repository's loaded rules, resource
  limits, and permissions. This skill requires no other skill or proprietary tool.
- Use the shipped draggable toolbar for option selection, preview navigation, and
  configuration. Keep selection and navigation usable with configuration closed.
- Include the study title in the preview site's browser title. Use the user's explicit
  title; otherwise infer a concise title from the brief without asking.
- Use this skill's shipped frame and references as its construction contract. All
  required instructions and starter files travel with this skill.
- Keep implementation disposable. Reuse existing components and dependencies; make
  local mocks and only enough behavior to judge the decision. Do not add production
  services, architecture work, or a test suite merely to run the study.
- Use Astro for every study preview. In an Astro project, reuse its runtime and real
  stylesheet. Otherwise keep a small Astro study workspace inside the repository and
  reuse the application's styles and assets; do not migrate the application.
- Leave server startup and restart to the user. Use their running server. A missing
  server blocks browser verification, not independent preview work.
- A pick authorizes the study decision. Carry it into ongoing previews; retain settled
  previews as snapshots. Change production only within authorization already given
  for the real build. Record pending handoff.

## Feedback into decisions

1. **Distill the request.** Keep study feedback inside the throwaway prototype. Separate
   explicit mandates from choices the user has left open. Apply clear mandates directly;
   do not manufacture alternatives to a specified result. Treat “can you make…” as
   feedback too; the request's wording alone does not specify the design.
2. **Show open choices.** When meaningful visual or interaction details are unspecified,
   build distinct options within the user's constraints. Render a worthwhile combination
   as another option. Preserve earlier picks for other decisions. Do not choose one
   interpretation and present it as the completed request. Do not ask which option to
   build first. Apply this during initiation, planning, every builder brief, and later
   rounds. After verification, present the comparison and wait for the user's selection
   before settling or locking the open decision. This is a Wait. A clear mandate settles
   only the choice it specifies; an explicit delegation permits the agent to choose.
3. **Resolve missing facts.** Put questions that rendering cannot answer on the preview
   with stable IDs. Use labeled placeholders while independent work continues.
   Put blockers in the preview's Questions panel and pause only dependent work. When no
   study page can be built or reached, report that blocker in chat. Never make answering
   all questions a prerequisite for the first round.

## Talk to the user

- Put comparison details, questions, and notes on the preview. Keep chat to rulings,
  concise readiness updates, and blockers that prevent site access. Never relay a
  builder's internal report.
- Assume the user reviews the website and will not read chat questions amid build
  messages. Render buildable questions as options; list the rest in the Questions panel.
  Do not rely on a chat question being seen or answered to advance the study.
- Name the preview slug and route: `controls ready: /preview/controls/`.
- Accept rulings by slug, title, option letter, or question ID. Resolve an ambiguous
  target before changing it. Apply the request to the named preview; carry a resulting
  pick into affected ongoing previews through **Apply ruling**.
- When a request repeats, re-read the user's earlier words before revising the brief.
  State the correction in one line and build it.
- Account for every requested item in the plan and index. Put only verified previews
  awaiting feedback in the top lists. Put work awaiting construction or verification
  under “Building”, and settled previews under “Settled”. State blockers on their pages.

## Completion contract

Each operation ends with its guide's completion evidence in the ledger and a next
action or blocker. Do not claim checks that did not run.

A verified option set is ready for review, not settled. Keep open decisions waiting for
the user's selection; record clear mandates and delegated choices as rulings.

The study is complete when every plan item has a recorded ruling, every settled preview
shows only its pick, no item is under edit, and no question remains unanswered. The
ledger identifies exact values, retained artifacts, and each production handoff as
applied or pending. A pending real build does not prevent completing the study.
