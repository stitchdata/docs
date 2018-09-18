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
  - name: "ListID"
    type: "string"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""

  - name: "Date"
    type: "string"
    description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "State"
    type: "string"
    description: ""

  - name: "CustomFields"
    type: "object"
    description: ""

    object-attributes: 
    - name: "Key"
      type: "string"
      description: ""

    - name: "Value"
      type: "string"
      description: ""

  - name: "ReadsEmailWith"
    type: "string"
    description: ""

  - name: "ConsentToTrack"
    type: "string"
    description: ""
---