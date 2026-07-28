---
name: github-pr-analysis
description: "Analyze GitHub pull requests to understand product changes for documentation planning. Use when: you have PR URLs from Jira or direct input, need to understand code/UI changes, want to identify affected features, or must draft docs based on a merged or open PR. Reads PR metadata, diffs, and source files to extract documentation-relevant details."
---

# GitHub PR analysis

## Prerequisites

**Required tools:**
- `mcp_github_search_pull_requests` — Search for PRs by Jira issue key (Step 1)
- `mcp_github_pull_request_read` — Fetch PR metadata, diffs, files, and check runs (Steps 2–4)
- `list_pull_request_files` — Get list of changed files with stats (Step 3)
- `get_file_contents` — Fetch full file content for key files (Step 4)

**Authentication:**
- GitHub MCP server must have valid GitHub token with read access to repos across `Talend`, `qlik-trial`, and `qlik-all` organizations
- No special admin permissions needed; standard read access sufficient

**Scope & searchable organizations:**
This skill searches PR titles only in these GitHub organizations:
- `https://github.com/Talend/`
- `https://github.com/qlik-trial/`
- `https://github.com/qlik-all/`

**Input format:**
Provide either:
- **Single Jira issue key** (e.g., `TLV-825`)
- **List of Jira issue keys** (e.g., QTUP-4018, QTUP-4162, QTUP-4170)
- **Direct PR URL** (e.g., `https://github.com/qlik-trial/data-quality-rules/pull/784`)

**Limitations:**
- Search only matches PR **title** — if Jira key is in PR body/comments only, you must provide the PR URL directly
- PR search is limited to 18 results per query (GitHub API); use direct URL if specific PR is not in top results
- Large PRs (>50 files) may require selective file focus to keep analysis scoped

## Procedure

### Step 1 — Identify PRs to analyze

When provided with a Jira issue key, use `mcp_github_search_pull_requests` to search for matching PR titles across these organizations:

- `Talend`
- `qlik-trial`
- `qlik-all`

If multiple Jira issue keys are provided, search PR titles for each key independently, then merge and deduplicate results.
Extract PR URLs from the search results for analysis in subsequent steps. 
If the search returns no results and you have a direct PR URL, proceed to Step 2.

### Step 2 — Fetch PR metadata

For each PR URL, extract `owner`, `repo`, and `pull_number` from the URL pattern (example: `https://github.com/qlik/cloud-services/pull/4567` → owner: `qlik`, repo: `cloud-services`, pull: `4567`). Then retrieve the following PR metadata using `mcp_github_pull_request_read`:

| Field | Purpose |
|-------|---------|
| `title` | Short description of the change |
| `body` | Full PR description (often contains user stories, context, screenshots) |
| `state` | open, closed, merged |
| `merged` | Boolean: was this PR merged? |
| `created_at` | When the PR was opened |
| `merged_at` | When it was merged (if applicable) |
| `user.login` | Author username |
| `base.ref` | Target branch (e.g., `main`, `develop`) |
| `head.ref` | Source branch (often contains ticket ID or feature name) |
| `labels` | Tags that may indicate feature area or risk level |

### Step 3 — Read the diff summary

Fetch the list of changed files with diff statistics:
- Use `list_pull_request_files` and for each file, note:
  - File path
  - Number of additions/deletions
  - Change type (added, modified, deleted, renamed)

Categorize files by relevance to documentation:

| File type | Doc relevance | Example |
|-----------|---------------|---------|
| UI components, pages, forms | **High** | `src/components/Dashboard.tsx` |
| API routes, controllers, schemas | **High** | `api/routes/data-sources.js` |
| Configuration files | **Medium** | `config/feature-flags.yaml` |
| Tests, mocks | **Low** (but may reveal use cases) | `tests/auth.spec.ts` |
| Build scripts, CI configs | **Very low** | `.github/workflows/build.yml` |

Focus detailed reading on high-relevance files in Step 4.

### Step 4 — Read source files for key changes

For each high-relevance file identified in Step 3:

1. **Read the diff/patch** first:
   - Look for new functions, classes, API endpoints, UI labels, error messages.
   - Identify removed features (deletions).

2. **Fetch the full file content** if the diff alone is insufficient:
   - Use `get_file_contents` with the PR's head ref to see the new version.
   - Use the base ref to see the old version if needed for comparison.

3. **Extract documentation-relevant elements**:
   - New API endpoints: method, path, parameters, response shape
   - New UI elements: labels, tooltips, dialog titles, button text
   - Configuration changes: new settings, environment variables, permissions
   - Error messages or validation rules
   - Feature flags or conditional behavior

### Step 5 — Identify product change patterns

Classify the type of change based on file analysis:

| Pattern | Indicators | Doc impact |
|---------|------------|------------|
| **New feature** | New files, new routes, new UI screens | Create new topic |
| **Feature enhancement** | Modified existing components, extended API | Update existing topic |
| **Deprecation** | Deleted files, `@deprecated` tags in code | Add deprecation notice, update migration guide |
| **Bug fix** | Test files, targeted fixes in existing logic | Usually no doc change; check if the bug was publicly documented |
| **UI text/label change** | Changes to string literals in UI code | Update screenshots, UI labels in topics |
| **Configuration change** | New env vars, deployment settings | Update admin/configuration topics |
| **API change (breaking)** | Modified signatures, removed endpoints | Update API reference, add migration note |
| **API change (additive)** | New optional parameters, new endpoints | Update API reference |

### Step 6 — Synthesize product change summary

Output a structured summary for each PR:

**PR: [title]**
- **URL**: [PR URL]
- **Status**: [merged_at date] or [state]
- **Author**: [user.login]
- **Branch**: [head.ref] → [base.ref]

**Change type**: [classification from Step 4]

**Key changes**:
- [Bullet list of notable changes extracted from files]
- Include new API endpoints with method + path
- Include new UI screens or dialogs
- Include new configuration parameters
- Note any deletions or deprecations

**Affected features/areas**:
- [Identify which product features or modules are impacted]

**Documentation notes**:
- [Specific elements that must appear in docs: parameters, values, labels, workflows]
- [Ambiguities or missing context flagged as `[ASSUMED-*]` items]

## Decision notes

- If a PR is still open (not merged), flag it as "Not yet merged — documentation is tentative."
- If the PR description links to design docs, mockups, or Figma files, note these as supplementary context sources.
- Avoid reading every file in large PRs. Focus on files with the highest doc relevance first (Step 3).
- Test files often reveal use cases, edge cases, and error handling. Skim them if the main source files lack clarity.
- PR comments may contain clarifications or decisions made during code review. Check the comments thread if the description or diff is unclear.
- For PRs with more than 50 changed files, analyze the most documentation-relevant files first and clearly state that the review is scoped unless the user requests exhaustive analysis.
- Some PRs are purely refactoring or internal changes. If no user-facing behavior changes, state "No documentation impact detected."

## Error handling

| Scenario | Action |
|----------|--------|
| PR URL is invalid | Verify the format and ask user to correct |
| PR is private and inaccessible | Check GitHub token permissions or ask user for access |
| 404 on PR or repo | Confirm owner/repo/number are correct; PR may have been deleted |
| File content unavailable | Note which files could not be read and continue with available data |

## Output format

Deliver one **product change summary** (Step 6) per PR analyzed. If analyzing multiple PRs, group summaries under a heading like "Analysis of linked PRs".

The output from this skill feeds directly into the documentation planning phase (answering design review questions and deciding which topics to update/create) or directly into the Draft agent for implementation.
