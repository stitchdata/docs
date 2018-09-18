---
tap: "campaign-monitor"
# version: "1.0"

name: "table_name"
doc-link: 
singer-schema: 
description: |
  ## description of the table

replication-method: "Key-based Incremental / Full Table"

replication-key:
  name: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "CampaignID"
    type: "string"
    description: ""

  - name: "Client"
    type: "string"
    description: ""

  - name: "Version"
    type: "string"
    description: ""

  - name: "Percentage"
    type: "number"
    description: ""

  - name: "Subscribers"
    type: "integer"
    description: ""
---