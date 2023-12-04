---
tap: "recharge"
version: "1"
key: "shop"

name: "shop"
doc-link: "https://developer.rechargepayments.com/#retrieve-shop"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/shop.json"
description: |
  The `{{ table.name }}` table contains info about your shop.

replication-method: "Full Table"
api-method:
  name: "Retrieve shop"
  doc-link: "https://developer.rechargepayments.com/#retrieve-shop"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The shop ID."
    # foreign-key-id: "shop-id"

  - name: "checkout_logo_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    description: "The date and time the shop was created."

  - name: "currency"
    type: "string"
    description: "The currency used by the store. For example: `USD`"

  - name: "domain"
    type: "string"
    description: "The global domain name of the store."

  - name: "email"
    type: "string"
    description: "**This field has been deprecated by {{ integration.display_name }}. Use `shop_email` instead.**"

  - name: "iana_timezone"
    type: "string"
    description: "The timezone of the shop in Iana database timezone format."

  - name: "my_shopify_domain"
    type: "string"
    description: "The store domain name in Shopify."

  - name: "name"
    type: "string"
    description: "The name of the store."

  - name: "shop_email"
    type: "string"
    description: "The email address of the shop owner."

  - name: "shop_phone"
    type: "string"
    description: "The phone number of the shop owner."

  - name: "timezone"
    type: "string"
    description: "The timezone of the shop."

  - name: "updated_at"
    type: "string"
    description: "The date and time the shop was last updated."
---