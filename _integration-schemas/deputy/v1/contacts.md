---
tap: "deputy"
version: "1"
key: "contact"

name: "contacts"
doc-link: "https://www.deputy.com/api-doc/Resources/Contact"

description: |
  The `{{ table.name }}` table contains info about contacts.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the contact was last modified."

  - name: "Phone1"
    type: "string"
    description: ""

  - name: "Phone2"
    type: "string"
    description: ""

  - name: "Phone3"
    type: "string"
    description: ""

  - name: "Fax"
    type: "string"
    description: ""

  - name: "Phone1Type"
    type: "string"
    description: ""

  - name: "Phone2Type"
    type: "string"
    description: ""

  - name: "Phone3Type"
    type: "string"
    description: ""

  - name: "PrimaryPhone"
    type: "integer"
    description: ""

  - name: "Email1"
    type: "string"
    description: ""

  - name: "Email2"
    type: "string"
    description: ""

  - name: "Email1Type"
    type: "string"
    description: ""

  - name: "Email2Type"
    type: "string"
    description: ""

  - name: "PrimaryEmail"
    type: "integer"
    description: ""

  - name: "Im1"
    type: "string"
    description: ""

  - name: "Im2"
    type: "string"
    description: ""

  - name: "Im1Type"
    type: "string"
    description: ""

  - name: "Im2Type"
    type: "string"
    description: ""

  - name: "Web"
    type: "string"
    description: ""

  - name: "Notes"
    type: "string"
    description: ""

  - name: "Saved"
    type: "boolean"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---