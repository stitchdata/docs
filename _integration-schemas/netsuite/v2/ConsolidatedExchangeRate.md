---
tap: "netsuite"
version: "2"
name: ConsolidatedExchangeRate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/ConsolidatedExchangeRate.html
description: |
  The `{{ table.name }}` table contains info about consolidated exchange rates. This is used in {{ integration.display_name }} OneWorld for consolidation purposes, ensuring currency amounts correctly roll up from child to parent subsidiaries.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "consolidated-exchange-rate"

replication-method: "Full Table"

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