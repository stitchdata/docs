---
tap: "snapchat-ads"
version: "1"
key: ""

name: "product_sets"
doc-link: https://developers.snapchat.com/api/docs/#get-all-product-sets
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/product_sets.json
description: "This stream will get all the Product Sets within the Catalog."

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "id"
    primary-key: true
    type: "string"
    description: "Id of the product set"

  - name: "catalog_id"
    type: "string"
    description: "Catalog's Id to which the product set belongs to"

  - name: "name"
    type: "string"
    description: "Name of the Product Set"

  - name: "filter"
    type: "object"
    description: "Filter rule to be applied"
      subattributes:

        - name: "updated_at"
          type: "date-time"
          description: "Latest Date and Time ast which product set was updated"

        - name: "created_at"
          type: "date-time"
          description: "Date and time at which product set was created"

---