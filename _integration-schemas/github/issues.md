---
tap: "github"
# version: ""

name: "issues"
doc-link: https://developer.github.com/v3/issues/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/issues.json
description: |
  The `issues` table contains info about repository issues.


replication-method: "Incremental"
api-method:
  name: "listIssuesForRepository"
  doc-link: https://developer.github.com/v3/issues/#list-issues-for-a-repository

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""
---
