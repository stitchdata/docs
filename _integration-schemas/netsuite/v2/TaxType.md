---
tap: "netsuite"
version: "2"
name: TaxType
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/TaxType.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/TaxType
description: |
  The `{{ table.name }}` table contains info about the tax types in your {{ integration.display_name }} account. A tax type determines where the tax paid or collected is tracked on the balance sheet. The balance sheet account to which {{ integration.display_name }} posts the collection or payment of tax is called the tax control account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "tax-type"
replication-method: "Full Table"
table-key-properties: internalId

attributes:
- name: description
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: name
  type: string
  description: ""
- name: nexusAccountsList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: doesNotAddToTotal
  type: boolean, string
  description: ""
- name: nexusesTaxList
  type: varies
  description: ""
- name: postToItemCost
  type: boolean, string
  description: ""
- name: reverseCharge
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: country
  type: varies
  description: ""
- name: taxInNetAmount
  type: boolean, string
  description: ""
---