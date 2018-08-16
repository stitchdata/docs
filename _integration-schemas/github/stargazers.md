---
tap: "github"
# version: ""

name: "stargazers"
doc-link: https://developer.github.com/v3/activity/starring/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/stargazers.json
description: |
  The `stargazers` table contains info about users who have starred a repository.

replication-method: "Key-based Incremental"

api-method:
  name: "listStargazers"
  doc-link: https://developer.github.com/v3/activity/starring/#list-stargazers

attributes:
  - name: "user_id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    # foreign-key-id: "stargazer-id"

  - name: "starred_at"
    type: "string"
    replication-key: true
    description: "The time the user starred the repository."

  - name: "user"
    type: "object"
    description: "Details about the user who starred the repository."
    object-attributes:
      - name: "id"
        type: "integer"
        description: "The user ID."
---
