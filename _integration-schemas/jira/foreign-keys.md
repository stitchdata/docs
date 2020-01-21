---
tap-reference: "jira"

version: "1"

foreign-keys:
  - id: "changelog-id"
    attribute: ""
    table: "changelogs"
    all-foreign-keys:
      - table: "changelogs"
        join-on: "id"

  - id: "issue-comment-id"
    attribute: "issueCommentId"
    table: "issue_comments"
    all-foreign-keys:
      - table: "issue_comments"
        join-on: "id"

  - id: "issue-id"
    attribute:  "issueId"
    table: "issues"
    all-foreign-keys:
      - table: "changelogs"
      - table: "issue_comments"
      - table: "issue_transitions"
      - table: "issues"
        join-on: "id"
      - table: "worklogs"

  - id: "issue-transition-id"
    attribute: "issueTransitionId"
    table: "issue_transitions"
    all-foreign-keys:
      - table: "issue_transitions"
        join-on: "id"

  - id: "project-type-key"
    attribute:  "projectTypeKey"
    table: "project_types"
    all-foreign-keys:
      - table: "project_types"
        join-on: "key"

  - id: "project-category-id"
    attribute:  "projectCategoryId"
    table: "project_categories"
    all-foreign-keys:
      - table: "project_categories"
        join-on: "id"
      - table: "projects"
        subattribute: "projectCategory"
        join-on: "id"

  - id: "project-id"
    attribute: "projectId"
    table: "projects"
    all-foreign-keys:
      - table: "projects"
        join-on: "id"
      - table: "versions"

  - id: "resolution-id"
    attribute: "resolutionId"
    table: "resolutions"
    all-foreign-keys:
      - table: "resolutions"
        join-on: "id"

  - id: "role-id"
    attribute: "roleId"
    table: "roles"
    all-foreign-keys:
      - table: "roles"
        join-on: "id"

  - id: "user-key"
    attribute: "key"
    table: "users"
    all-foreign-keys:
      - table: "changelogs"
        subattribute: "author"
      - table: "issue_comments"
        subattribute: "author"
      - table: "issue_comments"
        subattribute: "updateAuthor"
      - table: "issues"
        subtattribute: "fields"
        subtable: "attachment"
        subsubattribute: "author"
      - table: "projects"
        subattribute: "components__assignee"
      - table: "projects"
        subattribute: "components__lead"
      - table: "projects"
        subattribute: "components__realAssignee"
      - table: "projects"
        subattribute: "lead"
      - table: "users"
        join-on: "key"
      - table: "worklogs"
        subattribute: "author"
      - table: "worklogs"
        subattribute: "updateAuthor"

  - id: "version-id"
    attribute: "versionId"
    table: "versions"
    all-foreign-keys:
      - tables: "versions"
        join-on: "id"

  - id: "worklog-id"
    attribute: "worklogId"
    table: "worklogs"
    all-foreign-keys:
      - table: "worklogs"
        join-on: "id"
---