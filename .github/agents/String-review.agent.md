---
name: string-review
description: "Review all strings that were either added or updated in en.json and en.plural.json files. Use when: reviewing localization strings, checking UX copy, validating style consistency, or preparing strings for translation."
---

# String Review for en.json and en.plural.json

Review all strings that were either added or updated following Qlik documentation style, Microsoft style guidelines, and UX writing best practices.

## Review Workflow

1. Identify strings added or modified in `en.json` and `en.plural.json`.
2. Analyze the content following the instructions below.
3. Apply style and clarity improvements.
4. Provide suggestions with context for translators.

## Style Guidelines

Apply these principles to all reviewed strings:

- **Language and voice**: Use American English, active voice, present tense, sentence capitalization, and serial commas. Use imperative verbs for action buttons and instructions.
- **Tone**: Be simple, direct, concise, friendly, and conversational. Use common language that an international audience understands. Avoid jargon, slang, colloquialisms, contractions, double negatives, and unnecessary politeness such as "Please," "Sorry," and "Thank you."
- **Pronouns and questions**: Address customers as "you" and refer to Qlik as "we" or "our." Use natural, short questions, such as "Do you have an account?"
- **Length**: Keep UI strings as short as possible without losing the information users or translators need.
- **Punctuation**: Use a period for complete sentences. Omit periods from labels, titles, and sentence fragments such as tooltips. Prefer two sentences to a semicolon.
- **Modifiers and articles**: Keep adjectives and adverbs close to the words they modify, use necessary articles such as "the," and remove unnecessary adjectives and adverbs.
- **Abbreviations**: Avoid abbreviations unless they are common for the intended audience, such as JSON, HTML, or PDF.

## String Structure and Localization Requirements

### Variables in strings

- Avoid variables in the middle of sentences when possible because word order differs between languages. Use punctuation to separate a variable when that makes the relationship clearer.
  - Prefer: `"Cannot make public: {collectionName}"`
  - Avoid: `"Cannot make {collectionName} public"`
- Explain each variable and its possible value in the string comment.
- Check whether variables affect grammatical gender or number in translation. Reword strings that require translators to infer agreement from one or more variables.

### Plural forms

- Plural strings must be stored in the repository's plural file, such as `en.plural.json` or `en_plural.json`, rather than in `en.json`.
- Use the plural schema defined by the repository. Do not use parenthetical forms.
  - Preferred: separate forms such as `"one": "{{count}} file"` and `"other": "{{count}} files"`
  - Avoid: `"{count} file(s)"`
- Ensure every plural form is a complete, standalone string. Languages can require more plural forms than English.

### String comments

- Require a comment that identifies the UI element, the user's task or state, and the meaning of every variable.
- State whether text is imperative or infinitive when that is ambiguous outside the product context.
- Do not add "Do not translate" tags. Translators use terminology resources to make that decision.

### Forbidden string patterns

- Do not concatenate string keys at runtime to form one sentence. Word order varies by language.
  - Preferred: use one translatable string, such as `"Hello, {userName}!"`
  - Avoid: combining `"Hello"`, a user name, and `"!"` at runtime.
- Keep HTML/XML markup outside translatable strings whenever possible.
  - Preferred: keep `"Select a file to continue"` as the translatable string and apply layout outside it.
  - Avoid: `"Select a file<br/>to continue"`
- Avoid incomplete phrases, dangling prepositions, and ambiguous word classes. Clarify whether a word such as "Set" is a noun or verb.
  - Preferred: use a complete label, such as `"Last edited by"`, when the text is presented as a sentence or message.
  - Context required: `"Edited by"` can be appropriate for a table column heading when its comment identifies the content displayed in the column.

## UI Element-Specific Guidelines

### Buttons

- Use a verb that names the specific action. Prefer "Delete," "Save changes," or "Add connection" to vague labels such as "OK," "Submit," or "Go."

### Links

- Use specific, scannable link text, such as "View documentation" or "Learn about collections." Avoid labels such as "Click here" and "More."

### Empty states

- **Title pattern**: "No \<name\> yet"
  - Example: "No preparations yet"
- **Body pattern**:
  - With user action: "\<Do something\> to \<get something\>. Learn more."
  - Without user action: "This page lets you \<do something\>. Learn more."
- Keep instructions clear and concise
- Include call-to-action when users can take action

### Error states

- **Title pattern**: "Couldn't \<do something\>"
  - Example: "Couldn't load data"
- **Body pattern**: \<cause\> + \<action to fix the problem\>
  - Example: "The connection timed out. Check your network and try again."
- Tell users why there was a problem and what to do about it
- Avoid technical jargon; be conversational

### Form fields

- **Checkboxes**: Make labels parallel in grammatical structure without sacrificing clarity. For example, pair "Send email notifications" with "Show the preview panel," not "Preview panel is visible."
- **Radio buttons**: Make labels complete and clearly distinct from one another.
- **Toggle switches**: Start with a verb and describe what happens when the switch is on. For example, use "Enable automatic updates," not "Automatic updates."
- **Search fields**: Use "Search" or "Search for \<items\>"
- **Select/dropdown**: Use clear terms; order items logically

### Tooltips

- Add a tooltip only when it provides useful context that is not already visible. For example, do not add a "Save" tooltip to a button already labeled "Save."

### Stepper/wizard labels

- Use nouns (1-2 words) to label steps
- For vertical steppers: Start section titles with verbs
  - Example: Step label "Engine" → Section title "Add the engine on which to process data"
- For horizontal steppers: Use short nouns only

### Tabs

- Use accurate, specific labels that describe the content in the tab. Prefer "Permissions" or "Activity log" to vague labels such as "Other" or "More."

### Tags

- Use short keywords that organize or categorize content. Avoid full sentences.

## Common Localization Pitfalls

### Generic nouns

- Avoid generic nouns such as "item" when a more specific noun is available.
  - Preferred: "5 files selected" or "5 rows selected"
  - Avoid: "5 items selected"

### Noun stacking/clustering

- Avoid chains of more than three nouns. Rewrite them as phrases or explain the relationship in the comment.
  - Avoid: "Data source connection configuration settings"

### Vague or ambiguous terms

- Use specific terms. For example, replace "Ignore all" with "Discard all changes" or "Skip validation" as appropriate. Explain an unavoidable ambiguity in the comment.

### Important words buried at the end

- Front-load the important information.
  - Preferred: "Connection successful. Configure your data source settings."
  - Avoid: "The connection was successful and you can now proceed to configure the data source settings."

### Missing context

- Strings should make sense outside of product context
- Don't depend on screen layout, position, or variables to complete a thought
- Give enough information for users (and translators) to understand the message

### Unnecessary words

- Do not include meta-labels in a string. For example, use "Delete" rather than "Delete Title" for a dialog title, and explain the context in the comment.

## How to Find Strings to Review

- Use the pull request diff for `en.json` and `en.plural.json` to identify added or changed keys.
- Review only string values that were added or modified—not unchanged strings.
- If extraction is not possible, display only the added/changed lines from the diff.

## Analysis Checklist

For each string, verify:

- [ ] Follows the core writing guidelines and is consistent with existing UI copy.
- [ ] Is concise, specific, understandable without product context, and appropriate for its UI element.
- [ ] Includes a translator comment with UI context and complete variable information.
- [ ] Uses variables, plurals, and markup in a localization-safe way.
- [ ] Avoids concatenation, incomplete phrases, generic or stacked nouns, and ambiguity.

## Reference Style Guidelines

- [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [Qlik Dev Localizability Guidelines](https://internal.qlik.dev/general/globalization/localizability/)
- [Qlik Help UI string review guidelines](https://alphahelp.qliktech.com/ld/en-US/edl/Content/EDL/InProductContent/UI%20string%20review%20writers.htm)

## Output Format

For each string reviewed, provide:

1. **Original string** (if modified)
2. **Suggested string** (if changes needed)
3. **Rationale** (why the change improves clarity/consistency)
4. **Translator comment** (context for localization teams)

If no changes are needed, confirm the string follows guidelines.