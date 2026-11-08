# Run a task

## 1. Resolve and mark

Map the user's slug or title to one preview. Split a request spanning previews into
one task per preview. Read its rulings and dependencies. Record the verbatim request,
round, active references, and file ownership before briefing a builder.

Classify feedback through [rulings.md](rulings.md) before briefing the work. Put clear
mandates and open choices in separate fields. Apply mandates directly to the prototype;
turn unspecified visual or interaction choices into comparable options, not chat
questions. Carry nonblocking assumptions and placeholders forward. Resolve only true
blockers before assigning the affected work.

In the served checkout, set `building: true`; for a new preview, create an importable
stub with valid metadata. Commit the status change when local commits are permitted.
Keep the flag set through integration and verification.

Evidence: each requested preview appears under “Building” in the index, with a ledger event.

## 2. Assign isolated work

Give each builder one preview in a Git worktree. Keep worktrees outside watched source
paths or exclude them through the framework's documented watcher configuration.
Parallelize independent previews. Reserve shared frame and stylesheet edits for the
coordinator when builders are not modifying affected previews.

Use this brief, substituting actual paths and constraints:

```text
Build /<slug> in <worktree>; served checkout: <path>; base commit: <hash>.
Read this skill's SKILL.md, references/ledger.md, references/build.md, references/frame.md,
and the worktree's repository instructions.
User words: "<verbatim request>"
Decision: <one decision>. Round: <number>.
Carry over: <rulings, exact values, unchanged references>.
Mandates: <specified changes to apply directly to the prototype>.
Compare: <open choices and distinct options; none for a fully specified mandate>.
Allowed files: <route and preview-owned component/assets paths>.
Shared files are read-only. Do not start/restart a server or run a full build.
Checks: <repository's lightweight check command on these paths>.
Leave building: true. Keep every saved route importable.
Commit locally when permitted; do not push or integrate your own branch.
Report options, checks, spend, artifact paths, branch and commits in three lines.
```

Without subagents, act as the builder in an isolated worktree and return to phase 3.
Keep shared ledger writes coordinator-owned; builders return evidence to append.

Evidence: recorded owner, worktree, base commit, allowed paths, and complete brief.

## 3. Integrate and verify

Review the builder's changes for scope, ruled constraints, and importability. Integrate
one coherent preview task into the served branch when that local action is authorized.
Resolve metadata conflicts field by field; preserve newer requests, rulings, and status.
Do not overwrite them by choosing the builder's whole file.

On the user's running server, check every option at desktop and phone widths: assets,
fonts, toolbar navigation, knobs, links, relevant behavior, and the index entry.
Check selection and navigation with configuration closed, retained knob values,
piece motion after knob changes, reduced motion, and the study title in the browser tab.
Record route, dimensions, result, and evidence.
Without a running server or browser access, record a verification blocker and keep
`building: true`. Put the missing prerequisite in the Questions panel when the site is
reachable; otherwise report the site-access blocker in chat. Continue independent tasks.

For a defect, return this preview to phase 1 with a corrected brief. After verification
passes, clear `building`, move the preview into the index's top review lists, record the
ready event, and report the route in one line.

For a comparison, wait for the user's selection before settling its open decision.
This is a Wait. For a verified mandate, return to **Apply ruling** to record its result.

Copy valuable worktree scratch artifacts into the study's recorded archive before any
cleanup. Record their paths and the worktree's state. Follow repository permission
rules for worktree and branch cleanup; retain them when cleanup would destroy state.

When interrupted, ask the builder to save an importable state, commit when permitted,
and stop with `building: true`. Resume from its recorded commit and amended brief.

Evidence: integrated commits, browser results, truthful status, recoverable artifacts,
and next operation or blocker.
