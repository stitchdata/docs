---
tap: "selligent"
version: 1.0
key: ""

name: "owner"
doc-link: 
singer-schema: https://github.com/singer-io/tap-selligent/blob/master/tap_selligent/schemas.py
description: "This table contains owner data."

replication-method: "Full Table"

attributes:
  - name: "asset_id"
    type: "integer"
    primary-key: true
    description: ""
#    foreign-key-id: "owner-id"

  - name: "modified_time"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""     
---