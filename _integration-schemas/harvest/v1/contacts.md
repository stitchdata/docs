---
tap: "harvest"
version: "1.0"

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
    primary-key: true
    description: "The contact ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the contact was updated."

  - name: "client_id"
    type: "integer"
    description: "The ID of the client the contact is a part of."
    # foreign-keys:
    #   - table: "clients"
    #     attribute: "id"
    #   - table: "projects"
    #     attribute: "client_id"

  - name: "first_name"
    type: "string"
    description: "The contact's first name."

  - name: "last_name"
    type: "string"
    description: "The contact's last name."

  - name: "email"
    type: "string"
    description: "The email address for the contact."

  - name: "phone_office"
    type: "string"
    description: "The phone number for the contact."

  - name: "phone_mobile"
    type: "string"
    description: "The mobile phone for the contact."

  - name: "fax"
    type: "string"
    description: "The fax number for the contact."

  - name: "title"
    type: "string"
    description: "The contact's title. Ex: `Mrs`"

  - name: "created_at"
    type: "date-time"
    description: "The time the contact was created."
---
