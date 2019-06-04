---
tap: "chargebee"
version: "1.0"
key: "coupon"

name: "coupons"
doc-link: "https://apidocs.chargebee.com/docs/api/coupons"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/coupons.json"
description: |
  The `{{ table.name }}` table contains info about the coupons in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List coupons"
    doc-link: "https://apidocs.chargebee.com/docs/api/coupons#list_coupons"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The coupon ID."
    foreign-key-id: "coupon-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the coupon was last updated."

  - name: "addon_constraint"
    type: "string"
    description: |
      The addons the coupon can be applied to. Possible values are:

      - `none`
      - `all`
      - `specific`
      - `not_applicable`

  - name: "apply_discount_on"
    type: "string"
    description: ""

  - name: "apply_on"
    type: "string"
    description: |
      The invoice items for which this coupon needs to be applied. Possible values are:

      - `invoice_amount`: The coupon will be applied to the total invoice amount.
      - `each_specified_item`: the discount will be applied to each specified plan and addon item.

  - name: "archived_at"
    type: "date-time"
    description: "The time when the coupon was archived."

  - name: "created_at"
    type: "date-time"
    description: "The time when the coupon was created."

  - name: "discount_amount"
    type: "number"
    description: "When `discount_type: fixed_amount`, this value will be the discount value in cents."

  - name: "discount_percentage"
    type: "number"
    description: "When `discount_type: percentage`, this value will be the discount value percentage."

  - name: "discount_type"
    type: "string"
    description: |
      The type of discount. Possible values are:

      - `fixed_amount`
      - `percentage`

  - name: "duration_month"
    type: "integer"
    description: |
      When `duration_type: limited_period`, this value will be the duration in months the coupon can be applied.

  - name: "duration_type"
    type: "string"
    description: |
      The duration the coupon is applicable. Possible values are:

      - `one_time`
      - `forever`
      - `limited_period`

  - name: "max_redemptions"
    type: "integer"
    description: "The maximum number of times the coupon can be redeemed."

  - name: "name"
    type: "string"
    description: "The display name used in web interface for identifying the coupon."

  - name: "object"
    type: "string"
    description: ""

  - name: "plan_constraint"
    type: "string"
    description: |
      The plans the coupon can be applied to. Possible values are:

      - `none`
      - `all`
      - `specific`
      - `not_applicable`

  - name: "redemptions"
    type: "integer"
    description: "The number of times the coupon has been redeemed."

  - name: "resource_version"
    type: "integer"
    description: "The version number of the coupon. Each update of the coupon results in an incremental change of this value. **Note**: This attribute will be present only if the coupon has been updated after 2016-09-28."

  - name: "status"
    type: "string"
    description: |
      The status of the coupon. Possible values are:

      - `active`
      - `expired`
      - `archived`
      - `deleted`
---