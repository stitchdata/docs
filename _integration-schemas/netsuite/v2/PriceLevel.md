---
tap: "netsuite"
version: "2"
name: PriceLevel
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/PriceLevel.html
description: |
  The `{{ table.name }}` table contains info about the price level list in your {{ integration.display_name }} account. Price level defines a list of values that are used by opportunity and item records to set the price level for a specific item.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "price-level"

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
- name: discountpct
  type: string, number
  description: ""
- name: updateExistingPrices
  type: boolean, string
  description: ""
- name: isOnline
  type: boolean, string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
---