---
tap-reference: "facebook-ads"

foreign-keys:
  - id: "account-id"
    attribute: "account_id"
    all-foreign-keys:
      - table: "adcreative"
      - table: "ads"
      - table: "ads_insights"
      - table: "ads_insights_age_and_gender"
      - table: "ads_insights_country"
      - table: "ads_insights_platform_and_device"
      - table: "ads_insights_region"

  - id: "ad-label-id"
    attribute: "ad_label_id"
    all-foreign-keys:
      - table: "adcreative"
        subtable: "adLabels"
        join-on: "id"
      - table: "ads"
        join-on: "adLabels"
        join-on: "id"
      - table: "adsets"
        join-on: "adLabels"
        join-on: "id"

  - id: "adset-id"
    attribute: "adset_id"
    table: "adsets"
    join-on: "id"
    all-foreign-keys:
      - table: "ads"
      - table: "ads_insights"
      - table: "ads_insights"
      - table: "ads_insights_age_and_gender"
      - table: "ads_insights_country"
      - table: "ads_insights_platform_and_device"
      - table: "ads_insights_region"

  - id: "app-store-id"
    attribute: "app_store_id"
    all-foreign-keys:
      - table: "adcreative"
        subtable: "template_url_spec__ios"
      - table: "adcreative"
        subtable: "template_url_spec__ipad"
      - table: "adcreative"
        subtable: "template_url_spec__iphone"

  - id: "ad-id"
    attribute: "ad_id"
    table: "ads"
    join-on: "id"
    all-foreign-keys:
      - table: "ads"
        join-on: "id"
      - table: "ads_insights"
      - table: "ads_insights"
      - table: "ads_insights_age_and_gender"
      - table: "ads_insights_country"
      - table: "ads_insights_platform_and_device"
      - table: "ads_insights_region"
      - table: "campaigns"
        subtable: "ads"
        join-on: "id"

  - id: "campaign-id"
    attribute: "campaign_id"
    table: "campaigns"
    join-on: "id"
    all-foreign-keys:
      - table: "campaigns"
        join-on: "id"
      - table: "ads"
      - table: "ads_insights"
      - table: "ads_insights"
      - table: "ads_insights_age_and_gender"
      - table: "ads_insights_country"
      - table: "ads_insights_platform_and_device"
      - table: "ads_insights_region"

  - id: "ad-creative-id"
    attribute: "creative_id"
    table: "adcreative"
    join-on: "id"
    all-foreign-keys:
      - table: "adcreative"
        join-on: "id"
      - table: "ads"
        subattribute: "creative"
        join-on: "creative_id"

  - id: "offer-id"
    attribute: "offer_id"
    all-foreign-keys:
      - table: "adsets"
      - table: "adcreative"
        subtable: "object_story_spec__link_data"
      - table: "adcreative"
        subtable: "object_story_spec__template_data__child_attachments"
      - table: "adcreative"
        subtable: "object_story_spec__video_data"

  - id: "page-id"
    attribute: "page_id"
    all-foreign-keys:
      - table: "adsets"
      - table: "adcreative"
        subtable: "object_story_spec__link_data"

  - id: "pixel-id"
    attribute: "pixel_id"
    all-foreign-keys:
      - table: "adsets"

  - id: "product-set-id"
    attribute: "product_set_id"
    all-foreign-keys:
      - table: "adcreative"
      - table: "adsets"
        subattribute: "promoted_object"

  - id: "windows-app-id"
    attribute: "app_id"
    all-foreign-keys:
      - table: "adcreative"
        subtable: "template_url__spec__windows_phone"
---