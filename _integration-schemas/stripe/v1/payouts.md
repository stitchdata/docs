---
tap: "stripe"
version: "1.0"

name: "payouts"
doc-link: "https://stripe.com/docs/api/payouts"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/payouts.json"
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
    type: "date-time"
    replication-key: true
    description: "The time at which the payout was created. Measured in seconds since the Unix epoch."

  - name: "amount"
    type: "integer"
    description: "The amount (in cents) to be transferred to your bank account or debit card."

  - name: "amount_reversed"
    type: "integer"
    description: ""

  - name: "arrival_date"
    type: "date-time"
    description: "The date the payout is expected to arrive in the bank."

  - name: "automatic"
    type: "boolean"
    description: "Indicates if the payout was created by an automated payout schedule (`true`) or if it was requested manually (`false`)."

  - name: "balance_transaction"
    type: "string"
    description: "The ID of the balance transaction that describes the impact of this payout on your account balance."
    foreign-key-id: "balance-transaction-id"

  - name: "bank_account"
    type: "object"
    description: "Details about the bank account the payout is being sent to."
    doc-link: "https://stripe.com/docs/api/customer_bank_accounts/object"
    object-attributes:
      - name: "account_holder_name"
        type: "string"
        description: "The name of the person or business that owns the bank account."

      - name: "account_holder_type"
        type: "string"
        description: "The type of entity that holds the account. Possible values are `individual` or `company`."

      - name: "bank_name"
        type: "string"
        description: "The name of the bank associated with the routing number. For example: `WELLS FARGO`"

      - name: "country"
        type: "string"
        description: "The two-letter ISO code representing the country the bank account is located in."

      - name: "currency"
        type: "string"
        description: |
          The three-letter [ISO  code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"} for the currency paid out to the bank account.

      - name: "fingerprint"
        type: "string"
        description: "Uniquely identifies the bank account."

      - name: "id"
        type: "string"
        description: "The bank account ID in {{ integration.display_name }}."
        # foreign-key-id: "bank-account-id"

      - name: "last4"
        type: "string"
        description: "The last four digits associated with the bank account."

      - name: "metadata"
        type: "object"
        description: ""
        object-attributes:

      - name: "name"
        type: "string"
        description: "**Deprecated by {{ integration.display_name }}.**"

      - name: "object"
        type: "string"
        description: "The type of {{ integration.display_name }} object. This will be `bank_account`."

      - name: "routing_number"
        type: "string"
        description: "The routing transit number for the bank account."

      - name: "status"
        type: "string"
        description: |
          The status of the bank account. Possible values are:

          - `new` - Indicates the bank account hasn't been validated or had any activity.
          - `validated` - Indicates that {{ integration.display_name }} has determined the bank account exists.
          - `verified` - Indicates that bank account verification has succeeded.
          - `verification_failed` - Indicates that verfication failed.
          - `errored` - Indicates that a transfer sent to the bank account failed. Transfers will not be sent to the account until its details are updated.

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}.

  - name: "date"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: "The description of the payout."

  - name: "destination"
    type: "string"
    description: "The ID of the bank account of card the payout was sent to."

  - name: "failure_balance_transaction"
    type: "string"
    description: "If the payout failed or was canceled, this will be the ID of the balance transaction that reversed the initial balance transaction, and puts the funds from the failed payout back in your balance."
    foreign-key-id: "balance-transaction-id"

  - name: "failure_code"
    type: "string"
    description: |
      The error code explaining the reason for payout failure. Refer to [{{ integration.display_name }}'s documentation](https://stripe.com/docs/api#payout_failures){:target="new"} for a list of possible codes.

  - name: "failure_message"
    type: "string"
    description: "The message displaying to the user that further explains the reason for payout failure."

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: ""
    object-attributes:
      - name: ""
        value: ""
        description: ""

  - name: "method"
    type: "string"
    description: |
      The method used to send the payout. Possible values are:

      - `standard`
      - `instant`

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `payout`."

  - name: "recipient"
    type: "string"
    description: ""

  - name: "source_transaction"
    type: "string"
    description: "The ID of the charge or payment used to fund the payout."

  - name: "source_type"
    type: "string"
    description: |
      The source balance the payout came from. Possible values are:

      - `card`
      - `bank_account`
      - `alipay_account`

  - name: "statement_description"
    type: "string"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "statement_descriptor"
    type: "string"
    description: "Additional info about a payout to be displayed on the user's bank statement."

  - name: "status"
    type: "string"
    description: |
      The status of the payout. Possible values are:

      - `paid`
      - `pending`
      - `in_transit`
      - `canceled`
      - `failed`

  - name: "transfer_group"
    type: "string"
    description: "A string that identifies the payout as part of a group."

  - name: "type"
    type: "string"
    description: "The type of the payout. Possible values are `bank_account` or `card`."

  - name: "updated"
    type: "date-time"
    description: "The time the payout was last updated."
---