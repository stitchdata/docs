---
tap: "pardot"
version: "1"
key: "user"

name: "users"
doc-link: "http://developer.pardot.com/kb/object-field-references/#user"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Query users"
  doc-link: "http://developer.pardot.com/kb/api-version-3/users/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the user was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the user was created."

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "first_name"
    type: "string"
    description: "The user's first name."

  - name: "job_title"
    type: "string"
    description: "The user's job title."

  - name: "last_name"
    type: "string"
    description: "The user's last name."

  - name: "role"
    type: "string"
    description: "The user's role."
---