---
tap: "iterable"
version: "1"
key: ""

name: "metadata"
doc-link: https://api.iterable.com/api/docs#metadata_get
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/metadata.json
description: |
  The **{{ table.name }}** table contains the metadata for a single key in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get the metadata value of a single key"
  doc-link: "https://api.iterable.com/api/docs#metadata_get"

attributes:
  - name: "key"
    type: "string"
    primary-key: true
    description: "They metadata key."
    #foreign-key-id: "metadata-id"

  - name: "lastModified"
    type: "date-time"
    description: ""

  - name: "size"
    type: "integer"
    description: ""

  - name: "table"
    type: "string"
    description: ""

  - name: "value"
    type: "object"
    description: ""
    subattributes:
      - name: "inventory"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "sku"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "price"
        type: "integer"
        description: ""

      - name: "product_type"
        type: "string"
        description: ""

      - name: "compare_at_price"
        type: "number"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "product_id"
        type: "string"
        description: ""

      - name: "categories"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: ""
            description: ""

      - name: "vendor"
        type: "string"
        description: ""

      - name: "discount"
        type: "integer"
        description: ""

      - name: "imageUrl"
        type: "string"
        description: ""

      - name: "handle"
        type: "string"
        description: ""


---
