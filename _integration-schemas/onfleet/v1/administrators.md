---
tap: "onfleet"
version: "1.0"

name: "administrators"
doc-link: "http://docs.onfleet.com/docs/administrators#list-administrators"
singer-schema: "https://github.com/singer-io/tap-onfleet/blob/master/tap_onfleet/schemas/administrators.json"
description: |
  The `{{ table.name }}` table contains info about the administrators in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List administrators"
    doc-link: "http://docs.onfleet.com/docs/administrators#list-administrators"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The administrator ID."
    foreign-key-id: "administrator-id"

  - name: "timeLastModified"
    type: "date-time"
    replication-key: true
    description: "The time the administrator was last modified."

  - name: "email"
    type: "string"
    description: "The administrator's email address."

  - name: "isActive"
    type: "boolean"
    description: "Indicates if the administrator is active."

  - name: "metadata"
    type: "array"
    description: "Metadata about the administrator."
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "name"
    type: "string"
    description: "The complete name of the administrator."

  - name: "organization"
    type: "string"
    description: "The ID of the organization the administrator is associated with."
    foreign-key-id: "organization-id"

  - name: "phone"
    type: "string"
    description: "The administrator's phone number."

  - name: "timeCreated"
    type: "date-time"
    description: "The time the administrator was created."

  - name: "type"
    type: "string"
    description: |
      The type of the administrator. Possible values are:

      - `super` - The administrator is a super administrator. Each {{ integration.display_name }} will only have one administrator of this type.
      - `standard` - The administrator is a dispatcher.
---