---
tap: "facebook-ads"
version: "1"

name: "ads"
doc-link: https://developers.facebook.com/docs/reference/ads-api/adgroup/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/ads.json
description: |
  The `ads` table contains info about the ads in your Facebook Ads account.

  **This is a Core Object table**.

  #### updated_time and querying

  Because this table uses `updated_time` as part of the Primary Key, query results might return various versions of the same adgroup.

  To reflect the latest state of the adgroup, use the latest `updated_time` timestamp.

  #### Deleted ads

  If the **Include data from deleted campaigns, ads, and adsets** box in the integration's settings is checked, this table will include data for deleted ads.
  
replication-method: "Key-based Incremental"
attribution-window: true
api-method:
  name: ad - Reading
  doc-link: https://developers.facebook.com/docs/marketing-api/reference/adgroup

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The ad ID."
    foreign-key-id: "ad-id"

  - name: "updated_time"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: "The last time the ad was updated."

  - name: "account_id"
    type: "string"
    description: "The ID of the ad account that the ad belongs to."
    foreign-key-id: "account-id"

  - name: "campaign_id"
    type: "string"
    description: "The ID of the ad campaign that contains this ad."
    foreign-key-id: "campaign-id"

  - name: "adset_id"
    type: "string"
    description: "The ID of the ad set that contains this ad."
    foreign-key-id: "adset_id"

  - name: "adLabels"
    type: "array"
    description: "Details about the ad labels applied to the ad."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ad label ID."
        foreign-key-id: "ad-label-id"

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
    subattributes:
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
    subattributes:
      - name: "creative_id"
        type: "integer"
        description: "The ID of the creative used by the ad."
        foreign-key-id: "adcreative-id"

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
    subattributes:
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
    type: "array"
    description: |
      Targeting specs are ad set attributes that define who sees an ad.

      Stitch may create subtables named `ads__targeting__[spec_name]` for each targeting spec type that is applied to the ad set. For example: `ads__targeting__life_events`

      If you have many targeting specs applied to ads, a large number of subtables may be created in your destination.

    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ad ID."
        foreign-key-id: "ad-id"

      - name: "updated_time"
        type: "date-time"
        primary-key: true
        replication-key: true
        description: "The time the ad was last updated."

      - name: "behaviors"
        type: "array"
        description: "ID/name pairs of the behavior targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the behavior."

          - name: "name"
            type: "string"
            description: "The name of the behavior. Ex: `All travelers`"

      - name: "connections"
        type: "array"
        description: "ID/name pairs of the connection targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the connection. Ex: fans of your Page."

          - name: "name"
            type: "string"
            description: "The name of the connection. Ex: Stitch Data"

      - name: "custom_audiences"
        type: "array"
        description: "ID/name pairs of the custom audience targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the audience."

          - name: "name"
            type: "string"
            description: "The name of the audience. Ex: `Outbound Email Leads`"

      - name: "education_majors"
        type: "array"
        description: "ID/name pairs of the education major targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the education major."

          - name: "name"
            type: "string"
            description: "The name of the education major. Ex: `Computer Science`"

      - name: "excluded_connections"
        type: "array"
        description: "ID/name pairs of the excluded connection targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the excluded connection. Ex: Target people who aren't fans of your Page."

          - name: "name"
            type: "string"
            description: "The name of the excluded connection. Ex: Stitch Data"

      - name: "excluded_custom_audiences"
        type: "array"
        description: "ID/name pairs of the excluded custom audience targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the excluded custom audience."

          - name: "name"
            type: "string"
            description: "The name of the excluded custom audience."


      # Need to figure out how to display these two things. These arrays can contain 
      # any of the other array fields (ex: education_majors) and create MORE
      # subtables.

      # - name: "exclusions"
      #   type: "array"
      #   description: ""
      #   subattributes:
      #     - name: "id"
      #       type: "string"
      #       primary-key: true
      #       description: "The ID of the "

      #     - name: "name"
      #       type: "string"
      #       description: "The name of the "

      # - name: "flexible_spec"
      #   type: "array"
      #   description: ""
      #   subattributes:
      #     - name: "id"
      #       type: "string"
      #       primary-key: true
      #       description: "The ID of the "

      #     - name: "name"
      #       type: "string"
      #       description: "The name of the "

      - name: "family_statuses"
        type: "array"
        description: "ID/name pairs of the family status targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the family status."

          - name: "name"
            type: "string"
            description: "The name of the family status."

      - name: "friends_of_connections"
        type: "array"
        description: "ID/name pairs of the friend of connections targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the friend connection. Ex: Friends of people who are fans of your Page"

          - name: "name"
            type: "string"
            description: "The name of the friend connection."

      - name: "generation"
        type: "array"
        description: "ID/name pairs of the generation demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the generation demographic."

          - name: "name"
            type: "string"
            description: "The name of the generation demographic."

      - name: "geo_locations__cities"
        type: "array"
        description: "Details about the city demographic targeting specs applied to the ad."
        subattributes:
          - name: "key"
            type: "string"
            description: "The city's key."

          - name: "distance_unit"
            type: "string"
            description: "The unit used to measure `radius`."

          - name: "region"
            type: "string"
            description: "The region associated with the city."

          - name: "name"
            type: "string"
            description: "The name of the city."

          - name: "country"
            type: "string"
            description: "The country associated with the city."

          - name: "region_id"
            type: "string"
            description: "The ID of the region associated with the city."

          - name: "radius"
            type: "integer"
            description: "The radius around the city that is included in the targeting. For example: if `radius` is `10` and `distance_unit` is `mile`, an area of `10 miles` outside the given city will be targeted."

      - name: "geo_locations__location_types"
        type: "array"
        description: "Details about the location types included in the targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: |
              The type of location included in the targeting specs. Possible values are:

              - `country`
              - `country_group`
              - `region`
              - `city`
              - `zip`
              - `geo_market`
              - `electoral_district` - Only applicable in the United States.

      - name: "geo_locations__regions"
        type: "array"
        description: "Details about the region demographics included in the targeting specs applied to the ad."
        subattributes:
          - name: "name"
            type: "string"
            description: "The name of the region."

          - name: "country"
            type: "string"
            description: "The name of the country associated with the region."

          - name: "key"
            type: "string"
            description: "The key of the region."

      - name: "geo_locations__zips"
        type: "array"
        description: "Details about zip codes included in the targeting specs applied to the ad."
        subattributes:
          - name: "name"
            type: "string"
            description: "The name of the zip code. For example: `90210`"

          - name: "country"
            type: "string"
            description: "The country associated with the zip code. For example: `US`"

          - name: "key"
            type: "string"
            description: "The key of the zip code. For example: `US:90210`"

          - name: "primary_city_id"
            type: "string"
            description: "The ID of the city associated with the zip code. For example: `Beverly Hills`"

          - name: "region_id"
            type: "string"
            description: "The region associated with the zip code. For example: `California`"

      - name: "geo_locations__geo-markets"
        type: "array"
        description: "Details about the geo market demographics included in the targeting specs applied to the ad."
        subattributes:
          - name: "key"
            type: "string"
            description: "The key of the geo market."

          - name: "name"
            type: "string"
            description: "The name of the geo market."

      - name: "home_ownership"
        type: "array"
        description: "ID/name pairs of the home ownership demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the home ownership demographic."

          - name: "name"
            type: "string"
            description: "The name of the home ownership demographic."

      - name: "home_type"
        type: "array"
        description: "ID/name pairs of the home type demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the home type demographic."

          - name: "name"
            type: "string"
            description: "The name of the home type demographic."

      - name: "household_composition"
        type: "array"
        description: "ID/name pairs of the home composition targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the household composition type."

          - name: "name"
            type: "string"
            description: "The name of the household composition type. Ex: `Children in home`"

      - name: "income"
        type: "array"
        description: "ID/name pairs of the income demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the income demographic."

          - name: "name"
            type: "string"
            description: "The name of the income demographic."

      - name: "industries"
        type: "array"
        description: "ID/name pairs of the industry targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the industry type."

          - name: "name"
            type: "string"
            description: "The name of the industry type."

      - name: "interests"
        type: "array"
        description: "ID/name pairs of the interest targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the interest."

          - name: "name"
            type: "string"
            description: "The name of the interest. Ex: `Movies`, `Music`"

      - name: "life_events"
        type: "array"
        description: "ID/name pairs of the life event targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the life event."

          - name: "name"
            type: "string"
            description: "The name of the life event. Ex: `Recently moved`"

      - name: "moms"
        type: "array"
        description: "ID/name pairs of the mother demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the mom demographic."

          - name: "name"
            type: "string"
            description: "The name of the mom demographic."

      - name: "net_worth"
        type: "array"
        description: "ID/name pairs of the net worth demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the net worth demographic."

          - name: "name"
            type: "string"
            description: "The name of the net worth demographic."

      - name: "office_type"
        type: "array"
        description: "ID/name pairs of the office type targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the office type."

          - name: "name"
            type: "string"
            description: "The name of the office type."

      - name: "politics"
        type: "array"
        description: "ID/name pairs of the political demographic targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the political demographic."

          - name: "name"
            type: "string"
            description: "The name of the political demographic."

      - name: "user_adclusters"
        type: "array"
        description: "ID/name pairs of the user adcluster targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the user adcluster."

          - name: "name"
            type: "string"
            description: "The name of the user adcluster. Ex: `Cooking`, `Small Business Owners`"

      - name: "work_employers"
        type: "array"
        description: "ID/name pairs of the work employer targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the work employer."

          - name: "name"
            type: "string"
            description: "The name of the work employer. Ex: `Microsoft`"

      - name: "work_positions"
        type: "array"
        description: "ID/name pairs of the work position targeting specs applied to the ad."
        subattributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The ID of the work position."

          - name: "name"
            type: "string"
            description: "The name of the work position. Ex: `Contractor`"

    # Just value fields start here

      - name: "locales"
        type: "array"
        description: "The locale targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The locale to be targeted. Ex: `en`"

      - name: "geo_locations__countries"
        type: "array"
        description: "Details about the country demographic targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The country to be targeted."

      - name: "geo_locations__country_groups"
        type: "array"
        description: "The country group targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The country group code."

      - name: "messenger_positions"
        type: "array"
        description: "The Messenger position targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The Messenger position to be targeted. Ex: `sponsored_messages`"

      - name: "instagram_positions"
        type: "array"
        description: "The Instagram position targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The Instagram position to be targeted. Ex: `stream`, `story`"

      - name: "audience_network_positions"
        type: "array"
        description: "Audience network position targeting specs applied to the ad. Facebook's Audience Network feature allows the serving of ads on other publishers' iOS and Android apps and mobile websites."
        doc-link: https://developers.facebook.com/docs/marketing-api/audience-network
        subattributes:
          - name: "value"
            type: "string"
            description: "The audience network position to be targeted. Ex: `instream_video`"

      - name: "education_statuses"
        type: "array"
        description: "Education status targeting specs applied to the ad."
        doc-link: https://developers.facebook.com/docs/marketing-api/targeting-specs/education_and_workplace
        subattributes:
          - name: "value"
            type: "string"
            description: |
              The education level to be targeted. Facebook uses integers to represent each education level. For example:

              - `1` = `HIGH_SCHOOL`
              - `2` = `UNDERGRAD`

              [Refer to Facebook's documentation for the full list](https://developers.facebook.com/docs/marketing-api/targeting-specs/education_and_workplace).

      - name: "publisher_platforms"
        type: "array"
        description: "Publisher platform targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The publisher platform to be targeted. Ex: `facebook`"

      - name: "device_platforms"
        type: "array"
        description: "Device platform targeting specs applied to the ad. This is the type of device (`mobile`, `desktop`) someone who views your ad has."
        subattributes:
          - name: "value"
            type: "string"
            description: "The device platform to be targeted."

      - name: "facebook_positions"
        type: "array"
        description: "Facebook position targeting specs applied to the ad. The position is the location on Facebook where the ad is served. Ex: in the newsfeed or a suggested video."
        subattributes:
          - name: "value"
            type: "string"
            description: "The Facebook position to be targeted. Ex: `feed`"

      - name: "user_os"
        type: "array"
        description: "User operating system targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The user operating system to be targeted."

      - name: "user_device"
        type: "array"
        description: "User device targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The user device to be targeted."

      - name: "excluded_publisher_categories"
        type: "array"
        description: "Excluded publisher category targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The publisher category to be excluded."

      - name: "targeting_optimization"
        type: "array"
        description: "The targeting optimization specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The targeting optimization spec."

      - name: "relationship_statuses"
        type: "array"
        description: "Relationship status targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The relationship status to be targeted."

      - name: "interested_in"
        type: "array"
        description: "The targeting specs applied to the ad regarding topics users are interested in."
        subattributes:
          - name: "value"
            type: "string"
            description: "The topic to be targeted."

      - name: "excluded_user_device"
        type: "array"
        description: "Excluded user device targeting specs applied to the ad."
        subattributes:
          - name: "value"
            type: "string"
            description: "The device to be excluded."

  - name: "last_updated_by_app_id"
    type: "string"
    description: "The ID of the app that last updated the ad."

  - name: "recommendations"
    type: "array"
    description: "Details about the recommendations for the ad, if there are any."
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/ad-recommendation/
    subattributes:
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
    subattributes:
      - name: "value"
        type: "string"
        description: "The value for the tracking spec."

  - name: "conversion_specs"
    type: "array"
    description: |
      Conversion specs allow Facebook to surface the ad to users most likely to perform a desired decision. For example: adding to a shopping cart, viewing a particular page, or completing a form.
    doc-link: https://developers.facebook.com/docs/marketing-api/reference/conversion-action-query/
    subattributes:
      - name: "value"
        type: "string"
        description: |
          The conversion spec.
---