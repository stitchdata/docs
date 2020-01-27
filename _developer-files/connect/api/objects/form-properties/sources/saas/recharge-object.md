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
key: "source-form-properties-recharge-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "ReCharge Source Form Property"
api-type: "platform.recharge"
display-name: "ReCharge"

source-type: "saas"
docs-name: "recharge" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

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
    description: "Your {{ form-property.display-name }} access token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on obtaining this credential."
    value: "<{{ form-property.display-name | upcase }}_SECRET_KEY>"
---