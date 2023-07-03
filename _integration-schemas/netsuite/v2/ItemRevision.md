---
tap: "netsuite"
version: "2"
name: ItemRevision
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemRevision.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ItemRevision
description: ""
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: inactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: item
  type: varies
  description: ""
- name: effectiveDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: memo
  type: string
  description: ""
- name: obsoleteDate
  type: string
  description: ""
---