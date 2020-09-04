---
tap: "quickbooks"
version: "1"
key: "bill"

name: "bills"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/bill"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/bills.json"
description: |
  The `{{ table.name }}` table contains info about the bills, or requests for payment from third parties, in your {{ integration.display_name }} instance.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a bill"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/bill#query-a-bill"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The bill ID."
    foreign-key-id: "bill-id"

  - name: "APAccountRef"
    type: "object"
    description: "Details about the AP account associated with the bill."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The ID of the AP account."
        foreign-key-id: "account-id"

  - name: "Balance"
    type: "decimal"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency used in the bill."
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
    description: "Details about the department associated with the bill."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The ID of the department."
        foreign-key-id: "department-id"

  - name: "domain"
    type: "string"
    description: ""

  - name: "DueDate"
    type: "date-time"
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
            description: "Details about the account associated with the line item."
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "value"
                type: "string"
                description: "The account ID."
                foreign-key-id: "account-id"

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
            description: "Details about the tax code associated with the line item."
            subattributes:
              - name: "value"
                type: "string"
                description: "The tax code ID."
                foreign-key-id: "tax-code-id"

          - name: "UnitPrice"
            type: "integer"
            description: ""

      - name: "LineNum"
        type: "integer"
        description: ""

  - name: "LinkedTxn"
    type: "array"
    description: |
      A list of transactions associated with the bill.
    subattributes:
      - name: "TxnId"
        type: "string"
        description: |
          The ID of the linked transaction.

          Depending on the `TxnType` value, this may be a foreign key to the following tables:

          - [bill_payments.Id](#bill_payments) (`TxnType: BillPaymentCheck`)
          - [purchase_orders.Id](#purchase_orders) (`TxnType: PurchaseOrder`)
        foreign-key-id: "transaction-bill-id"

      - name: "TxnType"
        type: "string"
        description: |
          The type of the linked transaction. Possible values are:

          - `BillPaymentCheck`
          - `PurchaseOrder`

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

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "SalesTermRef"
    type: "object"
    description: "Details about the sales term associated with the bill."
    subattributes:
      - name: "value"
        type: "string"
        description: "The sales term ID."
        foreign-key-id: "term-id"

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
    description: "Details about the vendor associated with the bill."
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: "The ID of the vendor."
        foreign-key-id: "vendor-id"
---