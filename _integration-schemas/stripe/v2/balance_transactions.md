---
tap: "stripe"
version: "2"
key: ""

name: "balance_transactions"
doc-link: "https://stripe.com/docs/api/balance/balance_transaction"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/balance_transactions.json
description: "The `{{ table.name }}` table contains info about transactions have have contributed to your Stripe account balance, including charges, transfers, etc."

replication-method: "Key-based Incremental"

api-method:
  name: "List all balance history"
  doc-link: "https://stripe.com/docs/api/balance/balance_history"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The balance transaction ID."
    foreign-key-id: "balance-transaction-id"

  - name: "created"
    type: "string"
    replication-key: true
    description: "The time at which the object was created."  

  - name: "amount"
    type: "integer"
    description: ""

  - name: "available_on"
    type: "integer"
    description: ""

  - name: "currency"
    type: "string"
    description: &currency
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}.

  - name: "description"
    type: "string"
    description: &description
      An arbitrary string attached to the object. Often useful for displaying to users.

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "fee"
    type: "integer"
    description: ""

  - name: "fee_details"
    type: "array"
    description: "Detailed breakdown of fees (in cents) paid for this transaction."
    subattributes:
      - name: "application"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: *description

      - name: "amount"
        type: "integer"
        description: "Amount of the fee, in cents."

      - name: "currency"
        type: "string"
        description: *currency

  - name: "net"
    type: "integer"
    description: "Net amount of the transaction, in cents."

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `balance_transaction`."

  - name: "source"
    type: "string"
    description: |
      The {{ integration.display_name }} object to which this transaction is related.

  - name: "sourced_transfers"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: ""
        description: ""

  - name: "status"
    type: "string"
    description: "Indicates if the transaction's net funds are available in the {{ integration.display_name }}. Possible values are `available` or `pending`."

  - name: "type"
    type: "string"
    description: |
      The type of the transaction. Refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/reporting/balance-transaction-types){:target="new} for a list of possible values.

  - name: "updated"
    type: "string"
    description: "The time at which the balance transaction was last updated."
---