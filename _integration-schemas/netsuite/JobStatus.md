---
tap: "netsuite"
# version: "1.0"

name: "JobStatus"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/JobStatus.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "description"
    type: "string"
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

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""
---
