---
tap: "netsuite"
version: "2"
name: Classification
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Classification.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Classification
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: name
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: classTranslationList
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: subsidiaryList
  type: varies
  description: ""
