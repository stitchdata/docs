---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-task-cost-budget"

name: "project_task_cost_budgets"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_task_cost_budgets.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "amount"
    type: "number"
    description: ""

  - name: "is_calculated"
    type: "string"
    description: ""

  - name: "month_end"
    type: "date-time"
    description: ""

  - name: "month_start"
    type: "date-time"
    description: ""

  - name: "project_cost_category_id"
    type: "integer"
    description: ""

  - name: "project_id"
    type: "integer"
    description: ""

  - name: "project_task_id"
    type: "integer"
    description: ""
---