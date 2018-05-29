---
tap: "github"
# version: ""

name: "reviews"
doc-link:
singer-schema:
description: |

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "integer"
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

  - name: "body"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "commit_id"
    type: "string"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "pull_request_url"
    type: "string"
    description: ""
---
