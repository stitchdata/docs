---
tap: "harvest"
version: "2.0"

name: "contacts"
doc-link: https://help.getharvest.com/api-v2/clients-api/clients/contacts/
singer-schema: https://github.com/singer-io/tap-harvest/blob/master/tap_harvest/schemas/contacts.json
description: |
  The `{{ table.name }}` table contains info about the client contacts in your Harvest account.

replication-method: "Key-based Incremental"

api-method:
  name: listAllContacts
  doc-link: https://help.getharvest.com/api-v2/clients-api/clients/contacts/#list-all-contacts

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the contact was updated."

  - name: "client_id"
    type: "integer"
    description: "The contact's client id."
    foreign-key-id: "client-id"

  - name: "title"
    type: "string"
    description: "The title of the contact."

  - name: "first_name"
    type: "string"
    description: "The contact's first name."

  - name: "last_name"
    type: "string"
    description: "The contact's last name."

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
    type: "date-time"
    description: "The time the contact was created."
---