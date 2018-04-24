---
tap: "xero"
version: "1.0"

name: "bank_transactions"
doc-link: &api-doc https://developer.xero.com/documentation/api/banktransactions
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/bank_transactions.json
description: |
  The `bank_transactions` table contains info about the bank transactions in your Xero account.

replication-method: "Incremental"

api-method:
  name: getBankTransactions
  doc-link: *api-doc

attributes:
  - name: "BankTransactionId"
    type: "string"
    primary-key: true
    description: "The bank transaction ID."

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the bank transaction was last modified, in UTC."

  - name: "Type"
    type: "string"
    description: "The bank transaction type. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#BankTransactionTypes) for possible transaction types."
    doc-link: https://developer.xero.com/documentation/api/types#BankTransactionTypes

  - name: "Contact"
    type: "object"
    description: ""

  - name: "LineItems"
    type: "array"
    description: ""
    array-attributes:

  - name: "BankAccount"
    type: "array"
    description: ""
    reference: reference

  - name: "IsReconciled"
    type: "boolean"
    description: "If `true`, then the transaction has been reconciled."

  - name: "Date"
    type: "date-time"
    description: "The date of the transaction."

  - name: "DateString"
    type: "date-time"
    description: ""

  - name: "Reference"
    type: "string"
    description: "The reference for the transaction. Only applicable to `SPEND` and `RECEIVE` transactions."

  - name: "CurrencyCode"
    type: "string"
    description: "The currency that the bank transaction has been raised in."
    foreign-key: true

  - name: "CurrencyRate"
    type: "number"
    description: "The exchange rate to base currency when money is spent or received. Only used for bank transactions in non-base currency."

  - name: "Url"
    type: "string"
    description: "The URL link to a source document."

  - name: "Status"
    type: "string"
    description: |
      The status of the bank transaction. Possible values are:

      - `AUTHORISED`
      - `DELETED`

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts that the line items in the transaction contain. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive tax
      - `NoTax` - Line items have no tax
    doc-link: https://developer.xero.com/documentation/api/types#LineAmountTypes

  - name: "SubTotal"
    type: "number"
    description: "The total of the bank transaction, excluding taxes."

  - name: "TotalTax"
    type: "number"
    description: "The total tax of the bank transaction."

  - name: "Total"
    type: "number"
    description: "The total of the bank transaction, tax inclusive."

  - name: "PrepaymentID"
    type: "string"
    description: "The prepayment ID associated with the transaction. Applicable to bank transactions with `Type: SPEND-PREPAYMENT` or `Type: RECEIVE-PREPAYMENT`."
    foreign-key: true

  - name: "OverpaymentID"
    type: "string"
    description: "The overpayment ID associated with the transaction. Applicable to bank transactions with `Type: SPEND-OVERPAYMENT` or `Type: RECEIVE-OVERPAYMENT`."
    foreign-key: true

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the bank transaction has an attachment."

  # - name: "ExternalLinkProviderName"
  #   type: "string"
  #   description: ""
---