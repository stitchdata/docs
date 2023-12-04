---
tap: "square"
version: "1"
key: "order"

name: "orders"
doc-link: "https://developer.squareup.com/reference/square/orders-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/orders.json"
description: |
  The `{{ table.name }}` table contains information about order updates in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Search orders (V2)"
  doc-link: "https://developer.squareup.com/reference/square/orders-api/search-orders"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The order ID."
    foreign-key-id: "order-id"

  - name: "updated_at"
    type: "date-time"
    description: ""
    replication-key: true

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

      - name: "statement_description"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

  - name: "category_data"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

  - name: "closed_at"
    type: "date-time"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "delay_action"
    type: "string"
    description: ""

  - name: "delay_duration"
    type: "string"
    description: ""

  - name: "delayed_until"
    type: "string"
    description: ""

  - name: "discount_data"
    type: "object"
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

      - name: "discount_type"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "fulfillments"
    type: "array"
    description: ""
    subattributes:
      - name: "pickup_details"
        type: "object"
        description: ""
        subattributes:
          - name: "canceled_at"
            type: "date-time"
            description: ""

          - name: "expired_at"
            type: "date-time"
            description: ""

          - name: "expires_at"
            type: "date-time"
            description: ""

          - name: "note"
            type: "string"
            description: ""

          - name: "pickup_at"
            type: "date-time"
            description: ""

          - name: "recipient"
            type: "object"
            description: ""
            subattributes:
              - name: "display_name"
                type: "string"
                description: ""

          - name: "rejected_at"
            type: "date-time"
            description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "uid"
        type: "string"
        description: ""

  - name: "is_deleted"
    type: "boolean"
    description: ""

  - name: "line_items"
    type: "array"
    description: ""
    subattributes:
      - name: "base_price_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "catalog_object_id"
        type: "string"
        description: ""

      - name: "gross_sales_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "note"
        type: "string"
        description: ""

      - name: "quantity"
        type: "string"
        description: ""

      - name: "total_discount_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
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

      - name: "total_tax_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "uid"
        type: "string"
        description: ""

      - name: "variation_name"
        type: "string"
        description: ""

      - name: "variation_total_price_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

  - name: "location_id"
    type: "string"
    description: "The ID of the location associated with the order."
    foreign-key-id: "location-id"

  - name: "net_amounts"
    type: "object"
    description: ""
    subattributes:
      - name: "discount_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "service_charge_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "tax_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "tip_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
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

  - name: "note"
    type: "string"
    description: ""

  - name: "order_id"
    type: "string"
    description: "The order ID."
    foreign-key-id: "order-id"

  - name: "payment_id"
    type: "string"
    description: "The order payment ID."
    foreign-key-id: "payment-id"

  - name: "present_at_all_locations"
    type: "boolean"
    description: ""

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
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "reason"
    type: "string"
    description: ""

  - name: "receipt_number"
    type: "string"
    description: ""

  - name: "receipt_url"
    type: "string"
    description: ""

  - name: "refund_ids"
    type: "array"
    description: "A list of refunds associated with the order."
    subattributes:
      - name: "value"
        type: "string"
        description: "The refund IDs."
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

  - name: "refunds"
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

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "id"
        type: "string"
        description: "The refund ID."
        foreign-key-id: "refund-id"

      - name: "location_id"
        type: "string"
        description: "The location ID."
        foreign-key-id: "location-id"

      - name: "reason"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "tender_id"
        type: "string"
        description: ""
        foreign-key-id: "tender-id"

      - name: "transaction_id"
        type: "string"
        description: ""
        # foreign-key-id: "transaction-id"

  - name: "return_amounts"
    type: "object"
    description: ""
    subattributes:
      - name: "discount_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "service_charge_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "tax_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

      - name: "tip_money"
        type: "object"
        description: ""
        subattributes:
          - name: "amount"
            type: "integer"
            description: ""

          - name: "currency"
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

  - name: "returns"
    type: "array"
    description: ""
    subattributes:
      - name: "return_line_items"
        type: "array"
        description: ""
        subattributes:
          - name: "base_price_money"
            type: "object"
            description: ""
            subattributes:
              - name: "amount"
                type: "integer"
                description: ""

              - name: "currency"
                type: "string"
                description: ""

          - name: "gross_return_money"
            type: "object"
            description: ""
            subattributes:
              - name: "amount"
                type: "integer"
                description: ""

              - name: "currency"
                type: "string"
                description: ""

          - name: "quantity"
            type: "string"
            description: ""

          - name: "total_discount_money"
            type: "object"
            description: ""
            subattributes:
              - name: "amount"
                type: "integer"
                description: ""

              - name: "currency"
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

          - name: "total_tax_money"
            type: "object"
            description: ""
            subattributes:
              - name: "amount"
                type: "integer"
                description: ""

              - name: "currency"
                type: "string"
                description: ""

          - name: "uid"
            type: "string"
            description: ""

          - name: "variation_total_price_money"
            type: "object"
            description: ""
            subattributes:
              - name: "amount"
                type: "integer"
                description: ""

              - name: "currency"
                type: "string"
                description: ""

      - name: "source_order_id"
        type: "string"
        description: ""
        foreign-key-id: "order-id"

      - name: "uid"
        type: "string"
        description: ""

  - name: "source"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

  - name: "source_type"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tax_data"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

  - name: "tenders"
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

      - name: "card_details"
        type: "object"
        description: ""
        subattributes:
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

          - name: "entry_method"
            type: "string"
            description: ""

          - name: "status"
            type: "string"
            description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "tender-id"

      - name: "location_id"
        type: "string"
        description: ""
        foreign-key-id: "location-id"

      - name: "note"
        type: "string"
        description: ""

      - name: "payment_id"
        type: "string"
        description: ""
        foreign-key-id: "payment-id"

      - name: "transaction_id"
        type: "string"
        description: ""
        # foreign-key-id: "transaction-id"

      - name: "type"
        type: "string"
        description: ""

  - name: "total_discount_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
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

  - name: "total_service_charge_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

  - name: "total_tax_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

  - name: "total_tip_money"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: ""
  
  - name: "version"
    type: "integer"
    description: ""
---