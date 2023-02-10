---
tap: "snapchat-ads"
version: "1"
key: ""

name: "ad_account_stats_daily"
doc-link: https://developers.snapchat.com/api/docs/#get-ad-account-stats
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/shared/ad_account_stats.json
description: "This endpoint retrieves the spend metric for the specified Ad Account at DAY granularity, the spend metric is the only metric available for the ad account entity"

replication-method: "Key-based Incremental"

table-key-properties: "id, start_time"
valid-replication-keys: "end_time"

attributes:
  - name: "end_time"
    type: "date-time"
    description: "End Time (ISO 8601)"
    replication-key: true

  - name: "finalized_data_end_time"
    type: "date-time"
    description: "This attribute defines the time up until when non-conversion reporting metrics are finalized. You can query for all metrics before this time including uniques and reach and they will have the final numbers. For any time after the finalized_data_end_time the metrics are still undergoing de-duplication and finalization and may change accordingly"

  - name: "granularity"
    type: "string"
    description: "Metrics granularity. Example: DAY"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Ad Account ID"

  - name: "spend"
    type: "integer"
    description: "Amount Spent (micro-currency)"

  - name: "start_time"
    type: "date-time"
    description: "Start Time (ISO 8601)"
    primary-key: true

  - name: "swipe_up_attribution_window"
    type: "string"
    description: "Attribution window for swipe ups. Example: 1_DAY, 7_DAY, 28_DAY (default)"

  - name: "type"
    type: "string"
    description: "AD Type"

  - name: "view_attribution_window"
    type: "string"
    description: "Attribution window for views. Example: 1_HOUR, 3_HOUR, 6_HOUR, 1_DAY (default), 7_DAY, 28_DAY"
---