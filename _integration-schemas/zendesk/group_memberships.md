---
tap: "zendesk"
version: "1.0"

name: "group_memberships"
doc-link: https://developer.zendesk.com/rest_api/docs/support/group_memberships
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/group_memberships.json
description: |
  The `{{ table.name }}` table contains info about the groups your {{ integration.display_name }} agents are members of.

  **Note**: Retrieving group membership data requires {{ integration.display_name }} Agent or Admin permissions.

  #### Deleted group memberships

  As {{ integration.display_name }}'s API doesn't currently provide a method for identifying deleted group memberships, we recommend periodically dropping this table and allowing Stitch to re-create it. Currently, dropping and re-populating the table is the only way to detect deletions.

replication-method: "Key-based Incremental"

api-method:
  name: List memberships
  doc-link: https://developer.zendesk.com/rest_api/docs/support/group_memberships#list-memberships

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group membership ID."
    # foreign-key-id: "group-membership-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the membership was last updated."

  - name: "user_id"
    type: "integer"
    description: "The ID of the agent."
    foreign-key-id: "user-id"

  - name: "group_id"
    type: "integer"
    description: "The ID of the group."
    foreign-key-id: "group-id"

  - name: "default"
    type: "boolean"
    description: "If `true`, tickets designed directly to the agent assume this membership's group."

  - name: "created_at"
    type: "date-time"
    description: "The time the membership was created."

  - name: "url"
    type: "string"
    description: "The API URL of this membership record."
---