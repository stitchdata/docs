---
tap: netsuite
version: "2"
name: MerchandiseHierarchyNode
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/MerchandiseHierarchyNode.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/MerchandiseHierarchyNode
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: externalId
  type: string
  description: ""
- name: name
  type: string
  description: ""
- name: description
  type: string
  description: ""
- name: hierarchyVersionsList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
