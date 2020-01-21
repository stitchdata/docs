---
tap: "pipedrive"
version: "1"
key: "note"

name: "notes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/dynamic_typing/notes.json"
description: |
  The `{{ table.name }}` table contains info about recent notes in your {{ integration.display_name }} account. Notes are pieces of textual (HTML-formatted) information that can be attached to [`deals`](#deals), [`persons`](#persons) and [`organizations`](#organizations).

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent notes"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The note ID."
    foreign-key-id: "note-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the note was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "content"
    type: "string"
    description: ""

  - name: "deal"
    type: "object"
    description: ""
    subattributes:
      - name: "title"
        type: "string"
        description: ""

  - name: "deal_id"
    type: "integer"
    description: ""
    foreign-key-id: "deal-id"

  - name: "last_update_user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "org_id"
    type: "integer"
    description: ""
    foreign-key-id: "organization-id"

  - name: "organization"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

  - name: "person"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

  - name: "person_id"
    type: "integer"
    description: ""
    foreign-key-id: "person-id"

  - name: "pinned_to_deal_flag"
    type: "boolean"
    description: ""

  - name: "pinned_to_organization_flag"
    type: "boolean"
    description: ""

  - name: "pinned_to_person_flag"
    type: "boolean"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    subattributes:
      - name: "email"
        type: "string"
        description: ""

      - name: "icon_url"
        type: "string"
        description: ""

      - name: "is_you"
        type: "boolean"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---