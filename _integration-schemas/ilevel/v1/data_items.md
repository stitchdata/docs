---
tap: "ilevel"
version: "1"
key: "data-items"

name: "data_items"
doc-link: "{{ integration.api-docs }}"
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/data_items.json"
description: |
  The `{{ table.name }}` table contains info about global data items in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "GetDataItems"
  doc-link: "{{ integration.api-docs }}"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The data item ID."
    foreign-key-id: "data-item-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The time the data item was last modified."

  - name: "aggregation_null_replacement"
    type: "boolean"
    description: ""

  - name: "aggregation_type_id"
    type: "integer"
    description: ""

  - name: "asset_i_ds_string"
    type: "string"
    description: ""

  - name: "asset_id"
    type: "integer"
    description: ""
    foreign-key-id: "asset-id"

  - name: "category_id"
    type: "integer"
    description: ""

  - name: "conversion_type_id"
    type: "integer"
    description: ""

  - name: "data_value_type"
    type: "integer"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "enabled_capabilities_string"
    type: "string"
    description: ""

  - name: "excel_name"
    type: "string"
    description: ""

  - name: "format_decimals"
    type: "integer"
    description: ""

  - name: "format_type_id"
    type: "integer"
    description: ""

  - name: "formula_type_i_ds_string"
    type: "string"
    description: ""

  - name: "is_carry_over"
    type: "boolean"
    description: ""

  - name: "is_global"
    type: "boolean"
    description: ""

  - name: "is_monetary"
    type: "boolean"
    description: ""

  - name: "is_number_comma_separated"
    type: "boolean"
    description: ""

  - name: "is_putable"
    type: "boolean"
    description: ""

  - name: "is_scalable"
    type: "boolean"
    description: ""

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "object_type_id"
    type: "string"
    description: ""

  - name: "scenario_i_ds_string"
    type: "string"
    description: ""
---