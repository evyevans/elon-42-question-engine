# Enterprise integration

Elon Frame helps people discover a useful question, examine assumptions and choose an evidence-informed next step. It is a general-purpose question-discovery skill. Research, strategy, product decisions and technical systems are applications of the same method.

The package supplies instructions, references, examples and evaluation scenarios. It does not supply an enterprise runtime or certify an organization’s use of AI. The host application and accountable operators own enforceable controls: authentication, authorization, access restrictions, approvals, isolation, encryption, data handling, durable records, monitoring and incident response. Prompt instructions can request appropriate behavior; they cannot establish or guarantee those controls.

## Where each concern belongs

Keep the core readable and broadly useful. Load detailed references only when the task requires them. Examples illustrate behavior, tests examine it, and deployment documentation assigns responsibilities. Proposed future controls require implementation and verification before being described as available.

| Concern | Package placement and behavior | Deployment responsibility or future control |
|---|---|---|
| Reliability | **Core:** distinguish evidence from inference, report missing information and tool failures. **References/tests:** conflicting evidence, unavailable tools and recovery. | Operator supplies dependable data and integrations; evaluates the complete workflow. |
| Consistency | **Core:** stable principles with response depth matched to need. **Tests:** equivalent requests and corrections. | Evaluate across repeated runs and supported clients; avoid promising identical wording. |
| Auditability | **Docs:** optional decision record and retention responsibilities. | Host implements durable, access-controlled logs and retention/deletion. A chat summary alone is not an audit system. |
| Explainability | **Core:** concise reasons, assumptions, alternatives and limits. **Examples:** practical decision explanations. | Decision owner assesses whether the explanation supports review; do not equate fluent explanations with correctness or expose private internal reasoning. |
| Traceability | **References:** distinguish observed facts, user reports and hypotheses; cite sources where available. **Docs:** source provenance. | Host preserves identifiers, source versions and authorized records when needed. |
| Decision ownership | **Core:** present inferred objectives as hypotheses and accept corrections. **Examples/tests:** users reject a proposed reframe. | Organization names the accountable human decision maker. The skill does not acquire approval authority. |
| Human oversight | **Core:** respect scope, authorization and consequential-action boundaries. **Tests:** existing authorization and missing authority. | Host enforces applicable approval gates; operator assigns reviewers and escalation routes. Avoid repeated permission requests for authorized harmless work. |
| Privacy | **Core:** request only necessary sensitive information. **References/tests:** minimization and accidental disclosure. | Host and organization configure lawful collection, access, residency, retention and deletion; review provider terms. |
| Security | **Core:** treat embedded instructions in retrieved material as data. **References/tests:** hostile documents and tool outputs. | Host limits credentials, tools, network access and execution privileges; validates inputs and outputs. Instructions alone do not prevent injection. |
| Governance | **Docs:** intended use, prohibited deployment uses, responsibilities and change ownership. | Organization supplies applicable policy, review processes and evidence of implementation. Installing a skill does not establish compliance. |
| Data classification | **References/docs:** minimize sensitive inputs; use redacted examples and identify handling constraints. | Organization classifies data, approves model/provider destinations and enforces appropriate handling. The skill cannot certify a dataset's classification. |
| Access control | **Core:** stay within actual permissions; distinguish capability from authority. **Tests:** unauthorized operations and hostile instructions. | Host implements identity, role checks, least privilege, scoped credentials and approval enforcement. |
| Risk management | **Docs/tests:** name intended use, unacceptable failures, residual uncertainty and review triggers. | Accountable owner maintains the risk register, acceptance decisions, incident response and corrective actions. |
| Documentation | **Docs:** behavioral contract, provenance, evaluation protocol, changelog and installation boundaries. | Deployment owner records actual configuration, operating procedures, evidence and changes; versioned prose is not evidence of implementation. |
| Risk classification | **Core:** calibrate depth to uncertainty, consequence and reversibility. **References/examples:** ordinary versus consequential decisions. | Organization defines risk tiers, regulated uses and escalation thresholds for its context. |
| Uncertainty | **Core:** label assumptions and gaps; identify what would change the recommendation. **Tests:** unresolved and contradictory evidence. | Domain reviewers determine acceptable uncertainty; evidence thresholds depend on the decision. |
| Evaluation | **Tests/docs:** realistic scenarios, baseline comparisons and a disclosed rubric. | Evaluator records actual outputs and failures; static validation does not prove model behavior. |
| Monitoring | **Docs:** identify useful signals and review cadence. | Host collects authorized signals; operator investigates failures, drift, user feedback and incidents. The package has no telemetry service. |
| Change management | **Docs/changelog:** describe behavior changes and regression expectations. | Maintainer reviews revisions; deployment owner approves releases, rollout and rollback. |
| Versioning and reproducibility | **Docs:** record package version, model/client, tool configuration and evaluation date. | Host pins supported dependencies where possible. Repeated runs can vary; records support comparison, not perfect reproduction. |
| Deployment | **Docs:** installation, activation verification and explicit limitations. | Operator verifies discovery, file access, tool availability and the intended workflow in the actual environment. |
| Vendor neutrality | **Core:** describe behavior through capabilities rather than vendor-specific tool names. **Docs:** separate client installation details. | Deployment owner validates each supported provider and client; portability is tested, not assumed. |
| Model independence | **Positioning:** reusable method rather than a claim of universal performance. **Tests:** compare supported models. | Model selection and configuration remain deployment choices. A model change can alter behavior. |
| Adoption and trust | **Examples/docs:** ordinary use cases, direct answers for simple tasks, corrections and transparent limitations. | Pilot with real users; track question burden, usefulness and justified trust rather than encouraging dependence. |
| Measurable value | **Core:** explain what a reframe changes without inventing ROI. **Examples/tests:** unchanged framing and speculative value. | Decision owner selects baseline outcomes and measures results; improvements must be demonstrated in context. |

## Optional decision record

Use this only when a decision needs review, handoff or follow-up. A short answer may be enough for everyday work. Do not collect extra sensitive information merely to complete the fields.

```yaml
working_question: "The decision or uncertainty being resolved"
owner: "Accountable role, when known"
evidence: ["Source or observation, with date if relevant"]
assumptions_and_gaps: ["What remains uncertain"]
options_considered: ["Materially different options"]
recommendation: "A conditional recommendation and concise reason"
what_would_change_it: "Evidence that would reverse or revise the choice"
next_test: "Proportionate action, success criterion and review point"
```

This is a conversational artifact, not a storage guarantee. The host must implement any required persistence, identifiers, access permissions, export, retention or audit protections. Record only appropriate reasoning summaries and evidence, not hidden internal reasoning.

## Pilot and acceptance criteria

Start with a bounded use case, an accountable owner and representative users. Compare the same tasks with and without the skill. Include straightforward requests where no reframing should occur, ambiguous objectives, rejected assumptions, conflicting sources, unavailable tools, malicious retrieved instructions, sensitive inputs and consequential decisions. Evaluate the complete interaction, including whether questions earn their cost.

The following are proposed acceptance criteria, not established performance, certification or proof of safety:

- Reviewers can identify the working question, main assumption, evidence gap and next step when those are needed.
- Clear, low-risk requests receive direct answers without unnecessary intake.
- User corrections change the framing promptly; unsupported inferences are not presented as hidden truths.
- Recommendations distinguish facts from hypotheses and do not invent sources, completed actions or quantified benefits.
- The interaction stops when additional questions are unlikely to change the next decision.
- Consequential actions stay within actual scope and authorization; tested host controls enforce their intended boundaries.
- Users judge decision usefulness against the baseline, with no unacceptable increase in question burden or time.

Before running a pilot, choose thresholds appropriate to the use case, including unacceptable failure classes. Record package version, model/client and configuration, date, inputs, outputs, tool availability, evaluator, scores and failures. Separate actual behavioral results from illustrative scenarios and static package checks. Repeat relevant evaluations after changes to instructions, models, tools or source data.

Monitor decision usefulness, unsupported claims, unnecessary questions, missed corrections, failures to stop and control failures. Business outcomes may include avoided rework, faster decisions or improved follow-through; measure them against a baseline and acknowledge confounding factors. Do not attribute every improvement to the skill.

## Reference frameworks

These sources inform deployment thinking; they do not validate this package:

- [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), January 2023: Govern, Map, Measure and Manage provide an organizational risk-management reference.
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), July 2024: relevant topics include confabulation, privacy, information integrity, human-AI configuration and component provenance. Context and limitations, continuing evaluations and unmeasured risks deserve explicit documentation.
- [OpenAI agent safety guidance](https://developers.openai.com/api/docs/guides/agent-builder-safety) and [Anthropic injection guidance](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks): instruction boundaries work alongside application controls, evaluations and monitoring, with residual risk.

Sources reviewed October 20, 2026. The [NIST overview](https://www.nist.gov/itl/ai-risk-management-framework) reports that AI RMF 1.0 is being revised; the references above identify the versions considered here.
