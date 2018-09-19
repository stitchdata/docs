---
tap: "facebook-ads"
version: "1.0"

name: "[ads/adsets]__targeting"
description: |
  {{ site.data.alerts.note }} <strong>This is not a table that will display in the Stitch app for replication</strong>. The information outlined here is only applicable if you:

  <ol>
  <li>Are tracking the <code>targeting</code> column in either the <code>ads</code> or <code>adsets</code> tables,</li>
  <li>Have applied targeting specs to any of your Facebook ad sets, <strong>and</strong></li>
  <li>Use a data warehouse that doesn't support nested structures.</li>
  </ol>
  
  <p>If all of the above are true, Stitch may create a large number of subtables in your data warehouse.</p>
  {{ site.data.alerts.end }}

  For every applicable targeting spec, a subtable will be created.

  Below are the targeting specs Stitch will create subtables for and the attributes each subtable can contain.

replication-method: "Key-based Incremental"
attribution-window: true

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: |
      If the table name begins with `ads`, this column will contain the ad ID.

      If the table name begins with `adsets`, this column will contain the ad set ID.

  - name: "updated_time"
    type: "date-time"
    primary-key: true
    replication-key: true
    description: |
      If the table name begins with `ads`, this column contain the time the ad was last updated.

      If the table name begins with `adsets`, this column contain the time the ad set was last updated.

  - name: "behaviors"
    type: "array"
    description: "ID/name pairs of the behavior targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the behavior."

      - name: "name"
        type: "string"
        description: "The name of the behavior. Ex: `All travelers`"

  - name: "connections"
    type: "array"
    description: "ID/name pairs of the connection targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the connection. Ex: fans of your Page."

      - name: "name"
        type: "string"
        description: "The name of the connection. Ex: Stitch Data"

  - name: "custom_audiences"
    type: "array"
    description: "ID/name pairs of the custom audience targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the audience."

      - name: "name"
        type: "string"
        description: "The name of the audience. Ex: `Outbound Email Leads`"

  - name: "education_majors"
    type: "array"
    description: "ID/name pairs of the education major targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the education major."

      - name: "name"
        type: "string"
        description: "The name of the education major. Ex: `Computer Science`"

  - name: "excluded_connections"
    type: "array"
    description: "ID/name pairs of the excluded connection targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the excluded connection. Ex: Target people who aren't fans of your Page."

      - name: "name"
        type: "string"
        description: "The name of the excluded connection. Ex: Stitch Data"

  - name: "excluded_custom_audiences"
    type: "array"
    description: "ID/name pairs of the excluded custom audience targeting specs applied to the ad/ad set."
    array-attributes:
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
  #   array-attributes:
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
  #   array-attributes:
  #     - name: "id"
  #       type: "string"
  #       primary-key: true
  #       description: "The ID of the "

  #     - name: "name"
  #       type: "string"
  #       description: "The name of the "

  - name: "family_statuses"
    type: "array"
    description: "ID/name pairs of the family status targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the family status."

      - name: "name"
        type: "string"
        description: "The name of the family status."

  - name: "friends_of_connections"
    type: "array"
    description: "ID/name pairs of the friend of connections targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the friend connection. Ex: Friends of people who are fans of your Page"

      - name: "name"
        type: "string"
        description: "The name of the friend connection."

  - name: "generation"
    type: "array"
    description: "ID/name pairs of the generation demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the generation demographic."

      - name: "name"
        type: "string"
        description: "The name of the generation demographic."

  - name: "geo_locations__cities"
    type: "array"
    description: "Details about the city demographic targeting specs applied to the ad/ad set."
    array-attributes:
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
    description: "Details about the location types included in the targeting specs applied to the ad/ad set."
    array-attributes:
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
    description: "Details about the region demographics included in the targeting specs applied to the ad/ad set."
    array-attributes:
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
    description: "Details about zip codes included in the targeting specs applied to the ad/ad set."
    array-attributes:
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
    description: "Details about the geo market demographics included in the targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "key"
        type: "string"
        description: "The key of the geo market."

      - name: "name"
        type: "string"
        description: "The name of the geo market."

  - name: "home_ownership"
    type: "array"
    description: "ID/name pairs of the home ownership demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the home ownership demographic."

      - name: "name"
        type: "string"
        description: "The name of the home ownership demographic."

  - name: "home_type"
    type: "array"
    description: "ID/name pairs of the home type demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the home type demographic."

      - name: "name"
        type: "string"
        description: "The name of the home type demographic."

  - name: "household_composition"
    type: "array"
    description: "ID/name pairs of the home composition targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the household composition type."

      - name: "name"
        type: "string"
        description: "The name of the household composition type. Ex: `Children in home`"

  - name: "income"
    type: "array"
    description: "ID/name pairs of the income demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the income demographic."

      - name: "name"
        type: "string"
        description: "The name of the income demographic."

  - name: "industries"
    type: "array"
    description: "ID/name pairs of the industry targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the industry type."

      - name: "name"
        type: "string"
        description: "The name of the industry type."

  - name: "interests"
    type: "array"
    description: "ID/name pairs of the interest targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the interest."

      - name: "name"
        type: "string"
        description: "The name of the interest. Ex: `Movies`, `Music`"

  - name: "life_events"
    type: "array"
    description: "ID/name pairs of the life event targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the life event."

      - name: "name"
        type: "string"
        description: "The name of the life event. Ex: `Recently moved`"

  - name: "moms"
    type: "array"
    description: "ID/name pairs of the mother demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the mom demographic."

      - name: "name"
        type: "string"
        description: "The name of the mom demographic."

  - name: "net_worth"
    type: "array"
    description: "ID/name pairs of the net worth demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the net worth demographic."

      - name: "name"
        type: "string"
        description: "The name of the net worth demographic."

  - name: "office_type"
    type: "array"
    description: "ID/name pairs of the office type targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the office type."

      - name: "name"
        type: "string"
        description: "The name of the office type."

  - name: "politics"
    type: "array"
    description: "ID/name pairs of the political demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the political demographic."

      - name: "name"
        type: "string"
        description: "The name of the political demographic."

  - name: "user_adclusters"
    type: "array"
    description: "ID/name pairs of the user adcluster targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the user adcluster."

      - name: "name"
        type: "string"
        description: "The name of the user adcluster. Ex: `Cooking`, `Small Business Owners`"

  - name: "work_employers"
    type: "array"
    description: "ID/name pairs of the work employer targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The ID of the work employer."

      - name: "name"
        type: "string"
        description: "The name of the work employer. Ex: `Microsoft`"

  - name: "work_positions"
    type: "array"
    description: "ID/name pairs of the work position targeting specs applied to the ad/ad set."
    array-attributes:
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
    description: "The locale targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The locale to be targeted. Ex: `en`"

  - name: "geo_locations__countries"
    type: "array"
    description: "Details about the country demographic targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The country to be targeted."

  - name: "geo_locations__country_groups"
    type: "array"
    description: "The country group targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The country group code."

  - name: "messenger_positions"
    type: "array"
    description: "The Messenger position targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The Messenger position to be targeted. Ex: `sponsored_messages`"

  - name: "instagram_positions"
    type: "array"
    description: "The Instagram position targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The Instagram position to be targeted. Ex: `stream`, `story`"

  - name: "audience_network_positions"
    type: "array"
    description: "Audience network position targeting specs applied to the ad/ad set. Facebook's Audience Network feature allows the serving of ads on other publishers' iOS and Android apps and mobile websites."
    doc-link: https://developers.facebook.com/docs/marketing-api/audience-network
    array-attributes:
      - name: "value"
        type: "string"
        description: "The audience network position to be targeted. Ex: `instream_video`"

  - name: "education_statuses"
    type: "array"
    description: "Education status targeting specs applied to the ad/ad set."
    doc-link: https://developers.facebook.com/docs/marketing-api/targeting-specs/education_and_workplace
    array-attributes:
      - name: "value"
        type: "string"
        description: |
          The education level to be targeted. Facebook uses integers to represent each education level. For example:

          - `1` = `HIGH_SCHOOL`
          - `2` = `UNDERGRAD`

          [Refer to Facebook's documentation for the full list](https://developers.facebook.com/docs/marketing-api/targeting-specs/education_and_workplace).

  - name: "publisher_platforms"
    type: "array"
    description: "Publisher platform targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The publisher platform to be targeted. Ex: `facebook`"

  - name: "device_platforms"
    type: "array"
    description: "Device platform targeting specs applied to the ad/ad set. This is the type of device (`mobile`, `desktop`) someone who views your ad has."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The device platform to be targeted."

  - name: "facebook_positions"
    type: "array"
    description: "Facebook position targeting specs applied to the ad/ad set. The position is the location on Facebook where the ad is served. Ex: in the newsfeed or a suggested video."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The Facebook position to be targeted. Ex: `feed`"

  - name: "user_os"
    type: "array"
    description: "User operating system targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The user operating system to be targeted."

  - name: "user_device"
    type: "array"
    description: "User device targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The user device to be targeted."

  - name: "excluded_publisher_categories"
    type: "array"
    description: "Excluded publisher category targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The publisher category to be excluded."

  - name: "targeting_optimization"
    type: "array"
    description: "The targeting optimization specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The targeting optimization spec."

  - name: "relationship_statuses"
    type: "array"
    description: "Relationship status targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The relationship status to be targeted."

  - name: "interested_in"
    type: "array"
    description: "The targeting specs applied to the ad/ad set regarding topics users are interested in."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The topic to be targeted."

  - name: "excluded_user_device"
    type: "array"
    description: "Excluded user device targeting specs applied to the ad/ad set."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The device to be excluded."
---