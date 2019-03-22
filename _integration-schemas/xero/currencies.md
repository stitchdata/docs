---
tap: "xero"
version: "1.0"

name: "currencies"
doc-link: &api-doc https://developer.xero.com/documentation/api/currencies
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/currencies.json
description: |
  The `{{ table.name }}` table contains info about the currencies available in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: getCurrencies
  doc-link: *api-doc

attributes:
  - name: "Code"
    type: "string"
    primary-key: true
    description: "The three letter alpha code for the currency. Refer to [XE.com](http://www.xe.com/iso4217.php) for a list of codes."
    foreign-key-id: "currency-code"

  - name: "Description"
    type: "string"
    description: "The name of the currency."
---