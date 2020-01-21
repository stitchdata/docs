---
tap: "gitlab"
version: "1"

name: "milestones"
doc-link: https://gitlab.com/help/api/milestones.md#list-project-milestones
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/milestones.json
description: |
  The `{{ table.name }}` table contains info about project milestones.

  **Note**: To replicate milestone data, you must set this table and the [`projects`](#projects) table to replicate. Data for this table will only be replicated when the associated project (in the [`projects`](#projects) table) is also updated.

replication-method: "Key-based Incremental"
api-method:
  name: "listProjectMilestones"
  doc-link: https://gitlab.com/help/api/milestones.md#list-project-milestones

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The milestone ID."
    foreign-key-id: "milestone-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the milestone was last updated."

  - name: "iid"
    type: "integer"
    description: "The IID of the milestone."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project the milestone is associated with."
    foreign-key-id: "project-id"

  - name: "title"
    type: "string"
    description: "The title of the milestone."

  - name: "description"
    type: "string"
    description: "The description of the milestone."

  - name: "due_date"
    type: "string"
    description: "The date the milestone is due by."

  - name: "start_date"
    type: "string"
    description: "The start date of the milestone."

  - name: "state"
    type: "string"
    description: "The state of the milestone. Possible values are `active` and `closed`."

  - name: "created_at"
    type: "date-time"
    description: "The time the milestone was created."
---