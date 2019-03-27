---
tap: "netsuite"
# version: "1.0"

name: "ItemRevision"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/ItemRevision.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "effectiveDate"
    type: "date-time"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "inactive"
    type: "boolean, string"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "obsoleteDate"
    type: "date-time"
    description: ""
---
