---
tap: "quickbooks"
version: "2"
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
        subattributes: &name-value
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: ""

      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "Memo"
        type: "string"
        description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the deposit is in."
    subattributes: *name-value

  - name: "DepartmentRef"
    type: "object"
    description: "Details about the department associated with the deposit."
    subattributes: *name-value

  - name: "DepositToAccountRef"
    type: "object"
    description: "Details about the account to which the deposit was made."
    subattributes: *name-value

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
    description: ""

  - name: "GlobalTaxCalculation"
    type: "string"
    description: ""

  - name: "HomeTotalAmt"
    type: "decimal"
    description: ""

  - name: "Line"
    type: "array"
    description: ""
    subattributes:
      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "CustomField"
        type: "object"
        description: ""
        subattributes:
          - name: "DefinitionId"
            type: "string"
            description: ""
            
          - name: "Name"
            type: "string"
            description: ""
            
          - name: "StringValue"
            type: "string"
            description: ""
            
          - name: "Type"
            type: "string"
            description: ""

      - name: "DepositLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "AccountRef"
            type: "object"
            description: "Details about the account associated with the line item."
            subattributes: *name-value

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

  - name: "RecurDateRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TotalAmt"
    type: "decimal"
    description: ""

  - name: "TransactionLocationType"
    type: "string"
    description: ""

  - name: "TxnDate"
    type: "date-time"
    description: ""

  - name: "TxnSource"
    type: "object"
    description: ""

  - name: "TxnTaxDetail"
    type: "object"
    description: ""
    subattributes:
      - name: "TotalTax"
        type: "decimal"
        description: ""

      - name: "TaxLine"
        type: "object"
        description: ""
        subattributes:
          - name: "Amount"
            type: "string"
            description: ""
            
          - name: "DetailType"
            type: "string"
            description: ""

          - name: "TaxLineDetail"
            type: "object"
            description: ""
            subattributes:
              - name: "OverrideDeltaAmount"
                type: "decimal"
                description: ""
                
              - name: "PercentBased"
                type: "boolean"
                description: ""
                
              - name: "TaxInclusiveAmount"
                type: "decimal"
                description: ""
                
              - name: "TaxPercent"
                type: "decimal"
                description: ""
                
              - name: "TaxRateRef"
                type: "object"
                description: ""
                subattributes: *name-value

      - name: "TxnTaxCodeRef"
        type: "object"
        description: ""
        subattributes: *name-value
---