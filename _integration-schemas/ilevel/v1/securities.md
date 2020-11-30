---
tap: "ilevel"
version: "1"
key: "security"

name: "securities"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/securities.json"
description: |
  The `{{ table.name }}` table contains info about the securities in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "GetSecurities"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The security ID."
    foreign-key-id: "security-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The time the security was last modified."

  - name: "asset_id"
    type: "integer"
    description: ""
    foreign-key-id: "asset-id"

  - name: "excel_name"
    type: "string"
    description: ""

  - name: "has_data"
    type: "boolean"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "is_ownership"
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

  - name: "security_sub_type_id"
    type: "integer"
    description: ""

  - name: "security_sub_type_name"
    type: "string"
    description: ""

  - name: "security_type_id"
    type: "integer"
    description: ""

  - name: "security_type_name"
    type: "string"
    description: ""
---