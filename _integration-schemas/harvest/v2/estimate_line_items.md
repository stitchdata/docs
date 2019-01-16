---
tap: "harvest"
version: "2.0"

name: "estimate_line_items"
doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimates/#the-estimate-line-item-object
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/estimate_line_items.json
description: |
  The `{{ table.name }}` table contains info about the line items contained in estimates.

  **Note**: This table is updated based on new and updated `estimates`. This means that when an estimate is updated, this table will also be updated.

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"
  ## This is replicated as part of the parent table, estimates

api-method:
  name: List all estimates
  doc-link: https://help.getharvest.com/api-v2/estimates-api/estimates/estimates/#get-all-estimates

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The estimate line item ID."
    # foreign-key-id: "estimate-line-item-id"

  - name: "estimate_id"
    type: "integer"
    description: "The ID of the estimate the line item is a part of."
    foreign-key-id: "estimate-id"

  - name: "kind"
    type: "string"
    description: "The name of the estimate item category associated with the line item."

  - name: "description"
    type: "string"
    description: "The description of the item."

  - name: "quantity"
    type: "integer"
    description: "The unit quantity of the item."

  - name: "unit_price"
    type: "number"
    description: "The individual price per unit."

  - name: "amount"
    type: "number"
    description: "The line item subtotal, calculated as `quantity * unit_price`."

  - name: "taxed"
    type: "boolean"
    description: "If `true`, the estimate's `tax` percentage applies to the item."

  - name: "taxed2"
    type: "boolean"
    description: "If `true`, the estimate's `tax2` percentage applies to the item."
---