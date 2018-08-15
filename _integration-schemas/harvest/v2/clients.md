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
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "address"
    type: "string"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""

