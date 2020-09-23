---
tap: "quickbooks"
version: "1"
key: "sales-receipt"

name: "sales_receipts"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/salesreceipt"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/sales_receipts.json"
description: |
  The `{{ table.name }}` table contains info about the sales receipts recorded in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a sales receipt"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/salesreceipt/#query-a-salesreceipt"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The sales receipt ID."
    foreign-key-id: "sales-receipt-id"

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

  - name: "ClassRef"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "class-id"

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the sales receipt is in."
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
    description: "Details about the customer associated with the sales receipt."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "customer-id"

  - name: "DepartmentRef"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "department-id"

  - name: "DepositToAccountRef"
    type: "object"
    description: "Details about the account from to the sales payment was deposited."
    subattributes: &account-attributes
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

  - name: "EmailStatus"
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

      - name: "DiscountLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "DiscountAccountRef"
            type: "object"
            description: "Details about the account associated with the discount line."
            subattributes: *account-attributes

          - name: "DiscountPercent"
            type: "integer"
            description: ""

          - name: "PercentBased"
            type: "boolean"
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
    description: "Details about the payment method associated with the sales receipt."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The payment method ID."
        foreign-key-id: "payment-method-id"

  - name: "PaymentRefNum"
    type: "string"
    description: ""

  - name: "PrintStatus"
    type: "string"
    description: ""

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "ShipAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "City"
        type: "string"
        description: ""

      - name: "Country"
        type: "string"
        description: ""

      - name: "CountrySubDivisionCode"
        type: "string"
        description: ""

      - name: "Id"
        type: "string"
        description: ""

      - name: "Lat"
        type: "string"
        description: ""

      - name: "Line1"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

      - name: "PostalCode"
        type: "string"
        description: ""

  - name: "ShipDate"
    type: "date-time"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TotalAmt"
    type: "decimal"
    description: ""

  - name: "TrackingNum"
    type: "string"
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