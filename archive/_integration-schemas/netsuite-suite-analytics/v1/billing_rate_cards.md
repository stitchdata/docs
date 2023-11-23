---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-rate-card"

name: "billing_rate_cards"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billingratecard.html"
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

  - name: "billing_rate_card_extid"
    type: "string"
    description: ""

  - name: "billing_rate_card_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-rate-card-id"

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---