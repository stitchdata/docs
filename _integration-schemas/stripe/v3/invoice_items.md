---
tap: "stripe"
version: "3"
key: ""

name: "invoice_items"
doc-link: 
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/invoice_items.json
description: |
  The `{{ table.name }}` table contains info about items contained in customer invoices.

replication-method: "Key-based Incremental"

api-method:
    name: "List all invoice items"
    doc-link: "https://stripe.com/docs/api/invoiceitems/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice item ID."
    foreign-key-id: "invoice-item-id"

  - name: "date"
    type: "string"
    replication-key: true
    description: "The date the invoice item was added to the invoice."  

  - name: "amount"
    type: "integer"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customer"
    type: "string"
    description: "The ID of the customer who will be billed for the invoice item."
    foreign-key-id: "customer-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "discountable"
    type: "boolean"
    description: ""

  - name: "discounts"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "invoice"
    type: "string"
    description: "The ID of the invoice associated with the invoice item."
    foreign-key-id: "invoice-id"

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "object"
    type: "string"
    description: ""

  - name: "period"
    type: "object"
    description: ""
    subattributes:
    - name: "end"
      type: "string"
      description: ""

    - name: "start"
      type: "string"
      description: ""


  - name: "plan"
    type: "object, string"
    description: ""
    subattributes:
    - name: "nickname"
      type: "string"
      description: ""

    - name: "updated_by_event_type"
      type: "string"
      description: "Description of the event"

    - name: "amount_decimal"
      type: "string"
      description: ""

    - name: "tiers"
      type: "array"
      description: ""
      subattributes:
      - name: "flat_amount"
        type: "integer"
        description: ""

      - name: "unit_amount"
        type: "integer"
        description: ""

      - name: "up_to"
        type: "integer"
        description: ""


    - name: "object"
      type: "string"
      description: ""

    - name: "aggregate_usage"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "statement_description"
      type: "string"
      description: ""

    - name: "product"
      type: "string"
      description: "The product whose pricing this plan determines."
      foreign-key-id: "product-id"

    - name: "statement_descriptor"
      type: "string"
      description: ""

    - name: "interval_count"
      type: "integer"
      description: ""

    - name: "transform_usage"
      type: "object"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "amount"
      type: "integer"
      description: ""

    - name: "interval"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: "The plan ID."
      foreign-key-id: "plan-id"

    - name: "trial_period_days"
      type: "integer"
      description: ""

    - name: "usage_type"
      type: "string"
      description: ""

    - name: "active"
      type: "boolean"
      description: ""

    - name: "tiers_mode"
      type: "string"
      description: ""

    - name: "billing_scheme"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "metadata"
      type: "object"
      description: ""
      subattributes:

    - name: "updated"
      type: "string"
      description: ""


  - name: "proration"
    type: "boolean"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "subscription"
    type: "string"
    description: ""

  - name: "subscription_item"
    type: "string"
    description: ""

  - name: "tax_rates"
    type: "array"
    description: ""
    subattributes:
    - name: "id"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "active"
      type: "boolean"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "created"
      type: "string"
      description: ""

    - name: "description"
      type: "string"
      description: ""

    - name: "display_name"
      type: "string"
      description: ""

    - name: "inclusive"
      type: "boolean"
      description: ""

    - name: "jurisdiction"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "percentage"
      type: "string"
      description: ""

    - name: "state"
      type: "string"
      description: ""


  - name: "unit_amount"
    type: "integer"
    description: ""

  - name: "unit_amount_decimal"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---