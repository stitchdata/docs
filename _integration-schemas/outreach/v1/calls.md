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

  - name: "callPurposeId"
    type: "integer"
    description: ""

  - name: "completedAt"
    type: "date-time"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "dialedAt"
    type: "date-time"
    description: ""

  - name: "direction"
    type: "string"
    description: ""

  - name: "externalVendor"
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

  - name: "outcome"
    type: "string"
    description: ""

  - name: "phoneNumberId"
    type: "integer"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""

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

  - name: "sequenceStateId"
    type: "integer"
    description: ""

  - name: "sequenceStepId"
    type: "integer"
    description: ""

  - name: "shouldRecordCall"
    type: "boolean"
    description: ""

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
    - name: "items"
      type: "string"
      description: ""

  - name: "taskId"
    type: "integer"
    description: ""

  - name: "to"
    type: "string"
    description: ""

  - name: "uid"
    type: "string"
    description: ""

  - name: "userCallType"
    type: "string"
    description: ""

  - name: "userId"
    type: "integer"
    description: ""

  - name: "vendorCallId"
    type: "string"
    description: ""

  - name: "voicemailRecordingUrl"
    type: "string"
    description: ""
---