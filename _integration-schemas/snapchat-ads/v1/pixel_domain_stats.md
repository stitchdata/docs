---
tap: "snapchat-ads"
version: "1"
key: ""

name: "pixel_domain_stats"
doc-link: https://developers.snapchat.com/api/docs/#get-pixel-domains
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/pixel_domain_stats.json
description: "This stream retrieves the domains that have fired the pixel in the past 7 days."

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "domains"
    type: "array"
    description: "List of Domains"
    subattributes:
    - name: "domain_name"
      type: "string"
      description: "Domain Name"

    - name: "total_events"
      type: "integer"
      description: ""


  - name: "end_time"
    type: "date-time"
    description: "End Time (ISO 8601)"

  - name: "id"
    primary-key: true
    type: "string"
    description: "ID"

  - name: "pixel_id"
    type: "string"
    description: "Pixel ID"

  - name: "start_time"
    type: "date-time"
    description: "Start Time (ISO 8601)"

  - name: "type"
    type: "string"
    description: "Type"
---