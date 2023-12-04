---
tap: "netsuite-suite-analytics"
version: "1"
key: "global-inventory-relationship"

name: "global_inventory_relationships"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/globalinventoryrelationship.html"
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
  - name: "global_invt_relationship_extid"
    type: "string"
    description: ""
  - name: "global_invt_relationship_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
  - name: "inventory_subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"
  - name: "is_all_locations_cust_return"
    type: "string"
    description: ""
  - name: "is_all_locations_fulfillment"
    type: "string"
    description: ""
  - name: "is_allow_cross_sub_cust_return"
    type: "string"
    description: ""
  - name: "is_allow_cross_sub_fulfillment"
    type: "string"
    description: ""
  - name: "is_inactive"
    type: "string"
    description: ""
  - name: "originating_subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"
---