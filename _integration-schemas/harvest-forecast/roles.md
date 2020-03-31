---
tap: "harvest-forecast"
version: "1"
key: "roles"

name: "roles"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/roles.json"
description: "The `{{ table.name }}` table contains info about the roles in your {{ integration.display_name }} account."

replication-method: "Full Table"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The role ID."
    foreign-key-id: "role-id"

  - name: "harvest_role_id"
    type: "integer"
    description: "The ID of the role in Harvest."
  
  - name: "name"
    type: "string"
    description: "The name of the role"

  - name: "person_ids"
    type: "array"
    description: "Details about the person IDs."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The person ID"
        foreign-key-id: "person-id"

  - name: "placeholder_ids"
    type: "array"
    description: "Details about the placeholder IDs."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The placeholder ID."
        foreign-key-id: "placeholder-id"
---
