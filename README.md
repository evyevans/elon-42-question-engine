# Elon Frame

<img width="1376" height="768" alt="Elon Frame banner: a glowing network forms a question mark above a thinking figure, beneath the words The right question comes first. Question first. Build second." src="https://github.com/user-attachments/assets/10b993c1-7520-47d8-af5a-57701200ef5f" />

## Discover the question worth answering.

A free, general-purpose AI skill for examining a problem before investing in the answer.

Your first request might name the right task. It might also name a symptom, an assumed cause, or a solution chosen too early. Elon Frame helps you test that framing, find the question that matters, and move toward a useful answer or next step.

It works with personal decisions, business strategy, research, education, communication, product discovery, operations, and technical work. An agent or automation is one possible outcome. Sometimes a conversation, an experiment, or no new system is more useful.

**Clear request? Get a direct answer. Uncertain problem? Investigate only what could change the next step.**

## See the difference

**Request:** “Add an AI chatbot so users come back more often.”

**Useful question:** “What evidence points to unanswered questions as the reason people leave?”

If users are stuck during setup, fixing that step might help. If they finish setup and still leave, the problem may be elsewhere. A chatbot remains an option; it is a proposed solution to test.

The value is the decision difference, not a clever rewording. Keeping a well-supported original question is also a successful result. These are illustrative examples, not measured customer outcomes.

## Try it

1. Use **Code → Download ZIP** on this repository. A source ZIP and a separately published release are different things; use a release asset only if one exists.
2. Extract it and rename the outer folder to `elon-frame` if needed, keeping `SKILL.md` directly inside.
3. Install it using your client's skill instructions, or use the manual method below.
4. Try: **“Apply Elon Frame to this problem: [your situation].”**

### Native skill clients

For Claude Code, a conventional personal location is `~/.claude/skills/elon-frame/` and a project location is `.claude/skills/elon-frame/`. Follow your client's current discovery instructions. Other Agent Skills clients may use different locations and invocation syntax. The package follows the [Agent Skills format](https://agentskills.io/specification); that does not certify that every client has been tested.

For a client with custom-skill ZIP upload, follow its current upload requirements. If repackaging, include one top-level `elon-frame/` folder with `SKILL.md` and its resources. Installing a file does not establish that the skill activated; test it in a fresh session.

### Manual use in a chat

Attach `SKILL.md` and only the references needed for your task. If the assistant cannot read attachments, paste their content. This is manual instruction use, not native installation or automatic access to every repository file.

```text
Apply Elon Frame using the supplied SKILL.md. Answer clear requests directly. If the framing matters, identify the question worth resolving, distinguish evidence from assumptions, and investigate only what could change the next step. Propose rather than impose a reframe. Respect my corrections and scope. Do not invent context, evidence, benefits, or completed actions.
```

## What you get

When useful, a short decision record: the working question, why it matters, evidence and gaps, a recommendation or next test, and what would change it. It is optional; a simple request should not receive a form.

Start with an [everyday decision](examples/everyday-decision.md), [career choice](examples/career-decision.md), [research question](examples/research-framing.md), [product idea](examples/product-discovery.md), [business strategy](examples/business-strategy.md), [operational problem](examples/general-business-problem.md), or [real estate / RevOps problem](examples/real-estate-revops-example.md). Technical applications include [workflow automation](examples/workflow-automation.md) and [agent design](examples/ai-agent-design.md).

## How it is organized

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Standalone core behavior and selective reference routing |
| `references/` | Variables, discovery patterns, seven optional analytical lenses, evidence, safeguards and evaluation |
| `examples/` | Worked conversations across technical and nontechnical domains |
| `tests/` | Manual behavioral specifications and portable evaluation inputs |
| `scripts/` | Dependency-free static checks and validator regression tests |
| [Behavioral specification](docs/behavioral-specification.md) | Maintained behavioral contract |
| [Enterprise integration](docs/enterprise-integration.md) | Deployment responsibilities and limits |
| [Evaluation protocol](docs/evaluation-protocol.md) | How to test value, burden and failures |
| [Source provenance](docs/source-provenance.md) | Inspiration, evidence and third-party content boundaries |
| [Positioning and launch](docs/positioning-and-launch.md) | Product hypotheses and draft launch materials |
| [VALIDATION.md](VALIDATION.md) | What has actually been checked |

## Teams and enterprises

Use it inside approved tools to make assumptions, evidence gaps and decision ownership easier to review. The free core is complete. Potential paid services—facilitation, training, workflow adaptation and evaluation—would be separate offerings, not features shipped here.

This is a versioned instruction package, not enterprise infrastructure. Authentication, access control, sensitive-data handling, durable audit logs, monitoring, retention and approval enforcement belong to the host system and operating organization. No compliance, reliability, productivity or ROI guarantee is made. Validate the actual model, domain and integration before consequential use.

## Limits and attribution

Question-first is a heuristic. Better framing cannot repair false data, replace professional expertise or guarantee a better outcome. The project is independently authored and is not affiliated with or endorsed by Elon Musk, Anthropic, OpenAI or any model provider. It does not reproduce a public figure's cognitive method or proprietary system prompts. “Elon Q” is an invocation alias and naming candidate; the package and repository remain `elon-frame`.

No accounts, API keys, telemetry or external services are required by this package. Optional research uses only the host's actual tools and permissions.

## Contribute

Run `python3 scripts/validate.py` and `python3 scripts/test_validate.py`. Propose a realistic failing case, the smallest relevant improvement and its evidence. Share consented, sanitized examples. Written scenarios are not passed model tests. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE). Preserve existing notices when redistributing.
