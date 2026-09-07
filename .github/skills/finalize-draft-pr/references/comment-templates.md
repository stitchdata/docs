# PR and Jira Comment Templates

Templates for automated comments posted by the finalize-draft-pr skill.

---

## GitHub PR Comment Template

Use this template when posting comments to GitHub pull requests with `mcp_github_add_issue_comment`.

**Format:** Markdown

```markdown
## Documentation Preview

Preview the updated documentation on alphahelp (after build completes):

- [{page1-title}]({alphahelp-url-1})
- [{page2-title}]({alphahelp-url-2})
- [{page3-title}]({alphahelp-url-3})

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
| `{page1-title}` | Title displayed on the rendered page | `Creating analytics and visualizing data` |
| `{alphahelp-url-1}` | Full alphahelp URL for the file | `https://alphahelp.qliktech.com/rc/en-US/...` |
| `{brief-summary-from-plan-or-commit-message}` | 1-3 sentence summary of changes | "Added documentation for new Azure Blob Storage connector configuration options including authentication methods and connection string parameters." |

### Preview Link Label Format

Use the title displayed on the rendered page as each link label. Do not use a file name, path, topic ID, or page ID.

- For DITA, resolve the topic's `<title>`, including referenced variables.
- For Flare, use the title displayed as the page heading.
- Preserve the title's capitalization and product names.
- If the title cannot be resolved, flag it for manual review.

---

## Notes

- **Limit URLs:** If more than 10 files changed, include only the top 10 most significant files
- **Build timing:** Always include note about waiting for Jenkins build to complete
- **Archive links:** Provide both Flare and Talend archive pages for convenience
- **Changes summary:** Use the PR description or commit message summary (1-3 sentences max)
