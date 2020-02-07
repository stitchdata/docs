---
tap-reference: "bing-ads"

version: "2"

foreign-keys:
  - id: "account-id"
    attribute: "AccountId"
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
        join-on: "Id"
      - table: "ad_performance_report"
      - table: "adgroup_performance_report"
      - table: "age_gender_performance_report"
      - table: "campaign_performance_report"
      - table: "geographic_performance_report"
      - table: "goals_and_funnels_report"
      - table: "keyword_performance_report"
      - table: "search_query_performance_report"

  - id: "ad-id"
    attribute: "AdId"
    table: "ads"
    all-foreign-keys:
      - table: "ads"
        join-on: "Id"
      - table: "ad_performance_report"

  - id: "ad-group-id"
    attribute: "AdGroupId"
    table: "ad_groups"
    all-foreign-keys:
      - table: "ad_groups"
        join-on: "Id"
      - table: "ad_performance_report"
      - table: "adgroup_performance_report"
      - table: "age_gender_performance_report"
      - table: "campaign_performance_report"
      - table: "geographic_performance_report"
      - table: "goals_and_funnels_report"
      - table: "keyword_performance_report"
      - table: "search_query_performance_report"

  - id: "campaign-id"
    attribute: "CampaignId"
    table: "campaigns"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "Id"
      - table: "ad_performance_report"
      - table: "adgroup_performance_report"
      - table: "age_gender_performance_report"
      - table: "campaign_performance_report"
      - table: "geographic_performance_report"
      - table: "goals_and_funnels_report"
      - table: "keyword_performance_report"
      - table: "search_query_performance_report"
---