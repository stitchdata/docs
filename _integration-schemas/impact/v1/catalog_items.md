---
tap: "impact"
version: "1"
key: "catalog-item"

name: "catalog_items"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/catalog_items.json"
description: |
  The `{{ table.name }}` table contains info about a catalog's items.

replication-method: "Full Table"

api-method:
  name: "List catalogs"
  doc-link: "https://developer.impact.com/default#operations-Catalogs-ListCatalogs"

attributes:
  - name: "catalog_item_id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "catalog-item-id"

  - name: "additional_image_urls"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "adult"
    type: "boolean"
    description: ""

  - name: "age_group"
    type: "string"
    description: ""

  - name: "asin"
    type: "string"
    description: ""

  - name: "bullets"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "catalog_id"
    type: "integer"
    description: ""
    foreign-key-id: "catalog-id"

  - name: "category"
    type: "string"
    description: ""

  - name: "colors"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "condition"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "current_price"
    type: "number"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "estimated_ship_date"
    type: "date-time"
    description: ""

  - name: "expiration_date"
    type: "date-time"
    description: ""

  - name: "gender"
    type: "string"
    description: ""

  - name: "gtin"
    type: "string"
    description: ""

  - name: "gtin_type"
    type: "string"
    description: ""

  - name: "image_url"
    type: "string"
    description: ""

  - name: "inventory"
    type: "number"
    description: ""

  - name: "is_parent"
    type: "boolean"
    description: ""

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "launch_date"
    type: "date-time"
    description: ""

  - name: "manufacturer"
    type: "string"
    description: ""

  - name: "manufacturing_cost"
    type: "number"
    description: ""

  - name: "material"
    type: "string"
    description: ""

  - name: "mobile_url"
    type: "string"
    description: ""

  - name: "money1"
    type: "number"
    description: ""

  - name: "money2"
    type: "number"
    description: ""

  - name: "money3"
    type: "number"
    description: ""

  - name: "mpn"
    type: "string"
    description: ""

  - name: "multi_pack"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "numeric1"
    type: "number"
    description: ""

  - name: "numeric2"
    type: "number"
    description: ""

  - name: "numeric3"
    type: "number"
    description: ""

  - name: "original_format_category"
    type: "string"
    description: ""

  - name: "original_format_category_id"
    type: "integer"
    description: ""

  - name: "original_price"
    type: "number"
    description: ""

  - name: "parent_name"
    type: "string"
    description: ""

  - name: "parent_sku"
    type: "string"
    description: ""

  - name: "pattern"
    type: "string"
    description: ""

  - name: "product_bid"
    type: "number"
    description: ""

  - name: "shipping_height"
    type: "number"
    description: ""

  - name: "shipping_label"
    type: "string"
    description: ""

  - name: "shipping_length"
    type: "number"
    description: ""

  - name: "shipping_length_unit"
    type: "string"
    description: ""

  - name: "shipping_rate"
    type: "number"
    description: ""

  - name: "shipping_weight"
    type: "number"
    description: ""

  - name: "shipping_weight_unit"
    type: "string"
    description: ""

  - name: "shipping_width"
    type: "number"
    description: ""

  - name: "size"
    type: "string"
    description: ""

  - name: "size_unit"
    type: "string"
    description: ""

  - name: "stock_availability"
    type: "string"
    description: ""

  - name: "text1"
    type: "string"
    description: ""

  - name: "text2"
    type: "string"
    description: ""

  - name: "text3"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "weight"
    type: "number"
    description: ""

  - name: "weight_unit"
    type: "string"
    description: ""
---