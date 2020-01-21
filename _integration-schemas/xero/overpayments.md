---
tap: "xero"
version: "1"

name: "overpayments"
doc-link: &api-doc https://developer.xero.com/documentation/api/overpayments
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/overpayments.json
description: |
  The `{{ table.name }}` table contains info about overpayments, which are transactions where a customer pays too much or you mistakenly overpay a supplier.

replication-method: "Key-based Incremental"

api-method:
  name: getOverpayments
  doc-link: *api-doc

attributes:
  - name: "OverpaymentID"
    type: "string"
    primary-key: true
    description: "The overpayment ID."
    foreign-key-id: "overpayment-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the overpayment was last updated, in UTC."

  - name: "Type"
    type: "string"
    description: |
      The overpayment type. Possible values are:

      - `RECEIVE-OVERPAYMENT`
      - `SPEND-OVERPAYMENT`

  - name: "Contact"
    type: "array"
    description: |
      Details about the contact(s) associated with the overpayment.
    subattributes:
      - description: |
          This will contain the same attributes as the `contacts` table. Refer to the [`contacts`](#contacts) table schema for details.

  - name: "Date"
    type: "date-time"
    description: "The date the overpayment was made."

  - name: "Status"
    type: "string"
    description: |
      The status of the overpayment. Possible values are:

      - `AUTHORISED`
      - `PAID`
      - `VOIDED`

  - name: "AppliedAmount"
    type: "number"
    description: "The amount of the overpayment that has been applied."

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts of the line items in the overpayment. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive of tax
      - `NoTax` - Line items have no tax

  - name: "LineItems"
    type: "array"
    description: "Details about the line items contained in the overpayment."
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
        type: "array"
        description: |
          Details about the tracking categories applied to the line item, if applicable.
        subattributes:
          - description: |
              This will contain the same attributes as the `tracking_categories` table. Refer to the [`tracking_categories`](#tracking_categories) table schema for details.

  - name: "SubTotal"
    type: "number"
    description: "The subtotal of the overpayment, excluding taxes."

  - name: "TotalTax"
    type: "number"
    description: "The total tax on the overpayment."

  - name: "Total"
    type: "number"
    description: "The total of the overpayment, calculated as `SubTotal + TotalTax`."

  - name: "CurrencyCode"
    type: "string"
    description: "The currency used for the overpayment."
    foreign-key-id: "currency-code"

  - name: "CurrencyRate"
    type: "number"
    description: "The currency rate for a multicurrency overpayment."

  - name: "RemainingCredit"
    type: "number"
    description: "The remaining credit balance on the overpayment."

  - name: "Allocations"
    type: "array"
    description: "Details about the allocations associated with the overpayment."
    subattributes:
      - name: "Date"
        type: "date-time"
        description: |
          The date the overpayment was applied.

      - name: "Amount"
        type: "number"
        description: "The amount being applied to the invoice."

      - name: "Invoice"
        type: "object"
        description: |
          Details about the invoices the overpayment has been allocated against.
        subattributes:
          - name: "InvoiceID"
            type: "string"
            description: |
              The ID of the invoice the overpayment is being allocated against.
            foreign-key-id: "invoice-id"

  - name: "Payments"
    type: "array"
    description: |
      Details about the payments associated with the overpayment.
    subattributes:
      - description: |
          This will contain the same attributes as the `payments` table. Refer to the [`payments`](#payments) table schema for details.

  - name: "Reference"
    type: "string"
    description: "The overpayment's reference."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the overpyament has an attachment."

  - name: "DateString"
    type: "date-time"
    description: "The date the overpayment was made."
---