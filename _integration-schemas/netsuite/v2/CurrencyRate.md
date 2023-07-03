---
tap: netsuite
version: "2"
name: CurrencyRate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CurrencyRate.html
singer-schema: https://github.com/stitchdata/tap-netsuite/tree/master/tap_v2/schemas/CurrencyRate
description: ""
replication-method: "Full Table"
table-key-properties: internalId
valid-replication-keys: ""
attributes:
- name: internalId
  type: string
  description: ""
  primary-key: true
- name: baseCurrency
  type: varies
  description: ""
- name: transactionCurrency
  type: varies
  description: ""
- name: exchangeRate
  type: string, number
  description: ""
- name: effectiveDate
  type: string
  description: ""
- name: currencyRateType
  type: string
  description: ""
- name: nullFieldList
  type: varies
  description: ""
