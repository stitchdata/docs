---
tap: "quickbooks"
version: "1"
key: "purchase-order"

name: "purchase_orders"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/purchaseorder"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/purchase_orders.json"
description: |
  The `{{ table.name }}` table contains info about purchase orders in your {{ integration.display_name }} instance. A purchase order is a request to purchase goods or services from a third party.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a purchase order"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/purchaseorder/#query-a-purchaseorder"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The purchase order ID."
    foreign-key-id: "purchase-order-id"

  - name: "APAccountRef"
    type: "object"
    description: "Details about the AP account associated with the purchase order."
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
    description: "Details about the currency the purchase order is in."
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

  - name: "DepartmentRef"
    type: "object"
    description: "Details about the department associated with the purchase order."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The department ID."
        foreign-key-id: "department-id"

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

      - name: "ItemBasedExpenseLineDetail"
        type: "object"
        description: "Details about the item associated with the line item."
        subattributes:
          - name: "BillableStatus"
            type: "string"
            description: ""

          - name: "ClassRef"
            type: "object"
            description: "Details about the class associated with the line item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: "The class ID."
                foreign-key-id: "class-id"

          - name: "CustomerRef"
            type: "object"
            description: "Details about the customer associated with the line item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: "The customer ID."
                foreign-key-id: "customer-id"

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

      - name: "LineNum"
        type: "integer"
        description: ""

  - name: "LinkedTxn"
    type: "array"
    description: "Details about the transactions associated with the purchase order."
    subattributes:
      - name: "TxnId"
        type: "string"
        description: "The ID of the bill associated with the purchase order."
        foreign-key-id: "bill-id"

      - name: "TxnType"
        type: "string"
        description: "This will be `Bill`."

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

  - name: "POStatus"
    type: "string"
    description: ""

  - name: "ShipAddr"
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

      - name: "Long"
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

  - name: "VendorAddr"
    type: "object"
    description: ""
    subattributes:
      - name: "City"
        type: "string"
        description: ""

      - name: "Country"
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

      - name: "Long"
        type: "string"
        description: ""

  - name: "VendorRef"
    type: "object"
    description: "Details about the vendor associated with the purchase order."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The vendor ID."
        foreign-key-id: "vendor-id"
---