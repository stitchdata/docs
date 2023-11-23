---
tap: "google-ads"
version: "1"

name: "click_performance_report"
doc-link: https://developers.google.com/google-ads/api/fields/v12/overview
description: |
  The `{{ table.name }}` table contains statistics aggregated at each click level, and includes both valid and invalid clicks.

  [This is a **Report** table](#replication). See the **Replication** section for information on how data is replicated and loaded for this table.

replication-method: "Key-based Incremental"

attribution-window: true

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: "{{ system-column.record-hash-google-ads }}"

  - name: "date"
    type: "date-time"
    replication-key: true
    description: "The day the record pertains to."

  - name: "customer_id"
    type: "integer"
    description: "The ID of the Ads account that the record belongs to."
    foreign-key-id: "customer_id"

  - name: "ad_group_id"
    type: "integer"
    description: "The ID of the ad group that the record belongs to."
    foreign-key-id: "ad_group_id"

  - name: "campaign_id"
    type: "integer"
    description: "The ID of the campaign that the record belongs to."
    foreign-key-id: "campaign_id"
    
  - name: "campaign_labels"
    type: "string"
    description: ""  

  - name: "ad_group_name"
    type: "string"
    description: ""
  - name: "ad_group_status"
    type: "string"
    description: ""
  - name: "ad_network_type"
    type: "string"
    description: ""
  - name: "campaign_name"
    type: "string"
    description: ""
  - name: "campaign_status"
    type: "string"
    description: ""
  - name: "click_type"
    type: "string"
    description: ""
  - name: "click_view_ad_group_ad"
    type: "object, string"
    description: ""
  - name: "click_view_area_of_interest"
    type: "object"
    description: ""
    subattributes:
      - name: "city"
        type: "object, string"
        description: ""
      - name: "country"
        type: "object, string"
        description: ""
      - name: "metro"
        type: "object, string"
        description: ""
      - name: "most_specific"
        type: "object, string"
        description: ""
      - name: "region"
        type: "object, string"
        description: ""
  - name: "click_view_campaign_location_target"
    type: "object, string"
    description: ""
  - name: "click_view_gclid"
    type: "string"
    description: ""
  - name: "click_view_location_of_presence"
    type: "object"
    description: ""
    subattributes:
      - name: "city"
        type: "object, string"
        description: ""
      - name: "country"
        type: "object, string"
        description: ""
      - name: "metro"
        type: "object, string"
        description: ""
      - name: "most_specific"
        type: "object, string"
        description: ""
      - name: "region"
        type: "object, string"
        description: ""
  - name: "click_view_page_number"
    type: "integer"
    description: ""
  - name: "click_view_user_list"
    type: "object, string"
    description: ""
  - name: "clicks"
    type: "integer"
    description: ""
  - name: "customer_descriptive_name"
    type: "string"
    description: ""
  - name: "device"
    type: "string"
    description: ""
  - name: "month_of_year"
    type: "string"
    description: ""
  - name: "slot"
    type: "string"
    description: ""
---