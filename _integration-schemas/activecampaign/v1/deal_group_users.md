---
tap: "activecampaign"
version: "1"
key: ""

name: "deal_group_users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/deal_group_users.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The deal group user ID."
    #foreign-key-id: "deal-group-user-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "deal_group"
    type: "integer"
    description: "The pipeline ID."
    foreign-key-id: "pipeline-id"
  
  - name: "user"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---
