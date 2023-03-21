---
tap: "activecampaign"
version: "0.4"
key: ""

name: "goals"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/goals.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The goal ID."
    #foreign-key-id: "goal-id"

  - name: "automation"
    type: "integer"
    description: "The automation ID."
    foreign-key-id: "automation-id"
  - name: "automation_block"
    type: "integer"
    description: ""
  - name: "blockid"
    type: "integer"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "dirty_stats"
    type: "integer"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "seriesid"
    type: "integer"
    description: ""
---
