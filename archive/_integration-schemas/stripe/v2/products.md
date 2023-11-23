---
tap: "stripe"
version: "2"
key: ""

name: "products"
doc-link: "https://stripe.com/docs/api/products"
singer-schema: https://github.com/singer-io/tap-stripe/tree/master/tap_stripe/schemas/products.json
description: |
  The `{{ table.name }}` table contains info about the products in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all products"
    doc-link: "https://stripe.com/docs/api/products/list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The product ID."
    foreign-key-id: "product-id"

  - name: "created"
    type: "string"
    replication-key: true
    description: "Time at which the product was created. Measured in seconds since the Unix epoch."

  - name: "active"
    type: "boolean"
    description: ""

  - name: "attributes"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "caption"
    type: "string"
    description: ""

  - name: "deactivate_on"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "images"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "livemode"
    type: "boolean"
    description: ""

  - name: "metadata"
    type: "object"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "package_dimensions"
    type: "object"
    description: ""
    subattributes:
    - name: "width"
      type: "number"
      description: ""

    - name: "length"
      type: "number"
      description: ""

    - name: "weight"
      type: "number"
      description: ""

    - name: "height"
      type: "number"
      description: ""


  - name: "shippable"
    type: "boolean"
    description: ""

  - name: "statement_descriptor"
    type: "string"
    description: ""

  - name: "tax_code"
    type: "string"
    description: "A tax code ID."

  - name: "type"
    type: "string"
    description: ""

  - name: "unit_label"
    type: "string"
    description: ""

  - name: "updated"
    type: "string"
    description: ""

  - name: "updated_by_event_type"
    type: "string"
    description: "Description of the event"

  - name: "url"
    type: "string"
    description: ""
---