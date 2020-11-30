---
tap: "ilevel"
version: "1"
key: "investment"

name: "investments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/investments.json"
description: |
  The `{{ table.name }}` table contains info about the investments in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "GetInvestments"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The investment ID."
    foreign-key-id: "investment-id"

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: "The time the investment was last modified."

  - name: "acquisition_date"
    type: "date-time"
    description: ""

  - name: "commitment"
    type: "number"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "from_id"
    type: "integer"
    description: ""

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "ownership_percentage"
    type: "number"
    description: ""

  - name: "security_id"
    type: "integer"
    description: ""
    foreign-key-id: "security-id"

  - name: "status_id"
    type: "integer"
    description: ""

  - name: "to_id"
    type: "integer"
    description: ""

  - name: "type_id"
    type: "string"
    description: ""
---