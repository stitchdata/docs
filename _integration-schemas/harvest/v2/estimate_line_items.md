---
tap: "harvest"
version: "2.0"

name: "contacts"
doc-link: http://help.getharvest.com/api-v1/clients-api/clients/using-the-client-contacts-api/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/contacts.json
description: |
  The `contacts` table contains info about the client contacts in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: getAllContacts
  doc-link: http://help.getharvest.com/api-v1/clients-api/clients/using-the-client-contacts-api/#get-all-contacts

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "estimate_id"
    type: "integer"
    description: ""

  - name: "kind"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "unit_price"
    type: "number"
    description: ""

  - name: "amount"
    type: "number"
    description: ""

  - name: "taxed"
    type: "boolean"
    description: ""

  - name: "taxed2"
    type: "boolean"
    description: ""

