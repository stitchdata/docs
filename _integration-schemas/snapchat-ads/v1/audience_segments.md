---
tap: "snapchat-ads"
version: "1"
key: ""

name: "audience_segments"
doc-link: https://marketingapi.snapchat.com/docs/#get-all-audience-segments
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/audience_segments.json
description: "This stream retrieves all Customer List segments within a specified ad account."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "ad_account_id"
    type: "string"
    description: "Ad Account ID"

  - name: "approximate_number_users"
    type: "integer"
    description: "Approximate # of users in the segment"

  - name: "created_at"
    type: "date-time"
    description: "Date of creation"

  - name: "description"
    type: "string"
    description: "Audience Segment Description"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Segment ID"

  - name: "name"
    type: "string"
    description: "Segment Name"

  - name: "organization_id"
    type: "string"
    description: "Organization ID"

  - name: "retention_in_days"
    type: "integer"
    description: "# of days to retain audience members"

  - name: "source_type"
    type: "string"
    description: "Data source type"

  - name: "status"
    type: "string"
    description: "Status of the segment"

  - name: "targetable_status"
    type: "string"
    description: "Status of whether this segment can be targeted"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last update"

  - name: "upload_status"
    type: "string"
    description: "Upload status of the segment"

  - name: "visible_to"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""



