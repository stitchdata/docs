---
tap: "quickbooks"
version: "1"
key: "bill-payment"

name: "bill_payments"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/billpayment"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/bill_payments.json"
description: |
  The `{{ table.name }}` table contains info about payments made on bills received from vendors for goods or services.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a billpayment"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/billpayment#query-a-billpayment"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The bill payment ID."
    foreign-key-id: "bill-payment-id"

  - name: "CheckPayment"
    type: "object"
    description: ""
    subattributes:
      - name: "BankAccountRef"
        type: "object"
        description: "Details about the account associated with the check payment."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The account ID."
            foreign-key-id: "account-id"

      - name: "PrintStatus"
        type: "string"
        description: ""

  - name: "CreditCardPayment"
    type: "object"
    description: ""
    subattributes:
      - name: "CCAccountRef"
        type: "object"
        description: "Details about the account associated with the credit card payment."
        subattributes:
          - name: "name"
            type: "string"
            description: ""

          - name: "value"
            type: "string"
            description: "The account ID."
            foreign-key-id: "account-id"

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency used in the bill payment."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "DocNumber"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
    description: ""

  - name: "Line"
    type: "array"
    description: "Details about the individual line items associated with the bill payment."
    subattributes:
      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "LinkedTxn"
        type: "array"
        description: |
          A list of transactions associated with the bill payment.
        subattributes:
          - name: "TxnId"
            type: "string"
            description: |
              The ID of the linked transaction.

              Depending on the `TxnType` value, this may be a foreign key to the following tables:

              - [bills.Id](#bills) (`TxnType: Bill`)
              - [journal_entries.Id](#journal_entries) (`TxnType: JournalEntry`)
              - [vendor_credits.Id](#vendor_credits) (`TxnType: VendorCredit`)
            foreign-key-id: "transaction-bill-payment-id"

          - name: "TxnType"
            type: "string"
            description: |
              The type of the linked transaction. Possible values are:

              - `Bill`
              - `JournalEntry`
              - `VendorCredit`

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

  - name: "PayType"
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

  - name: "VendorRef"
    type: "object"
    description: "Details about the vendor associated with the bill payment."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The ID of the vendor."
        foreign-key-id: "vendor-id"
---