---
tap: "codat"
version: "1"
key: "credit-note"

name: "credit_notes"
doc-link: "https://docs.codat.io/docs/credit-notes"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/credit_notes.json"
description: |
  The `{{ table.name }}` table contains info about the credit notes in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
    name: "List credit notes for a company"
    doc-link: "https://docs.codat.io/reference/creditnotes#creditnotes_listpaged"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The credit note ID."
    foreign-key-id: "credit-note-id"

  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the credit note."

  - name: "creditNoteNumber"
    type: "string"
    description: "A user-friendly reference for the credit note."

  - name: "currency"
    type: "string"
    description: "The currency for the credit note."

  - name: "customerRef"
    type: "object"
    description: "Details about the customer the credit note has been issued to."
    subattributes:
      - name: "companyName"
        type: "string"
        description: "The name of the customer's company."

      - name: "id"
        type: "string"
        description: "The customer ID."
        foreign-key-id: "customer-id"

  - name: "issueDate"
    type: "date-time"
    description: "The date of the credit note as recorded in the accounting system."

  - name: "paymentAllocations"
    type: "array"
    description: "A list of credit note payment allocations."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The payment allocation ID."
        foreign-key-id: "payment-allocation-id"

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

  - name: "remainingCredit"
    type: "number"
    description: "The unused balance of the `totalAmount` originally raised."

  - name: "status"
    type: "string"
    description: |
      The status of the credit note. Possible values are:

      - `Draft`
      - `Submitted`
      - `Paid`
      - `Void`

  - name: "totalAmount"
    type: "number"
    description: "The total amount of the credit that has been applied to the customer's account receivable."
---