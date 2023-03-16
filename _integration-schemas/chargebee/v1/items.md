---
tap: "chargebee"
version: "1"
key: "item"

name: "items"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/item_model/items.json"
description: |
  The `{{ table.name }}` table contains info about the items in your {{ integration.display_name }} account.

  {{ integration.table-type | flatify }}

replication-method: "Key-based Incremental"

api-method:
  name: "List items"
  doc-link: "https://apidocs.chargebee.com/docs/api/items?prod_cat_ver=2#list_items"

product-catalog-version: "v2"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The item ID."
    foreign-key-id: "item-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the item was last updated."

  - name: "applicable_items"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "enabled_for_checkout"
    type: "boolean"
    description: ""

  - name: "enabled_in_portal"
    type: "boolean"
    description: ""

  - name: "gift_claim_redirect_url"
    type: "string"
    description: ""

  - name: "included_in_mrr"
    type: "boolean"
    description: ""

  - name: "is_giftable"
    type: "boolean"
    description: ""

  - name: "is_shippable"
    type: "boolean"
    description: ""

  - name: "item_applicability"
    type: "string"
    description: ""

  - name: "item_family_id"
    type: "string"
    description: ""
    foreign-key-id: "item-family-id"

  - name: "metadata"
    type: "string"
    description: ""

  - name: "metered"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "redirect_url"
    type: "string"
    description: ""

  - name: "resource_version"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "unit"
    type: "string"
    description: ""

  - name: "usage_calculation"
    type: "string"
    description: ""
---