---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-template"

name: "project_templates"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/projecttemplate.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "billing_rate_card_id"
    type: "integer"
    description: ""

  - name: "billing_schedule_type"
    type: "string"
    description: ""

  - name: "date_scheduled_end"
    type: "date-time"
    description: ""

  - name: "date_template_start"
    type: "date-time"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "is_limit_time_to_assignees"
    type: "string"
    description: ""

  - name: "is_source_item_from_brc"
    type: "string"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "project_expense_type_id"
    type: "integer"
    description: ""

  - name: "project_manager_id"
    type: "integer"
    description: ""
    foreign-key-id: "emplooyee-id"

  - name: "scheduling_method_id"
    type: "string"
    description: ""

  - name: "stitch_custom_field"
    type: "number"
    description: ""

  - name: "stitch_custom_field_check_box"
    type: "string"
    description: ""

  - name: "stitch_custom_field_currency"
    type: "number"
    description: ""

  - name: "stitch_custom_field_decimal"
    type: "number"
    description: ""

  - name: "template_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-rate-card-id"

  - name: "template_name"
    type: "string"
    description: ""

  - name: "use_budget_from_allocations"
    type: "string"
    description: ""

  - name: "use_calculated_billing_budget"
    type: "string"
    description: ""

  - name: "use_calculated_cost_budget"
    type: "string"
    description: ""
---