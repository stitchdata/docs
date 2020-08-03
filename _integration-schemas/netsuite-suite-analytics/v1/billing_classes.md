---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-class"

name: "billing_classes"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billing_classes.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "billing_class_extid"
    type: "string"
    description: ""

  - name: "billing_class_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "billing-class-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "sale_unit_id"
    type: "integer"
    description: ""

  - name: "units_type_id"
    type: "integer"
    description: ""
---