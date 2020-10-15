---
tap: "looker"
version: "1"
key: ""

name: "color_collections"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/color-collection#get_all_color_collections"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/color_collections.json"
description: |
  The `{{ table.name }}` table contains information about color collections in your {{ integration.display_name }} account.
  
replication-method: "Full Table"

api-method:
    name: "Get all Color Collections"
    doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/color-collection#get_all_color_collections"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The color collection ID."

  - name: "categoricalPalettes"
    type: "array"
    description: ""
    subattributes:
      - name: "colors"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""
      - name: "id"
        type: "string"
        description: ""
      - name: "label"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "divergingPalettes"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "label"
        type: "string"
        description: ""
      - name: "stops"
        type: "array"
        description: ""
        subattributes:
          - name: "color"
            type: "string"
            description: ""
          - name: "offset"
            type: "number"
            description: ""
      - name: "type"
        type: "string"
        description: ""
  
  - name: "label"
    type: "string"
    description: ""
  - name: "sequentialPalettes"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "label"
        type: "string"
        description: ""
      - name: "stops"
        type: "array"
        description: ""
        subattributes:
          - name: "color"
            type: "string"
            description: ""
          - name: "offset"
            type: "number"
            description: ""
      - name: "type"
        type: "string"
        description: ""
---
