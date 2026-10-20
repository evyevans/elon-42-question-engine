# Contributing

Keep question discovery general-purpose. Do not make every problem a technical architecture exercise. Preserve direct answers, user corrections, and explicit uncertainty.

For behavior changes, explain the failure being addressed, update the smallest relevant instruction or reference, and add a scenario with an expected outcome and failure signal. Avoid duplicating instructions across files. Read supporting references on demand rather than expanding the main skill indefinitely.

Run `python3 scripts/validate.py` and `python3 scripts/test_validate.py` from the repository root. Review the diff for broken relative paths, unsupported claims, secrets, and accidentally removed user work. Where possible, run matched baseline and skill-enabled scenarios and report the model and limitations. A written test case is not a passed test.

Keep redistribution notices. Do not add API keys, telemetry, automatic network calls, dependency installers, or unrelated prompts to the skill. GitHub deployment instructions belong outside the skill package.
