---
tap: "activecampaign"
version: "0.4"
key: ""

name: "conversion_triggers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/conversion_triggers.json"
description: ""

replication-method: 

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The conversion trigger ID."
    foreign-key-id: "conversion-trigger-id"

  - name: "udate"
    type: "date-time"
    description: "The date the conversion trigger was last updated."
    replication-key: true

  - name: "automation_block"
    type: "integer"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "conversion"
    type: "integer"
    description: "The conversion ID."
    foreign-key-id: "conversion-id"
  - name: "dynamic"
    type: "integer"
    description: ""
  
  - name: "modifier"
    type: "string"
    description: ""
  - name: "retroactive"
    type: "integer"
    description: ""
  - name: "trigger_type"
    type: "string"
    description: ""

  - name: "value"
    type: "string"
    description: ""
---
