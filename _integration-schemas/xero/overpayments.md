---
tap: "xero"
version: "1.0"

name: "overpayments"
doc-link: &api-doc https://developer.xero.com/documentation/api/overpayments
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/overpayments.json
description: |
  The `overpayments` table contains info about overpayments, which are transactions where a customer pays too much or you mistakenly overpay a supplier.

replication-method: "Incremental"

api-method:
  name: getOverpayments
  doc-link: *api-doc

attributes:
  - name: "OverpaymentID"
    type: "string"
    primary-key: true
    description: ""

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "Type"
    type: "string"
    description: |
      The overpayment type. Possible values are:

      - `RECEIVE-OVERPAYMENT`
      - `SPEND-OVERPAYMENT`

  - name: "Contact"
    type: 
    description: ""

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
    description: ""
    array-attributes:

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
    foreign-key: true

  - name: "CurrencyRate"
    type: "number"
    description: "The currency rate for a multicurrency overpayment."

  - name: "RemainingCredit"
    type: "number"
    description: "The remaining credit balance on the overpayment."

  - name: "Allocations"
    type: "array"
    description: ""
    array-attributes:

  - name: "Payments"
    type: "array"
    description: ""
    array-attributes:

  - name: "Reference"
    type: "string"
    description: ""

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the overpyament has an attachment."

  - name: "ID"
    type: "string"
    description: ""

  - name: "DateString"
    type: "date-time"
    description: ""
---