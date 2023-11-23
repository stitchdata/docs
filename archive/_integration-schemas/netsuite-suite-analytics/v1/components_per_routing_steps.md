---
tap: "netsuite-suite-analytics"
version: "1"
key: "components-per-routing-step"

name: "components_per_routing_steps"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/components_per_routing_steps.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "component_id"
    type: "integer"
    description: ""

  - name: "mfg_routing_id"
    type: "integer"
    description: ""

  - name: "sequence_id"
    type: "integer"
    description: ""

  - name: "sequence_number"
    type: "integer"
    description: ""
---