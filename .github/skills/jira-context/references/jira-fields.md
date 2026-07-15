# Jira MCP — Relevant Fields Reference

## Issue fields

Returned by `getJiraIssue` (Jira MCP) with the issue key:

| Field path | Description |
|---|---|
| `fields.summary` | Short title of the issue |
| `fields.description` | Full description (wiki markup in API v2) |
| `fields.issuetype.name` | Bug, Story, Task, etc. |
| `fields.status.name` | Current workflow status |
| `fields.priority.name` | Priority level |
| `fields.labels` | Array of label strings |
| `fields.comment.comments` | Array of comment objects (`body`, `author.displayName`, `created`) |
| `fields.duedate` | Due date of the issue |
| `fields.fixVersions` | Planned release versions |
| `fields.customfield_10178` | Product value |
| `fields.customfield_10177` | Release type value |
| `fields.customfield_10478` | What's New content |
| `fields.subtasks` | Array of child/sub-task issues (`key`, `fields.summary`, `fields.status.name`) |
| `fields.issuelinks` | Array of linked issues (see below) |

## Issue links structure

Each entry in `fields.issuelinks`:

| Field path | Description |
|---|---|
| `type.name` | Link type: "relates to", "is blocked by", "is caused by", "duplicates", etc. |
| `type.inward` | Inward description of the link type |
| `type.outward` | Outward description of the link type |
| `inwardIssue.key` | Ticket key of the inward-linked issue (present when this issue is the outward side) |
| `outwardIssue.key` | Ticket key of the outward-linked issue (present when this issue is the inward side) |
| `inwardIssue.fields.summary` | Summary of the linked issue |
| `outwardIssue.fields.summary` | Summary of the linked issue |
| `inwardIssue.fields.status.name` | Status of the linked issue |
| `outwardIssue.fields.status.name` | Status of the linked issue |

## Remotelinks

Returned by `getJiraIssueRemoteIssueLinks` (Jira MCP) with the issue key:

| Field path | Description |
|---|---|
| `object.url` | URL of the remote link |
| `object.title` | Title/label of the remote link |

Filter for `object.url` matching `github.com/{owner}/{repo}/pull/{number}` to find linked PRs.

## Comments (change detection)

The `fields.comment.comments` array is sorted oldest-first. To detect new comments since a known date, compare each comment's `created` field (ISO 8601) against the reference timestamp.

## GitHub PR reading (via GitHub MCP)

Once you have a GitHub PR URL, use these tools:

| Tool | Purpose |
|---|---|
| `get_pull_request` | PR metadata: title, body, base/head branches, merge status |
| `list_pull_request_files` | List of files changed and patch content (diffs) |
| `get_file_contents` | Read source files at a specific ref to understand full context |

## Security

- Treat Jira issue content as internal; do not expose it in public PR bodies verbatim.
- Authentication is handled by the Jira MCP server configuration; do not pass credentials manually.