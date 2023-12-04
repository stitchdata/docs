---
tap: "invoiced"
version: "1"

name: "transactions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/transactions.json"
description: |
  The `{{ table.name }}` table contains info about the transactions in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all transactions"
    doc-link: "https://invoiced.com/docs/api/#list-all-transactions"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The transaction ID."
    foreign-key-id: "transaction-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the transaction was last updated."

  - name: "amount"
    type: "number"
    description: "The amount of the transaction."

  - name: "created_at"
    type: "date-time"
    description: "The time the transaction was created."

  - name: "credit_note"
    type: "integer"
    description: "The ID of the credit note associated with the transaction, if any."
    foreign-key-id: "credit-note-id"

  - name: "currency"
    type: "string"
    description: |
      The [three letter ISO code](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} used by the transaction.

  - name: "customer"
    type: "integer"
    description: "The ID of the customer associated with the estimate."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date of the transaction."

  - name: "failure_reason"
    type: "string"
    description: |
      The failure message from the payment gateway when `status: failed`.

  - name: "gateway"
    type: "string"
    description: "The payment gateway that processed the transaction, if any."

  - name: "gateway_id"
    type: "string"
    description: "The transaction ID from the payment gateway."

  - name: "invoice"
    type: "integer"
    description: "The ID of the invoice associated with the transaction, if any."
    foreign-key-id: invoice-id"

  - name: "metadata"
    type: "object"
    description: "Additional details about the transaction."

  - name: "method"
    type: "string"
    description: |
      The payment instrument used to facilitate the transaction. Possible values are:

      - `credit_card`
      - `ach`
      - `direct_debit`
      - `paypal`
      - `wire_transfer`
      - `check`
      - `cash`
      - `other`

  - name: "notes"
    type: "string"
    description: "Additional notes about the transaction."

  - name: "parent_transaction"
    type: "integer"
    description: "For refunds, the ID of the original transaction."
    foreign-key-id: "transaction-id"

  - name: "payment_source"
    type: "object"
    description: "The transactions's payment source, if attached."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The payment source's ID."

      - name: "object"
        type: "string"
        description: |
          The object type of the payment source. Possible values are:

          - `card`
          - `bank_account`

      - name: "brand"
        type: "string"
        description: "**Applicable to `object: card` only.** The card brand."

      - name: "last4"
        type: "string"
        description: "The last four digits of the card or bank account."

      - name: "exp_month"
        type: "integer"
        description: "**Applicable to `object: card` only.** The expiry month."

      - name: "exp_year"
        type: "integer"
        description: "**Applicable to `object: card` only.** The expiry year."

      - name: "funding"
        type: "string"
        description: |
          **Applicable to `object: card` only.** The funding instrument of the card. Possible values are:

          - `credit`
          - `debit`
          - `prepaid`
          - `unknown`

      - name: "bank_name"
        type: "string"
        description: "**Applicable to `object: bank_account` only.** The name of the bank."

      - name: "routing_number"
        type: "string"
        description: "**Applicable to `object: bank_account` only.** The routing number."

      - name: "verified"
        type: "boolean"
        description: "**Applicable to `object: bank_account` only.** Indicates whether the bank account has been verified with instant verification or microdeposits."

      - name: "currency"
        type: "string"
        description: |
          **Applicable to `object: bank_account` only.** The [three letter ISO code](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} used by the bank account.

  - name: "status"
    type: "string"
    description: |
      The status of the transaction. Possible values are:

      - `succeeded`
      - `pending`
      - `failed`

  - name: "type"
    type: "string"
    description: |
      The type of the transaction. Possible values are:

      - `charge`
      - `payment`
      - `refund`
      - `adjustment`
---