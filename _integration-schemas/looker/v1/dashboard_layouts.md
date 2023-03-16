---
tap: "looker"
version: "1"
key: "dashboard-layout"

name: "dashboard_layouts"
doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboardlayouts"
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/dashboard_layouts.json"
description: |
  The `{{ table.name }}` table contains information about all dashboard layouts in your {{ integration.display_name }} instance.
  
replication-method: "Full Table"

api-method:
  name: "Get all dashboard layouts"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/dashboard#get_all_dashboardlayouts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The dashboard layout ID."
    foreign-key-id: "dashboard-layout-id"

  - name: "active"
    type: "boolean"
    description: ""

  - name: "column_width"
    type: "integer"
    description: ""

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "dashboard_layout_components"
    type: "array"
    description: ""
    subattributes:
      - name: "column"
        type: "integer"
        description: ""

      - name: "dashboard_element_id"
        type: "string"
        description: ""
        foreign-key-id: "dashboard-element-id"

      - name: "dashboard_layout_id"
        type: "string"
        description: ""
        foreign-key-id: "dashboard-layout-id"

      - name: "deleted"
        type: "boolean"
        description: ""

      - name: "element_title"
        type: "string"
        description: ""

      - name: "element_title_hidden"
        type: "boolean"
        description: ""

      - name: "height"
        type: "integer"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "row"
        type: "integer"
        description: ""

      - name: "vis_type"
        type: "string"
        description: ""

      - name: "width"
        type: "integer"
        description: ""

  - name: "dashboard_title"
    type: "string"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""
  
  - name: "type"
    type: "string"
    description: ""

  - name: "width"
    type: "integer"
    description: ""
---