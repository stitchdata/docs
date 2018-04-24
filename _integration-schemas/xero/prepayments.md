---
tap: "xero"
version: "1.0"

name: "prepayments"
doc-link: &api-doc https://developer.xero.com/documentation/api/prepayments
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/prepayments.json
description: |
  The `prepayments` table contains info about prepayments, which are payments made in advance of an invoice being raised for a customer or a bill being received from a supplier.

replication-method: "Incremental"

api-method:
  name: getPrepayments
  doc-link: *api-doc

attributes:
  - name: "PrepaymentID"
    type: "string"
    primary-key: true
    description: "The prepayment ID."

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
    type: 
    description: ""

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
    description: ""
    array-attributes:

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
    foreign-key: true

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
    description: ""
    array-attributes:

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the prepayment has an attachment."

  - name: "DateString"
    type: "date-time"
    description: ""
---