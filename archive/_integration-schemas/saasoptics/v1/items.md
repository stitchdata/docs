---
tap: "saasoptics"
version: "1"
key: "item"

name: "items"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/items.json"
description: |
  The `{{ table.name }}` table contains info about items, which are products and services you sell.

replication-method: "Key-based Incremental"

api-method:
  name: "Items List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013751567-Items-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "item-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "asset_account"
    type: "integer"
    description: ""

  - name: "avatax_id"
    type: "string"
    description: ""

  - name: "avatax_sales_tax_code"
    type: "string"
    description: ""

  - name: "billing_description"
    type: "string"
    description: ""

  - name: "billing_method"
    type: "integer"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "create_revenue"
    type: "boolean"
    description: ""

  - name: "default_duration"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "enable_create_transactions"
    type: "boolean"
    description: ""

  - name: "enforce_start_date_after_end_date"
    type: "boolean"
    description: ""

  - name: "gl_created"
    type: "date-time"
    description: ""

  - name: "gl_description"
    type: "string"
    description: ""

  - name: "gl_is_active"
    type: "boolean"
    description: ""

  - name: "gl_modified"
    type: "date-time"
    description: ""

  - name: "gl_name"
    type: "string"
    description: ""

  - name: "income_account"
    type: "integer"
    description: ""

  - name: "intacct_id"
    type: "string"
    description: ""

  - name: "intacct_modified"
    type: "date-time"
    description: ""

  - name: "intacct_recordno"
    type: "string"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "is_discount"
    type: "boolean"
    description: ""

  - name: "is_sales_tax"
    type: "boolean"
    description: ""

  - name: "is_taxable"
    type: "boolean"
    description: ""

  - name: "liability_account"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "needs_so_profile"
    type: "boolean"
    description: ""

  - name: "netsuite_id"
    type: "string"
    description: ""

  - name: "netsuite_modified"
    type: "date-time"
    description: ""

  - name: "normalized_term"
    type: "string"
    description: ""

  - name: "product_family"
    type: "string"
    description: ""

  - name: "qb_account"
    type: "integer"
    description: ""

  - name: "qb_id"
    type: "string"
    description: ""

  - name: "qb_only"
    type: "boolean"
    description: ""

  - name: "qb_sales_tax_code"
    type: "string"
    description: ""

  - name: "recurly_id"
    type: "string"
    description: ""

  - name: "recurring"
    type: "boolean"
    description: ""

  - name: "renew_all_open_transactions"
    type: "boolean"
    description: ""

  - name: "renew_using_same_item"
    type: "boolean"
    description: ""

  - name: "revenue_recognition_method"
    type: "integer"
    description: ""

  - name: "sf_do_not_sync"
    type: "boolean"
    description: ""

  - name: "source_system"
    type: "string"
    description: ""

  - name: "stripe_id"
    type: "string"
    description: ""

  - name: "sync_invoices"
    type: "boolean"
    description: ""

  - name: "transaction_end_date"
    type: "date-time"
    description: ""

  - name: "transaction_start_date"
    type: "date-time"
    description: ""

  - name: "wizard_enabled"
    type: "boolean"
    description: ""
---