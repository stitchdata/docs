---
tap: "activecampaign"
version: "1"
key: ""

name: "campaign_lists"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/campaign_lists.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign list ID."
    #foreign-key-id: "campaign-list-id"

  - name: "campaign"
    type: "integer"
    description: ""
  - name: "campaignid"
    type: "integer"
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  
  - name: "list"
    type: "integer"
    description: ""
  - name: "list_amt"
    type: "integer"
    description: ""
  - name: "listid"
    type: "integer"
    description: "The list ID."
    foreign-key-id: "list-id"
  - name: "name"
    type: "string"
    description: ""
  - name: "udate"
    type: "date-time"
    description: ""
  - name: "user"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---
