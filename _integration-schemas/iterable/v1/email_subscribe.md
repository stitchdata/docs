---
tap: "iterable"
version: "1"
key: ""

name: "email_subscribe"
doc-link: https://api.iterable.com/api/docs#export_exportDataJson
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/email_subscribe.json
description: |
  The **{{ table.name }}** table contains information about emails subscribed to your {{ integration.display_name }} campaign.

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
    description: "The time the subscription was created."  

  - name: "campaignId"
    type: "integer"
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "channelIds"
    type: "array"
    description: "The channel IDs the email is subscribed to."
    subattributes:
      - name: "items"
        type: "integer"
        description: "The channel ID."
        foreign-key-id: "channel-id"

  - name: "emailListId"
    type: "integer"
    description: ""

  - name: "emailListIds"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "integer"
        description: ""

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


  - name: "profileUpdatedAt"
    type: "date-time"
    description: ""

  - name: "signupSource"
    type: "string"
    description: ""

  - name: "templateId"
    type: "integer"
    description: "The template ID."
    foreign-key-id: "template-id"

  - name: "userId"
    type: "string"
    description: ""

  - name: "workflowId"
    type: "integer"
    description: ""

---
