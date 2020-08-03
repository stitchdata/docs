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
key: "source-form-properties-autopilot-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Autopilot Source Form Property"
api-type: "platform.autopilot"
display-name: "Autopilot"

source-type: "saas"
docs-name: "autopilot"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      An API key for the {{ form-property.display-name }} account that Stitch should replicate data from.
    value: "<API_KEY>"
---