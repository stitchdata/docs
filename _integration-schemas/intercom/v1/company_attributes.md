---
tap: "intercom"
version: "1"

name: "company_attributes"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#data-attribute-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/company_attributes.json"
description: |
  The `{{ table.name }}` lists data attributes for a specified company in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "listAllDataAttributes"
    doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#list-data-attributes"

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The name of the attribute."
    foreign-key-id: "attribute-name"

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
