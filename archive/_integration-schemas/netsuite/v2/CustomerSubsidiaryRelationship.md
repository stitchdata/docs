---
tap: "netsuite"
version: "2"
name: CustomerSubsidiaryRelationship
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerSubsidiaryRelationship.html
description: |
  The `{{ table.name }}` table contains info about customers shared with multiple subsidiaries.

  {{ integration.permission-for-table | flatify }}
replication-method: "Full Table"
table-key-properties: internalId

key: customer-subsidiary-relationship

attributes:
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: externalId
  type: string
  description: ""
- name: entity
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: isPrimarySub
  type: boolean, string
  description: ""
- name: primaryCurrency
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---