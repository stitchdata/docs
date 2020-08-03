---
tap: "codat"
version: "1"
key: "invoice"

name: "invoices"
doc-link: "https://docs.codat.io/docs/invoices-1"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about the invoices in your {{ integration.display_name }} instance. An invoice is an itemized record of goods or services sold to a [customer](#customers).

replication-method: "Key-based Incremental"

api-method:
  name: "List invoices for a company"
  doc-link: "https://docs.codat.io/reference/invoices#invoices_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the invoice."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "modifiedDate"
    type: "date-time"
    description: "The time the invoice was last modified."
    replication-key: true

  - name: "amountDue"
    type: "number"
    description: "The amount outstanding on the invoice."

  - name: "currency"
    type: "string"
    description: "The currency of the invoice."

  - name: "customerRef"
    type: "object"
    description: "Details about the customer the invoice is for."
    subattributes:
      - name: "companyName"
        type: "string"
        description: "The name of the company."

      - name: "id"
        type: "string"
        description: "The customer ID."
        foreign-key-id: "customer-id"

  - name: "dueDate"
    type: "date-time"
    description: "The date the invoice is due to be paid by."

  - name: "invoiceNumber"
    type: "string"
    description: "A user-friendly reference for the invoice."

  - name: "issueDate"
    type: "date-time"
    description: "The date the invoice was recorded in the accounting system."

  - name: "lineItems"
    type: "array"
    description: "A list of line items in the invoice."
    subattributes:
      - name: "description"
        type: "string"
        description: "A user-friendly name of the goods or services provided."

      - name: "discountAmount"
        type: "number"
        description: "The numerical value of any discounts applied."

      - name: "quantity"
        type: "number"
        description: "The number of units of goods or services provided."

      - name: "subTotal"
        type: "number"
        description: "The amount of the line, inclusive of discounts but exclusive of tax."

      - name: "taxAmount"
        type: "number"
        description: "The amount of tax for the line."

      - name: "totalAmount"
        type: "number"
        description: "The total amount of the line, including tax."

      - name: "unitAmount"
        type: "number"
        description: "The price of each unit of goods or services."

  - name: "paidOnDate"
    type: "date-time"
    description: "The date the invoice was marked as paid."

  - name: "paymentAllocations"
    type: "array"
    description: "A list of payment allocations associated with the invoice."
    subattributes:
      - name: "id"
        type: "string"
        description: "The payment allocation ID."

      - name: "currency"
        type: "string"
        description: "The currency of the payment allocation."

      - name: "date"
        type: "date-time"
        description: "The date the payment allocation was recorded."

      - name: "note"
        type: "string"
        description: "Additional info about the payment allocation."

      - name: "totalAmount"
        type: "number"
        description: "The total amount of the payment allocation."

  - name: "status"
    type: "string"
    description: |
      The status of the invoice. Possible values are:

      - `Draft` - Invoice has not been submitted to the Supplier. It may be in a pending state or is scheduled for future submission e.g. via email.
      - `Submitted` - Invoice is no longer a draft and has been sent to the Supplier. In this state, no payments have been made against the invoice (amountDue == totalAmount).
      - `PartiallyPaid` - The balance paid against the invoice is positive, but less than the total invoice amount (0 < amountDue < totalAmount).
      - `Paid` - Invoice is paid in full. This includes if the Invoice has been credited or overpaid (amountDue == 0).
      -` Void` - An invoice can become Void by being deleted, refunded, written off, or cancelled. Note, a voided Invoice may still be partiallyPaid and so all outstanding amounts on voided Inovices are removed from the AR (Accounts Receivable) account.

  - name: "subTotal"
    type: "number"
    description: "The total amount of the invoice, excluding tax."

  - name: "totalAmount"
    type: "number"
    description: "The amount of the invoice, including tax."

  - name: "totalDiscount"
    type: "number"
    description: "The numerical value of discounts applied to the invoice."

  - name: "totalTaxAmount"
    type: "number"
    description: "The amount of tax on the invoice."
---