---
tap: "looker"
version: "1"
key: "project-file"

name: "project_files"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/project_files.json"
description: |
  The `{{ table.name }}` table contains info about the files associated with projects in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all project files"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/project#get_all_project_files"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project file ID."
    # foreign-key-id: "project-file-id"

  - name: "editable"
    type: "boolean"
    description: ""

  - name: "extension"
    type: "string"
    description: ""

  - name: "git_status"
    type: "object"
    description: ""
    subattributes:
      - name: "action"
        type: "string"
        description: ""

      - name: "conflict"
        type: "boolean"
        description: ""

      - name: "revertable"
        type: "boolean"
        description: ""

      - name: "text"
        type: "string"
        description: ""

  - name: "mime_type"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: ""

  - name: "project_id"
    type: "string"
    description: ""
    foreign-key-id: "project-id"

  - name: "title"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---