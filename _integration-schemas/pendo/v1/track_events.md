---
tap: "pendo"
version: "1"
key: "track-event"

name: "track_events"
doc-link: "https://developers.pendo.io/docs/?bash#track-events"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/track_events.json"
description: |
  The `{{ table.name }}` table contains info about the track events recorded in your {{ integration.display_name }} account.

  {{ event-replication-note }}

replication-method: "Key-based Incremental"
replication-key:
  name: "day or hour"

attribution-window: true

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "account_id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "remote_ip"
    type: "string"
    primary-key: true
    description: ""

  - name: "server"
    type: "string"
    primary-key: true
    description: ""

  - name: "visitor_id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "visitor-id"

  - name: "app_id"
    type: "number"
    description: ""
    foreign-key-id: "app-id"

  - name: "day"
    type: "date-time"
    description: "{{ day-event-rep-key-note }}"

  - name: "hour"
    type: "date-time"
    description: "{{ hour-event-rep-key-note }}"

  - name: "num_events"
    type: "integer"
    description: ""

  - name: "num_minutes"
    type: "integer"
    description: ""

  - name: "properties"
    type: "object"
    description: ""
    subattributes:
      - name: "android"
        type: "boolean"
        description: ""

      - name: "any"
        type: "boolean"
        description: ""

      - name: "apple"
        type: "boolean"
        description: ""

      - name: "phone"
        type: "boolean"
        description: ""

      - name: "table"
        type: "boolean"
        description: ""

  - name: "track_type_id"
    type: "string"
    description: ""
    foreign-key-id: "track-type-id"

  - name: "user_agent"
    type: "string"
    description: ""
---