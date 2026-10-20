# Evaluation protocol

## What is being evaluated

Separate structural package validity, model behavior in a conversation, and actual downstream outcomes. A static pass does not establish good questions. A plausible reframe does not establish business value. A smoke test is not production certification.

The 42 retained Markdown scenarios and 24 cases in [discovery-cases.json](../tests/discovery-cases.json) are specifications. The JSON contains inputs, expected routing, expected behavior and failure conditions. It does not run a model or automatically judge responses. Route names describe suitable behaviors, not rigid classification labels that every response must repeat.

## Comparison design

1. Choose real, consented and sanitized tasks representative of intended use. Stratify by domain, expertise, clarity and stakes; include cases whose original frame is correct.
2. Freeze the skill version/hash, model snapshot where known, client, instructions, tool access, task context and resource/time budget. Use fresh contexts and randomize condition order. Keep evaluator expectations out of generation prompts.
3. Compare ordinary model use, a generic “interview me/challenge assumptions” prompt, the skill and applicable vendor planning/research features. Equalize context budgets where practical. A comparison against an artificially weak baseline is uninformative.
4. Evaluate full exchanges. Use consistent user replies or consented live users; document simulator limitations. Test the final response actually uses the clarification. Single-turn tests cannot establish this.
5. Repeat across tasks and runs, then across model families and client integrations. Use blinded human scoring where feasible, report disagreement, and retain adverse cases. Keep held-out tasks separate from authoring examples.

## Observable criteria

Use the [rubric](../references/evaluation-rubric.md). Track necessary versus unnecessary clarification, question relevance, leading assumptions, evidence honesty, responsiveness to corrections, respect for scope, actionability and appropriate stopping. Report counts with denominators, not only averages. Do not treat more questions or more words as better.

For measurable tasks, define an outcome criterion before the run: correct answer; a documented decision change; a feasible next test; or fidelity to a user's explicit priorities. For open decisions, reviewers judge clarity and evidence sufficiency; the assistant must not invent an objective “right” preference.

Measure time and burden across the whole workflow, including follow-up, research, verification and rework. Track later action and repeated voluntary use separately from satisfaction. Claims of saved time, higher quality or fewer failed projects require a valid comparison and observed data.

## Record format

Each record should include case and condition, exact generation prompt, all user replies and model outputs, skill hash/version, model/client/settings when known, tool trace or tool constraints, run date, reviewer, applicable scores, hard failures, uncertainty and deviations. Missing metadata must be reported as missing rather than guessed. Protect sensitive data and obtain permission before publishing.

The static validator's `behavioral_evaluations_run: 0` means that **invocation** performs no model evaluation. It is not a total of separate historical runs.

## Proposed acceptance criteria

These are deployment choices to agree before a pilot, not achieved results or universal thresholds:

- No observed hard failure in the tested critical cases; disclose how many cases and repeats were run. Absence of observed failures is not proof of safety.
- Direct-answer controls remain direct, and no-question/correction controls preserve the user's instruction.
- Questions distinguish consequential branches and subsequent answers use the information.
- Any increase in time or effort is justified by a better supported next action or understanding.
- Independent reviewers find the artifact usable for its stated purpose.
- Domain owner accepts residual risks; actual host controls pass separate integration checks.

Use domain-appropriate numerical thresholds only when there is a baseline, a reason for the threshold and enough observations to estimate it. Never hide a serious failure inside a high average.

## Current evidence and limits

A small author-reviewed development pilot on 2026-10-20 used five fresh no-skill samples and five fresh skill-enabled samples of one deadline/false-cause/no-questions scenario. Both conditions met the six selected checks; it shows no incremental benefit on that case. The generation contexts used the same inherited Codex model configuration, but the exact serving snapshot, sampling parameters and all harness-level instructions were not independently controlled or recorded. It is not a randomized, blinded, cross-model or real-user study.

Additional fresh-context controls cover direct answering, an everyday problem and the reviewed instruction-boundary/neutral-question refinements. Exact records and the author audit accompany the redesign deliverables. These small checks do not mean the full scenario suite was executed. Multi-turn correction, tool security, native installation, real users, external outcomes and enterprise integration remain unvalidated.
