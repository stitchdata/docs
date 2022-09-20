---
tap: "yotpo"
version: "2"
key: ""

name: "order_fulfillments"
doc-link: 
singer-schema: https://github.com/singer-io/tap-yotpo/tree/master/tap_yotpo/schemas/order_fulfillments.json
description: ""

replication-method: "Key-based Incremental"

api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The order fulfillment ID."
    foreign-key-id: "order-fulfillment-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the fulfillment was last updated."

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "external_id"
    type: "string"
    description: ""

  - name: "fulfilled_items"
    type: "array"
    description: ""
    subattributes:
      - name: "yotpo_product_id"
        type: "integer"
        description: ""

      - name: "external_product_id"
        type: "string"
        description: ""

      - name: "quantity"
        type: "integer"
        description: ""


  - name: "fulfillment_date"
    type: "date-time"
    description: ""

  - name: "order_id"
    type: "string"
    description: ""

  - name: "shipment_info"
    type: "object"
    description: ""
    subattributes:
      - name: "shipment_status"
        type: "string"
        description: ""

      - name: "tracking_company"
        type: "string"
        description: ""

      - name: "tracking_url"
        type: "string"
        description: ""

      - name: "tracking_number"
        type: "string"
        description: ""


  - name: "status"
    type: "string"
    description: ""
---