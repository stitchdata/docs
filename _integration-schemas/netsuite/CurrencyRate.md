---
tap: "netsuite"
# version: "1.0"

name: "CurrencyRate"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CurrencyRate.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "baseCurrency"
    type: "varies"
    description: ""

  - name: "effectiveDate"
    type: "date-time"
    description: ""

  - name: "exchangeRate"
    type: "number, string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "transactionCurrency"
    type: "varies"
    description: ""
---
