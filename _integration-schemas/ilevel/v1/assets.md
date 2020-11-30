---
tap: "ilevel"
version: "1"
key: "asset"

name: "assets"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/assets.json"
description: |
  The `{{ table.name }}` table contains info about the assets in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "GetAssets"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The asset ID."
    foreign-key-id: "asset-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The time when the asset was last modified."

  - name: "acquisition_as_of"
    type: "date-time"
    description: ""

  - name: "acquisition_date"
    type: "date-time"
    description: ""

  - name: "asset_status_id"
    type: "integer"
    description: ""

  - name: "calendar_type"
    type: "string"
    description: ""

  - name: "currency_code"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "excel_name"
    type: "string"
    description: ""

  - name: "has_acquisition_as_of"
    type: "boolean"
    description: ""

  - name: "industry_id"
    type: "integer"
    description: ""

  - name: "initial_period"
    type: "date-time"
    description: ""

  - name: "investment_thesis"
    type: "string"
    description: ""

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "lead_fund_id"
    type: "integer"
    description: ""
    foreign-key-id: "fund-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "object_type_id"
    type: "string"
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

  - name: "type_id"
    type: "integer"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---