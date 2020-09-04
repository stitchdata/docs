---
tap: "quickbooks"
version: "1"
key: "refund-receipt"

name: "refund_receipts"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/refundreceipt"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/refund_receipts.json"
description: |
  The `{{ table.name }}` table contains info about customer refunds recorded in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a refund receipt"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/refundreceipt/#query-a-refundreceipt"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The refund receipt ID."
    foreign-key-id: "refund-receipt-id"

  - name: "ApplyTaxAfterDiscount"
    type: "boolean"
    description: ""

  - name: "Balance"
    type: "integer"
    description: ""

  - name: "BillAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "Id"
        type: "string"
        description: ""

      - name: "Lat"
        type: "string"
        description: ""

      - name: "Line1"
        type: "string"
        description: ""

      - name: "Line2"
        type: "string"
        description: ""

      - name: "Line3"
        type: "string"
        description: ""

      - name: "Line4"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

  - name: "BillEmail"
    type: "object"
    description: ""
    subattributes:
      - name: "Address"
        type: "string"
        description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the refund receipt is in."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "CustomField"
    type: "array"
    description: ""
    subattributes:
      - name: "DefinitionId"
        type: "string"
        description: ""

      - name: "Name"
        type: "string"
        description: ""

      - name: "Type"
        type: "string"
        description: ""

  - name: "CustomerMemo"
    type: "object"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "CustomerRef"
    type: "object"
    description: "Details about the customer associated with the refund."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "customer-id"

  - name: "DepositToAccountRef"
    type: "object"
    description: "Details about the account from which the refund was made."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

  - name: "DocNumber"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
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

      - name: "Description"
        type: "string"
        description: ""

      - name: "DetailType"
        type: "string"
        description: ""

      - name: "Id"
        type: "string"
        description: ""

      - name: "LineNum"
        type: "integer"
        description: ""

      - name: "SalesItemLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "ItemRef"
            type: "object"
            description: "Details about the item associated with the sales line item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: "The item ID."
                foreign-key-id: "item-id"

          - name: "Qty"
            type: "decimal"
            description: ""

          - name: "TaxCodeRef"
            type: "object"
            description: "Details about the tax code associated with the sales line item."
            subattributes:
              - name: "value"
                type: "string"
                description: "The tax code ID."
                foreign-key-id: "tax-code-id"

          - name: "UnitPrice"
            type: "integer"
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
    description: "Details about the payment method associated with the refund."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The payment method ID."
        foreign-key-id: "payment-method-id"

  - name: "PrintStatus"
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

  - name: "TxnTaxDetail"
    type: "object"
    description: ""
    subattributes:
      - name: "TotalTax"
        type: "integer"
        description: ""
---