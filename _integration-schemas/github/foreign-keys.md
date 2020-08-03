---
tap-reference: "github"

version: "1"

foreign-keys:
  - id: "assignee-id"
    attribute: ""
    table: "assignees"
    all-foreign-keys:
      - table: "assignees"
        join-on: "id"

  - id: "collaborator-id"
    attribute: ""
    table: "collaborators"
    all-foreign-keys:
      - table: "collaborators"
        join-on: "id"
      - table: "pull_requests"
        subattribute: "user"
        join-on: "id"
      - table: "reviews"
        subattribute: "user"
        join-on: "id"

  - id: "comment-id"
    attribute: "comment_id"
    table: "comments"
    all-foreign-keys:
      - table: "comments"
        join-on: "id"

  - id: "commit-id"
    attribute: "commit_id"
    table: "commits"
    all-foreign-keys:
      - table: "commits"
        join-on: "id"
      - table: "reviews"
      - table: "review_comments"
      - table: "review_comments"
        join-on: "original_commit_id"

  - id: "issue-id"
    attribute: "issue_id"
    table: "issues"
    all-foreign-keys:
      - table: "issues"
        join-on: "id"
      - table: "pull_requests"
        join-on: "id"

  - id: "pull-request-id"
    attribute: "pull_request_id"
    table: "pull_requests"
    all-foreign-keys:
      - table: "pull_requests"
        join-on: "id"
      - table: "issues"
        join-on: "id"

  - id: "review-comment-id"
    attribute: "review_comment_id"
    table: "review_comments"
    all-foreign-keys:
      - table: "review_comments"
        join-on: "id"

  - id: "review-id"
    attribute: "review_id"
    table: "reviews"
    all-foreign-keys:
      - table: "reviews"
        join-on: "id"
      - table: "review_comments"
        join-on: "pull_request_review_id"

  - id: "sha"
    attribute: "sha"
    table: "commits"
    all-foreign-keys:
      - table: "commits"
        join-on: "sha"

  - id: "release-id"
    attribute: "id"
    table: "releases"
    all-foreign-keys:
      - table: "releases"
        join-on: "id"   
---