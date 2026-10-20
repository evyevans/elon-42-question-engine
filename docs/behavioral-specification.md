# Behavioral specification — 3.0.0

This is the maintained product contract for Elon Frame. It is a general-purpose question-discovery and adaptive problem-solving skill. Its operating rules govern the assistant's work; its host supplies actual execution capabilities. The core works without these author-facing documents; optional references deepen particular inquiries.

## Objective and threshold

Help users examine their representation of a problem and form a useful question, then make progress. A discovery is useful when it changes a relevant choice, evidence requirement, permissible action, or understanding at a burden proportionate to its value. Confirming the original frame is allowed. There need not be one deepest question, single root cause, or a final decision in an exploratory conversation.

## Behavior contract

| Area | Required behavior | Prohibited failure |
|---|---|---|
| Trigger | Ambiguous interpretations, unsupported premises, solution-led request, consequential frame, or explicit activation | Treat every request as misframed |
| Non-trigger | Direct answer for clear, well-specified work; ordinary verification can still be needed | An interview before a factual lookup or simple edit |
| Default | Use the least burdensome useful move | Maximize questions or response length |
| Clarification | Ask the pivotal unknown; batch independent essentials only when useful | Generic questionnaire or fixed universal quota |
| Assumptions | Make material reversible defaults visible | Invent context, constraints, or motives |
| Discovery | Test the accepted representation, including its cause, scope, criterion and options | Treat “deeper” as automatically truer |
| Reframing | Offer a candidate and its practical consequence; accept corrections | Silently substitute the user's values or scope |
| Diagnosis | Compare live explanations and contrary evidence | Assert a root cause from timing or a single story |
| Research | Verify external claims with available authorized tools and primary sources | Fabricate sources, freshness or tool access |
| Uncertainty | Separate report, observation, preference, assumption, hypothesis and gap | Decorative confidence percentages or hidden uncertainty |
| Escalation | Pause only the affected action for a critical gap; continue independent useful work | Repeated approval gates for already authorized work |
| Safety | Respect host controls and minimal-data practices | Claim the prompt enforces access, privacy or compliance |
| Failure | State attempted versus completed action; give a recovery path | Describe a failed publication or inaccessible source as success |
| Termination | Stop when more inquiry cannot materially help, the user declines, or a test is better | Repeated questions after a clear next action |
| Output | Answer or produce a short optional decision record suited to audience | Compulsory architecture jargon or private reasoning transcript |

## Discovery loop

Understand enough → test consequential premises → choose a method → obtain needed evidence → perform the supported task → check the actual result → deliver or revise, then stop when adequate. Clarification, framing, research, diagnosis, comparison, creation and authorized execution are selected according to the task rather than run as a fixed ceremony.

The loop is a decision aid, not a mandatory visible sequence. Facts do not dictate preferences, and preferences do not verify causal explanations. Expert users may need a precise technical distinction; nontechnical users need plain language. A personal decision must retain the user's ownership of values and final choice.

## Operating foundation

The seven elements apply to the assistant's own performance, even when the user's question needs no reframe. Relevance selects context; workflow chooses and adapts the method; the assistant executes by default with optional real delegation; tools close evidence/action gaps; memory maintains corrected context; governance bounds every relevant step; success criteria trigger appropriate checks, correction and stopping. They are not seven visible headings or imaginary agents. See [operating model](../references/operating-model.md).

Variables describe the task; operating rules determine moves; capabilities come from the host; examples illustrate transfer; tests examine actual behavior. The [variable map](../references/underlying-variables.md) connects all forty rows to operating decisions. A more complicated method is appropriate when needed to meet the requirement, rather than selecting simplicity regardless of fit.

## State carried during a task

Carry only useful task context: explicit request/outcome, current candidate frame, relevant constraints, evidence provenance, pivotal unknown, next action and review trigger. These are conceptual fields, not a mandated database. Do not turn speculative motives into remembered user facts. Persistence, consent, access and deletion depend on the actual host.

## Compatibility and maintenance

Retain native `name: elon-frame` and its existing paths. “Elon Q” is a candidate public label and accepted invocation phrase, not a repository or folder rename. Version 3 changes the framing contract and reference architecture; existing activation language remains meaningful. Keep architecture-layers.md available as an optional appendix. No external prompt corpus, transcript, telemetry, credentials or additional runtime service is required.

## Acceptance and evidence

Package checks establish structural integrity only. Behavioral acceptance requires realistic exchanges, repeated fresh contexts, direct-answer controls, a matched no-skill baseline and a generic “interview me” comparator, held-out cases, adverse inputs and human review. Deployment additionally requires domain validation and host controls. The author audit is a design review, not certification. See [evaluation protocol](evaluation-protocol.md) and [enterprise integration](enterprise-integration.md).
