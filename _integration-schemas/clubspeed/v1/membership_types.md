---
tap: "clubspeed"
version: "1"

name: "membership_types"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/membership_types.json"
description: |
  The `{{ table.name }}` table contains info about memberships.

replication-method: "Full Table"

attributes:
  - name: "membershipTypeId"
    type: "integer"
    primary-key: true
    description: "The membership type ID."
    foreign-key-id: "membership-type-id"

  - name: "description"
    type: "string"
    description: "The description of the membership type."

  - name: "enabled"
    type: "integer"
    description: "Indicates whether the membership type is currently enabled."

  - name: "expirationType"
    type: "integer"
    description: "The number of days when this membership will expire."

  - name: "expires"
    type: "boolean"
    description: "Indicates whether or not the membership should ever expire."

  - name: "priceLevel"
    type: "integer"
    description: "The price level that this membership type would grant to a customer."

  - name: "seq"
    type: "integer"
    description: "The sequence in which the membership type should appear in a dropdown."
---