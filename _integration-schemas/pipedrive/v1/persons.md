---
tap: "pipedrive"
version: "1.0"
key: "person"

name: "persons"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/dynamic_typing/persons.json"
description: |
  The `{{ table.name }}` table contains info about the recent persons in your {{ integration.display_name }} account. In {{ integration.display_name }}, a person represents a contact, or a customer you're doing a deal with.

replication-method: "Key-based Incremental"

api-method:
  name: "Get recent persons"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The person ID."
    foreign-key-id: "person-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the person was last updated."

  - name: "active_flag"
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

  - name: "closed_deals_count"
    type: "integer"
    description: ""

  - name: "company_id"
    type: "integer"
    description: ""

  - name: "done_activities_count"
    type: "integer"
    description: ""

  - name: "email"
    type: "array"
    description: ""
    subattributes:
      - name: "label"
        type: "string"
        description: ""

      - name: "primary"
        type: "boolean"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "email_messages_count"
    type: "integer"
    description: ""

  - name: "files_count"
    type: "integer"
    description: ""

  - name: "first_char"
    type: "string"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "followers_count"
    type: "integer"
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

  - name: "last_name"
    type: "string"
    description: ""

  - name: "last_outgoing_mail_time"
    type: "date-time"
    description: ""

  - name: "lost_deals_count"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "next_activity_date"
    type: "string"
    description: ""

  - name: "next_activity_id"
    type: "integer"
    description: ""
    foreign-key-id: "activity-id"

  - name: "next_activity_time"
    type: "string"
    description: ""

  - name: "notes_count"
    type: "integer"
    description: ""

  - name: "open_deals_count"
    type: "integer"
    description: ""

  - name: "org_id"
    type: "integer"
    description: ""
    foreign-key-id: "organization-id"

  - name: "org_name"
    type: "string"
    description: ""

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "owner_name"
    type: "string"
    description: ""

  - name: "participant_closed_deals_count"
    type: "integer"
    description: ""

  - name: "participant_open_deals_count"
    type: "integer"
    description: ""

  - name: "phone"
    type: "array"
    description: ""
    subattributes:
      - name: "label"
        type: "string"
        description: ""

      - name: "primary"
        type: "boolean"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "picture_id"
    type: "integer"
    description: ""

  - name: "reference_activities_count"
    type: "integer"
    description: ""

  - name: "related_closed_deals_count"
    type: "integer"
    description: ""

  - name: "related_lost_deals_count"
    type: "integer"
    description: ""

  - name: "related_open_deals_count"
    type: "integer"
    description: ""

  - name: "related_won_deals_count"
    type: "integer"
    description: ""

  - name: "timeline_last_activity_time"
    type: "date-time"
    description: ""

  - name: "timeline_last_activity_time_by_owner"
    type: "date-time"
    description: ""

  - name: "undone_activities_count"
    type: "integer"
    description: ""

  - name: "visible_to"
    type: "string"
    description: ""

  - name: "won_deals_count"
    type: "integer"
    description: ""
---