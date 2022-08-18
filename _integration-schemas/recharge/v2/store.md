---
tap: "recharge"
version: "2"
key: ""

name: "store"
doc-link: https://developer.rechargepayments.com/2021-11/store/store_retrieve
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/store.json
description: |
  The `{{ table.name }}` table contains info about your store.

replication-method: "Full Table"

api-method:
  name: "Retrieve store"
  doc-link: "https://developer.rechargepayments.com/2021-11/store/store_retrieve"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The store ID."
    #foreign-key-id: "store-id"

  - name: "checkout_logo_url"
    type: "string"
    description: ""

  - name: "checkout_platform"
    type: "string"
    description: ""

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customer_portal_base_url"
    type: "string"
    description: ""

  - name: "default_api_version"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "external_platform"
    type: "string"
    description: ""

  - name: "iana_timezone"
    type: "string"
    description: ""

  - name: "identifier"
    type: "string"
    description: ""

  - name: "merchant_portal_base_url"
    type: "string"
    description: ""

  - name: "my_shopify_domain"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "shop_email"
    type: "string"
    description: ""

  - name: "shop_phone"
    type: "string"
    description: ""

  - name: "timezone"
    type: "object"
    description: ""
    subattributes:
      - name: "iana_name"
        type: "string"
        description: ""

      - name: "iana_timezone"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""


  - name: "updated_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "weight_unit"
    type: "string"
    description: ""
---