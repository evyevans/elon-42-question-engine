# Contributing

Keep question discovery general-purpose. A change should improve a demonstrated task or documented gap, preserve direct answers and user agency, and keep the core self-contained. Do not make every problem an architecture exercise or add a new mandatory intake field for each edge case.

1. Explain the problem and show a realistic input, expected behavior and failure condition. Add or update a case in `tests/`; use a unique ID.
2. Change the smallest relevant instruction or reference. Preserve existing links, license and notices. Keep deep material on demand rather than repeating it throughout the core.
3. Run `python3 scripts/validate.py` and `python3 scripts/test_validate.py`. Review the full diff for broken links, copied third-party content, secrets and removed user work.
4. For behavior claims, compare fresh contexts against the same model without the skill and relevant generic/vendor alternatives. Follow [evaluation protocol](docs/evaluation-protocol.md); keep exact inputs, outputs, model metadata and limitations. A written case is not a passed test, and passing static checks is not efficacy evidence.
5. Describe what changed, why, and what was actually tested in a pull request. Disclose regressions and uncertainty; do not average away hard failures.

Use only consented, minimized and sanitized examples. Do not commit credentials, telemetry, copied proprietary prompts, raw private conversations, dependency installers or unrelated deployment prompts. Propose branding or native-name migrations separately. The free core remains complete under the existing MIT license.
