---
tap: "netsuite"
version: "2"
name: InventoryNumber
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/InventoryNumber.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/InventoryNumber
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
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
