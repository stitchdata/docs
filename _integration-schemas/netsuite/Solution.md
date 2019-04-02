---
tap: "netsuite"
# version: "1.0"

name: "Solution"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Solution.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "assigned"
    type: "varies"
    description: ""

  - name: "createdDate"
    type: "date-time"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "displayOnline"
    type: "boolean, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "longDescription"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "solutionCode"
    type: "string"
    description: ""

  - name: "solutionsList"
    type: "varies"
    description: ""

  - name: "status"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "topicsList"
    type: "varies"
    description: ""
---
