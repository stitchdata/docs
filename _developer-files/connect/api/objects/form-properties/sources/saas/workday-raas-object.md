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
key: "source-form-properties-workday-raas-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Workday RaaS Source Form Property"
api-type: "platform.workday-raas"
display-name: "Workday RaaS"

source-type: "saas"
docs-name: "workday-raas" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

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
  - name: "password"
    type: "string"
    required: true
    description: "Your password for your {{ form-property.display-name }} account."
    value: "<YOUR_PASSWORD>"

  - name: "reports"
    type: "string"
    required: true
    description: "Your report URL."
    value: "<YOUR_REPORT_URL>"
    
  - name: "username"
    type: "string"
    required: true
    description: "Your username for your {{ form-property.display-name }} account."
    value: "<YOUR_USERNAME>"    
---