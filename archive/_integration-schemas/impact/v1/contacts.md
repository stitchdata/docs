---
tap: "impact"
version: "1"
key: "contact"

name: "contacts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/contacts.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's contacts.

replication-method: "Full Table"

api-method:
  name: "Get contacts"
  doc-link: "https://developer.impact.com/default#operations-Contacts-GetContacts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "contact-id"

  - name: "accounts"
    type: "array, object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "cellphone_number"
    type: "string"
    description: ""

  - name: "cellphone_number_country"
    type: "string"
    description: ""

  - name: "email_address"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "labels"
    type: "array"
    description: ""
    subattribute:
      - name: "value"
        type: "string"
        description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "profile_image"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""

  - name: "work_phone_number"
    type: "integer"
    description: ""

  - name: "work_phone_number_country"
    type: "string"
    description: ""
---