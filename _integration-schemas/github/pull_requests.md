---
tap: "github"
# version: ""

name: "pull_requests"
doc-link: https://developer.github.com/v3/pulls/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/pull_requests.json
description: |
  The `pull_requests` table contains info about pull requests made against the repository.


replication-method: "Full Table"
api-method:
  name: "listPullRequests"
  doc-link: https://developer.github.com/v3/pulls/#list-pull-requests

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
