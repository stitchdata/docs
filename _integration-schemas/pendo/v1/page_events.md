---
tap: "pendo"
version: "1"
key: "page-event"

name: "page_events"
doc-link: "https://developers.pendo.io/docs/?bash#events"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/page_events.json"
description: |
  The `{{ table.name }}` table contains info about page events recorded in your {{ integration.display_name }} account.

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

  - name: "visitor_id"
    type: "string"
    description: ""
    foreign-key-id: "visitor-id"

  - name: "app_id"
    type: "string"
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

  - name: "page_id"
    type: "string"
    description: ""
    foreign-key-id: "page-id"

  - name: "parameters"
    type: "string"
    description: ""

  - name: "user_agent"
    type: "string"
    description: ""
---