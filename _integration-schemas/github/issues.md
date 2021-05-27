---
tap: "github"
version: "1"
key: "id"

name: "issues"
doc-link: https://developer.github.com/v3/issues/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/issues.json
description: |
  The `{{ table.name }}` table contains info about issues in the repositories specified for the integration.

  #### Issues and pull requests

  GitHub's API considers every pull request an issue, but not every issue may be a pull request. Therefore, this table may contain both issues and pull requests.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

api-method:
  name: "List issues for repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-repository-issues"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The issue ID."
    foreign-key-id: "issue-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "assignee"
    type: "object"
    description: ""

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
        foreign-key-id: "issue-label-id"

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

  - name: "node_id"
    type: "string"
    description: ""

  - name: "number"
    type: "integer"
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
    description: "The last time the issue was updated."

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

---