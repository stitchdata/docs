---
tap: "pipedrive"
version: "1"
key: "activity"

name: "activities"
doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/activities.json"
description: |
  The `{{ table.name }}` table contains info about recent activities  - calls, tasks, lunches, etc. - recorded in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent activities"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The activity ID."
    foreign-key-id: "activity-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the activity was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "assigned_to_user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "company_id"
    type: "integer"
    description: ""

  - name: "created_by_user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "deal_dropbox_bcc"
    type: "string"
    description: ""

  - name: "deal_id"
    type: "integer"
    description: ""

  - name: "deal_title"
    type: "string"
    description: ""

  - name: "done"
    type: "boolean"
    description: ""

  - name: "due_date"
    type: "string"
    description: ""

  - name: "due_time"
    type: "string"
    description: ""

  - name: "duration"
    type: "string"
    description: ""

  - name: "gcal_event_id"
    type: "string"
    description: ""

  - name: "google_calendar_etag"
    type: "string"
    description: ""

  - name: "google_calendar_id"
    type: "string"
    description: ""

  - name: "marked_as_done_time"
    type: "date-time"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "org_id"
    type: "integer"
    description: ""
    foreign-key-id: "organization-id"

  - name: "org_name"
    type: "string"
    description: ""

  - name: "owner_name"
    type: "string"
    description: ""

  - name: "participants"
    type: "array"
    description: ""
    subattributes:
      - name: "person_id"
        type: "integer"
        description: ""
        foreign-key-id: "person-id"

      - name: "primary_flag"
        type: "boolean"
        description: ""

  - name: "person_dropbox_bcc"
    type: "string"
    description: ""

  - name: "person_id"
    type: "integer"
    description: ""
    foreign-key-id: "person-id"

  - name: "person_name"
    type: "string"
    description: ""

  - name: "reference_id"
    type: "integer"
    description: ""

  - name: "reference_type"
    type: "string"
    description: ""

  - name: "subject"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"
---