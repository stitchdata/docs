---
tap: "ilevel"
version: "1"
key: "periodic-data-standard"

name: "periodic_data_standardized"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/periodic_data_standardized.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: "Key-based Incremental"

api-method:
  name: "todo"
  doc-link: ""

attributes:
  - name: "hash_key"
    type: "string"
    primary-key: true
    description: ""

  - name: "reported_date_value"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "currency_code"
    type: "string"
    description: ""

  - name: "data_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "data-item-id"

  - name: "data_value_type"
    type: "string"
    description: ""

  - name: "detail_id"
    type: "integer"
    description: ""

  - name: "end_of_period_value"
    type: "date-time"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "excel_formula"
    type: "string"
    description: ""

  - name: "exchange_rate_type"
    type: "string"
    description: ""

  - name: "period_type"
    type: "string"
    description: ""

  - name: "request_identifier"
    type: "integer"
    description: ""

  - name: "scenario_id"
    type: "integer"
    description: ""
    foreign-key-id: "scenario-id"

  - name: "standardized_data_id"
    type: "integer"
    description: ""

  - name: "value"
    type: "string"
    description: ""

  - name: "value_numeric"
    type: "number"
    description: ""

  - name: "value_string"
    type: "string"
    description: ""
---