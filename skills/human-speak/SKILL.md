---
name: human-speak
description: Edit, audit, or draft writing to remove recognizable AI phrasing and structural habits while preserving the writer's meaning and personal voice. Use when the user asks to humanize writing, remove AI slop, make copy sound natural, audit a draft for AI patterns, or invokes human-speak.
metadata:
  short-description: Make AI writing sound direct and human
  version: "1.1.0"
---

# Human Speak

Make writing sound like a specific person with something real to say. Remove canned AI patterns without replacing the writer's voice with generic polished prose.

The user's instructions take precedence over this skill. Respect requested tone, format, length, and intentional stylistic choices.

## Choose the job

**Edit is the default.** Rewrite the supplied draft using the minimum effective changes. Return the full edited draft followed by a short **What changed** section. If the user asks for clean copy only, omit the notes.

**Audit.** When the user asks to audit, scan, flag, or detect patterns without rewriting, name each pattern found, quote the smallest useful excerpt, and give a short fix. Do not score the writing, guess whether AI wrote it, or rewrite the draft unless asked.

**Draft.** When the user asks for new writing, apply the same rules while matching the supplied voice, source material, and format. Do not invent facts, experiences, quotes, numbers, or opinions.

## Before working

Read [references/patterns.md](references/patterns.md) for the complete pattern and phrase library.

When the user asks for the strongest giveaways or a prioritized checklist, use [references/top-20.md](references/top-20.md). Its order is editorial guidance, not an authorship detector.

Read the entire draft or source before changing it. Identify:

- the point the reader should understand or act on
- the writer's vocabulary, cadence, bluntness, humor, uncertainty, and level of polish
- details that must survive, including names, numbers, examples, mechanisms, and opinions

If no draft or usable source is provided, ask for it. For a new draft, proceed when the topic and purpose are clear. Ask one concise question only when the missing audience, format, or intended outcome would materially change the result.

## Editing rules

- Preserve meaning. Never add unsupported claims or make the writer sound more certain than the source.
- Preserve voice. Keep distinctive vocabulary, humor, bluntness, admissions, fragments, digressions, and rough edges when they feel intentional.
- Make the minimum effective edit. Leave strong human sentences alone.
- Lead with the point when setup adds nothing. Keep personal setup when it creates context, tension, or character.
- Prefer concrete facts, actions, mechanisms, consequences, names, and numbers over abstract importance.
- Use direct verbs and active voice when clearer. Do not force every sentence into the same rhythm.
- Repeat the correct word when it improves clarity. Do not rotate synonyms merely to avoid repetition.
- Do not narrate the reader's reaction or announce that a point is important. Make the evidence carry the emphasis.
- Avoid em dashes by default. Do not use emojis unless the user requests them or the existing voice clearly relies on them.
- Preserve the requested structure unless it is creating the problem. Explain meaningful reorganization in **What changed**.

## Finish

After an edit or new draft, check the result against [references/evaluation.md](references/evaluation.md). Fix failures before returning the answer.

Check sentence and paragraph shapes as well as exact phrases. Rewording a tee-up, contrast, or negative fragment does not remove the pattern. Rewrite the underlying thought as a direct sentence, then check again.

For an audit, return only evidence-backed findings. If no listed pattern appears, say so plainly. Do not manufacture findings to make the audit look useful.
