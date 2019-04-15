---
tap: "netsuite"
version: "1.0"

name: "CurrencyRate"
doc-link: "https://975200-sb2.app.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/currencyrate.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CurrencyRate.json"
description: |
  The `{{ table.name }}` table contains info about currency rate records in you {{ integration.display_name }} account. These are also known as Exchange Rate records in {{ integration.display_name }}.

  {{ integration.permission-for-table | flatify }}

permission:
  tab: "Lists"
  name: "Currency"

# feature-requirements:
#   tab: ""
#   name: ""

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "currency-rate-id"

  - name: "baseCurrency"
    type: "varies"
    description: ""

  - name: "effectiveDate"
    type: "date-time"
    description: ""

  - name: "exchangeRate"
    type: "number, string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "transactionCurrency"
    type: "varies"
    description: ""
---