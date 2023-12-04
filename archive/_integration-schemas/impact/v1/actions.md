---
tap: "impact"
version: "1"
key: "action"

name: "actions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/actions.json"
description: |
  The `{{ table.name }}` table contains info about a campaign's actions.

replication-method: "Key-based Incremental"

api-method:
  name: "Get actions"
  doc-link: "https://developer.impact.com/default#operations-Actions-GetActions"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "action-id"

  - name: "event_date"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "action_tracker_id"
    type: "integer"
    description: ""
    foreign-key-id: "action-tracker-id"

  - name: "action_tracker_name"
    type: "string"
    description: ""

  - name: "ad_id"
    type: "integer"
    description: ""
    foreign-key-id: "ad-id"

  - name: "amount"
    type: "number"
    description: ""

  - name: "caller_id"
    type: "string"
    description: ""
    # foreign-key-id: "caller-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "campaign_name"
    type: "string"
    description: ""

  - name: "cleared_date"
    type: "date-time"
    description: ""

  - name: "client_cost"
    type: "number"
    description: ""

  - name: "creation_date"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "customer_area"
    type: "string"
    description: ""

  - name: "customer_city"
    type: "string"
    description: ""

  - name: "customer_country"
    type: "string"
    description: ""

  - name: "customer_id"
    type: "string"
    description: ""
    foreign-key-id: "customer-id"

  - name: "customer_post_code"
    type: "string"
    description: ""

  - name: "customer_region"
    type: "string"
    description: ""

  - name: "customer_status"
    type: "string"
    description: ""

  - name: "delta_amount"
    type: "number"
    description: ""

  - name: "delta_payout"
    type: "number"
    description: ""

  - name: "intended_amount"
    type: "number"
    description: ""

  - name: "intended_payout"
    type: "number"
    description: ""

  - name: "ip_address"
    type: "string"
    description: ""

  - name: "locking_date"
    type: "date-time"
    description: ""

  - name: "media_partner_id"
    type: "integer"
    description: ""
    foreign-key-id: "media-partner-id"

  - name: "media_partner_name"
    type: "string"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "order_id"
    type: "string"
    description: ""
    # foreign-key-id: "order-id"

  - name: "payout"
    type: "number"
    description: ""

  - name: "promo_code"
    type: "string"
    description: ""

  - name: "referring_date"
    type: "date-time"
    description: ""

  - name: "referring_domain"
    type: "string"
    description: ""

  - name: "referring_type"
    type: "string"
    description: ""

  - name: "shared_id"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---