---
tap: "stripe"
version: "1.0"

name: "transfers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/transfers.json"
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
    type: "date-time"
    replication-key: true
    description: "The time the transfer was created. Measured in seconds since the Unix epoch."

  - name: "amount"
    type: "integer"
    description: "The amount (in cents) to be transferred."

  - name: "amount_reversed"
    type: "integer"
    description: "The amount (in cents) reversed."

  - name: "arrival_date"
    type: "date-time"
    description: "The date the transfer arrived."

  - name: "automatic"
    type: "boolean"
    description: ""

  - name: "balance_transaction"
    type: "string"
    description: "The ID of the balance transaction that describes the impact of the transfer on your account balance."
    foreign-key-id: "balance-transaction-id"

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"} of the currency the transfer is in.

  - name: "date"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: "The description of the transfer."

  - name: "destination"
    type: "string"
    description: "The ID of the {{ integration.display_name }} account the transfer was sent to."

  - name: "failure_balance_transaction"
    type: "string"
    description: "If the transfer failed or was canceled, this will be the ID of the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance."
    foreign-key-id: "balance-transaction-id"

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: ""
    object-attributes:

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `transfer`."

  - name: "recipient"
    type: "string"
    description: ""

  - name: "reversals"
    type: "array"
    description: ""

  - name: "reversed"
    type: "boolean"
    description: "Indicates whether the transfer has been fully reversed. If the transfer was only partially reversed, this will still be `false`."

  - name: "source_transaction"
    type: "string"
    description: "The ID of the charge or payment that was used to fund the transfer."

  - name: "source_type"
    type: "string"
    description: |
      The source balance the transfer came from. Possible values are:

      - `card`
      - `bank_account`
      - `alipay_account`

  - name: "statement_description"
    type: "string"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "statement_descriptor"
    type: "string"
    description: "Additional information that displays on the statment."

  - name: "transfer_group"
    type: "string"
    description: "A string that identifies the transfer as part of a group."

  - name: "updated"
    type: "date-time"
    description: ""
---