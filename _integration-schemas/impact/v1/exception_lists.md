---
tap: "impact"
version: "1"
key: "exception-list"

name: "exception_lists"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/exception_lists.json"
description: |
  The `{{ table.name }}` table contains info about exception lists.

replication-method: "Full Table"

api-method:
  name: "Get exception lists"
  doc-link: "https://developer.impact.com/default#operations-Exception_Lists-GetExceptionLists"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "exception-list-id"

  - name: "action_trackers"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "action-tracker-id"

      - name: "name"
        type: "string"
        description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "deactivation_date"
    type: "date-time"
    description: ""

  - name: "items_uri"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "number_of_items"
    type: "integer"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---