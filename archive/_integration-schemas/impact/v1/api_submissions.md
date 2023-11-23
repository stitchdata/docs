---
tap: "impact"
version: "1"
key: "api-submission"

name: "api_submissions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/api_submissions.json"
description: |
  The `{{ table.name }}` table contains info about API submissions.

replication-method: "Key-based Incremental"

api-method:
  name: "Get API submissions"
  doc-link: "https://developer.impact.com/default/documentation/Rest-Adv-v8#operations-API_Submissions-GetAPISubmissions"

attributes:
  - name: "batch_id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "api-submission-id"

  - name: "submission_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "action_tracker_id"
    type: "integer"
    description: ""
    foreign-key-id: "action-tracker-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "completion_date"
    type: "date-time"
    description: ""

  - name: "error_reason"
    type: "string"
    description: ""

  - name: "error_type"
    type: "string"
    description: ""

  - name: "event_code"
    type: "string"
    description: ""

  - name: "media_partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-partner-id"

  - name: "order_id"
    type: "string"
    description: ""
    # foreign-key-id: "order-id"

  - name: "payload"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---