---
tap: "stripe"
version: "1.0"

name: "invoice_line_items"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/invoice_line_items.json"
description: |
  The `{{ table.name }}` table contains info about the line items contained in invoices.

replication-method: ""

api-method:
    name: ""
    doc-link: ""
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The invoice line item ID."
    foreign-key-id: "invoice-line-item-id"

  - name: "amount"
    type: "integer"
    description: "The amount (in cents) of the charge to be applied to the upcoming invoice."

  - name: "currency"
    type: "string"
    description: |
       The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}.

  - name: "description"
    type: "string"
    description: "An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking."

  - name: "discountable"
    type: "boolean"
    description: "Indicates whether discounts can apply to this line item."

  - name: "invoice"
    type: "string"
    description: "The ID of the invoice that contains this line item."
    foreign-key-id: "invoice-id"

  - name: "invoice_item"
    type: "object"
    description: "The invoice item(s) associated with this invoice line item."
    object-attributes:

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: "Additional information attached to the invoice line item."
    object-attributes:
      - name: "TODO"
        type: 
        description: ""

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `charge`."

  - name: "period"
    type: "object"
    description: "The start and end dates of the period associated with the invoice line item."
    object-attributes:
      - name: "end"
        type: "date-time"
        description: "The time the period ended."

      - name: "start"
        type: "date-time"
        description: "The time the period started."

  - name: "plan"
    type: "object"
    description: "If the invoice line item is a proration, this will contain details about the plan of the subscription the proration was computed for."
    doc-link: "https://stripe.com/docs/api/plans/object"
    object-attributes:
      - name: "active"
        type: "boolean"
        description: "Indicates if the plan is currently available for new subscriptions."

      - name: "aggregate_usage"
        type: "string"
        description: |
          Indicates a usage aggregation strategy for plans of `usage_type: metered`. Possible values are:

          - `sum` - Sums up all usage during a period
          - `last_during_period` - Selects the last usage record reported within a period
          - `last_ever` - Selects the last usage record ever (across period bounds)
          - `max` - Selects the usage record with the maximum reported usage during a period

      - name: "amount"
        type: "integer"
        description: "The amount (in cents) to be charged on the interval specified."

      - name: "billing_scheme"
        type: "string"
        description: |
          Indicates how the price per period should be computed. Possible values are:

          - `per_unit` - Indicates that the fixed `amount` will be charged per unit (`quantity`) for plans with `usage_type: licensed`, or per unit of total usage for plans with `usage_type: metered`.
          - `tiered` - Indicates that unit pricing will be computed using a tiering strategy as defined using `tiers` and `tiers_mode`.

      - name: "created"
        type: "date-time"
        description: "Time at which the object was created. Measured in seconds since the Unix epoch."

      - name: "currency"
        type: "string"
        description: The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}, in lowercase.

      - name: "id"
        type: "string"
        description: "The plan ID."
        foreign-key-id: "plan-id"

      - name: "interval"
        type: "string"
        description: |
          The frequency with which a subscription should be billed. Possible values are `day`, `week`, `month`, or `year`.

      - name: "interval_count"
        type: "integer"
        description: |
          The number of intervals (specified by `interval`) between subscription billings.

          For example: `interval: month` and `interval_count: 3` would bill every three months.

      - name: "livemode"
        type: "boolean"
        description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

      - name: "metadata"
        type: "object"
        description: "Additional information attached to the plan."
        object-attributes:
          - name: "TODO"
            type: 
            description: ""

      - name: "nickname"
        type: "string"
        description: "A brief description of the plan, not visible to customers."

      - name: "object"
        type: "string"
        description: "The type of {{ integration.display_name }} object. This will be `plan`."

      - name: "product"
        type: "string"
        description: "The product whose pricing this plan determines."

      - name: "tiers"
        type: "array"
        description: "The pricing tiers associated with the plan."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The pricing tier."

      - name: "tiers_mode"
        type: "string"
        description: |
          Indicates if the pricing tier should be `graduated` or `volume`- based.

          - `volume` - The maximum quantity within a period determines the per unit price
          - `graduated` - Pricing can successively change as the quantity grows

      - name: "transform_usage"
        type: "string"
        description: "Applies a transformation to the reported usage or set quantity before computing the billed price."

      - name: "trial_period_days"
        type: "integer"
        description: "The default number of trial days when subscribing a customer to this plan."

      - name: "usage_type"
        type: "string"
        description: |
          Indicates how the quantity per period should be determined. Possible values are:

          - `metered` - Aggregates total usage based on usage records.
          - `licensed` - Automtaically bills the `quantity` set for a plan when it's added to a subscription.

  - name: "proration"
    type: "boolean"
    description: "Indicates if the invoice line item is a proration."

  - name: "quantity"
    type: "integer"
    description: "The quantity of units for the invoice line item."

  - name: "subscription"
    type: "string"
    description: "The ID of the subscription associated with the invoice line item."

  - name: "subscription_item"
    type: "string"
    description: "The subscription item associated with the invoice line item."
    foreign-key-id: "subscription-item-id"

  - name: "type"
    type: "string"
    description: "The type of the invoice line item."
---
