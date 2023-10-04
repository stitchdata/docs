---
tap: "netsuite"
version: "2"
name: CustomerMessage
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CustomerMessage.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/CustomerMessage
description: |
  The `{{ table.name }}` table contains info about standardized customer messages in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "customer-message"

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
- name: description
  type: string
  description: ""
- name: preferred
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---