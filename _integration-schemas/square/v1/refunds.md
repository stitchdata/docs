---
tap: "square"
version: "1"
key: "refund"

name: "refunds"
doc-link: "https://developer.squareup.com/reference/square/refunds-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/refunds.json"
description: |
  The `{{ table.name }}` table contains information about refunds on items in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List payment refunds (V2)"
  doc-link: "https://developer.squareup.com/reference/square/refunds-api/list-payment-refunds"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The refund ID."
    foreign-key-id: "refund-id"

  - name: "amount_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: ""
  
  - name: "location_id"
    type: "string"
    description: "The ID of the location associated with the refund."
    foreign-key-id: "location-id"

  - name: "order_id"
    type: "string"
    description: "The ID of the order associated with the refund."
    foreign-key-id: "order-id"

  - name: "payment_id"
    type: "string"
    description: "The ID of the payment associated with the refund."
    foreign-key-id: "payment-id"

  - name: "processing_fee"
    type: "array"
    description: ""
    subattributes:
      - name: "amount_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "effective_at"
        type: "date-time"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "reason"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---