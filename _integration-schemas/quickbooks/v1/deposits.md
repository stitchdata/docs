---
tap: "quickbooks"
version: "1"
key: "deposit"

name: "deposits"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/deposit"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/deposits.json"
description: |
  The `{{ table.name }}` table contains info about deposits in your {{ integration.display_name }} instance. These can be customer payments or new direct deposits.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a deposit"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/deposit#query-a-deposit"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The deposit ID."
    # foreign-key-id: "deposit-id"

  - name: "CashBack"
    type: "object"
    description: ""
    subattributes:
      - name: "AccountRef"
        type: "object"
        description: "Details about the account associated with the deposit."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The account ID."
            foreign-key-id: "account-id"

      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "Memo"
        type: "string"
        description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the deposit is in."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "DepartmentRef"
    type: "object"
    description: "Details about the department associated with the deposit."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The department ID."
        foreign-key-id: "department-id"

  - name: "DepositToAccountRef"
    type: "object"
    description: "Details about the account to which the deposit was made."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
    description: ""

  - name: "Line"
    type: "array"
    description: ""
    subattributes:
      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "DepositLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "AccountRef"
            type: "object"
            description: "Details about the account associated with the line item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: "The account ID."
                foreign-key-id: "account-id"

          - name: "CheckNum"
            type: "string"
            description: ""

          - name: "PaymentMethodRef"
            type: "object"
            description: "Details about the payment method associated with the line item."
            subattributes:
              - name: "value"
                type: "string"
                description: "The payment method."
                foreign-key-id: "payment-method-id"

      - name: "DetailType"
        type: "string"
        description: ""

      - name: "Id"
        type: "string"
        description: ""

      - name: "LineNum"
        type: "integer"
        description: ""

      - name: "LinkedTxn"
        type: "array"
        description: "Details about the transactions linked with the deposit."
        subattributes:
          - name: "TxnId"
            type: "string"
            description: |
              The ID of the linked transaction.

              Depending on the `TxnType` value, this may be a foreign key to the following tables:

              - [journal_entries.Id](#journal_entries) (`TxnType: JournalEntry`)
              - [payments.Id](#payments) (`TxnType: Payments`)
              - [refund_receipts.Id](#refund_receipts) (`TxnType: RefundReceipt`)
              - [sales_receipts.Id](#sales_receipts) (`TxnType: SalesReceipt`)
              - [transfers.Id](#transfers) (`TxnType: Transfer`)
            foreign-key-id: "transaction-deposit-id"

          - name: "TxnType"
            type: "string"
            description: |
              The type of the linked transaction. Possible values are:

              - `JournalEntry`
              - `Payment`
              - `RefundReceipt`
              - `SalesReceipt`
              - `Transfer`

          - name: "TxnLineId"
            type: "string"
            description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TotalAmt"
    type: "decimal"
    description: ""

  - name: "TxnDate"
    type: "date-time"
    description: ""
---