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
key: "source-form-properties-iterable-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Iterable Source Form Property"
api-type: "platform.iterable"
display-name: "Iterable"

source-type: "saas"
docs-name: "iterable-core" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

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
  - name: "api_key"
    type: "string"
    required: true
    description: "The {{ form-property.display-name }} API key."
    value: "<API_KEY>"

  - name: "api_window_in_days"
    type: "integer"
    required: false
    description: "The API window, in days."
    value: "X"  
---