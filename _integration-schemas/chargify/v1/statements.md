---
tap: "chargify"
version: "1"
key: "statement"

name: "statements"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/statements.json"
description: |
  The `{{ table.name }}` table contains info about the statements in your {{ integration.display_name }} instance. Statements show all account activity for a specific usage period and are similar to invoices, as they can be marked as currently paid or unpaid.

replication-method: "Full Table"

api-method:
  name: "List statements for a site"
  doc-link: "https://reference.chargify.com/v1/statements/list-statements-for-a-site"
  
attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The statement ID."
    foreign-key-id: "statement-id"

  - name: "basic_html_view"
    type: "string"
    description: ""

  - name: "closed_at"
    type: "date-time"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "customer_billing_address"
    type: "string"
    description: ""

  - name: "customer_billing_address_2"
    type: "string"
    description: ""

  - name: "customer_billing_city"
    type: "string"
    description: ""

  - name: "customer_billing_country"
    type: "string"
    description: ""

  - name: "customer_billing_state"
    type: "string"
    description: ""

  - name: "customer_billing_zip"
    type: "string"
    description: ""

  - name: "customer_first_name"
    type: "string"
    description: ""

  - name: "customer_last_name"
    type: "string"
    description: ""

  - name: "customer_organization"
    type: "string"
    description: ""

  - name: "customer_shipping_address"
    type: "string"
    description: ""

  - name: "customer_shipping_address_2"
    type: "string"
    description: ""

  - name: "customer_shipping_city"
    type: "string"
    description: ""

  - name: "customer_shipping_country"
    type: "string"
    description: ""

  - name: "customer_shipping_state"
    type: "string"
    description: ""

  - name: "customer_shipping_zip"
    type: "string"
    description: ""

  - name: "ending_balance_in_cents"
    type: "number"
    description: ""

  - name: "events"
    type: "array"
    description: ""
    subattributes:
      - name: "event"
        type: "object"
        description: ""
        subattributes:
          - name: "created_at"
            type: "date-time"
            description: ""

          - name: "event_specific_data"
            type: "object"
            description: ""
            subattributes:
              - name: "account_transaction_id"
                type: "number"
                description: ""

              - name: "product_id"
                type: "number"
                description: ""
                foreign-key-id: "product-id"

          - name: "id"
            type: "number"
            description: ""
            foreign-key-id: "event-id"

          - name: "key"
            type: "string"
            description: ""

          - name: "message"
            type: "string"
            description: ""

          - name: "subscription_id"
            type: "number"
            description: ""
            foreign-key-id: "subscription-id"

  - name: "future_payments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "html_view"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "opened_at"
    type: "date-time"
    description: ""

  - name: "settled_at"
    type: "date-time"
    description: ""

  - name: "starting_balance_in_cents"
    type: "number"
    description: ""

  - name: "subscription_id"
    type: "number"
    description: ""
    foreign-key-id: "subscription-id"

  - name: "text_view"
    type: "string"
    description: ""

  - name: "total_in_cents"
    type: "number"
    description: ""

  - name: "transactions"
    type: "array"
    description: ""
    subattributes:
      - name: "amount_in_cents"
        type: "number"
        description: ""

      - name: "component_id"
        type: "number"
        description: ""
        foreign-key-id: "component-id"

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "customer_id"
        type: "number"
        description: ""
        foreign-key-id: "customer-id"

      - name: "discount_amount_in_cents"
        type: "number"
        description: ""

      - name: "ending_balance_in_cents"
        type: "number"
        description: ""

      - name: "gateway_order_id"
        type: "number"
        description: ""

      - name: "gateway_transaction_id"
        type: "string"
        description: ""

      - name: "gateway_used"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""
        foreign-key-id: "transaction-id"

      - name: "item_name"
        type: "string"
        description: ""

      - name: "kind"
        type: "string"
        description: ""

      - name: "memo"
        type: "string"
        description: ""

      - name: "original_amount_in_cents"
        type: "number"
        description: ""

      - name: "payment_id"
        type: "number"
        description: ""

      - name: "product_id"
        type: "number"
        description: ""
        foreign-key-id: "product-id"

      - name: "starting_balance_in_cents"
        type: "number"
        description: ""

      - name: "statement_id"
        type: "number"
        description: ""
        foreign-key-id: "statement-id"

      - name: "subscription_id"
        type: "number"
        description: ""
        foreign-key-id: "subscription-id"

      - name: "success"
        type: "boolean"
        description: ""

      - name: "tax_id"
        type: "number"
        description: ""

      - name: "taxable_amount_in_cents"
        type: "number"
        description: ""

      - name: "taxations"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "anything"
            description: ""

      - name: "transaction_type"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---