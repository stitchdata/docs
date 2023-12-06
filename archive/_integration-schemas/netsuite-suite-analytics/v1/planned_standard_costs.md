---
tap: "netsuite-suite-analytics"
version: "1"
key: "planned-standard-cost"

name: "planned_standard_costs"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/planned_standard_costs.html"
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

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "memo"
    type: "string"
    description: ""

  - name: "planned_standard_cost_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "planned-standard-cost-id"

  - name: "standard_cost_version_id"
    type: "integer"
    description: ""
---