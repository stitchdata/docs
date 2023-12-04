---
tap: "zoom"
version: "1"
key: "meeting"

name: "meetings"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetings"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/meetings.json"
description: |
  The `{{ table.name }}` table contains information about instant, scheduled, and recurring meetings in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get meetings"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetings"

attributes:
  - name: "uuid"
    type: "string"
    primary-key: true
    description: "The meeting UUID."
    foreign-key-id: "meeting-uuid"

  - name: "agenda"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "encrypted_password"
    type: "string"
    description: ""

  - name: "h323_password"
    type: "string"
    description: ""

  - name: "host_id"
    type: "string"
    description: ""

  - name: "id"
    type: "integer"
    description: ""

  - name: "join_url"
    type: "string"
    description: ""

  - name: "meeting_id"
    type: "string"
    description: "The meeting ID."
    foreign-key-id: "meeting-id"

  - name: "occurences"
    type: "array"
    description: ""
    subattributes:
      - name: "duration"
        type: "integer"
        description: ""

      - name: "occurence_id"
        type: "string"
        description: ""

      - name: "start_time"
        type: "date-time"
        description: ""

      - name: "status"
        type: "string"
        description: ""

  - name: "password"
    type: "string"
    description: ""

  - name: "pmi"
    type: "integer"
    description: ""

  - name: "recurrence"
    type: "object"
    description: ""
    subattributes:
      - name: "end_date_time"
        type: "date-time"
        description: ""

      - name: "end_times"
        type: "integer"
        description: ""

      - name: "monthly_day"
        type: "integer"
        description: ""

      - name: "monthly_week"
        type: "integer"
        description: ""

      - name: "monthly_week_day"
        type: "integer"
        description: ""

      - name: "repeat_interval"
        type: "integer"
        description: ""

      - name: "type"
        type: "integer"
        description: ""

      - name: "weekly_days"
        type: "integer"
        description: ""

  - name: "settings"
    type: "object"
    description: ""
    subattributes:
      - name: "alternative_hosts"
        type: "string"
        description: ""

      - name: "approval_type"
        type: "integer"
        description: ""

      - name: "audio"
        type: "string"
        description: ""

      - name: "authentication_domains"
        type: "string"
        description: ""

      - name: "authentication_option"
        type: "string"
        description: ""

      - name: "auto_recording"
        type: "string"
        description: ""

      - name: "close_registration"
        type: "boolean"
        description: ""

      - name: "cn_meeting"
        type: "boolean"
        description: ""

      - name: "contact_email"
        type: "boolean"
        description: ""

      - name: "contact_name"
        type: "boolean"
        description: ""

      - name: "enforce_login"
        type: "boolean"
        description: ""

      - name: "enforce_login_domains"
        type: "string"
        description: ""

      - name: "global_dial_in_countries"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

      - name: "global_dial_in_numbers"
        type: "array"
        description: ""
        subattributes:
          - name: "city"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "country_name"
            type: "string"
            description: ""

          - name: "number"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

      - name: "host_video"
        type: "boolean"
        description: ""

      - name: "in_meeting"
        type: "boolean"
        description: ""

      - name: "join_before_host"
        type: "boolean"
        description: ""

      - name: "meeting_authentication"
        type: "boolean"
        description: ""

      - name: "mute_upon_entry"
        type: "boolean"
        description: ""

      - name: "participant_video"
        type: "boolean"
        description: ""

      - name: "registrants_confirmation_email"
        type: "boolean"
        description: ""

      - name: "registrants_email_notification"
        type: "boolean"
        description: ""

      - name: "registration_type"
        type: "integer"
        description: ""

      - name: "use_pmi"
        type: "boolean"
        description: ""

      - name: "waiting_room"
        type: "boolean"
        description: ""

      - name: "watermark"
        type: "boolean"
        description: ""

  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "start_url"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "topic"
    type: "string"
    description: ""

  - name: "tracking_fields"
    type: "array"
    description: ""
    subattributes:
      - name: "field"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "type"
    type: "integer"
    description: ""
---