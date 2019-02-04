---
tap: "revinate"
# version: "1.0"

name: "hotel_reviews_snapshot_by_site"
doc-link: https://porter.revinate.com/documentation#review-sites
singer-schema: https://github.com/singer-io/tap-revinate/blob/master/tap_revinate/schemas.py#L47
description: |
  The `{{ table.name }}` table contains snapshot summary stats of reviews for the last completed week, segmented by hotel and review site.

  **Note**: Stitch will only replicate review snapshot data for the hotels that the user whose API key is used to [authenticate the integration](#add-stitch-data-source) has access to. If you're missing records, verify that the authenticating user has access to those hotels in {{ integration.display_name }}.

  #### Replication {#review-snapshot--site-replication}

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

  - name: "review_site_id"
    type: "integer"
    primary-key: true
    description: "The review site ID."

  - name: "snapshot_start_date"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The snapshot start date."

  - name: "hotel_reviews_snapshot_url"
    type: "string"
    description: ""

  - name: "review_site_json"
    type: "string"
    description: ""

  - name: "review_site_main_url"
    type: "string"
    description: "The main URL of the review site."

  - name: "review_site_name"
    type: "string"
    description: "The review site name."

  - name: "review_site_url"
    type: "string"
    description: "The review site URL."

  - name: "review_site_slug"
    type: "string"
    description: ""

  - name: "site_average_rating"
    type: "number"
    description: ""

  - name: "site_json"
    type: "string"
    description: ""

  - name: "site_new_reviews"
    type: "integer"
    description: ""

  - name: "site_pos_reviews_pct"
    type: "number"
    description: ""

  - name: "site_trip_advisor_market_ranking"
    type: "integer"
    description: ""

  - name: "site_trip_advisor_market_ranking_pctl"
    type: "number"
    description: ""

  - name: "site_trip_advisor_market_size"
    type: "integer"
    description: ""

  - name: "snapshot_end_date"
    type: "integer"
    description: "The snapshot end date as a Unix timestamp."
---