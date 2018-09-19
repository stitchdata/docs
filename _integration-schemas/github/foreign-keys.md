---
tap-reference: "github"

# version: "1.0"

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

  - id: "commit-id"
    attribute: "commit_id"
    table: "commits"
    all-foreign-keys:
      - table: "commits"
        join-on: "id"
      - table: "reviews"

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

  - id: "review-id"
    attribute: "review_id"
    table: "reviews"
    all-foreign-keys:
      - table: "reviews"
        join-on: "id"

  - id: "sha"
    attribute: "sha"
    table: "commits"
    all-foreign-keys:
      - table: "commits"
        join-on: "sha"
---