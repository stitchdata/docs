---
tap: "zoom"
version: "1"
key: "webinar"

name: "webinars"
doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinars"
singer-schema: "https://github.com/singer-io/tap-zoom/blob/master/tap_zoom/schemas/webinars.json"
description: |
  The `{{ table.name }}` table contains information bout webinars scheduled from your {{ integration.display_name }} account.

  **Note**: [As per {{ integration.display_name }}'s docs]({{ table.api-method.doc-link }}){:target="new"}, the following requirements must be met to retrieve this data:

  - A Pro plan or higher with a webinar add-on
  - An authentication app with the `webinar:read:admin` and `webinar:read` scopes

replication-method: "Full Table"

api-method:
  name: "Get webinars"
  doc-link: "https://marketplace.zoom.us/docs/api-reference/zoom-api/webinars/webinars"

attributes:
  - name: "uuid"
    type: "string"
    primary-key: true
    description: "The webinar UUID."
    foreign-key-id: "webinar-uuid"
    
  - name: "agenda"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "duration"
    type: "integer"
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

  - name: "is_simulive"
    type: "boolean"
    description: ""

  - name: "join_url"
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

  - name: "record_file_id"
    type: "string"
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
    - name: "host_video"
      type: "boolean"
      description: ""

    - name: "panelists_video"
      type: "boolean"
      description: ""

    - name: "practice_session"
      type: "boolean"
      description: ""

    - name: "hd_video"
      type: "boolean"
      description: ""

    - name: "hd_video_for_attendees"
      type: "boolean"
      description: ""

    - name: "question_and_answer"
      type: "object"
      description: ""
      subattributes:
      - name: "allow_anonymous_questions"
        type: "boolean"
        description: ""

      - name: "answer_questions"
        type: "string"
        description: ""

      - name: "attendees_can_comment"
        type: "boolean"
        description: ""

      - name: "attendees_can_upvote"
        type: "boolean"
        description: ""

      - name: "allow_auto_reply"
        type: "boolean"
        description: ""

      - name: "auto_reply_text"
        type: "string"
        description: ""

      - name: "enable"
        type: "boolean"
        description: ""


    - name: "approval_type"
      type: "integer"
      description: ""

    - name: "panelist_authentication"
      type: "boolean"
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



    - name: "attendees_and_panelists_reminder_email_notification"
      type: "object"
      description: ""
      subattributes:
      - name: "enable"
        type: "boolean"
        description: ""

      - name: "type"
        type: "integer"
        description: ""


    - name: "follow_up_absentees_email_notification"
      type: "object"
      description: ""
      subattributes:
      - name: "enable"
        type: "boolean"
        description: ""

      - name: "type"
        type: "integer"
        description: ""


    - name: "follow_up_attendees_email_notification"
      type: "object"
      description: ""
      subattributes:
      - name: "enable"
        type: "boolean"
        description: ""

      - name: "type"
        type: "integer"
        description: ""


    - name: "registration_type"
      type: "integer"
      description: ""

    - name: "send_1080p_video_to_attendees"
      type: "boolean"
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

    - name: "alternative_host_update_polls"
      type: "boolean"
      description: ""

    - name: "show_share_button"
      type: "boolean"
      description: ""

    - name: "allow_multiple_devices"
      type: "boolean"
      description: ""

    - name: "on_demand"
      type: "boolean"
      description: ""

    - name: "panelists_invitation_email_notification"
      type: "boolean"
      description: ""

    - name: "global_dial_in_countries"
      type: "array"
      description: ""
      subattributes:
      - name: "items"
        type: "string"
        description: ""

    - name: "contact_name"
      type: "string"
      description: ""

    - name: "contact_email"
      type: "string"
      description: ""

    - name: "email_language"
      type: "string"
      description: ""

    - name: "registrants_confirmation_email"
      type: "boolean"
      description: ""

    - name: "registrants_restrict_number"
      type: "integer"
      description: ""

    - name: "notify_registrants"
      type: "boolean"
      description: ""

    - name: "post_webinar_survey"
      type: "boolean"
      description: ""

    - name: "survey_url"
      type: "string"
      description: ""

    - name: "registrants_email_notification"
      type: "boolean"
      description: ""

    - name: "meeting_authentication"
      type: "boolean"
      description: ""

    - name: "add_watermark"
      type: "boolean"
      description: ""

    - name: "add_audio_watermark"
      type: "boolean"
      description: ""

    - name: "authentication_option"
      type: "string"
      description: ""

    - name: "enable_session_branding"
      type: "boolean"
      description: ""

    - name: "authentication_domains"
      type: "string"
      description: ""

    - name: "authentication_name"
      type: "string"
      description: ""


  - name: "start_time"
    type: "date-time"
    description: ""

  - name: "start_url"
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