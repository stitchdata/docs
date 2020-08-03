---
tap: "xero"
version: "1"

name: "bank_transactions"
doc-link: &api-doc https://developer.xero.com/documentation/api/banktransactions
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/bank_transactions.json
description: |
  The `{{ table.name }}` table contains info about the bank transactions in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: getBankTransactions
  doc-link: *api-doc

attributes:
  - name: "BankTransactionId"
    type: "string"
    primary-key: true
    description: "The bank transaction ID."
    foreign-key-id: "bank-transaction-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the bank transaction was last modified, in UTC."

  - name: "Type"
    type: "string"
    description: |
      The bank transaction type. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#BankTransactionTypes){:target="new"} for possible transaction types.
    doc-link: https://developer.xero.com/documentation/api/types#BankTransactionTypes

  - name: "Contact"
    type: "object"
    description: ""

  - name: "LineItems"
    type: "array"
    description: "Details about the line items in the bank transaction."
    subattributes:
      - name: "LineItemID"
        type: "string"
        description: "The ID of the line item."

      - name: "Description"
        type: "string"
        description: "The description of the line item."

      - name: "Quantity"
        type: "number"
        description: "The quantity of the line item."

      - name: "UnitAmount"
        type: "number"
        description: "The amount of the line item."

      - name: "AccountCode"
        type: "string"
        description: "The account code associated with the line item."

      - name: "ItemCode"
        type: "string"
        description: "The code associated with the item."

      - name: "TaxType"
        type: "string"
        description: "The tax type associated with the line item."

      - name: "LineAmount"
        type: "number"
        description: "The total of the line item, calculated as `UnitAmount x Quantity`."

      - name: "TaxAmount"
        type: "number"
        description: "The total tax of the line item."

      - name: "DiscountRate"
        type: "number"
        description: "The discount rate of the line item, if applicable."

      - name: "Tracking"
        type: "array"
        description: |
          Details about the tracking categories applied to the line item, if applicable.
        subattributes:
          - description: |
              This will contain the same attributes as the `tracking_categories` table. Refer to the [`tracking_categories`](#tracking_categories) table schema for details.

  - name: "BankAccount"
    type: "array"
    description: |
      Details about the bank account used in the bank transaction.
    subattributes:
      - description: |
          This will contain the same attributes as the `accounts` table. Refer to the [`accounts`](#accounts) table schema for details.

  - name: "IsReconciled"
    type: "boolean"
    description: "If `true`, then the transaction has been reconciled."

  - name: "Date"
    type: "date-time"
    description: "The date of the transaction."

  - name: "DateString"
    type: "date-time"
    description: "The date of the transaction."

  - name: "Reference"
    type: "string"
    description: "The reference for the transaction. Only applicable to `SPEND` and `RECEIVE` transactions."

  - name: "CurrencyCode"
    type: "string"
    description: "The currency that the bank transaction has been raised in."
    foreign-key-id: "currency-code"

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
    foreign-key-id: "prepayment-id"

  - name: "OverpaymentID"
    type: "string"
    description: "The overpayment ID associated with the transaction. Applicable to bank transactions with `Type: SPEND-OVERPAYMENT` or `Type: RECEIVE-OVERPAYMENT`."
    foreign-key-id: "overpayment-id"

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the bank transaction has an attachment."

  # - name: "ExternalLinkProviderName"
  #   type: "string"
  #   description: ""
---