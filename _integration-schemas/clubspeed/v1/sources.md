---
tap: "clubspeed"
version: "1"

name: "sources"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/sources.json"
description: |
  The `{{ table.name }}` table contains info about how customers find and register at venues.

replication-method: "Full Table"

attributes:
  - name: "sourceId"
    type: "integer"
    primary-key: true
    description: "The source ID."
    foreign-key-id: "source-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the source has been soft deleted."

  - name: "enabled"
    type: "boolean"
    description: "Indicates whether the source is currently enabled."

  - name: "locationId"
    type: "integer"
    description: "The ID of the venue location the source applies to."

  - name: "name"
    type: "string"
    description: "The name of the source."

  - name: "seq"
    type: "integer"
    description: "The sequence in which the source should display in a dropdown."
---