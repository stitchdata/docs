---
tap: "selligent"
version: 1.0
key: ""

name: "program"
doc-link: 
singer-schema: https://github.com/singer-io/tap-selligent/blob/master/tap_selligent/schemas.py
description: "This table contains program data."


replication-method: "Full Table"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The asset_id of this mailing."
#    foreign-key-id: "program-id"

  - name: "modified_time"
    type: "string"
    description: ""

  - name: "asset_name"
    type: "string"
    description: ""

  - name: "asset_url"
    type: "string"
    description: ""

  - name: status
    type: "string"
    description: ""    

  - name: "type"
    type: "string"
    description: ""     
---