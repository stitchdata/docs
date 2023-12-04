---
tap-reference: "xero"
version: "1"

name: "nested_invoices"
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/nested_invoice.json

attributes:
  - name: "Type"
    type: "string"
    description: ""

  - name: "Contact"
    type: "array"
    description: "" #contacts

  - name: "Date"
    type: "date-time"
    description: ""

  - name: "DueDate"
    type: "date-time"
    description: ""

  - name: "Status"
    type: "string"
    description: ""

  - name: "LineAmountTypes"
    type: "string"
    description: ""

  - name: "LineItems"
    type: "array"
    description: "" #line_items

  - name: "SubTotal"
    type: "number"
    description: ""

  - name: "TotalTax"
    type: "number"
    description: ""

  - name: "Total"
    type: "number"
    description: ""

  - name: "TotalDiscount"
    type: "number"
    description: ""

  - name: "UpdatedDateUTC"
    type: "date-time"
    description: ""

  - name: "CurrencyCode"
    type: "string"
    description: ""

  - name: "CurrencyRate"
    type: "number"
    description: ""

  - name: "InvoiceID"
    type: "string"
    description: ""
    foreign-key: true

  - name: "InvoiceNumber"
    type: "string"
    description: ""

  - name: "Reference"
    type: "string"
    description: ""

  - name: "BrandingThemeID"
    type: "string"
    description: ""
    foreign-key: true

  - name: "Url"
    type: "string"
    description: ""

  - name: "SentToContact"
    type: "boolean"
    description: ""

  - name: "ExpectedPaymentDate"
    type: "date-time"
    description: ""

  - name: "PlannedPaymentDate"
    type: "date-time"
    description: ""

  - name: "HasAttachments"
    type: "boolean"
    description: ""

  - name: "AmountDue"
    type: "number"
    description: ""

  - name: "AmountPaid"
    type: "number"
    description: ""

  - name: "FullyPaidOnDate"
    type: "date-time"
    description: ""

  - name: "AmountCredited"
    type: "number"
    description: ""

  - name: "DueDateString"
    type: "string"
    description: ""

  - name: "IsDiscounted"
    type: "boolean"
    description: ""

  - name: "HasErrors"
    type: "boolean"
    description: ""

  - name: "DateString"
    type: "date-time"
    description: ""
---