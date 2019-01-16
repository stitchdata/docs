---
tap: "zendesk"
version: "1.0"

name: "macros"
doc-link: https://developer.zendesk.com/rest_api/docs/core/macros
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/macros.json
description: |
  The `macros` table contains info about the macros in your Zendesk account. Macros are actions defined by you that modify the values of a ticket’s fields.

  **Note**: Retrieving macro data requires Zendesk Agent or Admin permissions.

replication-method: "Key-based Incremental"

api-method:
  name: List macros
  doc-link: https://developer.zendesk.com/rest_api/docs/core/macros#list-macros

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The macro ID."
    # foreign-key-id: "macro-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the macro was last updated."

  - name: "actions"
    type: "array"
    description: "Details about what the macro does."
    array-attributes:
      - name: "field"
        type: "string"
        description: "The name of the ticket field to modify."

      - name: "value"
        type: "string"
        description: "The new value of the field."

  - name: "active"
    type: "boolean"
    description: "If `true`, the macro is active."

  - name: "created_at"
    type: "date-time"
    description: "The time the macro was created."

  - name: "description"
    type: "string"
    description: "The description of the macro."

  - name: "position"
    type: "integer"
    description: "The position of the macro."

  - name: "restriction"
    type: "object"
    description: "Details about who can access the macro."
    object-attributes:
      - name: "id"
        type: "integer"
        description: |
          The ID of the group or user who can access the macro.

          If everyone in the account can access the macro, this field will be null.
        foreign-key-id: "restriction-id"

      - name: "type"
        type: "string"
        description: |
          The type of restriction associated with the macro. Possible values are `Group` or `User`.

          If everyone in the account can access the macro, this field will be null.

      - name: "ids"
        type: "array"
        description: "The IDs of the groups or users who can access the macro."
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the group or user who can access the macro."
            foreign-key-id: "restriction-id"

  - name: "title"
    type: "string"
    description: "The title of the macro."

  - name: "url"
    type: "string"
    description: "The API URL of the macro."
---