---
tap: "xero"
version: "1.0"

name: "payments"
doc-link: &api-doc https://developer.xero.com/documentation/api/payments
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/payments.json
description: |
  The `{{ table.name }}` table contains info about the payments recorded in your Xero account. 

replication-method: "Key-based Incremental"

api-method:
  name: getPayments
  doc-link: *api-doc

attributes:
  - name: "PaymentID"
    type: "string"
    primary-key: true
    description: "The payment ID."
    foreign-key-id: "payment-id"

  - name: "UpdateDateUTC"
    type: "string"
    replication-key: true
    description: "The date the payment was last updated, in UTC."

  - name: "Date"
    type: "date-time"
    description: "The date the payment is being made."

  - name: "CurrencyRate"
    type: "number"
    description: "The exchange rate when the payment was received."

  - name: "Amount"
    type: "number"
    description: "The amount of the payment."

  - name: "Reference"
    type: "string"
    description: "An optional reference for the payment. For example: `Direct Debit`"

  - name: "IsReconciled"
    type: "boolean"
    description: "If `true`, the payment has been marked as manually reconciled. Refer to [Xero's documentation](https://help.xero.com/Q_BankRecNoImport) for more info."

  - name: "Status"
    type: "string"
    description: |
      The status of the payment. Possible values are:

      - `AUTHORISED`
      - `DELETED`

  - name: "PaymentType"
    type: "string"
    description: |
      The type of the payment. Possible values are:

      - `ACCRECPAYMENT` - Accounts Receivable Payment
      - `ACCPAYPAYMENT` - Accounts Payable Payment
      - `ARCREDITPAYMENT` - Accounts Receivable Credit Payment (Refund)
      - `APCREDITPAYMENT` - Accounts Payable Credit Payment (Refund)
      - `AROVERPAYMENTPAYMENT` - Accounts Receivable Overpayment Payment (Refund)
      - `ARPREPAYMENTPAYMENT` - Accounts Receivable Prepayment Payment (Refund)
      - `APPREPAYMENTPAYMENT` - Accounts Payable Prepayment Payment (Refund)
      - `APOVERPAYMENTPAYMENT` - Accounts Payable Overpayment Payment (Refund)

  - name: "Account"
    type: ""
    description: |
      Details about the account the payment was made from.

      {{ integration.sub-table | flatify | replace:"table_name","accounts" }}

  - name: "Invoice"
    type: ""
    description: |
      Details about the invoice the payment was made against.

      {{ integration.sub-table | flatify | replace:"table_name","invoices" }}

  - name: "CreditNote"
    type: "object"
    description: "Details about the credit note the payment was made against."
    subattributes:
      - name: "CreditNoteNumber"
        type: "string"
        description: "The number of the credit note the payment was made against."

  - name: "Prepayments"
    type: "array"
    description: "Details about the prepayment the payment was made against."
    subattributes:
      - name: "PrepaymentID"
        type: "string"
        description: "The ID of the prepayment the payment was made against."
        foreign-key-id: "prepayment-id"

  - name: "Overpayment"
    type: "array"
    description: "Details about the overpayment the payment was made against."
    subattributes:
      - name: "OverpaymentID"
        type: "string"
        foreign-key: true
        description: "The ID of the overpayment the payment was made against."

  - name: "BankAmount"
    type: "number"
    description: "The bank amount of the payment."

  - name: "HasValidationErrors"
    type: "boolean"
    description: "If `true`, a validation error is associated with the payment."

  # - name: "HasAccount"
  #   type: "boolean"
  #   description: ""

  - name: "BatchPaymentID"
    type: "string"
    description: "The ID of the batch the payment was included in, if applicable."
---