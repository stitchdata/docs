---
tap: "stripe"
version: "2"
key: ""

name: "plans"
doc-link: "https://stripe.com/docs/api/plans"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/plans.json
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
    type: "string"
    replication-key: true
    description: "Time at which the plan was created. Measured in seconds since the Unix epoch."
  
  - name: "active"
    type: "boolean"
    description: ""

  - name: "aggregate_usage"
    type: "string"
    description: ""

  - name: "amount"
    type: "integer"
    description: ""

  - name: "amount_decimal"
    type: "string"
    description: ""

  - name: "billing_scheme"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "interval"
    type: "string"
    description: ""

  - name: "interval_count"
    type: "integer"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nickname"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "product"
    type: "string"
    description: "The product whose pricing this plan determines."
    foreign-key-id: "product-id"

  - name: "statement_description"
    type: "string"
    description: ""

  - name: "statement_descriptor"
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


  - name: "tiers_mode"
    type: "string"
    description: ""

  - name: "transform_usage"
    type: "object"
    description: ""

  - name: "trial_period_days"
    type: "integer"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"

  - name: "usage_type"
    type: "string"
    description: ""
---