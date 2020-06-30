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
key: "source-form-properties-lever-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Lever Source Form Property"
api-type: "platform.lever"
display-name: "Lever"

source-type: "saas"
docs-name: "lever" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-api-token" }}) for instructions on obtaining this.
    value: "<YOUR_API_TOKEN>"
---