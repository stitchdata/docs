---
tap: "gitlab"
version: "1.0"

name: "branches"
doc-link: https://gitlab.com/help/api/branches.html
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/branches.json
description: |
  The `{{ table.name }}` table contains high-level info about repository branches in your projects.

  **Note**: To replicate branch data, you must set this table and the [`projects`](#projects) table to replicate. Data for this table will only be replicated when the associated project (in the [`projects`](#projects) table) is also updated.

replication-method: "Key-based Incremental"
replication-key:
  name: "projects.last_activity_at"

api-method:
  name: "listRepositoryBranches"
  doc-link: https://gitlab.com/help/api/branches.html#list-repository-branches

attributes:
  - name: "project_id"
    type: "integer"
    primary-key: true
    description: "The ID of the project associated with the branch."
    foreign-key-id: "project-id"

  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the branch."

  - name: "merged"
    type: "boolean"
    description: "Indicates if the branch has been merged."

  - name: "protected"
    type: "boolean"
    description: "Indicates if the branch is protected."

  - name: "developers_can_push"
    type: "boolean"
    description: "Indicates if developers can push to the branch."

  - name: "developers_can_merge"
    type: "boolean"
    description: "Indicates if developers can merge."

  - name: "commit_id"
    type: "string"
    description: "The ID of the commit."
    foreign-key-id: "commit-id"
---