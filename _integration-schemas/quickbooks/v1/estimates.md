---
tap: "quickbooks"
version: "1"
key: "estimate"

name: "estimates"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/estimate"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/estimates.json"
description: |
  The `{{ table.name }}` table contains info about the estimates in your {{ integration.display_name }} instance. An estimate is a financial proposal from a business to a [customer](#customers) for goods or services.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query an estimate"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/estimate#read-an-estimate"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The estimate ID."
    foreign-key-id: "estimate-id"

  - name: "ApplyTaxAfterDiscount"
    type: "boolean"
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
    description: "Details about the currency the estimate is in."
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
    description: "Details about the customer associated with the estimate."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The customer ID."
        foreign-key-id: "customer-id"

  - name: "DeliveryInfo"
    type: "object"
    description: ""
    subattributes:
      - name: "DeliveryType"
        type: "string"
        description: ""

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
            description: "Details about the item associated with the line item."
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
            description: "Details about the tax code associated with the line item."
            subattributes:
              - name: "value"
                type: "string"
                description: "The tax code ID."
                foreign-key-id: "tax-code-id"

          - name: "UnitPrice"
            type: "decimal"
            description: ""

  - name: "LinkedTxn"
    type: "array"
    description: "A list of the invoices associated with the estimate."
    subattributes:
      - name: "TxnId"
        type: "string"
        description: "The invoice ID."
        foreign-key-id: "invoice-id"

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

  - name: "PrintStatus"
    type: "string"
    description: ""

  - name: "ShipAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "City"
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

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TotalAmt"
    type: "decimal"
    description: ""

  - name: "TxnDate"
    type: "date-time"
    description: ""

  - name: "TxnStatus"
    type: "string"
    description: ""

  - name: "TxnTaxDetail"
    type: "object"
    description: ""
    subattributes:
      - name: "TaxLine"
        type: "array"
        description: ""
        subattributes:
          - name: "Amount"
            type: "decimal"
            description: ""

          - name: "DetailType"
            type: "string"
            description: ""

          - name: "TaxLineDetail"
            type: "object"
            description: ""
            subattributes:
              - name: "NetAmountTaxable"
                type: "decimal"
                description: ""

              - name: "PercentBased"
                type: "boolean"
                description: ""

              - name: "TaxPercent"
                type: "integer"
                description: ""

              - name: "TaxRateRef"
                type: "object"
                description: "Details about the tax rate associated with the estimate."
                subattributes:
                  - name: "value"
                    type: "string"
                    description: "The tax rate ID."
                    foreign-key-id: "tax-rate-id"

      - name: "TotalTax"
        type: "decimal"
        description: ""

      - name: "TxnTaxCodeRef"
        type: "object"
        description: "Details about the tax code associated with the estimate."
        subattributes:
          - name: "value"
            type: "string"
            description: "The tax code ID."
            foreign-key-id: "tax-code-id"
---