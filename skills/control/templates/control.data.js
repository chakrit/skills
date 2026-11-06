/*
 * Data for control.html, which sits next to this file and renders every view, count and
 * link from it. Update the page by editing only this file; change control.html only when
 * chakrit asks for a different view, column or group.
 *
 * The object assigned below, up to the closing "};", is strict JSON: double quotes, no
 * comments, no trailing commas. Values are plain text, never HTML. Keep every key,
 * including empty group lists. The page computes all counts, leaves empty groups out,
 * and shows a list of problems instead of the views when a key is missing, extra or
 * not a string.
 *
 * title      Page title.
 * updated    Date of the last edit, such as "2026-11-06". Set it on every edit.
 * tasks      Work only chakrit can do, by group: doing (In progress), todo (To do),
 *            done (Done). Row: {"item": "", "source": "", "since": ""}.
 * attention  Decisions and approvals an agent is waiting on, one entry per waiting agent:
 *            {"agent": "<agent name>", "items": [row, ...]}.
 *            Row: {"item": "", "where": "", "recommendation": "", "since": ""}, where
 *            "where" names the place chakrit acts. Remove a row once chakrit acts, and
 *            an agent's entry once it has no rows. Its sidebar count turns
 *            warning-coloured while it has rows.
 * backlog    Every task agents own, by group: blocked (Blocked), waiting (Waiting on
 *            chakrit), doing (In progress), todo (Queued), done (Done).
 *            Row: {"item": "", "agent": "", "source": "", "next": ""}. "source" is
 *            chakrit's verbatim words or the reporting agent; "next" names the next step,
 *            or the commit, PR or save location as evidence. Drop done rows older than a
 *            week.
 * links      Related control pages: {"label": "", "href": ""}, href relative to this
 *            file. Org controls on machine control's page, machine control on an org
 *            control's page.
 */
window.CONTROL = {
  "title": "{{title}}",
  "updated": "{{date}}",
  "tasks": {
    "doing": [],
    "todo": [],
    "done": []
  },
  "attention": [],
  "backlog": {
    "blocked": [],
    "waiting": [],
    "doing": [],
    "todo": [],
    "done": []
  },
  "links": []
};
