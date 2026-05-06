---
tap: "gitlab"
version: "1"

name: "group_milestones"
doc-link: https://docs.gitlab.com/ee/api/milestones.html#group-level-mr-approvals
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/group_milestones.json
description: |
  The `{{ table.name }}` table contains info about group-level milestones.

  **Note**: To replicate group milestone data, you must set this table and the [`groups`](#groups) table to replicate. Data for this table will only be replicated when the associated group (in the [`groups`](#groups) table) is also updated.

replication-method: "Key-based Incremental"

api-method:
  name: "listGroupMilestones"
  doc-link: https://docs.gitlab.com/ee/api/milestones.html#list-all-group-milestones

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

  - name: "group_id"
    type: "integer"
    description: "The ID of the group associated with the milestone."
    foreign-key-id: "group-id"

  - name: "title"
    type: "string"
    description: "The milestone title."

  - name: "description"
    type: "string"
    description: "The milestone description."

  - name: "state"
    type: "string"
    description: "The milestone state. Ex: `active` or `closed`"

  - name: "created_at"
    type: "date-time"
    description: "The time the milestone was created."

  - name: "updated_at"
    type: "date-time"
    description: "The time the milestone was last updated."

  - name: "start_date"
    type: "date-time"
    description: "The milestone start date."

  - name: "due_date"
    type: "date-time"
    description: "The milestone due date."

  - name: "expired"
    type: "boolean"
    description: "Indicates if the milestone has expired."

  - name: "web_url"
    type: "string"
    description: "The URL of the milestone."
---
