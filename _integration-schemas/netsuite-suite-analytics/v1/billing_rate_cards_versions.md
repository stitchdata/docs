---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-rate-card-version"

name: "billing_rate_cards_versions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_rate_cards_versions.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "billing_rate_card_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-rate-card-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_effective"
    type: "date-time"
    description: ""

  - name: "last_modified_by_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "version0"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-rate-card-version-id"
---