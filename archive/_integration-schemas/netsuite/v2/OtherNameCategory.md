---
tap: "netsuite"
version: "2"
name: OtherNameCategory
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/OtherNameCategory.html
description: |
  The `{{ table.name }}` table contains info about the other name categories in your {{ integration.display_name }} account. Other name category values are used on other name records to categorize them. The list of other name records is a collection of records for people or companies who are not vendors, customers, or employees.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "other-name-category"

replication-method: "Full Table"

attributes:
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: externalId
  type: string
  description: ""
- name: name
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---