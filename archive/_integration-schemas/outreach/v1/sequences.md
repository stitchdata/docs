---
tap: "outreach"
version: "1"
key: "sequence"

name: "sequences"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/sequences.json"
description: |
  The `{{ table.name }}` table contains info about sequences.

replication-method: "Key-based Incremental"

api-method:
  name: "Get sequences"
  doc-link: "https://api.outreach.io/api/v2/docs#sequence"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The sequence ID."
    foreign-key-id: "sequence-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the sequence was last updated."

  - name: "automationPercentage"
    type: "number"
    description: ""

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

  - name: "description"
    type: "string"
    description: ""

  - name: "durationInDays"
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

  - name: "finishOnReply"
    type: "boolean"
    description: ""

  - name: "lastUsedAt"
    type: "date-time"
    description: ""

  - name: "locked"
    type: "boolean"
    description: ""

  - name: "lockedAt"
    type: "date-time"
    description: ""

  - name: "maxActivations"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "negativeReplyCount"
    type: "integer"
    description: ""

  - name: "neutralReplyCount"
    type: "integer"
    description: ""

  - name: "numContactedProspects"
    type: "integer"
    description: ""

  - name: "numRepliedProspects"
    type: "integer"
    description: ""

  - name: "openCount"
    type: "integer"
    description: ""

  - name: "optOutCount"
    type: "integer"
    description: ""

  - name: "ownerId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "positiveReplyCount"
    type: "integer"
    description: ""

  - name: "primaryReplyAction"
    type: "string"
    description: ""

  - name: "primaryReplyPauseDuration"
    type: "integer"
    description: ""

  - name: "replyCount"
    type: "integer"
    description: ""

  - name: "rulesetId"
    type: "integer"
    description: ""

  - name: "scheduleCount"
    type: "integer"
    description: ""

  - name: "scheduleIntervalType"
    type: "string"
    description: ""

  - name: "secondaryReplyAction"
    type: "string"
    description: ""

  - name: "secondaryReplyPauseDuration"
    type: "integer"
    description: ""

  - name: "sequenceStepCount"
    type: "integer"
    description: ""

  - name: "sequenceType"
    type: "string"
    description: ""

  - name: "shareType"
    type: "string"
    description: ""

  - name: "tags"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "throttleCapacity"
    type: "integer"
    description: ""

  - name: "throttleMaxAddsPerDay"
    type: "integer"
    description: ""

  - name: "throttlePaused"
    type: "boolean"
    description: ""

  - name: "throttlePausedAt"
    type: "date-time"
    description: ""

  - name: "transactional"
    type: "boolean"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---