---
tap: "selligent"
version: 1.0
key: ""

name: "transactional_mailing"
doc-link: 
singer-schema: https://github.com/singer-io/tap-selligent/blob/master/tap_selligent/schemas.py
description: "This table contains transactional mailing data."


replication-method: "Full Table"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true 
    description: "The asset_id of this mailing."
#    foreign-key-id: "transactional-id"

  - name: "modified_time"
    type: "string"
    description: ""

  - name: "approved"
    type: "boolean"
    description: ""      

  - name: "asset_name"
    type: "string"
    description: ""

  - name: "channel"
    type: "string"
    description: ""

  - name: "compliance"
    type: "boolean"
    description: ""

  - name: "mailing_priority"
    type: "string"
    description: ""

  - name: "mailing_server_group"
    type: "string"
    description: ""

  - name: "mailing_status"
    type: "string"
    description: ""

  - name: "target"
    type: "object"
    description:
    subattributes:
     - name: "asset_id"
       type: "integer"
       description: ""

     - name: "asset_name"
       type: "string"
       description: ""

  - name: "version_number"
    type: "string"
    description: ""     
---