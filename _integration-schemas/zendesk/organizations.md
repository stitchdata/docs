---
tap: "zendesk"
version: "1.0"

name: "organizations"
doc-link: https://developer.zendesk.com/rest_api/docs/core/organizations
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/organizations.json
description: |
  The `organizations` table contains information about the organizations your end-users belong to. 

  **Note**: Retrieving organization data requires Zendesk Admin permissions.

replication-method: "Key-based Incremental"

api-method:
  name: Incremental organization export
  doc-link: https://developer.zendesk.com/rest_api/docs/core/incremental_export#incremental-organization-export

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The organization ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the organization was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the organization was last updated."

  - name: "details"
    type: "string"
    description: "Details about the organization, such as its address."

  - name: "domain_names"
    type: "array"
    description: "The domain names associated with the organization."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The domain name associated with the organization."

  - name: "external_id"
    type: "string"
    description: "The unique external ID to associated organizations to an external record."

  - name: "group_id"
    type: "integer"
    description: "The group ID associated with the organization. New tickets from users in this organization are automatically put in this group."
    foreign-key: true

  - name: "name"
    type: "string"
    description: "The name of the organization."

  - name: "notes"
    type: "string"
    description: "Notes about the organization."

  - name: "organization_fields"
    type: "object"
    description: "Details about this organization's custom fields."
    object-attributes:
      - name: "id"
        type: "integer"
        description: "The ID of the custom organization field."

      - name: "updated_at"
        type: "date-time"
        description: "The last time the field was updated."

      - name: "active"
        type: "boolean"
        description: "If `true`, the field is available for use."

      - name: "created_at"
        type: "date-time"
        description: "The time the field was created."

      - name: "description"
        type: "string"
        description: "The description of the custom organization field's purpose."

      - name: "key"
        type: "string"
        description: "The unique key that identifies the custom organization field."

      - name: "position"
        type: "integer"
        description: "The ordering of the field relative to other fields."

      - name: "raw_description"
        type: "string"
        description: "The dynamic content placeholder, if present, or the `description` value, if not."

      - name: "raw_title"
        type: "string"
        description: "The dynamic content placeholder, if present, or the `title` value, if not."

      - name: "regexp_for_validation"
        type: "string"
        description: "The validation pattern for a field value to be deemed valid."

      - name: "system"
        type: "boolean"
        description: "If `true`, only the `active` and `position` values of this field can be changed."

      - name: "tag"
        type: "string"
        description: "The tag associated with a field type of `checkbox`."

      - name: "title"
        type: "string"
        description: "The title of the custom organization field."

      - name: "type"
        type: "string"
        description: |
          The type of the custom organization field. Possible values are:

          - `checkbox`
          - `date`
          - `decimal`
          - `dropdown`
          - `integer`
          - `regexp`
          - `text`
          - `textarea`

      - name: "url"
        type: "string"
        description: "The API URL associated with the custom organization field."

      # - name: "custom_field_options"
      #   type: "array"
      #   description: "For `type: dropdown` fields, the options presented in the dropdown."
      #   array-attributes:
      #     - name: "value"
      #       type: "string"
      #       description: "The dropdown field option."

  - name: "shared_comments"
    type: "boolean"
    description: "If `true`, end users in this organization are able to see each other's comments on tickets."

  - name: "shared_tickets"
    type: "boolean"
    description: "If `true`, end users in this organization are able to see each other's tickets."

  - name: "tags"
    type: "array"
    description: "The tags associated with the organization."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The tag associated with the organization."
        foreign-key: true
        table: "tags"

  - name: "url"
    type: "string"
    description: "The API URL of the organization."
---
