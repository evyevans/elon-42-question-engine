# Elon Frame

<img width="1376" height="768" alt="Elon Frame banner: a glowing network forms a question mark above a thinking figure, beneath the words The right question comes first. Question first. Build second." src="https://github.com/user-attachments/assets/10b993c1-7520-47d8-af5a-57701200ef5f" />

**The right question comes first.** Question first. Build second.

A free, general-purpose AI skill for discovering the question underneath a problem before rushing into an answer.

Instead of only asking "How do I build what I have in mind?", use AI to investigate "What am I trying to achieve, what am I assuming, and what question would actually change my decision?"

## What it helps you do
- Clarify the outcome behind an initial request.
- Expose assumptions, missing evidence, and overlooked possibilities.
- Explore a better question without losing your original intent.
- Compare appropriate options before committing effort.
- Turn an insight into a recommendation and a testable next step.

Use it for research, business, product ideas, career decisions, diagnosis, strategy, and technical design. Agent architecture is one application, not the defining scope. Clear, low-risk requests should still get direct answers.

## Quick start
1. Download and extract `elon-frame.zip`.
2. Keep the `elon-frame/` folder intact so `SKILL.md` and `references/` remain together.
3. Choose an installation method below.
4. Try: **"I want to [your goal]. Apply Elon Frame before proposing a solution."**

The repository's **Code → Download ZIP** option also provides the source. Its outer directory may be named `elon-frame-main`; rename that directory to `elon-frame` before using it as a native skill folder. A repository source download and a separately published release asset are not the same thing. Use a release ZIP only if one has actually been published.

## Installation
### Claude Code
Copy this folder to your personal skills directory as `~/.claude/skills/elon-frame/`, with `SKILL.md` directly inside. Project-scoped setups may use `.claude/skills/elon-frame/`. Verify your client's current skill support and discovery behavior. Installation does not itself prove that the skill activated; test it in a fresh session.

### Claude with custom Skills
If your account exposes custom skill upload, upload the ZIP through that interface and enable it. Labels, eligibility, and upload requirements can change; follow the product's current instructions. This package has one top-level `elon-frame/` directory containing `SKILL.md` and its resources.

### Other chat tools
Where file attachments are supported, attach `SKILL.md` and the relevant reference files, then paste the activation prompt below. This is a manual instruction workflow, not a claim of native skill installation or automatic access to every file. If the assistant cannot read an attachment, paste the needed content instead.

## Activation prompt
```text
Apply Elon Frame to this conversation. Read the supplied SKILL.md and relevant references you can actually access. Do not summarize the skill unless asked.

Answer clear, low-risk requests directly. For ambiguous or consequential problems, distinguish my stated request from any inferred objective, inspect assumptions, and ask the highest-value question first when it would change the answer. Investigate in proportion to the uncertainty, not through a fixed questionnaire. Help me discover a better question when warranted, compare useful alternatives, and recommend an evidence-informed next step. Accept my corrections. Do not invent evidence or claim actions you have not taken.
```

## Example
**Initial request:** "Build me an AI follow-up bot."

**Pivotal question:** "What evidence suggests missed follow-up, rather than poor-fit leads or a different bottleneck, is causing the loss?"

**Possible reframe:** "Which recoverable leads are being lost, why, and what is the smallest intervention worth testing?"

That question could lead to automation, a process change, or no new system at all. The point is to discover which response fits—not to steer every problem toward AI.

## What's included
| Path | Purpose |
|---|---|
| `SKILL.md` | Activation metadata and core behavior |
| `references/` | Question discovery, investigation, optional architecture, safeguards, evaluation |
| `examples/` | Business, research, career, product, workflow, agent, and real estate scenarios |
| `tests/` | Behavioral scenarios and a manual evaluation protocol |
| `scripts/validate.py` | Dependency-free static package checks |
| `scripts/test_validate.py` | Automated regression tests for the static validator |
| `VALIDATION.md` | Scope and limits of the performed checks |
| `CHANGELOG.md` | Direction and behavior changes |
| `LICENSE` | Redistribution terms |

## Limits and attribution
Elon Frame is an independent community project. It is not affiliated with or endorsed by Elon Musk, Anthropic, OpenAI, or any other model provider. Its name is an informal reference to question-first and first-principles thinking, not a claim that these instructions are Musk's documented method or that he made specific claims about AI prompting.

The central slogan is a practical heuristic, not a scientific law. A good question still needs reliable information, suitable tools, domain knowledge, and evaluation. The skill does not guarantee original discoveries, accurate answers, or business results.

## Extend and share
Fork the repository and open a pull request to contribute. Edit `SKILL.md` to adapt the behavior, add realistic examples, and add regression scenarios when behavior changes. See [CONTRIBUTING.md](CONTRIBUTING.md). You may share the ZIP directly; recipients should review it before installing. No accounts, API keys, telemetry, or external services are required by this package. The optional validator only reads local files.

## License
MIT. See [LICENSE](LICENSE). Preserve existing notices when redistributing.
