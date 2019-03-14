---
tap: "stripe"
version: "1.0"

name: "subscription_items"
doc-link: "https://stripe.com/docs/api/subscription_items"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/subscription_items.json"
description: |
  The `{{ table.name }}` table contains info about subscription items. In {{ integration.display_name }}, subscription items are used to create customer subscriptions with more than one plan.

replication-method: "Key-based Incremental"

api-method:
    name: "List subscription items"
    doc-link: "https://stripe.com/docs/api/subscription_items/list"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The subscription item ID."
    foreign-key-id: "subscription-item-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "The time at which the subscription item was created. Measured in seconds since the Unix epoch."

  - name: "application_fee_percent"
    type: "number"
    doc-link: "https://stripe.com/docs/connect/subscriptions#creating-subscriptions"
    description: "The percentage {{ integration.display_name }} should take off the final invoice amount each billing period."

  - name: "cancel_at_period_end"
    type: "boolean"
    description: "Indicates if the subscription item is canceled at period end."

  - name: "canceled_at"
    type: "date-time"
    description: "The date the subscription was canceled."

  - name: "current_period_end"
    type: "date-time"
    description: "The time the current usage period is set to end."

  - name: "current_period_start"
    type: "date-time"
    description: "The time the current usage period started."

  - name: "customer"
    type: "string"
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "discount"
    type: "object"
    description: "Describes the current discount active on the subscription item."
    subattributes:
      - name: "coupon"
        type: "object"
        description: "Details about the coupon applied to the subscription item."
        subattributes:
          - name: "id"
            type: "string"
            description: "The coupon ID."
            foreign-key-id: "coupon-id"

          - name: "amount_off"
            type: "integer"
            description: "The amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer."

          - name: "created"
            type: "date-time"
            description: "The time at which the coupon was created. Measured in seconds since the Unix epoch."

          - name: "currency"
            type: "string"
            description: |
              The three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html){:target="new"} of the amount to take off (`amount_off`).

          - name: "duration"
            type: "string"
            description: |
              Indicates how long a customer who applies this coupon will get the discount. Possible values are:

              - `forever`
              - `once`
              - `repeating`

          - name: "duration_in_months"
            type: "integer"
            description: "Indicates the number of months the coupon applies if `duration: repeating`."

          - name: "livemode"
            type: "boolean"
            description: "Indicates if the coupon exists in live mode (`true`) or in test mode (`false`)."

          - name: "max_redemptions"
            type: "integer"
            description: "The maximum number of times this coupon can be redeemed in total across all customers before it is no longer valid."

          - name: "metadata"
            type: "object"
            description: ""
            subattributes:
              - name: ""
                type: ""
                description: ""

          - name: "name"
            type: "string"
            description: "The name of the coupon as it is displayed to customers."

          - name: "object"
            type: "string"
            description: "The type of {{ integration.display_name }} object. This will be `coupon`."

          - name: "percent_off"
            type: "integer"
            description: "The percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon."

          - name: "percent_off_precise"
            type: "number"
            description: ""

          - name: "redeem_by"
            type: "date-time"
            description: "The date afer which the coupon can no longer be redeemed."

          - name: "times_redeemed"
            type: "integer"
            description: "The number of times this coupon has been applied to a customer."

          - name: "valid"
            type: "boolean"
            description: "Taking into account all of the other coupon properties, indicates whether this coupon can still be applied to a customer."

  - name: "ended_at"
    type: "date-time"
    description: "If the subscription has ended, the date the subscription ended."

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `subscription_item`."

  - name: "plan"
    type: "object"
    description: "Details about the plan the customer subscribed to."
    subattributes:
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
        subattributes:
          - name: ""
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

      - name: "usage_type"
        type: "string"
        description: |
          Indicates how the quantity per period should be determined. Possible values are:

          - `metered` - Aggregates total usage based on usage records.
          - `licensed` - Automtaically bills the `quantity` set for a plan when it's added to a subscription.

  - name: "quantity"
    type: "integer"
    description: "The quantity of the plan to which the subscription should be subscribed."

  - name: "start"
    type: "date-time"
    description: "The date the most recent update to this subscription started."

  - name: "status"
    type: "string"
    description: |
      The status of the subscription. Possible values are:

      - `trialing` - The subscription is still in its trial period
      - `active` - The subscription is active and no longer in its trial period
      - `past_due` - The subscription is past due, either because payment to renew has failed or the subscription's invoice's due date has passed.
      - `canceled` - The subscription has been canceled. This status may also occur when:
         - A subscription is `past_due` and {{ integration.display_name }} has exhausted all payment retry attempts
         - A subscription is `past_due` and an invoice is sent and not paid by its due date, or an additional deadline after the original due date.
      - `unpaid` - The subscription is unpaid.

  - name: "subscription"
    type: "string"
    description: "The ID of the subscription the subscription item belongs to."
    foreign-key-id: "subscription-id"

  - name: "tax_percent"
    type: "number"
    description: "The tax rate applied to each invoice created by this subscription."

  - name: "trial_end"
    type: "date-time"
    description: "The time the trial associated with the subscription item ends."

  - name: "trial_start"
    type: "date-time"
    description: "The time the trial associated with the subscription item started."
---