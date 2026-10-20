# Elon Frame

<img width="1376" height="768" alt="The right question comes first. Question first, build second." src="https://github.com/user-attachments/assets/10b993c1-7520-47d8-af5a-57701200ef5f" />

A free, question-first skill for AI. It helps you and your AI find the question underneath the problem before anything gets answered, designed, or built.

> The quality of an answer is constrained by the quality of the question.

## What it does

Most people lead with whatever is on top of their mind: "build me X", "write me Y". Elon Frame slows that down just enough to ask what is actually being solved. It clarifies the objective, exposes hidden assumptions, defines what success looks like, and compares different paths before execution. The result is better answers, and often a better problem than the one you started with.

It works on any problem: business strategy, research, career decisions, product ideas, workflows, automation, and AI systems. Designing agents is one use case, not the point.

## Start here (non-technical)

1. Click the green **Code** button above, then **Download ZIP**. (If a Release exists, download `elon-frame.zip` from the **Releases** page instead.)
2. Unzip the download.
3. Pick the option that matches your AI tool:
   - **Claude.ai (paid plans with Skills enabled):** zip the `elon-frame` folder so `SKILL.md` sits inside it, then upload it under Settings > Capabilities/Skills.
   - **Claude Code:** place the folder in your skills directory (for example `~/.claude/skills/elon-frame/`) so `SKILL.md` is directly inside it.
   - **ChatGPT, Gemini, or any other AI:** attach `SKILL.md` and the files in `references/` to a new chat, then paste the activation prompt below.

## Activation prompt (copy and paste)

```text
I want you to use the attached Elon Frame skill as an active question-first reasoning framework for this conversation.

Read the attached SKILL.md first. Then read the files in references/ when they are relevant. Do not summarize the skill back to me. Apply it.

For simple, clear, low-risk requests, answer directly.
For ambiguous, strategic, high-stakes, or open-ended problems: identify my literal request, infer the underlying question or objective behind it (labeled as an inference), separate facts from assumptions, ask only the single highest-value clarifying question if the answer would change materially, then compare 2-4 genuinely different pathways and recommend the simplest safe, testable one. Tell me what deeper question or value the investigation surfaced. State what evidence would show the recommendation is wrong. Never claim to have performed actions you did not perform.
```

## Quick test

Start a new chat and say: *"I want to [your goal]. Apply Elon Frame before you answer."* Then watch whether the AI asks about your real objective instead of jumping to a solution.

## Make it your own

This is an open starting point. Edit `SKILL.md` to change the behavior, add your own examples to `examples/`, and add a test to `tests/` for anything you change. Share your version.

## What is inside

| Path | Purpose |
|---|---|
| `SKILL.md` | The skill itself (frontmatter plus operating instructions) |
| `references/` | Philosophy, question framework, architecture layers, safety, evaluation rubric |
| `examples/` | Vague request to well-framed request, including a real estate RevOps case |
| `tests/` | Ambiguity, adversarial, and edge-case checks |

## How it differs from generic prompting

- **Question-first:** it tests whether the question is well-formed before answering.
- **Investigative:** it looks for the underlying question and the deeper value in the problem, not just a faster answer.
- **Architecture-aware:** when you are building something, it reasons across relevance, workflows, agents, tools, memory, security, and success criteria.
- **Safety-bounded:** least privilege, human approval, and no invented actions.
- **Decision-oriented:** it ends in a recommended, testable next step.

## Contributing

Fork the repo, improve a file, and open a pull request. Add a new test in `tests/` for any behavior you change.

## License

MIT. See `LICENSE`.
