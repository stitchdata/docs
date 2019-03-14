---
tap: "gitlab"
# version: ""

name: "issues"
doc-link: https://gitlab.com/help/api/issues.md#list-project-issues
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/issues.json
description: |
  The `issues` table contains info about issues contained within projects.

replication-method: "Key-based Incremental"
api-method:
  name: "listProjectIssues"
  doc-link: https://gitlab.com/help/api/issues.md#list-project-issues

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The issue ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the issue was last updated."

  - name: "project_id"
    type: "integer"
    description: "The ID of the project associated with the issue."

  - name: "milestone_id"
    type: "integer"
    description: "The ID of the milestone associated with the issue."

  - name: "author_id"
    type: "integer"
    description: "The ID of the issue's author."

  - name: "assignee_id"
    type: "integer"
    description: "The ID of the user who is assigned to the issue."

  - name: "description"
    type: "string"
    description: "The issue's description."

  - name: "state"
    type: "string"
    description: "The state of the issue. Possible values are `opened` or `closed`."

  - name: "iid"
    type: "integer"
    description: "The IID of the issue."

  - name: "labels"
    type: "array"
    description: "A list of labels applied to the issue."
    subattributes:
      - name: "value"
        type: "string"
        description: "The name of the label."

  - name: "title"
    type: "string"
    description: "The title of the issue."

  - name: "created_at"
    type: "date-time"
    description: "The time the issue was created."

  - name: "subscribed"
    type: "boolean"
    description: "Indicates if the authenticating user (the user who created the integration in Stitch) is subscribed to the issue."

  - name: "user_notes_count"
    type: "integer"
    description: "The count of notes in the issue."

  - name: "due_date"
    type: "string"
    description: "The date the issue is due by."

  - name: "web_url"
    type: "string"
    description: "The URL of the issue."

  - name: "confidential"
    type: "boolean"
    description: "Indicates if the issue is confidential."
---