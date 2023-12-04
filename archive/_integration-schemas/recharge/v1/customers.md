---
tap: "recharge"
version: "1"
key: "customer"

name: "customers"
doc-link: "https://developer.rechargepayments.com/#list-customers"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about customer accounts with a shop.

replication-method: "Key-based Incremental"
api-method:
  name: "List customers"
  doc-link: "https://developer.rechargepayments.com/#list-customers"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time when the customer was last updated."

  - name: "billing_address1"
    type: "string"
    description: "The customer's billing address."

  - name: "billing_address2"
    type: "string"
    description: "Additional data about the customer's billing address."

  - name: "billing_city"
    type: "string"
    description: "The customer's billing city."

  - name: "billing_company"
    type: "string"
    description: "The customer's billing company."

  - name: "billing_country"
    type: "string"
    description: "The customer's billing country."

  - name: "billing_phone"
    type: "string"
    description: "The customer's billing phone."

  - name: "billing_province"
    type: "string"
    description: "The customer's billing state or province."

  - name: "billing_zip"
    type: "string"
    description: "The customer's billing zip code."

  - name: "braintree_customer_token"
    type: "string"
    description: "The customer's token in Braintree."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the customer was created."

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "first_charge_processed_at"
    type: "date-time"
    description: "The date when first charge was processed for customer."

  - name: "first_name"
    type: "string"
    description: "The customer's first name."

  - name: "has_card_error_in_dunning"
    type: "boolean"
    description: "If `true`, the customer has a card with an error in the dunning process."

  - name: "has_valid_payment_method"
    type: "boolean"
    description: "If `true`, the customer has a valid payment method."

  - name: "hash"
    type: "string"
    description: "The string identifier used in the customer's portal link."

  - name: "last_name"
    type: "string"
    description: "The customer's last name."

  - name: "number_active_subscriptions"
    type: "integer"
    description: "The number of active subscriptions associated with the customer."

  - name: "number_subscriptions"
    type: "integer"
    description: "The number of subscriptions for the customer."

  - name: "paypal_customer_token"
    type: "string"
    description: "The customer's token for PayPal."

  - name: "processor_type"
    type: "string"
    description: "The type of processor associated with the customer."

  - name: "reason_payment_method_not_valid"
    type: "string"
    description: "The reason the customer's payment method is invalid."

  - name: "shopify_customer_id"
    type: "string"
    description: "The customer's ID in Shopify."
    foreign-key-id: "shopify-customer-id"

  - name: "status"
    type: "string"
    description: "The status of the customer. Possible values are `active` and `failed`."
---