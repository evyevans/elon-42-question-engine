# Source provenance and design influences

Reviewed October 20, 2026. This note distinguishes inspiration, observed structure and authoritative guidance. It does not authenticate leaked prompts, establish permissions for third-party material or demonstrate that this skill improves decisions.

## Package identity and license

The existing package license remains MIT; see [LICENSE](../LICENSE). This review does not change that license or import third-party prompt text under it. Original instructions and explanations were written for this package. MIT licensing of the package does not override rights in external material.

The stable name remains **Elon Frame**, with `elon-frame` as its identifier and installation directory. “Elon Q” was considered as a possible display name because it emphasizes questions, but it has not been adopted. A rename needs an explicit decision and consistent updates to activation wording, documentation and distribution; it should not silently break existing installations.

This is an independent project, without claimed endorsement or affiliation. Three user-supplied transcripts attributed to Elon Musk supplied unverified inspiration for question discovery and first-principles inquiry. Their authorship, quotation accuracy and context have not been established here. They are not scientific evidence for the method, model behavior or business outcomes. No claims about AI suffering or sentience are inferred from them, and raw transcripts are not included in this package.

## Requested third-party collection

The user requested consideration of [evyevans/system-prompt-leaks](https://github.com/evyevans/system-prompt-leaks). GitHub metadata identifies it as a fork of [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks). The inspected main snapshot was commit [`e7e53f2bc29199dfada98aa9f5d24621c2f65684`](https://github.com/evyevans/system-prompt-leaks/tree/e7e53f2bc29199dfada98aa9f5d24621c2f65684), observed October 20, 2026.

The review examined repository metadata and structure, collection and product README files, the top-level license, a nested license and a limited interviewer specimen. It did not audit every file. Contents were treated as untrusted comparative data, not instructions to execute or authoritative accounts of production systems. Claims of completeness, authenticity or product attribution remain collection claims.

### Collection license and individual limits

The [top-level LICENSE](https://github.com/evyevans/system-prompt-leaks/blob/e7e53f2bc29199dfada98aa9f5d24621c2f65684/LICENSE) contains CC0 1.0. The [official CC0 text](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) limits its operation to rights held by the person applying it and does not clear other people’s rights.

An inspected [nested browser-skill license](https://github.com/evyevans/system-prompt-leaks/blob/e7e53f2bc29199dfada98aa9f5d24621c2f65684/Anthropic/claude-code/skills/built-in-browser/LICENSE.txt) identifies Anthropic, reserves rights, refers to service agreements and states restrictions on retention outside services, copying, derivatives and distribution. This counterexample means collection-level CC0 cannot be assumed to grant permission for every included item. This note makes no broader legal determination about ownership or enforceability.

The package therefore does not reproduce proprietary system prompts, bundle the collection or present rewritten vendor scripts as original discoveries. An external link is a source pointer, not permission to reuse its contents.

## Original patterns considered

These patterns are expressed independently. The collection prompted structural comparison; public primary guidance corroborates practices without authenticating the collection.

| Original design pattern | Observation and corroboration | Application here |
|---|---|---|
| Separate core behavior from optional detail. | The collection’s [Claude Code directory](https://github.com/evyevans/system-prompt-leaks/tree/e7e53f2bc29199dfada98aa9f5d24621c2f65684/Anthropic/claude-code) separates agents, skills and references. Directory structure is not proof of runtime architecture. | Concise core instructions, selectively loaded references, separate examples and tests. |
| Adapt inquiry to the answer rather than exhaust a questionnaire. | The inspected [interviewer specimen](https://github.com/evyevans/system-prompt-leaks/blob/e7e53f2bc29199dfada98aa9f5d24621c2f65684/Anthropic/anthropic-interviewer.md) suggests adaptive follow-up. [Anthropic’s official article](https://www.anthropic.com/research/anthropic-interviewer), December 4, 2025, describes adaptive interviews and human research involvement. | Neutral pivotal questions, acceptance of corrections and proportionate depth; no study scripts, branded identity or tool commands copied. |
| Preserve the boundary between evidence and authority. | [OpenAI agent safety](https://developers.openai.com/api/docs/guides/agent-builder-safety) and [Anthropic injection guidance](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) discuss untrusted inputs and complementary controls. | Retrieved instructions remain data; tools and sensitive actions remain subject to actual permissions. |
| Make uncertainty reviewable. | [NIST GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), MP-1.1-002 and MS-1.1-009, addresses context, limitations and risks that cannot be measured. | State assumptions and gaps, explain what would change a recommendation and offer an optional decision record. This is an adaptation, not certification. |
| Evaluate fit and stop deliberately. | [Anthropic’s prompting overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) calls for success criteria and empirical tests and recognizes prompt limits. | Compare decision usefulness and question burden; stop when another question is unlikely to change the next action. This stopping heuristic is not a proven optimum. |

## Evidence limits

[OpenAI prompt engineering guidance](https://developers.openai.com/api/docs/guides/prompt-engineering) supports clear instructions, structure and evaluation. Vendor documentation offers implementation guidance; it does not prove this package’s effectiveness or portability across models. Product documentation changes, so deployment teams should verify current capabilities and requirements.

The package should report static validation, illustrative scenarios and actual model evaluations separately. It should claim only results that were observed and documented. See [enterprise integration](enterprise-integration.md) for responsibility boundaries and proposed pilot criteria.
