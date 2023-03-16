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
    foreign-key-id: "account-id"

  - name: "action"
    type: "string"
    description: ""

  - name: "autoskipAt"
    type: "date-time"
    description: ""

  - name: "callId"
    type: "integer"
    description: ""
    foreign-key-id: "call-id"

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
    foreign-key-id: "user-id"

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "dueAt"
    type: "date-time"
    description: ""

  - name: "mailingId"
    type: "integer"
    description: ""
    foreign-key-id: "mailing-id"

  - name: "note"
    type: "string"
    description: ""

  - name: "opportunityId"
    type: "integer"
    description: ""
    foreign-key-id: "opportunity-id"

  - name: "ownerId"
    type: "integer"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""
    foreign-key-id: "prospect-id"

  - name: "scheduledAt"
    type: "date-time"
    description: ""

  - name: "sequenceId"
    type: "integer"
    description: ""
    foreign-key-id: "sequence-id"

  - name: "sequenceStateId"
    type: "integer"
    description: ""
    foreign-key-id: "sequence-state-id"

  - name: "sequenceStepId"
    type: "integer"
    description: ""
    foreign-key-id: "sequence-step-id"

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