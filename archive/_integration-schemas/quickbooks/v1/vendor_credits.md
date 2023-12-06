---
tap: "quickbooks"
version: "1"
key: "vendor-credit"

name: "vendor_credits"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/vendorcredit"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/vendor_credits.json"
description: |
  The `{{ table.name }}` table contains info about credits that a vendor owes your company.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a vendor credit"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/vendorcredit#query-a-vendorcredit"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The vendor credit ID."
    foreign-key-id: "vendor-credit-id"

  - name: "APAccountRef"
    type: "object"
    description: "Details about the AP account associated with the vendor credit."
    subattributes: &account-attributes
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The account ID."
        foreign-key-id: "account-id"

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the vendor credit is in."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The currency ID."
        foreign-key-id: "currency-id"

  - name: "DepartmentRef"
    type: "object"
    description: "Details about the department associated with the vendor credit."
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
      - name: "AccountBasedExpenseLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "AccountRef"
            type: "object"
            description: ""
            subattributes: *account-attributes

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

          - name: "TaxCodeRef"
            type: "object"
            description: "Details about the tax code associated with the line item."
            subattributes:
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

      - name: "LineNum"
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
    description: "Details about the vendor associated with the vendor credit."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The vendor ID."
        foreign-key-id: "vendor-id"
---