# PR and Jira Comment Templates

Templates for automated comments posted by the finalize-draft-pr skill.

---

## GitHub PR Comment Template

Use this template when posting comments to GitHub pull requests with `mcp_github_add_issue_comment`.

**Format:** Markdown

```markdown
## Documentation Preview

Preview the updated documentation on alphahelp (after build completes):

- [{file1-display-name}]({alphahelp-url-1})
- [{file2-display-name}]({alphahelp-url-2})
- [{file3-display-name}]({alphahelp-url-3})

### Changes Summary

{brief-summary-from-plan-or-commit-message}

### Branch Build Status

Check the [#pcm_doc_build_status](https://qlikdev.slack.com/archives/CJSRZ6J2D) Slack channel for build notifications.

**Archive pages:**
- [Flare branches archive](https://alphahelp.qliktech.com/rc/en-US/archive)
- [Talend branches listing](https://alphahelp.qliktech.com/talend/en-US/branches)

---

_This comment was posted automatically by the documentation automation system._
```

### Template Variables

| Variable | Description | Example |
|---|---|---|
| `{file1-display-name}` | Relative path from `Content/` (Flare) or feature folder (DITA) | `Sense_Hub/Introduction/creating-analytics.htm` |
| `{alphahelp-url-1}` | Full alphahelp URL for the file | `https://alphahelp.qliktech.com/rc/en-US/...` |
| `{brief-summary-from-plan-or-commit-message}` | 1-3 sentence summary of changes | "Added documentation for new Azure Blob Storage connector configuration options including authentication methods and connection string parameters." |

### File Display Name Format

Keep display names concise and readable:
- Use relative paths that make sense to reviewers
- Omit `Content/` prefix for clarity
- Keep folder context when helpful
- Examples:
  - `Connectors/Azure/Configuration.htm`
  - `engines/configure-docker-registry.dita`
  - `Introduction/creating-analytics.htm`

---

## Notes

- **Limit URLs:** If more than 10 files changed, include only the top 10 most significant files
- **Build timing:** Always include note about waiting for Jenkins build to complete
- **Archive links:** Provide both Flare and Talend archive pages for convenience
- **Changes summary:** Use the PR description or commit message summary (1-3 sentences max)
