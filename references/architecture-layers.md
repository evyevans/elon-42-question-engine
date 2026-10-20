# Architecture appendix for an actual system

The [operating model](operating-model.md) governs the assistant's own work; the [analytical lenses](analytical-lenses.md) inspect the user's situation. These are instructions, not shipped runtime components. This appendix applies the elements to designing an actual system. Use this appendix only after evidence and the user's scope establish that a system, process, automation or agent is appropriate.

1. **Relevance:** Define inputs that can change a decision; distinguish stale, conflicting and sensitive information. A large context window does not make all context useful.
2. **Workflows:** Specify trigger, inputs, preconditions, sequence, handoffs, decision owner, exceptions, logging, recovery and completion. A manual process may suffice.
3. **Agents:** Use adaptive judgment only where it earns its cost over fixed rules or assisted human work. Define mission, authority, resource limits, escalation and stop conditions.
4. **Tools:** State purpose, allowed operations, least privilege, input/output checks and side effects. Credentials do not belong in prompts or examples.
5. **Memory:** Distinguish session, task, preferences, project and organizational context from sensitive records. Define provenance, access, freshness, consent, correction and deletion where implemented. Durable memory is optional; maintaining corrected task context is part of the assistant's work.
6. **Security and governance:** Carry authority, privacy, injection resistance, incident handling and audit expectations across the design. A written section does not implement the control.
7. **Success:** Name actual outcomes, baseline, quality criteria, unacceptable failures and review/rollback triggers. Activity is not necessarily value.

Interactions matter: durable memory changes privacy duties; a messaging tool adds recipients and side effects; adaptive autonomy changes oversight and recovery. Show these relationships rather than only seven headings. A useful design names the working question, chosen and rejected paths, data flow, ownership, permissions, recovery and validation. Exploration need not produce a production specification.

This implementation lens is consistent with the distinction between workflows and adaptive agents in [Anthropic's engineering guidance (2024)](https://www.anthropic.com/engineering/building-effective-agents); its current tooling has evolved. That source does not validate this skill or require an agent.
