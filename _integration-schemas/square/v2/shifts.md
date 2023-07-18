---
tap: "square"
version: "2"
key: "shift"

name: "shifts"
doc-link: "https://developer.squareup.com/reference/square/labor-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/shifts.json"
description: |
  The `{{ table.name }}` table contains information about employee's shifts in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Search shifts (V2)"
  doc-link: "https://developer.squareup.com/reference/square/labor-api/search-shifts"

attributes:
  - name: "breaks"
    type: "array"
    description: ""
    subattributes:
    - name: "expected_duration"
      type: "string"
      description: ""

    - name: "id"
      type: "string"
      description: ""

    - name: "is_paid"
      type: "boolean"
      description: ""

    - name: "name"
      type: "string"
      description: ""

    - name: "end_at"
      type: "date-time"
      description: ""

    - name: "start_at"
      type: "date-time"
      description: ""

    - name: "break_type_id"
      type: "string"
      description: ""


  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "end_at"
    type: "date-time"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "location_id"
    type: "string"
    description: ""

  - name: "start_at"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "team_member_id"
    type: "string"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "version"
    type: "integer"
    description: ""

  - name: "wage"
    type: "object"
    description: ""
    subattributes:
    - name: "hourly_rate"
      type: "object"
      description: ""
      subattributes:
      - name: "amount"
        type: "integer"
        description: ""

      - name: "currency"
        type: "string"
        description: ""


    - name: "job_id"
      type: "string"
      description: ""

    - name: "title"
      type: "string"
      description: ""
---