---
tap: "chargify"
version: "1"
key: "invoice"

name: "invoices"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about invoices in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"
replication-key:
  name: "due_date"

api-method:
  name: "Read all invoices"
  doc-link: "https://reference.chargify.com/v1/invoices-legacy/list-all-invoices-by-subscription"
  
attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The invoice ID."
    # foreign-key-id: "invoice-id"

  - name: "amount_due_in_cents"
    type: "number"
    description: ""

  - name: "charges"
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

      - name: "ending_balance_in_cents"
        type: "number"
        description: ""

      - name: "gateway_order_id"
        type: "number"
        description: ""

      - name: "gateway_transaction_id"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""

      - name: "kind"
        type: "string"
        description: ""

      - name: "memo"
        type: "string"
        description: ""

      - name: "payment_id"
        type: "number"
        description: ""
        foreign-key-id: "transaction-id"

      - name: "product_id"
        type: "number"
        description: ""
        foreign-key-id: "product-id"

      - name: "starting_balance_in_cents"
        type: "number"
        description: ""

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

      - name: "transaction_type"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "number"
    type: "number"
    description: ""

  - name: "paid_at"
    type: "date-time"
    description: ""

  - name: "payments_and_credits"
    type: "array"
    description: ""
    subattributes:
      - name: "amount_in_cents"
        type: "number"
        description: ""

      - name: "card_expiration"
        type: "string"
        description: ""

      - name: "card_number"
        type: "string"
        description: ""

      - name: "card_type"
        type: "string"
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

      - name: "ending_balance_in_cents"
        type: "number"
        description: ""

      - name: "gateway_order_id"
        type: "number"
        description: ""

      - name: "gateway_transaction_id"
        type: "string"
        description: ""

      - name: "id"
        type: "number"
        description: ""

      - name: "kind"
        type: "string"
        description: ""

      - name: "memo"
        type: "string"
        description: ""

      - name: "payment_id"
        type: "number"
        description: ""
        foreign-key-id: "transaction-id"

      - name: "product_id"
        type: "number"
        description: ""
        foreign-key-id: "product-id"

      - name: "starting_balance_in_cents"
        type: "number"
        description: ""

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

      - name: "transaction_type"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "site_id"
    type: "number"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "statement_id"
    type: "number"
    description: ""
    foreign-key-id: "statement-id"

  - name: "subscription_id"
    type: "number"
    description: ""
    foreign-key-id: "subscription-id"

  - name: "total_amount_in_cents"
    type: "number"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
---