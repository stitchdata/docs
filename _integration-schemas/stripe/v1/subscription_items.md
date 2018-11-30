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
    description: ""

  - name: "cancel_at_period_end"
    type: "boolean"
    description: "Indicates if the subscription item is canceled at period end."

  - name: "canceled_at"
    type: "date-time"
    description: ""

  - name: "current_period_end"
    type: "date-time"
    description: "The time the current usage period is set to end."

  - name: "current_period_start"
    type: "date-time"
    description: "The time the current usage period started."

  - name: "customer"
    type: "string"
    description: ""
    foreign-key-id: "customer-id"

  - name: "discount"
    type: "object"
    description: ""
    object-attributes:

  - name: "ended_at"
    type: "date-time"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: "Indicates if the object exists in live mode (`true`) or in test mode (`false`)."

  - name: "metadata"
    type: "object"
    description: ""
    object-attributes:

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `subscription_item`."

  - name: "plan"
    type: "object"
    description: "Details about the plan the customer is subscribed to."
    object-attributes:
      - name: "TBD"
        type: "TBD"
        description: ""

  - name: "quantity"
    type: "integer"
    description: "The quantity of the plan to which the subscription should be subscribed."

  - name: "start"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subscription"
    type: "string"
    description: "The ID of the subscription the subscription item belongs to."
    foreign-key-id: "subscription-id"

  - name: "tax_percent"
    type: "number"
    description: ""

  - name: "trial_end"
    type: "date-time"
    description: "The time the trial associated with the subscription item ends."

  - name: "trial_start"
    type: "date-time"
    description: "The time the trial associated with the subscription item started."
---
