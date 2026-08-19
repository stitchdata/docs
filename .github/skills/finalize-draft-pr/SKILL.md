---
name: finalize-draft-pr
description: "Commit documentation changes, mark the completed Copilot first draft, push to remote, create PR with reviewer assignment and alphahelp preview links in PR body, and post preview links to Jira. Use when: Draft-doc completes and user confirms draft ready, need to finalize documentation changes and create a PR for documentation review."
---

# Finalize Draft PR

Commits all documentation changes, creates a marker commit for the completed Copilot first draft, pushes to remote branch, creates a pull request with alphahelp preview URLs in the PR body, assigns reviewer automatically, and posts preview links to the DOC Jira ticket.

## When to Use

- After Draft-doc agent completes writing documentation
- When user confirms "draft is ready for review"
- As the final automated step before human review

## Prerequisites

**Required tools:**
- `create_file` or `replace_string_in_file` — Write modified files to local disk
- `run_in_terminal` — Execute local git commands (add, commit, push)
- `mcp_github_create_pull_request` — Create the PR on GitHub
- `mcp_github_update_pull_request` — Assign reviewers
- `mcp_jira_getJiraIssue` — Fetch DOC ticket details for reviewer assignment
- `mcp_jira_addCommentToJiraIssue` — Post comment to DOC ticket

**Authentication:**
- Git configured locally with credentials (or SSH key for git push)
- GitHub MCP server must have repository write access for PR creation
- Jira MCP server must have issue read and comment permissions

**Configuration:**
- `cloudId`: Jira site URL (e.g., `https://qlik-dev.atlassian.net`)
- `repo_owner`: GitHub repository owner (e.g., `qlik-trial`)
- `repo_name`: GitHub repository name (e.g., `help-documentation`)
- `base_branch`: Target branch for PR (default: `daily`)
- `repository_root`: Absolute path to repository root (e.g., `c:\src\help-documentation`)
- User mapping file: `references/user-mapping.json` — Maps Jira usernames to GitHub usernames
- URL construction reference: `references/alphahelp-url-construction.md` — Patterns for building alphahelp URLs

**Important:** This skill assumes a **local workflow** where files are written to disk and git operations are performed in the local repository. This ensures GitHub Desktop and local git state remain in sync.

## Procedure Overview

1. Prepare commit data
2. Write files to local disk, stage, commit, mark the completed first draft, and push to remote
   - Step 2a: Write modified files to disk
   - Step 2b: Stage and commit locally
   - Step 2c: Create the first-draft baseline marker
   - Step 2d: Push to remote branch
3. Construct alphahelp URLs (must be done before creating PR)
4. Create pull request with preview links in PR body
5. Assign reviewer from DOC ticket
6. Post preview links to Jira ticket
7. Return results

## Procedure

### Step 1 — Prepare commit data

Collect all changed files from Draft-doc output. Files should be provided as:

```json
{
  "files_changed": [
    {
      "path": "Content/Sense/Managing/DataConnections.htm",
      "content": "<full file content>"
    },
    {
      "path": "Content/Resources/Snippets/NewConnector.flsnp",
      "content": "<full file content>"
    }
  ]
}
```

**Validation:**
- Ensure all paths are relative to repository root
- Confirm all files have content (non-empty)

**Error handling:** If the file list is empty, verify whether the Draft-doc agent already committed the documentation changes. If the feature branch contains commits ahead of the base branch, continue to Step 2c. Otherwise, surface an error because there is no draft to finalize.

---

### Step 2a — Write modified files to local disk

For each file in the `files_changed` array, write the modified content to disk. The repository root path must be provided as input.

**For each file:**

1. Determine the absolute path: `{repository_root}\{relative_path}` (e.g., `c:\src\help-documentation\Content\Sense\Managing\DataConnections.htm`)
2. If the file already exists:
   - Use `replace_string_in_file` to update the content
   - Requires matching the old content exactly (including whitespace)
   - **Alternatively:** Use `create_file` with overwrite if `replace_string_in_file` cannot match reliably
3. If the file is new:
   - Use `create_file` to create it
4. Verify the file was written successfully (check file exists)

**Success criteria:** All modified files exist on disk with correct content.

**Error handling:**
- File not found (for replace): Surface error — file may have moved or been deleted
- Path invalid: Surface error — verify path is within repository
- Write permission denied: Surface error — check directory permissions
- Content mismatch (for replace): Surface error — content may have diverged locally; abort workflow

---

### Step 2b — Stage and commit changes locally

Use `run_in_terminal` to execute git commands in the repository root.

**Command sequence:**

```powershell
cd {repository_root}
git status
git add {relative_file_paths}
git commit -m "{commit_message}"
```

**Detailed steps:**

1. **Verify clean working state:**
   ```powershell
   cd c:\src\help-documentation
   git status
   ```
   Expected: Shows modified/untracked files OR shows clean working tree
   
   If uncommitted changes exist that shouldn't be committed, surface error and ask user to review

2. **Pull latest remote changes to avoid non-fast-forward push:**
   ```powershell
   git pull origin {branch_name}
   ```
   Expected: Local branch is up to date with the remote. If a merge conflict occurs, surface the error and ask the user to resolve it before continuing.

3. **Stage the specific files:**
   ```powershell
   git add "Content/Sense/Managing/DataConnections.htm"
   git add "Content/Resources/Snippets/NewConnector.flsnp"
   ```
   (One `git add` per file, or combine with spaces: `git add file1 file2 file3`)
   
   Expected: Files staged, ready for commit

4. **Commit with message:**
   ```powershell
   git commit -m "[DOC-1234] Update documentation for <feature-summary>" -m "- Updated DataConnections.htm with new connector details" -m "- Added snippet for connector configuration" -m "- Updated related topics"
   ```
   
   Expected: Commit created, shows commit SHA and file list

**Commit message format:**
- First line: `[<doc_ticket_key>] <brief summary from plan>`
- Blank line
- Bullet list of changed files with brief description

**Success criteria:** 
- `git status` shows clean working tree OR only unchanged tracked files
- `git log -1` shows the new commit with correct message
- Commit SHA is returned for tracking

**Error handling:**
- Nothing to commit: If the feature branch already contains documentation commits ahead of the base branch, continue to Step 2c. Otherwise, verify that files were written in Step 2a.
- Merge conflicts: Surface error — base branch may have diverged; ask user to manually rebase
- Author identity not configured: Surface error — user must configure `git config user.name` and `user.email`
- Commit failed: Surface full error message and stop

---

### Step 2c — Create the first-draft baseline marker

After all Copilot-generated documentation changes have been committed, create an empty commit to identify the completed first draft.

This commit establishes the baseline that can later be compared with the final writer-edited version. It must be created regardless of whether Copilot created zero, one, or several commits earlier in the workflow.

Before creating the marker, check whether the current branch already contains a commit with the exact `Initial-Draft-By: GitHub Copilot` trailer. If it does, do not create another marker.

**Command:**

```bash
git commit --allow-empty -m "[DOC-1234] Mark completed Copilot first draft" -m "Initial-Draft-By: GitHub Copilot"
```

**Commit message format:**

```text
[<doc_ticket_key>] Mark completed Copilot first draft

Initial-Draft-By: GitHub Copilot
```

**Important:**

- Use the exact trailer `Initial-Draft-By: GitHub Copilot`
- Create the marker only after all Copilot first-draft changes are committed
- Do not add documentation changes to the marker commit
- Create no more than one first-draft marker per feature branch

**Success criteria:**

- Exactly one first-draft marker exists in the feature branch commit range
- The marker contains the exact `Initial-Draft-By: GitHub Copilot` trailer
- `git rev-parse HEAD` returns the marker commit SHA when a new marker was
  created

**Error handling:**

- Marker already exists: Reuse the existing marker SHA and continue
- Marker creation failed: Surface the full Git error message and stop
- Multiple markers found: Surface an error and ask the user to review the
  branch history before continuing

---

### Step 2d — Push to remote branch

Use `run_in_terminal` to push the committed changes to the remote repository with upstream tracking, then fetch to sync local tracking info for GitHub Desktop.

**Commands:**

```powershell
git push -u origin {branch_name}
git fetch origin
```

Example:
```powershell
git push -u origin branch-qcs-DOC-1234-created-by-copilot
git fetch origin
```

**Why `-u` flag:** The `-u` (or `--set-upstream`) flag automatically configures the local branch to track the remote branch. This is essential for GitHub Desktop and other Git GUIs to recognize the branch as published.

**Why fetch after push:** The `git fetch` updates local tracking references and ensures all Git clients see the branch correctly.

**Success criteria:**
- `git push` completes successfully
- Remote branch is updated with the new commit
- `git fetch` updates local tracking references
- `git branch -vv` shows branch tracked correctly

**Error handling:**
- Authentication failed: Surface error — verify GitHub credentials/SSH key is configured
- Push rejected (branch not found): Surface error — ensure branch was created with correct name
- Push rejected (non-fast-forward): Surface error — base branch may have diverged; ask user to pull/rebase
- No commits to push: Surface error — verify that the marker commit was created or found in Step 2c
- Other errors: Surface full error message and stop

**Verification step (optional):**
After push, verify the remote has the commits:
```powershell
git log -1 origin/{branch_name}
```
Should show the same commit SHA as local `git log -1`

---

### Step 2 Summary

After completing steps 2a, 2b, 2c, and 2d:
- ✓ Modified files exist on local disk
- ✓ Files are staged and committed locally
- ✓ The completed Copilot first draft is identified by a marker commit
- ✓ Commit is pushed to remote branch
- ✓ Local tracking references are synced (git fetch)
- ✓ Local git state matches remote state
- ✓ GitHub Desktop and Git Extensions will show the branch as published correctly

---

### Step 3 — Construct alphahelp URLs for changed files

Build preview URLs for reviewers to access the documentation on alphahelp (internal staging environment).

**Important:** These URLs must be constructed before creating the PR (Step 4) so they can be included in the PR body at creation time.

#### Step 3a — Load URL construction reference

Read and follow the patterns in:
```
.github/skills/finalize-draft-pr/references/alphahelp-url-construction.md
```

This reference contains all URL construction logic:
- Repository detection (Flare vs DITA)
- Product code mappings
- Path transformation rules
- DITA mapid/pageid extraction
- Complete examples

**Apply the patterns from the reference file** to construct URLs for each changed file.

#### Step 3b — Filter and prioritize files

Generate URLs only for reviewable content files:

**Include:**
- `.htm` files (Flare topics)
- `.dita` files (DITA topics)

**Exclude:**
- Image files (`.png`, `.jpg`, `.svg`)
- Snippet files (`.flsnp`) — unless they're the only changes
- CSS/JS files
- Configuration files (`.flprj`, `.fltoc`, ditamap metadata)

**Prioritization:**
1. New files (added in the PR)
2. Files with substantial content changes
3. Main topic files over shared resources

**Limit:** If more than 10 files changed, include only the top 10 most significant files to avoid overwhelming the comment.

#### Step 3c — Handle edge cases

**Snippets only:**
- If only snippets changed, note: "Updated shared snippets (no direct preview URL)"
- Optionally identify which topics include those snippets

**Configuration/structure changes only:**
- Note: "Configuration changes only (no content URLs)"

**DITA mapid not found:**
- Mark URL as `[MAPID-NEEDED] - https://alphahelp.qliktech.com/talend/en-US/[MAPID]/{branch-name}/{pageid}`
- Flag for manual review

**Build not yet complete:**
- Note: "URLs will be available after Jenkins build completes (check #pcm_doc_build_status Slack channel)"

---

### Step 4 — Create pull request

**Important:** 
1. Verify that Steps 2a-2d (local git operations) have completed successfully
2. Verify that Step 3 (alphahelp URL construction) has completed successfully
3. The preview links from Step 3 must be included in the PR body at creation time

Use `mcp_github_create_pull_request` with:

| Parameter | Value |
|-----------|-------|
| `owner` | Repository owner |
| `repo` | Repository name |
| `title` | PR title (see format below) |
| `head` | Feature branch name (e.g., `branch-qcs-DOC-1234-created-by-copilot`) |
| `base` | Target branch (default: `daily`) |
| `body` | PR description (see format below) |
| `draft` | `false` (create as ready for review) |

**PR title format:**
```
[DOC-1234] Add documentation for Azure Blob Storage connector
```
- Format: `[<doc_ticket_key>] <plan summary>`
- Keep concise (under 100 characters if possible)

**PR body format:**
```markdown
## Documentation Update

**DOC Ticket:** [DOC-1234](https://qlik-dev.atlassian.net/browse/DOC-1234)
**Parent Ticket:** [TLV-5678](https://qlik-dev.atlassian.net/browse/TLV-5678)

### Summary

<Brief summary from plan — 2-3 sentences>

### Documentation Preview

Preview on alphahelp (after build completes):

- [{file1-display-name}]({alphahelp-url-1})
- [{file2-display-name}]({alphahelp-url-2})
- [{file3-display-name}]({alphahelp-url-3})

### Changes

- Updated DataConnections.htm with Azure Blob Storage connector details
- Added configuration snippet for authentication
- Updated table of supported connectors

### Branch Build Status

Check [#pcm_doc_build_status](https://qlikdev.slack.com/archives/CJSRZ6J2D) for build notifications.

**Archive pages:**
- [Flare branches archive](https://alphahelp.qliktech.com/rc/en-US/archive)
- [Talend branches listing](https://alphahelp.qliktech.com/talend/en-US/branches)

### Review Notes

<Any specific review guidance from plan or Draft-doc>

---
*This PR was created automatically by the documentation automation system.*
```

**Success criteria:** PR is created and returns PR number and URL.

**Error handling:**
- PR already exists: Check if existing PR is for same head/base; if so, return existing PR info and proceed to assignment
- Branch not found: Surface error — Step 2d may have failed; verify git push succeeded
- No commits on branch: Surface error — Step 2b may have failed; verify local commit succeeded
- Permission denied: Surface error — check GitHub MCP token permissions
- Other errors: Surface full error message and stop

---

### Step 5 — Assign reviewer from DOC ticket

Fetch DOC ticket assignee using `mcp_jira_getJiraIssue` with `fields=assignee`

#### Step 5a — Fetch DOC ticket assignee

Use `mcp_jira_getJiraIssue` with:

| Parameter | Value |
|-----------|-------|
| `cloudId` | Jira site URL |
| `issueIdOrKey` | DOC ticket key |
| `fields` | `["assignee"]` |

Extract `fields.assignee.displayName` and `fields.assignee.emailAddress` if available.

**Map Jira user to GitHub username:**
- If email is available, attempt to match to known GitHub username (via configuration or heuristic)
- Common pattern: Jira display name → GitHub username (lowercase, no spaces)
- Example: "Jane Doe" → `janedoe` or email `jane.doe@qlik.com` → `janedoe`

**Fallback:** If no assignee or mapping fails, ask user for reviewer username interactively.

**Check if assignee is PR creator:**
- Get the PR creator from the PR object returned in Step 4 (`pr.user.login`)
- If the mapped GitHub username matches the PR creator username, skip Step 5b (cannot assign review to self)
- If they differ, proceed with Step 5b

#### Step 5b — Assign reviewer to PR

**Note:** Skip this step if DOC ticket assignee is the same person as the PR creator (detected in Step 5a).

Use `mcp_github_update_pull_request` with:

| Parameter | Value |
|-----------|-------|
| `owner` | Repository owner |
| `repo` | Repository name |
| `pullNumber` | PR number from Step 4 |
| `reviewers` | `["<github_username>"]` |

**Success criteria:** Reviewer is assigned to the PR.

**Error handling:**
- User not found: Log warning, ask user to manually assign reviewer
- Permission denied: Log warning, PR created but reviewer not assigned
- Other errors: Log warning but don't fail workflow — PR is still usable

---

### Step 6 — Post comment to Jira DOC ticket

Post PR and preview links to the DOC Jira ticket for tracking purposes.

Use `mcp_jira_addCommentToJiraIssue` with:

| Parameter | Value |
|-----------|-------|
| `cloudId` | Jira site URL |
| `issueIdOrKey` | DOC ticket key (e.g., `DOC-1234`) |
| `commentBody` | Comment text (see format below) |
| `contentFormat` | `markdown` |

**Jira comment format (keep it simple):**
```markdown
Pull request: [PR #{pr_number}]({pr_url})

Preview on alphahelp:
* [{file1}]({url1})
* [{file2}]({url2})
* [{file3}]({url3})
```

**That's it.** Just PR link + alphahelp URLs. No extra formatting, no build notes, no automation disclaimer.

**Success criteria:** Comment is posted to Jira ticket.

**Error handling:**
- Permission denied: Log warning, inform user to manually post links
- Ticket not found: Log warning (ticket may have been moved/deleted)
- Other errors: Log warning but don't fail workflow

**Note:** Preview links are already included in the PR body (from Step 4), so no separate GitHub comment is needed.

---

### Step 7 — Return results

Return a structured result with:

```json
{
  "commit_sha": "abc123def456...",
  "files_committed": 3,
  "pr_number": 1234,
  "pr_url": "https://github.com/qlik-oss/help-documentation/pull/1234",
  "pr_title": "[DOC-1234] Add documentation for Azure Blob Storage connector",
  "reviewer_assigned": true,
  "reviewer_username": "janedoe",
  "alphahelp_urls": [
    {
      "file": "Content/Connectors/Azure/Configuration.htm",
      "url": "https://alphahelp.qliktech.com/rc/en-US/connectors-DOC-1234-azure-blob-rc/Content/Connectors/Azure/Configuration.htm"
    },
    {
      "file": "Content/Connectors/Azure/Authentication.htm",
      "url": "https://alphahelp.qliktech.com/rc/en-US/connectors-DOC-1234-azure-blob-rc/Content/Connectors/Azure/Authentication.htm"
    }
  ],
  "jira_comment_posted": true
}
```

Output a user-friendly summary:
```
✓ Documentation committed and pushed
  Files changed: 3
  Commit: abc123d
  Branch: branch-qcs-DOC-1234

✓ Pull request created: #1234
  Title: [DOC-1234] Add documentation for Azure Blob Storage connector
  Link: https://github.com/qlik-oss/help-documentation/pull/1234
  Preview links included in PR body
  
✓ Reviewer assigned: @janedoe
  (or "⚠ Reviewer not assigned: DOC ticket assignee is PR creator" if skipped)

✓ Preview link posted to Jira ticket DOC-1234

Preview documentation on alphahelp (after build completes):
  - https://alphahelp.qliktech.com/rc/en-US/connectors-DOC-1234-azure-blob-rc/Content/Connectors/Azure/Configuration.htm
  - https://alphahelp.qliktech.com/rc/en-US/connectors-DOC-1234-azure-blob-rc/Content/Connectors/Azure/Authentication.htm

Next steps:
- Wait for Jenkins build to complete (check #pcm_doc_build_status Slack channel)
- Preview the documentation on alphahelp
- Review the documentation in the PR
- Address any review comments
- Merge when approved
```

---

## Inputs

Required:
- `branch_name` (string) — Feature branch with documentation changes
- `files_changed` (array) — Array of objects with `path` and `content`
- `doc_ticket_key` (string) — DOC Jira ticket key (e.g., `DOC-1234`)
- `pr_title` (string) — Pull request title
- `cloudId` (string) — Jira site URL
- `repo_owner` (string) — GitHub repository owner
- `repo_name` (string) — GitHub repository name

Optional:
- `base_branch` (string) — Target branch (default: `daily`)
- `pr_body` (string) — Custom PR description (auto-generated if not provided)
- `commit_message` (string) — Custom commit message (auto-generated if not provided)
- `reviewer_override` (string) — GitHub username to assign (overrides Jira assignee)
- `draft_pr` (boolean) — Create as draft PR (default: false)

---

## Outputs

- `commit_sha` (string) — SHA of the commit created
- `files_committed` (number) — Count of files committed
- `pr_number` (number) — GitHub PR number
- `pr_url` (string) — Full URL to pull request
- `pr_title` (string) — PR title (echo)
- `reviewer_assigned` (boolean) — Whether reviewer assignment succeeded
- `reviewer_username` (string) — GitHub username of assigned reviewer
- `alphahelp_urls` (array) — List of preview URLs with file paths
- `comments_posted` (object) — Status of comments posted to Jira

---

## Notes

- **Atomic operation:** Commit and push happen together; if push fails, commit is not created on remote
- **First-draft marker:** The workflow creates one empty marker commit after all Copilot first-draft changes have been committed
- **Reviewer mapping:** Requires configuration or heuristic to map Jira users to GitHub usernames
- **Self-assignment prevention:** If DOC ticket assignee is the same person as the PR creator, reviewer assignment is skipped (cannot assign review to self)
- **PR ready state:** PR is created as "ready for review" by default (not draft)
- **Alphahelp URLs:** Preview links are constructed automatically based on repository type (Flare or DITA) and branch naming conventions
- **Automated comments:** Preview links are posted to the Jira DOC ticket; the GitHub PR includes preview links in the PR body to facilitate review
- **Build dependency:** Preview URLs won't work until Jenkins completes the branch build; reviewers should wait for build notifications

---

## Reviewer Assignment Strategies

**Priority order:**
1. Use `reviewer_override` if provided (manual override)
2. Get assignee from DOC Jira ticket
3. Check if assignee is the same as PR creator → skip if same (cannot assign to self)
4. Map Jira user to GitHub username (via configuration)
5. Ask user interactively if mapping fails

**Mapping configuration example:**
```json
{
  "jira_to_github": {
    "jane.doe@qlik.com": "janedoe",
    "john.smith@qlik.com": "jsmith",
    "alice.jones@qlik.com": "ajones"
  }
}
```

**Interactive fallback:**
If no assignee or mapping fails, use `vscode_askQuestions` tool:
```
Question: "Who should review this PR?"
Options: [List of common documentation reviewers]
```

---

## Error Recovery

**If commit/push fails:**
1. Check branch exists and is up to date
2. Verify GitHub token has push permissions
3. Check for merge conflicts (may need to sync base branch)
4. Verify file paths are valid and within repository

**If PR creation fails:**
1. Check if PR already exists for this branch
2. Verify head branch has commits ahead of base branch
3. Check repository settings allow PR creation

**If reviewer assignment fails:**
1. Manually assign reviewer in GitHub UI
2. Update Jira-to-GitHub username mapping
3. Consider using team assignment instead of individual

**If alphahelp URL construction fails:**
1. Verify branch naming follows conventions (see git-branch-creation skill)
2. Check if product code mapping exists in reference file
3. For DITA: Verify ditamap references the changed topic
4. Fall back to posting generic build status links (archive/listing pages)

**If comment posting fails:**
1. Verify Jira and GitHub authentication/permissions
2. Manually post preview links to Jira and PR
3. Check comment format is valid (markdown for Jira, markdown for GitHub)

---

## Local vs. Remote Workflows

### Local Workflow (Writers trigger from VS Code)

**Use steps 2a-2d as documented above.**

- Agents provide modified file content in responses
- Files are written to local disk
- Git operations are performed locally (add → commit → mark baseline → push)
- Local git state syncs with remote state
- GitHub Desktop shows commits and branch state correctly
- Writers can verify changes before merge
- Works seamlessly with PR creation and review

**Advantages:**
- ✓ Local git state matches remote state
- ✓ GitHub Desktop integration works correctly
- ✓ Writers have full control and visibility
- ✓ Can manually modify before push if needed
- ✓ Supports offline workflows (push later)

### Remote Workflow (Service Account, Future)

**Alternative approach using `mcp_github_push_files`** (for v2 or service account automation):

When deployed as a remote service (e.g., GitHub Actions, scheduled job, external CI/CD):
- No local git state to maintain
- Use `mcp_github_push_files` to commit directly to remote via GitHub API
- No need to execute local git commands
- Atomicity guaranteed by GitHub API
- Works for fully-automated, no-human-intervention scenarios

**Advantages for remote deployment:**
- ✓ No local file I/O required
- ✓ No git command execution needed
- ✓ Single atomic operation via API
- ✓ Works from any runtime environment (containers, cloud, etc.)

**Note:** Current implementation prioritizes **local workflows** (writers manually trigger) because it's the immediate need. Remote workflows can be added as V2 with conditional logic that detects the execution context.

---

## Future Enhancements

**V1 (Current - Local Workflows):**
- ✅ Local file I/O with create_file / replace_string_in_file
- ✅ Local git operations (add → commit → mark baseline → push)
- ✅ Completed Copilot first-draft baseline marker
- ✅ GitHub MCP for PR creation and reviewer assignment
- ✅ Alphahelp preview URL construction
- ✅ Automated comments to Jira with preview links

**V2 Enhancements (planned or ideas):**
- **Remote workflow support:** Conditional logic to detect execution context (local vs. remote); use `mcp_github_push_files` for remote deployments
- **Team assignment:** Assign to GitHub team instead of individual
- **Labels:** Auto-apply labels to PR based on affected files or Jira labels
- **Build status integration:** Wait for Jenkins build completion before posting URLs (with timeout)
- **Screenshot capture:** Automatically capture screenshots of changed pages for visual review
- **Component map URLs:** Support for docs-components standard/mediation map patterns
