---
tap: "ilevel"
version: "1"
key: "fund"

name: "funds"
doc-link: "{{ integration.api-docs }}"
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/funds.json"
description: |
  The `{{ table.name }}` table contains info about the funds in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "GetFunds"
  doc-link: "{{ integration.api-docs }}"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The fund ID."
    foreign-key-id: "fund-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "business_unit_id"
    type: "integer"
    description: ""

  - name: "calendar_type"
    type: "string"
    description: ""

  - name: "color"
    type: "string"
    description: ""

  - name: "currency_code"
    type: "string"
    description: ""

  - name: "enabled_capabilities_string"
    type: "string"
    description: ""

  - name: "excel_name"
    type: "string"
    description: ""

  - name: "has_logo"
    type: "boolean"
    description: ""

  - name: "initial_period"
    type: "date-time"
    description: ""

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "object_type_id"
    type: "string"
    description: ""

  - name: "owner_type_id"
    type: "integer"
    description: ""

  - name: "period_mapping"
    type: "object"
    description: ""
    subattributes:
      - name: "fiscal_period_mapping"
        type: "array"
        description: ""
        subattributes:
          - name: "calendar_period"
            type: "integer"
            description: ""

          - name: "calendar_quarter"
            type: "integer"
            description: ""

          - name: "calendar_quarter_offset"
            type: "integer"
            description: ""

          - name: "calendar_type"
            type: "string"
            description: ""

          - name: "fiscal_period"
            type: "integer"
            description: ""

          - name: "fiscal_quarter"
            type: "integer"
            description: ""

          - name: "object_id"
            type: "integer"
            description: ""

          - name: "is_fiscal_year_end"
            type: "boolean"
            description: ""

          - name: "is_calendar_year_end"
            type: "boolean"
            description: ""

  - name: "status"
    type: "integer"
    description: ""

  - name: "status_id"
    type: "integer"
    description: ""

  - name: "total_committed_capital"
    type: "number"
    description: ""

  - name: "type_of_plan_id"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "vintage"
    type: "integer"
    description: ""
---