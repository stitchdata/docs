---
tap: "square"
version: "1"
key: ""

name: "shifts"
doc-link: "https://developer.squareup.com/reference/square/labor-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/shifts.json"
description: |
  The `{{ table.name }}` table contains information about employee's shifts in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
    name: "Search shifts"
    doc-link: "https://developer.squareup.com/reference/square/labor-api/search-shifts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The shift ID."

  - name: "updated_at"
    type: "date-time"
    description: "The time the shift was last updated."
    replication-key: true
      
  - name: "breaks"
    type: "array"
    description: ""
    subattributes:
      - name: "break_type_id"
        type: "string"
        description: ""
      - name: "end_at"
        type: "date-time"
        description: ""
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
      - name: "start_at"
        type: "date-time"
        description: ""
  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "employee_id"
    type: "string"
    description: "The employee ID that the shift belongs to."
    foreign-key-id: "employee-id"

  - name: "end_at"
    type: "date-time"
    description: ""
  
  - name: "location_id"
    type: "string"
    description: "The location ID of the shift."
    foreign-key-id: "location-id"
  - name: "start_at"
    type: "date-time"
    description: ""
  - name: "status"
    type: "string"
    description: ""
  - name: "timezone"
    type: "string"
    description: ""
  
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
      - name: "title"
        type: "string"
        description: ""
---
