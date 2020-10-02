---
tap: "saasoptics"
version: "1"
key: "invoice"

name: "invoices"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about invoices in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Invoice List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013918148-Invoices-CRUD-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "invoice-id"

  - name: "auditentry_modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "applied_amount"
    type: "number"
    description: ""

  - name: "auditentry_created"
    type: "date-time"
    description: ""

  - name: "auditentry_created_by_name"
    type: "string"
    description: ""

  - name: "auditentry_modified_by_name"
    type: "string"
    description: ""

  - name: "auditentry_qb_created"
    type: "date-time"
    description: ""

  - name: "auditentry_qb_modified"
    type: "date-time"
    description: ""

  - name: "avatax_commit_timestamp"
    type: "date-time"
    description: ""

  - name: "avatax_id"
    type: "string"
    description: ""

  - name: "avatax_modify_timestamp"
    type: "date-time"
    description: ""

  - name: "avatax_reconciliation_status"
    type: "string"
    description: ""

  - name: "avatax_status"
    type: "string"
    description: ""

  - name: "balance"
    type: "number"
    description: ""

  - name: "billing_addr1"
    type: "string"
    description: ""

  - name: "billing_addr2"
    type: "string"
    description: ""

  - name: "billing_addr3"
    type: "string"
    description: ""

  - name: "billing_city"
    type: "string"
    description: ""

  - name: "billing_country"
    type: "string"
    description: ""

  - name: "billing_state"
    type: "string"
    description: ""

  - name: "billing_zip_code"
    type: "string"
    description: ""

  - name: "contract"
    type: "integer"
    description: ""

  - name: "date"
    type: "date-time"
    description: ""

  - name: "deleted_in_qb"
    type: "boolean"
    description: ""

  - name: "do_not_sync"
    type: "boolean"
    description: ""

  - name: "due_date"
    type: "date-time"
    description: ""

  - name: "ei_theme"
    type: "integer"
    description: ""

  - name: "email_from_so"
    type: "boolean"
    description: ""

  - name: "enable_ach_payment"
    type: "boolean"
    description: ""

  - name: "enable_cc_payment"
    type: "boolean"
    description: ""

  - name: "exported_date"
    type: "date-time"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "foreign_exchange_rate"
    type: "number"
    description: ""

  - name: "ignore_date_when_syncing"
    type: "boolean"
    description: ""

  - name: "is_paid"
    type: "boolean"
    description: ""

  - name: "line_items"
    type: "array"
    description: ""
    subattributes:
      - name: "deleted_in_qb"
        type: "boolean"
        description: ""

      - name: "exported_date"
        type: "date-time"
        description: ""

      - name: "external_id"
        type: "string"
        description: ""

      - name: "home_amount"
        type: "number"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "invoice"
        type: "integer"
        description: ""
        foreign-key-id: "invoice-id"

      - name: "item"
        type: "integer"
        description: ""
        foreign-key-id: "item-id"

      - name: "local_amount"
        type: "number"
        description: ""

      - name: "modified"
        type: "date-time"
        description: ""

      - name: "no_transaction_permitted"
        type: "boolean"
        description: ""

      - name: "notes"
        type: "string"
        description: ""

      - name: "number"
        type: "string"
        description: ""

      - name: "qb_class"
        type: "integer"
        description: ""

      - name: "qb_time_modified"
        type: "date-time"
        description: ""

      - name: "qb_txn_line_id"
        type: "string"
        description: ""

      - name: "quantity"
        type: "number"
        description: ""

      - name: "recurly_id"
        type: "string"
        description: ""

      - name: "refund_of"
        type: "integer"
        description: ""

      - name: "refund_of_stripe_id"
        type: "string"
        description: ""

      - name: "sf_id"
        type: "string"
        description: ""

      - name: "stripe_id"
        type: "string"
        description: ""

      - name: "sync_date"
        type: "date-time"
        description: ""

      - name: "transaction"
        type: "integer"
        description: ""
        foreign-key-id: "transaction-id"
  - name: "memo"
    type: "string"
    description: ""

  - name: "number"
    type: "string"
    description: ""

  - name: "other"
    type: "string"
    description: ""

  - name: "po_number"
    type: "string"
    description: ""

  - name: "qb_ar_account"
    type: "integer"
    description: ""

  - name: "qb_class"
    type: "integer"
    description: ""

  - name: "qb_currency"
    type: "integer"
    description: ""

  - name: "qb_customer_message"
    type: "integer"
    description: ""

  - name: "qb_number"
    type: "string"
    description: ""

  - name: "qb_payment_terms"
    type: "integer"
    description: ""

  - name: "qb_sales_rep"
    type: "integer"
    description: ""

  - name: "qb_template"
    type: "integer"
    description: ""

  - name: "qb_txn_id"
    type: "string"
    description: ""

  - name: "recurly_id"
    type: "string"
    description: ""

  - name: "refund_of"
    type: "integer"
    description: ""

  - name: "sales_tax"
    type: "number"
    description: ""

  - name: "sales_tax_percentage"
    type: "number"
    description: ""

  - name: "sf_id"
    type: "string"
    description: ""

  - name: "ship_date"
    type: "date-time"
    description: ""

  - name: "shipping_addr1"
    type: "string"
    description: ""

  - name: "shipping_addr2"
    type: "string"
    description: ""

  - name: "shipping_addr3"
    type: "string"
    description: ""

  - name: "shipping_city"
    type: "string"
    description: ""

  - name: "shipping_country"
    type: "string"
    description: ""

  - name: "shipping_state"
    type: "string"
    description: ""

  - name: "shipping_zip_code"
    type: "string"
    description: ""

  - name: "stripe_id"
    type: "string"
    description: ""

  - name: "stripe_refund_id"
    type: "string"
    description: ""

  - name: "subtotal"
    type: "number"
    description: ""

  - name: "sync_date"
    type: "date-time"
    description: ""

  - name: "to_be_emailed"
    type: "boolean"
    description: ""

  - name: "to_be_printed"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---