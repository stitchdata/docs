---
tap: "square"
version: "2"
key: ""

name: "team_members"
doc-link: 
singer-schema: https://github.com/singer-io/tap-square/tree/TDL-23352-schema-changes/tap_square/schemas/team_members.json
description: ""

replication-method: "Key_based Incremental"

table-key-properties: ""
valid-replication-keys: "updated_at"

attributes:
  - name: "assigned_locations"
    type: "object"
    description: ""
    subattributes:
    - name: "assignment_type"
      type: "string"
      description: ""

    - name: "location_ids"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""


  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "email_address"
    type: "string"
    description: ""

  - name: "family_name"
    type: "string"
    description: ""

  - name: "given_name"
    type: "string"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "is_owner"
    type: "boolean"
    description: ""

  - name: "phone_number"
    type: "string"
    description: ""

  - name: "reference_id"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""
    replication-key: true
---