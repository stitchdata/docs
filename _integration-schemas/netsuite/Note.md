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
    type: "anything"
    description: ""

  - name: "author"
    type: "anything"
    description: ""

  - name: "customFieldList"
    type: "anything"
    description: ""

  - name: "customForm"
    type: "anything"
    description: ""

  - name: "direction"
    type: "anything"
    description: ""

  - name: "entity"
    type: "anything"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "folder"
    type: "anything"
    description: ""

  - name: "internalId"
    type: "string"
    description: ""

  - name: "item"
    type: "anything"
    description: ""

  - name: "lastModifiedDate"
    type: "date-time"
    description: ""

  - name: "media"
    type: "anything"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "noteDate"
    type: "date-time"
    description: ""

  - name: "noteType"
    type: "anything"
    description: ""

  - name: "nullFieldList"
    type: "anything"
    description: ""

  - name: "record"
    type: "anything"
    description: ""

  - name: "recordType"
    type: "anything"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "topic"
    type: "anything"
    description: ""

  - name: "transaction"
    type: "anything"
    description: ""
---
