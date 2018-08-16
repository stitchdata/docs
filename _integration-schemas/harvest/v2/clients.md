---
tap: "harvest"
version: "2.0"

name: "clients"
doc-link: https://help.getharvest.com/api-v2/clients-api/clients/clients/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/clients.json
description: |
  The `clients` table contains info about the clients in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: listAllClients
  doc-link: https://help.getharvest.com/api-v2/clients-api/clients/clients/#list-all-clients

attributes:
  - name: "id"
    type: "integer"
    description: "Unique ID for the client."

  - name: "name"
    type: "string"
    description: "A textual description of the client."

  - name: "is_active"
    type: "boolean"
    description: "Whether the client is active or archived."

  - name: "address"
    type: "string"
    description: "The physical address for the client."

  - name: "currency"
    type: "string"
    description: "The currency code associated with this client."

  - name: "created_at"
    type: "string"
    description: "Date and time the client was created."

  - name: "updated_at"
    type: "string"
    description: "Date and time the client was last updated."

