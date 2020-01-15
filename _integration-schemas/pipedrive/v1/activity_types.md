---
tap: "pipedrive"
version: "1"
key: "activity-type"

name: "activity_types"
doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/ActivityTypes"
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/activity_types.json"
description: |
  The `{{ table.name }}` table contains info about the different kinds of activities in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get all activity types"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/ActivityTypes/get_activityTypes"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The activity type ID."
    #foreign-key-id: "activity-type-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the activity type was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "color"
    type: "string"
    description: ""

  - name: "icon_key"
    type: "string"
    description: ""

  - name: "is_custom_flag"
    type: "boolean"
    description: ""

  - name: "key_string"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "order_nr"
    type: "integer"
    description: ""
---