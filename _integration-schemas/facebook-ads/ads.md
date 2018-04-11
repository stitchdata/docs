---
tap: "facebook-ads"
version: 1.0

name: "ads"
doc-link: https://developers.facebook.com/docs/reference/ads-api/adgroup/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/ads.json
description: |
  The `ads` table contains info about the ads in your Facebook Ads account.

  **This is a Core Object table**.

  #### updated_time & Querying
  Because this table uses `updated_time` as part of the Primary Key, query results might return various versions of the same adgroup.

  To reflect the latest state of the adgroup, use the latest `updated_time` timestamp.

  #### Deleted Ads
  If the **Include data from deleted campaigns, ads, and adsets** box in the integration's settings is checked, this table will include data for deleted ads.
  
replication-method: "Incremental"
attribution-window: true
api-method:
  name: ad - Reading
  doc-link: https://developers.facebook.com/docs/marketing-api/reference/adgroup

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ad ID."

  - name: "updated_time"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The last time the ad was updated."

  - name: "account_id"
    type: "string"
    description: "The ID of the ad account that the ad belongs to."

  - name: "campaign_id"
    type: "string"
    description: "The ID of the ad campaign that contains this ad."
    foreign-key: true

  - name: "adset_id"
    type: "string"
    description: "The ID of the ad set that contains this ad."
    foreign-key: true

  - name: "adLabels"
    type: "array"
    description: "Details about the ad labels applied to the ad."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ad label ID."

      - name: "created_time"
        type: "date-time"
        description: "The time the ad label was created."

      - name: "name"
        type: "string"
        description: "The name of the ad label."

      - name: "updated_time"
        type: "date-time"
        description: "The last time the ad label was updated."

  - name: "bid_type"
    type: "string"
    description: |
      The bid type of the ad. According to Facebook's documentation, possible values include:

      - `CPC`
      - `CPM`
      - `MULTI_PREMIUM`
      - `ABSOLUTE_OCPM`
      - `CPA`

  - name: "bid_amount"
    type: "integer"
    description: "The bid amount for the ad that will be used in auction instead of the ad set `bid_amount`, if specified."

  - name: "bid_info"
    type: "object"
    description: ""
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

  - name: "status"
    type: "string"
    description: |
      The configured status of the ad. Possible values include:

      - `ACTIVE`
      - `PAUSED`
      - `DELETED`
      - `ARCHIVED`

  - name: "creative"
    type: "object"
    description: "Details about the creative used by the ad."
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-creative/
    object-attributes:
      - name: "creative_id"
        type: "integer"
        description: "The ID of the creative used by the ad."
        foreign-key: true

      # - name: "id"
      #   type: "integer"
      #   primary-key: true
      #   description: ""

  - name: "created_time"
    type: "date-time"
    description: "The time the ad was created."

  - name: "name"
    type: "string"
    description: "The name of the ad."

  - name: "effective_status"
    type: "string"
    description: |
      The effective status of the ad. According to Facebook's documentation, possible values include:

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

  - name: "targeting"
    type: "object"
    description: "Details about the targeting specs applied to the ad."
    object-attributes:
      - name: "age_max"
        type: "string"
        description: "The maximum age of the targeted audience."

      - name: "age_min"
        type: "integer"
        description: "The minimum age of the targeted audience."

      - name: "app_install_state"
        type: "string"
        description: "The app install state of the targeted audience."

  - name: "targeting"
    type: ""
    description: |
      Targeting specs are ad set attributes that define who sees an ad.

      Stitch may create subtables named `ads__targeting__[spec_name]` for each targeting spec type that is applied to the ad set. For example: `ads__targeting__life_events`

      [Read more about the subtables that may be created here](#[ads/adsets]__targeting).

  - name: "last_updated_by_app_id"
    type: "string"
    description: "The ID of the app that last updated the ad."

  - name: "recommendations"
    type: "array"
    description: "Details about the recommendations for the ad, if there are any."
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation/
    array-attributes:
      - name: "code"
        type: "integer"
        primary-key: true
        description: "The recommendation code."

      - name: "blame_field"
        type: "string"
        description: "Field to associate the recommendation with."

      - name: "confidence"
        type: "string"
        description: "Indicates how reliable the recommendation is. Possible values are `HIGH`, `MEDIUM`, and `LOW`."

      - name: "importance"
        type: "string"
        description: "Indicates how important the recommendation is. Possible values are `HIGH`, `MEDIUM`, and `LOW`."

      - name: "message"
        type: "string"
        description: "The content of the recommendation message."

      - name: "title"
        type: "string"
        description: "The title of the recommendation."

  - name: "tracking_specs"
    type: "array"
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/conversion-action-query/
    description: |
      Tracking specs are actions taken by people interacting with the ad. **Note**: tracking specs only **track** - they don't optimize or charge based on that action occurring.

      Stitch may create subtables named named `ads__tracking_specs__[spec_type]` for any tracking spec type applied to the ad. Subtables are created for any tracking spec type.

      If you have applied many tracking specs to your ads, this will result in a large number of subtables in your data warehouse. [Refer to Facebook's documentation for a full list of tracking specs](https://developers.facebook.com/docs/marketing-api/reference/conversion-action-query/).

      Subtables created for tracking specs will, in general, have the following schema:
    array-attributes:
      - name: |
          {{ system-column.level-id | replace: "#", "1" }}
        type: "integer"
        primary-key: true
        description: |
          This column functions the same as the `{{ system-column.level-id | replace: "#", "0" }}` column.

      - name: "value"
        type: "string"
        description: "The value for the tracking spec."

  - name: "conversion_specs"
    type: "array"
    description: |
      Conversion specs allow Facebook to surface the ad to users most likely to perform a desired decision. For example: adding to a shopping cart, viewing a particular page, or completing a form.
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/conversion-action-query/
    array-attributes:
      - name: |
          {{ system-column.level-id | replace: "#", "1" }}
        type: "integer"
        primary-key: true
        description: |
          This column functions the same as the `{{ system-column.level-id | replace: "#", "0" }}` column.

      - name: "value"
        type: "string"
        description: |
          Depending on the conversion specs you've applied to the ad, if any, Stitch may create subtables for each spec type. Subtables that are created will be named `ads__conversion_specs__[spec_type]`

          Aside from the columns listed in this subtable (`_sdc_level_0_id`, `_sdc_source_key_id`, etc), these tables will contain a field named `value`.

          Stitch will create a subtable for any conversion spec type. If you have applied many conversion specs, this will result in a large number of subtables in your data warehouse.

          [Refer to Facebook's documentation for a full list of conversion specs](https://developers.facebook.com/docs/marketing-api/reference/conversion-action-query/).
---