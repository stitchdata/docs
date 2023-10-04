---
tap: "netsuite"
version: "2"
name: TaxGroup
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TaxGroup.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/TaxGroup
description: |
  The `{{ table.name }}` table contains info about the tax groups in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "tax-group"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: taxItemList
  type: varies
  description: ""
- name: taxitem1
  type: varies
  description: ""
- name: isDefault
  type: boolean, string
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: nexusCountry
  type: varies
  description: ""
- name: city
  type: string
  description: ""
- name: county
  type: string
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: state
  type: string
  description: ""
- name: rate
  type: string, number
  description: ""
- name: taxitem2
  type: varies
  description: ""
- name: unitprice1
  type: string
  description: ""
- name: piggyback
  type: boolean, string
  description: ""
- name: taxType
  type: varies
  description: ""
- name: externalId
  type: string
  description: ""
- name: unitprice2
  type: string
  description: ""
- name: zip
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: subsidiaryList
  type: varies
  description: ""
- name: itemId
  type: string
  description: ""
---