# Elon Frame

![The Right Question Comes First: Question first. Build second.](assets/elon-frame-banner.jpg)

A question-first reasoning skill for AI. It helps an AI find the right question before it builds the answer.

> The quality of an answer is constrained by the quality of the question.

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
For ambiguous, strategic, high-stakes, architecture, automation, agent, or workflow requests: identify my literal request, infer my likely underlying objective (labeled as an inference), separate facts from assumptions, ask only the single highest-value clarifying question if the answer would change materially, then compare 2-4 genuinely different pathways and recommend the simplest safe, testable one. State what evidence would show the recommendation is wrong. Never claim to have performed actions you did not perform.
```

## Quick test

Start a new chat and say: *"Help me decide whether this problem needs an agent, a workflow, or neither. Apply Elon Frame."*

## What is inside

| Path | Purpose |
|---|---|
| `SKILL.md` | The skill itself (frontmatter plus operating instructions) |
| `references/` | Philosophy, question framework, architecture layers, safety, evaluation rubric |
| `examples/` | Vague request to well-framed request, including a real estate RevOps case |
| `tests/` | Ambiguity, adversarial, and edge-case checks |
| `assets/` | Banner image used in this README |

## How it differs from generic prompting

- **Question-first:** it tests whether the question is well-formed before answering.
- **Architecture-aware:** it reasons across relevance, workflows, agents, tools, memory, security, and success criteria.
- **Safety-bounded:** least privilege, human approval, and no invented actions.
- **Decision-oriented:** it ends in a recommended, testable next step.

## Contributing

Fork the repo, improve a file, and open a pull request. Add a new test in `tests/` for any behavior you change.

## License

MIT. See `LICENSE`.
