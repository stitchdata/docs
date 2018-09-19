---
tap-reference: "bing-ads"

# version: "1.0"

foreign-keys:
  - id: "account-id"
    attribute: "accountId"
    table: "accounts"
    all-foreign-keys:
      - table: "accounts"
        join-on: "id"
      - table: "ad_performance_report"
      - table: "adgroup_performance_report"
      - table: "age_gender_performance_report"
      - table: "campaign_performance_report"
      - table: "geographic_performance_report"
      - table: "goals_and_funnels_report"
      - table: "keyword_performanc_report"
      - table: "search_query_performance_report"

  - id: "ad-id"
    attribute: "adId"
    table: "ads"
    all-foreign-keys:
      - table: "ads"
        join-on: "id"

  - id: "ad-group-id"
    attribute: "adGroupId"
    table: "ad_groups"
    all-foreign-keys:
      - table: "ad_groups"
        join-on: "id"
      - table: "ad_performance_report"
      - table: "adgroup_performance_report"
      - table: "age_gender_performance_report"
      - table: "campaign_performance_report"
      - table: "geographic_performance_report"
      - table: "goals_and_funnels_report"
      - table: "keyword_performanc_report"
      - table: "search_query_performance_report"

  - id: "campaign-id"
    attribute: "campaignId"
    table: "campaigns"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
---