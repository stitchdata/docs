---
tap: "netsuite"
version: "2"
name: BomRevision
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/BomRevision.html
description: |
  The `{{ table.name }}` table contains info about updates on bills of materials.

  {{ integration.permission-for-table | flatify }}
replication-method: "Full Table"
table-key-properties: internalId

key: bom-revision

attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: effectiveStartDate
  type: string
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
- name: componentList
  type: varies
  description: ""
- name: effectiveEndDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: billOfMaterials
  type: varies
  description: ""
- name: createdDate
  type: string
  description: ""
- name: memo
  type: string
  description: ""
---