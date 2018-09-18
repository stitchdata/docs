---
tap: "campaign-monitor"
# version: "1.0"

name: "table_name"
doc-link: 
singer-schema: 
description: |
  ## description of the table

replication-method: "Key-based Incremental / Full Table"

replication-key:
  name: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  - name: "CampaignID"
    type: "string"
    description: ""

  - name: "Recipients"
    type: "integer"
    description: ""

  - name: "TotalOpened"
    type: "integer"
    description: ""

  - name: "Clicks"
    type: "integer"
    description: ""

  - name: "Unsubscribed"
    type: "integer"
    description: ""

  - name: "Bounced"
    type: "integer"
    description: ""

  - name: "UniqueOpened"
    type: "integer"
    description: ""

  - name: "SpamComplaints"
    type: "integer"
    description: ""

  - name: "WebVersionURL"
    type: "string"
    description: ""

  - name: "WebVersionTextURL"
    type: "string"
    description: ""

  - name: "WorldviewURL"
    type: "string"
    description: ""

  - name: "Forwards"
    type: "integer"
    description: ""

  - name: "Likes"
    type: "integer"
    description: ""

  - name: "Mentions"
    type: "integer"
    description: ""
---