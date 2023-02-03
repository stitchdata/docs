---
tap: "shopify"
version: "1"

name: "inventory_items"
doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/inventoryitem#top"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/inventory_items.json"
description: |
  The `{{ table.name }}` table contains info about items in a shop.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of inventory items"
    doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/inventoryitem#get-inventory-items"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The inventory item ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","inventory item" | replace: "[ACTION]","last updated" }}

  - name: "admin_graphql_api_id"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","inventory item" | replace: "[ACTION]","created" }}

  - name: "sku"
    type: "string"
    description: "The unique SKU (stock keeping unit) of the inventory item."

  - name: "requires_shipping"
    type: "boolean"
    description: "Whether a customer needs to provide a shipping address when placing an order containing the inventory item."

  - name: "cost"
    type: "string"
    description: "The unit cost of the inventory item."

  - name: "country_code_of_origin"
    type: "string"
    description: "The ISO 3166-1 alpha-2 country code of where the item came from."

  - name: "province_code_of_origin"
    type: "string"
    description: "The ISO 3166-2 alpha-2 province code of where the item came from. "

  - name: "harmonized_system_code"
    type: "integer"
    description: "The general Harmonized System (HS) code for the inventory item."

  - name: "tracked"
    type: "boolean"
    description: "Whether inventory levels are tracked for the item."

  - name: "country_harmonized_system_codes"
    type: "array"
    description: "The country-specific Harmonized System (HS) codes for the item."
    subattributes:
      - name: "harmonized_system_code"
        type: "string"
        description: "The Harmonized System (HS) code."
        
      - name: "country_code"
        type: "string"
        description: "The ISO 3166-1 alpha-2 country code."
---