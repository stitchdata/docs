---
tap: "snapchat-ads"
version: "1"
key: ""

name: "creatives"
doc-link: https://developers.snapchat.com/api/docs/#get-all-creatives
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/creatives.json
description: "This endpoint retrieves all creatives associated with an ad account"

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "ad_account_id"
    type: "string"
    description: "Ad Account ID"

  - name: "ad_product"
    type: "string"
    description: "Type of Ad Product"

  - name: "ad_to_lens_properties"
    type: "object"
    description: ""

  - name: "ad_to_message_properties"
    type: "object"
    description: ""

  - name: "app_install_properties"
    type: "object"
    description: ""

  - name: "brand_name"
    type: "string"
    description: "Brand Name"

  - name: "call_to_action"
    type: "string"
    description: "Call to Action"

  - name: "collection_properties"
    type: "object"
    description: ""

  - name: "composite_properties"
    type: "object"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: "Date of creation"

  - name: "deep_link_properties"
    type: "object"
    description: "Deep Link properties"

  - name: "dynamic_render_properties"
    type: "object"
    description: "Dynamic Render Properties"

  - name: "forced_view_eligibility"
    type: "string"
    description: "Indicates whether Creative can be used as a Commercial"

  - name: "headline"
    type: "string"
    description: "Headline (displayed under brand name)"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Creative ID"

  - name: "longform_video_properties"
    type: "object"
    description: "specifies the attributes for the Long Form Video Attachment"

  - name: "name"
    type: "string"
    description: "Creative Name"

  - name: "packaging_status"
    type: "string"
    description: "Creative packaging status"

  - name: "playback_type"
    type: "string"
    description: "Specifies whether the creatives within the composite auto-advance or loop"

  - name: "preview_creative_id"
    type: "string"
    description: "ID of the preview creative"

  - name: "preview_properties"
    type: "object"
    description: "Preview properties for the campaign"

  - name: "render_type"
    type: "string"
    description: "Render Type. Example: STATIC, DYNAMIC"

  - name: "review_status"
    type: "string"
    description: "Creative Review Status"

  - name: "shareable"
    type: "boolean"
    description: "Allow Users to Share with Friends"

  - name: "top_snap_crop_position"
    type: "string"
    description: "Top Snap Crop Position"

  - name: "top_snap_media_id"
    type: "string"
    description: "Top Snap Media ID"

  - name: "type"
    type: "string"
    description: "Creative Type"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last updated"
    replication-key: true

  - name: "web_view_properties"
    type: "object"
    description: "Defines the url for `Shop Now` button Required when interaction_type == WEB_VIEW. Only url in web_view_properties can be used"
---