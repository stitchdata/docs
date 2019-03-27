---
tap: "netsuite"
# version: "1.0"

name: "ConsolidatedExchangeRate"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ConsolidatedExchangeRate.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
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

  - name: "internalId"
    type: "string"
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
    type: "anything"
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
