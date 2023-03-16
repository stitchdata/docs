---
tap: "looker"
version: "1"
key: "model-set"

name: "model_sets"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/model_sets.json"
description: |
  The `{{ table.name }}` table contains info about the role model sets in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all model sets"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/role#get_all_model_sets"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The model set ID."
    foreign-key-id: "model-set-id"

  - name: "all_access"
    type: "boolean"
    description: ""

  - name: "built_in"
    type: "boolean"
    description: ""

  - name: "models"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""
---