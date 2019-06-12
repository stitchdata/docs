---
tap: "pipedrive"
version: "1.0"
key: "organization"

name: "organizations"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-pipedrive/blob/master/tap_pipedrive/schemas/recents/dynamic_typing/organizations.json"
description: |
  The `{{ table.name }}` table contains info about the recent organizations in your {{ integration.display_name }} account. Organizations are companies and other types of organizations you are making deals with.

replication-method: ""

api-method:
  name: "Get recent organizations"
  doc-link: "https://developers.pipedrive.com/docs/api/v1/#!/Recents"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The organization ID."
    foreign-key-id: "organization-id"

  - name: "update_time"
    type: "date-time"
    replication-key: true
    description: "The time the organization was last updated."

  - name: "active_flag"
    type: "boolean"
    description: ""

  - name: "activities_count"
    type: "integer"
    description: ""

  - name: "add_time"
    type: "date-time"
    description: ""

  - name: "address"
    type: "string"
    description: ""

  - name: "address_admin_area_level_1"
    type: "string"
    description: ""

  - name: "address_admin_area_level_2"
    type: "string"
    description: ""

  - name: "address_country"
    type: "string"
    description: ""

  - name: "address_formatted_address"
    type: "string"
    description: ""

  - name: "address_locality"
    type: "string"
    description: ""

  - name: "address_postal_code"
    type: "string"
    description: ""

  - name: "address_route"
    type: "string"
    description: ""

  - name: "address_street_number"
    type: "string"
    description: ""

  - name: "address_sublocality"
    type: "string"
    description: ""

  - name: "address_subpremise"
    type: "string"
    description: ""

  - name: "category_id"
    type: "integer"
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

  - name: "country_code"
    type: "string"
    description: ""

  - name: "done_activities_count"
    type: "integer"
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

  - name: "owner_id"
    type: "integer"
    description: ""

  - name: "owner_name"
    type: "string"
    description: ""

  - name: "people_count"
    type: "integer"
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