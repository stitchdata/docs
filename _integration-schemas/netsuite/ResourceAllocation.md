---
tap: "netsuite"
# version: "1.0"

name: "ResourceAllocation"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ResourceAllocation.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "allocationAmount"
    type: "number, string"
    description: ""

  - name: "allocationResource"
    type: "anything"
    description: ""

  - name: "allocationType"
    type: "anything"
    description: ""

  - name: "allocationUnit"
    type: "anything"
    description: ""

  - name: "approvalStatus"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "endDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "nextApprover"
    type: "anything"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "numberHours"
    type: "number, string"
    description: ""

  - name: "percentOfTime"
    type: "number, string"
    description: ""

  - name: "project"
    type: "anything"
    description: ""

  - name: "requestedby"
    type: "anything"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""
---
