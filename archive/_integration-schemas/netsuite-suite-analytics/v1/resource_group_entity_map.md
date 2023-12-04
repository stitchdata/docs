---
tap: "netsuite-suite-analytics"
version: "1"
key: "resource-group-entity-map"

name: "resource_group_entity_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/resource_group_entity_map.html"
description: |
  From NetSuite's documentation:

  > This table contains data related to the assigned members of a resource group. Each resource group entity must have an assigned resource group. The table’s data is only available for accounts with Project Management enabled.

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "entity_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "entity-id"

  - name: "group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    # foreign-key-id: "resource-group-id"
---