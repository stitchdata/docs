---
tap: "recurly"
version: "1.0"

name: "coupons"
key: "coupon"

doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recurly/blob/master/tap_recurly/schemas/coupons.json"
description: |
  The `{{ table.name }}` table contains info about the coupons available in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "List a site's coupons"
    doc-link: "https://partner-docs.recurly.com/v2018-08-09#operation/list_coupons"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The coupon ID."
    foreign-key-id: "coupon-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time when the coupon was last updated."

  - name: "applies_to_all_plans"
    type: "boolean"
    description: "Indicates if the coupon is valid for all plans."

  - name: "applies_to_non_plan_charges"
    type: "boolean"
    description: "Indicates if the coupon is valid for one-time, non-plan charges."

  - name: "code"
    type: "string"
    description: "The code the customer enters to redeem the coupon."

  - name: "coupon_type"
    type: "string"
    description: |
      The type of the coupon. Possible values are:

      - `single_code`
      - `bulk`

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the coupon was created."

  - name: "discount"
    type: "object"
    description: "Details of the discount a coupon applies."
    subattributes:
      - name: "currencies"
        type: "array"
        description: "**Applicable only when `type: fixed`.** The currencies associated with the coupon discount."
        subattributes:
          - name: "amount"
            type: "number"
            description: "The value of the fixed discount that the coupon applies."

          - name: "currency"
            type: "string"
            description: "The three-letter ISO 4217 currency code."

      - name: "percent"
        type: "integer"
        description: "**Applicable only when `type: percent`.** The percent of the total that is used to calculate the discount."

      - name: "trial"
        type: "object"
        description: "**Applicable only when `type: free_trial`**. Details about the discount for free trials."
        subattributes:
          - name: "length"
            type: "integer"
            description: "The trial length measured in units, specified by `unit`."

          - name: "unit"
            type: "string"
            description: |
              The temporal unit of the free trial. Possible values are:

              - `day`
              - `week`
              - `month`

      - name: "type"
        type: "string"
        description: |
          The type of discount the coupon applies. Possible values are:

          - `percent`
          - `fixed`
          - `free_trial`

  - name: "duration"
    type: "string"
    description: |
      The duration that the coupon will be applied to invoices for. Possible values are:

      - `forever`
      - `single_use` - The coupon can be applied only to the first invoice.
      - `temporal` - The coupon can be applied to invoices for the duration determined by the `temporal_unit` and `temporal_amount` attributes.

  - name: "expired_at"
    type: "date-time"
    description: "The date and time the coupon was expired early or reached its `max_redemptions`."

  - name: "free_trial_amount"
    type: "integer"
    description: "The duration of time the `free_trial_unit` is for."

  - name: "free_trial_unit"
    type: "string"
    description: |
      The description of the unit of time the coupon is for. Used with the `free_trial_amount` attribute to determine the duration of time the coupon is for. Possible values are:

      - `day`
      - `week`
      - `month`

  - name: "hosted_page_description"
    type: "string"
    description: "This description will show up when a customer redeems a coupon on your Hosted Payment Pages, or if you choose to show the description on your own checkout page."

  - name: "invoice_description"
    type: "string"
    description: "The description of the coupon as it will appear on invoices."

  - name: "max_redemptions"
    type: "integer"
    description: "The maximum number of redemptions for the coupon. The coupon will expire when the maximum redemption is hit."

  - name: "max_redemptions_per_account"
    type: "integer"
    description: "The number of times a specific account can redeem the coupon."

  - name: "name"
    type: "string"
    description: "The internal name for the coupon."

  - name: "object"
    type: "string"
    description: ""

  - name: "plans"
    type: "string"
    description: ""

  - name: "plans_names"
    type: "array"
    description: "A list of plan names that the coupon may be applied to."
    subattributes:
      - name: "value"
        type: "anything"
        description: "The plan name."

  - name: "redeem_by"
    type: "date-time"
    description: "the date and time the coupon will expire and can no longer be redeemed."

  - name: "redemption_resource"
    type: "string"
    description: |
      Indicates if the coupon is for all eligible charges on the account or only a specific subscription. Possible values are:

      - `account`
      - `subscription`

  - name: "state"
    type: "string"
    description: |
      The coupon's redemption status. Possible values are:

      - `redeemable`
      - `maxed_out`
      - `expired`

  - name: "temporal_amount"
    type: "integer"
    description: "**Applicable when `duration: temporal_amount`**. The duration that the coupon will be applied to invoices for, calculated as an integer multiplied by `temporal_unit`."

  - name: "temporal_unit"
    type: "string"
    description: |
      **Applicable when `duration: temporal_amount`**. The unit of time used to calculate the duration that the coupon will be applied to invoices for. Possible values are:

      - `day`
      - `week`
      - `month`
      - `year`

  - name: "unique_coupon_codes_count"
    type: "integer"
    description: "The total number of unique redemptions for the coupon."
---