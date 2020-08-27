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

  - name: "host_id"
    type: "string"
    description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "join_url"
    type: "string"
    description: ""

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
      - name: "allow_multiple_devices"
        type: "boolean"
        description: ""

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

      - name: "hd_video"
        type: "boolean"
        description: ""

      - name: "host_video"
        type: "boolean"
        description: ""

      - name: "meeting_authentication"
        type: "boolean"
        description: ""

      - name: "notify_registrants"
        type: "boolean"
        description: ""

      - name: "on_demand"
        type: "boolean"
        description: ""

      - name: "panelists_video"
        type: "boolean"
        description: ""

      - name: "post_webinar_survey"
        type: "boolean"
        description: ""

      - name: "practice_session"
        type: "boolean"
        description: ""

      - name: "registrants_confirmation_email"
        type: "boolean"
        description: ""

      - name: "registrants_email_notification"
        type: "boolean"
        description: ""

      - name: "registrants_restrict_number"
        type: "integer"
        description: ""

      - name: "registration_type"
        type: "integer"
        description: ""

      - name: "show_share_button"
        type: "boolean"
        description: ""

      - name: "survey_url"
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