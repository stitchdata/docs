---
tap: "outreach"
version: "1"
key: "sequence-template"

name: "sequence_templates"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/sequence_templates.json"
description: |
  The `{{ table.name }}` table contains info about templates used by sequence steps.

replication-method: "Full Table"

api-method:
  name: "Get sequence templates"
  doc-link: "https://api.outreach.io/api/v2/docs#sequenceTemplate"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The sequence template ID."

  - name: "bounceCount"
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

  - name: "deliverCount"
    type: "integer"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "enabledAt"
    type: "date-time"
    description: ""

  - name: "failureCount"
    type: "integer"
    description: ""

  - name: "isReply"
    type: "boolean"
    description: ""

  - name: "negaitveReplyCount"
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

  - name: "positiveReplyCount"
    type: "integer"
    description: ""

  - name: "replyCount"
    type: "integer"
    description: ""

  - name: "scheduleCount"
    type: "integer"
    description: ""

  - name: "sequenceStepId"
    type: "integer"
    description: ""

  - name: "templateId"
    type: "integer"
    description: ""

  - name: "updatedAt"
    type: "date-time"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---