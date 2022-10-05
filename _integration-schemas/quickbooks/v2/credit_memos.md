---
tap: "quickbooks"
version: "2"
key: "credit-memo"

name: "credit_memos"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/creditmemo"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/credit_memos.json"
description: |
  The `{{ table.name }}` table contains info about the credit memos in your {{ integration.display_name }} instance. A credit memo is a transaction representing a refund or credit of payment for goods or services that have been sold.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a credit memo"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/creditmemo#query-a-credit-memo"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The credit memo ID."
    foreign-key-id: "credit-memo-id"

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

  - name: "BillEmail"
    type: "object"
    description: ""
    subattributes:
      - name: "Address"
        type: "string"
        description: ""

  - name: "ClassRef"
    type: "object"
    description: "Details about the class associated with the credit memo."
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency used in the credit memo."
    subattributes: *name-value

  - name: "CustomField"
    type: "array"
    description: "Custom fields associated with the credit memo."
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
    description: "Details about the customer associated with the credit memo."
    subattributes: *name-value

  - name: "DepartmentRef"
    type: "object"
    description: ""
    subattributes: *name-value

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

  - name: "GlobalTaxCalculation"
    type: "string"
    description: ""

  - name: "HomeBalance"
    type: "decimal"
    description: ""

  - name: "HomeTotalAmt"
    type: "decimal"
    description: ""

  - name: "InvoiceRef"
    type: "object"
    description: ""
    subattributes: *name-value

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
          - name: "ServiceDate"
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
            type: "decimal"
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
    type: "string"
    description: ""

  - name: "PrintStatus"
    type: "string"
    description: ""

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "RecurDataRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "RemainingCredit"
    type: "integer"
    description: ""

  - name: "SalesTermRef"
    type: "object"
    description: "Details about the term associated with the credit memo."
    subattributes: *name-value

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

  - name: "TxnTaxDetail"
    type: "object"
    description: ""
    subattributes:
      - name: "TotalTax"
        type: "integer"
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

  - name: "domain"
    type: "string"
    description: ""
---