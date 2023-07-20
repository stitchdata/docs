---
tap: "netsuite"
version: "2"
name: Folder
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Folder.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Folder
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
replication-key:
  name: lastModifiedDate
attributes:
- name: description
  type: string
  description: ""
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: bundleable
  type: boolean, string
  description: ""
- name: group
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: folderType
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: _class
  type: varies
  description: ""
- name: hideInBundle
  type: boolean, string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: isPrivate
  type: boolean, string
  description: ""
- name: location
  type: varies
  description: ""
---