---
tap: "netsuite"
version: "2"
name: ItemDemandPlan
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ItemDemandPlan.html
description: |
  The `{{ table.name }}` table contains info about item demand plans in your {{ integration.display_name }} account. An item demand plan transaction stores the quantity expected to be needed, during specified time periods, for an item.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "item-demand-plan"

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
- name: startDate
  type: string
  description: ""
- name: month
  type: varies
  description: ""
- name: demandPlanCalendarType
  type: varies
  description: ""
- name: subsidiary
  type: varies
  description: ""
- name: year
  type: string, integer
  description: ""
- name: endDate
  type: string
  description: ""
- name: demandPlanMatrix
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