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
    type: "varies"
    description: ""

  - name: "allocationType"
    type: "varies"
    description: ""

  - name: "allocationUnit"
    type: "varies"
    description: ""

  - name: "approvalStatus"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "numberHours"
    type: "number, string"
    description: ""

  - name: "percentOfTime"
    type: "number, string"
    description: ""

  - name: "project"
    type: "varies"
    description: ""

  - name: "requestedby"
    type: "varies"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: ""
---
