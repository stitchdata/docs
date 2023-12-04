---
tap: "netsuite-suite-analytics"
version: "1"
key: "customer-type"

name: "customer_types"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/customer_types.html"
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

  - name: "customer_type_extid"
    type: "string"
    description: ""
  - name: "customer_type_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "customer-type-id"
  
  - name: "isinactive"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "parent_id"
    type: "integer"
    description: ""
---