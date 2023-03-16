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
key: "source-form-properties-dixa-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Dixa Source Form Property"
api-type: "platform.dixa"
display-name: "Dixa"

source-type: "saas"
docs-name: "dixa"

property-description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display_name }} API token.
    value: "<API_TOKEN>"
---