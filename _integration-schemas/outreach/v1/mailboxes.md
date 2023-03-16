---
tap: "outreach"
version: "1"
key: "mailbox"

name: "mailboxes"
doc-link: "https://api.outreach.io/api/v2/docs#mailbox"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/mailboxes.json"
description: |
  The `{{ table.name}}` table contains information about your {{ integration.display_name }} email mailbox.

replication-method: "Key-based Incremental"

api-method:
  name: "Get mailboxes"
  doc-link: "https://api.outreach.io/api/v2/docs#mailbox"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The mailbox ID."
    foreign-key-id: "mailbox-id"

  - name: "updatedAt"
    type: "date-time"
    description: "The time the mailbox was last updated."
    replication-key: true 

  - name: "authId"
    type: "integer"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "editable"
    type: "boolean"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "emailProvider"
    type: "string"
    description: ""

  - name: "emailSignature"
    type: "string"
    description: ""

  - name: "ewsEndpoint"
    type: "string"
    description: ""

  - name: "ewsSslVerifyMode"
    type: "integer"
    description: ""

  - name: "exchangeVersion"
    type: "string"
    description: ""

  - name: "imapHost"
    type: "string"
    description: ""

  - name: "imapPort"
    type: "integer"
    description: ""

  - name: "imapSsl"
    type: "boolean"
    description: ""

  - name: "maxEmailsPerDay"
    type: "integer"
    description: ""

  - name: "maxMailingsPerDay"
    type: "integer"
    description: ""

  - name: "maxMailingsPerWeek"
    type: "integer"
    description: ""

  - name: "optOutMessage"
    type: "string"
    description: ""

  - name: "optOutSignature"
    type: "string"
    description: ""

  - name: "prospectEmailExclusions"
    type: "string"
    description: ""

  - name: "providerId"
    type: "integer"
    description: ""

  - name: "providerType"
    type: "string"
    description: ""

  - name: "sendDisabled"
    type: "boolean"
    description: ""

  - name: "sendErroredAt"
    type: "date-time"
    description: ""

  - name: "sendMaxRetries"
    type: "integer"
    description: ""

  - name: "sendMethod"
    type: "string"
    description: ""

  - name: "sendPeriod"
    type: "integer"
    description: ""

  - name: "sendRequiresSync"
    type: "boolean"
    description: ""

  - name: "sendSuccessAt"
    type: "date-time"
    description: ""

  - name: "sendThreshold"
    type: "integer"
    description: ""

  - name: "sendgridWebhookUrl"
    type: "string"
    description: ""

  - name: "smtpHost"
    type: "string"
    description: ""

  - name: "smtpPort"
    type: "integer"
    description: ""

  - name: "smtpSsl"
    type: "boolean"
    description: ""

  - name: "smtpUsername"
    type: "string"
    description: ""

  - name: "syncActiveFrequency"
    type: "integer"
    description: ""

  - name: "syncDisabled"
    type: "boolean"
    description: ""

  - name: "syncErroredAt"
    type: "date-time"
    description: ""

  - name: "syncFinishedAt"
    type: "date-time"
    description: ""

  - name: "syncMethod"
    type: "string"
    description: ""

  - name: "syncOutreachFolder"
    type: "boolean"
    description: ""

  - name: "syncPassiveFrequency"
    type: "integer"
    description: ""

  - name: "syncSuccessAt"
    type: "date-time"
    description: ""

  - name: "updaterId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "userId"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "username"
    type: "string"
    description: ""

  - name: "validateSend"
    type: "boolean"
    description: ""

  - name: "validateSync"
    type: "boolean"
    description: ""
---