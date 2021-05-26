---
tap: "github"
version: "1"
key: "issue-milestone"

name: "issue_milestones"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/issue_milestones.json"
description: |
  The `{{ table.name }}` table contains info about issue milestones for the repositories specified in the integration.

replication-method: "Key-based Incremental"

api-method:
  name: "List milestones"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-milestones"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The issue milestone ID."
    foreign-key-id: "issue-milestone-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "closed_at"
    type: "date-time"
    description: ""

  - name: "closed_issues"
    type: "number"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "creator"
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

  - name: "description"
    type: "string"
    description: ""

  - name: "due_on"
    type: "date-time"
    description: ""

  - name: "html_url"
    type: "string"
    description: ""

  - name: "labels_url"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "number"
    type: "number"
    description: ""

  - name: "open_issues"
    type: "number"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---