---
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
key: "source-form-properties-closeio-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Close.io Source Form Property"
api-type: "platform.closeio"
display-name: "Close.io"

source-type: "saas"
docs-name: "closeio"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display_name }} API key. API keys can be generated in {{ form-property.display_name }} by navigating to **Settings > Your API Keys**.
    value: "<API_KEY>"
---