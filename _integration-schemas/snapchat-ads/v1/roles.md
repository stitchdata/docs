---
tap: "snapchat-ads"
version: "1"
key: ""

name: "roles"
doc-link: https://developers.snapchat.com/api/docs/?python#get-all-roles-in-organization
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/roles.json
description: "This stream retrieves all Roles assigned within an Organization"

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "id"
    primary-key: true
    type: "string"
    description: "Role Id"

    - name: "updated_at"
    type: "date-time"
    description: "Date and time at which the role was updated"

    - name: "created_at"
    type: "date-time"
    description: "Date and time at which the role was created"

    - name: "container_kind"
    type: "string"
    description: "Name of the Container to which the role is associated with. Example: AdAccounts, Organizations, Catalogs"

    - name: "container_id"
    type: "string"
    description: "Id of the Container."

    - name: "member_id"
    type: "string"
    description: "Id of the member"

    - name: "organization_id"
    type: "string"
    description: "Id of the Oranization"

    - name: "type"
    type: "string"
    description: "Different types of the roles. Example: Admin, Creative, General, Reports, Audience"
---