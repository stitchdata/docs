---
tap: "harvest"
version: "2"

name: "clients"
doc-link: https://help.getharvest.com/api-v2/clients-api/clients/clients/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/clients.json
description: |
  The `{{ table.name }}` table contains info about the clients in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: listAllClients
  doc-link: https://help.getharvest.com/api-v2/clients-api/clients/clients/#list-all-clients

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "Unique ID for the client."
    foreign-key-id: "client-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the client was updated."

  - name: "name"
    type: "string"
    description: "The client's name. Ex: `Stitch Data`"

  - name: "is_active"
    type: "boolean"
    description: "Indicates if the client is active or archived."

  - name: "address"
    type: "string"
    description: "The physical address for the client."

  - name: "currency"
    type: "string"
    description: "The currency denomination used by the client."

  - name: "created_at"
    type: "date-time"
    description: "The time the client was updated."
---