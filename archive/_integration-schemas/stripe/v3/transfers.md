---
tap: "stripe"
version: "3"
key: ""

name: "transfers"
doc-link: 
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/transfers.json
description: |
  The `{{ table.name }}` table contains info about transfers sent to connected accounts.

replication-method: "Key-based Incremental"

api-method:
    name: "List all transfers"
    doc-link: "https://stripe.com/docs/api/transfers/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The transfer ID."
    foreign-key-id: "transfer-id"
    
  - name: "created"
    type: "string"
    replication-key: true
    description: "The time the transfer was created. Measured in seconds since the Unix epoch."

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
    description: "The ID of the balance transaction that describes the impact of the transfer on your account balance."
    foreign-key-id: "balance-transaction-id"

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
    description: "If the transfer failed or was canceled, this will be the ID of the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance."
    foreign-key-id: "balance-transaction-id"

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "recipient"
    type: "string"
    description: ""

  - name: "reversals"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "object"
      description: ""

  - name: "reversed"
    type: "boolean"
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

  - name: "transfer_group"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---