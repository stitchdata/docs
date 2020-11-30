---
tap: "ilevel"
version: "1"
key: "scenario"

name: "scenarios"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ilevel/blob/master/tap_ilevel/schemas/scenarios.json"
description: |
  The `{{ table.name }}` table contains info about the scenarios in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "GetScenarios"
  doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The scenario ID."
    foreign-key-id: "scenario-id"

  - name: "excel_name"
    type: "string"
    description: ""

  - name: "is_soft_deleted"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---