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
      - table: "issue_events"
      - table: "pull_request_reviews"
      - table: "reviews"
      - table: "review_comments"
      - table: "review_comments"
        join-on: "original_commit_id"

  - id: "commit-comment-id"
    attribute: ""
    table: "commit_comments"
    all-foreign-keys:
      - table: "commit_comments"
        join-on: "id"

  - id: "issue-label-id"
    table: "issue_labels"
    attribute: ""
    all-foreign-keys:
      - table: "issue_labels"
        join-on: "id"

  - id: "issue-milestone-id"
    table: "issue_milestones"
    attribute: ""
    all-foreign-keys:
      - table: "issue_milestones"
        join-on: "id"

  - id: "issue-id"
    attribute: "issue_id"
    table: "issues"
    all-foreign-keys:
      - table: "issues"
        join-on: "id"
      - table: "issue_events"
      - table: "pull_requests"
        join-on: "id"

  - id: "label-id"
    table: "labels"
    attribute: "labels.id"
    all-foreign-keys:
      - table: "issue_events"
      - table: "issue_labels"
        join-on: "id"
      - table: "issues"
      - table: "pull_requests"

  - id: "milestone-id"
    table: "milestones"
    attribute: ""
    all-foreign-keys:
      - table: "issue_events"
        subattribute: "issue.milestone"
        join-on: "id"

  - id: "project-id"
    table: "projects"
    attribute: ""
    all-foreign-keys:
      - table: "projects"
        join-on: "id"

  - id: "pull-request-id"
    attribute: "pull_request_id"
    table: "pull_requests"
    all-foreign-keys:
      - table: "issues"
        join-on: "id"
      - table: "pr_commits"
        join-on: "pr_id"
      - table: "pull_requests"
        join-on: "id"

  - id: "review-comment-id"
    attribute: "review_comment_id"
    table: "review_comments"
    all-foreign-keys:
      - table: "review_comments"
        join-on: "id"
      - table: "review_comments"
        join-on: "in_reply_to_id"

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
      - table: "events"
        subattribute: "payload.commits"
      - table: "pr_commits"

  - id: "release-id"
    attribute: "id"
    table: "releases"
    all-foreign-keys:
      - table: "releases"
        join-on: "id"

  - id: "team-member-id"
    table: "team_members"
    attribute: ""
    all-foreign-keys:
      - table: "team_members"
        join-on: "id"

  - id: "team-id"
    table: "teams"
    attribute: ""
    all-foreign-keys:
      - table: "teams"
        join-on: "id"
---