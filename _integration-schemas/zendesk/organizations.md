---
tap: "zendesk"
version: "1.0"

name: "organizations"
doc-link: https://developer.zendesk.com/rest_api/docs/core/organizations
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/organizations.json
description: |
  The `organizations` table contains company information about your end-users.

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

  - name: "group_id"
    type: "integer"
    description: "The group ID associated with the organization. New tickets from users in this organization are automatically put in this group."
    foreign-key: true

  - name: "created_at"
    type: "date-time"
    description: "The time the organization was last updated."

  - name: "tags"
    type: "array"
    description: "The IDs of the tags associated with the organization."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The ID of the tag associated with the organization."
        foreign-key: true
        table: "tags"

  - name: "shared_tickets"
    type: "boolean"
    description: "If `true`, end users in this organization are able to see each other's tickets."

  - name: "organization_fields"
    type: "object"
    description: "Details about this organization's custom fields."
    object-attributes:
      - name: ""
        type: ""
        description: "[TODO]"

  - name: "notes"
    type: "string"
    description: "Notes about the organization."

  - name: "domain_names"
    type: "array"
    description: "The domain names associated with the organization."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The domain name associated with the organization."

  - name: "shared_comments"
    type: "boolean"
    description: "If `true`, end users in this organization are able to see each other's comments on tickets."

  - name: "details"
    type: "string"
    description: "Details about the organization, such as its address."

  - name: "name"
    type: "string"
    description: "The name of the organization."

  - name: "external_id"
    type: "string"
    description: "The unique external ID to associated organizations to an external record."

  - name: "url"
    type: "string"
    description: "The API URL of the organization."
---