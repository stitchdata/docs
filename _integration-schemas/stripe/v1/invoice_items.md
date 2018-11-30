---
tap: "stripe"
version: "1.0"

name: "invoice_items"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/invoice_items.json"
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
    type: "date-time"
    replication-key: true
    description: "The date the invoice item was added to the invoice."

  - name: "amount"
    type: "integer"
    description: "The amount (in the `currency` specified_ of the invoice item. This is equal to `unit_amount * quantity`."

  - name: "currency"
    type: "string"
    description: |
      The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}, in lowercase.

  - name: "customer"
    type: "string"
    description: "The ID of the customer who will be billed for the invoice item."
    foreign-key-id: "customer-id"

  - name: "description"
    type: "string"
    description: "A description of the invoice item."

  - name: "discountable"
    type: "boolean"
    description: "Indicates if discounts will apply to the invoice item (`true`). This will always be `false` for prorations."

  - name: "invoice"
    type: "string"
    description: "The ID of the invoice associated with the invoice item."
    foreign-key-id: "invoice-id"

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: "Additional information attached to the invoice item."
    object-attributes:
      - name: "TODO"
        type: 
        description: ""

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `invoiceitem`."

  - name: "period"
    type: "object"
    description: "The start and end dates of the period associated with the invoice item."
    object-attributes:
      - name: "end"
        type: "date-time"
        description: "The time the period ends."

      - name: "start"
        type: "date-time"
        description: "The time the period starts."

  - name: "plan"
    type: "object"
    description: "If the invoice item is a proration, this will contain details about the plan of the subscription the proration was computed for."
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
        description: |
          The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"}, in lowercase.

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
    description: "Indicates whether the invoice item was created automatically as a proration adjustment when the customer switched plans."

  - name: "quantity"
    type: "integer"
    description: |
      The quantity of units for the invoice item.

      If the invoice item is a proration, the quantity of the subscription that the proration was computed for.

  - name: "subscription"
    type: "string"
    description: "The subscription that this invoice item was created for."
    foreign-key-id: "subscription-id"

  - name: "subscription_item"
    type: "string"
    description: "The subscription item associated with the invoice item."
    foreign-key-id: "subscription-item-id"

  - name: "unit_amount"
    type: "integer"
    description: "The unity amount (in the `currency` specified) of the invoice item."

  - name: "updated"
    type: "date-time"
    description: "Time at which the object was last updated."
---