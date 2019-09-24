---
tap: "selligent"
version: 1.0
key: ""

name: "campaign"
doc-link: 
singer-schema: https://github.com/singer-io/tap-selligent/blob/master/tap_selligent/schemas.py
description: "This table contains campaign data."

replication-method: "Full Table"

replication-key:
  name: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "asset_id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "campaign-id"

  - name: "modified_time"
    type: "string"
    description: ""

  - name: "asset_name"
    type: "string"
    description: ""

  - name: "version_number"
    type: "string"
    description: ""     
---