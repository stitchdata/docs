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
key: "source-form-properties-ga360-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Analytics 360 Source Form Property"
api-type: "platform.ga360"
display-name: "Google Analytics 360"

source-type: "saas"
docs-name: "google-analytics-360" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "dataset_id"
    type: "string"
    required: true
    description: ""
    value: ""

  - name: "page_size"
    type: "string"
    required: false
    description: ""
    value: ""
    
  - name: "project_id"
    type: "string"
    required: true
    description: ""
    value: ""
    
  - name: "service_account_json"
    type: "string"
    required: false
    description: ""
    value: ""      
---