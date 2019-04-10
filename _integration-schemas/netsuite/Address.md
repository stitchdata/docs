---
tap: "netsuite"
# version: "1.0"

name: "Address"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Address.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "addr1"
    type: "string"
    description: ""

  - name: "addr2"
    type: "string"
    description: ""

  - name: "addr3"
    type: "string"
    description: ""

  - name: "addrPhone"
    type: "string"
    description: ""

  - name: "addrText"
    type: "string"
    description: ""

  - name: "addressee"
    type: "string"
    description: ""

  - name: "attention"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "country"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "override"
    type: "boolean, string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---
