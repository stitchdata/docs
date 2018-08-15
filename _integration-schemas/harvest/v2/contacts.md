---
tap: "harvest"
version: "2.0"

name: "contacts"
doc-link: https://help.getharvest.com/api-v2/clients-api/clients/contacts/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/contacts.json
description: |
  The `contacts` table contains info about the client contacts in your Harvest account.

replication-method: "Key-based Incremental"
api-method:
  name: listAllContacts
  doc-link: https://help.getharvest.com/api-v2/clients-api/clients/contacts/#list-all-contacts

attributes:
  - name: "id"
    type: "integer"
    description: ""

  - name: "client_id"
    type: "integer"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "phone_office"
    type: "string"
    description: ""

  - name: "phone_mobile"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "created_at"
    type: "string"
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""

