---
tap: "x-y"
version: "1.0"
key: "stock"

name: "stock_transfer"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-x-y/blob/master/tap_x_y/schemas/stock_transfer.json"
description: |
  The `{{ table.name }}` table contains information about stock transfers in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The stock ID."
    foreign-key-id: "stock-id"

  - name: "last_modified"
    type: "integer"
    description: "The time the stock transfer was last modified."
    replication-key: true

  - name: "date"
    type: "integer"
    description: ""
  - name: "from_location_uri"
    type: "string"
    description: ""
  
  - name: "item_uri"
    type: "string"
    description: "The item URI."
    foreign-key-id: "item-id"
  
  - name: "quantity"
    type: "integer"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "stocktransfer_uri"
    type: "string"
    description: ""
  - name: "to_location_uri"
    type: "string"
    description: ""
  - name: "transfer_out"
    type: "integer"
    description: ""
  - name: "transferred_out_by_uri"
    type: "string"
    description: ""
  - name: "transferred_out_on"
    type: "integer"
    description: ""
---
