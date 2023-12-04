---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-subscription"

name: "billing_subscriptions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_subscriptions.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "subscription_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-subscription-id"

  - name: "advance_renewal_period_number"
    type: "integer"
    description: ""

  - name: "advance_renewal_period_unit_id"
    type: "string"
    description: ""

  - name: "amount"
    type: "number"
    description: ""

  - name: "billing_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-account-id"

  - name: "currency"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_end"
    type: "date-time"
    description: ""

  - name: "date_estimated_revrec_end"
    type: "date-time"
    description: ""

  - name: "date_start"
    type: "date-time"
    description: ""

  - name: "default_renewal_method_id"
    type: "string"
    description: ""

  - name: "default_renewal_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-id"

  - name: "default_renewal_price_book_id"
    type: "integer"
    description: ""

  - name: "default_renewal_term_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-term-id"

  - name: "default_renewal_trantype_id"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "generate_modification_elements"
    type: "string"
    description: ""

  - name: "initial_term_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-term-id"

  - name: "is_auto_renewal"
    type: "string"
    description: ""

  - name: "is_sub_start_date_as_rsd"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-id"

  - name: "price_book_id"
    type: "integer"
    description: ""

  - name: "sales_order_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"

  - name: "subscription_extid"
    type: "string"
    description: ""

  - name: "subscription_number"
    type: "string"
    description: ""

  - name: "subscription_revision"
    type: "integer"
    description: ""
---