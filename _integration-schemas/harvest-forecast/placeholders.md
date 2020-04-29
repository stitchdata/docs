---
tap: "harvest-forecast"
version: "1"
key: "placeholders"

name: "placeholders"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/placeholders.json"
description: "The `{{ table.name }}` table contains info about the placeholders in your {{ integration.display_name }} account."

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The placeholder ID."
    foreign-key-id: "placeholder-id"

  - name: "updated_at"
    type: "date-time"
    description: "The date the placeholder was last updated."
    replication-key: true

  - name: "archived"
    type: "boolean"
    description: "Whether or not the placeholder has been archived."

  - name: "name"
    type: "string"
    description: "The placeholder name."

  - name: "roles"
    type: "array"
    description: "Details about the role."
    subattributes:
      - name: "value"
        type: "string"
        description: "The value of the role."
        foreign-key-id: "role-id"

  - name: "updated_by_id"
    type: "integer"
    description: "The ID of the person who updated the placeholder."
    foreign-key-id: "person-id"
---
