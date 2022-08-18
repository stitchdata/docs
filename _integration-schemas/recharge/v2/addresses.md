---
tap: "recharge"
version: "2"
key: ""

name: "addresses"
doc-link: https://developer.rechargepayments.com/2021-11/addresses/list_addresses
singer-schema: https://github.com/singer-io/tap-recharge/tree/master/tap_recharge/schemas/addresses.json
description: |
  The `{{ table.name }}` table contains info about the addresses (shipping locations) a customer has. A subscription is tied to a given address, but a customer can have multiple addresses.

replication-method: "Key-based Incremental"

api-method:
  name: "List addresses"
  doc-link: "https://developer.rechargepayments.com/2021-11/addresses/list_addresses"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The address ID."
    foreign-key-id: "address-id"

  - name: "updated_at"
    format: "date-time"
    type: "string"
    replication-key: true
    description: "The date and time the address was last updated."


  - name: "address1"
    type: "string"
    description: ""

  - name: "address2"
    type: "string"
    description: ""

  - name: "cart_attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""


  - name: "cart_note"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "company"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "country_code"
    type: "string"
    description: ""

  - name: "created_at"
    format: "date-time"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""

  - name: "discount_id"
    type: "integer"
    description: ""

  - name: "discounts"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""


  - name: "first_name"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "note_attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""


  - name: "order_attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""



  - name: "order_note"
    type: "string"
    description: ""

  - name: "original_shipping_lines"
    type: "array"
    description: ""
    subattributes:
      - name: "code"
        type: "string"
        description: ""

      - name: "price"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""


  - name: "payment_method_id"
    type: "integer"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "presentment_currency"
    type: "string"
    description: ""

  - name: "province"
    type: "string"
    description: ""

  - name: "shipping_lines_override"
    type: "array"
    description: ""
    subattributes:
      - name: "code"
        type: "string"
        description: ""

      - name: "price"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""


  - name: "zip"
    type: "string"
    description: ""
---