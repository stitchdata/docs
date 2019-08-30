---
tap: "ringcentral"
version: "1.0"
key: ""

name: "contacts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ringcentral/blob/master/tap_ringcentral/schemas/contacts.json"
description: |
  The `{{ table.name }}` contains info about corporate users of federated accounts.

replication-method: "Full Table"

api-method:
    name: "Get Corporate Directory Entry"
    doc-link: "https://developers.ringcentral.com/api-reference/Internal-Contacts/readDirectoryEntry"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "account"
    type: "object"
    description: "Details about the owning account."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The owning account ID."

  - name: "email"
    type: "string"
    description: "The contact's email address."

  - name: "extensionNumber"
    type: "integer"
    description: "The contact's phone number extension."

  - name: "firstName"
    type: "string"
    description: "The contact's first name."

  - name: "jobTitle"
    type: "string"
    description: "The contact's job title."

  - name: "lastName"
    type: "string"
    description: "The contact's last name."

  - name: "name"
    type: "string"
    description: "The contact's name, for non-user extensions."

  - name: "phoneNumbers"
    type: "array"
    description: "The contact's phone numbers."
    subattributes:
      - name: "phoneNumber"
        type: "string"
        description: "The phone number."

      - name: "type"
        type: "string"
        description: "The phone number type."

      - name: "usageType"
        type: "string"
        description: "The phone number's category."

  - name: "status"
    type: "string"
    description: "The contact's status."

  - name: "type"
    type: "string"
    description: "The contact's type."
---