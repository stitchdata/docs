---
tap: "freshdesk"
version:

name: "groups"
doc-link: https://developers.freshdesk.com/api/#groups
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/groups.json
description: |
  The `{{ table.name }}` table contains info about the groups your agents belong to.

replication-method: "Key-based Incremental"
api-method:
  name: "listAllGroups"
  doc-link: https://developers.freshdesk.com/api/#list_all_groups

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The group ID."
    foreign-key-id: "group-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The timestamp when the group was last updated."

  - name: "agent_ids"
    type: "array"
    description: "IDs of the agents that belong to the group."
    subattributes:
      - name: "value"
        type: "integer"
        primary-key: true
        description: "The ID of an agent that belongs to the group."
        foreign-key-id: "agent-id"

  - name: "auto_ticket_assign"
    type: "boolean"
    description: "Indicates if automatic ticket assignment is enabled for the group."

  - name: "business_hour_id"
    type: "integer"
    description: "Unique ID of the business hour associated with the group."

  - name: "description"
    type: "string"
    description: "The description of the group."

  - name: "escalate_to"
    type: "integer"
    description: "The ID of the user to whom an escalation email is sent if a ticket is unassigned."

  - name: "name"
    type: "string"
    description: "The name of the group."

  - name: "unassigned_for"
    type: "string"
    description: |
      The time after which an escalation email is sent if a ticket remains unassigned. Possible values include:

      - `30m` for 30 minutes
      - `1h` for 1 hour
      - `2h` for 2 hours
      - `4h` for 4 hours
      - `8h` for 8 hours
      - `12h` for 12 hours
      - `1d` for 1 day
      - `2d` for 2 days
      - `3d` for 3 days

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the group was first created."
---