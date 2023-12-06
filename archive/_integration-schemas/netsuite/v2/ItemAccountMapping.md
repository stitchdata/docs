---
tap: "netsuite"
version: "2"
name: ItemAccountMapping
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemAccountMapping.html
description: |
  The `{{ table.name }}` table contains details about the item account mapping record in your {{ integration.display_name }} account.

  For accounts using {{ integration.display_name }} Multi-Book Accounting, the item account mapping record enables you to configure secondary accounting books to post to accounts different from the primary book, based on the item that is the subject of the transaction. These mappings are used by transactions where the item determines the account to which the transaction posts.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-account-mapping"

replication-method: "Full Table"

attributes:
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: accountingBook
  type: varies
  description: ""
- name: customDimension
  type: varies
  description: ""
- name: destinationAccount
  type: varies
  description: ""
- name: itemAccount
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: sourceAccount
  type: varies
  description: ""
- name: effectiveDate
  type: string
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: endDate
  type: string
  description: ""
- name: externalId
  type: string
  description: ""
- name: customForm
  type: varies
  description: ""
- name: _class
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: location
  type: varies
  description: ""
---