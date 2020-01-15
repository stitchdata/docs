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
key: "source-form-properties-shippo-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Shippo Source Form Property"
api-type: "platform.shippo"
display-name: "Shippo"

source-type: "saas"
docs-name: "shippo"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api-creds" }}) for instructions on retrieving this credential.
    value: "<API_TOKEN>"
---