---
tap: "impact"
version: "1"
key: "exception-list-item"

name: "exception_list_items"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/exception_list_items.json"
description: |
  The `{{ table.name }}` table contains info about an exception list's items.

replication-method: "Full Table"

api-method:
  name: "Get exception list items"
  doc-link: "https://developer.impact.com/default#operations-Exception_Lists-GetExceptionListItems"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "exception-list-item-id"

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "list_id"
    type: "integer"
    description: ""
    foreign-key-id: "exception-list-id"

  - name: "match_mode"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""

  - name: "value"
    type: "string"
    description: ""
---