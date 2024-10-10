---
tap: "google-ads"
version: "1"
name: "labels"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/Label
description: |
  The `{{ table.name }}` table contains info about labels.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resource_name"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "text_label"
    type: "object"
    description: ""
    subattributes:
      - name: "background_color"
        type: "string"
        description: ""
        
      - name: "description"
        type: "string"
        description: ""

  - name: "id"
    type: "integer"
    description: ""
    primary-key: true

  - name: "name"
    type: "string"
    description: ""

---