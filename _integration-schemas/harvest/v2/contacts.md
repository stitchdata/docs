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
    description: "Unique ID for the contact."

  - name: "client_id"
    type: "integer"
    description: "The contact's client id."

  - name: "title"
    type: "string"
    description: "The title of the contact."

  - name: "first_name"
    type: "string"
    description: "The first name of the contact."

  - name: "last_name"
    type: "string"
    description: "The last name of the contact."

  - name: "email"
    type: "string"
    description: "The contact’s email address."

  - name: "phone_office"
    type: "string"
    description: "The contact’s office phone number."

  - name: "phone_mobile"
    type: "string"
    description: "The contact’s mobile phone number."

  - name: "fax"
    type: "string"
    description: "The contact’s fax number."

  - name: "created_at"
    type: "string"
    description: "Date and time the contact was created."

  - name: "updated_at"
    type: "string"
    description: "Date and time the contact was last updated."

