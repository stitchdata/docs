---
tap: "pendo"
version: "1"
key: "visitor-history"

name: "visitor_history"
doc-link: "https://developers.pendo.io/docs/?bash#visitor"
singer-schema: "https://github.com/singer-io/tap-pendo/blob/master/tap_pendo/schemas/visitor_history.json"
description: |
  The `{{ table.name }}` table contains info about visitor activity.

replication-method: "Key-based Incremental"

api-method:
  name: "Aggregation"
  doc-link: "https://api/v1/aggregation"

attributes:
  - name: "visitor_id"
    type: "string"
    primary-key: true
    description: "The visitor ID."
    foreign-key-id: "visitor-id"

  - name: "last_ts"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "app_id"
    type: "integer"
    description: ""
    foreign-key-id: "app-id"

  - name: "duration"
    type: "integer"
    description: ""

  - name: "feature_id"
    type: "string"
    description: ""
    foreign-key-id: "feature-id"

  - name: "guide_id"
    type: "string"
    description: ""
    foreign-key-id: "guide-id"

  - name: "guide_step_id"
    type: "string"
    description: ""
    foreign-key-id: "guide-step-id"

  - name: "page_id"
    type: "string"
    description: ""
    foreign-key-id: "page-id"

  - name: "parsed_user_agent"
    type: "object"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "os"
        type: "string"
        description: ""

      - name: "version"
        type: "string"
        description: ""

  - name: "ts"
    type: "date-time"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "untagged_url"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---