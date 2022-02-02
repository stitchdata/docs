---
tap: "activecampaign"
version: "1"
key: ""

name: "tasks"
doc-link: "https://developers.activecampaign.com/reference#tasks"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/tasks.json"
description: |
  The `{{ table.name }}` table contains information about tasks to do in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all tasks"
    doc-link: "https://developers.activecampaign.com/reference#list-all-tasks"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task ID."
    #foreign-key-id: "task-id"

  - name: "udate"
    type: "date-time"
    description: "The time the task was last updated."
    replication-key: true

  - name: "assignee"
    type: "integer"
    description: ""
  - name: "automation"
    type: "integer"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "deal_task_type"
    type: "integer"
    description: "The deal task type ID."
    foreign-key-id: "task-type-id"
  - name: "done_automation"
    type: "integer"
    description: ""
  - name: "duedate"
    type: "date-time"
    description: ""
  - name: "edate"
    type: "date-time"
    description: ""
  
  - name: "note"
    type: "string"
    description: ""
  - name: "owner"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "relid"
    type: "integer"
    description: ""
  - name: "reltype"
    type: "string"
    description: ""
  - name: "status"
    type: "integer"
    description: ""
  - name: "title"
    type: "string"
    description: ""

  - name: "user"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---
