---
tap: "looker"
version: "1"
key: "lookml-model"

name: "lookml_models"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_all_lookml_models"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/lookml_models.json"
description: |
  The `{{ table.name }}` table contains information about all LookML models in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all LookML models"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/lookml-model#get_all_lookml_models"

attributes:
  - name: "name"
    type: "string"
    primary-key: true
    description: "The LookML model name."

  - name: "project_name"
    type: "string"
    primary-key: true
    description: "The project name."

  - name: "allowed_db_connection_names"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "explores"
    type: "array"
    description: ""
    subattributes:
      - name: "description"
        type: "string"
        description: ""

      - name: "group_label"
        type: "string"
        description: ""

      - name: "hidden"
        type: "boolean"
        description: ""

      - name: "label"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "has_content"
    type: "boolean"
    description: ""

  - name: "label"
    type: "string"
    description: ""

  - name: "unlimited_db_connections"
    type: "boolean"
    description: ""
---