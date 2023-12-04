---
tap: "chargebee"
version: "20-05-2019"
key: "plan"

name: "plans"
doc-link: "https://apidocs.chargebee.com/docs/api/plans"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/plans.json"
description: |
  The `{{ table.name }}` table contains info about the plans in your {{ integration.display_name }} account. Plans are used to specify prices and billing frequencies for [`subscriptions`](#subscriptions).

replication-method: "Key-based Incremental"

api-method:
    name: "List plans"
    doc-link: "https://apidocs.chargebee.com/docs/api/plans#list_plans"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The plan ID."
    foreign-key-id: "plan-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the plan was last updated."

  - name: "billing_cycles"
    type: "integer"
    description: "The number of billing cycles the subscription is active."

  - name: "charge_model"
    type: "string"
    description: |
      Defines how the recurring charges for the subscription are calculated. Possible values are:

      - `flat_fee`
      - `per_unit`
      - `tiered`
      - `volume`
      - `stairstep`

  - name: "description"
    type: "string"
    description: "The description of the plan to show in hosted pages and the customer portal."

  - name: "free_quantity"
    type: "integer"
    description: "The free quantity the subscriptions of the plan will have. Only quantities more than this value will be charged for the subscription."

  - name: "invoice_notes"
    type: "string"
    description: "Invoice notes associated with the subscription."

  - name: "name"
    type: "string"
    description: "The display name of the plan."

  - name: "period"
    type: "integer"
    description: |
      Defines the billing frequency for the plan. Used with `period_unit` to create a billing schedule for the plan.

      For example: If `period_unit: week` and `period: 3`, billing would occur every `3 weeks`.

  - name: "period_unit"
    type: "string"
    description: |
      The time unit for the billing period. Used with `period` to create a billing schedule for the plan.

      For example: If `period_unit: week` and `period: 3`, billing would occur every `3 weeks`.

      Possible values are:

      - `day`
      - `week`
      - `month`
      - `year`

  - name: "price"
    type: "integer"
    description: "The price of the plan."

  - name: "redirect_url"
    type: "string"
    description: "The URL to redirect on successful checkout."

  - name: "setup_cost"
    type: "integer"
    description: "The one-time setup fee charged as part of the first invoice for the plan."

  - name: "sku"
    type: "string"
    description: "Ssed as Product name/code in your third party accounting application. {{ integration.display_name }} will use it as an alternate name in your accounting application."

  - name: "status"
    type: "string"
    description: |
      The plan state. Possible values are:

      - `active`
      - `archived`

  - name: "tax_profile_id"
    type: "string"
    description: "The ID of the tax profile for the plan."

  - name: "taxable"
    type: "boolean"
    description: "Indicates if the plan is taxable or not."

  - name: "trial_period"
    type: "integer"
    description: |
      The free time window for the customer to try the product. Used with `trial_period_unit` to create the free trial period.

      For example: If `trial_period: day` and `trial_period_unit: 14`, the trial period would be `14 days`.

  - name: "trial_period_unit"
    type: "string"
    description: |
      The time unit for the trial period. Used with `trial_period` to create the free trial period.

      For example: If `trial_period: day` and `trial_period_unit: 14`, the trial period would be `14 days`.

      Possible values are:

      - `day`
      - `month`
---