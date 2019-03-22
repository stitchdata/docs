---
tap: "invoiced"
version: "1.0"

name: "estimates"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/estimates.json"
description: |
  The `{{ table.name }}` table contains info about the estimates, or quotes you provide to customers, in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all estimates"
    doc-link: "https://invoiced.com/docs/api/#list-all-estimates"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The estimate ID."
    #foreign-key-id: "estimate-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the estimate was last updated."

  # - name: "approval"
  #   type: "object"
  #   description: ""
  #   subattributes: 

  - name: "approved"
    type: "boolean"
    description: "Indicates whether the estimate has been approved."

  - name: "balance"
    type: "number"
    description: "The balance of the estimate."

  - name: "closed"
    type: "boolean"
    description: "If `true`, an estimate is closed and considered bad debt. No further payments are allowed."

  - name: "created_at"
    type: "date-time"
    description: "The time the estimate was created."

  - name: "currency"
    type: "string"
    description: |
      The [three letter ISO code](https://en.wikipedia.org/wiki/ISO_4217){:target="new"} used by the estimate.

  - name: "customer"
    type: "integer"
    description: "The ID of the customer associated with the estimate."
    foreign-key-id: "customer-id"

  - name: "date"
    type: "date-time"
    description: "The date of the estimate."

  - name: "deposit"
    type: "number"
    description: "The deposit required for the estimate."

  - name: "deposit_paid"
    type: "boolean"
    description: "Indicates whether the `deposit` has been paid in full."

  - name: "discounts"
    type: "array"
    description: "The discounts applicable to the estimate."
    subattributes:
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
    description: "If `true`, the estimate is a draft. If `false`, the estimate is considered outstanding."

  - name: "expiration_date"
    type: "date-time"
    description: "The expiration date of the estimate."

  - name: "invoice"
    type: "integer"
    description: "The ID of the invoice associated with the estimate."
    foreign-key-id: "invoice-id"

  - name: "items"
    type: "array"
    description: "The line items associated with the estimate."
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
    description: "Additional information about the estimate."
    subattributes:

  - name: "name"
    type: "string"
    description: "The name of the estimate."

  - name: "notes"
    type: "string"
    description: "Additional notes about the estimate."

  - name: "number"
    type: "string"
    description: "The reference number assigned to the estimate."

  - name: "paid"
    type: "boolean"
    description: "Indicates if the estimate has been paid."

  - name: "payment_terms"
    type: "string"
    description: "The payment terms for the estimate."

  - name: "status"
    type: "string"
    description: |
      The status of the estimate. Possible values are:

      - `draft`
      - `not_sent`
      - `sent`
      - `approved`
      - `invoiced`
      - `declined`

  - name: "subtotal"
    type: "number"
    description: "The subtotal of the estimate."

  - name: "taxes"
    type: "array"
    description: "The taxes applicable to the estimate."
    subattributes: *taxes

  - name: "total"
    type: "number"
    description: "The total of the estimate."
---