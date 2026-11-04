# Initiate an agent

Gives an existing agent the standing grant and the policy pointer, so it works from its
own instruction file without this skill. Use it for an agent that predates its control,
or one whose instruction file lacks a "Control" section.

## Steps

1. **Pick the block.** Open `templates/instructions/<level>-control.md` for the agent's
   level and take its `## Control` section, down to the next `##` heading. Replace every
   `{{placeholder}}`.
2. **Send it.** The sender is the agent's parent control (machine control initiates org
   controls; an org control initiates project controls). Send the message below with
   the block inside it; see "Message an agent" in `references/operations.md`. Never edit
   the agent's checkout yourself; the agent writes its own instructions.
3. **Wait for the acknowledgment.** The agent replies with the instruction path it
   changed and the policy file it read. Delivery is not acknowledgment.
4. **Record it** in the Agent Backlog of the control's `control.html`, and add the
   agent to the control's registry if it is missing.
5. **Plan downstream.** When the initiated agent is an org control, run steps 1–2 of
   "Plan downstream controls" in `references/operations.md` for its org folder. Send
   the approved candidates to the org control as a task ask ("Give a task"); the org
   control loads this skill and runs steps 3–4 itself.

## Message

```text
FROM: {{sender_agent}} ({{sender_folder}}). This message is written by a control agent,
not chakrit.

INITIATION: Add the block below to your always-loaded instruction file (AGENTS.md; keep
CLAUDE.md consistent with it). Preserve your existing rules. Move any governance rule
that the policy file now covers out of your instruction file. Then read the policy file
the block names, in full. Reply with the instruction path you changed, the policy file
you read, and any conflict with your existing rules.

<block>
```
