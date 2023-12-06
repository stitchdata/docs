---
tap: "netsuite"
version: "2"
name: CurrencyRate
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2023_1/schema/record/CurrencyRate.html
description: |
  The `{{ table.name }}` table contains info about currency rate records in you {{ integration.display_name }} account. These are also known as Exchange Rate records in {{ integration.display_name }}.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "currency-rate"

replication-method: "Full Table"

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
---