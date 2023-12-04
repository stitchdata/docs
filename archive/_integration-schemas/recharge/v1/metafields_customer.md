---
tap: "recharge"
version: "1"
key: "customer-metafield"

name: "metafields_customer"
doc-link: "https://developer.rechargepayments.com/#list-metafields"
singer-schema: "https://github.com/singer-io/tap-recharge/blob/master/tap_recharge/schemas/metafields_customer.json"
description: |
  The `{{ table.name }}` table contains info about metafields related to customers.

replication-method: "Key-based Incremental"
api-method:
  name: "List customer metafields"
  doc-link: "https://developer.rechargepayments.com/#list-metafields"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer metafield ID."
    foreign-key-id: "customer-metafield-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The date and time the customer metafield was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The date and time the customer metafield was created."

  - name: "description"
    type: "string"
    description: "The description of the metafield."

  - name: "key"
    type: "string"
    description: "The name of the metafield."

  - name: "namespace"
    type: "string"
    description: "The category or container that differentiates the metafield from other fields."

  - name: "owner_id"
    type: "integer"
    description: "The ID of the owner resource."
    foreign-key-id: "owner-id"

  - name: "owner_resource"
    type: "string"
    description: |
      The type of resource that owns the metafield. This will be `customer`.

  - name: "value"
    type: "string"
    description: "The content of the metafield."

  - name: "value_type"
    type: "string"
    description: "The data type of the metafield. For example: `integer`"
---