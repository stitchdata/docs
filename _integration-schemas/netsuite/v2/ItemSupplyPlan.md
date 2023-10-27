---
tap: "netsuite"
version: "2"
name: ItemSupplyPlan
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemSupplyPlan.html
description: |
  The `{{ table.name }}` table contains info about the item supply plans in your {{ integration.display_name }} account. An item supply plan lists the purchase orders or work orders required to ensure that item quantity meets expected demand.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-supply-plan"

replication-method: "Key-based Incremental"
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: item
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: orderList
  type: varies
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
- name: units
  type: varies
  description: ""
- name: location
  type: varies
  description: ""
- name: memo
  type: string
  description: ""
---