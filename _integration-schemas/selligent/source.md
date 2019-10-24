---
tap: "selligent"
version: 1.0
key: ""

name: "source"
doc-link: 
singer-schema: https://github.com/singer-io/tap-selligent/blob/master/tap_selligent/schemas.py
description: "This table contains source data."


replication-method: "Full Table"

attributes:
  - name: "asset_id"
    type: "integer"
    primary-key: true
    description: ""
#    foreign-key-id: "source-id"

  - name: "modified_time"
    type: "string"
    description: ""

  - name: "asset_name"
    type: "string"
    description: ""

  - name: "data_source_type"
    type: "string"
    description: ""  

  - name: "version_number"
    type: "string"
    description: ""     
---