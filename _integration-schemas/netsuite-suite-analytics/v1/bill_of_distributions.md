---
tap: "netsuite-suite-analytics"
version: "1"
key: "bill-of-distributions"

name: "bill_of_distributions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bill_of_distributions.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "bill_of_distribution_extid"
    type: "string"
    description: ""

  - name: "bill_of_distribution_id"
    type: "integer"
    netsuiteprimary-key: true
    description: ""
    # foreign-key-id: "bill-of-distribution-id"

  - name: "date_created"
    type:  "date-time"
    description: ""

  - name: "distribution_category_id"
    type: "integer"
    description: ""

  - name: "distribution_network_id"
    type: "integer"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
---