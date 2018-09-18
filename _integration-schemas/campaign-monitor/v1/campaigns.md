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

  - name: "FromName"
    type: "string"
    description: ""

  - name: "FromEmail"
    type: "string"
    description: ""

  - name: "ReplyTo"
    type: "string"
    description: ""

  - name: "WebVersionURL"
    type: "string"
    description: ""

  - name: "WebVersionTextURL"
    type: "string"
    description: ""

  - name: "Subject"
    type: "string"
    description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "SentDate"
    type: "string"
    description: ""

  - name: "TotalRecipients"
    type: "number"
    description: ""
---