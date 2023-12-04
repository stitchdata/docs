---
tap: "activecampaign"
version: "1"
key: ""

name: "task_types"
doc-link: "https://developers.activecampaign.com/reference#deal-task-types"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/task_types.json"
description: |
  The `{{ table.name }}` table contains information about task types in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all task types"
    doc-link: "https://developers.activecampaign.com/reference#list-all-deal-task-types"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task type ID."
    foreign-key-id: "task-type-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "defduration"
    type: "integer"
    description: ""
  
  - name: "status"
    type: "integer"
    description: ""
  - name: "title"
    type: "string"
    description: ""
  - name: "udate"
    type: "date-time"
    description: ""
---
