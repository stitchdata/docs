---
tap: "activecampaign"
version: "1"
key: ""

name: "calendars"
doc-link: "https://developers.activecampaign.com/reference#calendar-feeds"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/calendars.json"
description: |
  The `{{ table.name }}` table contains information about calendar feeds in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all calendar feeds"
    doc-link: "https://developers.activecampaign.com/reference#list-all-calendar-feeds"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The calendar feed ID."
    #foreign-key-id: "calendar-id"

  - name: "mdate"
    type: "date-time"
    description: "The date the calendar feed was last modified."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""

  - name: "notification"
    type: "integer"
    description: ""
  - name: "title"
    type: "string"
    description: ""
  - name: "token"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---
