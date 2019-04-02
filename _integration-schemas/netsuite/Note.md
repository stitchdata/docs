---
tap: "netsuite"
# version: "1.0"

name: "Note"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Note.json"
description: |
  The `{{ table.name }}` table contains info about 

replication-method: ""

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "activity"
    type: "varies"
    description: ""

  - name: "author"
    type: "varies"
    description: ""

  - name: "customFieldList"
    type: "varies"
    description: ""

  - name: "customForm"
    type: "varies"
    description: ""

  - name: "direction"
    type: "varies"
    description: ""

  - name: "entity"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "folder"
    type: "varies"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "item"
    type: "varies"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "media"
    type: "varies"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "noteDate"
    type: "date-time"
    description: ""

  - name: "noteType"
    type: "varies"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "record"
    type: "varies"
    description: ""

  - name: "recordType"
    type: "varies"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "topic"
    type: "varies"
    description: ""

  - name: "transaction"
    type: "varies"
    description: ""
---
