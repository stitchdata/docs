---
tap: "chargify"
version: "1"
key: "transaction"

name: "transactions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/transactions.json"
description: |
  The `{{ table.name }}` table contains info about the transactions for your {{ integration.display_name }} site.

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

api-method:
  name: "Read transactions for a site"
  doc-link: "https://reference.chargify.com/v1/transactions/list-transactions-for-the-site"
  
attributes:
  - name: "id"
    type: "number"
    primary-key: true
    description: "The transaction ID."
    foreign-key-id: "transaction-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: ""

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

  - name: "gateway_used"
    type: "string"
    description: ""

  - name: "item_name"
    type: "string"
    description: ""

  - name: "kind"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "number"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "payment_id"
    type: "number"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "product_id"
    type: "number"
    description: ""
    foreign-key-id: "product-id"

  - name: "refunded_amount_in_cents"
    type: "number"
    description: ""

  - name: "role"
    type: "string"
    description: ""

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

  - name: "transaction_type"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---