---
tap: "pipedrive"
version: "1"
key: "product"

name: "products"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/dynamic_typing/products.json"
description: |
  The `{{ table.name }}` table contains info about the recent products in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent products"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the product was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "files_count"
    type: "integer"
    description: ""

  - name: "first_char"
    type: "string"
    description: ""

  - name: "followers_count"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "owner_name"
    type: "string"
    description: ""

  - name: "prices"
    type: "array"
    description: ""
    subattributes:
      - name: "USD"
        type: "object"
        description: ""
        subattributtes:
          - name: "id"
            type: "integer"
            description: ""

          - name: "product_id"
            type: "integer"
            description: ""

          - name: "price"
            type: "integer"
            description: ""

          - name: "currency"
            type: "string"
            description: ""

          - name: "cost"
            type: "number"
            description: ""

          - name: "overhead_cost"
            type: "number"
            description: ""

  - name: "selectable"
    type: "boolean"
    description: ""

  - name: "tax"
    type: "integer"
    description: ""

  - name: "unit"
    type: "string"
    description: ""

  - name: "visible_to"
    type: "string"
    description: ""
---