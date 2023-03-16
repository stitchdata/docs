---
tap: "outreach"
version: "1"
key: "mailing"

name: "mailings"
doc-link: "https://api.outreach.io/api/v2/docs#mailing"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/mailings.json"
description: |
  The `{{ table.name}}` table is a representation of a platform-related email.

replication-method: "Key-based Incremental"

api-method:
  name: "Get mailings"
  doc-link: "https://api.outreach.io/api/v2/docs#mailing"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The mailing ID."
    #foreign-key-id: "mailing-id"

  - name: "updatedAt"
    type: "date-time"
    description: "The time the mailing was last updated."
    replication-key: true

  - name: "bodyHtml"
    type: "string"
    description: ""

  - name: "bodyText"
    type: "string"
    description: ""

  - name: "bouncedAt"
    type: "date-time"
    description: ""

  - name: "calendarId"
    type: "integer"
    description: ""

  - name: "clickCount"
    type: "integer"
    description: ""

  - name: "clickedAt"
    type: "date-time"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "deliveredAt"
    type: "date-time"
    description: ""

  - name: "errorBacktrace"
    type: "string"
    description: ""

  - name: "errorReason"
    type: "string"
    description: ""

  - name: "followUpTaskScheduledAt"
    type: "date-time"
    description: ""

  - name: "followUpTaskType"
    type: "string"
    description: ""

  - name: "mailboxAddress"
    type: "string"
    description: ""

  - name: "mailboxId"
    type: "integer"
    description: ""
    foreign-key-id: "mailbox-id"

  - name: "mailingType"
    type: "string"
    description: ""

  - name: "markedAsSpamAt"
    type: "date-time"
    description: ""

  - name: "messageId"
    type: "string"
    description: ""

  - name: "notifyThreadCondition"
    type: "string"
    description: ""

  - name: "notifyThreadScheduledAt"
    type: "date-time"
    description: ""

  - name: "notifyThreadStatus"
    type: "string"
    description: ""

  - name: "openCount"
    type: "integer"
    description: ""

  - name: "openedAt"
    type: "date-time"
    description: ""

  - name: "opportunityId"
    type: "integer"
    description: ""
    foreign-key-id: "opportunity-id"

  - name: "overrideSafetySettings"
    type: "boolean"
    description: ""

  - name: "prospectId"
    type: "integer"
    description: ""
    foreign-key-id: "prospect-id"

  - name: "references"
    type: "string"
    description: ""

  - name: "repliedAt"
    type: "date-time"
    description: ""

  - name: "retryAt"
    type: "date-time"
    description: ""

  - name: "retryCount"
    type: "integer"
    description: ""

  - name: "retryInterval"
    type: "integer"
    description: ""

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

  - name: "subject"
    type: "string"
    description: ""

  - name: "taskId"
    type: "integer"
    description: ""
    foreign-key-id: "task-id"

  - name: "templateId"
    type: "integer"
    description: ""

  - name: "trackLinks"
    type: "boolean"
    description: ""

  - name: "trackOpens"
    type: "boolean"
    description: ""

  - name: "unsubscribedAt"
    type: "date-time"
    description: ""
---