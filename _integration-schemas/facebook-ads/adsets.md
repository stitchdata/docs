---
tap: "facebook-ads"
version: 1.0

name: "adsets"
doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/adsets.json
description: |
  The `adsets` table contains info about the Ad Sets in your Facebook Ads account.

  **This is a Core Object table**.

  #### updated_time & Querying

  Because this table uses `updated_time` as part of the Primary Key, query results might return various versions of the same adgroup. 

  To reflect the latest state of the adgroup, use the latest `updated_time` timestamp.

  #### Deleted Adsets
  If the **Include data from deleted campaigns, ads, and adsets** box in the integration's settings is checked, this table will include data for deleted adsets.
  
replication-method: "Incremental"
attribution-window: true
api-method:
  name: adSet - Reading
  doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ID of the ad set."

  - name: "updated_time"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The last time the ad set was updated."

  - name: "name"
    type: "string"
    description: "The name of the ad set."

  - name: "end_time"
    type: "date-time"
    description: "The end time of the ad set."

  - name: "promoted_object"
    type: "object"
    description: "Details about the object an ad set promotes, such as a Page or app."
    doc-link: "https://developers.facebook.com/docs/marketing-api/reference/ad-promoted-object/"
    object-attributes:
      - name: "custom_event_type"
        type: "string"
        description: "The event from an App event of a mobile app or tag of a conversion pixel."

      - name: "pixel_id"
        type: "string"
        description: "The ID of a Facebook conversion pixel. Used with offsite conversion campaigns."

      - name: "pixel_rule"
        type: "string"
        description: "The rule of a Facebook conversion pixel."

      - name: "page_id"
        type: "string"
        description: "The ID of the Facebook page."

      - name: "object_store_url"
        type: "string"
        description: "The URL of the mobile or digital store where the application can be bought or downloaded."

      - name: "application_id"
        type: "string"
        description: "The ID of a Facebook application."

      - name: "product_set_id"
        type: "string"
        description: "The ID of a product set within an ad set-level product catalog."

      - name: "offer_id"
        type: "string"
        description: "The ID of an offer from a Facebook page."

  - name: "account_id"
    type: "string"
    description: "The ad account ID."

  - name: "daily_budget"
    type: "number"
    description: "The daily budget of the ad set."

  - name: "budget_remaining"
    type: "number"
    description: "The remaining budget of the ad set."

  - name: "effective_status"
    type: "string"
    description: |
      The effective status of the ad set. According to Facebook's documentation, possible values include:

      - `ACTIVE`
      - `PAUSED`
      - `DELETED`
      - `PENDING_REVIEW`
      - `DISAPPROVED`
      - `PREAPPROVED`
      - `PENDING_BILLING_INFO`
      - `CAMPAIGN_PAUSED`
      - `ARCHIVED`
      - `ADSET_PAUSED`

  - name: "campaign_id"
    type: "string"
    description: "The ID of the campaign containing this ad set."

  - name: "created_time"
    type: "date-time"
    description: "The time the ad set was created."

  - name: "start_time"
    type: "date-time"
    description: "The start time of the ad set."

  - name: "lifetime_budget"
    type: "number"
    description: "The lifetime budget of the ad set."

  - name: "targeting"
    type: ""
    description: |
      Targeting specs are ad set attributes that define who sees an ad.

      Stitch may create subtables named `adsets__targeting__[spec_name]` for each targeting spec type that is applied to the ad set. For example: `adsets__targeting__life_events`

      [Read more about the subtables that may be created here](#[ads/adsets]__targeting).

  - name: "bid_info"
    type: "object"
    description: "Details about the bid information for this ad set."
    object-attributes:
      - name: "clicks"
        type: "integer"
        description: "The clicks you placed on your bid."

      - name: "actions"
        type: "integer"
        description: "The actions you placed on your bid."

      - name: "reach"
        type: "integer"
        description: "The reach you placed on your bid."

      - name: "impressions"
        type: "integer"
        description: "The impressions you placed on your bid."

      - name: "social"
        type: "integer"
        description: "The social value you placed on your bid."

  - name: "adLabels"
    type: "array"
    description: "Details about the ad labels applied to the ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ad label ID."

      - name: "name"
        type: "string"
        description: "The name of the ad label."

      - name: "created_time"
        type: "date-time"
        description: "The time the ad label was created."

      - name: "updated_time"
        type: "date-time"
        description: "The time the ad label was last updated."
---