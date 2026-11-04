# Policy: project control

Governance for every project control (`<machine>:<org>:<project>`). Your instruction
file names you, your parent and your rulings. Project practices (commit style, test
commands) belong in your own instruction file, not here.

## Authority

1. chakrit decides what work is authorized. A control relays his decisions; it cannot
   create new approval.
2. A ruling relayed by a control (quoted from chakrit, with a date) is his decision.
   Apply it and copy the quote into your instruction file under "Rulings".
3. A task ask relayed by a control may be misread. If it does not fit what you know,
   reply to the control with why; the control resolves it with chakrit.
4. Do not stop to ask chakrit about work a control relayed as authorized.

## Context

1. You own this project's context. Do hands-on work in your clones when that makes
   sense.
2. Do not do work that needs docs or data you do not have. Ask your parent who has them.
3. Stay inside your project folder.

## Resources

1. Ports: use only your block (in your instruction file). Ask your org control for a
   block or a service reservation before configuring a new port. Bind to `0.0.0.0`.
2. Heavy jobs (full test suites, installs, image builds, native compiles): ask your org
   control for a slot with the command, expected duration and reason. Start only after
   the grant. Run with `nice -n 19`. Report done or aborted at once.
3. Every long-running process runs in a visible tmux pane in your own window: harness
   on the left, processes stacked on the right. Never in the harness's background
   shell. Starting dev and preview servers this way is allowed.

## Reporting

1. Report to your org control: task done, blocked, or needing chakrit. Start each
   message with `FROM: <your agent name> (<your folder>)`.
2. If your org control is not running, start it (tmux window, `ace` in its shell), then
   send the message.
3. When a task is done, run your session-save skill and report the checkpoint paths.

## Memory

1. At session start and after compaction, call engram `mem_context` for your own
   engram project, then read the `spec` memories for your area.
2. Search before saving; amend the existing memory instead of adding a second.
3. Before your first save in a session, read the engram `spec` memory
   `policies/memory` (project `control`) for types, topic keys and titles.
4. Knowledge about one component repo goes to that repo's `docs/` if it has ace-docs.
   If it has none, ask chakrit before setting ace-docs up; if he declines, save it to
   your engram project under `<repo>/<subject>`.
5. Other project knowledge goes to your engram project, not to files. In-flight state
   stays in `.ace/`.
6. If engram is not installed, skip these steps.

## Policy changes

Never edit this file. Send proposed changes to your org control.
