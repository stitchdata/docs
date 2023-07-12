---
tap: "zoom"
version: "2"
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

  - name: "assistant_id"
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

  - name: "host_email"
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
    description: ""

  - name: "occurrences"
    type: "array"
    description: ""
    subattributes:
    - name: "occurrence_id"
      type: "string"
      description: ""

    - name: "start_time"
      type: "date-time"
      description: ""

    - name: "duration"
      type: "integer"
      description: ""

    - name: "status"
      type: "string"
      description: ""


  - name: "password"
    type: "string"
    description: ""

  - name: "pmi"
    type: "string"
    description: ""

  - name: "pre_schedule"
    type: "boolean"
    description: ""

  - name: "recurrence"
    type: "object"
    description: ""
    subattributes:
    - name: "type"
      type: "integer"
      description: ""

    - name: "repeat_interval"
      type: "integer"
      description: ""

    - name: "weekly_days"
      type: "string"
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

    - name: "end_times"
      type: "integer"
      description: ""

    - name: "end_date_time"
      type: "date-time"
      description: ""


  - name: "settings"
    type: "object"
    description: ""
    subattributes:
    - name: "allow_multiple_devices"
      type: "boolean"
      description: ""

    - name: "calendar_type"
      type: "integer"
      description: ""

    - name: "email_notification"
      type: "boolean"
      description: ""

    - name: "encryption_type"
      type: "string"
      description: ""

    - name: "focus_mode"
      type: "boolean"
      description: ""

    - name: "show_share_button"
      type: "boolean"
      description: ""

    - name: "host_video"
      type: "boolean"
      description: ""

    - name: "participant_video"
      type: "boolean"
      description: ""

    - name: "private_meeting"
      type: "boolean"
      description: ""

    - name: "jbh_time"
      type: "integer"
      description: ""

    - name: "join_before_host"
      type: "boolean"
      description: ""

    - name: "mute_upon_entry"
      type: "boolean"
      description: ""

    - name: "watermark"
      type: "boolean"
      description: ""

    - name: "use_pmi"
      type: "boolean"
      description: ""

    - name: "approval_type"
      type: "integer"
      description: ""

    - name: "registration_type"
      type: "integer"
      description: ""

    - name: "audio"
      type: "string"
      description: ""

    - name: "audio_conference_info"
      type: "string"
      description: ""

    - name: "auto_recording"
      type: "string"
      description: ""

    - name: "alternative_hosts"
      type: "string"
      description: ""

    - name: "alternative_hosts_email_notification"
      type: "boolean"
      description: ""

    - name: "alternative_host_update_polls"
      type: "boolean"
      description: ""

    - name: "close_registration"
      type: "boolean"
      description: ""

    - name: "waiting_room"
      type: "boolean"
      description: ""

    - name: "host_save_video_order"
      type: "boolean"
      description: ""

    - name: "global_dial_in_countries"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

    - name: "language_interpretation"
      type: "object"
      description: ""
      subattributes:
      - name: "enable"
        type: "boolean"
        description: ""

      - name: "interpreters"
        type: "array"
        description: ""
        subattributes:
        - name: "email"
          type: "string"
          description: ""

        - name: "languages"
          type: "string"
          description: ""



    - name: "global_dial_in_numbers"
      type: "array"
      description: ""
      subattributes:
      - name: "country"
        type: "string"
        description: ""

      - name: "country_name"
        type: "string"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "number"
        type: "string"
        description: ""

      - name: "type"
        type: "string"
        description: ""


    - name: "breakout_room"
      type: "object"
      description: ""
      subattributes:
      - name: "enable"
        type: "boolean"
        description: ""

      - name: "rooms"
        type: "array"
        description: ""
        subattributes:
        - name: "name"
          type: "string"
          description: ""

        - name: "participants"
          type: "array"
          description: ""
          subattributes:
          - name: "items"
            type: "string"
            description: ""



    - name: "custom_keys"
      type: "array"
      description: ""
      subattributes:
      - name: "key"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""


    - name: "approved_or_denied_countries_or_regions"
      type: "object"
      description: ""
      subattributes:
      - name: "approved_list"
        type: "array"
        description: ""
        subattributes:
        - name: "items"
          type: "string"
          description: ""

      - name: "denied_list"
        type: "array"
        description: ""
        subattributes:
        - name: "items"
          type: "string"
          description: ""

      - name: "enable"
        type: "boolean"
        description: ""

      - name: "method"
        type: "string"
        description: ""


    - name: "authentication_exception"
      type: "array"
      description: ""
      subattributes:
      - name: "email"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "join_url"
        type: "string"
        description: ""


    - name: "contact_name"
      type: "string"
      description: ""

    - name: "contact_email"
      type: "string"
      description: ""

    - name: "registrants_confirmation_email"
      type: "boolean"
      description: ""

    - name: "registrants_email_notification"
      type: "boolean"
      description: ""

    - name: "meeting_authentication"
      type: "boolean"
      description: ""

    - name: "authentication_name"
      type: "string"
      description: ""

    - name: "authentication_option"
      type: "string"
      description: ""

    - name: "authentication_domains"
      type: "string"
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

    - name: "visible"
      type: "boolean"
      description: ""


  - name: "type"
    type: "integer"
    description: ""
---