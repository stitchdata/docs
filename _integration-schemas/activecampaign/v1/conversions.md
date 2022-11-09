---
tap: "activecampaign"
version: "0.3"
key: ""

name: "conversions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/conversions.json"
description: ""

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The conversion ID."
    foreign-key-id: "conversion-id"

  - name: "udate"
    type: "date-time"
    description: "The date the conversion was last updated."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "currency"
    type: "string"
    description: ""
  - name: "enforcelimit"
    type: "integer"
    description: ""
  
  - name: "limit"
    type: "integer"
    description: ""
  - name: "name"
    type: "string"
    description: ""

  - name: "value"
    type: "integer"
    description: ""
---
