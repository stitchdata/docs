---
tap: "shopify"
version: "1.0"

name: "customers"
doc-link: "https://help.shopify.com/en/api/reference/customers"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the shop's customers. This includes their contact details, order history, and email marketing preferences.

  #### Customer metafield data

  To replicate customer metafield data, you must set this table and the [`metafields`](#metafields) table to replicate.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of customers"
    doc-link: "https://help.shopify.com/en/api/reference/customers/customer#index"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","customer" | replace: "[ACTION]","last updated" }}

  - name: "accepts_marketing"
    type: "boolean"
    description: "Indicates if the customer has consented to receive marketing emails."

  - name: "addresses"
    type: "array"
    description: "A list of the 10 most recently updated addresses for the customer."
    subattributes: &address-fields
      - name: "address1"
        type: "string"
        description: "The street address."

      - name: "address2"
        type: "string"
        description: "The second line of the street address."

      - name: "city"
        type: "string"
        description: "The city, town, or village."

      - name: "company"
        type: "string"
        description: "The company associated with the address."

      - name: "country"
        type: "string"
        description: "The country associated with the address."

      - name: "country_code"
        type: "string"
        description: "The two-letter country code corresponding to the `country`."

      - name: "country_name"
        type: "string"
        description: "The normalized `country` name."

      - name: "customer_id"
        type: "integer"
        description: "The customer's ID."
        foreign-key-id: "customer-id"

      - name: "default"
        type: "boolean"
        description: "Indicates if the address is the default address for the customer."

      - name: "first_name"
        type: "string"
        description: "The customer's first name."

      - name: "id"
        type: "integer"
        description: "The address ID."

      - name: "last_name"
        type: "string"
        description: "The customer's last name."

      - name: "name"
        type: "string"
        description: "The customer's first and last names."

      - name: "phone"
        type: "string"
        description: "The customer's phone number at this address."

      - name: "province"
        type: "string"
        description: "The customer's region name."

      - name: "province_code"
        type: "string"
        description: "The two-letter province code for the region."

      - name: "zip"
        type: "string"
        description: "The customer's postal or zip code."

  # - name: "admin_graphql_api_id"
  #   type: "string"
  #   description: ""

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","customer" | replace: "[ACTION]","created" }}

  - name: "default_address"
    type: "object"
    description: "Details about the default address for the customer."
    object-properties: *address-fields

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "first_name"
    type: "string"
    description: "The customer's first name."

  - name: "last_name"
    type: "string"
    description: "The customer's last name."

  - name: "last_order_id"
    type: "integer"
    description: "The ID of the customer's last order."
    foreign-key-id: "order-id"

  - name: "last_order_name"
    type: "string"
    description: "The name of the customer's last order."

  - name: "multipass_identifier"
    type: "string"
    description: "The ID of the cu stomer's Multipass login."

  - name: "note"
    type: "string"
    description: "A note about the customer."

  - name: "orders_count"
    type: "integer"
    description: "The number of orders associated with the customer."

  - name: "phone"
    type: "string"
    description: |
      The phone number for the customer, in [E.164 format](https://en.wikipedia.org/wiki/E.164){:target="new"}.

  - name: "state"
    type: "string"
    description: |
      The state of the customer's account with a shop. Possible values are:

      - `disabled` - The customer doesn't have an active account.
      - `invited` - The customer has received an email invite to create an account.
      - `enabled` - The customer has created an account.
      - `declined` - The customer has declined the eamil invite to create an account.

  - name: "tags"
    type: "string"
    description: "Tags that the shop owner has attached to the customer."

  - name: "tax_exempt"
    type: "boolean"
    description: |
      Indicates if the customer is exempt from paying taxes on their order. If `true`, taxes will not be applied to an order at checkout.

  - name: "total_spent"
    type: "string"
    description: "The total amount of money that the customer has spent across their order history."

  - name: "verified_email"
    type: "boolean"
    description: "Indicates if the customer has verified their email address."
---