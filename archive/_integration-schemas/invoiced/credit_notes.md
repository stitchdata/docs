---
tap: "invoiced"
version: "1"

name: "credit_notes"
doc-link: "https://invoiced.com/docs/api/#credit-note-object"
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/credit_notes.json"
description: |
  The `{{ table.name }}` table contains info about the credit notes in your {{ integration.display_name }} account. A credit note represents a balance you owe to a customer.

replication-method: "Key-based Incremental"

api-method:
    name: "List all credit notes"
    doc-link: "https://invoiced.com/docs/api/#list-all-credit-notes"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The credit note ID."
    foreign-key-id: "credit-note-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the credit note was last updated."

  - name: "balance"
    type: "number"
    description: "The balance owed on the credit note."

  - name: "closed"
    type: "boolean"
    description: "If `true`, the credit note has been closed and is considered bad debt. No further payments are allowed."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the credit note was created."

  - name: "currency"
    type: "string"
    description: |
      The [three letter ISO code](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} for the currency used in the credit note.

  - name: "customer"
    type: "integer"
    description: "The ID of the customer associated with the credit note."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date of the credit note."

  - name: "discounts"
    type: "array"
    description: "The discounts associated with the credit note."
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
    description: "If `false`, the credit note is considered outstanding. If `true`, the credit note is a draft."

  - name: "invoice"
    type: "integer"
    description: "The ID of the invoice associated with the credit note."
    foreign-key-id: "invoice-id"

  - name: "items"
    type: "array"
    description: "The line items associated with the credit note."
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
    description: "Additional information about the credit note."
    subattributes: *metadata
  
  - name: "name"
    type: "string"
    description: "The internal name of the credit note."

  - name: "notes"
    type: "string"
    description: "Additional notes displayed on the credit note."

  - name: "number"
    type: "string"
    description: "The reference number assigned to the credit note, used in the {{ integration.display_name }} dashboard."

  - name: "paid"
    type: "boolean"
    description: "If `true`, the credit note has been paid in full."

  - name: "status"
    type: "string"
    description: |
      The status of the credit note. Possible values are:

      - `draft`
      - `open`
      - `paid`
      - `closed`

  - name: "subtotal"
    type: "number"
    description: "The subtotal of the credit note."

  - name: "taxes"
    type: "array"
    description: "The taxes associated with the credit note."
    subattributes: *taxes

  - name: "total"
    type: "number"
    description: "The total of the credit note."
---