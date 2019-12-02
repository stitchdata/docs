---
tap: "3plcentral"
version: "1.0"

name: "stock_summaries"
doc-link: "http://api.3plcentral.com/rels/"
singer-schema: "https://github.com/singer-io/tap-3plcentral/blob/master/tap_3plcentral/schemas/stock_summaries.json"
description: "This table contains information about stock summaries."

replication-method: "Full Table"

api-method:
    name: "3PL Central REL documentaion"
    doc-link: "http://api.3plcentral.com/rels/inventory/stocksummaries"

attributes:
  - name: "facility_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "facility-id"

  - name: "item_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "item-id"

  - name: "allocated"
    type: "number"
    description: ""

  - name: "available"
    type: "number"
    description: ""
  
  - name: "item_identifier"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "item-identifier"
      - name: "sku"
        type: "string"
        description: ""

  - name: "on_hand"
    type: "number"
    description: ""

  - name: "on_hold"
    type: "number"
    description: ""

  - name: "qualifier"
    type: "string"
    description: ""

  - name: "total_received"
    type: "number"
    description: ""
---
