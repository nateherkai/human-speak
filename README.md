# Human Speak

Remove recognizable AI writing patterns without flattening the writer's voice.

Human Speak edits, audits, and drafts writing that sounds direct, specific, and natural. It catches canned insight framing, fake reveals, dramatic fragments, vague authority, inflated buzzwords, reaction narration, recap endings, and other patterns that make AI-assisted writing sound interchangeable.

It also protects the parts many editing prompts erase: vocabulary, cadence, bluntness, humor, uncertainty, digressions, and useful imperfections.

## Install the skill

The simplest cross-platform installation uses the open skills installer:

```sh
npx skills add nateherkai/human-speak --skill human-speak --global --yes
```

You can also ask Claude or Codex:

```text
Install the human-speak skill globally from https://github.com/nateherkai/human-speak
```

### Claude Code plugin installation

```text
/plugin marketplace add nateherkai/human-speak
/plugin install human-speak@human-speak
```

Claude Code namespaces plugin skills, so the plugin form is available as `/human-speak:human-speak`. Use the standalone skill installation above when you want the shorter `/human-speak` command.

### Codex

After installation, invoke the skill as `$human-speak`. Codex uses `$skill-name` syntax rather than slash commands.

## Use it

### Edit a draft

```text
/human-speak

[paste draft]
```

Human Speak returns the edited draft and a short explanation of what changed. Ask for "clean copy only" when you do not want the notes.

### Audit without rewriting

```text
/human-speak audit this without rewriting:

[paste draft]
```

The audit names each pattern, quotes the evidence, and gives a short fix. It does not guess whether AI wrote the text.

### Draft new copy

```text
/human-speak write a LinkedIn post from these notes in my voice:

[paste notes]
```

## What it catches

- Secret-insight framing such as "What nobody tells you"
- Tee-ups such as "Here's where it gets crazy"
- Binary reframes such as "It's not X. It's Y."
- Mechanical three-beat rhythms and dramatic fragments
- Fake rhetorical questions and colon reveals
- Superficial analysis using "highlighting" or "underscoring"
- Importance puffery and unsupported consensus claims
- Generic filler, empty adverbs, and inflated buzzwords
- Reaction narration after facts and statistics
- Fake-profound and recap endings
- Formatting habits such as decorative bold, unnecessary headings, emojis, and em dashes

The full catalog lives in [`patterns.md`](skills/human-speak/references/patterns.md).

## Repository structure

```text
.codex-plugin/plugin.json
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
skills/human-speak/SKILL.md
skills/human-speak/references/patterns.md
skills/human-speak/references/evaluation.md
```

## Development

Run the package checks:

```sh
python scripts/validate_package.py
```

For Claude Code, you can also run:

```sh
claude plugin validate .
claude --plugin-dir .
```

## Attribution

Human Speak began as Nate Herk's personal AI Phrase Kill List and incorporates ideas from Peter Yang's MIT-licensed [No AI Slop](https://github.com/petergyang/no-ai-slop) skill. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## License

MIT
