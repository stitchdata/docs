---
tap: "chargebee"
version: "1.0"
key: "transaction"

name: "transactions"
doc-link: "https://apidocs.chargebee.com/docs/api/transactions"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/transactions.json"
description: |
  The `{{ table.name }}` table contains info about the transactions that have occurred in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List transactions"
    doc-link: "https://apidocs.chargebee.com/docs/api/transactions#list_transactions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The transaction ID."
    foreign-key-id: "transaction-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the transaction was last updated."

  - name: "amount"
    type: "integer"
    description: "The amount for the transaction."

  - name: "amount_unused"
    type: "integer"
    description: "**Applicable only for payments.** The unused amount present for the transaction."

  - name: "base_currency_code"
    type: "string"
    description: ""

  - name: "currency_code"
    type: "string"
    description: "The currency code for the transaction, in ISO 4217 format."

  - name: "customer_id"
    type: "string"
    description: "The ID of the customer associated with the transaction."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date the transaction occurred."

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the transaction has been deleted."

  - name: "error_code"
    type: "string"
    description: "The error code received from the payment gateway on failure."

  - name: "error_text"
    type: "string"
    description: "The error message received from the payment gateway on failure."

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "fraud_flag"
    type: "string"
    description: |
      Indicates whether or not the transaction has been identified as fraudulent. Possible values are:

      - `safe`
      - `suspicious`
      - `fraudulent`

  - name: "fraud_reason"
    type: "string"
    description: "A short description why the transaction was marked as fraudulent or suspicious."

  - name: "gateway"
    type: "string"
    description: "The name of the gateway used to process the transaction."

  - name: "gateway_account_id"
    type: "string"
    description: "The account ID of the gateway used to process the transaction."

  - name: "id_at_gateway"
    type: "string"
    description: "The ID with which the transaction is referred in the `gateway`."

  - name: "linked_credit_notes"
    type: "array"
    description: "**Applicable only for refund transactions.** The list of credit notes the transaction is associated with."
    subattributes:
      - name: "applied_amount"
        type: "integer"
        description: "The transaction amount applied to the invoice."

      - name: "applied_at"
        type: "date-time"
        description: "The time the credit note was applied."

      - name: "cn_date"
        type: "date-time"
        description: "The date the credit note was created."

      - name: "cn_id"
        type: "string"
        description: "The credit note ID."
        foreign-key-id: "credit-note-id"

      - name: "cn_reason_code"
        type: "string"
        description: |
          The reason for the credit note. Possible values are:

          - `write_off`
          - `subscription_change`
          - `subscription_cancellation`
          - `subscription_pause`
          - `chargeback`
          - `product_unsatisfactory`
          - `service_unsatisfactory`
          - `order_change`
          - `order_cancellation`
          - `waiver`
          - `other`
          - `fraudulent`

      - name: "cn_reference_invoice_id"
        type: "string"
        description: "The invoice ID."
        foreign-key-id: "invoice-id"

      - name: "cn_status"
        type: "string"
        description: |
          The status of the credit note. Possible values are:

          - `adjusted`
          - `refunded`
          - `refund_due`
          - `voided`

      - name: "cn_total"
        type: "integer"
        description: "The total amount of the credit note."

  - name: "linked_invoices"
    type: "array"
    description: "**Applicable only for payment transactions.** The list of invoices the transaction has been applied to."
    subattributes:
      - name: "applied_amount"
        type: "integer"
        description: "The transaction amount applied to the invoice."

      - name: "applied_at"
        type: "date-time"
        description: "The time at which the transaction was applied."

      - name: "invoice_date"
        type: "date-times"
        description: "The date the invoice was issued."

      - name: "invoice_id"
        type: "string"
        description: "The invoice ID."
        foreign-key-id: "invoice-id"

      - name: "invoice_status"
        type: "string"
        description: |
          The current status of the invoice. Possible values are:

          - `paid`
          - `posted`
          - `payment_due`
          - `not_paid`
          - `voided`
          - `pending`

      - name: "invoice_total"
        type: "integer"
        description: "The total amount of the invoice."

  - name: "linked_refunds"
    type: "array"
    description: "**Applicable only for payment transactions.** The list of refunds issued for the payment transaction."
    subattributes:
      - name: "txn_amount"
        type: "integer"
        description: "The total amount of the transaction."

      - name: "txn_date"
        type: "date-time"
        description: "The date the transaction occured."

      - name: "txn_id"
        type: "string"
        description: "the transaction ID."
        foreign-key-id: "transaction-id"

      - name: "txn_status"
        type: "string"
        description: |
          The status of the transaction. Possible values are:

          - `in_progress`
          - `success`
          - `voided`
          - `failure`
          - `timeout`
          - `needs_attention`

  - name: "masked_card_number"
    type: "string"
    description: "**Applicable only when `payment_method: card`.** The masked card number used for the transaction."

  - name: "object"
    type: "string"
    description: ""

  - name: "payment_method"
    type: "string"
    description: |
      The payment method for the transaction. Possible values are:

      - `card`
      - `cash`
      - `check`
      - `chargeback`
      - `bank_transfer`
      - `amazon_payments`
      - `paypal_express_checkout`
      - `direct_debit`
      - `alipay`
      - `unionpay`
      - `apple_pay`
      - `wechat_pay`
      - `ach_credit`
      - `other`

  - name: "payment_source_id"
    type: "string"
    description: "The ID of the payment source used for the transaction."
    foreign-key-id: "payment-source-id"

  - name: "reference_number"
    type: "string"
    description: "The reference number for the transaction."

  - name: "reference_transaction_id"
    type: "string"
    description: "**Applicable only when `type` is `refund` or `payment_reversal`.** The reference payment ID."
    foreign-key-id: "transaction-id"

  - name: "refunded_txn_id"
    type: "string"
    description: "**Applicable only when `type: refund`**. The ID of the original transaction that was refunded."
    foreign-key-id: "transaction-id"

  - name: "resource_version"
    type: "integer"
    description: "The version number of the transaction. Each update of the transaction results in an incremental change of this value. **Note**: This attribute will be present only if the credit note has been updated after 2016-09-28."

  - name: "reversal_txn_id"
    type: "string"
    description: "**Applicable only when `type: payment_reversal`**. The ID of the original transaction that was reversed."

  - name: "settled_at"
    type: "date-time"
    description: "The time at which the final status of the transaction has been marked."

  - name: "status"
    type: "string"
    description: |
      The status of the transaction. Possible values are:

      - `in_progress`
      - `success`
      - `voided`
      - `failure`
      - `timeout`
      - `needs_attention`

  - name: "subscription_id"
    type: "string"
    description: "The ID of the subscription associated with the transaction."
    foreign-key-id: "subscription-id"

  - name: "type"
    type: "string"
    description: |
      The type of the transaction. Possible values are:

      - `authorization`
      - `payment`
      - `refund`
      - `payment_reversal`

  - name: "validated_at"
    type: "date-time"
    description: ""
---