---
tap: "closeio"
version: "1"

name: "custom_fields"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-closeio/blob/master/tap_closeio/schemas/custom_fields.json"

description: |
  The `{{ table.name }}` table contains info about the custom fields in your {{ integration.display_name }} account.

  Custom fields allow you to store arbitrary data on leads in {{ integration.display_name }}. [Refer to {{ integration.display_name }}'s documentation](https://help.close.io/customer/portal/articles/1104820-custom-fields) for more info.

replication-method: "Key-based Incremental"

api-method:
  name: "List all custom fields for your organization"
  doc-link: "https://developer.close.io/#custom-fields-list-all-the-custom-fields-for-your-organization"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The custom field ID."
    # foreign-key-id: "custom-field-id"

  - name: "date_updated"
    type: "string"
    replication-key: true
    description: "The date the custom field was last updated."

  - name: "choices"
    type: "array"
    description: "For `choices` custom fields, a list of choices available for the custom field."
    subattributes:
      - name: "value"
        type: "string"
        description: "The choice available for the field."

  - name: "created_by"
    type: "string"
    description: "The ID of the user who created the custom field."
    foreign-key-id: "user-id"

  - name: "date_created"
    type: "string"
    description: "The date the custom field was created."

  - name: "editable_with_roles"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: "The name of the custom field."

  - name: "organization_id"
    type: "string"
    description: "The ID of the organization associated with the custom field."
    foreign-key-id: "organization-id"

  - name: "type"
    type: "string"
    description: |
      The type of the custom field. Possible values include:

      - `choices`
      - `date`
      - `date/time`
      - `hidden`
      - `number`
      - `text`
      - `user`

  - name: "updated_by"
    type: "string"
    description: "The ID of the user who last updated the custom field."
    foreign-key-id: "user-id"
---