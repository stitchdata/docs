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
docs-name: "twitter-ads" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "account_ids"
    type: "string"
    required: true
    description: |
      "Your {{ form-property.display-name }} account ID. If adding multiple IDs, the list must be comma-delimited. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-account-id" }}) to retrieve this information."
    value: "<YOUR_ACCOUNT_ID_1>,<YOUR_ACCOUNT_ID_2>"

  - name: "attribution_window"
    type: "string"
    required: false
    description: |
      The number of days of historical records to replicate for each replication job.
    value: "XX"
    
  - name: "country_codes"
    type: "string"
    required: false
    description: |
      The comma-delimited list of ISO 2-letter country codes for targeting and segmenttation.
    value: "US,MX,CA,DE"
    
  - name: "reports"
    type: "array"
    required: false
    description: |
      An array of objects, each object pertaining to a custom report you want to create.
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
        description: "The name of the custom report you want to create."
      - name: "entity"
        type: "string"
        required: false
        description: "The entity your custom report will source from."
      - name: "segment"
        type: "string"
        required: false
        description: "The specific segment within the entity that the report will replicate data from."
      - name: "granularity"
        type: "string"
        required: false
        description: "The level of detail you want in your custom report."
    
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
      Your {{ form-property.display-name }} OAuth application's consumer key. This is obtained when you create an OAuth app with Google.
    value: "<CONSUMER_KEY>"
    
  - name: "consumer_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's consumer secret. It is obtained when you create an OAuth app with Google.
    value: "<CONSUMER_SECRET>"    
---