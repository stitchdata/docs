---
tap: "netsuite"
# version: "1.0"

name: "Nexus"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Nexus.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "country"
    type: "anything"
    description: ""

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

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "parentNexus"
    type: "anything"
    description: ""

  - name: "state"
    type: "anything"
    description: ""

  - name: "taxAgency"
    type: "anything"
    description: ""

  - name: "taxAgencyPst"
    type: "anything"
    description: ""

  - name: "taxCode"
    type: "anything"
    description: ""
---
