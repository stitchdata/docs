---
tap: "netsuite-suite-analytics"
version: "1"
key: "project-task-dependency"

name: "project_task_dependencies"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/project_task_dependencies.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "dependency_type"
    type: "string"
    description: ""

  - name: "lag_days"
    type: "integer"
    description: ""

  - name: "predecessor_task_id"
    type: "integer"
    description: ""

  - name: "successor_task_id"
    type: "integer"
    description: ""
---