---
tap: "outreach"
version: "1"
key: "call"

name: "calls"
doc-link: "https://api.outreach.io/api/v2/docs#call"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/calls.json"
description: |
  The `{{ table.name}}` table contains information about inbound and outbound calls in your {{ integration.display_name }} call logs.

replication-method: "Key-based Incremental"

api-method:
  name: "Get calls"
  doc-link: "https://api.outreach.io/api/v2/docs#call"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The call ID."
    foreign-key-id: "call-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the call was last updated."
    
  - name: "answeredAt"
    type: "date-time"
    description: ""

  - name: "callDispositionId"
    type: "integer"
    description: ""
    foreign-key-id: "call-disposition-id"

  - name: "callPurposeId"
    type: "integer"
    description: ""
    foreign-key-id: "call-purpose-id"

  - name: "completedAt"
    type: "date-time"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "direction"
    type: "string"
    description: ""

  - name: "from"
    type: "string"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "opportunityId"
    type: "integer"
    description: ""
    foreign-key-id: "opportunity-id"

  - name: "outcome"
    type: "string"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""
    foreign-key-id: "prospect-id"

  - name: "recordingUrl"
    type: "string"
    description: ""

  - name: "returnedAt"
    type: "date-time"
    description: ""

  - name: "sequenceAction"
    type: "string"
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

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "taskId"
    type: "integer"
    description: ""
    foreign-key-id: "task-id"

  - name: "to"
    type: "string"
    description: ""

  - name: "userCallType"
    type: "string"
    description: ""

  - name: "userId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "voicemailRecordingUrl"
    type: "string"
    description: ""
---