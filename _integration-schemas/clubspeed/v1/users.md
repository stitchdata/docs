---
tap: "clubspeed"
version: "1"

name: "users"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about employees and system users. **Note**: While some employees may also be [`customers`](#customers), this table does not contain customer information.

replication-method: "Full Table"

attributes:
  - name: "userId"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "cardId"
    type: "integer"
    description: "The card ID for the user."

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the user has been soft deleted."

  - name: "email"
    type: "string"
    description: "The email address for the user."

  - name: "empStartDate"
    type: "date-time"
    description: "The date on which the user started employment."

  - name: "enabled"
    type: "boolean"
    description: "Indicates whether the user is currently enabled."

  - name: "firstname"
    type: "string"
    description: "The user's first name."

  - name: "isSystemUser"
    type: "boolean"
    description: "Indicates whether the user is a system/application user or a track employee."

  - name: "lastname"
    type: "string"
    description: "The user's last name."

  - name: "phone"
    type: "string"
    description: "The user's phone number."

  - name: "username"
    type: "string"
    description: "The user's username."
---