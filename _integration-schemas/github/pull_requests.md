---
tap: "github"
# version: ""

name: "pull_requests"
doc-link:
singer-schema:
description: |

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "number"
    type: "integer"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "user"
    type: "object"
    description: ""

    object-attributes:
    - name: "login"
      type: "string"
      description: ""

    - name: "id"
      type: "integer"
      description: ""

  - name: "merged_at"
    type: "string"
    description: ""

  - name: "closed_at"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""
---
