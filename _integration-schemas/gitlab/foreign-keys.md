---
tap-reference: "gitlab"

# version: "1.0"

foreign-keys:
  - id: "project-id"
    attribute: "project_id"
    table: "projects"
    all-foreign-keys:
      - table: "branches"
      - table: "commits"
      - table: "issues"
      - table: "milestones"
      - table: "projects"

  - id: "commit-id"
    attribute: "commit_id"
    table: "commits"
    all-foreign-keys:
      - table: "commits"
        join-on: "id"
      - table: "branches"

  - id: "issue-id"
    attribute: "issue_id"
    table: "issues"
    all-foreign-keys:
      - table: "issues"
        join-on: "id"

  - id: "milestone-id"
    attribute: "milestone_id"
    table: "milestones"
    all-foreign-keys:
      - table: "issues"
      - table: "milestones"
        join-on: "id"

  - id: "user-id"
    attribute: "user_id"
    table: "users"
    all-foreign-keys:
      - table: "projects"
        join-on: "creator_id"
      - table: "users"
        join-on: "id"
---