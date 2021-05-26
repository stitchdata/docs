---
tap: "github"
version: "1"
key: "stargazer"

name: "stargazers"
doc-link: https://developer.github.com/v3/activity/starring/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/stargazers.json
description: |
  The `{{ table.name }}` table contains info about users who have starred a repository.

replication-method: "Key-based Incremental"

api-method:
  name: "List stargazers"
  doc-link: "https://docs.github.com/en/rest/reference/activity#list-stargazers"

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
    subattributes:
      - name: "id"
        type: "integer"
        description: "The user ID."
---
