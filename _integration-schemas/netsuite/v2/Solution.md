---
tap: "netsuite"
version: "2"
name: Solution
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Solution.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Solution
description: ""
replication-method: "Key-based Incremental"
table-key-properties: internalId
valid-replication-keys: lastModifiedDate
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: assigned
  type: varies
  description: ""
- name: solutionsList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: lastModifiedDate
  type: string
  description: ""
  replication-key: true
- name: topicsList
  type: varies
  description: ""
- name: title
  type: string
  description: ""
- name: displayOnline
  type: boolean, string
  description: ""
- name: solutionCode
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: status
  type: varies
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: createdDate
  type: string
  description: ""
- name: longDescription
  type: string
  description: ""
- name: message
  type: string
  description: ""
---