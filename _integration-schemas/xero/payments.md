---
tap: "xero"
version: "1.0"

name: "payments"
doc-link: &api-doc https://developer.xero.com/documentation/api/payments
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/payments.json
description: |
  The `payments` table contains info about the payments recorded in your Xero account. 

replication-method: "Incremental"

api-method:
  name: getPayments
  doc-link: *api-doc

attributes:
  - name: "PaymentID"
    type: "string"
    primary-key: true
    description: "The payment ID."

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
    description: ""

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
    type: 
    description: ""

  - name: "Invoice"
    type: 
    description: ""

  - name: "CreditNote"
    type: "object"
    description: ""
    object-attributes:

  - name: "Prepayments"
    type: "array"
    description: ""
    array-attributes:
      - name: "PrepaymentID"
        type: "string"
        foreign-key: true
        description: ""

  - name: "Overpayment"
    type: "array"
    description: ""
    array-attributes:
      - name: "OverpaymentID"
        type: "string"
        foreign-key: true
        description: ""

  - name: "BankAmount"
    type: "number"
    description: ""

  - name: "HasValidationErrors"
    type: "boolean"
    description: ""

  - name: "HasAccount"
    type: "boolean"
    description: ""

  - name: "BatchPaymentID"
    type: "string"
    description: "The ID of the batch the payment was included in, if applicable."
---