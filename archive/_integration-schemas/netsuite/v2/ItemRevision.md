---
tap: "netsuite"
version: "2"
name: ItemRevision
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemRevision.html
description: |
  The `{{ table.name }}` table contains info about item revisions in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-revision"

replication-method: "Full Table"

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