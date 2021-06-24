---
tap: "outreach"
version: "1"
key: "sequence-state"

name: "sequence_states"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/sequence_states.json"
description: |
  The `{{ table.name }}` table contains info about currently sequenced prospects.

replication-method: "Key-based Incremental"

api-method:
  name: "Get sequence steps"
  doc-link: "https://api.outreach.io/api/v2/docs#sequenceState"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The sequence state ID."
    foreign-key-id: "sequence-state-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the sequence state was last updated."

  - name: "accountId"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "activeAt"
    type: "date-time"
    description: ""

  - name: "bounceCount"
    type: "integer"
    description: ""

  - name: "callCompletedAt"
    type: "date-time"
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

  - name: "errorReason"
    type: "string"
    description: ""

  - name: "failureCount"
    type: "integer"
    description: ""

  - name: "naturalReplyCount"
    type: "integer"
    description: ""

  - name: "negativeReplyCount"
    type: "integer"
    description: ""

  - name: "openCount"
    type: "integer"
    description: ""

  - name: "optOutCount"
    type: "integer"
    description: ""

  - name: "pauseReason"
    type: "string"
    description: ""

  - name: "positiveReplyCount"
    type: "integer"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""
    foreign-key-id: "prospect-id"

  - name: "repliedAt"
    type: "date-time"
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

  - name: "state"
    type: "string"
    description: ""

  - name: "stateChangedAt"
    type: "date-time"
    description: ""
---