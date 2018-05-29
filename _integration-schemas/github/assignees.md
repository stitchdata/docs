---
tap: "github"
# version: ""

name: "commits"
doc-link:
singer-schema:
description: |
  The `commits` table contains info about repository commits in a project.

replication-method: "Incremental"
api-method:
  name:
  doc-link:

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
