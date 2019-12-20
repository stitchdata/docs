---
tap-reference: "google-adwords"

version: "1.0"

foreign-keys:
  - id: "customer-id"
    attribute: "customerId"
    table: "accounts"
    all-foreign-keys:
      - table: "account_performance_report"
      - table: "accounts"
      - table: "ad_groups"
      - table: "ad_performance_report"
      - table: "adgroup_performance_report"
      - table: "age_range_performance_report"
      - table: "audience_performance_report"
      - table: "call_metrics_call_details_performance_report"
      - table: "campaign_performance_report"
      - table: "campaigns"
      - table: "click_performance_report"
      - table: "criteria_performance_report"
      - table: "display_keyword_performance_report"
      - table: "display_topics_performance_report"
      - table: "final_url_report"
      - table: "gender_performance_report"
      - table: "geo_performance_report"
      - table: "keywordless_query_report"
      - table: "keywords_performance_report"
      - table: "search_query_performance_report"
      - table: "video_performance_report"

  - id: "adgroup-id"
    attribute: "adGroupId"
    table: "ad_groups"
    all-foreign-keys:
      - table: "ad_groups"
        join-on: "id"
      - table: "ads"

  - id: "base-adgroup-id"
    attribute: "baseAdGroupId"
    table: "ad_groups"
    all-foreign-keys:
      - table: "ads"
      - table: "ad_groups"

  - id: "base-campaign-id"
    attribute: "baseCampaignId"
    table: "campaigns"
    all-foreign-keys:
      - table: "ads"
      - table: "ad_groups"
      - table: "campaigns"

  - id: "campaign-id"
    attribute: "campaignId"
    table: "campaigns"
    all-foreign-keys:
      - table: "ad_groups"
      - table: "campaigns"

  - id: "label-id"
    attribute: "id"
    table: ""
    all-foreign-keys:
      - table: "ad_groups"
        subtable: "labels"
      - table: "campaigns"
        subtable: "labels"
---