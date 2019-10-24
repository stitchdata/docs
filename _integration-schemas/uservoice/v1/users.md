---
tap: "uservoice"
version: "1.0"

name: "users"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Users
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/.py
description: |
  The `{{ table.name }}` table contains info about your users. This includes both {{ integration.display_name }} admins and end users. 

replication-method: "Key-based Incremental"

api-method:
  name: List users
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-users

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the user was last updated."

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The time the user was created."

  - name: "guid"
    type: "string"
    description: "The user GUID."

  - name: "name"
    type: "string"
    description: "The name of the user."

  - name: "email_address"
    type: "string"
    description: "The email address associated with the user."

  - name: "job_title"
    type: "string"
    description: "The job title of the user."

  - name: "avatar_url"
    type: "string"
    description: "The URL of the user's avatar."

  - name: "last_ip"
    type: "string"
    description: "The last seen IP address associated with the user."

  - name: "country"
    type: "string"
    description: "The user's country."

  - name: "region"
    type: "string"
    description: "The user's region."

  - name: "city"
    type: "string"
    description: "The user's city."

  - name: "satisfaction_score"
    type: "integer"
    description: "The user's NPS rating."

  - name: "allowed_state"
    type: "string"
    description: "The user's allowed state. For example: `allowed`"

  - name: "state"
    type: "string"
    description: "The user's state. For example: `normal`"

  - name: "supported_suggestions_count"
    type: "integer"
    description: "The total number of suggestions the user is a supporter of."

  - name: "is_admin"
    type: "boolean"
    description: "If `true`, the user is a {{ integration.display_name }} admin."

  - name: "is_owner"
    type: "boolean"
    description: "If `true`, the user is the {{ integration.display_name }} account owner."

  - name: "email_confirmed"
    type: "boolean"
    description: "If `true`, the user's `email_address` has been verified."

  - name: "status_notifications"
    type: "boolean"
    description: "If `true`, the user will receive status update notifications."

  - name: "comment_notifications"
    type: "boolean"
    description: "If `true`, the user will receive comment notifications."

  - name: "links"
    type: "object"
    description: ""
    subattributes: 
      - name: "teams"
        type: "array"
        description: "The ID(s) of the team(s) the user is a member of."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The ID of the team the user is a member of."
            foreign-key-id: "team-id"

      - name: "current_nps_rating"
        type: "integer"
        description: "The user's current NPS rating."

      - name: "previous_nps_rating"
        type: "integer"
        description: "The user's previous NPS rating."

      - name: "external_users"
        type: "array"
        description: "The ID(s) of the external user(s) associated with the user."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The ID of the external user associated with the user."
            foreign-key-id: "external-user-id"
---