---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-task"

name: "project_tasks"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/projecttask.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.
      
  - name: "actual_work"
    type: "integer"
    description: ""

  - name: "allocated_work"
    type: "integer"
    description: ""

  - name: "assigned_id"
    type: "integer"
    description: ""

  - name: "calculated_work"
    type: "integer"
    description: ""

  - name: "calculated_work_baseline"
    type: "integer"
    description: ""

  - name: "constraint_type"
    type: "string"
    description: ""

  - name: "due_date"
    type: "date-time"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "end_date_baseline"
    type: "date-time"
    description: ""

  - name: "estimated_cost"
    type: "integer"
    description: ""

  - name: "estimated_cost_baseline"
    type: "integer"
    description: ""

  - name: "estimated_cost_baseline_frn"
    type: "integer"
    description: ""

  - name: "estimated_cost_foreign"
    type: "integer"
    description: ""

  - name: "estimated_work"
    type: "integer"
    description: ""

  - name: "estimated_work_baseline"
    type: "integer"
    description: ""

  - name: "finish_by_date"
    type: "date-time"
    description: ""

  - name: "is_milestone"
    type: "string"
    description: ""

  - name: "is_non_billable"
    type: "string"
    description: ""

  - name: "is_on_critical_path"
    type: "string"
    description: ""

  - name: "is_summary_task"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "parent_task_id"
    type: "integer"
    description: ""

  - name: "percent_complete"
    type: "integer"
    description: ""

  - name: "percent_complete_by_allocation"
    type: "integer"
    description: ""

  - name: "planned_work"
    type: "integer"
    description: ""

  - name: "planned_work_baseline"
    type: "integer"
    description: ""

  - name: "priority"
    type: "string"
    description: ""

  - name: "project_id"
    type: "integer"
    description: ""

  - name: "projecttask_extid"
    type: "string"
    description: ""

  - name: "projecttask_id"
    type: "integer"
    description: ""

  - name: "slack_minutes"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "start_date_0"
    type: "date-time"
    description: ""

  - name: "start_date_baseline"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "taskorder"
    type: "integer"
    description: ""

  - name: "use_calculated_billing_budget"
    type: "string"
    description: ""

  - name: "use_calculated_cost_budget"
    type: "string"
    description: ""
---