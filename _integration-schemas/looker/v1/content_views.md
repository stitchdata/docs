---
tap: "looker"
version: "1"
key: "content-view"

name: "content_views"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/content_views.json"
description: |
  The `{{ table.name }}` table contains info about user content views recorded in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Search users"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/user#search_users"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The content view ID."
    # foreign-key-id: "content-view-id"

  - name: "content_metadata_id"
    type: "string"
    description: ""
    foreign-key-id: "content-metadata-id"

  - name: "dashboard_id"
    type: "string"
    description: ""
    foreign-key-id: "dashboard-id"

  - name: "favorite_count"
    type: "integer"
    description: ""

  - name: "group_id"
    type: "string"
    description: ""
    foreign-key-id: "group-id"

  - name: "last_viewed_at"
    type: "string"
    description: ""

  - name: "look_id"
    type: "string"
    description: ""
    foreign-key-id: "look-id"

  - name: "start_of_week_date"
    type: "string"
    description: ""

  - name: "user_id"
    type: "string"
    description: ""
    foreign-key-id: "user-id"

  - name: "view_count"
    type: "integer"
    description: ""
---