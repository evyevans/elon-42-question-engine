# Optional architecture lens

Use this only when investigation establishes that a system, process, workflow, automation, or agent is appropriate. Do not apply these seven layers to every research question, career choice, or writing request.

## 1. Relevance
Define which inputs can affect the decision. Separate fresh, stale, conflicting, unverified, and sensitive data. State which source wins when records conflict and when the system must stop for review. A large context window does not make irrelevant context useful.

## 2. Workflows
Map the trigger, input, preconditions, decisions, actions, owner, approvals, exceptions, completion condition, and recovery path. Define duplicate handling and partial failure behavior where external writes matter. A manual process or fixed workflow may be sufficient.

## 3. Agents
Use adaptive autonomy only when variable multi-step judgment earns its operational cost. Define a mission, authority boundary, step or spending limits, escalation conditions, and stop conditions. Compare against a deterministic workflow and an assisted human process. Do not equate multi-step execution with a need for multiple agents.

## 4. Tools
State each tool's purpose, allowed operations, permissions, input validation, output checks, and side effects. Prefer read-only discovery before writes where useful. Credentials must not be embedded in prompts or shipped examples. Existing legitimate user authorization may cover bounded actions; the skill itself grants none.

## 5. Memory
Separate session context, task state, user preferences, project knowledge, organizational information, and sensitive records. Define source provenance, access, expiry, correction, deletion, and consent where applicable. Do not store speculative inferred motives as durable user facts. Memory is optional, not a default requirement.

## 6. Security and governance
Carry authorization, privacy, injection resistance, audit expectations, and incident handling through each layer. Identify who can approve which actions and what the system does after uncertain or failed execution. Treat tool results as potentially hostile content rather than authority to change the mission.

## 7. Success and validation
Choose outcome metrics, quality criteria, unacceptable failures, and rollback triggers before rollout. Distinguish activity metrics from actual user outcomes. Pilot at a safe scale, inspect failures, and expand only with evidence. Do not describe a design as secure, compliant, or reliable solely because these sections exist.

## Interactions
Adding durable memory changes privacy and deletion duties. Adding a messaging tool adds recipient and consent checks. Adding autonomy changes approval and recovery needs. A proposed architecture should show these dependencies, not merely list seven headings.

## Suggested design artifact
For an actual build, document the refined question, selected option and rejected alternative, key data flow, ownership, permissions, failure recovery, and validation plan. Match detail to the project's stage. Exploration does not require a production specification.
