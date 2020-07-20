---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-twitter-ads-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Twitter Ads Source Form Property"
api-type: "platform.twitter-ads"
display-name: "Twitter Ads"

source-type: "saas"
docs-name: "twitter-ads"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "account_ids"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} account ID, or a comma-delimited list of account IDs. For example: `accountId1, accountId2`

      Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-account-id" }}) to retrieve this information.
    value: "<YOUR_ACCOUNT_ID_1>,<YOUR_ACCOUNT_ID_2>"

  - name: "attribution_window"
    type: "string"
    required: false
    description: |
      The number of days of historical records to replicate for custom report tables during each replication job.
    value: "14"
    
  - name: "country_codes"
    type: "string"
    required: false
    description: |
      A comma-delimited list of ISO 2-letter country codes for targeting and segmentation. **Note**: This value is required to use some segment types in custom reports. Refer to the [Segment compatibility reference]({{ doc-link | append: "#custom-report-configuration-options--segments" }}) for more info.
    value: "US,MX,CA,DE"
    
  - name: "reports"
    type: "array"
    required: false
    description: |
      An array of objects, each object pertaining to a custom report.

      **Note**: If provided, each property in this object must be provided to fully configure the custom report.
    value: |
      [
         {
              "name": "campaigns_genders_hourly_report",
              "enitity": "CAMPAIGN",
              "segment": "GENDER",
              "granularity": "HOUR"
           },
           {
              "name": "line_items_regions_daily_report",
              "enitity": "LINE_ITEM",
              "segment": "REGIONS",
              "granularity": "DAY"
           }
         ]  
    subattributes:
      - name: "name"
        type: "string"
        required: false
        description: "The name of the custom report."
      
      - name: "entity"
        type: "string"
        required: false
        description: |
          The {{ integration.display_name }} entity (object) to report on. The entity determines the metrics (fields) available for selection and the segments you can apply to those metrics. Refer to the [Custom report options compatibility reference]({{ doc-link | append: "#custom-report-configuration-options" }}) for more info.

          Accepted values are:

          {% assign source-documentation = site.saas-integrations | where:"key","twitter-ads-setup" | first %}
          {% assign source-reference = source-documentation.other-sections | where:"anchor","reference" | first %}
          {% assign custom-report-options = source-reference.custom-report-options %}

          {% for entity in custom-report-options.entities %}
          - `{{ entity.name | upcase }}`
          {% endfor %}
      
      - name: "segment"
        type: "string"
        required: false
        description: |
          The segment to apply to the `entity`'s available metrics. **Note**: Some entity and segment combinations may be incompatible. Refer to the [Segment compatibility reference]({{ doc-link | append: "#custom-report-configuration-options--segments" }}) for more info.

          Accepted values are:

          {% for segment in custom-report-options.segments %}
          - `{{ segment.name | upcase }}`
          {% endfor %}
      
      - name: "granularity"
        type: "string"
        required: false
        description: |
          The granularity of the custom report data. Accepted values are:

          - `DAY`
          - `HOUR`
          - `TOTAL`
    
  - name: "with_deleted"
    type: "string"
    required: false
    description: |
      Whether to include logically deleted records, that fall outside of the attribution window, in the results. This value will be `true` or `false`.

    

# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The access token of the {{ form-property.display-name }} account being connected to Stitch.
    value: "<ACCESS_TOKEN>"

  - name: "access_token_secret"
    type: "string"
    required: true
    credential: true
    description: |
      The token secret key of the {{ form-property.display-name }} account being connected to Stitch.
    value: "<ACCESS_TOKEN_SECRET>"

  - name: "consumer_key"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's consumer key. This is obtained when you create an OAuth app with Twitter.
    value: "<CONSUMER_KEY>"
    
  - name: "consumer_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's consumer secret. This is obtained when you create an OAuth app with Twitter.
    value: "<CONSUMER_SECRET>"    
---