---
tap: "harvest"
# version:

name: "clients"
doc-link: http://help.getharvest.com/api-v1/clients-api/clients/using-the-clients-api/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/clients.json
description: |
  The `clients` table contains info about the clients in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: getAllClients
  doc-link: http://help.getharvest.com/api-v1/clients-api/clients/using-the-clients-api/#get-all-clients

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The client ID."
    # foreign-keys:
    #   - table: "contacts"
    #     attribute: "client_id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the client was updated."

  - name: "name"
    type: "string"
    description: "The client's name. Ex: `Stitch Data`"

  - name: "active"
    type: "boolean"
    description: "Indicates if the client is active or archived."

  - name: "currency"
    type: "string"
    description: "The currency denomination used by the client."

  - name: "highrise_id"
    type: "boolean"
    description: "The optional Highrise ID for the client, if using Harvest's legacy integration."

  - name: "cache_version"
    type: "integer"
    description: "The cache version for the client."

  - name: "created_at"
    type: "date-time"
    description: "The time the client was updated."

  - name: "currency_symbol"
    type: "string"
    description: "The symbol associated with the client's selected currency denomination."

  - name: "details"
    type: "string"
    description: "Additional details about the client, usually address information."

  - name: "default_invoice_timeframe"
    type: "string"
    description: "The default invoice timeframe for the client."

  - name: "last_invoice_kind"
    type: "string"
    description: "The type of the last invoice."
---