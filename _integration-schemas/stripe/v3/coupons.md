---
tap: "stripe"
version: "3"
key: ""

name: "coupons"
doc-link: "https://stripe.com/docs/api/coupons"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/coupons.json
description: |
  The `{{ table.name }}` table contains info about percent or amount-off discounts that may be applied to a customer. **Note:** Coupons only apply to invoices; they don't apply to one-off charges.

replication-method: "Key-based Incremental"

api-method:
    name: "List all coupons"
    doc-link: "https://stripe.com/docs/api/coupons/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The coupon ID."
    foreign-key-id: "coupon-id"

  - name: "created"
    type: "string"
    replication-key: true
    description: "Time at which the object was created. Measured in seconds since the Unix epoch."  

  - name: "amount_off"
    type: "integer"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "duration"
    type: "string"
    description: ""

  - name: "duration_in_months"
    type: "integer"
    description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "max_redemptions"
    type: "integer"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""
    subattributes:

  - name: "name"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "percent_off"
    type: "number"
    description: ""

  - name: "percent_off_precise"
    type: "number"
    description: ""

  - name: "redeem_by"
    type: "string"
    description: ""

  - name: "times_redeemed"
    type: "integer"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"

  - name: "valid"
    type: "boolean"
    description: ""
---