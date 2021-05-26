---
tap: "github"
version: "1"
key: "pull-request-review"

name: "pull_request_reviews"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/pull_request_reviews.json"
description: |
  The `{{ table.name }}` table contains info about pull request reviews in repositories specified for the integration.

  **Note**: In order to replicate this table, you must also set the [`pull_requests`](#pull_requests) table to replicate.

replication-method: "Key-based Incremental"

api-method:
  name: "List reviews for a pull request"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-reviews-for-a-pull-request"

attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The pull request review ID."
    foreign-key-id: "pull-request-review-id"

  - name: "_links"
    type: "object"
    description: ""
    subattributes:
      - name: "html"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "pull_request"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "commit_id"
    type: "string"
    description: ""
    foreign-key-id: "commit-id"

  - name: "html_url"
    type: "string"
    description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "pull_request_url"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "submitted_at"
    type: "date-time"
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