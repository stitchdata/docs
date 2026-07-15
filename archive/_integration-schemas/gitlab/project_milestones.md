---
tap: "gitlab"
version: "1"

name: "project_milestones"
doc-link: https://docs.gitlab.com/ee/api/milestones.html#list-project-milestones
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/project_milestones.json
description: |
  The `{{ table.name }}` table contains info about project-level milestones.

  **Note**: To replicate project milestone data, you must set this table and the [`projects`](#projects) table to replicate. Data for this table will only be replicated when the associated project (in the [`projects`](#projects) table) is also updated.

replication-method: "Key-based Incremental"
replication-key:
  name: "projects.last_activity_at"

api-method:
  name: "listProjectMilestones"
  doc-link: https://docs.gitlab.com/ee/api/milestones.html#list-project-milestones

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The milestone ID."
    foreign-key-id: "milestone-id"

  - name: "iid"
    type: "integer"
    primary-key: true
    description: "The milestone internal ID."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the milestone."
    foreign-key-id: "project-id"

  - name: "title"
    type: "string"
    description: "The milestone title."

  - name: "description"
    type: "string"
    description: "The milestone description."

  - name: "due_date"
    type: "date-time"
    description: "The milestone due date."

  - name: "start_date"
    type: "date-time"
    description: "The milestone start date."

  - name: "state"
    type: "string"
    description: "The milestone state. Ex: `active` or `closed`"

  - name: "updated_at"
    type: "date-time"
    description: "The time the milestone was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the milestone was created."

  - name: "expired"
    type: "boolean"
    description: "Indicates if the milestone has expired."
---
