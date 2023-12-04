---
tap: "twilio"
version: "1"
key: ""

name: "account_balance"
doc-link: ""
singer-schema: https://github.com/singer-io/tap-twilio/tree/master/tap_twilio/schemas/account_balance.json
description: |
  The **{{ table.name }}** returns your {{ integration.display_name }} acocunt balance.

replication-method: "Full Table"  

api-method:
    name: "Account Balance"
    doc-link: ""

attributes:
  - name: "account_sid"
    type: "string"
    primary-key: true
    description: "A 34 character string that uniquely identifies the account"

  - name: "balance"
    type: "number"
    description: "Remaining account balance"

  - name: "currency"
    type: "string"
    description: "Currency type"
---