---
tap: "stripe"
version: "1"

name: "coupons"
doc-link: "https://stripe.com/docs/api/coupons"
singer-schema: "https://github.com/singer-io/tap-stripe/blob/master/tap_stripe/schemas/coupons.json"
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
    type: "date-time"
    replication-key: true
    description: "Time at which the object was created. Measured in seconds since the Unix epoch."

  - name: "amount_off"
    type: "integer"
    description: "The amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer."

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
    description: |
      Indicates the number of months the coupon applies if `duration: repeating`.

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
      - name: "ANYTHING"
        type: "ANYTHING"
        description: "This info will vary."
 
  - name: "name"
    type: "string"
    description: "The name of the coupon as it is displayed to customers."

  - name: "object"
    type: "string"
    description: "The type of {{ integration.display_name }} object. This will be `coupon`."

  - name: "percent_off"
    type: "number"
    description: "The percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon."

  - name: "percent_off_precise"
    type: "number"
    description: ""

  - name: "redeem_by"
    type: "date-time"
    description: "The date after which the coupon can no longer be redeemed."

  - name: "times_redeemed"
    type: "integer"
    description: "The number of times this coupon has been applied to a customer."

  - name: "updated"
    type: "date-time"
    description: "The time at which the coupon was last updated."

  - name: "valid"
    type: "boolean"
    description: "Taking into account all of the other coupon properties, indicates whether this coupon can still be applied to a customer."
---