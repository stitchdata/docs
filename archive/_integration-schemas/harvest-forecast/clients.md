---
tap: "harvest-forecast"
version: "1"

name: "clients"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/clients.json
description: |
  The `{{ table.name }}` table contains info about the clients in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The client ID."
    foreign-key-id: "client-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the client was last updated."

  - name: "archived"
    type: "boolean"
    description: "If `true`, the client has been archived."

  - name: "harvest_id"
    type: "integer"
    description: "The ID of the client in Harvest."

  - name: "name"
    type: "string"
    description: "The name of the client."

  - name: "updated_by_id"
    type: "integer"
    description: "The ID of the person who last updated the client."
    foreign-key-id: "person-id"
---
