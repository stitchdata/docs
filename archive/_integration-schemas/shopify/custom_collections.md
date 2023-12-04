---
tap: "shopify"
version: "1"

name: "custom_collections"
doc-link: "https://shopify.dev/docs/admin-api/rest/reference/products/customcollection?api[version]=2019-07"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/custom_collections.json"
description: |
  The `{{ table.name }}` table contains info about custom collections. A custom collection is a grouping of products that a merchant creates to make their store easier to browse.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of custom collections"
    doc-link: "https://shopify.dev/docs/admin-api/rest/reference/products/customcollection?api[version]=2019-07"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The custom collection ID."
    foreign-key-id: "collection-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","custom collection" | replace: "[ACTION]","last updated" }}

  # - name: "admin_graphql_api_id"
  #   type: "string"
  #   description: ""

  - name: "body_html"
    type: "string"
    description: |
      The description of the custom collection in HTML format.

  - name: "handle"
    type: "string"
    description: "A human-readable string for the custom collection, automatically generated from its title."

  - name: "image"
    type: "object"
    description: "Details about images associated with the custom collection."
    subattributes:
      - name: "alt"
        type: "string"
        description: "Alternative text that describes the collection image."

      - name: "created_at"
        type: "string"
        description: |
          {{ table.date-time | replace: "[ITEM]","image" | replace: "[ACTION]","created" }}

      - name: "height"
        type: "integer"
        description: "The height of the image in pixels."

      - name: "src"
        type: "string"
        description: "The source URL that specifies the location of the image."

      - name: "width"
        type: "integer"
        description: "The width of the image in pixels."

  - name: "published_at"
    type: "string"
    description: |
      {{ table.date-time | replace: "[ITEM]","custom collection" | replace: "[ACTION]","published" }} This will be `null` for a hidden custom collection.

  - name: "published_scope"
    type: "string"
    description: |
      Indicates if the collection is published to the Point of Sale channel. Possible values are:

      - `web` - The custom collection is published to the Online Store channel, but not to the Point of Sale channel.
      - `global` - The custom collection is published to both the Online Store and Point of Sale channels.

  - name: "sort_order"
    type: "string"
    description: |
      The order in which products in the custom collection appear. Possible values are:

      - `alpha-asc` - Alphabetically, in ascending order (A - Z).
      - `alpha-desc` - Alphabetically, in descending order (Z - A).
      - `best-selling` - By best-selling products.
      - `created` - By date created, in ascending order (oldest - newest).
      - `created-desc` - By date created, in descending order (newest - oldest).
      - `manual` - Order created by the shop owner.
      - `price-asc` - By price, in ascending order (lowest - highest).
      - `price-desc` - By price, in descending order (highest - lowest).

  - name: "template_suffix"
    type: "string"
    description: "The suffix of the Liquid template being used. For example: If the value is `custom`, the collection is using the `collection.custom.liquid` template."

  - name: "title"
    type: "string"
    description: "The name of the custom collection."
---