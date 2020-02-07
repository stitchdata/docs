---
tap: "closeio"
version: "1"

name: "users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-closeio/blob/master/tap_closeio/schemas/users.json"

description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

  In {{ integration.display_name }}, users are typically your co-workers and sales reps, or those inside your company.

replication-method: "Key-based Incremental"

api-method:
  name: "List all users who are members of your organizations"
  doc-link: "https://developer.close.io/#users-list-all-the-users-who-are-members-of-the-same-organizations-as-you-are"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "date_updated"
    type: "string"
    replication-key: true
    description: "The date the user was last updated."

  - name: "date_created"
    type: "string"
    description: "The date the user was created."

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "first_name"
    type: "string"
    description: "The first name of the user."

  - name: "image"
    type: "string"
    description: "The URL of the user's avatar."

  - name: "last_name"
    type: "string"
    description: "The last name of the user."

  - name: "last_used_timezone"
    type: "string"
    description: "The user's last used timezone."

  - name: "organizations"
    type: "array"
    description: "A list of organizations associated with the user."
    subattributes:
      - name: "value"
        type: "string"
        primary-key: true
        description: "The organization ID."
        foreign-key-id: "organization-id"
---
