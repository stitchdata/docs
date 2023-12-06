---
tap: "adroll"
version: "1"
key: "ad"

name: "ads"
doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-ad-get"
singer-schema: "https://github.com/singer-io/tap-adroll/blob/master/tap_adroll/schemas/ads.json"
description: |
  The `{{ table.name }}` table contains information about the ads and creatives associated with the advertisables in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get advertiseable ads"
  doc-link: "https://developers.nextroll.com/docs/crud-api/reference.html#get--api-v1-advertisable-get_ads"

attributes:
  - name: "eid"
    type: "string"
    primary-key: true
    description: "The ad EID."
    foreign-key-id: "ad-id"

  - name: "ad_format"
    type: "string"
    description: ""

  - name: "ad_format_id"
    type: "integer"
    description: ""

  - name: "ad_format_name"
    type: "string"
    description: ""

  - name: "ad_parameters"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "adgroups"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "ad-group-id"

      - name: "status"
        type: "string"
        description: ""

  - name: "advertisable"
    type: "string"
    description: ""
    foreign-key-id: "advertisable-id"

  - name: "app_id"
    type: "string"
    description: ""

  - name: "body"
    type: "string"
    description: ""

  - name: "body_dynamic"
    type: "string"
    description: ""

  - name: "brand_name"
    type: "string"
    description: ""

  - name: "call_to_action"
    type: "string"
    description: ""

  - name: "created_date"
    type: "date-time"
    description: ""

  - name: "destination_url"
    type: "string"
    description: ""

  - name: "display_url_override"
    type: "string"
    description: ""

  - name: "has_edits"
    type: "boolean"
    description: ""

  - name: "has_future_campaigns"
    type: "boolean"
    description: ""

  - name: "has_pending_edits"
    type: "boolean"
    description: ""

  - name: "headline"
    type: "string"
    description: ""

  - name: "headline_dynamic"
    type: "string"
    description: ""

  - name: "height"
    type: "integer"
    description: ""

  - name: "inventory_type"
    type: "string"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "is_fb_dynamic"
    type: "boolean"
    description: ""

  - name: "is_liquid"
    type: "string"
    description: ""

  - name: "is_outlined"
    type: "boolean"
    description: ""

  - name: "lead_gen_form_id"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "message_dynamic"
    type: "string"
    description: ""

  - name: "multi_share_optimized"
    type: "string"
    description: ""

  - name: "multiple_products"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "original_ad"
    type: "string"
    description: ""
    foreign-key-id: "ad-id"

  - name: "outline_color"
    type: "string"
    description: ""

  - name: "replacement_ad"
    type: "string"
    description: ""

  - name: "src"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "updated_date"
    type: "date-time"
    description: ""

  - name: "valid_clicktag"
    type: "boolean"
    description: ""

  - name: "width"
    type: "integer"
    description: ""
---