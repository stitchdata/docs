---
tap: "harvest"
version: "2.0"

name: "estimate_item_categories"
doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-item-categories/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/estimate_item_categories.json
description: |
  The `estimate_item_categories` table contains info about the estimate item categories in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: listAllEstimateItemCategories
  doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimate-item-categories/#list-all-estimate-item-categories

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The estimate item category ID."
    # foreign-key-id: "estimate-item-category-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "Date and time the estimate item category was last updated."

  - name: "name"
    type: "string"
    description: "The name of the estimate item category."

  - name: "created_at"
    type: "string"
    description: "Date and time the estimate item category was created."
---