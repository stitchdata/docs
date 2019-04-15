---
tap: "netsuite"
version: "1.0"

name: "ConsolidatedExchangeRate"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/consolidatedexchangerate.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ConsolidatedExchangeRate.json"
description: |
  The `{{ table.name }}` table contains info about consolidated exchange rates. This is used in {{ integration.display_name }} OneWorld for consolidation purposes, ensuring currency amounts correctly roll up from child to parent subsidiaries.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Currency"

feature-requirements:
  - name: "{{ integration.display_name }} OneWorld"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "consolidated-exchange-rate-id"

  - name: "accountingBook"
    type: "string"
    description: ""

  - name: "averageRate"
    type: "number, string"
    description: ""

  - name: "currentRate"
    type: "number, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "fromCurrency"
    type: "string"
    description: ""

  - name: "fromSubsidiary"
    type: "string"
    description: ""

  - name: "historicalRate"
    type: "number, string"
    description: ""

  - name: "isDerived"
    type: "boolean, string"
    description: ""

  - name: "isEliminationSubsidiary"
    type: "boolean, string"
    description: ""

  - name: "isPeriodClosed"
    type: "boolean, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "postingPeriod"
    type: "string"
    description: ""

  - name: "toCurrency"
    type: "string"
    description: ""

  - name: "toSubsidiary"
    type: "string"
    description: ""
---