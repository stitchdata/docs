---
tap: "recharge"
version: "2"
key: ""

name: "customers"
doc-link: https://developer.rechargepayments.com/2021-11/customers/customers_list
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/customers.json
description: |
  The `{{ table.name }}` table contains info about customer accounts with a shop.

replication-method: "INCREMENTAL"

api-method:
  name: "List customers"
  doc-link: "https://developer.rechargepayments.com/2021-11/customers/customers_list"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time when the customer was last updated."

  - name: "analytics_data"
    type: "object"
    description: ""
    subattributes:
      - name: "utm_params"
        type: "array"
        description: ""
        subattributes:
          - name: "utm_campaign"
            type: "string"
            description: ""

          - name: "utm_content"
            type: "string"
            description: ""

          - name: "utm_data_source"
            type: "string"
            description: ""

          - name: "utm_source"
            type: "string"
            description: ""

          - name: "utm_medium"
            type: "string"
            description: ""

          - name: "utm_term"
            type: "string"
            description: ""

          - name: "utm_timestamp"
            type: "string"
            description: ""



  - name: "billing_address1"
    type: "string"
    description: ""

  - name: "billing_address2"
    type: "string"
    description: ""

  - name: "billing_city"
    type: "string"
    description: ""

  - name: "billing_company"
    type: "string"
    description: ""

  - name: "billing_country"
    type: "string"
    description: ""

  - name: "billing_phone"
    type: "string"
    description: ""

  - name: "billing_province"
    type: "string"
    description: ""

  - name: "billing_zip"
    type: "string"
    description: ""

  - name: "braintree_customer_token"
    type: "string"
    description: ""

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "external_customer_id"
    type: "object"
    description: ""
    subattributes:
      - name: "ecommerce"
        type: "string"
        description: ""


  - name: "first_charge_processed_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "has_card_error_in_dunning"
    type: "boolean"
    description: ""

  - name: "has_payment_method_in_dunning"
    type: "boolean"
    description: ""

  - name: "has_valid_payment_method"
    type: "boolean"
    description: ""

  - name: "hash"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "number_active_subscriptions"
    type: "integer"
    description: ""

  - name: "number_subscriptions"
    type: "integer"
    description: ""

  - name: "paypal_customer_token"
    type: "string"
    description: ""

  - name: "processor_type"
    type: "string"
    description: ""

  - name: "reason_payment_method_not_valid"
    type: "string"
    description: ""

  - name: "shopify_customer_id"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "subscriptions_active_count"
    type: "integer"
    description: ""

  - name: "subscriptions_total_count"
    type: "integer"
    description: ""
---