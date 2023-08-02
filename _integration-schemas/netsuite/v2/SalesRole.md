---
tap: "netsuite"
version: "2"
name: SalesRole
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SalesRole.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/SalesRole
description: |
  The `{{ table.name }}` table contains info about the sales roles in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "sales-role"
replication-method: "Full Table"
table-key-properties: internalId

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
- name: isSalesRep
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---