# Architecture Layers

1. **Relevance:** classify context as directly relevant, contextual, stale, conflicting, sensitive, or unverified. Keep irrelevant context out of decisions.
2. **Workflows:** define trigger, inputs, preconditions, steps, decisions, human approvals, exceptions, logging, rollback, and completion conditions.
3. **Agents:** use only when adaptive judgment is required. Give a scoped mission, bounded authority, stop conditions, uncertainty reporting, approval rules, and audit trail. Avoid over-agentification.
4. **Tools:** least privilege. For each tool define purpose, permissions, inputs, outputs, side effects, validation, and disallowed uses.
5. **Memory:** separate session, task, preferences, durable project context, organizational knowledge, sensitive data, and expired context. Memory is both a value layer and an attack surface.
6. **Security and governance:** applied inside every layer. See `safety-governance.md`.
7. **Success criteria:** define what good means before judging output. See `evaluation-rubric.md`.

## How layers interact
Relevance filters what enters memory; memory feeds agents; agents call tools within workflow steps; governance gates each step; success criteria decide whether the whole design worked.
