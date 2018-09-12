---
tap: "harvest-forecast"
version: "1.0"

name: "people"
doc-link:
singer-schema: https://github.com/singer-io/tap-harvest-forecast/blob/master/tap_harvest_forecast/schemas/people.json
description: |
  The `{{ table.name }}` table contains info about the people in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The person ID."
    foreign-key-id: "person-id"

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The last time the person was updated."

  - name: "admin"
    type: "boolean"
    description: "If `true`, the person is an admin in {{ integration.display_name }}."

  - name: "archived"
    type: "boolean"
    description: "If `true`, the person has been archived."

  - name: "avatar_url"
    type: "string"
    description: "The full URL of the avatar associated with the person."

  - name: "color_blind"
    type: "string"
    description: "Indicates if the person uses {{ integration.display_name }}'s color blind-friendly version of the heat map feature."

  - name: "email"
    type: "string"
    description: "The email address associated with the person."

  - name: "first_name"
    type: "string"
    description: "The person's first name."

  - name: "harvest_user_id"
    type: "integer"
    description: "The ID of the person in Harvest."

  - name: "last_name"
    type: "string"
    description: "The person's last name."

  - name: "login"
    type: "string"
    description: ""

  - name: "personal_feed_token_id"
    type: "integer"
    description: ""

  - name: "roles"
    type: "array"
    description: "A list of the roles assigned to the person."
    array-attributes: 
      - name: "value"
        type: "string"
        description: "The name of the role assigned to the person."

  - name: "subscribed"
    type: "boolean"
    description: "If `true`, the person is subscribed to the weekly schedule digest."

  - name: "updated_by_id"
    type: "string"
    description: "The ID of the person who last updated the person."
    foreign-key-id: "person-id"

  - name: "weekly_capacity"
    type: "integer"
    description: "The total number of hours the person is available during the week."

  - name: "working_days"
    type: "object"
    description: "Details about the person's availability during the week."
    object-attributes: 
      - name: "monday"
        type: "boolean"
        description: &working-days |
          If `true`, the person is available to work on {{ subattribute.name | capitalize | append: "s" }}.

      - name: "tuesday"
        type: "boolean"
        description: *working-days

      - name: "wednesday"
        type: "boolean"
        description: *working-days

      - name: "thursday"
        type: "boolean"
        description: *working-days

      - name: "friday"
        type: "boolean"
        description: *working-days

      - name: "saturday"
        type: "boolean"
        description: *working-days

      - name: "sunday"
        type: "boolean"
        description: *working-days
---