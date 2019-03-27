---
tap: "stripe"
version: "1.0"

name: "plans"
doc-link: "https://stripe.com/docs/api/plans"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/plans.json"
description: |
  The `{{ table.name }}` table contains info about the plans in your {{ integration.display_name }} account. A plan defines the base price, currency, and billing cycle for subscriptions.

replication-method: "Key-based Incremental"

api-method:
    name: "List all plans"
    doc-link: "https://stripe.com/docs/api/plans/list"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The plan ID."
    foreign-key-id: "plan-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "Time at which the plan was created. Measured in seconds since the Unix epoch."

  - name: "active"
    type: "boolean"
    description: "Indicates whether the plan is currently availble for new subscriptions."

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

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}.

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
    description: ""
    anchor-id: 1
    subattributes:
      - name: "ANYTHING"
        type: "ANYTHING"
        description: "This info will vary."

  - name: "name"
    type: "string"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "nickname"
    type: "string"
    description: "A brief description of the plan, not visible to customers."

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `plan`."

  - name: "product"
    type: "string"
    description: "The product whose pricing this plan determines."

  - name: "statement_description"
    type: "string"
    description: "**Deprecated by {{ integration.display_name }}**."

  - name: "statement_descriptor"
    type: "string"
    description: "Extra information about a plan. This will appear on your customer’s credit card statement."

  - name: "tiers"
    type: "array"
    description: "The pricing tiers associated with the plan."
    subattributes:
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

  - name: "updated"
    type: "date-time"
    description: "The time the plan was last updated."

  - name: "usage_type"
    type: "string"
    description: |
      Indicates how the quantity per period should be determined. Possible values are:

      - `metered` - Aggregates total usage based on usage records.
      - `licensed` - Automtaically bills the `quantity` set for a plan when it's added to a subscription.
---