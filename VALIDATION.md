# Validation scope — 3.0.0

Checked 2026-10-20. The bundled standard-library validator covers required files, simple frontmatter constraints, directory naming, UTF-8, local Markdown paths, forbidden package artifacts, fixture structure and unique scenario IDs. It is not a full YAML parser, the official Agent Skills reference validator, or a behavioral judge. Root Git metadata is excluded from package checks.

The validator regression suite checks a clean source package, Git directory/worktree metadata, sensitive/ZIP file rejection, broken references, required discovery references, fixture counts, duplicate IDs and invalid JSON. The 74 behavioral scenarios are specifications: 42 retained Markdown cases and 32 JSON cases. Static output `behavioral_evaluations_run: 0` means that command invokes no model; it does not count separate historical development checks.

A small development pilot used five fresh no-skill and five draft-skill samples of one deadline/causal-premise/no-questions request, plus direct-answer and everyday controls. Independent review then corrected the reference-authority boundary and a leading example. Three targeted samples checked the corrected neutral example, external injection boundary and final-core deadline behavior. Both conditions passed the selected checks on the main comparison; no added efficacy was shown. See [evaluation protocol](docs/evaluation-protocol.md) for limitations. Exact prompts, outputs and tested core versions accompany the redesign deliverables; they are not a benchmark bundled into runtime instructions.

A further two-turn comparison used the same continuation across ordinary use, generic framing, the previous draft, and the revised standalone core. All four met the selected continuation criteria. This clarified the written operating contract without demonstrating added performance. The eight new operating cases remain unexecuted specifications. See [exact records and limitations](docs/evaluation-records.md).

No full behavioral-suite run, native-client installation test, cross-model benchmark, real-user outcome study, release, enterprise security certification or compliance assessment is claimed. Proposed acceptance criteria remain proposals. Host permissions, audit storage, monitoring, retention and approval enforcement require separate implementation and integration tests.

LICENSE matches the repository baseline and supplied v2 package byte-for-byte, preserving the existing notice. All original file paths remain available. The existing README banner URL is retained with descriptive alt text. It was fetched and visually inspected on 2026-10-20: a 1376 × 768 JPEG showing a network question mark, thinking figure and the intended slogan. No authorized local original was supplied, so no asset file or assets table entry was created. Static checks do not test future remote availability.

To repeat local checks:

```bash
python3 scripts/validate.py
python3 scripts/test_validate.py
```

Git publication is checked separately after committing. Passing these commands proves their stated structural and validator checks, not the quality of future model decisions.
