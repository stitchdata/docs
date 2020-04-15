---
tap: "saasoptics"
version: "1"
key: "transaction"

name: "transactions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/transactions.json"
description: |
  The `{{ table.name }}` table contains info about transactions.

replication-method: "Key-based Incremental"

api-method:
  name: "Transaction List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/360000066333-Transactions-CRUD-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "always_use_amount_as_normalized_amount"
    type: "boolean"
    description: ""

  - name: "auditentry_created"
    type: "date-time"
    description: ""

  - name: "auditentry_created_by_name"
    type: "string"
    description: ""

  - name: "auditentry_modified"
    type: "date-time"
    description: ""

  - name: "auditentry_modified_by_name"
    type: "string"
    description: ""

  - name: "automatically_update_revenue"
    type: "boolean"
    description: ""

  - name: "autorenewal_profile"
    type: "integer"
    description: ""
    foreign-key-id: "autorenwal-profile-id"

  - name: "billing_method"
    type: "integer"
    description: ""
    foreign-key-id: "billing-method"

  - name: "cancelled"
    type: "boolean"
    description: ""

  - name: "contract"
    type: "integer"
    description: ""
    foreign-key-id: "contract-id"

  - name: "conversion"
    type: "string"
    description: ""

  - name: "crm_opportunity_id"
    type: "string"
    description: ""

  - name: "crm_opportunity_line_item_id"
    type: "string"
    description: ""

  - name: "different_invoice_item_permitted"
    type: "boolean"
    description: ""

  - name: "do_not_sync_invoices"
    type: "boolean"
    description: ""

  - name: "duration"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "flagged"
    type: "string"
    description: ""

  - name: "foreign_exchange_rate"
    type: "number"
    description: ""

  - name: "home_amount"
    type: "number"
    description: ""

  - name: "home_arr_amount"
    type: "number"
    description: ""

  - name: "home_normalized_amount"
    type: "number"
    description: ""

  - name: "home_normalized_rate"
    type: "number"
    description: ""

  - name: "home_rate"
    type: "number"
    description: ""

  - name: "ili_qb_class"
    type: "string"
    description: ""

  - name: "invoice_description"
    type: "string"
    description: ""

  - name: "is_autorenewal"
    type: "boolean"
    description: ""

  - name: "item"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "item_class"
    type: "integer"
    description: ""

  - name: "local_amount"
    type: "number"
    description: ""

  - name: "local_arr_amount"
    type: "number"
    description: ""

  - name: "local_normalized_amount"
    type: "number"
    description: ""

  - name: "local_normalized_rate"
    type: "number"
    description: ""

  - name: "local_rate"
    type: "number"
    description: ""

  - name: "monthyear"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "number"
    type: "string"
    description: ""

  - name: "number_field1"
    type: "number"
    description: ""

  - name: "number_field2"
    type: "number"
    description: ""

  - name: "order_date"
    type: "date-time"
    description: ""

  - name: "order_number"
    type: "string"
    description: ""

  - name: "project"
    type: "integer"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "recognize"
    type: "boolean"
    description: ""

  - name: "reconcile_required"
    type: "boolean"
    description: ""

  - name: "renew_using_item"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "renewal_amount"
    type: "number"
    description: ""

  - name: "renewal_amount_percentage"
    type: "number"
    description: ""

  - name: "renewal_amount_value"
    type: "number"
    description: ""

  - name: "renewal_duration"
    type: "string"
    description: ""

  - name: "renewal_factor"
    type: "integer"
    description: ""

  - name: "renewal_of_set"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "renewal_probability"
    type: "number"
    description: ""

  - name: "renewal_quantity"
    type: "number"
    description: ""

  - name: "revenue_amount"
    type: "number"
    description: ""

  - name: "revenue_notes"
    type: "string"
    description: ""

  - name: "sales_manager"
    type: "string"
    description: ""

  - name: "sales_rep"
    type: "string"
    description: ""

  - name: "sf_group_id"
    type: "string"
    description: ""

  - name: "sf_id"
    type: "string"
    description: ""

  - name: "sf_opportunity_id"
    type: "string"
    description: ""

  - name: "sf_opportunity_line_item_id"
    type: "string"
    description: ""

  - name: "sf_renewal_opportunity_id"
    type: "string"
    description: ""

  - name: "sf_renewal_opportunity_line_item_id"
    type: "string"
    description: ""

  - name: "sf_renewal_opportunity_rule"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "term_number"
    type: "integer"
    description: ""

  - name: "text_field1"
    type: "string"
    description: ""

  - name: "text_field2"
    type: "string"
    description: ""

  - name: "unbalanced_revenue_exception"
    type: "boolean"
    description: ""
---