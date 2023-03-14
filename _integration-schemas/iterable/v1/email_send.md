---
tap: "iterable"
version: "1"
key: ""

name: "email_send"
doc-link: https://api.iterable.com/api/docs#export_exportDataJson
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/email_send.json
description: |
  The **{{ table.name }}** table contains information about campaign emails you sent in your {{ integration.display_name }} account.

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
    description: "The time the email was sent."

  - name: "campaignId"
    type: "integer"
    description: "The campaign ID"
    foreign-key-id: "campaign-id"

  - name: "catalogCollectionCount"
    type: "integer"
    description: ""

  - name: "catalogLookupCount"
    type: "integer"
    description: ""

  - name: "channelId"
    type: "integer"
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "contentId"
    type: "integer"
    description: ""

  - name: "espName"
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


  - name: "messageBusId"
    type: "string"
    description: ""

  - name: "messageId"
    type: "string"
    description: ""

  - name: "messageTypeId"
    type: "integer"
    description: ""

  - name: "productRecommendationCount"
    type: "integer"
    description: ""

  - name: "templateId"
    type: "integer"
    description: "The template ID."
    foreign-key-id: "template-id"

  - name: "transactionalData"
    type: "object"
    description: ""
    subattributes:
      - name: "inventory"
        type: "integer"
        description: ""

      - name: "eventName"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "sku"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "price"
        type: "integer"
        description: ""

      - name: "product_type"
        type: "string"
        description: ""

      - name: "compare_at_price"
        type: "number"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "templateId"
        type: "integer"
        description: ""

      - name: "product_id"
        type: "string"
        description: ""

      - name: "categories"
        type: "array"
        description: ""
        subattributes:
         - name: "items"
           type: ""
           description: ""

      - name: "createdAt"
        type: "date-time"
        description: ""

      - name: "campaignId"
        type: "integer"
        description: ""

      - name: "vendor"
        type: "string"
        description: ""

      - name: "eventUpdatedAt"
        type: "date-time"
        description: ""

      - name: "discount"
        type: "integer"
        description: ""

      - name: "imageUrl"
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


      - name: "handle"
        type: "string"
        description: ""


---
