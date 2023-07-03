---
tap: netsuite
version: "2"
name: Account
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/Account.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/Account
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: description
  type: string
  description: ""
- name: acctNumber
  type: string
  description: ""
- name: department
  type: varies
  description: ""
- name: nullFieldList
  type: varies
  description: ""
- name: acctName
  type: string
  description: ""
- name: cashFlowRate
  type: varies
  description: ""
- name: parent
  type: varies
  description: ""
- name: includeChildren
  type: boolean, string
  description: ""
- name: eliminate
  type: boolean, string
  description: ""
- name: localizationsList
  type: varies
  description: ""
- name: unit
  type: varies
  description: ""
- name: exchangeRate
  type: string
  description: ""
- name: customFieldList
  type: varies
  description: ""
- name: isInactive
  type: boolean, string
  description: ""
- name: deferralAcct
  type: varies
  description: ""
- name: restrictToAccountingBookList
  type: varies
  description: ""
- name: acctType
  type: varies
  description: ""
- name: legalName
  type: string
  description: ""
- name: inventory
  type: boolean, string
  description: ""
- name: currency
  type: varies
  description: ""
- name: openingBalance
  type: string, number
  description: ""
- name: revalue
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: generalRate
  type: varies
  description: ""
- name: _class
  type: varies
  description: ""
- name: unitsType
  type: varies
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: curDocNum
  type: string, integer
  description: ""
- name: billableExpensesAcct
  type: varies
  description: ""
- name: subsidiaryList
  type: varies
  description: ""
- name: tranDate
  type: string
  description: ""
- name: location
  type: varies
  description: ""
- name: category1099Misc
  type: varies
  description: ""
