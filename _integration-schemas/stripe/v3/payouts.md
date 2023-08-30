---
tap: "stripe"
version: "3"
key: ""

name: "payouts"
doc-link: "https://stripe.com/docs/api/payouts"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/payouts.json
description: |
  The `{{ table.name }}` table contains info about payouts, which occur when you receive funds from {{ integration.display_name }} or initiate a payout to a bank account of the debit card of a connected {{ integration.display_name }} account.


replication-method: "Key-based Incremental"

api-method:
    name: "List all payouts"
    doc-link: "https://stripe.com/docs/api/payouts/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The payout ID."
    foreign-key-id: "payout-id"
     
  - name: "created"
    type: "string"
    replication-key: true
    description: "The time at which the payout was created. Measured in seconds since the Unix epoch."

  - name: "amount"
    type: "integer"
    description: ""

  - name: "amount_reversed"
    type: "integer"
    description: ""

  - name: "arrival_date"
    type: "string"
    description: ""

  - name: "automatic"
    type: "boolean"
    description: ""

  - name: "balance_transaction"
    type: "string"
    description: "The ID of the balance transaction that describes the impact of this payout on your account balance."
    foreign-key-id: "balance-transaction-id"

  - name: "bank_account"
    type: "object"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "routing_number"
      type: "string"
      description: ""

    - name: "account_holder_type"
      type: "string"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "bank_name"
      type: "string"
      description: ""

    - name: "last4"
      type: "string"
      description: ""

    - name: "fingerprint"
      type: "string"
      description: ""

    - name: "account_holder_name"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "status"
      type: "string"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "date"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "destination"
    type: "string"
    description: ""

  - name: "failure_balance_transaction"
    type: "string"
    description: "If the payout failed or was canceled, this will be the ID of the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance."
    foreign-key-id: "balance-transaction-id"

  - name: "failure_code"
    type: "string"
    description: ""

  - name: "failure_message"
    type: "string"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "method"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "original_payout"
    type: "string"
    description: ""

  - name: "recipient"
    type: "string"
    description: ""

  - name: "reversed_by"
    type: "string"
    description: ""

  - name: "source_transaction"
    type: "string"
    description: ""

  - name: "source_type"
    type: "string"
    description: ""

  - name: "statement_description"
    type: "string"
    description: ""

  - name: "statement_descriptor"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "transfer_group"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---