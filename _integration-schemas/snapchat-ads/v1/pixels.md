---
tap: "snapchat-ads"
version: "1"
key: ""

name: "pixels"
doc-link: https://developers.snapchat.com/api/docs/#get-the-pixel-associated-with-an-ad-account
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/pixels.json
description: "This stream retrieves the pixel associated with the specified Ad Account."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "id"
    primary-key: true
    type: "string"
    description: "Pixel ID"

    - name: "ad_account_id"
    type: "string"
    description: "Ad Account ID"

    - name: "name"
    type: "string"
    description: "Name of the pixel"

    - name: "organization_id"
    type: "string"
    description: "Organization ID"

    - name: "updated_at"
    type: "date-time"
    description: "Date and time at which the pixel was last updated"

    - name: "created_at"
    type: "object"
      format: "date-time"
    description: "Date and time at which the pixel was created"

    - name: "status"
    type: "string"
    description: "Status of the pixel. Example: Active, "

    - name: "effective_status"
    type: "string"
    description: ""

    - name: "pixel_javascript"
    type: "string"
    description: "Javascript snippet for the created pixel"

  - name: "visible_to"
    type: "array"
    description: ""
    subattributes:
    - type: "string"
      description: ""
---