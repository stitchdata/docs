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
key: "source-form-properties-pinterest-ads-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Pinterest Ads Source Form Property"
api-type: "platform.pinterest-ads"
display-name: "Pinterest Ads"

source-type: "saas"
docs-name: "" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "advertisers"
    type: "string"
    required: true
    description: |
      A comma-delimited list of the advertiser ID's in your {{ form-property.display-name }} you want to replicate data from."
    value: "<ADVERTISER_ID1>, <ADVERTISER_ID2>"

  - name: "attribution_window"
    type: "string"
    required: false
    description: |
      Defines the number, in days, Stitch should use as an attribution window. To ensure your {{ form-property.display-name }} and Stitch settings align, we recommend using the same attribution window in Stitch that you use in {{ form-property.display-name }}. This option is only available to suppport users. Please only change if you understand the impact.
    value: "30"
    
  - name: "date_window_size"
    type: "string"
    required: false
    description: |
      Defines the number, in days, for a date looping window. Date looping will return records whose `from_date` and `to_date` fall between the number of days in the defined window size. This option is only available to suppport users. Please only change if you understand the impact.
    value: "30"    


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.pinterest.com/docs/redoc/adsreporting/#section/User-Authorization/Start-the-OAuth-flow-(explicit-server-side)"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The {{ form-property.display-name }} token to use in future requests to the {{ form-property.display-name }} API, created after a successful OAuth handshake.
    value: "<YOUR_ACCESS_TOKEN>"    
---