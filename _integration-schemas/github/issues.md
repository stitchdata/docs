---
tap: "github"
version: "1"
key: "id"

name: "issues"
doc-link: https://developer.github.com/v3/issues/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/issues.json
description: |
  The `issues` table contains info about repository issues.

  #### Issues and pull requests

  GitHub's API considers every pull request an issue, but not every issue may be a pull request. Therefore, this table may contain both issues and pull requests.

replication-method: "Key-based Incremental"

api-method:
  name: "List issues for repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-repository-issues"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The issue ID."
    foreign-key-id: "issue-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the issue was updated."
---
