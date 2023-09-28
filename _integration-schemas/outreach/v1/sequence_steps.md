---
tap: "outreach"
version: "1"
key: "sequence-step"

name: "sequence_steps"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/sequence_steps.json"
description: |
  The `{{ table.name }}` table contains info about individual steps within automated sequences.

replication-method: "Key-based Incremental"

api-method:
  name: "Get sequence steps"
  doc-link: "https://api.outreach.io/api/v2/docs#sequenceStep"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The sequence step ID."
    foreign-key-id: "sequence-step-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the sequence step was last updated."

  - name: "bounceCount"
    type: "integer"
    description: ""

  - name: "callPurposeId"
    type: "integer"
    description: ""

  - name: "clickCount"
    type: "integer"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "date"
    type: "date-time"
    description: ""

  - name: "deliverCount"
    type: "integer"
    description: ""

  - name: "displayName"
    type: "string"
    description: ""

  - name: "failureCount"
    type: "integer"
    description: ""

  - name: "interval"
    type: "integer"
    description: ""

  - name: "negativeReplyCount"
    type: "integer"
    description: ""

  - name: "neutralReplyCount"
    type: "integer"
    description: ""

  - name: "openCount"
    type: "integer"
    description: ""

  - name: "optOutCount"
    type: "integer"
    description: ""

  - name: "order"
    type: "integer"
    description: ""

  - name: "positiveReplyCount"
    type: "integer"
    description: ""

  - name: "replyCount"
    type: "integer"
    description: ""

  - name: "scheduleCount"
    type: "integer"
    description: ""

  - name: "sequenceId"
    type: "integer"
    description: ""
    foreign-key-id: "sequence-id"

  - name: "stepType"
    type: "string"
    description: ""

  - name: "taskAutoskipDelay"
    type: "integer"
    description: ""

  - name: "taskNote"
    type: "string"
    description: ""

  - name: "taskPriorityId"
    type: "integer"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---