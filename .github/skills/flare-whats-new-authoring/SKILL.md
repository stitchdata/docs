---
name: flare-whats-new-authoring
description: "Use when: drafting Qlik Cloud What's new changelog entries in help-documentation for TLV tickets; selecting or creating the correct quarterly snippet; applying required conditions, date, title, description, and links."
---

# Flare What's New Authoring Skill

## Overview
Use this skill to add or update Qlik Cloud What's new changelog entries in the help-documentation repository for TLV tickets.

## When to Use
Use this skill only when all of the following conditions are true:
- The current repository is `help-documentation`.
- The primary Jira issue key starts with `TLV-`.
- The change is for Qlik Cloud. (Do not use this skill for Qlik Sense on Windows, QlikView, or product-specific changelogs outside Qlik Cloud.)

## Steps

### 1. Extract Source Text
  - Read the Jira What's New field: `fields.customfield_10478` (see `jira-context/references/jira-fields.md`).
  - If the What's New field is populated, use its content as the source to populate the changelog title and description.
  - If the What's New field is empty, use `[ASSUMED-TITLE]` and `[ASSUMED-DESCRIPTION]` placeholders and add a follow-up note in the agent output.

### 2. Extract Source Date
  - Read the Jira Due date field: `fields.duedate` (see `jira-context/references/jira-fields.md`).
  - If Jira Due date is populated, use it to determine the quarter and populate the changelog release date.
  - If Jira Due date is empty, use `[ASSUMED-DATE]` and add a follow-up note in the agent output.

### 3. Select Target Snippet File
  **Reference files**
  - Main changelog topic: `Content/Sense_Hub/Introduction/saas-change-log.htm`
  - Snippet folder: `Content/Resources/Snippets/WhatsNew/`

  **Decision**
  - If Jira Due date is populated:
    1. Determine `YYYY-QN` (`QN` = quarter: `Q1`-`Q4`).
    2. Use target file pattern: `whats-new-saas-YYYY-QN.flsnp`.
      - Example filename: `whats-new-saas-2026-Q3.flsnp`
      - Example snippetBlock format:
      `<MadCap:snippetBlock src="../../Resources/Snippets/WhatsNew/whats-new-saas-2026-Q3.flsnp"/>`
    3. If the file does not exist, create it and add a snippetBlock reference in `saas-change-log.htm` in newest-first order.
  - If Jira Due date is empty:
    1. Use the snippet file referenced by the first `MadCap:snippetBlock` element in `Content/Sense_Hub/Introduction/saas-change-log.htm`.

### 4. Draft and Insert the What's New Entry
  **Formatting**
  - Follow the formatting requirements in: `Content/EDL/HowTos/AddNewsItemChangelog.htm`

  **Required Elements**
  - Create a `<div class="news-item" ...>` with required conditions
  - Add an `<h2 MadCap:conditions="Targets.NotToTranslate">` element with release date (format: `MMMM D, YYYY`)
  - Add an `<h3>` title that follows  Qlik style guidelines
  - Add description paragraph(s)
  - Add one or more links to the most relevant help topics related to the new feature

  **Title and Description**
  - If the What's New field is populated:
    - Treat the Jira What's New field as the source of truth for the title and description.
    - Preserve the original wording unless changes are required to fix obvious errors, product naming issues, or Qlik style violations.
    - Use the first non-empty line as the `<h3>` title.
    - Use the remaining non-empty lines as description paragraph(s), in order.
    - If there is only one non-empty line, use it as the title and set the description to `[ASSUMED-DESCRIPTION]`.
  - If the What's New field is empty:
    - Use `[ASSUMED-TITLE]` as the `<h3>` title.
    - Use `[ASSUMED-DESCRIPTION]` as the description paragraph.
    - Add a follow-up note in the agent output that the Jira What's New field should be populated or confirmed.

  **Date and Placement**
  - If Jira Due date is populated:
    1. Use it for the release date heading.
    2. Insert entries in descending date order based on `<h2 MadCap:conditions="Targets.NotToTranslate">`.
  - If Jira Due date is empty:
    1. Use `[ASSUMED-DATE]` in the date heading.
    2. Place entries with `[ASSUMED-DATE]` at the top until the real date is available.
    3. Add a follow-up note in the agent output that Jira Due date should be populated or confirmed.

### 5. Apply Conditions on the `news-item` Div
  **Required conditions**
  - Exactly one `Cloud_Platform_Area.*`
  - One or more `Cloud_Platform_Category.*` when applicable
  - Optional `Cloud_Platform_Gov.*` only when needed

  **Selection guidance**
  - Use the condition names listed in `Content/EDL/HowTos/AddNewsItemChangelog.htm` for Area and Category selection.
  - Infer platform area and category from TLV context and related help topics.

## Output Requirements
The final output must include:
- Updated or created quarterly What's new snippet file
- Updated `saas-change-log.htm` snippetBlock list if a new quarter file was created
- Follow-up notes listing all `[ASSUMED-*]` placeholders
