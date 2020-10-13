---
tap: "square"
version: "1"
key: "category"

name: "categories"
doc-link: "https://developer.squareup.com/reference/square/catalog-api/v1-list-categories"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/categories.json"
description: |
  The `{{ table.name }}` table contains information about item categories for a given location in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "List catalog (`type: category`) (V2)"
  doc-link: "https://developer.squareup.com/reference/square/catalog-api/list-catalog"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The category ID."
    foreign-key-id: "category-id"

  - name: "updated_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "absent_at_location_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "location-id"

  - name: "category_data"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

  - name: "is_deleted"
    type: "boolean"
    description: ""

  - name: "present_at_all_locations"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: ""
  
  - name: "version"
    type: "integer"
    description: ""
---