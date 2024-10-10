---
tap: "google-ads"
version: "1"
name: "ad_group_criterion"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v12/AdGroupCriterion
description: |
  The `{{ table.name }}` table contains info about ad group criteria.

  [This is a **Core Object** table](#replication).

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "customer_id"
    type: "integer"
    description: ""

  - name: "campaign_id"
    type: "integer"
    description: ""

  - name: "resource_name"
    type: "string"
    description: ""

  - name: "display_name"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "quality_info"
    type: "object"
    description: ""
    subattributes:
      - name: "creative_quality_score"
        type: "string"
        description: ""
      
      - name: "post_click_quality_score"
        type: "string"
        description: ""
      
      - name: "search_predicted_ctr"
        type: "string"
        description: ""
      
      - name: "quality_score"
        type: "integer"
        description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "system_serving_status"
    type: "string"
    description: ""

  - name: "approval_status"
    type: "string"
    description: ""

  - name: "disapproval_reasons"
    type: "array"
    description: ""
    subattributes:
      - name: "reason"
        type: "string"
        description: ""

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - name: "label"
        type: "string"
        description: ""

  - name: "effective_cpc_bid_source"
    type: "string"
    description: ""

  - name: "effective_cpm_bid_source"
    type: "string"
    description: ""

  - name: "effective_cpv_bid_source"
    type: "string"
    description: ""

  - name: "effective_percent_cpc_bid_source"
    type: "string"
    description: ""

  - name: "position_estimates"
    type: "object"
    description: ""
    subattributes:
      - name: "first_page_cpc_micros"
        type: "integer"
        description: ""

      - name: "first_position_cpc_micros"
        type: "integer"
        description: ""
        
      - name: "top_of_page_cpc_micros"
        type: "integer"
        description: ""
        
      - name: "estimated_add_clicks_at_first_position_cpc"
        type: "integer"
        description: ""
        
      - name: "estimated_add_cost_at_first_position_cpc"
        type: "integer"
        description: ""

  - name: "final_urls"
    type: "array"
    description: ""
    subattributes:
      - name: "url"
        type: "string"
        description: ""

  - name: "final_mobile_urls"
    type: "array"
    description: ""
    subattributes:
      - name: "url"
        type: "string"
        description: ""

  - name: "url_custom_parameters"
    type: "array"
    description: ""
    subattributes:
      - name: "parameter"
        type: "object"
        description: ""
        subattributes:
          - name: "key"
            type: "string"
            description: ""
            
          - name: "value"
            type: "string"
            description: ""

  - name: "criterion_id"
    type: "integer"
    description: ""
    primary-key: true

  - name: "ad_group"
    type: "string"
    description: ""

  - name: "ad_group_id"
    type: "integer"
    description: ""
    primary-key: true

  - name: "negative"
    type: "boolean"
    description: ""

  - name: "bid_modifier"
    type: "double"
    description: ""

  - name: "cpc_bid_micros"
    type: "integer"
    description: ""

  - name: "cpm_bid_micros"
    type: "integer"
    description: ""

  - name: "cpv_bid_micros"
    type: "integer"
    description: ""

  - name: "percent_cpc_bid_micros"
    type: "integer"
    description: ""

  - name: "effective_cpc_bid_micros"
    type: "integer"
    description: ""

  - name: "effective_cpm_bid_micros"
    type: "integer"
    description: ""

  - name: "effective_cpv_bid_micros"
    type: "integer"
    description: ""

  - name: "effective_percent_cpc_bid_micros"
    type: "integer"
    description: ""

  - name: "final_url_suffix"
    type: "string"
    description: ""

  - name: "tracking_url_template"
    type: "string"
    description: ""

  - name: "criterion"
    type: "object"
    description: "The ad group criterion. It is one of the objects listed under criterion in the [Google Ads API documentation](https://developers.google.com/google-ads/api/reference/rpc/v12/AdGroupCriterion#criterion)."

---