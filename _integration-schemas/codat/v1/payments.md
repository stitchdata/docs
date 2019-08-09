---
tap: "codat"
version: "1.0"
key: "payment"

name: "payments"
doc-link: "https://docs.codat.io/docs/payments-1"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/payments.json"
description: |
  The `{{ table.name }}` table contains info about the payments, or Accounts Receivable transactions, in your {{ integration.display_name }} instance. This includes details about invoices and credit notes.

replication-method: "Full Table"

api-method:
    name: "List payments for a company"
    doc-link: "https://docs.codat.io/reference/payments#payments_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the payment."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The payment ID."

  - name: "currency"
    type: "string"
    description: "The ISO currency code the payment was recorded in."

  - name: "customerRef"
    type: "object"
    description: "Details about the customer the payment was recorded against."
    subattributes:
      - name: "companyName"
        type: "string"
        description: "The name of the company."

      - name: "id"
        type: "string"
        description: "The customer's ID."
        foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date the payment was recorded."

  - name: "lines"
    type: "array"
    description: "A list of lines associated with the payment."
    subattributes:
      - name: "amount"
        type: "number"
        description: "The amount in the payment currency."

      - name: "links"
        type: "array"
        description: "A list of allocations for the payment line."
        subattributes:
          - name: "id"
            type: "string"
            description: |
              The ID of the transaction represented by the link. Depending on the link `type`, this will be equivalent to the following:

              - `CreditNote`: [`credit_notes.id`](#credit_notes)
              - `Invoice`: [`invoice.id`](#invoices)
              - `Payment`: [`payment.id`](#payments)

          - name: "type"
            type: "string"
            description: |
              The type of the link. Possible values are:

              - `Unlinked` (unused)
              - `Invoice`
              - `CreditNote`
              - `Refund`
              - `Payment`
              - `PaymentOnAccount`
              - `Other`

  - name: "note"
    type: "string"
    description: "Additional information about the payment."

  - name: "totalAmount"
    type: "number"
    description: "The amount of the payment in the payment currency."
---