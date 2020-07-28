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

content-type: "api-form"
form-type: "source"
key: "source-form-properties-intercom-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Intercom Source Form Property"
api-type: "platform.intercom"
display-name: "Intercom"

source-type: "saas"
docs-name: "intercom" 

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
  - name: "access_token"
    type: "string"
    required: true
    description: "The token used to access your workspace's data via API."
    value: "YOU_API_ACCESS_TOKEN"
---