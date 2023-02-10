---
tap: "snapchat-ads"
version: "1"
key: ""

name: "product_catalogs"
doc-link: https://developers.snapchat.com/api/docs/#get-all-catalogs
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/product_catalogs.json
description: "This stream will retrieve a list of all the catalogs within an organization"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "default_product_set_id"
    type: "string"
    description: "Default product set that includes all the products in the catalog"

  - name: "event_sources"
    type: "array"
    description: "List of Pixel IDs and/or the Snap App IDs that reports events for the Catalog"
    subattributes:
      - name: "id"
        type: "string"
        description: "Pixel ID"

      - name: "type"
        type: "string"
        description: "Pixel Type"


  - name: "id"
    primary-key: true
    type: "string"
    description: "Catalog's Id"

  - name: "source"
    type: "string"
    description: "Indicates the source of Catalog, set automatically on creation"

  - name: "name"
    type: "string"
    description: "Name of the catalog"

  - name: "organization_id"
    type: "string"
    description: "Organization's Id"

  - name: "updated_at"
    type: "date-time"
    description: "latest Date and time at which the catalog was updated"

  - name: "created_at"
    type: "date-time"
    description: "Date and time at which the catalog was created"
---