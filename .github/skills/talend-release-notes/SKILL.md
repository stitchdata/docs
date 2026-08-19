---
name: talend-release-notes
description: "Use when drafting or updating Talend monthly release notes in DITA. Enforces structure, metadata, file naming, and map integration across all release-note product areas in docs-core."
---

# Talend release-notes drafting

Use this skill to create or update Talend release notes in docs-core with consistent monthly structure across all products and subsystems.

## When to use

Invoke this skill when all of the following are true:
- The current repository is `docs-core`.
- The request is for Talend monthly release notes in `en/release-notes/`.

Use the following signals as supporting evidence:
- The request includes month keys like `RYYYY-MM`.
- The Jira `fixVersion` field includes a monthly value matching `RYYYY-MM` or `8.0.1-RYYYY-MM`.
- The request names one or more Talend release-note product areas.

### When to create release notes during documentation work

This skill also applies when **documenting any product change** (new features, notable fixes, deprecations, removals, or other updates) that warrants a release note entry. If the Jira task links to a product code issue (e.g., QTDM-*, TDP-*, etc.) marked Done, and the change introduces user-facing functionality or impacts product usage, create or update the corresponding monthly release note entry in addition to updating the product documentation. If the required monthly release-note files do not exist, create them as part of this work. Release notes are mandatory for product documentation work.

## Inputs

Supported product areas include:
- Monthly wrapper and highlights video (`RYYYY-MM_c.dita`, `RYYYY-MM-highlights-video_c.dita`).
- Talend Studio (`RYYYY-MM_studio_c.dita`, plus child topics such as `..._studio_new-features...`, `..._studio_notable-fixes...`, `..._studio_deprecated-removed-items...`).
- Talend Runtime (`RYYYY-MM_runtime_c.dita`).
- Talend Remote Engine (`RYYYY-MM_talend-remote-engine_c.dita`).
- Talend Dynamic Engine (`RYYYY-MM_dynamic-engine_c.dita` or existing month-specific variant).
- Talend Cloud Management Console (`RYYYY-MM_cloud-management-console_c.dita`).
- Talend Cloud API Designer (`RYYYY-MM_talend-cloud-api-designer_c.dita`).
- Talend Administration Center (`RYYYY-MM_administration-center_c.dita`).
- Talend Cloud Migration Toolkit (`RYYYY-MM-cloud-migration-toolkit_c.dita`).
- Installers and software requirements (`RYYYY-MM_installers_r.dita`, `RYYYY-MM_software-requirements_r.dita`).
- Talend Data Catalog wrapper and children (`RYYYY-MMcatalog81.dita`, `RYYYY-MM-talend-data-catalog-application81_r.dita`, `RYYYY-MM-talend-data-catalog-bridges81_r.dita`).

If the month is missing, use `[ASSUMED-MONTH]` in planning notes only, add an adjacent follow-up note, and ask for month confirmation before creating or renaming monthly files.

### Follow-up note placement (required)

When assumptions or missing data remain, write follow-up notes in the source DITA file being updated or created (not only in chat output).

- Place each follow-up note immediately next to the corresponding `[ASSUMED-*]` placeholder in the same paragraph, list item, or table cell.
- Each follow-up note must include the exact data required to replace that placeholder.
- If multiple release-note files are updated, add adjacent follow-up notes in each file that contains unresolved placeholders.

## Required outputs

Create or update only the product files requested for that month under `en/release-notes/` and update `en/maps-guides/release-notes-80.ditamap` when new monthly topics are introduced. If a required monthly release-note file does not exist yet, create it using the nearest existing month as the template pattern for the same product area. Do not skip a required release-note entry only because the target monthly file is missing.

The final output must include:
- The updated monthly release-note file set for requested product area(s).
- Any required update to `en/maps-guides/release-notes-80.ditamap` when new monthly topicrefs are added.
- In-source adjacent follow-up notes for all unresolved placeholders (`[ASSUMED-*]`) and the exact data needed to replace them.

For a new monthly product topic, ensure:
- File naming follows existing monthly patterns for that product area.
- Topic `id` and `pageid` are month-aligned and consistent with nearby months.
- Parent/child topicref placement matches the structure used by adjacent month entries.

When a month-level wrapper (`RYYYY-MM_c.dita`) or product parent topic for that month is missing, create the missing parent first, then add the child entry in the proper location.

## Procedure

### Step 1 - Collect source inputs

1. Read Jira source content for each release-note entry (summary, description, acceptance details, and relevant comments).
2. Read Jira `fixVersion` values and confirm the monthly key (`RYYYY-MM` or `8.0.1-RYYYY-MM`).
3. If source details are incomplete, keep wording conservative, add `[ASSUMED-DETAILS]`, and record required confirmations in an adjacent follow-up note.
4. If product-area targeting is unclear, add `[ASSUMED-PRODUCT-AREA]` and ask for confirmation before creating new product-specific files.

### Step 2 - Identify month and target section

1. Parse the target month in `RYYYY-MM` format.
2. Locate the month node in `en/maps-guides/release-notes-80.ditamap`.
3. Reuse the nearest existing month as the structural pattern when adding a new month or new product subsection.
4. If the month node is missing in the map, create the month wrapper and add its topicref in chronological position.
5. If the month exists but the required product topic or child topic does not, create the missing file and add its topicref under the correct month parent.

### Step 3 - Classify entries

Classify each item using the destination topic structure:
- If the target topic already has named sections (for example, New features for Talend Studio), place entries in the matching section.
- If the target topic is a general concept topic, integrate entries in its existing section model without forcing new section names.
- If creating a new table-based topic, use clear section/table headings aligned with existing product patterns for that month.

If classification is unclear, keep wording conservative and mark assumptions with `[ASSUMED-CLASSIFICATION]`.

Classification decision rules:
- Determine classification from the **nature of the product change** in the linked implementation
  ticket(s) and acceptance details, not from the Documentation Jira issue type.
- `new-features`:
  Use when the capability is additive or newly available to users.
  Typical cues: "now available", "new option", "support for", "can now".
  Issue-type hint: task/story items with additive user impact usually belong here.
- `notable-fixes`:
  Use when the entry restores expected behavior, corrects an error, or resolves a broken workflow.
  Typical cues: "issue fixed", "no longer fails", "workaround removed".
  Issue-type hint: bug/defect items with corrective user impact usually belong here.
- `deprecated-removed-items`:
  Use when the entry announces deprecation, end-of-support intent, or removal of a capability.
  Typical cues: "deprecated", "removed", "no longer supported", "replaced by".
  Issue-type hint: if functionality is deprecated or removed, classify here regardless of issue type.
- `known-issues` subsection:
  If an issue remains unresolved in the release and requires a workaround, place it in the known-issues
  portion of the notable-fixes/known-issues topic for that month.
- When uncertain, compare with the previous two monthly files in the same product area and follow
  the dominant pattern; if still ambiguous, add `[ASSUMED-CLASSIFICATION]` and record the missing confirmation in an adjacent follow-up note.

### Step 4 - Draft DITA topics

Draft according to the existing topic type for the product area:
- Use `<concept>` as the default topic type for release-note topics.
- When updating an existing release-note file that is already a `<reference>`, keep its current type unless a migration is explicitly requested.
- Keep section names and structure aligned with adjacent monthly files for the same product area.
- Keep content concise and user-focused.
- In all `<simpletable>` content, keep `<stentry>` content to direct text or inline elements only; do not use block elements such as `<p>` inside `<stentry>`.

#### Highlights video topic conventions

The highlights video topic (`RYYYY-MM-highlights-video_c.dita`) has a fixed structure identical every month. Copy the previous month's file content and update only:
- The topic `id` and `pageid` to the new month
- The Vidyard URL (two occurrences: `data` attribute in `<object>` and the thumbnail `<param>` value)

The user must supply the Vidyard URL for the new release. If not provided, use `[ASSUMED-VIDYARD-URL]` as a placeholder and record it in an adjacent follow-up note.

#### Talend Studio topics conventions

**Child topics**: The Talend Studio monthly entry (`_studio_c.dita`) can have the following child topics, in this order:
1. Software requirements (`_studio_software-requirements_r.dita`) — not always present
2. New features (`_studio_new-features_c.dita`)
3. Notable fixes and known issues (`_studio_notable-fixes-known-issues_c.dita`) — not always present
4. Deprecated and removed features (`_studio_deprecated-removed-items_c.dita`) — not always present

Create only the child topics relevant to the release. Always use an empty `<shortdesc/>` in child topics. Only populate it when a release has a single defining theme that affects all users (for example, a mandatory platform requirement). That is an exception, not the default. 

**Sections in child topics**: The standard section order is:
1. Shared features
2. Application Integration
3. Big Data
4. Continuous Integration
5. Data Integration
6. Data Mapper
7. Data Quality

Include only the sections that have entries for the release. Do not generate empty sections as placeholders.

**Writing guidelines — new features**

Each entry uses a two-column `<simpletable>` with headers `Feature` and `Description`.

- **Feature (first column)**: Use the following naming patterns:
  - New version or option supported: **Support for XXX (to XXX)** — e.g., "Support for Kafka version 3.2.x"
  - New functionality or check box: **New option (for XXX) to do XXX** — e.g., "New option for tFileInputExcel to customize the ratio between deflated and inflated bytes to detect zip bomb"
  - Enhancement of an existing item: **Enhancement of XXX to XXX** — e.g., "Enhancement of tFileInputDelimited to support dynamic schema in Spark Jobs"
  - For component-related features, list component names or family names depending on how many are affected — e.g., "New components to connect to Google Bigtable to store or retrieve data"
- **Description (second column)**: Answer the following questions, when applicable:
  - What does this new feature do?
  - Why is this new feature useful for the user?
- You can include a screenshot (with a red frame) using `<image>` inside a `<fig>`, and a link to a scenario if one exists.

**Writing guidelines — notable fixes and known issues**

This topic uses **two distinct `<simpletable>` elements**: one for notable fixes (`id="notable-fixes"`), one for known issues (`id="known-issues"`). Both use headers `Issue` and `Description`.

- **Issue (first column)**: Describe the issue only — do not explain how it is solved. Use the following naming patterns:
  - General issue: **Issue(s) when/with XXX** or **XXX when/with XXX** — e.g., "Issues when using a flattening map with EDI 834 documents", "Slow refresh of Job design when moving JDBC components in case of large database tables"
  - Job-related issue: **Job(s) fail(s) to XXX** or **XXX fail(s) to XXX** — e.g., "Jobs fail when tab characters are used as delimiters in CSV files"
  - Studio error message: do not copy the full message; use **An error occurs when/with XXX** — e.g., "An error occurs when tDBOutput receives data of FLOAT type from tDBInput through a dynamic column"
- **Description (second column)**: Answer the following questions, when applicable:
  - What was the issue?
  - How has it been fixed?
  - What is the workaround if it is not fixed yet (if any)?
- **Never link to a Jira ticket or filter.** Talend projects are private; external users cannot access them.

**Writing guidelines — deprecated and removed features**

This topic uses **two distinct `<simpletable>` elements**: one for deprecated features, one for removed features. Both use headers `Item` and `Description`.

- **Item (first column)**: Name of the deprecated or removed item.
- **Description (second column)**: Answer the following questions, when applicable:
  - What has been removed or deprecated?
  - Does the deprecation or removal apply to something specific only?
  - What is used instead of the removed or deprecated item?

**Writing guidelines - upcoming major changes**

Do not create a dedicated child topic for upcoming major changes. Instead, add a `<section>` at the end of the application parent topic (for example, `_studio_c.dita`). Do not use `<note type="warning">`; the section title is sufficient to signal importance. Do not use the phrase "breaking changes" in the title, but you may use it in the body text.

#### Talend Dynamic Engine topic conventions

The Dynamic Engine release-note topic is a single `<concept>` file (not split into child topics). Use a non-empty `<shortdesc>` summarizing the top 1–3 themes in one sentence.

Include only the sections that have content for the release, in this order:

1. `upcoming-changes` — forward-looking warnings for the next release; name the target release period in the section title (e.g., "Upcoming changes in R2026-08"); omit if none
2. `new-features` — `<simpletable>` with `Feature` and `Description` columns; one row per feature or release milestone; use `<codeph>` for version strings, keys, and commands
3. `maintenance-releases` — `<simpletable>` with `Release` and `Description` columns; link each row to its detailed changelog when one exists; omit if none
4. `known-limitations` — state the limitation, scope, and workaround together; prefer a two-column `<simpletable>` with `Impact scope` and `Workaround` when there are multiple entries; omit if none
5. `deprecated-and-removed-items` — same structure as `new-features`; if an item is removed without replacement, state that explicitly; omit if none

#### Talend Catalog conventions
- Use `<concept>` for `RYYYY-MMcatalog81.dita` wrapper.
- Keep `<shortdesc>` concise and aligned with existing monthly wrappers.
- Use `<concept>` for new `application81` and `bridges81` entries.
- When updating existing `application81` or `bridges81` files that are `<reference>`, keep their current type unless a migration is explicitly requested.

**Bridge naming standards**

- For import bridges, use the official bridge name only (for example, `Qlik Sense`, not `Qlik Sense import`).
- For export bridges, append `export` to the official bridge name (for example, `Erwin Data Modeler export`).
- Validate bridge names against Meta Integration Supported Tools: `https://metaintegration.net/Products/MIMB/SupportedTools.html`.

**Catalog entry structure**

- For both `application81` and `bridges81` topics, use two sections with two-column simple tables:
  - `New features and improvements` with headers `Feature` and `Description`.
  - `Notable fixes` with headers `Issue` and `Description`.
- Keep each description concise and specific; target short, user-focused entries.

**Catalog file naming and metadata patterns**

- Wrapper concept: `RYYYY-MMcatalog81.dita`
  - Topic `id`: `rYYYY-MMcatalog81`
  - `pageid`: `rYYYY-MM-catalog`
- Application reference: `RYYYY-MM-talend-data-catalog-application81_r.dita`
  - Topic `id`: `rYYYY-MM-talend-data-catalog-application81_r`
  - `pageid`: `rYYYY-MM-talend-data-catalog-application81`
- Bridges reference: `RYYYY-MM-talend-data-catalog-bridges81_r.dita`
  - Topic `id`: `rYYYY-MM-talend-data-catalog-bridges81_r`
  - `pageid`: `rYYYY-MM-talend-data-catalog-bridges81`

Follow adjacent monthly files for exact casing, delimiters, and conref usage when existing repository patterns differ.

### Step 5 - Apply naming and metadata rules

Validate:
- File names, topic `id`, and `pageid` follow monthly conventions.
- Existing taxonomy conrefs are preserved.
- Metadata is aligned with adjacent monthly topics.
- Product naming is consistent with established release-note wording (for example: Talend Studio, Talend Runtime, Talend Remote Engine).

### Step 6 - Update release-notes map

In `en/maps-guides/release-notes-80.ditamap`:
1. Locate `RYYYY-MM_c.dita`.
2. Insert new product topicrefs only when new files are created for that month.
3. Preserve product ordering and nesting based on adjacent months.
4. For Catalog additions, nest `application81` and `bridges81` under `RYYYY-MMcatalog81.dita`.
5. Preserve existing indentation and order.
6. If the month node does not exist, add it and include all newly created in-scope product topicrefs needed for the requested entry.

### Step 7 - Validate output

1. Invoke `qlik-writing-guidelines` for style and clarity checks.
2. Invoke `dita-markup-validation` to validate DITA structure.
3. Fix validation issues before final output.

## Constraints

- Do not invent unsupported features, version numbers, or issue details.
- Do not modify `en/archive-release-notes/`.
- Keep changes scoped to the requested release notes.
- Record unresolved details as specific placeholders in `[ASSUMED-*]` format with adjacent in-source follow-up notes.

## Completion checklist

- Target month and product area(s) identified.
- Only in-scope product files updated.
- Existing topic type and section model respected.
- Map updated only when new monthly topicrefs were added.
- `qlik-writing-guidelines` and `dita-markup-validation` invoked.
- Adjacent in-source follow-up notes are present for all unresolved `[ASSUMED-*]` placeholders.
