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
key: "source-form-properties-zoom-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Zoom Source Form Property"
api-type: "platform.zoom"
display-name: "Zoom"

source-type: "saas"
docs-name: "zoom" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "client_id"
    type: "string"
    required: false
    description: |
      Your {{ form-property.display-name }} client ID. Only use this if you plan to connect to Stitch using an OAuth app. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-tokens" }}) to retrieve this information.
    value: "<YOUR_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: false
    description: |
      Your {{ form-property.display-name }} client secret key. Only use this if you plan to connect to Stitch using an OAuth app. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-tokens" }}) to retrieve this information.
    value: "<YOUR_CLIENT_SECRET>"
    
  - name: "jwt"
    type: "string"
    required: false
    description: |
      Your {{ form-property.display-name }} JSON Web Token (JWT). Only use this if you plan to connect to Stitch using a JWT app. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-tokens" }}) to retrieve this information.
    value: "<YOUR_JWT>"
    
  - name: "refresh_token"
    type: string
    required: false
    description: |
      Your {{ form-property.display-name }} refresh token. Only use this if you plan to connect to Stitch using an OAuth app. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-tokens" }}) to retrieve this information.
    value: "<YOUR_REFRESH_TOKEN>"      
---