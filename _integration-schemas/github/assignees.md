---
tap: "github"
# version: ""

name: "assignees"
doc-link: https://developer.github.com/v3/issues/assignees/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/assignees.json
description: |
  The `assignees` table contains info about the available assignees for issues in a repository.

replication-method: "Full Table"
api-method:
  name: "listAssignees"
  doc-link: https://developer.github.com/v3/issues/assignees/#list-assignees

attributes:
  - name: "login"
    type: "string"
    description: ""

  - name: "id"
    type: "integer"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---
