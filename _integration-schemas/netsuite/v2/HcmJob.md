---
tap: "netsuite"
version: "2"
name: HcmJob
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/HcmJob.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/HcmJob
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: title
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: employmentCategory
  type: varies
  description: ""
- name: jobId
  type: string
  description: ""
---