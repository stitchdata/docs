---
tap: "typeform"
version: "2"
key: "form"

name: "forms"
doc-link: "https://developer.typeform.com/responses/"
singer-schema: "https://github.com/singer-io/tap-typeform/blob/master/tap_typeform/schemas/forms.json"
description: |
  The `{{ table.name }}` table contains info about the forms (public and private) that are accesible by the user who authorized the integration in Stitch.

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve forms"
  doc-link: "https://developer.typeform.com/create/reference/retrieve-forms/"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The form ID."
    foreign-key-id: "form-id"

  - name: "last_updated_at"
    type: "string"
    replication-key: true
    description: "The time of the last update in the form."

  - name: "self"
    type: "object"
    description: "The URL for the typeform."
    subattributes: &href
      - name: "href"
        type: "string"
        description: ""

  - name: "settings"
    type: "object"
    description: ""
    subattributes:
      - name: "is_public"
        type: "boolean"
        description: ""

      - name: "is_trial"
        type: "boolean"
        description: ""

  - name: "theme"
    type: "object"
    description: "The URL for the theme the typeform uses."
    subattributes: *href

  - name: "title"
    type: "string"
    description: "The title of the form."

  - name: "type"
    type: "string"
    description: ""

  - name: "_links"
    type: "object"
    description: ""
    subattributes:
      - name: "display"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: "The time the form was created."
---