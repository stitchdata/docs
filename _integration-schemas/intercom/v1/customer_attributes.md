---
tap: "intercom"
version: "1"

name: "customer_attributes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/customer_attributes.json"
description: |
  The `{{ table.name }}` table contains information about your customers in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the customer attribute."
    foreign-key-id: "customer-attribute-name"

  - name: "admin_id"
    type: "integer"
    description: ""
  - name: "api_writable"
    type: "boolean"
    description: ""
  - name: "archived"
    type: "boolean"
    description: ""
  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "custom"
    type: "boolean"
    description: ""
  - name: "data_type"
    type: "string"
    description: ""
  - name: "description"
    type: "string"
    description: ""
  - name: "full_name"
    type: "string"
    description: ""
  - name: "label"
    type: "string"
    description: ""
  
  - name: "options"
    type: "null"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "ui_writable"
    type: "boolean"
    description: ""
  - name: "updated_at"
    type: "date-time"
    description: ""
---
