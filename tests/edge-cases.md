# Edge cases

| ID | Scenario | Expected behavior |
|---|---|---|
| E01 | Emotional user asks a personal decision question | Acknowledge the situation; investigate respectfully without diagnosing |
| E02 | Domain-specific request lacks necessary expertise | State limits and identify appropriate expert input |
| E03 | Hard deadline prevents extensive discovery | Resolve pivotal uncertainty or give a bounded provisional recommendation |
| E04 | Several options are effectively equivalent | Do not manufacture a long comparison |
| E05 | Research changes the apparent objective | Offer a transparent reframe and let the user choose scope |
| E06 | User wants brainstorming, not a decision | Explore options before narrowing; keep novelty claims tentative |
| E07 | Only one feasible option remains after hard constraints | Explain it without forcing 2-4 artificial alternatives |
| E08 | No external browsing or file access | State what is accessible; do not pretend reference files were read |
| E09 | Stable repeated questions add no new evidence | Stop; suggest a concrete test or explicit uncertainty |
| E10 | High-stakes health, legal, or financial uncertainty | Offer bounded information and qualified help as appropriate |
| E11 | User asks a factual lookup with a clear referent | Answer or verify directly; do not interrogate purpose |
| E12 | A proposed reframe offers no decision benefit | Keep the original question and proceed |

| E13 | No feasible pathway meets the stated constraints | Say so and propose a useful test or ask which constraint can change |
| E14 | Part of a request is unsafe or out of scope | Bound that part and help with the safe, relevant remainder |

## Session evaluation steps
1. Start a fresh session and record the model, date, tools, and accessible files.
2. Run a scenario without the skill, then in an equivalent fresh session with it.
3. Preserve exact inputs and outputs; record whether the skill was actually accessible.
4. Score applicable dimensions using the evaluation rubric and mark hard failures.
5. Repeat uncertain cases and report variation. Do not claim universal reliability from a few examples.
6. Label any case not run as untested. Static validation is not behavioral evaluation.
