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
    type: "varies"
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
    type: "varies"
    description: ""

  - name: "parentNexus"
    type: "varies"
    description: ""

  - name: "state"
    type: "varies"
    description: ""

  - name: "taxAgency"
    type: "varies"
    description: ""

  - name: "taxAgencyPst"
    type: "varies"
    description: ""

  - name: "taxCode"
    type: "varies"
    description: ""
---
