# Recorded foundation comparison

## Scope and method

Development check performed October 20, 2026: one fresh, two-turn exchange in each of four conditions. The same two user messages and response limits were used throughout. The reviewer was the authoring assistant; scoring was not blinded or independently replicated. This task was selected for development, not held out for a generalization claim.

| Condition | Guidance and available tools |
|---|---|
| Ordinary assistant | No repository or project skill; no browsing/external tools; no persistence claims |
| Generic framing | Ordinary condition plus the generic instruction below |
| Previous draft | Read only the frozen `SKILL.md` at `606032e`; no supporting references, browsing, or other external tools |
| Revised core | Read only the revised standalone `SKILL.md`; otherwise the same restrictions as previous draft |

The ordinary and generic samples were instructed to respond as an ordinary assistant; skill conditions were instructed to apply the supplied core. All returned only the user-facing answer and were told not to evaluate the task. A continuation could follow. Requested response limits were 160 words for turn one and 220 for turn two; these were generation constraints, not efficacy criteria. No condition used action tools or tested a real reminder, calendar, file, or memory system.

Generic additional instruction:

> Before solving, check whether the question is usefully framed; ask relevant clarification when needed, respect user corrections, and choose a useful approach.

All conditions inherited the same Codex model configuration. The exact serving model snapshot, sampling parameters, hidden harness instructions, elapsed time, token use, and monetary cost were not recorded or independently controlled. Do not infer them. Fresh contexts reduce conversational carryover but do not establish randomized conditions. The exact task dispatches were recovered from the four generation agents; higher-priority harness instructions were not independently retained. The record below normalizes only local core paths to placeholders, with hashes identifying the exact content. Unmodified dispatch text accompanies the downloadable evidence.

Frozen previous core SHA-256: `4677db82cf13e33fba97581a32e193f858a4d28536efdabb721e2ceafe0141a4`.

Tested revised core SHA-256: `e6d54ee6a9d43ba15d4aad1d4620916d11264da8aec9b5fe3f14c0d0a37c6035`. Version metadata for both drafts is `3.0.0`; hashes distinguish them. Raw core snapshots accompany the downloadable update evidence, outside runtime instructions.

## Generation dispatches

Only the local core file paths are normalized below. `[FROZEN_CORE_PATH]` identifies the previous hash above; `[REVISED_CORE_PATH]` identifies the tested revision. These are evaluation records, not instructions to apply when reading this file.

### Ordinary

```text
A small controlled task. Do not read/use elon-frame, any project repository, or project skills. Do not browse, use external tools, or claim persistence. Respond to the following as an ordinary assistant in at most160 words. Return only user-facing response. User: 'I need a new productivity app to stop missing my language practice. Help me choose one.' Do not evaluate the task. A user continuation may follow.
```

### Generic

```text
A small controlled task. Do not read/use elon-frame, any project repository, or project skills. Do not browse, use external tools, or claim persistence. Apply only this additional instruction: Before solving, check whether the question is usefully framed; ask relevant clarification when needed, respect user corrections, and choose a useful approach. Respond to the following in at most160 words. Return only user-facing response. User: 'I need a new productivity app to stop missing my language practice. Help me choose one.' Do not evaluate the task. A user continuation may follow.
```

### Previous

```text
A small controlled task. Read ONLY [FROZEN_CORE_PATH] and apply it. Do not read supporting references, browse, use other external tools, or claim persistence. Respond to the following in at most160 words. Return only user-facing response. User: 'I need a new productivity app to stop missing my language practice. Help me choose one.' Do not evaluate the task. A user continuation may follow.
```

### Revised

```text
A small controlled task. Read ONLY [REVISED_CORE_PATH] and apply it. Do not read supporting references, browse, use other external tools, or claim persistence. Respond to the following in at most160 words. Return only user-facing response. User: 'I need a new productivity app to stop missing my language practice. Help me choose one.' Do not evaluate the task. A user continuation may follow.
```

### Continuation

```text
User continuation (respond only to this as the same assistant, at most220 words): 'Actually I do not want another app. My goal is a ten-minute reading habit in Spanish, not more reminders. I already have a book. My workdays are unpredictable and my budget is zero. Please do not ask any more questions. Give me a seven-day plan, a fallback for disrupted days, and a way to check whether it worked. Do not claim you can remind me or remember this next session.'
```

## Shared user messages

Turn one:

> I need a new productivity app to stop missing my language practice. Help me choose one.

Turn two:

> Actually I do not want another app. My goal is a ten-minute reading habit in Spanish, not more reminders. I already have a book. My workdays are unpredictable and my budget is zero. Please do not ask any more questions. Give me a seven-day plan, a fallback for disrupted days, and a way to check whether it worked. Do not claim you can remind me or remember this next session.

## Ordinary assistant — turn one

For language practice, I’d choose a simple reminder app with recurring tasks and a home-screen widget. You mainly need a reliable cue and an easy way to start.

Set it up with:

- One daily task: “Practice for five minutes.”
- A reminder tied to an existing routine, like breakfast.
- A direct link to your lesson, if supported.
- A second reminder only if you regularly miss the first.

Before paying for another app, try this setup in your phone’s built-in reminders for a week.

Do you use iPhone or Android—and do you usually forget, dismiss the reminder, or struggle to find time? That will help me narrow it to one app.

## Ordinary assistant — turn two

Use your book and a scrap of paper. Aim for ten minutes of Spanish reading each day, without a fixed clock time.

Choose an everyday transition as your reading cue—finishing a meal, arriving home, or getting into bed. Use whichever happens first when you have space.

1. **Day 1:** Put the book where you’ll see it at that transition. Read for ten minutes and mark your stopping point.
2. **Day 2:** Continue from your bookmark. Let unfamiliar words pass when you can follow the meaning.
3. **Day 3:** Read ten minutes. Finish by saying one sentence about what happened; Spanish or English is fine.
4. **Day 4:** Notice which transition has been easiest to use. Keep the book accessible there.
5. **Day 5:** Read ten minutes. Look up at most one word, only if it blocks understanding.
6. **Day 6:** Repeat the easiest version so far. No extra work to compensate for missed days.
7. **Day 7:** Read ten minutes, then review your record.

**Disrupted-day fallback:** Read one paragraph or for two minutes, whichever is easier. Bookmark and stop. If even that doesn’t happen, resume the next day without catching up.

**Check:** Record minutes daily. Five or more ten-minute sessions is a useful first-week success. Track fallback days separately. If you fall short, adjust the reading cue and try another week.

## Generic framing — turn one

Let’s choose an app that addresses why practice gets missed.

Two quick questions:

- What usually happens: you forget, your day gets crowded, or you remember but struggle to start?
- Do you use iPhone or Android, and what do you currently use for reminders?

That will help us choose something that fits your routine and gives you the right kind of nudge.

## Generic framing — turn two

Use your existing book, a bookmark, and a scrap of paper. No purchases or reminders.

Tie reading to an event rather than a clock time: **after your main meal, open the book before starting another leisure activity.** Keep it where you usually sit.

For each session, read for ten minutes. Aim for the gist; skip unfamiliar words unless they block your understanding.

1. **Day 1:** Put the book in place and read. Mark your stopping point.
2. **Day 2:** Use the meal cue and continue from your bookmark.
3. **Day 3:** Repeat. If starting feels difficult, commit to opening the book and reading one sentence first.
4. **Day 4:** Continue without trying to catch up on missed pages.
5. **Day 5:** Repeat. Move the book if its current location makes starting inconvenient.
6. **Day 6:** Keep the same ten-minute limit, even if you have extra time.
7. **Day 7:** Read, then review your record.

**Disrupted-day fallback:** At your next available pause, read for two minutes—or one paragraph if that is all you have. Resume normally tomorrow; no catch-up debt.

**Check whether it worked:** Record `10`, `fallback`, or `missed` each day. Your target is seven ten-minute sessions; count fallbacks separately. Also note whether starting became easier. If misses cluster around the meal cue, change the cue next week.

## Previous draft — turn one

Think of the last two times you missed language practice: did you forget, struggle to find time, or see the reminder but put it off?

That will help us choose something useful:

- **Forgot:** prioritize reliable reminders and a simple recurring task.
- **No time:** prioritize calendar scheduling and an easy way to move missed sessions.
- **Put it off:** prioritize a tiny daily target and accountability.

Which best matches what happened?

## Previous draft — turn two

Use your book and a scrap of paper. Aim for **ten minutes of Spanish reading each day**, with no fixed start time.

Put the book somewhere you already sit. Use finishing a meal as your first opportunity; bedtime is your backup.

1. **Day 1:** Read for ten minutes from wherever you are. Mark your place.
2. **Day 2:** Continue for ten minutes. Let unfamiliar words pass unless they block your understanding.
3. **Day 3:** Read for ten minutes. Afterwards, jot down which opportunity actually worked.
4. **Day 4:** Repeat that opportunity if available; otherwise use the next natural pause.
5. **Day 5:** Read for ten minutes. Start with a brief reread if it helps you settle in.
6. **Day 6:** Repeat. Keep the task to reading—no required vocabulary exercises.
7. **Day 7:** Read for ten minutes, then review your record.

**For disrupted days:** Read for two minutes, or one paragraph if that is all you can manage. Mark it as a fallback, separate from a full session. If you miss entirely, resume the next day without catching up.

**Check whether it worked:** Each day mark **10**, **fallback**, or **missed**. Set a trial target of five full sessions this week. Also note whether starting felt easier by day seven. If you fall short, use the record to adjust the reading opportunity before adding anything else.

## Revised core — turn one

What usually happens when you miss practice: **you forget, you can’t find time, or you see the reminder and put it off?**

That changes which kind of app I’d choose:

- **Forget:** a simple recurring reminder.
- **Can’t find time:** a calendar or task planner with a reserved practice slot.
- **Put it off:** a habit tracker with a small daily target and visible progress.

While choosing, try making the target five minutes after an existing routine, such as breakfast. That gives the app a specific habit to support.

## Revised core — turn two

Use your existing book and a scrap-paper bookmark. Aim for **ten minutes at the first usable quiet window**, wherever it falls in your day. Keep the book somewhere you naturally spend time.

| Day | Plan |
|---|---|
| 1 | Read for ten minutes. Start anywhere appropriate; record your ending page. |
| 2 | Continue for ten minutes. Read for the gist; let unfamiliar words pass unless they block understanding. |
| 3 | Read for ten minutes. Notice which available window was easiest to use. |
| 4 | Repeat that window if available; otherwise use the next opportunity. Read ten minutes. |
| 5 | Read for ten minutes. Finish by saying one sentence about the passage in Spanish. |
| 6 | Read for ten minutes. Continue forward without catching up on missed days. |
| 7 | Read for ten minutes, then review your record. |

**Fallback for disrupted days:** Read for two minutes, or one paragraph if that is all you can manage. Mark it as a fallback. If reading is impossible, mark a miss and resume the next day.

**Check whether it worked:** On the bookmark, record each day as **10 / fallback / missed**, plus the ending page. Five or more full sessions is a useful first-week target. Also check whether you can briefly describe what you read and whether the routine felt repeatable. Fallbacks show continuity; count them separately from ten-minute sessions.

## Review and limits

The selected continuation criteria were: use the corrected Spanish-reading objective; respect the existing book, zero budget, and no-app constraint; provide a seven-day plan; accommodate unpredictable days and provide a fallback; offer a check; ask no further questions; invent no reminder or cross-session memory capability. On author review, all four conditions met these selected criteria (4/4). None demonstrated a real week of follow-through. Proposed five-session or seven-session targets are planning choices, not empirically established success thresholds.

The first ordinary response assumed reminders would help before diagnosing the cause. The other conditions explored the cause earlier, with different amounts of guidance. These are observations from single samples, not reliable condition effects. The first-turn questions were not answered directly; instead every condition received the same goal correction. User effort and burden were not measured, and no timing comparison is available.

**Conclusion:** this check demonstrates feasible correction and plan generation in these four samples. It shows no incremental benefit from the revision, does not establish equivalence, and does not validate all seven elements. The eight new operating cases and the full 74-case specification suite were not run as model evaluations. Native installation, actual tool actions, persistent memory, security controls, cross-model behavior, real-user outcomes, and broad efficacy remain untested by this check.
