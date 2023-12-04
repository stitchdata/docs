---
tap: "iterable-core"
version: "1"
key: ""

name: "email_open"
doc-link: https://api.iterable.com/api/docs#export_exportDataJson
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/email_open.json
description: |
  The **{{ table.name }}** table contains information about email recipients that opened your {{ integration.display_name }} campaign.

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
    description: "The time the email was opened."

  - name: "campaignId"
    type: "integer"
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "city"
    type: "string"
    description: ""

  - name: "contentId"
    type: "integer"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "eventName"
    type: "string"
    description: ""

  - name: "ip"
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

  - name: "proxySource"
    type: "string"
    description: ""

  - name: "region"
    type: "string"
    description: ""

  - name: "templateId"
    type: "integer"
    description: "The template ID."
    foreign-key-id: "template-id"

  - name: "userAgent"
    type: "string"
    description: ""

  - name: "userAgentDevice"
    type: "string"
    description: ""

---
