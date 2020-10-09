---
tap: "square"
version: "1"
key: "payment"

name: "payments"
doc-link: "https://developer.squareup.com/reference/square/payments-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/payments.json"
description: |
  The `{{ table.name }}` table contains information about all payments taken in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List payments (V2)"
  doc-link: "https://developer.squareup.com/reference/square/payments-api/v1-list-payments"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The payment ID."
    foreign-key-id: "payment-id"

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

  - name: "card_details"
    type: "object"
    description: ""
    subattributes:
      - name: "auth_result_code"
        type: "string"
        description: ""

      - name: "avs_status"
        type: "string"
        description: ""

      - name: "card"
        type: "object"
        description: ""
        subattributes:
          - name: "bin"
            type: "string"
            description: ""

          - name: "card_brand"
            type: "string"
            description: ""

          - name: "card_type"
            type: "string"
            description: ""

          - name: "exp_month"
            type: "integer"
            description: ""

          - name: "exp_year"
            type: "integer"
            description: ""

          - name: "fingerprint"
            type: "string"
            description: ""

          - name: "last_4"
            type: "string"
            description: ""

          - name: "prepaid_type"
            type: "string"
            description: ""

      - name: "cvv_status"
        type: "string"
        description: ""

      - name: "entry_method"
        type: "string"
        description: ""

      - name: "errors"
        type: "array"
        description: ""
        subattributes:
          - name: "category"
            type: "string"
            description: ""

          - name: "code"
            type: "string"
            description: ""

          - name: "detail"
            type: "string"
            description: ""

          - name: "field"
            type: "string"
            description: ""

      - name: "statement_description"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

  - name: "cardholder_name"
    type: "string"
    description: ""
    
  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "customer_id"
    type: "string"
    description: ""
    # foreign-key-id: "customer-id"

  - name: "delay_action"
    type: "string"
    description: ""

  - name: "delay_duration"
    type: "string"
    description: ""

  - name: "delayed_until"
    type: "date-time"
    description: ""

  - name: "location_id"
    type: "string"
    description: "The ID of the location associated with the payment."
    foreign-key-id: "location-id"

  - name: "note"
    type: "string"
    description: ""

  - name: "order_id"
    type: "string"
    description: "The ID of the order associated with the payment."
    foreign-key-id: "order-id"

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

  - name: "receipt_number"
    type: "string"
    description: ""

  - name: "receipt_url"
    type: "string"
    description: ""

  - name: "reference_id"
    type: "string"
    description: ""

  - name: "refund_ids"
    type: "array"
    description: "A list of refunds associated with the payment."
    subattributes:
      - name: "value"
        type: "string"
        description: "The refund ID."
        foreign-key-id: "refund-id"

  - name: "refunded_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

  - name: "source_type"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "total_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---