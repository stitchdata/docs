---
tap: "netsuite"
version: "2"
name: ContactCategory
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ContactCategory.html
description: |
  The `{{ table.name }}` table contains info about the types of contacts in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "contact-category"

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
- name: _private
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---