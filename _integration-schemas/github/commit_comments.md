---
tap: "github"
version: "1"
key: "commit-comment"

name: "commit_comments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/commit_comments.json"
description: |
  The `{{ table.name }}` table contains info about the commit comments in the repositories specified for the integration.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

api-method:
  name: "List commit comments for a repository"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-commit-comments-for-a-repository"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The commit comment ID."
    foreign-key-id: "commit-comment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "commit_id"
    type: "string"
    description: ""
    foreign-key-id: "commit-id"

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "line"
    type: "number"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: ""

  - name: "position"
    type: "number"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    subattributes:
      - name: "avatar_url"
        type: "string"
        description: ""

      - name: "events_url"
        type: "string"
        description: ""

      - name: "followers_url"
        type: "string"
        description: ""

      - name: "following_url"
        type: "string"
        description: ""

      - name: "gists_url"
        type: "string"
        description: ""

      - name: "gravatar_id"
        type: "string"
        description: ""

      - name: "html_url"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""

      - name: "login"
        type: "string"
        description: ""

      - name: "node_id"
        type: "string"
        description: ""

      - name: "organizations_url"
        type: "string"
        description: ""

      - name: "received_events_url"
        type: "string"
        description: ""

      - name: "repos_url"
        type: "string"
        description: ""

      - name: "site_admin"
        type: "boolean"
        description: ""

      - name: "starred_url"
        type: "string"
        description: ""

      - name: "subscriptions_url"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""
---