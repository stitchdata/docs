---
tap: "helpscout"
version: "1"

key: "mailbox"
name: "mailboxes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/mailboxes.json"
description: |
  The `{{ table.name }}` table contains info about the mailboxes in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List mailboxes"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/mailboxes/list/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The mailbox ID."
    foreign-key-id: "mailbox-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The UTC time the mailbox was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The UTC time the mailbox was created."

  - name: "email"
    type: "string"
    description: "The email address for the mailbox."

  - name: "name"
    type: "string"
    description: "The name of the mailbox."

  - name: "slug"
    type: "string"
    description: "The key used to represent the mailbox."
---