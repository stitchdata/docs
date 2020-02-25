---
tap: "recharge"
version: "1"
key: ""

name: "discounts"
doc-link: "https://developer.rechargepayments.com/#list-discounts"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/discounts.json"
description: |
  The `{{ table.name }}` table contains info about discounts.

replication-method: "Key-based Incremental"
api-method:
  name: "List discounts"
  doc-link: "https://developer.rechargepayments.com/#list-discounts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The discount ID."
    foreign-key-id: "discount-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the discount was created."

  - name: "applies_to_id"
    type: "integer"
    description: "The ID of the product or collection associated with the discount."

  - name: "applies_to_product_type"
    type: "string"
    description: |
      The type of product the discount applies to. Possible values are:

      - `ALL`
      - `ONETIME`
      - `SUBSCRIPTION`

  - name: "applies_to_resource"
    type: "string"
    description: |
      The type of resource the discount applies to. Possible values are:

      - `shopify_product`
      - `shopify_collection_id`

  - name: "code"
    type: "string"
    description: "The name of the discount."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the discount was created."

  - name: "duration"
    type: "string"
    description: |
      The number of times a discount will be automatically re-applied to a new queued charge after its first use on a successful charge. Possible values are:

      - `forever`: The discount will re-apply unlimited times
      - `usage_limit`: The discount will re-apply based on the `duration_usage_limit` value
      - `simple_use`: The discount will not re-apply

  - name: "duration_usage_limit"
    type: "integer"
    description: "**Applicable only when `duration: usage_limit`.** The number of times a discount will be automatically re-applied to a new queued charge after its first use on a successful charge."

  - name: "ends_at"
    type: "date-time"
    description: "The date when the discount expires."

  - name: "once_per_customer"
    type: "boolean"
    description: "If `true`, the discount can only be used for a given customer checkout or manually applied once on the customer portal. Once applied, it will continue to be reapplied to each new charge on the address unless the `discount_duration` specifies otherwise."

  - name: "starts_at"
    type: "date-time"
    description: "The date when the discount begins."

  - name: "status"
    type: "string"
    description: |
      The status of the discount. Possible values are:

      - `enabled`
      - `disabled`
      - `fully_disabled`

  - name: "times_used"
    type: "integer"
    description: "The number of times the discount was used by customers at checkout."

  - name: "usage_limit"
    type: "integer"
    description: "The maximum number of times the discount can be used by all customers."

  - name: "value"
    type: "integer"
    description: "The discounted value to be applied."
---