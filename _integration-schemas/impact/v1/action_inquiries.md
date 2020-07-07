---
tap: "impact"
version: "1"
key: "action-inquiry"

name: "action_inquiries"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/action_inquiries.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's action inquiries.

replication-method: "Key-based Incremental"

api-method:
  name: "Get action inquiries"
  doc-link: "https://developer.impact.com/default#operations-Action_Inquiries-GetActionInquiries"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "action-inquiry-id"

  - name: "creation_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "action_id"
    type: "string"
    description: ""
    foreign-key-id: "action-id"

  - name: "action_uri"
    type: "string"
    description: ""

  - name: "auto_approval_date"
    type: "date-time"
    description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "comments"
    type: "array"
    description: ""
    subattributes:
      - name: "comment"
        type: "string"
        description: ""

      - name: "date"
        type: "date-time"
        description: ""

      - name: "user"
        type: "string"
        description: ""

  - name: "expected_payout"
    type: "number"
    description: ""

  - name: "final_payout"
    type: "number"
    description: ""

  - name: "inquiry_type"
    type: "string"
    description: ""

  - name: "media_partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-partner-id"

  - name: "media_partner_name"
    type: "string"
    description: ""

  - name: "order_id"
    type: "string"
    description: ""
    # foreign-key-id: "order-id"

  - name: "reject_reason"
    type: "string"
    description: ""

  - name: "resolution_date"
    type: "date-time"
    description: ""

  - name: "resolution_deadline_date"
    type: "date-time"
    description: ""

  - name: "resolution_status"
    type: "string"
    description: ""

  - name: "tracking_link"
    type: "string"
    description: ""

  - name: "transaction_amount"
    type: "number"
    description: ""

  - name: "transaction_date"
    type: "date-time"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---