---
tap: "uservoice"
version: "1.0"

name: "product_areas"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/.py
description: |
  The `{{ table.name }}` table contains info about your product areas, which can be assigned to features to organize them into groups.

replication-method: "Key-based Incremental"

api-method:
  name: List product areas
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-product-areas

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The product area ID."
    foreign-key-id: "product-area-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the product area was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the product area was created."

  - name: "name"
    type: "string"
    description: "The name of the product area. For example: `Admin - features`"

  - name: "links"
    type: "object"
    description: "The IDs of the users who created/updated the product area."
    subattributes: 
      - name: "updated_by"
        type: "integer"
        description: "The ID of the user who last updated the product area."
        foreign-key-id: "user-id"

      - name: "created_by"
        type: "integer"
        description: "The ID of the user who created the product area."
        foreign-key-id: "user-id"
---