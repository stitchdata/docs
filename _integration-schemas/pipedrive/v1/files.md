---
tap: "pipedrive"
version: "1"
key: "file"

name: "files"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/files.json"
description: |
  The `{{ table.name }}` table contains info about the recently updated files in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent files"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The file ID."
    foreign-key-id: "file-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the file was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "activity_id"
    type: "integer"
    description: ""
    foreign-key-id: "activity-id"

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "cid"
    type: "string"
    description: ""

  - name: "deal_id"
    type: "integer"
    description: ""
    foreign-key-id: "deal-id"

  - name: "deal_name"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "email_message_id"
    type: "integer"
    description: ""

  - name: "file_name"
    type: "string"
    description: ""

  - name: "file_size"
    type: "integer"
    description: ""

  - name: "file_type"
    type: "string"
    description: ""

  - name: "inline_flag"
    type: "boolean"
    description: ""

  - name: "log_id"
    type: "integer"
    description: ""

  - name: "mail_message_id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "note_id"
    type: "integer"
    description: ""
    foreign-key-id: "note-id"

  - name: "org_id"
    type: "integer"
    description: ""
    foreign-key-id: "organization-id"

  - name: "org_name"
    type: "string"
    description: ""

  - name: "people_name"
    type: "string"
    description: ""

  - name: "person_id"
    type: "integer"
    description: ""
    foreign-key-id: "person-id"

  - name: "person_name"
    type: "string"
    description: ""

  - name: "product_id"
    type: "integer"
    description: ""
    foreign-key-id: "product-id"

  - name: "product_name"
    type: "string"
    description: ""

  - name: "remote_id"
    type: "string"
    description: ""

  - name: "remote_location"
    type: "string"
    description: ""

  - name: "s3_bucket"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---