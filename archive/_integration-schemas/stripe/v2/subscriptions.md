---
tap: "stripe"
version: "2"
key: ""

name: "subscriptions"
doc-link: "https://stripe.com/docs/api/subscriptions"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/subscriptions.json
description: |
  The `{{ table.name }}` table contains info about subscriptions, which allow you to charge a customer on a recurring basis. A subscription ties a customer to a particular [plan](#plans).

replication-method: "Key-based Incremental"

api-method:
    name: "List subscriptions"
    doc-link: "https://stripe.com/docs/api/subscriptions/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The subscription ID."
    foreign-key-id: "subscription-id"

  - name: "created"
    type: "string"
    replication-key: true
    description: "The time the subscription was created. Measured in second since the Unix epoch."

  - name: "application_fee_percent"
    type: "number"
    description: ""

  - name: "billing"
    type: "string"
    description: ""

  - name: "billing_cycle_anchor"
    type: "string"
    description: ""

  - name: "billing_thresholds"
    type: "object"
    description: ""
    subattributes:
    - name: "amount_gte"
      type: "integer"
      description: ""

    - name: "reset_billing_cycle_anchor"
      type: "boolean"
      description: ""


  - name: "cancel_at"
    type: "string"
    description: ""

  - name: "cancel_at_period_end"
    type: "boolean"
    description: ""

  - name: "canceled_at"
    type: "string"
    description: ""

  - name: "collection_method"
    type: "string"
    description: ""

  - name: "current_period_end"
    type: "string"
    description: ""

  - name: "current_period_start"
    type: "string"
    description: ""

  - name: "customer"
    type: "string"
    description: "The ID of the customer who owns the subscription."
    foreign-key-id: "customer-id"

  - name: "days_until_due"
    type: "integer"
    description: ""

  - name: "default_payment_method"
    type: "string"
    description: ""

  - name: "default_source"
    type: "string"
    description: ""

  - name: "discount"
    type: "object"
    description: ""
    subattributes:
    - name: "end"
      type: "string"
      description: ""

    - name: "coupon"
      type: "object"
      description: ""
      subattributes:
      - name: "metadata"
        type: "object"
        description: ""

      - name: "valid"
        type: "boolean"
        description: ""

      - name: "livemode"
        type: "boolean"
        description: ""

      - name: "amount_off"
        type: "integer"
        description: ""

      - name: "redeem_by"
        type: "string"
        description: ""

      - name: "duration_in_months"
        type: "integer"
        description: ""

      - name: "percent_off_precise"
        type: "number"
        description: ""

      - name: "max_redemptions"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "times_redeemed"
        type: "integer"
        description: ""

      - name: "id"
        type: "string"
        description: "The coupon ID."
        foreign-key-id: "coupon-id"

      - name: "duration"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

      - name: "percent_off"
        type: "number"
        description: ""

      - name: "created"
        type: "string"
        description: ""


    - name: "customer"
      type: "string"
      description: ""

    - name: "start"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""

    - name: "subscription"
      type: "string"
      description: ""

    - name: "checkout_session"
      type: "string"
      description: "The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode."

    - name: "id"
      type: "string"
      description: "The ID of the discount object. "

    - name: "invoice"
      type: "string"
      description: "The invoice that the discount’s coupon was applied to, if it was applied directly to a particular invoice."

    - name: "invoice_item"
      type: "string"
      description: "The invoice item id (or invoice line item id for invoice line items of type=‘subscription’) that the discount’s coupon was applied to, if it was applied directly to a particular invoice item or invoice line item."

    - name: "promotion_code"
      type: "string"
      description: "The promotion code applied to create this discount."


  - name: "ended_at"
    type: "string"
    description: ""

  - name: "invoice_customer_balance_settings"
    type: "object"
    description: ""
    subattributes:
    - name: "consume_applied_balance_on_void"
      type: "boolean"
      description: ""


  - name: "items"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "latest_invoice"
    type: "string"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

  - name: "next_pending_invoice_item_invoice"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "pause_collection"
    type: "object"
    description: ""
    subattributes:
    - name: "behavior"
      type: "string"
      description: ""

    - name: "resumes_at"
      type: "string"
      description: ""


  - name: "pending_invoice_item_interval"
    type: "object"
    description: ""
    subattributes:
    - name: "interval"
      type: "string"
      description: ""

    - name: "interval_count"
      type: "integer"
      description: ""


  - name: "pending_setup_intent"
    type: "string"
    description: ""

  - name: "plan"
    type: "object"
    description: ""
    subattributes:
    - name: "metadata"
      type: "object"
      description: ""

    - name: "product"
      type: "string"
      description: "The product whose pricing this plan determines."
      foreign-key-id: "product-id"

    - name: "statement_description"
      type: "string"
      description: ""

    - name: "currency"
      type: "string"
      description: ""

    - name: "livemode"
      type: "boolean"
      description: ""

    - name: "tiers_mode"
      type: "string"
      description: ""

    - name: "active"
      type: "boolean"
      description: ""

    - name: "id"
      type: "string"
      description: "The plan ID."
      foreign-key-id: "plan-id"

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


    - name: "created"
      type: "string"
      description: ""

    - name: "nickname"
      type: "string"
      description: ""

    - name: "transform_usage"
      type: "object"
      description: ""

    - name: "interval_count"
      type: "integer"
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

    - name: "aggregate_usage"
      type: "string"
      description: ""

    - name: "trial_period_days"
      type: "integer"
      description: ""

    - name: "billing_scheme"
      type: "string"
      description: ""

    - name: "statement_descriptor"
      type: "string"
      description: ""

    - name: "usage_type"
      type: "string"
      description: ""

    - name: "object"
      type: "string"
      description: ""


  - name: "quantity"
    type: "integer"
    description: ""

  - name: "schedule"
    type: "string"
    description: ""

  - name: "start"
    type: "string"
    description: ""

  - name: "start_date"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tax_percent"
    type: "number"
    description: ""

  - name: "transfer_data"
    type: "object"
    description: ""
    subattributes:
    - name: "amount_percent"
      type: "string"
      description: ""

    - name: "destination"
      type: "string"
      description: ""


  - name: "trial_end"
    type: "string"
    description: ""

  - name: "trial_start"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"
---