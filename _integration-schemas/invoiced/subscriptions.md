---
tap: "invoiced"
version: "1"

name: "subscriptions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/subscriptions.json"
description: |
  The `{{ table.name }}` table contains info about the subscriptions in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all subscriptions"
    doc-link: "https://invoiced.com/docs/api/#list-all-subscriptions"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The subscription ID."
    foreign-key-id: "subscription-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the subscription was last updated."

  - name: "addons"
    type: "array"
    description: "Details about subscription's add ons."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The subscription ID."

      - name: "object"
        type: "string"
        description: "This will be `subscription_addon`."

      - name: "plan"
        type: "integer"
        description: "The ID of the plan associated with the subscription."
        foreign-key-id: "plan-id"

      - name: "quantity"
        type: "integer"
        description: "The quantity of the subscription add on."

      - name: "description"
        type: "string"
        description: "The description of the add on."

      - name: "created_at"
        type: "date-time"
        description: "The time when the add on was created."

  # - name: "approval"
  #   type: "object"
  #   description: ""

  - name: "cancel_at_period_end"
    type: "boolean"
    description: "If `true`, the subscription will be canceled at the end of the current billing period."

  - name: "canceled_at"
    type: "date-time"
    description: "The time when the subscription was canceled."

  - name: "contract_period_end"
    type: "date-time"
    description: ""

  - name: "contract_period_start"
    type: "date-time"
    description: ""

  - name: "contract_renewal_cycles"
    type: "integer"
    description: ""

  - name: "contract_renewal_mode"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: "The time when the subscription was created."

  - name: "customer"
    type: "integer"
    description: "The ID of the customer associated with the subscription."
    foreign-key-id: "customer-id"

  - name: "cycles"
    type: "integer"
    description: "The number of billing cycles the subscription runs for. When `null`, the subscription will run until canceled."

  - name: "discounts"
    type: "array"
    description: "The discounts applicable to the subscription."
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

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "mrr"
    type: "number"
    description: "The amount the subscription contributes to monthly recurring revenue."

  - name: "period_end"
    type: "date-time"
    description: "The start of the current billing period."

  - name: "period_start"
    type: "date-time"
    description: "The end of the current billing period."

  - name: "plan"
    type: "string"
    description: "The ID of the plan associated with the subscription."
    foreign-key-id: "plan-id"

  - name: "quantity"
    type: "number"
    description: "The plan quantity."

  - name: "recurring_total"
    type: "number"
    description: "The total recurring amount, including taxes."

  - name: "renewed_last"
    type: "date-time"
    description: "The date the subscription was last renewed."

  - name: "renews_next"
    type: "date-time"
    description: "The date the subscription renews next."

  - name: "start_date"
    type: "date-time"
    description: "The time the subscription starts, or started."

  - name: "status"
    type: "string"
    description: |
      The status of the subscription. Possible values are:

      - `not_started`
      - `active`
      - `past_due`
      - `finished`
      - `canceled`

  - name: "taxes"
    type: "array"
    description: "The taxes applicable to the subscription."
    subattributes:
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
---