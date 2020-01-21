---
tap: "github"
version: "1"

name: "comments"
doc-link: https://developer.github.com/v3/comments/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/comments.json
description: |
  The `comments` table contains info about comments made on issues.

replication-method: "Key-based Incremental"

api-method:
  name: "List comments on a pull request"
  doc-link: https://developer.github.com/v3/pulls/comments/#list-comments-on-a-pull-request

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The comment ID."
    # foreign-key-id: "comment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the comment was last updated."

  # - name: "author_association"
  #   type: "string"
  #   description: ""

  - name: "body"
    type: "string"
    description: "The body of the comment."

  - name: "created_at"
    type: "date-time"
    description: "The time the comment was created."

  - name: "home_url"
    type: "string"
    description: "The home URL of the comment."

  - name: "html_url"
    type: "string"
    description: "The HTML URL of the comment."

  - name: "issue_url"
    type: "string"
    description: "The URL of the issue associated with the comment."

  - name: "node_id"
    type: "string"
    description: "The node ID."

  - name: "url"
    type: "string"
    description: "The GitHub URL of the comment."

  - name: "user"
    type: "object"
    description: "Details about the user who created the comment."
    subattributes:
      - name: "login"
        type: "string"
        description: "The login name of the user who created the comment."

      - name: "id"
        type: "string"
        description: "The ID of the user who created the comment."

      - name: "node_id"
        type: "string"
        description: "The node ID of the user who created the comment."

      - name: "avatar_url"
        type: "string"
        description: "The URL of the avatar of the user who created the comment."

      - name: "gravatar_id"
        type: "string"
        description: "The URL of the Gravatar of the user who created the comment."

      - name: "url"
        type: "string"
        description: "The API URL of the user who created the comment."

      - name: "html_url"
        type: "string"
        description: "The GitHub URL of the user who created the comment."

      - name: "followers_url"
        type: "string"
        description: "The URL to the user's followers page."

      - name: "following_url"
        type: "string"
        description: "The URL to the user's following page."

      - name: "gists_url"
        type: "string"
        description: "The URL to the user's gists page."

      - name: "starred_url"
        type: "string"
        description: "The URL to the user's starred page."

      - name: "subscriptions_url"
        type: "string"
        description: "The URL to the user's subscriptions page."

      - name: "organizations_url"
        type: "string"
        description: "The URL to the user's organizations page."

      - name: "repos_url"
        type: "string"
        description: "The URL to the user's repositories page."

      - name: "events_url"
        type: "string"
        description: "The URL to the user's events page."

      - name: "received_events_url"
        type: "string"
        description: "The URL to the user's received events page."

      - name: "type"
        type: "string"
        description: "The type of the user."

      - name: "site_admin"
        type: "string"
        description: "Indicates if the user is a site administrator."
---