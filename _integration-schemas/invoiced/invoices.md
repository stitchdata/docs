---
tap: "invoiced"
version: "1.0"

name: "invoices"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/invoices.json"
description: |
  The `{{ table.name }}` table contains info about the invoices in your {{ integration.display_name }} account. An invoice represents a balance owed to you by a customer.

replication-method: "Key-based Incremental"

api-method:
    name: "List all invoices"
    doc-link: "https://invoiced.com/docs/api/#list-all-invoices"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The invoice ID."
    foreign-key-id: "invoice-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the invoice was last updated."

  - name: "attempt_count"
    type: "integer"
    description: "The number of payment attempts for the invoice."

  - name: "autopay"
    type: "boolean"
    description: "If `true`, AutoPay is enabled for the invoice."

  - name: "balance"
    type: "number"
    description: "The balance of the invoice."

  - name: "closed"
    type: "boolean"
    description: "If `true`, an invoice is closed and considered bad debt. No further payments are allowed."

  - name: "created_at"
    type: "date-time"
    description: "The time the invoice was created."

  - name: "currency"
    type: "string"
    description: |
      The [three letter ISO code](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} used by the invoice.

  - name: "customer"
    type: "integer"
    description: "The ID of the customer associated with the invoice."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date of the invoice."

  - name: "discounts"
    type: "array"
    description: "The discounts applicable to the estimate."
    subattributes: &discounts
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The discount ID."
        foreign-key-id: "discount-id"

      - name: "object"
        type: "string"
        description: "This will be `discount`."

      - name: "amount"
        type: "integer"
        description: "The amount of the discount."

      - name: "coupon"
        type: "object"
        description: "The coupon the discount was calculated from, if applicable."

      - name: "expires"
        type: "date-time"
        description: "The time until the discount expires." 

  - name: "draft"
    type: "boolean"
    description: "If `true`, the invoice is a draft. If `false`, the invoice is considered outstanding."

  - name: "due_date"
    type: "date-time"
    description: "The due date of the invoice."

  - name: "items"
    type: "array"
    description: "The line items associated with the invoice."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The line item ID."
        foreign-key-id: "line-item-id"

      - name: "object"
        type: "string"
        description: "This will be `line_item`."

      - name: "catalog_item"
        type: "string"
        description: "The catalog item ID."

      - name: "type"
        type: "string"
        description: "The line item type."

      - name: "name"
        type: "string"
        description: "The name of the line item."

      - name: "description"
        type: "string"
        description: "The description of the line item."

      - name: "quantity"
        type: "integer"
        description: "The quantity of the line item."

      - name: "unit_cost"
        type: "integer"
        description: "The unit cost or rate of the line item."

      - name: "amount"
        type: "integer"
        description: "The total amount of the line item, calculated as `quantity x unit_cost`."

      - name: "discountable"
        type: "boolean"
        description: "If `true`, the line item is discountable and included in the credit note's total discounts."

      - name: "discounts"
        type: "array"
        description: "The discounts applicable to the line item."
        subattributes: *discounts

      - name: "taxable"
        type: "boolean"
        description: "If `true`, the line item is taxable and included in the credit note's total taxes."

      - name: "taxes"
        type: "array"
        description: "The taxes applicable to the line item."
        subattributes: &taxes
          - name: "id"
            type: "integer"
            primary-key: true
            description: "The tax ID."
            foreign-key-id: "tax-id"

          - name: "object"
            type: "string"
            description: "This will be `tax`."

          - name: "amount"
            type: "number"
            description: "The amount of tax."

          - name: "tax_rate"
            type: "number"
            description: "The tax rate the tax was calculated from."

      - name: "metadata"
        type: "object"
        description: "Additional information about the line item."
        subattributes: &metadata
          - name: ""
            type: 
            description: ""

  - name: "metadata"
    type: "object"
    description: "Additional information about the invoice."
    subattributes:

  - name: "name"
    type: "string"
    description: "The name of the invoice."

  - name: "needs_attention"
    type: "boolean"
    description: ""

  - name: "next_payment_attempt"
    type: "date-time"
    description: "The time of the next scheduled payment attempt, when in automatic collection."

  - name: "notes"
    type: "string"
    description: "Additional notes about the invoice."

  - name: "number"
    type: "string"
    description: "The reference number assigned to the invoice."

  - name: "paid"
    type: "boolean"
    description: "Indicates whether an invoice has been paid in full."

  - name: "payment_terms"
    type: "string"
    description: "The payment terms for the invoice. "

  - name: "status"
    type: "string"
    description: |
      The status of the invoice. Possible values are:

      - `draft`
      - `not_sent`
      - `sent`
      - `viewed`
      - `past_due`
      - `pending`
      - `paid`

  - name: "subscription"
    type: "integer"
    description: "The subscription ID, if the invoice came from a subscription."
    foreign-key-id: "subscription-id"

  - name: "subtotal"
    type: "number"
    description: "The subtotal of the invoice."

  - name: "taxes"
    type: "array"
    description: "The taxes applicable to the invoice."
    subattributes: *taxes

  - name: "total"
    type: "number"
    description: "The total of the invoice."
---