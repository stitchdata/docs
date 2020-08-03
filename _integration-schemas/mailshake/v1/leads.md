---
tap: "mailshake"
version: "1"
key: "lead"

name: "leads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailshake/blob/master/tap_mailshake/schemas/leads.json"
description: |
  The `{{ table.name }}` table contains info about the leads in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List leads"
  doc-link: "https://api-docs.mailshake.com/?shell#List59"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "lead-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "assignedTo"
    type: "object"
    description: ""
    subattributes:
      - name: "emailAddress"
        type: "string"
        description: ""

      - name: "first"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "team-member-id"

      - name: "last"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

  - name: "campaign"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "date-time"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "campaign-id"

      - name: "object"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""

  - name: "lastStatusChangeDate"
    type: "date-time"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "openedDate"
    type: "date-time"
    description: ""

  - name: "recipient"
    type: "object"
    description: ""
    subattributes:
      - name: "created"
        type: "date-time"
        description: ""

      - name: "emailAddress"
        type: "string"
        description: ""

      - name: "fields"
        type: "object"
        description: ""
        subattributes: 

      - name: "first"
        type: "string"
        description: ""

      - name: "fullName"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "recipient-id"

      - name: "last"
        type: "string"
        description: ""

      - name: "object"
        type: "string"
        description: ""

  - name: "status"
    type: "string"
    description: ""
---