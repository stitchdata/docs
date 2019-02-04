---
tap: "revinate"
# version: "1.0"

name: "hotel_reviews_snapshot_by_time"
doc-link: https://porter.revinate.com/documentation#review-sites
singer-schema: https://github.com/singer-io/tap-revinate/blob/master/tap_revinate/schemas.py#L70
description: |
  The `{{ table.name }}` table contains snapshot summary stats of reviews for the last completed week, segmented by hotel and time.

  **Note**: Stitch will only replicate review snapshot data for the hotels that the user whose API key is used to [authenticate the integration](#add-stitch-data-source) has access to. If you're missing records, verify that the authenticating user has access to those hotels in {{ integration.display_name }}.

  #### Replication {#review-snapshot-time-replication}

  During each replication job, snapshot data for the last completed week will be replicated. This means that if the integration is scheduled to run every 30 minutes, then snapshot data for the last week will be replicated every 30 minutes.

replication-method: "Key-based Incremental"
attribution-window: true
api-method:
  name: Get review snapshots by hotel ID
  doc-link: https://porter.revinate.com/documentation#hotels

attributes:
  - name: "hotel_id"
    type: "integer"
    primary-key: true
    description: "The hotel ID."
    foreign-key-id: "hotel-id"

  - name: "unix_time"
    type: "integer"
    primary-key: true
    description: ""

  - name: "hotel_reviews_snapshot_url"
    type: "string"
    description: ""

  - name: "snapshot_average_rating"
    type: "number"
    description: ""

  - name: "snapshot_new_reviews"
    type: "number"
    description: ""

  - name: "snapshot_pos_reviews_pct"
    type: "number"
    description: ""

  - name: "snapshot_trip_advisor_market_ranking"
    type: "integer"
    description: ""

  - name: "snapshot_trip_advisor_market_ranking_pctl"
    type: "number"
    description: ""

  - name: "snapshot_trip_advisor_market_size"
    type: "integer"
    description: ""

  - name: "time_period_json"
    type: "string"
    description: ""
---