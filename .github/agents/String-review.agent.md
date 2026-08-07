---
name: string-review
description: "Review all strings that were either added or updated in en.json and en.plural.json files. Use when: reviewing localization strings, checking UX copy, validating style consistency, or preparing strings for translation."
---

# String Review for en.json and en.plural.json

Review all strings that were either added or updated following Qlik documentation style, Microsoft style guidelines, and UX writing best practices.

## Review Workflow

1. Analyze the content following the instructions below.
2. Identify strings added or modified in `en.json` and `en.plural.json`.
3. Apply style and clarity improvements.
4. Provide suggestions with context for translators.

## Style Guidelines

Apply these principles to all reviewed strings:

- **Language**: American English, active voice (use passive only when action is more important than subject)
- **Tone**: Simple, direct, concise. Friendly and conversational.
- **Vocabulary**: Common, everyday language for international audiences.
- **Capitalization**: Sentence case; avoid jargon.
- **Verb forms**: Present tense. Use simple forms for past/future when needed.
- **Questions**: Short forms (e.g., "Don't have an account?" not "Do you not have an account?")
- **Plurals**: Use plural forms; avoid parenthetical plurals (use "objects" not "object(s)")
- **Politeness**: Avoid "Please," "Sorry," "Thank you" in UI strings—they reduce clarity and directness.
- **Pronouns**: Use second person (you) for customers; first-person plural (we, our) for the company.

## How to Find Strings to Review

- Use the pull request diff for `en.json` and `en.plural.json` to identify added or changed keys.
- Review only string values that were added or modified—not unchanged strings.
- If extraction is not possible, display only the added/changed lines from the diff.

## Analysis Checklist

For each string, verify:

- [ ] Follows Qlik documentation style (precise verbs, minimal words, active voice)
- [ ] Follows Microsoft style guidelines (sentence case, click usage, etc.)
- [ ] Clarity for international audiences (no idioms, slang, or contractions in labels)
- [ ] Comment is clear for translators (purpose, usage, variable values)
- [ ] Concise and direct (no wordy phrasing)
- [ ] Present tense (or simple past/future when appropriate)
- [ ] Consistent with existing UI copy in the product

## Reference Style Guidelines

- [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [Qlik Help Documentation](https://help.qlik.com/en-US/)

## Output Format

For each string reviewed, provide:

1. **Original string** (if modified)
2. **Suggested string** (if changes needed)
3. **Rationale** (why the change improves clarity/consistency)
4. **Translator comment** (context for localization teams)

If no changes are needed, confirm the string follows guidelines.