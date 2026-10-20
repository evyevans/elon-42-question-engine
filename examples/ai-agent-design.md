# Agent design: one application, not the default destination

**Transferable behavior:** Select an appropriate executor and scope actual permissions before delegating or acting. The setting illustrates this rule; it does not define the skill's scope.

## Request
"Create agents to research competitors, update the CRM, and email recommendations."

## Good first move
"Which decision should this support, and which changes are the agents actually authorized to make?"

## Illustrative continuation
User: "I want a weekly briefing. No CRM edits or outgoing email without review."

Assistant: "The narrower objective is a reliable weekly briefing with review, not autonomous operations. A scheduled read-only workflow may fit better than several agents."

Compare manual-assisted research, a fixed briefing workflow, and bounded adaptive research. Use the architecture reference only now: source relevance, schedule, tool scope, optional memory, injection resistance, review, and validation. Preserve review requirements; do not silently add external writes.

## Value and test
The frame removes unneeded autonomy and surfaces source quality as a key uncertainty. Pilot a briefing and inspect coverage and factual accuracy. If sources require unpredictable navigation, bounded adaptive research may earn its complexity.

## Another application: customer email
For "handle my customer emails," first distinguish repetitive, low-risk categories from cases needing human judgment. A fixed workflow that classifies and drafts for review may suffice. Start with mailbox read and draft permissions; add sending or adaptive autonomy only when authorized and supported by evaluation. Inspect draft usefulness and unapproved-send failures, rather than assuming fewer edits alone proves quality.
