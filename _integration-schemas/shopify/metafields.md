---
tap: "shopify"
version: "1"

name: "metafields"
doc-link: "https://help.shopify.com/en/api/reference/metafield"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/metafields.json"
description: |
  The `{{ table.name }}` table contains info about resource metafields. These are arbitrary fields used to store additional information about resources.

  #### Metafield replication and resource types {#metafield-replication-and-resources}

  **By default, this table will include only shop-level metafield data**. To replicate the metafields for a given resource type, this table and the table for the resource must be set to replicate.

  For example: To replicate metafield data for Orders, the `orders` table must also be set to replicate.

  Metafield data is available for [`customers`](#customers), [`products`](#products), and [`orders`](#orders).

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of metafields that belong to a resource"
    doc-link: "https://help.shopify.com/en/api/reference/metafield#index"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The metafield ID."
    # foreign-key-id: "metafield-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","metafield" | replace: "[ACTION]","last updated" }}

  # - name: "admin_graphql_api_id"
  #   type: "string"
  #   description: ""

  - name: "created_at"
    type: "date-time"
    description: |
      {{ table.date-time | replace: "[ITEM]","customer" | replace: "[ACTION]","created" }}

  - name: "description"
    type: "string"
    description: "A description of the info that the metafield contains."

  - name: "key"
    type: "string"
    description: "The name of the metafield."

  - name: "namespace"
    type: "string"
    description: "A container for a set of metafields."

  - name: "owner_id"
    type: "integer"
    description: "The ID of the resource that the metafield is attached to."

  - name: "owner_resource"
    type: "string"
    description: |
      The type of resource that the metafield is attached to. Possible values are:

      - `Customer`
      - `Order`
      - `Product`

  - name: "value"
    type: "integer, object, string"
    description: "The information to be stored as metadata."

  - name: "value_type"
    type: "string"
    description: |
      The metafield's information type. Possible values are:

      - `string`
      - `integer`
      - `json_strong`
---