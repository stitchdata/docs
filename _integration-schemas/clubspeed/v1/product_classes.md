---
tap: "clubspeed"
version: "1.0"

name: "product_classes"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/product_classes.json"
description: |
  The `{{ table.name }}` table contains info about classes applied to [`products`](#products). Product classes determine how products are aggregated in {{ integration.display_name }}'s reporting system.

replication-method: "Full Table"

attributes:
  - name: "productClassId"
    type: "integer"
    primary-key: true
    description: "The product class ID."
    foreign-key-id: "product-class-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the product class has been soft deleted."

  - name: "description"
    type: "string"
    description: "The description of the product class."

  - name: "exportName"
    type: "string"
    description: "The export name to be used when building exports from reports."
---