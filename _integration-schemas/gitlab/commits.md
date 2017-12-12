---
tap: "gitlab"
# version: ""

name: "commits"
doc-link: https://gitlab.com/help/api/commits.md
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/commits.json
description: |
  The `commits` table contains info about repository commits in a project.

  #### `commits` & Incremental Replication

  Data for this table will only be replicated when the associated project (in the `projects` table) is also updated.

replication-method: "Incremental"
api-method:
  name: "listRepositoryCommits"
  doc-link: https://gitlab.com/help/api/commits.md#list-repository-commits

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The commit ID."

  - name: "n/a"
    replication-key: true

  - name: "created_at"
    type: "date-time"
    description: "The time the commit was created."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the commit."

  - name: "short_id"
    type: "string"
    description: "The short ID of the commit."

  - name: "title"
    type: "string"
    description: "The title of the commit."

  - name: "author_name"
    type: "string"
    description: "The name of the commit's author."

  - name: "author_email"
    type: "string"
    description: "The email of the commit's author."

  - name: "committer_name"
    type: "string"
    description: "The name of the committer."

  - name: "committer_email"
    type: "string"
    description: "The email address of the committer."

  - name: "message"
    type: "string"
    description: "The commit message."

  - name: "allow_failure"
    type: "boolean"
    description: "Indicates if failures are allowed."
---