---
tap: "activecampaign"
version: "0.3"
key: ""

name: "ecommerce_customers"
doc-link: "https://developers.activecampaign.com/reference#customers"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/ecommerce_customers.json"
description: |
  The `{{ table.name }}` table contains the aggregated e-commerce data from customers in your {{ integration.display_name }} account who are using an external e-commerce service.

replication-method: "Key-based Incremental"

api-method:
    name: "List all customers"
    doc-link: "https://developers.activecampaign.com/reference#list-all-customers"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "tstamp"
    type: "date-time"
    description: "The time the customer was last updated."
    replication-key: true

  - name: "avg_product_category"
    type: "string"
    description: ""
  - name: "avg_revenue_per_order"
    type: "null"
    description: ""
  - name: "connection"
    type: "integer"
    description: ""
  - name: "connectionid"
    type: "integer"
    description: "The connection ID."
    foreign-key-id: "connection-id"
  - name: "email"
    type: "string"
    description: ""
  - name: "externalid"
    type: "string"
    description: ""
  
  - name: "total_orders"
    type: "integer"
    description: ""
  - name: "total_products"
    type: "integer"
    description: ""
  - name: "total_revenue"
    type: "null"
    description: ""
  
---
