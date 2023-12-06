---
tap: "zendesk"
version: "1"

name: "ticket_fields"
doc-link: https://developer.zendesk.com/rest_api/docs/support/ticket_fields
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/ticket_fields.json
description: |
  The `{{ table.name }}` table contains info about the basic text and custom ticket fields in your {{ integration.display_name }} account.

  **Note**: Retrieving ticket metric data requires {{ integration.display_name }} Agent or Admin permissions.

replication-method: "Key-based Incremental"

api-method:
  name: List ticket fields
  doc-link: https://developer.zendesk.com/rest_api/docs/support/ticket_fields#list-ticket-fields

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ticket field ID."
    foreign-key-id: "ticket-field-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the ticket field was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the ticket field was created."

  - name: "title_in_portal"
    type: "string"
    description: "The title of the ticket field when shown to end users."

  - name: "visible_in_portal"
    type: "boolean"
    description: "If `true`, the ticket field is visible to end users."

  - name: "collapsed_for_agents"
    type: "boolean"
    description: "If `true`, the ticket field is hidden alongside infrequently used fields by default."

  - name: "regexp_for_validation"
    type: "string"
    description: "The validation pattern for a value in the ticket field to be deemed valuable."

  - name: "title"
    type: "string"
    description: "The title of the ticket field."

  - name: "position"
    type: "integer"
    description: "The relative position of the ticket."

  - name: "type"
    type: "string"
    description: |
      The type of the ticket field. Possible values:

      - `checkbox`
      - `date`
      - `decimal`
      - `integer`
      - `regexp`
      - `tagger`
      - `text`
      - `textarea`

  - name: "editable_in_portal"
    type: "boolean"
    description: "If `true`, the ticket field is editable by end users."

  - name: "raw_title_in_portal"
    type: "string"
    description: "The dynamic content placeholder, if present. If not, the `title_in_portal` value."

  - name: "tag"
    type: "string"
    description: "The tag value to set for checkbox fields when checked."

  - name: "removable"
    type: "boolean"
    description: "If `true`, the ticket field isn't a system basic field that must be present on allt ickets for the account."

  - name: "active"
    type: "boolean"
    description: "If `true`, the field is available."

  - name: "url"
    type: "string"
    description: "The API URL for the ticket field."

  - name: "raw_title"
    type: "string"
    description: "The dynamic content placeholder, if present. If not, the `title` value."

  - name: "required"
    type: "boolean"
    description: "If `true`, the ticket field must have a value when updated by agents."

  - name: "description"
    type: "string"
    description: "The description of the ticket field shown to end users."

  - name: "raw_description"
    type: "string"
    description: "The dynamic content placeholder, if present, or the `description` value, if not."

  - name: "agent_description"
    type: "string"
    description: "The description of the ticket field that only agents can see."

  - name: "required_in_portal"
    type: "boolean"
    description: "If `true`, the ticket field must have a value when updated by end users."

  - name: "custom_field_options"
    type: "array"
    description: |
      Options for ticket fields with `type:"tagger"`.
    subattributes:
      - name: "id"
        type: "integer"
        description: "The ID of the custom ticket field."

      - name: "name"
        type: "string"
        description: "The name of the custom ticket field."

      - name: "value"
        type: "string"
        description: "The value of the custom ticket field."

      # - name: "default"
      #   type: "boolean"
      #   description: ""

      # - name: "raw_name"
      #   type: "string"
      #   description:
---