---
tap: "netsuite"
version: "2"
name: SalesTaxItem
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/SalesTaxItem.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/SalesTaxItem
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: description
  type: string
  description: ""
- name: exempt
  type: boolean, string
  description: ""
- name: service
  type: boolean, string
  description: ""
- name: purchaseAccount
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: excludeFromTaxReports
  type: boolean, string
  description: ""
- name: isDefault
  type: boolean, string
  description: ""
- name: parent
  type: varies
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: eccode
  type: boolean, string
  description: ""
- name: effectiveFrom
  type: string
  description: ""
- name: displayName
  type: string
  description: ""
- name: name
  type: string
  description: ""
- name: nexusCountry
  type: varies
  description: ""
- name: taxAccount
  type: varies
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: city
  type: string
  description: ""
- name: saleAccount
  type: varies
  description: ""
- name: taxAgency
  type: varies
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
- name: validUntil
  type: string
  description: ""
- name: rate
  type: string
  description: ""
- name: export
  type: boolean, string
  description: ""
- name: taxType
  type: varies
  description: ""
- name: reverseCharge
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: zip
  type: string
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: available
  type: varies
  description: ""
- name: subsidiaryList
  type: varies
  description: ""
- name: itemId
  type: string
  description: ""
---