---
tap: "selligent"
version: 1.0
key: ""

name: "internal_datasource"
doc-link: 
singer-schema: https://github.com/singer-io/tap-selligent/blob/master/tap_selligent/schemas.py
description: "This table contains internal data source data."

replication-method: "Full Table"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The asset_id of this mailing."
    # foreign-key-id: "internal-id"

  - name: "modified_time"
    type: "string"
    description: ""

  - name: "asset_name"
    type: "string"
    description: ""

  - name: "asset_url"
    type: "string"
    description: ""

  - name: "cloud_sync"
    type: "boolean"
    description: ""

  - name: "data_source_stat"
    type: "object"
    descrption: ""  
    subattributes:
     - name: "num_total_rec"
       type: "integer"
       description: ""

  - name: "version_number"
    type: "string"
    description: ""     
---
