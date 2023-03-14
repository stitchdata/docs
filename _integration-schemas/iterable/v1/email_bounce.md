---
tap: "iterable"
version: "1"
key: ""

name: "email_bounce"
doc-link: https://api.iterable.com/api/docs#export_exportDataJson
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/email_bounce.json
description: |
  The **{{ table.name }}** table contains information about bounced emails within your {{ integration.display_name }} campaign.

replication-method: "Key-based Incremental"

api-method:
  name: "Export data to JSON"
  doc-link: "https://api.iterable.com/api/docs#export_exportDataJson"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The user email."
    foreign-key-id: "email-id"

  - name: "createdAt"
    type: "date-time"
    replication-key: true
    description: "The time the email bounce was created."  

  - name: "campaignId"
    type: "integer"
    description: "The campaign ID."
    foreign-key-id: "campaign-id"


  - name: "eventName"
    type: "string"
    description: ""

  - name: "itblInternal"
    type: "object"
    description: ""
    subattributes:
    - name: "documentCreatedAt"
      type: "date-time"
      description: ""

    - name: "documentUpdatedAt"
      type: "date-time"
      description: ""


  - name: "messageId"
    type: "string"
    description: ""

  - name: "recipientState"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "templateId"
    type: "integer"
    description: "The template ID."
    foreign-key-id: "template-id"

---
