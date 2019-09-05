---
tap: "helpscout"
version: "1.0"

key: "mailbox-field"
name: "mailbox_fields"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-helpscout/blob/master/tap_helpscout/schemas/mailbox_fields.json"
description: |
  The `{{ table.name }}` table contains info about the custom fields associated with your {{ integration.display_name }} mailboxes.

replication-method: "Full Table"

api-method:
    name: "List mailbox custom fields"
    doc-link: "https://developer.helpscout.com/mailbox-api/endpoints/mailboxes/mailbox-fields/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The mailbox field ID."
    #foreign-key-id: "mailbox-field-id"

  - name: "mailbox_id"
    type: "integer"
    description: "The ID of the mailbox associated with the mailbox field."
    foreign-key-id: "mailbox-id"

  - name: "name"
    type: "string"
    description: " The name of the mailbox field."

  - name: "options"
    type: "array"
    description: "**Applicable when `type: dropdown`**. The options for the dropdown field."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The option ID."

      - name: "order"
        type: "integer"
        description: "The order the option is displayed in in {{ integration.display_name }}."

      - name: "label"
        type: "string"
        description: "The option label."

  - name: "order"
    type: "integer"
    description: "The order the mailbox field is displayed in in {{ integration.display_name }}."

  - name: "required"
    type: "boolean"
    description: "Indicates if the mailbox field is required."

  - name: "type"
    type: "string"
    description: "The type of the mailbox field."
---