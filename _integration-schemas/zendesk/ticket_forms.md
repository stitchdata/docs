---
tap: "zendesk"
version: "1.0"

name: "ticket_forms"
doc-link: https://developer.zendesk.com/rest_api/docs/core/ticket_forms
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/ticket_forms.json
description: |
  The `ticket_forms` table contains info about the ticket forms in your Zendesk account.

  **Note**: Replicating ticket form requires that you be on an Enterprise Zendesk plan or a Professional plan with the corresponding add-on, and have Admin permissions in Zendesk.

replication-method: "Key-based Incremental"

api-method:
  name: List ticket forms
  doc-link: https://developer.zendesk.com/rest_api/docs/core/ticket_forms#list-ticket-forms

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ticket form ID."
    foreign-key-id: "ticket-form-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the ticket form was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the ticket form was created."

  - name: "name"
    type: "string"
    description: "The name of the ticket form."

  - name: "raw_name"
    type: "string"
    description: "The dynamic content placeholder, if present. If not, the `name` value."

  - name: "display_name"
    type: "string"
    description: "The name of the ticket form that is displayed to the end user."

  - name: "raw_display_name"
    type: "string"
    description: "The dynamic content placeholder, if present. If not, the `display_name` value."

  - name: "url"
    type: "string"
    description: "The url of the ticket form."

  - name: "position"
    type: "integer"
    description: "The relative position of the ticket form."

  - name: "active"
    type: "boolean"
    description: "If `true`, the ticket form is set to active."

  - name: "default"
    type: "boolean"
    description: "If `true`, the ticket form is the default form for the account."

  - name: "end_user_available"
    type: "boolean"
    description: "If `true`, the ticket form is visible to the end user"

  - name: "in_all_brands"
    type: "boolean"
    description: "If `true`, the ticket form is available for use in all brands on the account"

  - name: "ticket_field_ids"
    type: "array"
    description: "IDs of all ticket fields which are in this ticket form."
    array-attributes:
      - name: "value"
        type: "integer"
        description: "The ID of the ticket field."
        foreign-key-id: "ticket-field-id"

  - name: "restricted_brand_ids"
    type: "array"
    description: "IDs of all brands that this ticket form is restricted to."
    array-attributes:
      - name: "value"
        type: "integer"
        description: "The ID of the brand."
---
