---
tap: "xero"
version: "1.0"

name: "prepayments"
doc-link: &api-doc https://developer.xero.com/documentation/api/prepayments
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/prepayments.json
description: |
  The `{{ table.name }}` table contains info about prepayments, which are payments made in advance of an invoice being raised for a customer or a bill being received from a supplier.

replication-method: "Key-based Incremental"

api-method:
  name: getPrepayments
  doc-link: *api-doc

attributes:
  - name: "PrepaymentID"
    type: "string"
    primary-key: true
    description: "The prepayment ID."
    foreign-key-id: "prepayment-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the prepayment was last updated, in UTC."

  - name: "Type"
    type: "string"
    description: |
      The prepayment type. Possible values are:

      - `RECEIVE-PREPAYMENT`
      - `SPEND-PREPAYMENT`

  - name: "Contact"
    type: ""
    description: |
      Details about the contact(s) associated with the prepayment.

      {{ integration.subtable-note | flatify | replace:"table_name","contacts" }}

  - name: "Date"
    type: "date-time"
    description: "The date the prepayment was created."

  - name: "Status"
    type: "string"
    description: |
      The status of the prepayment. Possible values are:

      - `AUTHORISED`
      - `PAID`
      - `VOIDED`

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts of the line items in the prepayment. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive of tax
      - `NoTax` - Line items have no tax

  - name: "LineItems"
    type: "array"
    description: "Details about the line items contained in the prepayment."
    subattributes:
      - name: "LineItemID"
        type: "string"
        description: "The ID of the line item."

      - name: "Description"
        type: "string"
        description: "The description of the line item."

      - name: "Quantity"
        type: "number"
        description: "The quantity of the line item."

      - name: "UnitAmount"
        type: "number"
        description: "The amount of the line item."

      - name: "AccountCode"
        type: "string"
        description: "The account code associated with the line item."

      - name: "ItemCode"
        type: "string"
        description: "The code associated with the line item."

      - name: "TaxType"
        type: "string"
        description: "The tax type associated with the line item."

      - name: "LineAmount"
        type: "number"
        description: "The total of the line item, calculated as `UnitAmount x Quantity`."

      - name: "TaxAmount"
        type: "number"
        description: "The total tax of the line item."

      - name: "DiscountRate"
        type: "number"
        description: "The discount rate of the line item, if applicable."

      - name: "Tracking"
        type: ""
        description: |
          Details about the tracking categories applied to the line item, if applicable.

          {{ integration.subsubtable-note | flatify | replace:"table_name","tracking_categories" }}

  - name: "SubTotal"
    type: "number"
    description: "The subtotal of the prepayment."

  - name: "TotalTax"
    type: "number"
    description: "The total tax on the prepayment."

  - name: "Total"
    type: "number"
    description: "The total amount of the prepayment, calculated as `SubTotal + TotalTax`."

  - name: "CurrencyCode"
    type: "string"
    description: "The currency used for the prepayment."
    foreign-key-id: "currency-code"

  - name: "CurrencyRate"
    type: "number"
    description: "The currency rate for a multicurrency prepayment."

  - name: "Reference"
    type: "string"
    description: "If available, the number of the invoice associated with the prepayment."

  - name: "RemainingCredit"
    type: "number"
    description: "The remaining credit balance on the prepayment."

  - name: "Allocations"
    type: "array"
    description: "Details about the allocation of the prepayment."
    subattributes:
      - name: "Date"
        type: "date-time"
        description: |
          The date the {{ table.name | append: " " | remove: "s " | replace: "_", " " }} was applied.

      - name: "Amount"
        type: "number"
        description: "The amount being applied to the invoice."

      - name: "Invoice"
        type: "object"
        description: |
          Details about the invoices the {{ table.name | append: " " | remove: "s " | replace: "_", " " }} has been allocated against.
        subattributes:
          - name: "InvoiceID"
            type: "string"
            description: |
              The ID of the invoice the {{ table.name | append: " " | remove: "s " | replace: "_", " " }} is being allocated against.
            foreign-key-id: "invoice-id"

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the prepayment has an attachment."

  - name: "DateString"
    type: "date-time"
    description: "The date the prepayment was made."
---