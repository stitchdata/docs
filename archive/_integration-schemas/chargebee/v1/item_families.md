---
tap: "chargebee"
version: "1"
key: "item-family"

name: "item_families"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/item_model/item_families.json"
description: |
  The `{{ table.name }}` table contains info about item families.

  {{ integration.table-type | flatify }}

replication-method: "Key-based Incremental"

api-method:
  name: "List item families"
  doc-link: "https://apidocs.chargebee.com/docs/api/item_families?prod_cat_ver=2#list_item_families"

product-catalog-version: "v2"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The item family ID."
    foreign-key-id: "item-family-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the item family was last updated."

  - name: "description"
    type: "string"
    description: "A description of the item family."

  - name: "name"
    type: "string"
    description: "The name of the item family."

  - name: "object"
    type: "string"
    description: ""

  - name: "resource_version"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: |
      The status of the item family.
---