---
tap: "github"
# version: ""

name: "stargazers"
doc-link: https://developer.github.com/v3/activity/starring/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/stargazers.json
description: |
  The `stargazers` table contains info about a repository's stars.

replication-method: "Incremental"
api-method:
  name: "listStargazers"
  doc-link: https://developer.github.com/v3/activity/starring/#list-stargazers

  - name: "user"
    type: "object"
    description: ""
    object-attributes:
    - name: "id"
      type: "integer"
      description: ""

  - name: "starred_at"
    type: "string"
    description: ""

  - name: "user_id"
    type: "integer"
    description: ""
---
