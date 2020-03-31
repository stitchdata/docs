---
tap: "chargebee"
version: "1"
key: "gifts"

name: "gifts"
doc-link: "https://apidocs.chargebee.com/docs/api/gifts"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/gifts.json"
description: "The `{{ table.name }}` table contains info about the gifts in your {{ integration.display_name }} account."

replication-method: "Key-based Incremental"

api-method:
    name: "List gifts"
    doc-link: "https://apidocs.chargebee.com/docs/api/gifts#list_gifts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The gift ID."
    foreign-key-id: "gift-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the gift was last updated"
    replication-key: true

  - name: "auto_claim"
    type: "boolean"
    description: "Whether or not the gift is an auto-claim gift."

  - name: "claim_expiry_date"
    type: "date-time"
    description: "The date until which the gift can be received."

  - name: "gift_receiver"
    type: "object"
    description: "Details of the gift receiver."
    subattributes:
      - name: "customer_id"
        type: "string"
        foreign-key-id: "customer-id"
        description: "The receiver's customer ID."
      - name: "email"
        type: "string"
        description: "The receiver's email."
      - name: "first_name"
        type: "string"
        description: "The first name of the receiver."
      - name: "last_name"
        type: "string"
        description: "The last name of the receiver."
      - name: "subscription_id"
        type: "string"
        description: "The subscription created for the gift."
        foreign-key-id: "subscription-id"

  - name: "gift_timelines"
    type: "array"
    description: "The gift timeline details."
    subattributes:
      - name: "occurred_at"
        type: "date-time"
        description: "The timestamp of when this event occured."
      - name: "status"
        type: "string"
        description: |
          The status of the gift. The possible values are:
          - `scheduled`
          - `unclaimed`
          - `claimed`
          - `cancelled`
          - `expired`

  - name: "gifter"
    type: "object"
    description: "The gifter's details."
    subattributes:
      - name: "customer_id"
        type: "string"
        description: "The gifter's customer ID."
      - name: "invoice_id"
        type: "string"
        description: "The gifter's gift invoice ID."
        foreign-key-id: "invoice_id"
      - name: "note"
        type: "string"
        description: "The personalize message for the gift."
      - name: "signature"
        type: "string"
        description: "The gifter's signature."

  - name: "resource_version"
    type: "integer"
    description: "The version number of this resource."

  - name: "scheduled_at"
    type: "date-time"
    description: "The date in which the receiver will recieve the gift notification."

  - name: "status"
    type: "string"
    description: |
      The status of the gift. The possible values are:
      - `scheduled`
      - `unclaimed`
      - `claimed`
      - `cancelled`
      - `expired`
---
