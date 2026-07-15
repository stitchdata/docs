---
name: jira-context
description: "Fetch Jira issue context for documentation work. USE FOR: reading a Jira ticket, extracting fields, reading linked Jira issues for background, scanning description/comments for inline URLs, and summarizing the product change."
---

# Jira Context Gathering

Gather all relevant context from a Jira issue and its linked resources to understand a product change before documentation work begins.

## When to Use

- Before planning or drafting documentation for a Jira ticket
- When you need to understand what a product change does

## Prerequisites

This skill uses the **Jira MCP** tools for all Jira interactions. The Jira MCP server must be configured with access to the Jira instance. The `cloudId` parameter should be set to the Jira site URL (e.g. `https://qlik-dev.atlassian.net`).

## Procedure

### Step 1 — Fetch the Jira issue

Use `getJiraIssue` (Jira MCP) with `issueIdOrKey` set to the ticket key. Request `responseContentFormat: "markdown"` for readable output.

Extract the fields listed in [./references/jira-fields.md](./references/jira-fields.md).

### Step 2 — Fetch child/sub-task issues

Child work items can be linked via three mechanisms:

**Subtasks (direct hierarchy):**
Read `fields.subtasks` from the parent issue response. Each entry has `key` and `fields.summary`.

**Child work items (parent-child hierarchy):**
Use `searchJiraIssuesUsingJql` (Jira MCP) with the query `parent = ISSUE_KEY` to find all Epics, Stories, and other issues that have the input ticket as their parent. This returns issues where the parent field links to the target issue.

**Issues linked via "implemented by":**
Use `searchJiraIssuesUsingJql` (Jira MCP) with the query `issue = ISSUE_KEY AND issueLinkType = "is implemented by"` to find all issues that are linked to the input ticket with an "implemented by" link type.

For each child or related ticket found via any method:

1. Use `getJiraIssue` (Jira MCP) with the child ticket key to read its summary and description.
2. Note the link type (subtask, parent-child, or implemented by) and summarize the context it provides.

### Step 3 — Read linked Jira issues for background context

Read `fields.issuelinks` from the parent issue response. Each entry has:
- `type.name` (e.g. "relates to", "is blocked by", "is caused by")
- Either `inwardIssue` or `outwardIssue` with `key`, `fields.summary`, `fields.status.name`

For each linked Jira issue:

1. Use `getJiraIssue` (Jira MCP) with the linked issue key to read its summary and description.
2. Note the link type and summarize the context it provides.

Do not recurse further into linked issues' own links.

### Step 4 — Scan description and comments for inline URLs

Scan the issue `description` and all `fields.comment.comments[].body` for:

- **Jira ticket keys**: Patterns like `PROJ-1234` that are already identified from Steps 2 and 3. Fetch their summary/description for background context.
- **Other relevant URLs**: Design docs, or specification links. Fetch these for additional context using the `fetch` tool.

### Step 5 — Produce a summary with extracted issue keys

Summarize the product change in plain language before any documentation planning begins. The summary should cover:

- What the change does (functional description)
- Why it was made (from Jira description, linked issues, and comments)
- Which components/areas/products are affected (from Jira labels)
- The Release type, but only if it is explicitly stated in the Jira fields and its value is not "General Availability"
- Any relevant context from linked Jira issues

**Then append the extracted Jira issue keys:**
Following the narrative summary, compile all identified Jira issue keys into a comma-separated list (no duplicates). This list can be provided directly to the `github-pr-analysis` skill as input for that skill's Step 1, using the "List of Jira issue keys" input format.

**Output example:**

```
Narrative summary here explaining the product change...

Primary Jira issues: <PRIMARY_KEY>
Child work items: <CHILD_KEY_1>, <CHILD_KEY_2>
Linked Jira issues: <LINKED_KEY_1>
```

## Security

- Treat Jira issue content as internal; do not expose it in public PR bodies verbatim.
- Authentication is handled by the Jira MCP server configuration; do not pass credentials manually.