---
tap: "outreach"
version: "1"
key: "task"

name: "tasks"
doc-link: "https://api.outreach.io/api/v2/docs#task"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/tasks.json"
description: |
  The `{{ table.name}}` table contains information about items that require action in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Get tasks"
  doc-link: "https://api.outreach.io/api/v2/docs#task"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The task ID."
    foreign-key-id: "task-id"
  
  - name: "updatedAt"
    type: "date-time"
    description: "The time the task was last updated."
    replication-key: true

  - name: "accountId"
    type: "integer"
    description: ""

  - name: "action"
    type: "string"
    description: ""

  - name: "autoskipAt"
    type: "date-time"
    description: ""

  - name: "callId"
    type: "integer"
    description: ""

  - name: "compiledSequenceTemplateHtml"
    type: "string"
    description: ""

  - name: "completed"
    type: "boolean"
    description: ""

  - name: "completedAt"
    type: "date-time"
    description: ""

  - name: "completerId"
    type: "integer"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""

  - name: "dueAt"
    type: "date-time"
    description: ""

  - name: "mailingId"
    type: "integer"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "opportunityAssociation"
    type: "string"
    description: ""

  - name: "opportunityId"
    type: "integer"
    description: ""

  - name: "ownerId"
    type: "integer"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""

  - name: "scheduledAt"
    type: "date-time"
    description: ""

  - name: "sequenceId"
    type: "integer"
    description: ""

  - name: "sequenceStateId"
    type: "integer"
    description: ""

  - name: "sequenceStepId"
    type: "integer"
    description: ""

  - name: "sequenceTemplateId"
    type: "integer"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "stateChangedAt"
    type: "date-time"
    description: ""

  - name: "subjectId"
    type: "integer"
    description: ""

  - name: "taskPriorityId"
    type: "integer"
    description: ""

  - name: "taskThemeId"
    type: "integer"
    description: ""

  - name: "taskType"
    type: "string"
    description: ""

  - name: "templateId"
    type: "integer"
    description: ""
---