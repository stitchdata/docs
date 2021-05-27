---
tap: "github"
version: "1"
key: "issue-event"

name: "issue_events"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/issue_events.json"
description: |
  The `{{ table.name }}` table contains info about issue events in the repositories specified for the integration.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "`updated_at` if non-NULL; otherwise `created_at`"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

api-method:
  name: "List issue events for a repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-issue-events-for-a-repository"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The issue event ID."
    # foreign-key-id: "issue-event-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "actor"
    type: "object"
    description: ""
    subattributes: &user-attributes
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
        type: "integer"
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

  - name: "assignee"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "assigner"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "commit_id"
    type: "string"
    description: ""
    foreign-key-id: "commit-id"

  - name: "commit_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "event"
    type: "string"
    description: ""

  - name: "issue"
    type: "object"
    description: ""
    subattributes:
      - name: "active_lock_reason"
        type: "string"
        description: ""

      - name: "assignee"
        type: "object"
        description: ""
        subattributes: *user-attributes

      - name: "assignees"
        type: "array"
        description: ""
        subattributes: *user-attributes

      - name: "author_association"
        type: "string"
        description: ""

      - name: "body"
        type: "string"
        description: ""

      - name: "closed_at"
        type: "date-time"
        description: ""

      - name: "comments"
        type: "integer"
        description: ""

      - name: "comments_url"
        type: "string"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "events_url"
        type: "string"
        description: ""

      - name: "html_url"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "issue-id"

      - name: "labels"
        type: "array"
        description: ""
        subattributes:
          - name: "color"
            type: "string"
            description: ""

          - name: "default"
            type: "boolean"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "label-id"

          - name: "name"
            type: "string"
            description: ""

          - name: "node_id"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "labels_url"
        type: "string"
        description: ""

      - name: "locked"
        type: "boolean"
        description: ""

      - name: "milestone"
        type: "object"
        description: ""
        subattributes:
          - name: "closed_at"
            type: "string"
            description: ""

          - name: "closed_issues"
            type: "integer"
            description: ""

          - name: "created_at"
            type: "date-time"
            description: ""

          - name: "creator"
            type: "object"
            description: ""
            subattributes: *user-attributes

          - name: "description"
            type: "string"
            description: ""

          - name: "due_on"
            type: "date-time"
            description: ""

          - name: "html_url"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "milestone-id"

          - name: "labels_url"
            type: "string"
            description: ""

          - name: "node_id"
            type: "string"
            description: ""

          - name: "number"
            type: "integer"
            description: ""

          - name: "open_issues"
            type: "integer"
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

      - name: "node_id"
        type: "string"
        description: ""

      - name: "number"
        type: "integer"
        description: ""

      - name: "performed_via_github_app"
        type: "string"
        description: ""

      - name: "pull_request"
        type: "object"
        description: ""
        subattributes:
          - name: "diff_url"
            type: "string"
            description: ""

          - name: "html_url"
            type: "string"
            description: ""

          - name: "patch_url"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "repository_url"
        type: "string"
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

      - name: "user"
        type: "object"
        description: ""
        subattributes: *user-attributes

  - name: "label"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "performed_via_github_app"
    type: "string"
    description: ""

  - name: "rename"
    type: "object"
    description: ""
    subattributes:
      - name: "from"
        type: "string"
        description: ""

      - name: "to"
        type: "string"
        description: ""

  - name: "requested_reviewer"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "review_requester"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "url"
    type: "string"
    description: ""
---