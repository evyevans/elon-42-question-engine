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

## Selective open-source refresh

The foundation revision also inspected current metadata and selected source files from the six requested repositories on October 20, 2026. The links below pin the observed default-branch revisions. This was a read-only source review, not installation, execution, or effectiveness testing. No third-party prompt text, code, or dependencies were imported; the operating rules are original synthesis.

| Source at observed revision | Mechanism informing this revision | Boundary and rights observation |
|---|---|---|
| [severity1/claude-code-prompt-improver](https://github.com/severity1/claude-code-prompt-improver/tree/50aae187bb4f08b852f318234b654df3332726a4) | Its [clarity nudge](https://github.com/severity1/claude-code-prompt-improver/blob/50aae187bb4f08b852f318234b654df3332726a4/scripts/nudge_builtins.py) uses context before a larger clarification flow. | MIT; not archived when reviewed. The hook emits instructions, not an independently validated clarity classification. Do not inherit mandatory exploration agents, question quotas, or every-prompt wrapping. |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research/tree/1b7d2e80db9faa586165c60e09096dbbfd483a64) | [Research state](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/src/open_deep_research/state.py) separates a brief, notes, and findings; [prompts](https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/src/open_deep_research/prompts.py) request source-preserving compression. | MIT; archived August 21, 2026. Citation instructions do not validate claims. Do not adopt the framework, default concurrency, exhaustive report style, or blanket failure policy. |
| [anthropics/skills](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) | [Skill creator](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md) illustrates progressive disclosure, baseline comparisons, and evidence-backed assertions. | Not archived; no blanket repository license. Skill creator has an [Apache 2.0 license](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/LICENSE.txt); document skills have separate proprietary terms. Public availability does not imply permission to adapt every file. Keep acceptance cases untouched by prompt optimization. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy/tree/ab1ca173e60ec39cde2328e37a149d5812e36d31) | Explicit [signatures](https://github.com/stanfordnlp/dspy/blob/ab1ca173e60ec39cde2328e37a149d5812e36d31/dspy/signatures/signature.py) and [candidate evaluation](https://github.com/stanfordnlp/dspy/blob/ab1ca173e60ec39cde2328e37a149d5812e36d31/dspy/teleprompt/gepa/gepa.py) support task contracts and retained evaluation evidence. | MIT; not archived. Metrics and evaluators can be wrong; training reuse can overfit. Do not add optimizer infrastructure or treat model judgments as truth. |
| [obra/superpowers](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) | [Verification guidance](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md) ties completion claims to evidence; [brainstorming](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/brainstorming/SKILL.md) permits direct execution of a complete brief. | MIT; not archived. Use proportionate checks rather than importing the whole workflow, rigid rituals, repeated approvals, or mandatory orchestration. |
| [evyevans/system-prompt-leaks](https://github.com/evyevans/system-prompt-leaks/tree/e7e53f2bc29199dfada98aa9f5d24621c2f65684) | Comparative organization only: separate tool-specific instructions and distinguish represented state from actual execution. | Not archived. Root CC0 and nested proprietary restrictions coexist; authenticity remains unverified. See the detailed collection review above. No prompts copied or executed. |

These observations identify useful design mechanisms and limits, not rankings or proof that this package is better. Any future substantial copying needs a fresh file-specific rights review and applicable attribution; the package's MIT license is not a substitute.
