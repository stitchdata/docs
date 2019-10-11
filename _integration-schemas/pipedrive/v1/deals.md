---
tap: "pipedrive"
version: "1.0"
key: "deal"

name: "deals"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/dynamic_typing/deals.json"
description: |
  The `{{ table.name }}` table contains info about updates made recently to the deals in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent deals"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The deal ID."
    foreign-key-id: "deal-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the deal was last updated."

  - name: "active"
    type: "boolean"
    description: ""

  - name: "activities_count"
    type: "integer"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "cc_email"
    type: "string"
    description: ""

  - name: "close_time"
    type: "date-time"
    description: ""

  - name: "creator_user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "currency"
    type: "string"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "done_activities_count"
    type: "integer"
    description: ""

  - name: "email_messages_count"
    type: "integer"
    description: ""

  - name: "expected_close_date"
    type: "string"
    description: ""

  - name: "files_count"
    type: "integer"
    description: ""

  - name: "first_won_time"
    type: "date-time"
    description: ""

  - name: "followers_count"
    type: "integer"
    description: ""

  - name: "formatted_value"
    type: "string"
    description: ""

  - name: "formatted_weighted_value"
    type: "string"
    description: ""

  - name: "last_activity_date"
    type: "string"
    description: ""

  - name: "last_activity_id"
    type: "integer"
    description: ""
    foreign-key-id: "activity-id"

  - name: "last_incoming_mail_time"
    type: "date-time"
    description: ""

  - name: "last_outgoing_mail_time"
    type: "date-time"
    description: ""

  - name: "lost_reason"
    type: "string"
    description: ""

  - name: "lost_time"
    type: "date-time"
    description: ""

  - name: "next_activity_date"
    type: "string"
    description: ""

  - name: "next_activity_duration"
    type: "string"
    description: ""

  - name: "next_activity_id"
    type: "integer"
    description: ""
    foreign-key-id: "activity-id"

  - name: "next_activity_note"
    type: "string"
    description: ""

  - name: "next_activity_subject"
    type: "string"
    description: ""

  - name: "next_activity_time"
    type: "string"
    description: ""

  - name: "next_activity_type"
    type: "string"
    description: ""

  - name: "notes_count"
    type: "integer"
    description: ""

  - name: "org_hidden"
    type: "boolean"
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

  - name: "participants_count"
    type: "integer"
    description: ""

  - name: "person_hidden"
    type: "boolean"
    description: ""

  - name: "person_id"
    type: "integer"
    description: ""

  - name: "person_name"
    type: "string"
    description: ""

  - name: "pipeline_id"
    type: "integer"
    description: ""
    foreign-key-id: "pipeline-id"

  - name: "probability"
    type: "number"
    description: ""

  - name: "products_count"
    type: "integer"
    description: ""

  - name: "reference_activities_count"
    type: "integer"
    description: ""

  - name: "rotten_time"
    type: "date-time"
    description: ""

  - name: "stage_change_time"
    type: "date-time"
    description: ""

  - name: "stage_id"
    type: "integer"
    description: ""
    foreign-key-id: "stage-id"

  - name: "stage_order_nr"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "undone_activities_count"
    type: "integer"
    description: ""

  - name: "user_id"
    type: "integer"
    description: ""
    foreign-key-id: "user-id"

  - name: "value"
    type: "number"
    description: ""

  - name: "visible_to"
    type: "string"
    description: ""

  - name: "weighted_value"
    type: "number"
    description: ""

  - name: "won_time"
    type: "date-time"
    description: ""
---