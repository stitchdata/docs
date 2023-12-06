---
tap: "netsuite"
version: "2"
name: InventoryNumber
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/InventoryNumber.html
description: |
  The `{{ table.name }}` table contains info about the serial or lot numbers in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "inventory-number"

replication-method: "Full Table"

attributes:
- name: inventoryNumber
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: locationsList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: units
  type: string
  description: ""
- name: memo
  type: string
  description: ""
- name: expirationDate
  type: string
  description: ""
---