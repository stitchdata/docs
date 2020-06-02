---
tap: "netsuite-suite-analytics"
version: "1"
key: "opportunity"

name: "opportunities"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/opportunities.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "accounting_period_id"
    type: "integer"
    description: ""
    foreign-key-id: "accounting-period-id"

  - name: "action_item"
    type: "string"
    description: ""

  - name: "billaddress"
    type: "string"
    description: ""

  - name: "closed"
    type: "date-time"
    description: ""

  - name: "company_status_id"
    type: "integer"
    description: ""
    foreign-key-id: "company-status-id"

  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "email"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "expected_close"
    type: "date-time"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "fob"
    type: "string"
    description: ""

  - name: "forecast_type"
    type: "string"
    description: ""

  - name: "is_tax_reg_override"
    type: "string"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "lead_source_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "memorized"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "needs_bill"
    type: "string"
    description: ""

  - name: "partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "partner-id"

  - name: "payment_terms_id"
    type: "integer"
    description: ""
    foreign-key-id: "payment-term-id"

  - name: "probability"
    type: "number"
    description: ""

  - name: "projected_total"
    type: "number"
    description: ""

  - name: "promotion_code_instance_id"
    type: "integer"
    description: ""
    foreign-key-id: "coupon-code-id"

  - name: "related_tranid"
    type: "string"
    description: ""

  - name: "renewal"
    type: "date-time"
    description: ""

  - name: "reversing_transaction_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction--id"

  - name: "sales_rep_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "shipaddress"
    type: "string"
    description: ""

  - name: "shipment_received"
    type: "date-time"
    description: ""

  - name: "shipping_item_id"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tax_reg_id"
    type: "integer"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "trandate"
    type: "date-time"
    description: ""

  - name: "tranid"
    type: "string"
    description: ""

  - name: "transaction_extid"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""

  - name: "transaction_partner"
    type: "string"
    description: ""

  - name: "transaction_type"
    type: "string"
    description: ""

  - name: "weighted_total"
    type: "integer"
    description: ""

  - name: "win_loss_reason_id"
    type: "integer"
    description: ""
    foreign-key-id: "win-loss-reason-id"
---