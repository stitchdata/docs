---
tap: "impact"
version: "1"
key: "action-update"

name: "action_updates"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/action_updates.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's action updates.

replication-method: "Key-based Incremental"

api-method:
  name: "List action updates"
  doc-link: "https://developer.impact.com/default#operations-Action_Updates-ListActionUpdates"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "action-update-id"

  - name: "update_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "action_date"
    type: "date-time"
    description: ""

  - name: "action_id"
    type: "string"
    description: ""
    foreign-key-id: "action-id"

  - name: "action_tracker_id"
    type: "integer"
    description: ""
    foreign-key-id: "action-tracker-id"

  - name: "action_uri"
    type: "string"
    description: ""

  - name: "ad_id"
    type: "integer"
    description: ""
    foreign-key-id: "ad-id"

  - name: "caller_id"
    type: "string"
    description: ""
    # foreign-key-id: "caller-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "category"
    type: "string"
    description: ""

  - name: "clearing_date"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "customer_status"
    type: "string"
    description: ""

  - name: "delta_amount"
    type: "number"
    description: ""

  - name: "delta_payout"
    type: "number"
    description: ""

  - name: "disposition"
    type: "string"
    description: ""

  - name: "locking_date"
    type: "date-time"
    description: ""

  - name: "media_partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-partner-id"

  - name: "order_id"
    type: "string"
    description: ""
    # foreign-key-id: "order-id"

  - name: "quantity"
    type: "integer"
    description: ""

  - name: "shared_id"
    type: "string"
    description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "state_detail"
    type: "string"
    description: ""

  - name: "state_detail_description"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---