---
tap: "zendesk"
version: "1"

name: "organizations"
doc-link: https://developer.zendesk.com/rest_api/docs/support/organizations
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/organizations.json
description: |
  The `{{ table.name }}` table contains information about the organizations your end-users belong to.

  #### Custom organization fields

  Stitch's {{ integration.display_name }} integration will replicate any custom fields associated with organization records.

  **Note**: Replicating organization custom fields requires that you be on a Team, Professional, or Enterprise {{ integration.display_name }} plan and have Admin permissions in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: Incremental organization export
  doc-link: https://developer.zendesk.com/rest_api/docs/support/incremental_export#incremental-organization-export

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The organization ID."
    foreign-key-id: "organization-id"

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
    subattributes:
      - name: "value"
        type: "string"
        description: "The domain name associated with the organization."

  - name: "external_id"
    type: "string"
    description: "The unique external ID to associated organizations to an external record."

  - name: "group_id"
    type: "integer"
    description: "The group ID associated with the organization. New tickets from users in this organization are automatically put in this group."
    foreign-key-id: "group-id"

  - name: "name"
    type: "string"
    description: "The name of the organization."

  - name: "notes"
    type: "string"
    description: "Notes about the organization."

  - name: "organization_fields"
    type: "object"
    description: "Details about this organization's custom fields."
    subattributes:
      - name: "[zendesk_field_name]"
        type: ""
        description: |
          For every not null custom field on an organization's record, a field named `{{ attribute.name | append: "__" | append: "[zendesk_field_name]" }}`, where `[zendesk_field_name]` is the name of the field in Zendesk, will be created.

          The data type of these fields will vary depending on the field's type in Zendesk. Generally:

          - Text-based fields will be `STRING`
          - Dropdown fields will be `STRING`
          - Numeric fields will be `INTEGER`
          - Decimal fields will be `NUMBER`
          - Checkbox fields will be `BOOLEAN`
          - Date fields will be `STRING`, formatted as `DATE-TIME`

  - name: "shared_comments"
    type: "boolean"
    description: "If `true`, end users in this organization are able to see each other's comments on tickets."

  - name: "shared_tickets"
    type: "boolean"
    description: "If `true`, end users in this organization are able to see each other's tickets."

  - name: "tags"
    type: "array"
    description: "The tags associated with the organization."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag associated with the organization."
        foreign-key-id: "tag-id"

  - name: "url"
    type: "string"
    description: "The API URL of the organization."
---