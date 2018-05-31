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
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The assignee ID."

  - name: "login"
    type: "string"
    description: "The user's username."

  - name: "type"
    type: "string"
    description: "The user's type."

  - name: "url"
    type: "string"
    description: "The profile URL associated with the user."
---
