---
tap: "netsuite-suite-analytics"
version: "1"
key: "mfg-routing-steps"

name: "mfg_routing_steps"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/mfg_routing_steps.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "lag_amount"
    type: "integer"
    description: ""

  - name: "lag_type"
    type: "string"
    description: ""

  - name: "lag_units"
    type: "string"
    description: ""

  - name: "mfg_cost_template_id"
    type: "integer"
    description: ""

  - name: "mfg_routing_id"
    type: "integer"
    description: ""

  - name: "mfg_work_center_id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "operation_yield"
    type: "integer"
    description: ""

  - name: "run_rate"
    type: "integer"
    description: ""

  - name: "sequence_0"
    type: "integer"
    description: ""

  - name: "setup_time"
    type: "integer"
    description: ""
---