---
name: markdown-markup-validation
description: "Use when: validating Markdown output for Qlik Help content, including standard Markdown, Markdig styling, images, links, and embedded HTML."
---

# Markdown Markup Validation Skill

Use this skill to validate Markdown source for Qlik Help content. The build uses Markdig with repository-specific styling extensions. Apply `qlik-writing-guidelines` separately for writing, accessibility, localization, and naming.

## YAML Front Matter

- Start each topic with a YAML front-matter block delimited by `---` on its own first and closing lines.
- Preserve the fields and values of an existing topic unless the change requires an update.
- For a new topic, copy the front matter from a nearby topic in the same guide. Most guides use `title`, `description`, `categories`, `hidden`, `isApi`, `qlik-products`, `persona`, and `topics`; legacy data-integration topics use only the applicable taxonomy lists.
- Use YAML lists for multiple `qlik-products`, `persona`, or `topics` values. Keep Boolean values as `True` or `False`.
- Quote a scalar value when it contains YAML-significant characters, such as `:`, `#`, `{`, or `}`.

## Validate

- Use a single level-one heading for the topic title. Do not skip heading levels.
- Escape Markdown punctuation with `\` when it must be literal. Use a blank line for a new paragraph and `<br/>` only for a forced line break.
- Use `**bold**`, `_italic_`, and backticks for inline code. Use matching fenced code blocks for multi-line code.
- Use consistent list markers and indent nested list items. Ordered lists can use `1.` for every item; Markdig numbers them automatically.
- Use Markdown tables with a header row and alignment delimiter row. Keep the number of cells consistent across rows.
- Use forward slashes in local paths. Internal published-topic links use paths such as `/Content/cloud-platform/topic.htm`; external links use full `https://` URLs and `{target=_blank class=see-also-link-external}`.
- Give images meaningful alternative text. Use `alt=""` only for decorative images.

## Markdig Styling

- Add an inline style with `::text::{class=style-name}`.
- Add a block style with a matching `:::{class=style-name}` opening delimiter and `:::` closing delimiter on their own lines. Use this for note, tip, and warning blocks.
- Add a block attribute directly after the paragraph it styles, for example `Introduction text.{class=introduction}`.
- Use a matching `^^^Caption` opening delimiter and `^^^` closing delimiter for a figure containing a Markdown image.
- Keep attributes in balanced braces and place them directly after the element they modify.
- Do not create, add, or edit `data-mc-conditions` or `mc-data-conditions` feature-condition markup. Flag any existing feature-condition markup for the content owner to resolve.

## Embedded HTML

- Use embedded HTML only when Markdown or a Markdig extension cannot produce the required output.
- Ensure HTML tags and comments are balanced, correctly nested, and use quoted attribute values.