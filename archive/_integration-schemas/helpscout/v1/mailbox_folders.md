---
tap: "helpscout"
version: "1"

key: "mailbox-folder"
name: "mailbox_folders"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/mailbox_folders.json"
description: |
  The `{{ table.name }}` table contains info about the mailbox folders in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List mailbox folders"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/mailboxes/mailbox-folders/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The mailbox folder ID."
    foreign-key-id: "mailbox-folder-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time when the mailbox folder was last updated."

  - name: "active_count"
    type: "integer"
    description: "The number of active conversations in the mailbox folder."

  - name: "mailbox_id"
    type: "integer"
    description: "The ID of the mailbox containing the folder."
    foreign-key-id: "mailbox-id"

  - name: "name"
    type: "string"
    description: "The name of the mailbox folder."

  - name: "total_count"
    type: "integer"
    description: "The total number of conversations in the mailbox folder."

  - name: "type"
    type: "string"
    description: "The type of the mailbox folder."

  - name: "user_id"
    type: "integer"
    description: ""
---