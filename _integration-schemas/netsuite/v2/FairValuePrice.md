---
tap: "netsuite"
version: "2"
name: FairValuePrice
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/FairValuePrice.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/FairValuePrice
description: |
  The `{{ table.name }}` table contains info about the fair value price list in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "fair-value-price"

replication-method: "Full Table"

attributes:
- name: lowValuePercent
  type: string, number
  description: ""
- name: highValuePercent
  type: string, number
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: itemRevenueCategory
  type: varies
  description: ""
- name: dimensionList
  type: varies
  description: ""
- name: fairValueRangePolicy
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
- name: isVsoePrice
  type: boolean, string
  description: ""
- name: highValue
  type: string, number
  description: ""
- name: fairValueFormula
  type: varies
  description: ""
- name: fairValue
  type: string, number
  description: ""
- name: currency
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
- name: unitsType
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: lowValue
  type: string, number
  description: ""
- name: units
  type: varies
  description: ""
---