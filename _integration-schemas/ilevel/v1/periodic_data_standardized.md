---
tap: "ilevel"
version: "1"
key: "periodic-data-standard"

name: "periodic_data_standardized"
doc-link: "{{ integration.api-docs }}"
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/periodic_data_standardized.json"
description: |
  The `{{ table.name }}` table contains info about periodic standardized data.

replication-method: "Key-based Incremental"

api-method:
  name: "iGetBatch"
  doc-link: "{{ integration.api-docs }}"

attributes:
  - name: "hash_key"
    type: "string"
    primary-key: true
    description: |
      This column is a Stitch-generated MD5 hash that should be used as a Primary Key. The hash is created using the following columns:

      {% assign hash-key-columns = table.attributes | where:"hash-key",true | sort:"name" %}
      {% for attribute in hash-key-columns %}
      - `{{ attribute.name }}`
      {% endfor %}

  - name: "reported_date_value"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "currency_code"
    type: "string"
    description: ""
    hash-key: true

  - name: "data_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "data-item-id"
    hash-key: true

  - name: "data_value_type"
    type: "string"
    description: ""
    hash-key: true

  - name: "detail_id"
    type: "integer"
    description: ""

  - name: "end_of_period_value"
    type: "date-time"
    description: ""
    hash-key: true

  - name: "entity_id"
    type: "integer"
    description: ""
    hash-key: true

  - name: "excel_formula"
    type: "string"
    description: ""

  - name: "exchange_rate_type"
    type: "string"
    description: ""
    hash-key: true

  - name: "period_type"
    type: "string"
    description: ""
    hash-key: true

  - name: "request_identifier"
    type: "integer"
    description: ""

  - name: "scenario_id"
    type: "integer"
    description: ""
    foreign-key-id: "scenario-id"
    hash-key: true

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