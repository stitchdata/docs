---
tap: "netsuite"
version: "1.0"

name: "Note"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/note.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Note.json"
description: |
  The `{{ table.name }}` table contains info about the notes in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "note"

replication-method: "Key-based Incremental"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "note-id"

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: ""

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

  - name: "item"
    type: "varies"
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