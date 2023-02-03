---
tap: "tiktok-ads"
version: "1"
key: "ads"

name: "ads"
doc-link: https://ads.tiktok.com/marketing_api/docs?id=1708572923161602
singer-schema: https://github.com/singer-io/tap-tiktok-ads/tree/master/tap_tiktok_ads/schemas/ads.json
description: ""

replication-method: "Key-based Incremental"

table-key-properties: "advertiser_id, campaign_id, adgroup_id, ad_id, modify_time"
valid-replication-keys: "modify_time"

attributes:
  - name: "ad_format"
    type: string"
    description: "The creative type. Enum values: SINGLE_IMAGE, SINGLE_VIDEO, CAROUSEL."

  - name: "ad_id"
    type: integer"
    description: "Ad ID"
    primary-key: true

  - name: "ad_name"
    type: string"
    description: "Ad Name"

  - name: "ad_text"
    type: string"
    description: "The ad text. It is shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. Keyword match type is exact match."

  - name: "adgroup_id"
    type: integer"
    description: "Ad group ID"
    primary-key: true

  - name: "adgroup_name"
    type: string"
    description: "Ad group Name"

  - name: "advertiser_id"
    type: integer"
    description: "Advertiser ID"
    primary-key: true

  - name: "app_name"
    type: string"
    description: "The display name of app download ad"

  - name: "call_to_action"
    type: string"
    description: "For call-to-action text, see (Enumeration - Call-to-action)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929]"

  - name: "campaign_id"
    type: integer"
    description: "Campaign ID"
    primary-key: true

  - name: "campaign_name"
    type: string"
    description: "Campaign Name"

  - name: "card_id"
    type: integer"
    description: "Image card ID, gift code card ID, or premium badge ID"

  - name: "click_tracking_url"
    type: string"
    description: "Click monitoring URL."

  - name: "create_time"
    type: string"
    format: "date-time"
    description: "Time at which the ad was created."

  - name: "display_name"
    type: string"
    description: "The display name of landing page or pure exposure ad"

  - name: "dpa_fallback_type"
    type: string"
    description: "In DPA scenario, the fallback behavior of deeplink evokes failed. Return when the corresponding campaign objective_type is CATALOG_SALES."

  - name: "dpa_open_url_type"
    type: string"
    description: "Indicates the source of the direct link used in the ad. This field is returned when the corresponding campaign objective_type is CATALOG_SALES."

  - name: "dpa_video_tpl_id"
    type: string"
    description: "Catalog video template ID. Return when the corresponding campaign objective_type is CATALOG_SALES."

  - name: "fallback_type"
    type: string"
    description: "Fallback Type. If the audience do not have the app installed, you can have them fall back to install the app, or to view a specific web page. Not applicable for Deferred Deeplink. Allowed values: APP_INSTALL, WEBSITE, UNSET. If website is chosen, you need to specify the url via landing_page_url field."

  - name: "image_ids"
    type: array"
    description: "A list of image IDs"
    subattributes:
    - name: "items"
      type: string"
      description: "Image ID"

  - name: "image_mode"
    type: string"
    description: ""

  - name: "impression_tracking_url"
    type: string"
    description: "Display monitoring URL"

  - name: "is_aco"
    type: boolean"
    description: "Whether the ad is an automated ad. Set to true for automated ad and false for non-automated ad"

  - name: "is_creative_authorized"
    type: boolean"
    description: "Whether you grant displaying some of your ads in our TikTok For Business Creative Center. Only valid for non-US advertisers, the default value is false. Note: is_creative_authorized can only be used for video ads."

  - name: "is_new_structure"
    type: boolean"
    description: "Whether the campaign is a new structure (for the same campaign, the structure of campaign, adgroups and ads are the same)"

  - name: "item_duet_status"
    type: string"
    description: "Whether to enable dueting for the Spark Ad post. This field is valid only when promotional_music_disabled is set to false. Enum values: ENABLE, DISABLE. This field is only valid for Spark Ad posts."

  - name: "item_stitch_status"
    type: string"
    description: "Whether to enable stitching for the Spark Ad post. This field is valid only when promotional_music_disabled is set to false. Enum values: ENABLE, DISABLE. This field is only valid for Spark Ad posts."

  - name: "landing_page_url"
    type: string"
    description: "Landing page URL"

  - name: "landing_page_urls"
    type: string"
    description: "Multiple landing page URLs"

  - name: "modify_time"
    type: string"
    format: "date-time"
    description: "Time at which the ad was Modified."
	  replication-key: true
    primary-key: true

  - name: "open_url"
    type: string"
    description: "The specific location where you want your audience to go if they have your app installed. See open_url_type for more."

  - name: "open_url_type"
    type: string"
    description: "The open URL type. Allowed values differs based on campaign objectives. Allowed values: NORMAL(supported in Traffic, Conversion & CatalogSales), DEFERRED_DEEPLINK(supported in AppInstall & Catalog Sales)."

  - name: "opt_status"
    type: string"
    description: "Operation status, optional values include: DISABLE (the ad is disabled), ENABLE (the ad is enabled), FROZEN (the ad is terminated and cannot be enabled)"

  - name: "page_id"
    type: integer"
    description: "Instant Page (Instant Form, storefront page, tiktok instant page or app profile page) ID"

  - name: "playable_url"
    type: string"
    description: "Playable material url"

  - name: "profile_image"
    type: string"
    description: "Avatar URL"

  - name: "promotional_music_disabled"
    type: boolean"
    description: "Whether to disable the promotional use of the music in the Spark Ad post. The default value is true. If you want to allow dueting and stitching for the Spark Ad post, you need to set this field to false. This field is only valid for Spark Ad posts."

  - name: "status"
    type: string"
    description: "Ad status（Secondary status，See (Enumeration-Ad Status - Secondary Status)[https://ads.tiktok.com/marketing_api/docs?id=1701890985340929].
    Note: This field is not returned in the sandbox environment because the ad is not actually delivered."

  - name: "tiktok_item_id"
    type: string"
    description: "The ID of the TikTok post to be used as an ad. It can be obtained from Get Spark Ad post endpoint."

  - name: "vast_moat"
    type: boolean"
    description: "Whether Moat Viewability Verification is enabled for the ad. TikTok has partnered with Moat to launch viewability measurement for Brand Auction and Reach & Frequency In-feed ads purchased on TikTok for Business."

  - name: "video_id"
    type: string"
    description: "The video ID. When TikTok posts are used as ads, video_id is invalid. You can get the the ID of a TikTok post via the tiktok_item_id field"
---