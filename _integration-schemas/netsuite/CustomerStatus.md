---
tap: "netsuite"
# version: "1.0"

name: "CustomerStatus"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/CustomerStatus.json"
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

  - name: "includeInLeadReports"
    type: "boolean, string"
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

  - name: "probability"
    type: "number, string"
    description: ""

  - name: "stage"
    type: "anything"
    description: ""
---
