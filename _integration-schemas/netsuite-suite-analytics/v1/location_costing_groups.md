---
tap: "netsuite-suite-analytics"
version: "1"
key: "location-costing-group"

name: "location_costing_groups"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/location_costing_groups.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "location_costing_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "location-costing-group-id"

  - name: "location_costing_group_name"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""
---