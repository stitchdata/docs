---
tap: "recharge"
version: "1"
key: "address"

name: "addresses"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/addresses.json"
description: |
  The `{{ table.name }}` table contains info about the addresses (shipping locations) a customer has. A subscription is tied to a given address, but a customer can have multiple addresses.

replication-method: "Key-based Incremental"
api-method:
  name: "List addresses"
  doc-link: "https://developer.rechargepayments.com/#list-addresses"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The address ID."
    foreign-key-id: "address-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the address was last updated."

  - name: "address1"
    type: "string"
    description: "The street associated with the address."

  - name: "address2"
    type: "string"
    description: "Any additional information associated with the address."

  - name: "cart_attributes"
    type: "array"
    description: "**This field has been deprecated by {{ integration.display_name }}.** Use `note_attributes` instead."
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "cart_note"
    type: "string"
    description: "The note that that will be passed to the `note` field of orders made within the address."

  - name: "city"
    type: "string"
    description: "The city associated with the address."

  - name: "company"
    type: "string"
    description: "The company associated with the address."

  - name: "country"
    type: "string"
    description: "The country associated with the address."

  - name: "created_at"
    type: "date-time"
    description: "The date and time when the address was created."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the customer associated with the address."
    foreign-key-id: "customer-id"

  - name: "discount_id"
    type: "integer"
    description: "The ID of the discount that is applied on the address."
    foreign-key-id: "discount-id"

  - name: "first_name"
    type: "string"
    description: "The customer’s first name associated with the address."

  - name: "last_name"
    type: "string"
    description: "The customer’s last name associated with the address."

  - name: "note_attributes"
    type: "array"
    description: "Extra information that is added to the order."
    subattributes: *name-value

  - name: "original_shipping_lines"
    type: "array"
    description: "**This field has been deprecated by {{ integration.display_name }}.** Use `shipping_lines_override` instead."
    subattributes: &shipping-lines
      - name: "code"
        type: "string"
        description: "A reference to the shipping used."

      - name: "price"
        type: "string"
        description: "The price of the shipping used."

      - name: "title"
        type: "string"
        description: "The title of the shipping used."

  - name: "phone"
    type: "string"
    description: "The phone number associated with the address."

  - name: "province"
    type: "string"
    description: "The state or province associated with the address."

  - name: "shipping_lines_override"
    type: "array"
    description: "Details about the shipping used if the original shipping for the address has been overridden."
    subattributes: *shipping-lines

  - name: "zip"
    type: "string"
    description: "The zip code associated with the address."
---