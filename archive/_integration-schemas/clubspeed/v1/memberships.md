---
tap: "clubspeed"
version: "1"

name: "memberships"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/memberships.json"
description: |
  The `{{ table.name }}` table contains info about memberships, which is a pairing of a [`customer`](#customers) and [`membership_type`](#membership_types).

replication-method: "Key-based Incremental"

attributes:
  - name: "customerId"
    type: "integer"
    primary-key: true
    description: "The customer ID."

  - name: "membershipTypeId"
    type: "integer"
    primary-key: true
    description: "The membership type ID."

  - name: "changed"
    type: "date-time"
    replication-key: true
    description: "The date at which the membership last changed."

  - name: "byUserId"
    type: "integer"
    description: "The ID of the user who created the membership."
    foreign-key-id: "user-id"

  - name: "expiration"
    type: "date-time"
    description: "The date at which the membership will expire."

  - name: "notes"
    type: "string"
    description: "Any notes about the membership."
---