---
tap: netsuite
version: "2"
name: Deleted
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Deleted.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Deleted
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId, type
valid-replication-keys: deletedDate
attributes:
- name: deletedDate
  type: string
  description: ""
  replication-key: true
- name: name
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: externalId
  type: string
  description: ""
- name: type
  type: string
  description: ""
  primary-key: true
- name: scriptId
  type: string
  description: ""
- name: customRecord
  type: boolean
  description: ""
