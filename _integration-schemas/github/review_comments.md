---
tap: "github"
version: "1.0"

name: "review_comments"
doc-link: https://developer.github.com/v3/pulls/comments/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/review_comments.json
description: |
  The `review_comments` table contains info about comments made on pull request reviews.

  **Note**: In order to replicate this table, you must also set the [`pull_requests`](#pull_requests) table to replicate.

replication-method: "Key-based Incremental"

api-method:
  name: "List comments on a pull request"
  doc-link: https://developer.github.com/v3/pulls/comments/#list-comments-on-a-pull-request

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The review comment ID."
    # foreign-key-id: "review-comment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the review comment was last updated."

  # - name: "assignee"
  #   type: "string"
  #   description: ""

  # - name: "assignees"
  #   type: "string"
  #   description: ""

  # - name: "author_association"
  #   type: "string"
  #   description: ""

  # - name: "base"
  #   type: "string"
  #   description: ""

  - name: "body"
    type: "string"
    description: "The body of the review comment."

  # - name: "comments_url"
  #   type: "string"
  #   description: ""

  - name: "commit_id"
    type: "string"
    description: "The ID of the commit the review comment is associated with."
    foreign-key-id: "commit-id"

  # - name: "commits_url"
  #   type: "string"
  #   description: ""

  - name: "created_at"
    type: "date-time"
    description: "The time the review comment was created."

  # - name: "diff_hunk"
  #   type: "string"
  #   description: ""

  - name: "diff_url"
    type: "string"
    description: "The diff URL associated with the review comment."

  # - name: "head"
  #   type: "string"
  #   description: ""

  # - name: "home_url"
  #   type: "string"
  #   description: ""

  - name: "html_url"
    type: "string"
    description: "The HTML URL of the review comment."

  - name: "in_reply_to_id"
    type: "integer"
    description: "If the review comment is a reply to another review comment, this will be the ID of the review comment it is in response to."

  - name: "issue_url"
    type: "string"
    description: "The URL of the issue associated with the review comment."

  # - name: "labels"
  #   type: "string"
  #   description: ""

  # - name: "locked"
  #   type: "string"
  #   description: ""

  # - name: "merge_commit_sha"
  #   type: "string"
  #   description: ""

  # - name: "milestone"
  #   type: "string"
  #   description: ""

  - name: "node_id"
    type: "string"
    description: "The review comment's node ID."

  - name: "original_position"
    type: "integer"
    description: "The original position of the review comment."

  - name: "original_commit_id"
    type: "string"
    description: "The ID of the original comment the review comment is associated with."
    foreign-key-id: "commit-id"  

  # - name: "patch_url"
  #   type: "string"
  #   description: ""

  - name: "pull_request_review_id"
    type: "integer"
    description: "The ID of the pull request review the comment is a part of."
    foreign-key-id: "review-id"

  - name: "path"
    type: "string"
    description: "The path of the file the review comment was made on."

  - name: "position"
    type: "integer"
    description: "The position of the review comment."

  - name: "pull_request_url"
    type: "string"
    description: "The URL of the pull request associated with the review comment."

  # - name: "requested_reviewers"
  #   type: "string"
  #   description: ""

  # - name: "requested_teams"
  #   type: "string"
  #   description: ""

  # - name: "review_comment_url"
  #   type: "string"
  #   description: ""

  # - name: "review_comments_url"
  #   type: "string"
  #   description: ""

  # - name: "statuses_url"
  #   type: "string"
  #   description: ""

  - name: "url"
    type: "string"
    description: "The GitHub URL of the review comment."

  - name: "user"
    type: "object"
    description: "Details about the user who created the review comment."
    subattributes:
      - name: "login"
        type: "string"
        description: "The login name of the user who created the review comment."

      - name: "id"
        type: "string"
        description: "The ID of the user who created the review comment."
---