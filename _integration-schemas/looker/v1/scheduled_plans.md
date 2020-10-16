---
tap: "looker"
version: "1"
key: "scheduled-plan"

name: "scheduled_plans"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/scheduled_plans.json"
description: |
  The `{{ table.name }}` table contains info about all scheduled plans in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all scheduled plans"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/scheduled-plan#get_all_scheduled_plans"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The scheduled plan ID."
    foreign-key-id: "scheduled-plan-id"

  - name: "color_theme"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "crontab"
    type: "string"
    description: ""

  - name: "dashboard_filters"
    type: "string"
    description: ""

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "datagroup"
    type: "string"
    description: ""

  - name: "embed"
    type: "boolean"
    description: ""

  - name: "enabled"
    type: "boolean"
    description: ""

  - name: "filters_string"
    type: "string"
    description: ""

  - name: "include_links"
    type: "boolean"
    description: ""

  - name: "last_run_at"
    type: "date-time"
    description: ""

  - name: "long_tables"
    type: "boolean"
    description: ""

  - name: "look_id"
    type: "string"
    description: ""
    foreign-key-id: "look-id"

  - name: "lookml_dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "lookml-dashboard-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "next_run_at"
    type: "date-time"
    description: ""

  - name: "pdf_landscape"
    type: "boolean"
    description: ""

  - name: "pdf_paper_size"
    type: "string"
    description: ""

  - name: "query_id"
    type: "string"
    description: ""
    foreign-key-id: "query-id"

  - name: "require_change"
    type: "boolean"
    description: ""

  - name: "require_no_results"
    type: "boolean"
    description: ""

  - name: "require_results"
    type: "boolean"
    description: ""

  - name: "run_as_recipient"
    type: "boolean"
    description: ""

  - name: "run_once"
    type: "boolean"
    description: ""

  - name: "scheduled_plan_destination"
    type: "array"
    description: ""
    subattributes:
      - name: "address"
        type: "string"
        description: ""

      - name: "apply_formatting"
        type: "boolean"
        description: ""

      - name: "apply_vis"
        type: "boolean"
        description: ""

      - name: "format"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "looker_recipient"
        type: "boolean"
        description: ""

      - name: "message"
        type: "string"
        description: ""

      - name: "parameters"
        type: "string"
        description: ""

      - name: "scheduled_plan_id"
        type: "string"
        description: ""
        foreign-key-id: "scheduled-plan-id"

      - name: "secret_parameters"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

  - name: "send_all_results"
    type: "boolean"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    subattributes:
      - name: "avatar_url"
        type: "string"
        description: ""

      - name: "display_name"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "user-id"

      - name: "last_name"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"
---