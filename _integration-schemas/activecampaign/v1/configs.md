---
tap: "activecampaign"
version: "0.4"
key: ""

name: "configs"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/configs.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The configuration ID."
    #foreign-key-id: "config-id"

  - name: "updated_timestamp"
    type: "date-time"
    description: "The time the configuration was last updated."
    replication-key: true  

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "created_by"
    type: "integer"
    description: ""
  - name: "created_timestamp"
    type: "date-time"
    description: ""
  
  - name: "item"
    type: "string"
    description: ""
  - name: "keyname"
    type: "string"
    description: ""
  - name: "owner"
    type: "integer"
    description: ""
  - name: "section"
    type: "string"
    description: ""
  - name: "udate"
    type: "date-time"
    description: ""
  - name: "updated_by"
    type: "integer"
    description: ""
  
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
  - name: "val"
    type: "string"
    description: ""
---
