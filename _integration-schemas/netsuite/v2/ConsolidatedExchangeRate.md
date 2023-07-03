---
tap: "netsuite"
version: "2"
name: ConsolidatedExchangeRate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ConsolidatedExchangeRate.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/ConsolidatedExchangeRate
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: nullFieldList
  type: varies
  description: ""
- name: accountingBook
  type: string
  description: ""
- name: postingPeriod
  type: string
  description: ""
- name: fromSubsidiary
  type: string
  description: ""
- name: isDerived
  type: boolean, string
  description: ""
- name: toCurrency
  type: string
  description: ""
- name: toSubsidiary
  type: string
  description: ""
- name: averageRate
  type: string, number
  description: ""
- name: isPeriodClosed
  type: boolean, string
  description: ""
- name: externalId
  type: string
  description: ""
- name: currentRate
  type: string, number
  description: ""
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: fromCurrency
  type: string
  description: ""
- name: historicalRate
  type: string, number
  description: ""
- name: isEliminationSubsidiary
  type: boolean, string
  description: ""
---