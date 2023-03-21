---
tap: "activecampaign"
version: "0.4"
key: ""

name: "automation_blocks"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/automation_blocks.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The automation block ID."
    #foreign-key-id: "block-id"

  - name: "mdate"
    type: "date-time"
    description: "The date the block was last modified."

  - name: "automation"
    type: "integer"
    description: "The automation ID."
    foreign-key-id: "automation-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "deleted"
    type: "integer"
    description: ""
 
  - name: "ordernum"
    type: "integer"
    description: ""
  - name: "params"
    type: "array, object"
    description: ""
    
  - name: "parent"
    type: "integer"
    description: ""
---
