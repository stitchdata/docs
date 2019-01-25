---
tap: "toggl"
version: "1.0"

name: "users"
doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/users.md"
singer-schema: "https://github.com/singer-io/tap-toggl/blob/master/tap_toggl/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
    name: "Get workspace users"
    doc-link: "https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-users"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "at"
    type: "date-time"
    replication-key: true
    description: "The date and time the user was last updated."

  - name: "beginning_of_week"
    type: "integer"
    description: |
      The user's beginning of the week. Possible values are:

      - `0` - Sunday
      - `1` - Monday
      - `2` - Tuesday
      - `3` - Wednesday
      - `4` - Thursday
      - `5` - Friday
      - `6` - Saturday

  - name: "date_format"
    type: "string"
    description: "The date format the user uses."

  - name: "default_wid"
    type: "integer"
    description: "The ID of the user's default workspace."
    foreign-key-id: "workspace-id"

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "fullname"
    type: "string"
    description: "The user's full name."

  - name: "image_url"
    type: "string"
    description: "The URL of the user's profile picture."

  - name: "invitation"
    type: "string"
    description: ""

  - name: "jquery_date_format"
    type: "string"
    description: "The jQuery date format."

  - name: "jquery_timeofday_format"
    type: "string"
    description: "The jQuery time of day format."

  - name: "language"
    type: "string"
    description: "The user's language."

  - name: "new_blog_post"
    type: "string"
    description: ""

  - name: "record_timeline"
    type: "boolean"
    description: ""

  - name: "render_timeline"
    type: "boolean"
    description: ""

  - name: "retention"
    type: "integer"
    description: ""

  - name: "should_upgrade"
    type: "boolean"
    description: ""

  - name: "sidebar_piechart"
    type: "boolean"
    description: "Indicates if the user will have a pie chart shown in their sidebar in the {{ integration.display_name }} app."

  - name: "store_start_and_stop_time"
    type: "boolean"
    description: "Indicates whether start and stop times are saved on time entries."

  - name: "timeline_enabled"
    type: "boolean"
    description: ""

  - name: "timeline_experiment"
    type: "boolean"
    description: ""

  - name: "timeofday_format"
    type: "string"
    description: "The formatting used for the time of day for the user."
---