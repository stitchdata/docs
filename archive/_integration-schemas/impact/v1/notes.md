---
tap: "impact"
version: "1"
key: "note"

name: "notes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/notes.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's notes.

replication-method: "Key-based Incremental"

api-method:
  name: "Get notes"
  doc-link: "https://developer.impact.com/default#operations-Notes-GetNotes"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "note-id"

  - name: "modification_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "attachments"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "content"
    type: "string"
    description: ""

  - name: "creation_date"
    type: "string"
    description: ""

  - name: "creator"
    type: "string"
    description: ""

  - name: "media_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-id"

  - name: "media_name"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---