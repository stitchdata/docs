---
tap: "quickbooks"
version: "1"
key: "purchase"

name: "purchases"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/purchase"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/purchases.json"
description: |
  The `{{ table.name }}` table contains info about the purchases recorded in your {{ integration.display_name }} instance. This table includes all purchase types: `Cash`, `Check`, and `CreditCard`.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a purchase"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/purchase/#query-a-purchase"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The purchase ID."
    foreign-key-id: "purchase-id"

  - name: "AccountRef"
    type: "object"
    description: "Details about the account associated with the purchase."
    subattributes: &account-attributes
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

  - name: "Credit"
    type: "boolean"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the purchase is in."
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

  - name: "EntityRef"
    type: "object"
    description: "Details about the entity with whom the purchase is associated."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: |
          The type of the entity. Possible values are:

          - `Customer`
          - `Employee`
          - `Vendor`

      - name: "value"
        type: "string"
        description: |
          The ID of the entity associated with the purchase.

          Depending on the `type` value, this may be a foreign key to the following tables:

          - [customers.Id](#customers) (`type: Customer`)
          - [employees.Id](#employees) (`type: Employee`)
          - [vendors.Id](#vendors) (`type: Vendor`)
        foreign-key-id: "entity-id"

  - name: "ExchangeRate"
    type: "decimal"
    description: ""

  - name: "Line"
    type: "array"
    description: ""
    subattributes:
      - name: "AccountBasedExpenseLineDetail"
        type: "object"
        description: ""
        subattributes: 
          - name: "AccountRef"
            type: "object"
            description: "Details about the account associated with the line item."
            subattributes: *account-attributes

          - name: "BillableStatus"
            type: "string"
            description: ""

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

          - name: "TaxCodeRef"
            type: "object"
            anchor-id: 1
            description: "Details about the tax code associated with the line item."
            subattributes: &tax-code
              - name: "value"
                type: "string"
                description: "The tax code ID."
                foreign-key-id: "tax-code-id"

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
        description: ""
        subattributes:
          - name: "BillableStatus"
            type: "string"
            description: ""

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
            anchor-id: 2
            description: "Details about the tax code associated with the line item."
            subattributes: *tax-code

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

  - name: "PaymentType"
    type: "string"
    description: ""

  - name: "PrintStatus"
    type: "string"
    description: ""

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "PurchaseEx"
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

  - name: "RemitToAddr"
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
---