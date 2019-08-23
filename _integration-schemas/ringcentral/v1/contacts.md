---
tap: "ringcentral"
version: "1.0"
key: ""

name: "contacts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ringcentral/blob/master/tap_ringcentral/schemas/contacts.json"
description: |
  The `{{ table.name }}` contains info about 

replication-method: "Key-based Incremental"

replication-key:
  name: "dateFrom : dateTo"

api-method:
    name: "Get Corporate Directory Entry"
    doc-link: "https://developers.ringcentral.com/api-reference/Internal-Contacts/readDirectoryEntry"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "account"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "extensionNumber"
    type: "integer"
    description: ""

  - name: "firstName"
    type: "string"
    description: ""

  - name: "jobTitle"
    type: "string"
    description: ""

  - name: "lastName"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "phoneNumbers"
    type: "array"
    description: ""
    subattributes:
      - name: "phoneNumber"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""

      - name: "usageType"
        type: "string"
        description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---