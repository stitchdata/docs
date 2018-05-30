---
tap: "github"
# version: ""

name: "collaborators"
doc-link: https://developer.github.com/v3/repos/collaborators/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/collaborators.json
description: |
  The `collaborators` table contains info about

replication-method: "Full Table"
api-method:
  name: "listCollaborators"
  doc-link: https://developer.github.com/v3/repos/collaborators/#list-collaborators

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
