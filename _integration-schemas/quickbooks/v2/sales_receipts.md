---
tap: "quickbooks"
version: "2"
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
    subattributes: &address
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

  - name: "CreditCardPayment"
    type: "object"
    description: ""
    subattributes:
      - name: "CreditChargeResponse"
        type: "object"
        description: ""
        subattributes:
          - name: "Status"
            type: "string"
            description: ""

          - name: "AuthCode"
            type: "string"
            description: ""

          - name: "TxnAuthorizationTime"
            type: "date-time"
            description: ""

          - name: "CCTransId"
            type: "string"
            description: ""

      - name: "CreditChargeInfo"
        type: "object"
        description: ""
        subattributes:
          - name: "CcExpiryMonth"
            type: "integer"
            description: ""

          - name: "ProcessPayment"
            type: "boolean"
            description: ""

          - name: "PostalCode"
            type: "string"
            description: ""

          - name: "Amount"
            type: "number"
            description: ""

          - name: "NameOnAcct"
            type: "string"
            description: ""

          - name: "CcExpiryYear"
            type: "integer"
            description: ""

          - name: "Type"
            type: "string"
            description: ""

          - name: "BillAddrStreet"
            type: "string"
            description: ""

  - name: "CustomField"
    type: "array"
    description: ""
    subattributes:
      - name: "StringValue"
        type: "string"
        description: ""

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

  - name: "DeliveryInfo"
    type: "object"
    description: ""
    subattributes:
      - name: "DeliveryTime"
        type: "date-time"
        description: ""

      - name: "DeliveryType"
        type: "string"
        description: ""

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

  - name: "Line"
    type: "array"
    description: ""
    subattributes:
      - &line-amount
        name: "Amount"
        type: "decimal"
        description: ""

      - &line-desc
        name: "Description"
        type: "string"
        description: ""

      - name: "DescriptionLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "ServiceDate"
            type: "date-time"
            description: ""
            
          - name: "TaxCodeRef"
            type: "object"
            description: ""
            subattributes: &name-value
              - name: "name"
                type: "string"
                description: ""
                
              - name: "value"
                type: "string"
                description: ""

      - &line-detailtype
        name: "DetailType"
        type: "string"
        description: ""

      - name: "DiscountLineDetail"
        type: "object"
        description: ""
        subattributes: *name-value
            

      - name: "GroupLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "GroupItemRef"
            type: "object"
            description: ""
            subattributes: *name-value

          - name: "Line"
            type: "object"
            description: ""
            subattributes:
              - *line-amount

              - *line-desc

              - *line-detailtype

              - &line-id
                name: "Id"
                type: "string"
                description: ""

              
              - &line-linenum
                name: "LineNum"
                type: "integer"
                description: ""

              - name: "SalesItemLineDetail"
                type: "object"
                description: ""
                subattributes:
                  - &salesitemlinedetail-classref
                    name: "ClassRef"
                    type: "object"
                    description: ""
                    subattributes: *name-value

                  - &salesitemlinedetail-discountamt
                    name: "DiscountAmt"
                    type: "decimal"
                    description: ""

                  - &salesitemlinedetail-discountrate
                    name: "DiscountRate"
                    type: "decimal"
                    description: ""

                  - &salesitemlinedetail-itemaccountref
                    name: "ItemAccountRef"
                    type: "object"
                    description: ""
                    subattributes: *name-value

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

                  - &salesitemlinedetail-markupinfo
                    name: "MarkupInfo"
                    type: "object"
                    description: ""
                    subattributes: 
                      - name: "MarkupIncomeAccountRef"
                        type: "object"
                        description: ""
                        subattributes: *name-value

                      - name: "Percent"
                        type: "decimal"
                        description: ""

                      - name: "PriceLevelRef"
                        type: "object"
                        description: ""
                        subattributes: *name-value

                  - name: "Qty"
                    type: "decimal"
                    description: ""

                  - &salesitemlinedetail-servicedate
                    name: "ServiceDate"
                    type: "date-time"
                    description: ""

                  - &salesitemlinedetail-taxclassificationref
                    name: "TaxClassificationRef"
                    type: "object"
                    description: ""
                    subattributes: *name-value

                  - name: "TaxCodeRef"
                    type: "object"
                    description: "Details about the tax code associated with the sales line item."
                    subattributes:
                      - name: "value"
                        type: "string"
                        description: "The tax code ID."
                        foreign-key-id: "tax-code-id"

                  - &salesitemlinedetail-taxinclusiveamt
                    name: "TaxInclusiveAmt"
                    type: "decimal"
                    description: ""

                  - name: "UnitPrice"
                    type: "decimal"
                    description: ""

          - name: "Quantity"
            type: "decimal"
            description: ""

      - *line-id

      - *line-linenum

      - name: "SalesItemLineDetail"
        type: "object"
        description: ""
        subattributes:
          - *salesitemlinedetail-classref
          
          - *salesitemlinedetail-discountamt

          - *salesitemlinedetail-discountrate
          
          - *salesitemlinedetail-itemaccountref
          
          - *salesitemlinedetail-markupinfo
          
          - *salesitemlinedetail-servicedate
          
          - *salesitemlinedetail-taxclassificationref
          
          - *salesitemlinedetail-taxinclusiveamt


      - name: "SubtotalLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "ItemRef"
            type: "object"
            description: ""
            subattributes: *name-value

  - name: "LinkedTxn"
    type: "array"
    description: ""
    subattributes:
      - name: "TxnId"
        type: "string"
        description: ""

      - name: "TxnLineId"
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

  - name: "RecurDateRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "ShipAddr"
    type: "object"
    description: ""
    subattributes: *address

  - name: "ShipDate"
    type: "date-time"
    description: ""

  - name: "ShipMethodRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "ShipFromAddr"
    type: "object"
    description: ""
    subattributes: *address

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TaxSource"
    type: "string"
    description: ""

  - name: "TotalAmt"
    type: "decimal"
    description: ""

  - name: "TrackingNum"
    type: "string"
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
---