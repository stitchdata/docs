---
tap: "stripe"
version: "2"
key: ""

name: "invoice_line_items"
doc-link: "https://stripe.com/docs/api/invoices/line_item"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/invoice_line_items.json
description: |
  The `{{ table.name }}` table contains info about the line items contained in invoices.

  **Note**: In order to replicate invoice line item data, the [`invoices`](#invoices) table must also be set to replicate.

  #### Invoice line item replication

  To replicate invoice line items, Stitch will use the Replication Key of the corresponding invoice in the [`invoices`](#invoices) table to detect new and updated records. This means that any time an invoice is updated, its associated line items will also be replicated.

  For example: An invoice with five line items is updated when its status changes from `draft` to `open`. The record in `invoices` will be replicated, as will the records for its five line items. In this example, a total of six records will be replicated.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve an invoice's line items"
    doc-link: "https://stripe.com/docs/api/invoices/invoice_lines"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice line item ID."
    foreign-key-id: "invoice-line-item-id"

  - name: "invoice"
    type: "string"
    primary-key: true
    description: "The ID of the invoice that contains this line item."
    foreign-key-id: "invoice-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "Time at which the **parent invoice** was created. Measured in seconds since the Unix epoch. Refer to table notes for additional details."  

  - name: "amount"
    type: "integer"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "discount_amounts"
    type: "array"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "discount"
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

  - name: "invoice_item"
    type: "string"
    description: "The invoice item(s) associated with this invoice line item."
    foreign-key-id: "invoice-item-id"

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "period"
    type: "object"
    description: ""
    subattributes:
    - name: "start"
      type: "string"
      description: ""

    - name: "end"
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

    - name: "updated"
      type: "string"
      description: ""


  - name: "price"
    type: "object"
    description: "The price of the line item."
    subattributes:
    - name: "id"
      type: "string"
      description: "Unique identifier for the object."

    - name: "object"
      type: "string"
      description: "String representing the object’s type. Objects of the same type share the same value."

    - name: "active"
      type: "boolean"
      description: "Whether the price can be used for new purchases."

    - name: "billing_scheme"
      type: "string"
      description: "Describes how to compute the price per period."

    - name: "created"
      type: "string"
      description: "Time at which the object was created."

    - name: "currency"
      type: "string"
      description: "Three-letter ISO currency code, in lowercase. Must be a supported currency."

    - name: "lookup_key"
      type: "string"
      description: "A lookup key used to retrieve prices dynamically from a static string."

    - name: "nickname"
      type: "string"
      description: "A brief description of the price, hidden from customers."

    - name: "product"
      type: "string"
      description: "The ID of the product this price is associated with."

    - name: "recurring"
      type: "object"
      description: "The recurring components of a price such as interval and usage_type."
      subattributes:
      - name: "aggregate_usage"
        type: "string"
        description: "Specifies a usage aggregation strategy for prices of usage_type=metered"

      - name: "interval"
        type: "string"
        description: "The frequency at which a subscription is billed. One of day, week, month or year."

      - name: "interval_count"
        type: "integer"
        description: "The number of intervals (specified in the interval attribute) between subscription billings."

      - name: "usage_type"
        type: "string"
        description: "Configures how the quantity per period should be determined. Can be either metered or licensed"


    - name: "tax_behavior"
      type: "string"
      description: "Specifies whether the price is considered inclusive of taxes or exclusive of taxes"

    - name: "tiers"
      type: "array"
      description: "Each element represents a pricing tier"
      subattributes:
      - name: "flat_amount"
        type: "integer"
        description: "Price for the entire tier."

      - name: "flat_amount_decimal"
        type: "string"
        description: "singer.decimal Same as flat_amount, but contains a decimal value with at most 12 decimal places."

      - name: "unit_amount"
        type: "integer"
        description: "Per unit price for units relevant to the tier."

      - name: "unit_amount_decimal"
        type: "string"
        description: "Same as unit_amount, but contains a decimal value with at most 12 decimal places."

      - name: "up_to"
        type: "integer"
        description: "Up to and including to this quantity will be contained in the tier."


    - name: "tiers_mode"
      type: "string"
      description: "Defines if the tiering price should be graduated or volume based."

    - name: "transform_quantity"
      type: "object"
      description: "Apply a transformation to the reported usage or set quantity before computing the amount billed"
      subattributes:
      - name: "divide_by"
        type: "integer"
        description: "Divide usage by this number."

      - name: "round"
        type: "string"
        description: "After division, either round the result up or down."


    - name: "type"
      type: "string"
      description: "One of one_time or recurring depending on whether the price is for a one-time purchase or a recurring (subscription) purchase."

    - name: "unit_amount"
      type: "integer"
      description: "The unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit."

    - name: "unit_amount_decimal"
      type: "string"
      description: "The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if billing_scheme=per_unit."

    - name: "livemode"
      type: "boolean"
      description: "The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places. Only set if billing_scheme=per_unit."

    - name: "metadata"
      type: "object"
      description: "Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format."


  - name: "proration"
    type: "boolean"
    description: ""

  - name: "proration_details"
    type: "object"
    description: "For a credit proration line_item, the original debit line_items to which the credit proration applies."

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "subscription"
    type: "string"
    description: "The ID of the subscription associated with the invoice line item."
    foreign-key-id: "subscription-id"

  - name: "subscription_item"
    type: "string"
    description: "The subscription item associated with the invoice line item."
    foreign-key-id: "subscription-item-id"

  - name: "tax_amounts"
    type: "array"
    description: ""
    subattributes:
    - name: "amount"
      type: "integer"
      description: ""

    - name: "inclusive"
      type: "boolean"
      description: ""

    - name: "tax_rate"
      type: "string"
      description: ""


  - name: "tax_rates"
    type: "array"
    description: "The tax rates which apply to the line item."
    subattributes:
    - name: "id"
      type: "string"
      description: "Unique identifier for the object."

    - name: "object"
      type: "string"
      description: "String representing the object’s type. Objects of the same type share the same value."

    - name: "active"
      type: "boolean"
      description: "Defaults to true. When set to false, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set."

    - name: "country"
      type: "string"
      description: "Two-letter country code"

    - name: "created"
      type: "string"
      description: "Time at which the object was created."

    - name: "description"
      type: "string"
      description: "An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers."

    - name: "display_name"
      type: "string"
      description: "The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page."

    - name: "inclusive"
      type: "boolean"
      description: "This specifies if the tax rate is inclusive or exclusive."

    - name: "jurisdiction"
      type: "string"
      description: "The jurisdiction for the tax rate."

    - name: "livemode"
      type: "boolean"
      description: "Has the value true if the object exists in live mode or the value false if the object exists in test mode."

    - name: "percentage"
      type: "string"
      description: "This represents the tax rate percent out of 100."

    - name: "state"
      type: "string"
      description: "ISO 3166-2 subdivision code, without country prefix."

    - name: "tax_type"
      type: "boolean"
      description: "The high-level tax type, such as vat or sales_tax."

    - name: "metadata"
      type: "object"
      description: "Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format."


  - name: "type"
    type: "string"
    description: ""
---