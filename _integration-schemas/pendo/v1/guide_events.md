---
tap: "pendo"
version: "1"
key: "guide-event"

name: "guide_events"
doc-link: "https://developers.pendo.io/docs/?bash#guide-events"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/guide_events.json"
description: |
  The `{{ table.name }}` table contains info about guide events recorded in your {{ integration.display_name }} account.

  {{ event-replication-note }}

replication-method: "Key-based Incremental"

attribution-window: true

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "account_id"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "server"
    type: "string"
    primary-key: true
    description: ""

  - name: "remote_ip"
    type: "string"
    primary-key: true
    description: ""

  - name: "browser_time"
    type: "date-time"
    description: ""
    replication-key: true  

  - name: "visitor_id"
    type: "string"
    description: ""
    foreign-key-id: "visitor-id"

  - name: "account_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
        foreign-key-id: "account-id"

  - name: "app_id"
    type: "string"
    description: ""
    foreign-key-id: "app-id"

  - name: "country"
    type: "string"
    description: ""

  - name: "day"
    type: "date-time"
    description: "{{ day-event-rep-key-note }}"

  - name: "guide_id"
    type: "string"
    description: ""
    foreign-key-id: "guide-id"

  - name: "hour"
    type: "date-time"
    description: "{{ hour-event-rep-key-note }}"

  - name: "latitude"
    type: "number"
    description: ""

  - name: "load_time"
    type: "integer"
    description: ""

  - name: "longitude"
    type: "number"
    description: ""

  - name: "poll_id"
    type: "string"
    description: ""
    foreign-key-id: "poll-id"

  - name: "poll_response"
    type: "string"
    description: ""

  - name: "region"
    type: "string"
    description: ""

  - name: "server_name"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_agent"
    type: "string"
    description: ""
---