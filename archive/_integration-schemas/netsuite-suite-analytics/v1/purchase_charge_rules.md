---
tap: "netsuite-suite-analytics"
version: "1"
key: "purchase-charge-rule"

name: "purchase_charge_rules"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/purchase_charge_rules.html"
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

  - name: "cap"
    type: "number"
    description: ""

  - name: "charge_rule_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "purchase-charge-rule-id"

  - name: "charge_rule_type_id"
    type: "string"
    description: ""

  - name: "charge_stage_id"
    type: "string"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "mark_up_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "project_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "purchase_charge_rule_extid"
    type: "string"
    description: ""

  - name: "purchase_saved_search_id"
    type: "integer"
    description: ""

  - name: "rate_multiplier"
    type: "number"
    description: ""

  - name: "rule_name"
    type: "string"
    description: ""

  - name: "rule_order"
    type: "integer"
    description: ""
---