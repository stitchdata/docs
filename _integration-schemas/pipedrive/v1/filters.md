---
tap: "pipedrive"
version: "1.0"
key: "filter"

name: "filters"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/filters.json"
description: |
  The `{{ table.name }}` table contains info about the filters, or data validation conditions, used in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get all filters"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Filters"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The filter ID."
   # foreign-key-id: "filter-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the filter was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "custom_view_id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "temporary_flag"
    type: "boolean"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "visible_to"
    type: "string"
    description: ""
---