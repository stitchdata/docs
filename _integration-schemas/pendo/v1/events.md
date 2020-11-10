---
tap: "pendo"
version: "1"
key: "event"

name: "events"
doc-link: "https://developers.pendo.io/docs/?bash#events"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about events recorded in your {{ integration.display_name }} account.

  {% capture event-replication-note %}
  **Note**: The **Lookback Window** and **Period** settings you define [during setup](#add-stitch-data-source) determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.
  {% endcapture %}

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

  - name: "day"
    type: "date-time"
    description: |
      {% capture day-event-rep-key-note %}If the **Period** setting is set to `Day`, this field will be used as the table's Replication Key.{% endcapture %}

      {{ day-event-rep-key-note }}

  - name: "hour"
    type: "date-time"
    description: |
      {% capture hour-event-rep-key-note %}If the **Period** setting is set to `Hour`, this field will be used as the table's Replication Key.{% endcapture %}

      {{ hour-event-rep-key-note }}

  - name: "app_id"
    type: "string"
    description: ""
    foreign-key-id: "app-id"

  - name: "feature_id"
    type: "string"
    description: ""
    foreign-key-id: "feature-id"

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