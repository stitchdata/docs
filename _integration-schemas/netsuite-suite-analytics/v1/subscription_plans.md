---
tap: "netsuite-suite-analytics"
version: "1"
key: "subscription-plan"

name: "subscription_plans"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/subscriptionplan.html"
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

  - name: "advance_renewal_period_number"
    type: "string"
    description: ""

  - name: "advance_renewal_period_unit_id"
    type: "string"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "default_renewal_method_id"
    type: "string"
    description: ""

  - name: "default_renewal_plan_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-plan-id"

  - name: "default_renewal_term_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-term-id"

  - name: "default_renewal_trantype_id"
    type: "string"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""
    foreign-key-id: "department-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "income_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "initial_term_id"
    type: "integer"
    description: ""
    foreign-key-id: "subscription-term-id"

  - name: "is_auto_renewal"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_include_children"
    type: "string"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "plan_extid"
    type: "string"
    description: ""

  - name: "plan_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "subscription-plan-id"

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"
---