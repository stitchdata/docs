---
tap: "quickbooks"
version: "2"
key: "invoice"

name: "invoices"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about the invoices in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query an invoice"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice#query-an-invoice"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "AllowIPNPayment"
    type: "boolean"
    description: ""

  - name: "AllowOnlineACHPayment"
    type: "boolean"
    description: ""

  - name: "AllowOnlineCreditCardPayment"
    type: "boolean"
    description: ""

  - name: "AllowOnlinePayment"
    type: "boolean"
    description: ""

  - name: "ApplyTaxAfterDiscount"
    type: "boolean"
    description: ""

  - name: "Balance"
    type: "decimal"
    description: ""

  - name: "BillAddr"
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

      - name: "Line2"
        type: "string"
        description: ""

      - name: "Line3"
        type: "string"
        description: ""

      - name: "Line4"
        type: "string"
        description: ""

      - name: "Line5"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

      - name: "Country"
        type: "string"
        description: ""

      - name: "PostalCode"
        type: "string"
        description: ""

  - name: "BillEmail"
    type: "object"
    description: ""
    subattributes:
      - name: "Address"
        type: "string"
        description: ""

  - name: "BillEmailBcc"
    type: "object"
    description: ""
    subattributes:
      - name: "Address"
        type: "string"
        description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the invoice is in."
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

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

      - name: "StringValue"
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
    description: "Details about the customer associated with the invoice."
    subattributes: *name-value

  - name: "ClassRef"
    type: "object"
    description: "Details about the class associated with the invoice."
    subattributes: *name-value

  - name: "DeliveryInfo"
    type: "object"
    description: ""
    subattributes:
      - name: "DeliveryType"
        type: "string"
        description: ""
        
      - name: "DeliveryTime"
        type: "date-time"
        description: ""

  - name: "DepartmentRef"
    type: "object"
    description: "Details about the department the invoice is in."
    subattributes: *name-value

  - name: "Deposit"
    type: "decimal"
    description: ""

  - name: "DepositToAccountRef"
    type: "object"
    description: "Details about the deposit account associated with the invoice."
    subattributes: *name-value

  - name: "domain"
    type: "string"
    description: ""

  - name: "DocNumber"
    type: "string"
    description: ""

  - name: "DueDate"
    type: "date-time"
    description: ""

  - name: "EmailStatus"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
    description: ""

  - name: "FreeFormAddress"
    type: "boolean"
    description: ""

  - name: "GlobalTaxCalculation"
    type: "string"
    description: ""

  - name: "HomeBalance"
    type: "decimal"
    description: ""

  - name: "HomeTotalAmt"
    type: "decimal"
    description: ""

  - name: "InvoiceLink"
    type: "string"
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

      - name: "DescriptionLineDetail"
        type: "object"
        description: ""
        subattributes: ""
          - name: "ServiceData"
            type: "date-time"
            description: ""
            
          - name: "TaxCodeRef"
            type: "object"
            description: ""
            subattributes: *name-value

      - name: "GroupLineDetail"
        type: "object"
        description: ""
        subattributes: ""
          - name: "GroupItemRef"
            type: "object"
            description: ""
            subattributes: *name-value
            
          - name: "Line"
            type: "object"
            description: ""
            subattributes:
             - name: "Amount"
               type: "decimal"
               description: ""
               
             - name: "Description"
               type: "string"
               description: ""

             - name: "Detailtype"
               type: "string"
               description: ""

             - name: "Id"
               type: "string"
               description: ""

             - name: "LineNum"
               type: "decimal"
               description: ""

             - name: "SalesItemLineDetail"
               type: "object"
               description: ""
               subattributes:
                 - name: "ClassRef"
                   type: "object"
                   description: ""
                   subattributes: *name-value
                   
                 - name: "DiscountAmt"
                   type: "decimal"
                   description: ""
                   
                 - name: "DiscountRate"
                   type: "decimal"
                   description: ""
                   
                 - name: "ItemAccountRef"
                   type: "object"
                   description: ""
                   subattributes: *name-value
                   
                 - name: "ItemRef"
                   type: "object"
                   description: ""
                   subattributes: *name-value
                   
                 - name: "MarkupInfo"
                   type: "object"
                   description: ""
                   subattributes:
                     - name: "MarkupIncomeAccountRef"
                       type: "object"
                       description: ""
                       
                     - name: "Percent"
                       type: "decimal"
                       description: ""
                       subattributes: *name-value
                       
                     - name: "PriceLevelRef"
                       type: "object"
                       description: ""
                       subattributes: *name-value
                   
                 - name: "Qty"
                   type: "integer"
                   description: ""
                   
                 - name: "ServiceDate"
                   type: "date-time"
                   description: ""
                   
                 - name: "TaxClassificationRef"
                   type: "object"
                   description: ""
                   subattributes: *name-value
                   
                 - name: "TaxCodeRef"
                   type: "object"
                   description: ""
                   subattributes: *name-value
                   
                 - name: "TaxInclusiveAmt"
                   type: "decimal"
                   description: ""
                   
                 - name: "UnitPrice"
                   type: "decimal"
                   description: ""
            
          - name: "Quantity"
            type: "decimal"
            description: ""

      - name: "SubtotalLineDetail"
        type: "object"
        description: ""
        subattributes: ""
          - name: "ItemRef"
            type: "object"
            description: ""
            subattributes: *name-value

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
            subattributes: *name-value

          - name: "Qty"
            type: "integer"
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
            type: "integer"
            description: ""

  - name: "LinkedTxn"
    type: "array"
    description: "Details about the transactions associated with the invoice."
    subattributes:
      - name: "TxnLineId"
        type: "string"
        description: ""

      - name: "TxnId"
        type: "string"
        description: |
          The ID of the linked transaction.

          Depending on the `TxnType` value, this may be a foreign key to the following tables:

          - [estimates.Id](#estimates) (`TxnType: Estimate`)
          - [payments.Id](#payments) (`TxnType: Payment`)
          - [purchases.Id](#purchases) (`TxnType: Purchase`)
          - [time_activities.Id](#time_activities) (`TxnType: TimeActivity`)
        foreign-key-id: "transaction-invoice-id"

      - name: "TxnType"
        type: "string"
        description: |
          The type of the linked transaction. Possible values are:

          - `Estimate`
          - `Payment`
          - `Purchase`
          - `TimeActivity`

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

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "RecurDateRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "SalesTermRef"
    type: "object"
    description: "Details about the sales term associated with the invoice."
    ubattributes: *name-value

  

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

      - name: "Line2"
        type: "string"
        description: ""

      - name: "Line3"
        type: "string"
        description: ""

      - name: "Line4"
        type: "string"
        description: ""

      - name: "Line5"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

      - name: "PostalCode"
        type: "string"
        description: ""

      - name: "Country"
        type: "string"
        description: ""

  - name: "ShipDate"
    type: "date-time"
    description: ""

  - name: "ShipFromAddr"
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

      - name: "Line5"
        type: "string"
        description: ""

      - name: "Long"
        type: "string"
        description: ""

      - name: "City"
        type: "string"
        description: ""

      - name: "Country"
        type: "string"
        description: ""

      - name: "CountrySubDivisionCode"
        type: "string"
        description: ""

      - name: "PostalCode"
        type: "string"
        description: ""

  - name: "ShipMethodRef"
    type: "object"
    description: "Details about the shipping method associated with the invoice."
    subattributes: *name-value

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

  - name: "TrackingNum"
    type: "string"
    description: ""

  - name: "TxnDate"
    type: "date-time"
    description: ""

  - name: "TxnSource"
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

              - name: "OverrideDeltaAmount"
                type: "number"
                description: ""

              - name: "PercentBased"
                type: "boolean"
                description: ""

              - name: "TaxInclusiveAmount"
                type: "number"
                description: ""

              - name: "TaxPercent"
                type: "decimal"
                description: ""

              - name: "TaxRateRef"
                type: "object"
                description: "Details about the tax rate associated with the tax line."
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
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: "The tax code ID."
            foreign-key-id: "tax-code-id"
---