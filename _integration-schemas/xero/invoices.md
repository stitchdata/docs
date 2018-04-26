---
tap: "xero"
version: "1.0"

name: "invoices"
doc-link: &api-doc https://developer.xero.com/documentation/api/invoices
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/invoices.json
description: |
  The `invoices` table contains info about sales invoices, which are requests for payment for goods and services.

replication-method: "Incremental"

api-method:
  name: getInvoices
  doc-link: *api-doc

attributes:
  - name: "InvoiceID"
    type: "string"
    primary-key: true
    description: "The invoice ID."

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the invoice was last updated, in UTC."

  - name: "Type"
    type: "string"
    description: |
      The type of the invoice. Possible values are:

      - `ACCPAY` - A bill, or an Accounts Payable or supplier invoice
      - `ACCREC` - A sales invoice, or an Accounts Receivable or customer invoice

  - name: "Contact"
    type: "" 
    description: |
      Details about the contact(s) associated with the invoice.

      {{ integration.subtable-note | flatify | replace:"table_name","contacts" }}

  - name: "Date"
    type: "date-time"
    description: "The date the invoice was issued."

  - name: "DueDate"
    type: "date-time"
    description: "The date the invoice is due."

  - name: "Status"
    type: "string"
    description: |
      The status of the invoice. Possible values are:

      - `DRAFT` 
      - `SUBMITTED`
      - `AUTHORISED`
      - `DELETED`
      - `VOIDED`
      - `PAID`

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts that the line items in the invoice contain. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive tax
      - `NoTax` - Line items have no tax
    doc-link: https://developer.xero.com/documentation/api/types#LineAmountTypes

  - name: "LineItems"
    type: "array"
    description: "Details about the line items contained in the invoice."
    array-attributes:
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
    description: "The total of the invoice, excluding taxes."

  - name: "TotalTax"
    type: "number"
    description: "The total tax on the invoice."

  - name: "Total"
    type: "number"
    description: "The total of the invoice, calculated as `SubTotal + TotalTax`."

  - name: "TotalDiscount"
    type: "number"
    description: "The total of discounts applied to invoice line items."

  - name: "CurrencyCode"
    type: "string"
    description: "The currency that the invoice has been raised in."
    foreign-key: true

  - name: "CurrencyRate"
    type: "number"
    description: "The currency rate, if the invoice is a multicurrency invoice."

  - name: "InvoiceNumber"
    type: "string"
    description: |
      An identifier for the invoice. The value this field contains varies depending on the invoice `Type`:

      - `ACCPAY` - A non-unique alpha-numeric code identifying the invoice. In the Xero UI, this displays as **Reference**.
      - `ACCREC` - A unique alpha-numeric code identifying the invoice.

  - name: "Reference"
    type: "string"
    description: "**Applicable only to `Type: ACCREC` invoices**. An additional reference number."

  - name: "BrandingThemeID"
    type: "string"
    description: "The ID of the branding theme applied to the invoice."
    foreign-key: true

  - name: "Url"
    type: "string"
    description: "The URL link to a source document."

  - name: "SentToContact"
    type: "boolean"
    description: "IF `true`, the invoice will display in the Xero app as 'Sent'."

  - name: "ExpectedPaymentDate"
    type: "date-time"
    description: "For sales invoices (`Type: ACCREC`), the expected payment date."

  - name: "ExpectedPaymentDateString"
    type: "date-time"
    description: "For sales invoices, the expected payment date."

  - name: "PlannedPaymentDate"
    type: "date-time"
    description: "For bills (`Type: ACCPAY`), the planned payment date."

  - name: "PlannedPaymentDateString"
    type: "date-time"
    description: "For bills, the planned payment date."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the invoice has an attachment."

  - name: "Payments"
    type: ""
    description: |
      Details about the payments associated with the invoice.

      {{ integration.subtable-note | flatify | replace:"table_name","payments" }}

  - name: "CreditNotes"
    type: ""
    description: |
      Details about the credit notes associated with the invoice.

      {{ integration.subtable-note | flatify | replace:"table_name","credit_notes" }}

  - name: "Prepayments"
    type: ""
    description: |
      Details about the prepayments associated with the invoice.

      {{ integration.subtable-note | flatify | replace:"table_name","prepayments" }}

  - name: "Overpayments"
    type: ""
    description: |
      Details about the overpayments associated with the invoice.

      {{ integration.subtable-note | flatify | replace:"table_name","overpayments" }}

  - name: "AmountDue"
    type: "number"
    description: "The amount remaining to be paid on the invoice."

  - name: "AmountPaid"
    type: "number"
    description: "The sum of payments received for the invoice."

  - name: "FullyPaidOnDate"
    type: "date-time"
    description: "The date the invoice was fully paid."

  - name: "AmountCredited"
    type: "number"
    description: "The sum of all credit notes, overpayments, and prepayments applied to the invoice."

  - name: "DueDateString"
    type: "date-time"
    description: "The date the invoice is due."

  # - name: "IsDiscounted"
  #   type: "boolean"
  #   description: ""

  # - name: "HasErrors"
  #   type: "boolean"
  #   description: ""

  - name: "DateString"
    type: "date-time"
    description: "The date the invoice was issued."
---