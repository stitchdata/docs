---
tap: "netsuite"
# version: "1.0"

name: "PartnerCategory"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PartnerCategory.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
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

  - name: "parent"
    type: "anything"
    description: ""
---
