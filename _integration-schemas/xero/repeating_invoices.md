---
tap: "xero"
version: "1.0"

name: "repeating_invoices"
doc-link: &api-doc https://developer.xero.com/documentation/api/repeating-invoices
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/repeating_invoices.json
description: |
  The `repeating_invoices` table contains info about invoices set up to repeat in your Xero account. A repeating invoice is a recurring transaction, or a transaction that occurs on a regular basis.

replication-method: "Full Table"

api-method:
  name: getRepeatingInvoices
  doc-link: *api-doc

attributes:
  - name: "RepeatingInvoiceID"
    type: "string"
    primary-key: true
    description: "The repeating invoice ID."

  - name: "Type"
    type: "string"
    description: |
      The invoice type. Possible values are:

      - `ACCPAY` - A bill, or an Accounts Payable or supplier invoice
      - `ACCREC` - A sales invoice, or an Accounts Receivable or customer invoice

  - name: "Contact"
    type: 
    description: ""

  - name: "Schedule"
    type: "object"
    description: "Details about the schedule used by the repeating invoice."
    object-attributes:
      - name: "Unit"
        type: "string"
        description: "The unit of time used by the repeating invoice schedule. One of the following: `WEEKLY` or `MONTHLY`."

      - name: "DueDateType"
        type: "string"
        description: |
          The payment terms of the repeating invoice schedule. Possible values are:

          - `DAYSAFTERBILLDATE` - _n_ day(s) after the bill date
          - `DAYSAFTERBILLMONTH`- _n_ day(s) after the bill month
          - `OFCURRENTMONTH` - Of the current month
          - `OFFOLLOWINGMONTH` - Of the following month

      - name: "StartDate"
        type: "date-time"
        description: "The date the first invoice of the current version of the repeating schedule was generated. This value will change if/when the repeating invoice is modified."

      - name: "DueDate"
        type: "integer"
        description: "An integer used with the schedule's due date type to indicate the calendar date of the payment term."

      - name: "EndDate"
        type: "string"
        description: "The invoice end date. Applicable only if the template has a set end date."

      - name: "NextScheduleDate"
        type: "date-time"
        description: "The calendar date of the next invoice in the schedule to be generated."

      - name: "Period"
        type: "integer"
        description: "Integer used with the schedule unit. For example: `1` (every 1 week), `2` (every 2 months)"

  - name: "LineItems"
    type: "array"
    description: ""

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts of the line items in the repeating invoice. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive of tax
      - `NoTax` - Line items have no tax

  - name: "Reference"
    type: "string"
    description: "**Applicable only to `ACCREC` repeating invoices.** The additional reference number for the invoice."

  - name: "BrandingThemeID"
    type: "string"
    description: "The ID of the branding theme applied to the repeating invoice."
    foreign-key: true

  - name: "CurrencyCode"
    type: "string"
    description: "The currency that the invoice has been raised in."
    foreign-key: true

  - name: "Status"
    type: "string"
    description: |
      The status of the repeating invoice. Possible values are:

      - `DRAFT`
      - `AUTHORISED`

  - name: "SubTotal"
    type: "number"
    description: "The subtotal of the repeating invoice."

  - name: "TotalTax"
    type: "number"
    description: "The total tax on the repeating invoice."

  - name: "Total"
    type: "number"
    description: "The total amount of the repeating invoice, calculated as `SubTotal + TotalTax`."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the repeating invoice has an attachment."

  - name: "ID"
    type: "string"
    description: ""

---