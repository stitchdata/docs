---
tap: "quickbooks"
version: "2"
key: "payment"

name: "payments"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/payments.json"
description: |
  The `{{ table.name }}` table contains info about the payments recorded in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a payment"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment/#query-a-payment"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The payment ID."
    foreign-key-id: "payment-id"

  - name: "ARAccountRef"
    type: "object"
    description: ""
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "CreditCardPayment"
    type: "object"
    description: ""
    subattributes: 
      - name: "CreditChargeInfo"
        type: "object"
        description: ""
        subattributes:
          - name: "Amount"
            type: "string"
            description: ""

          - name: "BillAddrStreet"
            type: "string"
            description: ""

          - name: "CcExpiryMonth"
            type: "string"
            description: ""

          - name: "CcExpiryYear"
            type: "string"
            description: ""

          - name: "NameOnAcct"
            type: "string"
            description: ""

          - name: "PostalCode"
            type: "string"
            description: ""

          - name: "ProcessPayment"
            type: "boolean"
            description: ""

          - name: "Type"
            type: "string"
            description: ""

      - name: "CreditChargeResponse"
        type: "object"
        description: ""
          - name: "AuthCode"
            type: "string"
            description: ""

          - name: "CCTransId"
            type: "string"
            description: ""

          - name: "Status"
            type: "string"
            description: ""

          - name: "TxnAuthorization"
            type: "date-time"
            description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the payment is in."
    subattributes: *name-value

  - name: "CustomerRef"
    type: "object"
    description: "Details about the customer associated with the payment."
    subattributes: *name-value

  - name: "DepositToAccountRef"
    type: "object"
    description: "Details about the account the payment was deposited into."
    subattributes:
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
    description: "Details about the transactions that make up the payment."
    subattributes:
      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "LineEx"
        type: "object"
        description: ""
        subattributes:
          - name: "any"
            type: "array"
            description: ""
            subattributes:
              - name: "declaredType"
                type: "string"
                description: ""

              - name: "globalScope"
                type: "boolean"
                description: ""

              - name: "name"
                type: "string"
                description: ""

              - name: "nil"
                type: "boolean"
                description: ""

              - name: "scope"
                type: "string"
                description: ""

              - name: "typeSubstituted"
                type: "boolean"
                description: ""

              - name: "value"
                type: "object"
                description: ""
                subattributes:
                  - name: "Name"
                    type: "string"
                    description: ""

                  - name: "Value"
                    type: "string"
                    description: ""

      - name: "LinkedTxn"
        type: "array"
        description: "Details about the transaction."
        subattributes:
          - name: "TxnId"
            type: "string"
            description: |
              The ID of the linked transaction.

              Depending on the `TxnType` value, this may be a foreign key to the following tables:

              - [credit_memos.Id](#) (`TxnType: CreditMemo`)
              - [invoices.Id](#invoices) (`TxnType: Invoice`)
              - [purchases.Id](#purchases) (`TxnType: Expense`, 'Check', or 'CreditCardCredit')
            foreign-key-id: "transaction-payment-id"

          - name: "TxnType"
            type: "string"
            description: |
              The type of the linked transaction. Possible values are:

              - `CreditMemo`
              - `Expense`
              - `Invoice`
              - `Check`
              - `CreditCardCredit`

  - name: "LinkedTxn"
    type: "array"
    description: ""
    subattributes:
      - name: "TxnId"
        type: "string"
        description: ""

      - name: "TxnType"
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

  - name: "PaymentMethodRef"
    type: "object"
    description: "Details about the payment method associated with the payment."
    subattributes:
      - name: "value"
        type: "string"
        description: "The payment method ID."
        foreign-key-id: "payment-method-id"

  - name: "PaymentRefNum"
    type: "string"
    description: ""

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "ProcessPayment"
    type: "boolean"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TaxExemptionRef"
    type: "object"
    description: ""
    subattributes: *name-value

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
    type: "string"
    description: ""

  - name: "UnappliedAmt"
    type: "integer"
    description: ""
---